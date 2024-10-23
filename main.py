# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from dotenv import load_dotenv

from smartlib.controllers import TaskController
from smartlib.models import TaskDatabase
from smartlib.views import TaskView

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class TaskStates(StatesGroup):
    title = State()


class TaskEditStates(StatesGroup):
    title = State()


class TelegramBot:

    def __init__(self, token):
        self.db = TaskDatabase()
        self.controller = TaskController(self.db)
        self.view = TaskView(self.controller)
        self.bot = Bot(
            token=token,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML
            )
        )
        self.dp = Dispatcher()
        self.dp.message(Command("start"))(self.cmd_start)
        self.dp.callback_query()(self.callback_handler)
        self.dp.message(TaskStates.title)(self.process_task_title)
        self.dp.message(TaskEditStates.title)(self.process_edit_task_title)

    async def callback_handler(self, callback_query: types.CallbackQuery, state: FSMContext) -> None:
        if callback_query.data.startswith("task_"):
            task_index = int(callback_query.data.split("_")[1]) - 1
            tasks = self.controller.get_all_tasks(callback_query.from_user.id)
            if 0 <= task_index < len(tasks):
                task = tasks[task_index]
                await self.show_task_details(callback_query.message, task)
        elif callback_query.data.startswith("edit_task_"):
            task_id = int(callback_query.data.split("_")[2])
            await self.edit_task(callback_query.message, task_id, state)
        elif callback_query.data.startswith("complete_task_"):
            task_id = int(callback_query.data.split("_")[2])
            await self.complete_task(callback_query.message, task_id, callback_query.from_user)
        elif callback_query.data.startswith("delete_task_"):
            task_id = int(callback_query.data.split("_")[2])
            await self.delete_task(callback_query.message, task_id, callback_query.from_user)
        elif callback_query.data == "show_tasks":
            await self.show_tasks(callback_query.message, user=callback_query.from_user)
        elif callback_query.data == "back_to_start":
            await self.cmd_start(callback_query.message, user=callback_query.from_user)
        elif callback_query.data == "add_task":
            await self.add_task(callback_query.message, user=callback_query.from_user, state=state)
        elif callback_query.data.startswith("toggle_task_"):
            task_id = int(callback_query.data.split("_")[2])
            await self.toggle_task(callback_query.message, task_id, callback_query.from_user)

    async def cmd_start(self, message: types.Message, user: types.User = None) -> None:
        if user is None:
            user = message.from_user

        self.controller.create_user(
            user_id=user.id,
            full_name=user.full_name or 'Anonim',
        )

        await self.view.show_welcome(message, user)

    async def show_task_details(self, message: types.Message, task) -> None:
        await self.view.show_task_details(message, task)

    async def add_task(self, message: types.Message, user: types.User = None, state: FSMContext = None) -> None:
        if user is None:
            user = message.from_user

        await state.set_state(TaskStates.title)
        await message.answer(f"{user.full_name} enter the name of your task: ")

    async def process_task_title(self, message: types.Message, state: FSMContext) -> None:
        task_title = message.text
        if len(task_title) > 50:
            await message.answer("⚠️ The name is too long. Please enter a name no longer than 50 characters:")
            return
        self.controller.create_task(message.from_user.id, task_title)
        await message.answer(f"Task '{task_title}' added!")
        await state.clear()
        await self.cmd_start(message)

    async def show_tasks(self, message: Message, user: types.User = None) -> None:
        await self.view.show_tasks(message, user)

    async def toggle_task(self, message: types.Message, task_id: int, user: types.User) -> None:
        task = self.controller.get_task(task_id)
        if task.completed:
            self.controller.update_task(task_id, completed=False)
            await message.answer("The task is marked as not completed!")
        else:
            self.controller.update_task(task_id, completed=True)
            await message.answer("The task is marked as completed!")
        await self.show_tasks(message, user=user)

    async def edit_task(self, message: types.Message, task_id: int, state: FSMContext) -> None:
        task = self.controller.get_task(task_id)
        await state.update_data(task_id=task_id)
        await state.set_state(
            TaskEditStates.title)
        await message.answer(f"Old name:\n{task.title}\nEnter a new task name:")

    async def complete_task(self, message: types.Message, task_id: int, user: types.User) -> None:
        self.controller.update_task(task_id, completed=True)
        await message.answer("The task is marked as completed!")
        await self.show_tasks(message, user=user)

    async def delete_task(self, message: types.Message, task_id: int, user: types.User) -> None:
        self.controller.delete_task(task_id)
        await message.answer("🔥 Task deleted!")
        await self.show_tasks(message, user=user)

    async def process_edit_task_title(self, message: types.Message, state: FSMContext) -> None:
        data = await state.get_data()
        task_id = data.get("task_id")
        task_title = message.text
        if len(task_title) > 50:
            await message.answer("⚠️ The title is too long. Please., "
                                 "enter a name no longer than 50 characters:")
            return
        self.controller.update_task(task_id, task_title,)
        await message.answer(
            f"Task updated: '{task_title}'!")
        await state.clear()
        await self.show_tasks(message, user=message.from_user)

    async def run(self):
        await self.dp.start_polling(self.bot)


def main():
    api_token = os.getenv("API_TOKEN")
    bot = TelegramBot(api_token)
    asyncio.run(bot.run())


if __name__ == '__main__':
    main()

# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class TaskView:
    def __init__(self, controller):
        self.controller = controller

    async def show_welcome(self, message: types.Message, user: types.User):
        builder = InlineKeyboardBuilder()
        builder.row(
            types.InlineKeyboardButton(
                text="✚ Add task",
                callback_data="add_task"
            )
        )
        builder.row(types.InlineKeyboardButton(
            text=f"📝 My tasks [{self.controller.get_all_tasks(user.id)}]",
            callback_data="show_tasks")
        )
        builder.row(types.InlineKeyboardButton(
            text="🐱 GitHub", url="https://github.com")
        )

        msg = (f"<b>{user.full_name}</b>! Welcome to your ToDo app.\n\n"
               f'To view your tasks, click "My tasks"')

        await message.answer(msg, reply_markup=builder.as_markup())

    async def show_tasks(self, message: types.Message, user: types.User):
        builder = InlineKeyboardBuilder()
        tasks = self.controller.get_all_tasks(user.id)

        if not tasks:
            builder.row(types.InlineKeyboardButton(
                text="◀️ To the main page",
                callback_data="back_to_start")
            )
            await message.answer("You have no tasks.", reply_markup=builder.as_markup())
            return

        msg = f'<b>{user.full_name}</b>, here are your tasks:'
        for n, task in enumerate(tasks, 1):
            builder.row(types.InlineKeyboardButton(
                text=f"{task.name} (Completed: {task.completed})",
                callback_data=f"task_{n}")
            )
        builder.row(types.InlineKeyboardButton(
            text="◀️ Back",
            callback_data="back_to_start")
        )

        await message.answer(msg, reply_markup=builder.as_markup())

    async def show_task_details(self, message: types.Message, task):
        button_text = "❌ Mark as not completed" if task.completed else "✅ Mark as done"
        keyboard = InlineKeyboardBuilder()
        keyboard.row(
            types.InlineKeyboardButton(
                text="✏️ Change",
                callback_data=f"edit_task_{task.id}"
            )
        )
        keyboard.row(
            types.InlineKeyboardButton(
                text=button_text,
                callback_data=f"toggle_task_{task.id}"
            )
        )
        keyboard.row(
            types.InlineKeyboardButton(
                text="🔥 Delete",
                callback_data=f"delete_task_{task.id}"
            )
        )
        keyboard.row(
            types.InlineKeyboardButton(
                text="◀️ To the tasks",
                callback_data="show_tasks"
            )
        )
        text = (f"📝 Task:\n\n{task.name}\n\n"
                f"⏳ Status: {'Completed' if task.completed else 'Not completed'}\n")
        await message.answer(
            text,
            reply_markup=keyboard.as_markup()
        )

    async def task_added(self, message: types.Message, task_title: str):
        await message.answer(f"Task '{task_title}' added!")

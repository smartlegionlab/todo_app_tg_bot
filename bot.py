# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

from utils.config import AppConfig

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class TelegramBot:
    config = AppConfig()

    def __init__(self, token):
        self.bot = Bot(
            token=token,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML
            )
        )
        self.dp = Dispatcher()
        self.dp.message(Command("start"))(self.cmd_start)

    async def cmd_start(self, message: types.Message, user: types.User = None) -> None:
        if user is None:
            user = message.from_user

        msg = f"<b>{user.full_name}</b>. Welcome to <b>{self.config.app_name}</b>.\n\n"

        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="🐱 GitHub", url=self.config.github_url)
        )
        await message.answer(msg, reply_markup=builder.as_markup())

    async def run(self):
        await self.dp.start_polling(self.bot)


def main():
    api_token = os.getenv("API_TOKEN")
    bot = TelegramBot(api_token)
    asyncio.run(bot.run())


if __name__ == '__main__':
    main()

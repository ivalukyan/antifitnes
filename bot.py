import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from env import TOKEN
from auth import signup
from auth import login


router = Router()


async def main():
    """
    bot - main construction fun of bot
    dp - dispatcher
    """
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    dp = Dispatcher()
    dp.include_routers(signup.router, login.router)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.dispatcher.dispatcher import FSMContext
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from env import TOKEN
from auth import signup
from auth import login
from schedule import training_session
from stats import top


router = Router()


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(
        f"Здравствуйте, <i>{message.from_user.first_name}</i>, вас приветствует бот спортивного клуба\n\n"
        f"Для того чтобы продолжить ввойдите в свой аккканут с помощью команды - <b>/login</b>\n"
        f"или зарегестрируйтесь с помощью команды - <b>/signup</b>")


async def main():
    """
    bot - main construction fun of bot
    dp - dispatcher
    """
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    dp = Dispatcher()
    dp.include_routers(signup.router, login.router, training_session.router, top.router, router)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

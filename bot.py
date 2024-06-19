import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from env import TOKEN
from src.auth import signup, login
from src.schedule import training_session
from src.stats import top
from src.admin import adm
from src.db.db_users import create_users

router = Router()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await create_users()
    await message.answer(
        f"Здравствуйте, <i>{message.from_user.first_name}</i>, вас приветствует бот спортивного клуба\n\n"
        f"Для того чтобы продолжить ввойдите в свой аккканут с помощью команды - <b>/login</b>\n"
        f"или зарегестрируйтесь с помощью команды - <b>/signup</b>\n"
        f"Для того чтобы узнать возможонсти бота - <b>/help</b>")


@router.message(Command('help'))
async def command_help(message: Message) -> None:
    await message.answer(f"‼️<b>КОМАНДЫ</b>‼️\n\n"
                         f"<i>/help</i> - возможность посмотреть все команды\n"
                         f"<i>/signup</i> - команда для регистрации пользователя\n"
                         f"<i>/login</i> - команда для входа пользователя\n"
                         f"<i>/schedule</i> - команда для записи на тренировку\n"
                         f"<i>/top</i> - команда для просмотра рейтингов")


async def main():
    """
    bot - main construction fun of bot
    dp - dispatcher
    """
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    dp = Dispatcher()
    dp.include_routers(signup.router, login.router, training_session.router, top.router, adm.router, router)

    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    asyncio.run(main())

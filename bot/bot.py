import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from env import BotEnv
from auth.login import router as login_router
from profile.profile import router as profile_router
from schedules.training_session import router as schedule_router
from records.records import router as record_router
from admin import adm
from yaclients.yaclients import CRMain
from db.router import cursor, conn
from db.db_profile import get_name
from yaclients.yaclients import update_without_db


bot_env = BotEnv()

router = Router()
bot = Bot(token=bot_env.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.update_data(user_id=message.from_user.id, name=message.from_user.first_name, username=message.from_user.username)

    await message.answer(
        f"Здравствуйте, <i>{message.from_user.first_name}</i>, вас приветствует бот спортивного клуба\n\n",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Войти', callback_data='login')],
            [InlineKeyboardButton(text="Помощь", callback_data='help')]
        ]))


@router.callback_query(F.data == "help")
async def command_help(callback: CallbackQuery) -> None:
    await callback.message.edit_text(f"‼️<b>КОМАНДЫ</b>‼️\n\n",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Войти", callback_data="login")],
                                         [InlineKeyboardButton(text="Профиль", callback_data="profile")],
                                         [InlineKeyboardButton(text="Запись на тренировку", callback_data="schedule")],
                                         [InlineKeyboardButton(text="Рекорды", callback_data="top")],
                                         [InlineKeyboardButton(text="Назад", callback_data="back")]
                                     ]))


@router.callback_query(F.data == "back")
async def back_to_menu(callback: CallbackQuery):

    await callback.message.edit_text(
        f"Здравствуйте, <i>{callback.message.chat.first_name}</i>, вас приветствует бот спортивного клуба\n\n",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Войти', callback_data='login')],
            [InlineKeyboardButton(text="Помощь", callback_data='help')]
        ]))


@router.message(Command('update'))
async def command_update(message: Message) -> None:
    await update_without_db(message)


@router.message(Command('updatedb'))
async def command_update_db(message: Message) -> None:
    await CRMain(message)


@router.message(Command('delete'))
async def command_delete(message: Message) -> None:
    cursor.execute("""SELECT phone_number FROM public.bot_app_profile""")
    result = cursor.fetchall()
    if result is None:
        await message.answer("пользоатели уже удалены!")
    else:
        cursor.execute("""DELETE FROM public.bot_app_profile""")
        conn.commit()
        await message.answer("Пользователи удалены!")


async def main():
    """
    bot - main construction fun of bot
    dp - dispatcher
    """
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    dp = Dispatcher()
    dp.include_routers(login_router, schedule_router, record_router, adm.router, profile_router, router)
    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    asyncio.run(main())
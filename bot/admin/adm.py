import aiohttp

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)

from bot import bot
from db.db_profile import get_all_users
from env import HOST_PROD, BotEnv

bot_env = BotEnv()

router = Router()


class Form(StatesGroup):
    """
    req_adm - state for send messages from users
    """

    # Admin
    mailing = State()


# ADMIN
def check_admin(user_id) -> bool:
    if str(user_id) in bot_env.admin:
        return True
    return False


@router.message(Command('admin'))
async def login(message: Message, state: FSMContext) -> None:
    if check_admin(message.from_user.id):
        await message.answer("<b>АДМИН ПАНЕЛЬ</b>", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Рассылка", callback_data="request_adm")],
            [InlineKeyboardButton(text="Админ панель", url=f'http://{HOST_PROD}:8000/admin')],
            [InlineKeyboardButton(text="Cайт спорт-бот", url=f'http://{HOST_PROD}:8000/')]
        ]))
    else:
        await message.answer("Вам не выдана данная роль")


@router.callback_query(F.data == "request_adm")
async def callback_request_adm(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.mailing)
    await callback.message.edit_text("Введите сообщение для рассылки: ")


@router.message(Form.mailing)
async def request_adm(message: Message, state: FSMContext) -> None:
    mes = message.text
    users = await get_all_users()
    if users is None:
        await message.answer("Пользователи не найдены")
    else:
        for _ in users:
            await bot.send_message(int(_), f"‼️РАССЛЫКА‼️\n\n"
                                           f"{mes}")

    await state.clear()

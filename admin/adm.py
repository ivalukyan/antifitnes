from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)

from bot import bot
from db.db_users import get_all_users
from env import ADMINS

router = Router()


class Form(StatesGroup):
    """
    req_adm - state for send messages from users
    """

    # Admin
    req_adm = State()


# ADMIN
def check_admin(user_id) -> bool:
    if user_id in ADMINS:
        return True
    return False


@router.message(Command('admin'))
async def login(message: Message, state: FSMContext) -> None:
    if check_admin(message.from_user.id):
        await message.answer("<b>АДМИН ПАНЕЛЬ</b>", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Рассылка", callback_data="request_adm")]
        ]))
    else:
        await message.answer("Вам не выдана данная роль")


@router.callback_query(F.data == "request_adm")
async def request_adm(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.req_adm)
    await callback.message.edit_text("Введите сообщение для рассылки: ")


@router.message(Form.req_adm)
async def request_adm(state: FSMContext) -> None:
    users = get_all_users()
    for _ in users:
        bot.send_message(_, "‼️РАССЛЫКА‼️")

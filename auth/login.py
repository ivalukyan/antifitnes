import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)

router = Router()


class Form(StatesGroup):
    """
    number_login - state for input number user
    """

    # Loging
    number_login = State()


# Login in your personal account
@router.message(Command('login'))
async def login(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.number_login)
    await message.answer("<b>ВХОД В СИСТЕМУ</b>\n\n"
                         "Введите номер своего телефона: ")


@router.message(Form.number_login)
async def input_number(message: Message, state: FSMContext) -> None:
    await state.update_data(input_number=message.text)
    data = await state.get_data()
    # В дальнейшем будет сравнение с БД
    if '89897353234' == str(
            data['input_number']):
        await message.answer(f"{message.from_user.first_name}, добро пожаловать, в спортивный клуб!")
        await message.answer("Функционал", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Становая тяга", callback_data="norm_1"),
                InlineKeyboardButton(text="Жим лежа", callback_data="norm_2"),
                InlineKeyboardButton(text="Присед", callback_data="norm_3"),
            ]
        ]))
    else:
        await message.answer("Упс...похоже ошибка в веденных данных")


@router.callback_query(F.data == "norm_1")
async def callback_query_norm_1(callback: CallbackQuery, state: FSMContext) -> None:
    try:
        await callback.message.answer("60x5")
    except Exception.args:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
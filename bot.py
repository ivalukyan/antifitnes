import asyncio
import logging
import pickle
import sys
import re
import bcrypt
from os import getenv
from typing import Any, Dict

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)
from aiogram.methods import EditMessageText, DeleteMessage
from env import TOKEN

router = Router()

hash_pass = bcrypt.hashpw('Qwerty1234!'.encode(), bcrypt.gensalt())
user_data = {'user1': {'number': 89795353234, 'password': {hash_pass}}}  # Для тестов /loging так как пока без БД


class Form(StatesGroup):
    """
    signup_number - state from user for adding number
    signup_password - state for adding user`s password
    approved_signup - state for checking data`s user
    replace_signup - state for replacing data`s user
    """
    # Signup
    signup_gender = State()
    signup_number = State()
    signup_approve = State()
    signup_end = State()
    signup_replace = State()

    save_name = State()
    save_number = State()

    # Loging
    number_login = State()
    password_login = State()


@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer(
        f"Здравствуйте, <i>{message.from_user.first_name}</i>, вас приветствует бот спортивного клуба\n\n"
        f"Для того чтобы продолжить ввойдите в свой аккканут с помощью команды - <b>/login</b>\n"
        f"или зарегестрируйтесь с помощью команды - <b>/signup</b>")


@router.message(Command('signup'))
async def signup(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.from_user.first_name)
    await state.update_data(username=message.from_user.username)
    await message.answer("Укажите свой пол:", reply_markup=ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="м"),
            KeyboardButton(text="ж"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True))
    await state.set_state(Form.signup_gender)


@router.message(Form.signup_gender, F.text.casefold() == "м")
async def gen_men(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(Form.signup_number)
    await message.answer("Введите номер телефона:")


@router.message(Form.signup_number, F.text.casefold() == "ж")
async def geb_women(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(Form.signup_number)
    await message.answer("Введите номер телефона:")


def check_number(user_number) -> bool:
    phone_number_pattern = r'^\+\d{1,2}|8\d{3}\d{3}\d{4}$'

    if re.match(phone_number_pattern, user_number):
        return True
    else:
        return False


@router.message(Form.signup_number)
async def add_number(message: Message, state: FSMContext) -> None:
    number = message.text
    if check_number(number):
        await state.update_data(number=number)
        await state.set_state(Form.signup_approve)
        data = await state.get_data()
        await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                             f"Имя: {data['name']}\n"
                             f"Пол: {data['gender']}"
                             f"Имя пользователя: {data['username']}\n"
                             f"Телефон: {data['number']}\n")
        await message.answer("Подтвердите если все данные введены корректно:",
                             reply_markup=ReplyKeyboardMarkup(keyboard=[
                                 [
                                     KeyboardButton(text="да"),
                                     KeyboardButton(text="нет"),
                                 ]
                             ], resize_keyboard=True, one_time_keyboard=True))
        await state.set_state(Form.signup_end)
    else:
        await message.answer("Упс... походу вы ввели не номер телефона")


@router.message(Form.signup_end, F.text.casefold() == "да")
async def end_signup(message: Message, state: FSMContext) -> None:
    await message.answer("Вы успешно зарегистрированные в системе!\n\n"
                         "В войдите в аккаунт с помощью - <b>/login</b>")
    # Отправка данных админу и в БД


@router.message(Form.signup_end, F.text.casefold() == "нет")
async def edit_form_signup(message: Message, state: FSMContext) -> None:
    # Исправление поля выбранного пользователем с помощью кнопки
    await state.set_state(Form.signup_replace)
    await message.answer(f"<i>{message.from_user.first_name}</i>, какое поле вы хотели бы заменить?\n",
                         reply_markup=ReplyKeyboardMarkup(keyboard=[
                             [
                                 KeyboardButton(text="Имя"),
                                 KeyboardButton(text="Номер"),
                                 KeyboardButton(text="↩️")
                             ]
                         ], resize_keyboard=True, one_time_keyboard=True))


@router.message(Form.signup_replace, F.text.casefold() == "имя")
async def replace_name_form_signup(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.save_name)
    await message.answer("Введите новое имя: ")


@router.message(Form.signup_replace, F.text.casefold() == "номер")
async def replace_number_form_signup(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.save_number)
    await message.answer("Введите новый номер: ")


@router.message(Form.signup_replace, F.text.casefold() == "↩️")
async def back_menu_form_signup(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                         f"Имя: {data['name']}\n"
                         f"Пол: {data['gender']}\n"
                         f"Имя пользователя: {data['username']}\n"
                         f"Телефон: {data['number']}\n")
    await message.answer("Подтвердите если все данные введены корректно:", reply_markup=ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="да"),
            KeyboardButton(text="нет"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True))
    await state.set_state(Form.signup_end)


@router.message(Form.save_name)
async def save_new_name(message: Message, state: FSMContext) -> None:
    name = message.text
    await state.update_data(name=name)
    data = await state.get_data()
    # Добавление данных в БД
    await message.answer("Имя заменено, вы успешно зарегистрированы")
    await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                         f"Имя: {data['name']}\n"
                         f"Пол: {data['gender']}\n"
                         f"Имя пользователя: {data['username']}\n"
                         f"Телефон: {data['number']}\n")


@router.message(Form.save_number)
async def save_new_number(message: Message, state: FSMContext) -> None:
    number = message.text
    await state.update_data(number=number)
    data = await state.get_data()
    await message.answer("Номер изменен")
    await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                         f"Имя: {data['name']}\n"
                         f"Пол: {data['gender']}\n"
                         f"Имя пользователя: {data['username']}\n"
                         f"Телефон: {data['number']}\n")


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
    print(data)
    if str(user_data['user1']['number']) == str(
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


async def main():
    """
    bot - main construction fun of bot
    dp - dispatcher
    """
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)

    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

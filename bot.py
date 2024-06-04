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
    ReplyKeyboardRemove,
)
from aiogram.methods import EditMessageText
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
    signup_number = State()
    signup_password = State()
    approved_signup = State()
    replace_signup = State()
    save_name = State()
    save_number = State()
    save_password = State()
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
    await state.set_state(Form.signup_number)
    await state.update_data(name=message.from_user.first_name)
    await state.update_data(username=message.from_user.username)
    await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                         f"Имя: {message.from_user.first_name}\n"
                         f"Телефон: (не найден)\n"
                         f"Имя пользователя: {message.from_user.username}\n"
                         f"Пароль: (не найден)\n\n"
                         f"Укажите свой номер телефона!!!")


@router.message(Command('login'))
async def login(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.number_login)
    await message.answer("<b>ВХОД В СИСТЕМУБ</b>\n\n"
                         "Номер: \n"
                         "Пароль: ")
    await message.answer("Введите номер своего телефона ->")


@router.message(Form.number_login)
async def input_number(message: Message, state: FSMContext) -> None:
    await state.update_data(input_number=message.text)
    await state.set_state(Form.password_login)
    await message.answer("Введите пароль ->")


@router.message(Form.password_login)
async def input_password(message: Message, state: FSMContext) -> None:
    await state.update_data(input_password=message.text)
    data = await state.get_data()
    if bcrypt.checkpw(data['input_password'].encode(), hash_pass) and str(user_data['user1']['number']) == str(data['input_number']):
        await message.answer("Добро пожаловать, в спортивный клуб!")
    else:
        await message.answer("Упс...похоже ошибка в веденных данных")


def check_number(user_number) -> bool:
    phone_number_pattern = r'^\+\d{1,2}|8\d{3}\d{3}\d{4}$'

    if re.match(phone_number_pattern, user_number):
        return True
    else:
        return False


@router.message(Form.signup_number)
async def add_number(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    number = message.text
    if check_number(number):
        await state.update_data(number=number)
        await state.set_state(Form.signup_password)
        await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                             f"Имя: {data['name']}\n"
                             f"Телефон: {number}\n"
                             f"Имя пользователя: {data['username']}\n\n"
                             f"Придумайте пароль: ")
    else:
        await message.answer("Упс... походу вы ввели не номер телефона")


def check_password(user_password):
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    if re.match(password_pattern, user_password):
        return True
    else:
        return False


@router.message(Form.signup_password)
async def add_user_password(message: Message, state: FSMContext):
    data = await state.get_data()
    password = message.text
    if check_password(password):
        hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        await state.update_data(password=hash_password)
        await state.set_state(Form.approved_signup)
        await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                             f"Имя: {data['name']}\n"
                             f"Телефон: {data['number']}\n"
                             f"Имя пользователя: {data['username']}\n"
                             f"Пароль: {password}\n\n"
                             f"Если все верно подтвердите кнопкой  - <b>ДА</b>\n"
                             f"или если данные требуют изменения подтвердите кнопкой - <b>НЕТ</b>",
                             reply_markup=ReplyKeyboardMarkup(keyboard=[
                                 [
                                     KeyboardButton(text="Да"),
                                     KeyboardButton(text="Нет"),
                                 ]
                             ], resize_keyboard=True, one_time_keyboard=True))
    else:
        await message.answer("Ваш пароль не соответствует требованиям\n\n"
                             " - Должен содержать как минимум одну заглавную букву\n"
                             " - Должен содержать как минимум одну строчную букву\n"
                             " - Должен содержать как минимум одну цифру\n"
                             " - Должен содержать как минимум один из специальных символов\n"
                             " - Длина пароля должна быть не менее 8 символов")


@router.message(Form.approved_signup, F.text.casefold() == "да")
async def end_signup(message: Message, state: FSMContext) -> None:
    await message.answer("Вы успешно зарегистрированные в системе!\n\n"
                         "В войдите в аккаунт с помощью - <b>/login</b>")
    # Отправка данных админу и в БД


@router.message(Form.approved_signup, F.text.casefold() == "нет")
async def edit_form_signup(message: Message, state: FSMContext) -> None:
    # Исправление поля выбранного пользователем с помощью кнопки
    await state.set_state(Form.replace_signup)
    await message.answer(f"<i>{message.from_user.first_name}</i>, какое поле вы хотели бы заменить?\n",
                         reply_markup=ReplyKeyboardMarkup(keyboard=[
                             [
                                 KeyboardButton(text="Имя"),
                                 KeyboardButton(text="Номер"),
                                 KeyboardButton(text="Пароль")
                             ]
                         ], resize_keyboard=True, one_time_keyboard=True))


@router.message(Form.replace_signup, F.text.casefold() == "имя")
async def replace_name_form_signup(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.save_name)
    await message.answer("Введите новое имя: ")


@router.message(Form.replace_signup, F.text.casefold() == "номер")
async def replace_number_form_signup(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.save_number)
    await message.answer("Введите новый номер: ")


@router.message(Form.replace_signup, F.text.casefold() == "пароль")
async def replace_password_form_signup(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.save_password)
    await message.answer("Введите новый пароль: ")


@router.message(Form.save_name)
async def save_new_name(message: Message, state: FSMContext) -> None:
    name = message.text
    await state.update_data(name=name)
    data = await state.get_data()
    # Добавление данных в БД
    await message.answer("Имя заменено, вы успешно зарегистрированы")
    await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                         f"Имя: {data['name']}\n"
                         f"Телефон: {data['number']}\n"
                         f"Имя пользователя: {data['username']}\n"
                         f"Пароль: {data['password']}\n\n")


@router.message(Form.save_number)
async def save_new_number(message: Message, state: FSMContext) -> None:
    number = message.text
    if check_password(number):
        await state.update_data(number=number)
        # Добавление данных в БД
        data = await state.get_data()
        await message.answer("Номер заменен, вы успешно зарегистрированы")
        await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                             f"Имя: {data['name']}\n"
                             f"Телефон: {data['number']}\n"
                             f"Имя пользователя: {data['username']}\n"
                             f"Пароль: {data['password']}\n\n")
    else:
        await message.answer("Упс... похоже вы ввели не номер телефона")


@router.message(Form.save_password)
async def save_new_password(message: Message, state: FSMContext) -> None:
    password = message.text
    if check_password(password):
        hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        await state.update_data(password=hash_password)
        # Добавление данных в БД
        data = await state.get_data()
        await message.answer("Пароль заменен, вы успешно зарегистрированы")
        await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                             f"Имя: {data['name']}\n"
                             f"Телефон: {data['number']}\n"
                             f"Имя пользователя: {data['username']}\n"
                             f"Пароль: {data['password']}\n\n")
    else:
        await message.answer("Ваш пароль не соответствует требованиям\n\n"
                             " - Должен содержать как минимум одну заглавную букву\n"
                             " - Должен содержать как минимум одну строчную букву\n"
                             " - Должен содержать как минимум одну цифру\n"
                             " - Должен содержать как минимум один из специальных символов\n"
                             " - Длина пароля должна быть не менее 8 символов")


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

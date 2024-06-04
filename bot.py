import asyncio
import logging
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


class Form(StatesGroup):
    """
    signup_number - state from user for adding number
    signup_password - state for adding user`s password
    approved_signup - state for checking data`s user
    """
    signup_number = State()
    signup_password = State()
    approved_signup = State()


@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer(f"Здравствуйте, <i>{message.from_user.first_name}</i>, вас приветствует бот спортивного клуба\n\n"
        f"Для того чтобы продолжить ввойдите в свой аккканут с помощью команды - <b>/login</b>\n"
        f"или зарегестрируйтесь с помощью команды - <b>/signup</b>")





@router.message(Command('signup'))
async def signup(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.signup_number)
    await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                         f"Имя: {message.from_user.first_name}\n"
                         f"Телефон: (не найден)\n"
                         f"Имя пользователя: {message.from_user.username}\n"
                         f"Пароль: (не найден)\n\n"
                         f"Укажите свой номер телефона!!!")


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
        await state.set_state(Form.signup_password)
        await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                             f"Имя: {message.from_user.first_name}\n"
                             f"Телефон: {number}\n"
                             f"Имя пользователя: {message.from_user.username}\n\n"
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
                             f"Имя: {message.from_user.first_name}\n"
                             f"Телефон: {data['number']}\n"
                             f"Имя пользователя: {message.from_user.username}\n"
                             f"Пароль: {hash_password}\n\n"
                             f"Если все верно подтвердите кнопкой  - ДА\n"
                             f"или если данные требуют изменения подтвердите кнопкой - НЕТ",
                             reply_markup=ReplyKeyboardMarkup(keyboard=[
                [
                    KeyboardButton(text="Да"),
                    KeyboardButton(text="Нет"),
                ]
            ], resize_keyboard=True, one_time_keyboard=True))
    else:
        await message.answer("Ваш пароль не соответсвует требованиям\n\n"
                             " - Должен содержать как минимум одну заглавную букву\n"
                             " - Должен содержать как минимум одну строчную букву\n"
                             " - Должен содержать как минимум одну цифру\n"
                             " - Должен содержать как минимум один из специальных символов\n"
                             " - Длина пароля должна быть не менее 8 символов")

@router.message(Form.approved_signup, F.text.casefold() == "да")
async def end_signup(message: Message, state: FSMContext) -> None:
    await message.answer("Вы успешно зарегестрированны в системе!")
    # Отправка данных админу и в БД


@router.message(Form.approved_signup, F.text.casefold() == "нет")
async def edit_form_signup(message: Message, state: FSMContext) -> None:
    ...
    # Исправление поля выбраного пользователем с помощью кнопки


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

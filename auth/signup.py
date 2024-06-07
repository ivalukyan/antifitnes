import re

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)

router = Router()


class Form(StatesGroup):
    """
    signup_number - state from user for adding number
    signup_password - state for adding user`s password
    signup_approve - state for checking data`s user
    signup_replace - state for replacing data`s user
    signup_end - state for ending registration
    save_name - state for saving user's name
    save_number - state for saving user's number
    """
    # Signup
    signup_gender = State()
    signup_number = State()
    signup_approve = State()
    signup_end = State()
    signup_replace = State()

    save_name = State()
    save_number = State()


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
    await message.answer("Укажите свой пол:", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="м", callback_data="gen_m"),
            InlineKeyboardButton(text="ж", callback_data="gen_j"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True))


@router.callback_query(F.data == "gen_m")
async def gen_m_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(gender='м')
    await state.set_state(Form.signup_number)
    await callback.message.answer("Введите номер телефона: ")


@router.callback_query(F.data == "gen_j")
async def gen_j_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(gender='ж')
    await state.set_state(Form.signup_number)
    await callback.message.answer('Введите номер телефона: ')


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
                             f"Пол: {data['gender']}\n"
                             f"Имя пользователя: {data['username']}\n"
                             f"Телефон: {data['number']}\n")
        await message.answer("Подтвердите если все данные введены корректно:",
                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="да", callback_data="yes"),
                                     InlineKeyboardButton(text="нет", callback_data="no"),
                                 ]
                             ], resize_keyboard=True, one_time_keyboard=True))
        await state.set_state(Form.signup_end)
    else:
        await message.answer("Упс... походу вы ввели не номер телефона")


@router.callback_query(F.data == "yes")
async def yes_callback(callback: CallbackQuery) -> None:
    await callback.message.answer("Вы успешно зарегистрированные в системе!\n\n"
                                  "В войдите в аккаунт с помощью - <b>/login</b>")
    # Отправка данных админу и в БД


@router.callback_query(F.data == "no")
async def no_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.signup_replace)
    await callback.message.answer(
        f"<i>{callback.message.from_user.first_name}</i>, какое поле вы хотели бы заменить?\n",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Имя", callback_data="name"),
                InlineKeyboardButton(text="Номер", callback_data="number"),
                InlineKeyboardButton(text="↩️", callback_data="back")
            ]
        ], resize_keyboard=True, one_time_keyboard=True))


@router.callback_query(F.data == "name")
async def name_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.save_name)
    await callback.message.answer("Введите новое имя: ")


@router.callback_query(F.data == "number")
async def number_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.save_number)
    await callback.message.answer("Введите новый номер: ")


@router.callback_query(F.data == 'back')
async def back_callback(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    await callback.message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                         f"Имя: {data['name']}\n"
                         f"Пол: {data['gender']}\n"
                         f"Имя пользователя: {data['username']}\n"
                         f"Телефон: {data['number']}\n")
    await callback.message.answer("Подтвердите если все данные введены корректно:", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="да", callback_data="yes"),
                InlineKeyboardButton(text="нет", callback_data="no"),
            ]
        ]
    ), resize_keyboard=True, one_time_keyboard=True)


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

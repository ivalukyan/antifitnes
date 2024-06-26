import re

from aiogram import F, Router
from aiogram.client.session import aiohttp
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)

from src.db.db_users import get_all_users, add_user
from src.db.db_profile import add_info_profile
from src.db.db_standards import insert_standard
from env import ALL_USERS_URL, PROFILE_URL

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


@router.message(Command('signup'))
async def signup(message: Message, state: FSMContext) -> None:
    await state.update_data(id=message.from_user.id)
    await state.update_data(first_name=str(message.from_user.first_name))
    await state.update_data(username=str(message.from_user.username))
    if message.from_user.id not in (await get_all_users()):
        await message.answer("Укажите свой пол:", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="м", callback_data="gen_m"),
                InlineKeyboardButton(text="ж", callback_data="gen_j"),
            ]
        ], resize_keyboard=True, one_time_keyboard=True))
    else:
        await message.answer("Вы уже зарегистрированны.")


@router.callback_query(F.data == "gen_m")
async def gen_m_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(gender='Men')
    await state.set_state(Form.signup_number)
    await callback.message.edit_text("Введите номер телефона: ")


@router.callback_query(F.data == "gen_j")
async def gen_j_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(gender='Women')
    await state.set_state(Form.signup_number)
    await callback.message.edit_text('Введите номер телефона: ')


async def check_number(user_number) -> bool:
    phone_number_pattern = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{10}$'

    if re.match(phone_number_pattern, user_number):
        return True
    else:
        return False


async def check_name(user_name) -> bool:
    name_pattern = r'^[А-Я][а-яё]*$'

    if re.match(name_pattern, user_name):
        return True
    else:
        return False


@router.message(Form.signup_number)
async def add_number(message: Message, state: FSMContext) -> None:
    number = message.text
    if await check_number(number):
        await state.update_data(number=number)
        await state.set_state(Form.signup_approve)
        data = await state.get_data()
        await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                             f"Имя: {data['first_name']}\n"
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
async def yes_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_text("Вы успешно зарегистрированные в системе!\n\n"
                                     "Войдите в аккаунт с помощью - <b>/login</b>")
    data = await state.get_data()

    if data["gender"] == 'Men':
        await add_user(data['id'], data['first_name'], data['username'], 'gen_men', data['number'])
        await add_info_profile(data['id'], "", 0, "", "")
        await insert_standard(data['id'])
    elif data["gender"] == 'Women':
        await add_user(data['id'], data['first_name'], data['username'], 'gen_women', data['number'])
        await add_info_profile(data['id'], "", 0, "", "")
        await insert_standard(data['id'])


@router.callback_query(F.data == "no")
async def no_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.signup_replace)
    await callback.message.edit_text(
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
    await callback.message.edit_text("Введите новое имя: ")


@router.callback_query(F.data == "number")
async def number_callback(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Form.save_number)
    await callback.message.edit_text("Введите новый номер: \n<i>пример: +79889999898</i>")


@router.callback_query(F.data == 'back')
async def back_callback(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    await callback.message.edit_text(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
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
    if await check_name(name):
        await state.update_data(name=name)
        data = await state.get_data()
        await message.answer("Имя заменено, вы успешно зарегистрированы")
        await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                             f"Имя: {data['name']}\n"
                             f"Пол: {data['gender']}\n"
                             f"Имя пользователя: {data['username']}\n"
                             f"Телефон: {data['number']}\n")
        await message.answer("Вы успешно зарегистрированные в системе!\n\n"
                             "Войдите в аккаунт с помощью - <b>/login</b>")

        if data["gender"] == 'Men':
            await add_user(data['id'], name, data['username'], 'gen_men', data['number'])
            await add_info_profile(data['id'], "", 0, "", "")
            await insert_standard(data['id'])
        elif data["gender"] == 'Women':
            await add_user(data['id'], name, data['username'], 'gen_women', data['number'])
            await add_info_profile(data['id'], "", 0, "", "")
            await insert_standard(data['id'])
        await state.clear()

    else:
        await message.answer("Упс... имя введено не верно")


@router.message(Form.save_number)
async def save_new_number(message: Message, state: FSMContext) -> None:
    number = message.text
    if check_number(number):
        await state.update_data(number=number)
        data = await state.get_data()
        await message.answer("Номер изменен")
        await message.answer(f"<b>РЕГИСТРАЦИЯ</b>\n\n"
                             f"Имя: {data['name']}\n"
                             f"Пол: {data['gender']}\n"
                             f"Имя пользователя: {data['username']}\n"
                             f"Телефон: {data['number']}\n")
        await message.answer("Вы успешно зарегистрированные в системе!\n\n"
                             "Войдите в аккаунт с помощью - <b>/login</b>")

        if data["gender"] == 'Men':
            await add_user(data['id'], data['first_name'], data['username'], 'gen_men', data['number'])
            await add_info_profile(data['id'], "", 0, "", "")
            await insert_standard(data['id'])
        elif data["gender"] == 'Women':
            await add_user(data['id'], data['first_name'], data['username'], 'gen_women', data['number'])
            await add_info_profile(data['id'], "", 0, "", "")
            await insert_standard(data['id'])
        await state.clear()
    else:
        await message.answer("Упс... номер введен не правильно")

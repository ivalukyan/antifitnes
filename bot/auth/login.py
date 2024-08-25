import re

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton,
    Message)

from db.db_profile import update_profile, get_all_phones, get_telegram_status
from db.db_standards import get_standards_by_id
from yaclients.yaclients import search, crm, get_history_client, get_personal_id, get_abonements

router = Router()


class Form(StatesGroup):
    """
    number_login - state for input number user
    """

    # Loging
    number_login = State()


# Login in your personal account
@router.callback_query(F.data == "login")
async def login(callback: CallbackQuery, state: FSMContext) -> None:

    if await get_telegram_status(callback.message.chat.id):
        await callback.message.edit_text("Вы уже зарегестрированы", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Профиль", callback_data="profile")]
        ]))
    else:
        await state.set_state(Form.number_login)
        await callback.message.answer("<b>ВХОД В СИСТЕМУ</b>\n\n"
                                      "Введите номер своего телефона\n<i>пример:</i> +79889897878")


@router.message(Form.number_login)
async def input_number(message: Message, state: FSMContext) -> None:
    await message.answer('Настраиваем ваш профиль...')

    # Записываем веденный номер телефона в состояние
    await state.update_data(input_number=message.text)

    data = await state.get_data()

    if await checking_number(data['input_number']) and await get_all_phones(data['input_number'][-10:]):

        # Not prod: при отсутствии данных бот создавал default данные в таблице Standards - Нормативы
        # await insert_standard(message.from_user.id, crm['names'][await search(data['input_number'])])

        # Not prod: при отсутствии данных бот создавал default данные в таблице Statistic - Статистика
        # await insert_stats(message.from_user.id, crm['names'][await search(data['input_number'])])

        await update_profile(
            telegram_id=message.from_user.id,
            telegram_status=True,
            username=message.from_user.username,
            training_history=await get_history_client(crm['user_token'],
                                                      data['input_number'][-11:],
                                                      await get_personal_id(await search(
                                                          data['input_number']))),
            info_subscription=await get_abonements(crm['user_token'], data['input_number']),
            current_standard=await get_standards_by_id(message.from_user.id),
            phone_number=data['input_number'][-10:]
        )

        await message.answer("Вы успешно вошли!", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Профиль", callback_data="profile")]
        ]))

    else:
        await message.answer("К сожалению, Вы не являетесь клиентом клуба",
                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                 [InlineKeyboardButton(text="Назад", callback_data="back")]
                             ]))


async def checking_number(user_number) -> bool:
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
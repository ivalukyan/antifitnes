import re

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)

from src.db.db_standards import get_standards_by_id, insert_standard
from src.db.db_profile import (training_history, number_of_referral_points, info_subscription, add_info_profile,
                               get_name, check_login)
from src.srm.srm_bot import check_crm, update_profile, crm_info, search, crm, get_name_by_id, get_history_client, \
    get_personal_id, get_abonements
from src.db.db_stats import insert_stats
from src.db.db_statistics import get_statistics_by_user

router = Router()

login_users = []


class Form(StatesGroup):
    """
    number_login - state for input number user
    """

    # Loging
    number_login = State()


# Login in your personal account
@router.message(Command('login'))
async def login(message: Message, state: FSMContext) -> None:
    if await check_login(message.from_user.id):
        await state.set_state(Form.number_login)
        await message.answer("<b>ВХОД В СИСТЕМУ</b>\n\n"
                             "Введите номер своего телефона: \n<i>пример:</i> +79889998989")
    else:
        await message.answer("Вы уже зарегестрированы, используйте команду - /profile чтобы зайти в профиль клиента")


@router.message(Form.number_login)
async def input_number(message: Message, state: FSMContext) -> None:
    await message.answer('Настраиваем ваш профиль...')

    # Записываем веденный номер телефона в состояние
    await state.update_data(input_number=message.text)

    data = await state.get_data()

    await crm_info()

    if await check_crm(data['input_number']) and await checking_number(data['input_number']):

        await message.answer("Вы успешно вошли!\nВоспользуйтесь командой  - /profile")

        login_users.append(message.from_user.id)

        await insert_standard(message.from_user.id, crm['names'][await search(data['input_number'])])

        await insert_stats(message.from_user.id, crm['names'][await search(data['input_number'])])

        if crm['sexes'][await search(data['input_number'])] == 'Мужской':
            await add_info_profile(user_id=message.from_user.id,
                                   first_name=crm['names'][await search(data['input_number'])],
                                   username=message.from_user.username,
                                   gender='gen_men',
                                   phone_number=data['input_number'],
                                   training_history=await get_history_client(crm['user_token'],
                                                                             data['input_number'],
                                                                             await get_personal_id(await search(
                                                                                 data['input_number']))),
                                   number_of_referral_points=0,
                                   info_subscription=await get_abonements(crm['user_token'], data['input_number']),
                                   current_standard=await get_standards_by_id(message.from_user.id)
                                   )
        elif crm['sexes'][await search(data['input_number'])] == 'Женский':
            await add_info_profile(user_id=message.from_user.id,
                                   first_name=crm['names'][await search(data['input_number'])],
                                   username=message.from_user.username,
                                   gender='gen_women',
                                   phone_number=data['input_number'],
                                   training_history=await get_history_client(crm['user_token'],
                                                                             data['input_number'],
                                                                             await get_personal_id(await search(
                                                                                 data['input_number']))),
                                   number_of_referral_points=0,
                                   info_subscription=await get_abonements(crm['user_token'], data['input_number']),
                                   current_standard=await get_standards_by_id(message.from_user.id)
                                   )
        await state.clear()

    else:
        await message.answer("К сожалению, Вы не являетесь клиентом клуба")
        await state.clear()


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

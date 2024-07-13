import re

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
)

from src.db.db_profile import (check_login)
from src.db.db_profile import update_profile
from src.db.db_standards import get_standards_by_id, insert_standard
from src.db.db_stats import insert_stats
from src.srm.srm_bot import search, crm, get_history_client, get_personal_id, get_abonements

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
    if await check_login(message.from_user.id):
        await state.set_state(Form.number_login)
        await message.answer("<b>ВХОД В СИСТЕМУ</b>\n\n"
                             "Введите номер своего телефона: \n<i>пример:</i> +79889998989")
    else:
        await message.answer("Вы уже зарегестрированы\n<i>/profile</i> -  чтобы зайти в профиль клиента")


@router.message(Form.number_login)
async def input_number(message: Message, state: FSMContext) -> None:
    await message.answer('Настраиваем ваш профиль...')

    # Записываем веденный номер телефона в состояние
    await state.update_data(input_number=message.text)

    data = await state.get_data()

    if await checking_number(data['input_number']):

        await insert_standard(message.from_user.id, crm['names'][await search(data['input_number'])])

        await insert_stats(message.from_user.id, crm['names'][await search(data['input_number'])])

        await update_profile(
            telegram_id=message.from_user.id,
            telegram_status=True,
            username=message.from_user.username,
            training_history=await get_history_client(crm['user_token'],
                                                      data['input_number'],
                                                      await get_personal_id(await search(
                                                          data['input_number']))),
            number_of_referral_points=0,
            info_subscription=await get_abonements(crm['user_token'], data['input_number']),
            current_standard=await get_standards_by_id(message.from_user.id),
            phone_number=data['input_number'][-10:]
        )

        await message.answer("Вы успешно вошли!\nВоспользуйтесь командой  - /profile")

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

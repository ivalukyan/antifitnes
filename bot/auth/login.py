import re

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message

from db.router import Session
from db.db_profile import update_profile, get_telegram_status, update_profile, Profile
from db.db_standards import get_standards_by_id
from yaclients.yaclients import Yclients
from env import Crm

router = Router()
crm = Crm()


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

    api = Yclients(bearer_token=crm.bearer, company_id=crm.company_id, user_token=crm.user)

    if await checking_number(user_number=data['input_number']) and await check_login_in_crm(phone=data["input_number"]):

        # Not prod: при отсутствии данных бот создавал default данные в таблице Standards - Нормативы
        # await insert_standard(message.from_user.id, crm['names'][await search(data['input_number'])])

        # Not prod: при отсутствии данных бот создавал default данные в таблице Statistic - Статистика
        # await insert_stats(message.from_user.id, crm['names'][await search(data['input_number'])])
        if await signin_check(data["input_number"]):

            db_session = Session()
            db_session.query(Profile).filter(Profile.telegram_id == message.from_user.id).update({'telegram_id':message.from_user.id,
                                                                                                  'first_name': await api.name(data["input_number"]),
                                                                                                  'username': message.from_user.username,
                                                                                                  'gender': await api.gender(await api.id(data["input_number"])),
                                                                                                  'training_history': await api.history(data["input_number"], await api.id(data["input_number"])),
                                                                                                  'number_of_referral_points': await api.referals(await api.id(data["input_number"])),
                                                                                                  'info_subscription': await api.abonement(data["input_number"]),
                                                                                                  'current_standard': await get_standards_by_id(message.from_user.id),
                                                                                                  'telegram_status': True})
            db_session.commit()

        else:
            await update_profile(telegram_id=message.from_user.id, first_name=await api.name(data["input_number"]),
                                username=message.from_user.username, gender=await api.gender(await api.id(data["input_number"])),
                                phone=data["input_number"], history=await api.history(data["input_number"], await api.id(data["input_number"])),
                                referral=await api.referals(await api.id(data["input_number"])), subscription=await api.abonement(data["input_number"]),
                                standard=await get_standards_by_id(message.from_user.id), status=True)

        await message.answer("Вы успешно вошли!", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Профиль", callback_data="profile")]
        ]))
        await state.clear()

    else:
        await message.answer("К сожалению, Вы не являетесь клиентом клуба",
                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                 [InlineKeyboardButton(text="Назад", callback_data="back")]
                             ]))
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
    

async def check_login_in_crm(phone: str) -> bool:
    
    api = Yclients(bearer_token=crm.bearer, company_id=crm.company_id, user_token=crm.user)
    info = await api.id(phone=phone)
    if not info:
        return False
    return True


async def signin_check(phone: str) -> None:

    db_session = Session()
    res = db_session.query(Profile).filter(Profile.phone_number == phone).first()

    if not res:
        return False
    return True
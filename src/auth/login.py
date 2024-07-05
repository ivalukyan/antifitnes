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

database = {'user_id': 0}


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
                         "Введите номер своего телефона: \n<i>пример:</i> +79889998989")


@router.message(Form.number_login)
async def input_number(message: Message, state: FSMContext) -> None:
    await message.answer('Настраиваем ваш профиль...')

    # Записываем веденный номер телефона в состояние
    await state.update_data(input_number=message.text)

    # Записываем id пользователя
    database['user_id'] = message.from_user.id
    data = await state.get_data()

    await crm_info()

    if await check_crm(data['input_number']) and await checking_number(data['input_number']):

        await message.answer("Вы успешно вошли!")

        if await check_login(message.from_user.id):

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

        await message.answer(
            f"{await get_name_by_id(await search(data['input_number']))}, добро пожаловать, в спортивный клуб!")

        await message.answer("📎Профиль📎", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="История тренировок", callback_data="history_tren"),
                InlineKeyboardButton(text="Кол-во реферальных баллов", callback_data="ref_bonus"),
            ],
            [
                InlineKeyboardButton(text="Абонемент", callback_data="card"),
                InlineKeyboardButton(text="Нормативы", callback_data="normatives")
            ],
            [InlineKeyboardButton(text="Статистика", callback_data="statistics")]
        ]))
    else:
        await message.answer("К сожалению, Вы не являетесь клиентом клуба")
    await state.clear()


@router.callback_query(F.data == "history_tren")
async def callback_history_tren(callback: CallbackQuery) -> None:
    msg = await training_history(database['user_id'])
    await callback.message.edit_text(f"🔗ИСТОРИЯ ТРЕНИРОВОК🔗\n\n %s" % msg,
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "ref_bonus")
async def callback_ref_bonus(callback: CallbackQuery) -> None:
    msg = await number_of_referral_points(database['user_id'])
    await callback.message.edit_text("🔗Реферальные бонусы🔗\n\n%s" % msg,
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "card")
async def callback_card(callback: CallbackQuery) -> None:
    msg = await info_subscription(database['user_id'])
    await callback.message.edit_text(f"🪪АБОНЕМЕНТ🪪\n\n{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "normatives")
async def callback_normatives(callback: CallbackQuery) -> None:
    msg = await get_standards_by_id(database['user_id'])
    await callback.message.edit_text(f"📉АНАЛИЗ НОРМАТИВОВ📉\n\n{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "statistics")
async def callback_statistics(callback: CallbackQuery) -> None:
    await callback.message.edit_text('Выберите год', reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="2024", callback_data="2024")],
            [InlineKeyboardButton(text="2025", callback_data="2025")],
            [InlineKeyboardButton(text="2026", callback_data="2026")],
            [InlineKeyboardButton(text="2027", callback_data="2027")],
            [InlineKeyboardButton(text="2028", callback_data="2028")],
            [InlineKeyboardButton(text="2029", callback_data="2029")],
            [InlineKeyboardButton(text="2030", callback_data="2030")]
        ]
    ))


@router.callback_query(F.data == "2024")
async def callback_2024(callback: CallbackQuery) -> None:
    msg = await get_statistics_by_user(database['user_id'], '2024')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2025")
async def callback_2024(callback: CallbackQuery) -> None:
    msg = await get_statistics_by_user(database['user_id'], '2025')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2026")
async def callback_2024(callback: CallbackQuery) -> None:
    msg = await get_statistics_by_user(database['user_id'], '2026')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2027")
async def callback_2024(callback: CallbackQuery) -> None:
    msg = await get_statistics_by_user(database['user_id'], '2027')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2028")
async def callback_2024(callback: CallbackQuery) -> None:
    msg = await get_statistics_by_user(database['user_id'], '2028')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2029")
async def callback_2024(callback: CallbackQuery) -> None:
    msg = await get_statistics_by_user(database['user_id'], '2029')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2030")
async def callback_2024(callback: CallbackQuery) -> None:
    msg = await get_statistics_by_user(database['user_id'], '2030')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "back_menu")
async def callback_back_menu(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_text("📎Профиль📎", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="История тренировок", callback_data="history_tren"),
            InlineKeyboardButton(text="Кол-во реферальных баллов", callback_data="ref_bonus"),
        ],
        [
            InlineKeyboardButton(text="Абонемент", callback_data="card"),
            InlineKeyboardButton(text="Нормативы", callback_data="normatives")
        ],
        [InlineKeyboardButton(text="Статистика", callback_data="statistics")]
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

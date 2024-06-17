from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)

from auth.signup import check_number
from db.db_users import get_phone_number, get_name, check_login
from db.db_standards import get_standards_by_id
from db.db_profile import training_history, number_of_referral_points, info_subscription

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
                         "Введите номер своего телефона: ")


@router.message(Form.number_login)
async def input_number(message: Message, state: FSMContext) -> None:
    await state.update_data(input_number=message.text)
    database['user_id'] = message.from_user.id
    # user = await get_users()
    data = await state.get_data()
    if check_login(message.from_user.id) and check_number(data['input_number']):
        if get_phone_number(message.from_user.id)[-10:] == data['input_number'][-10:]:
            await message.answer(f"{get_name(message.from_user.id)}, добро пожаловать, в спортивный клуб!")
            await message.answer("📎Профиль📎", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="История тренировок", callback_data="history_tren"),
                    InlineKeyboardButton(text="Кол-во реферальных баллов", callback_data="ref_bonus"),
                ],
                [
                    InlineKeyboardButton(text="Абонемент", callback_data="card"),
                    InlineKeyboardButton(text="Нормативы", callback_data="normatives")
                ]
            ]))
        else:
            await message.answer("Упс...похоже ошибка в веденных данных")
        await state.clear()
    else:
        await message.answer("Вы не зарегестрированы в системе, сначала зарегистрируйтесь")


@router.callback_query(F.data == "history_tren")
async def callback_history_tren(callback: CallbackQuery) -> None:
    msg = training_history(database['user_id'])
    await callback.message.edit_text(f"🔗ИСТОРИЯ ТРЕНИРОВОК🔗\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "ref_bonus")
async def callback_ref_bonus(callback: CallbackQuery) -> None:
    msg = number_of_referral_points(database['user_id'])
    await callback.message.edit_text("🔗Реферальные бонусы🔗\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "card")
async def callback_card(callback: CallbackQuery) -> None:
    msg = info_subscription(database['user_id'])
    await callback.message.edit_text("🪪АБОНЕМЕНТ🪪\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "normatives")
async def callback_normatives(callback: CallbackQuery) -> None:
    msg = get_standards_by_id(database['user_id'])
    await callback.message.edit_text(f"📉АНАЛИЗ НОРМАТИВОВ📉\n\n"
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
        ]
    ]))
    await state.clear()

from aiogram import F, Router
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)

from src.db.db_standards import get_standards_by_id, insert_standard
from src.db.db_profile import (training_history, number_of_referral_points, info_subscription,
                               get_name)
from src.db.db_statistics import get_statistics_by_user
from src.auth.login import login_users

router = Router()


class Form(StatesGroup):
    """
    number_login - state for input number user
    """

    # Profile
    profile = State()


@router.message(Command('profile'))
async def profile(message: Message, state: FSMContext):
    if message.from_user.id in login_users:
        await message.answer(
            f"{await get_name(message.from_user.id)}, добро пожаловать, в спортивный клуб!")

        await state.update_data(user_id=message.from_user.id)

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
        await message.answer("Вы не зарегестрированы, используйте команду - /login")


@router.callback_query(F.data == "history_tren")
async def callback_history_tren(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await training_history(data['user_id'])
    await callback.message.edit_text(f"🔗ИСТОРИЯ ТРЕНИРОВОК🔗\n\n %s" % msg,
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "ref_bonus")
async def callback_ref_bonus(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await number_of_referral_points(data['user_id'])
    await callback.message.edit_text("🔗Реферальные бонусы🔗\n\n%s" % msg,
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "card")
async def callback_card(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await info_subscription(data['user_id'])
    await callback.message.edit_text(f"🪪АБОНЕМЕНТ🪪\n\n{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "normatives")
async def callback_normatives(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await get_standards_by_id(data['user_id'])
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
async def callback_2024(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await get_statistics_by_user(data['user_id'], '2024')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2025")
async def callback_2024(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await get_statistics_by_user(data['user_id'], '2025')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2026")
async def callback_2024(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await get_statistics_by_user(data['user_id'], '2026')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2027")
async def callback_2024(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await get_statistics_by_user(data['user_id'], '2027')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2028")
async def callback_2024(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await get_statistics_by_user(data['user_id'], '2028')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2029")
async def callback_2024(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await get_statistics_by_user(data['user_id'], '2029')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="back_menu")]
                                     ]))


@router.callback_query(F.data == "2030")
async def callback_2024(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    msg = await get_statistics_by_user(data['user_id'], '2030')
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

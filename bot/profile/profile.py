from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)

from db.db_profile import get_telegram_status
from db.db_profile import (training_history, number_of_referral_points, info_subscription,
                               get_name)
from db.db_standards import get_standards_by_id
from db.db_statistics import get_statistics_by_user

from db.db_profile import Session, Profile

router = Router()


class Form(StatesGroup):
    """
    number_login - state for input number user
    """

    # Profile
    profile = State()


@router.callback_query(F.data == "profile")
async def profile(callback: CallbackQuery):

    if await get_telegram_status(callback.message.chat.id):

        await callback.message.edit_text(f"{await get_name(callback.message.chat.id)},"
                                         f" добро пожаловать, в спортивный клуб!\n\n📎Профиль📎",
                                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                             [
                                                 InlineKeyboardButton(text="История тренировок",
                                                                      callback_data="history_tren"),
                                                 InlineKeyboardButton(text="Кол-во реферальных баллов",
                                                                      callback_data="ref_bonus"),
                                             ],
                                             [
                                                 InlineKeyboardButton(text="Абонемент", callback_data="card"),
                                                 InlineKeyboardButton(text="Нормативы", callback_data="normatives")
                                             ],
                                             [InlineKeyboardButton(text="Статистика", callback_data="statistics")],
                                             [InlineKeyboardButton(text="Выйти", callback_data="logout"),
                                              InlineKeyboardButton(text="Назад", callback_data="back")]
                                         ]))
    else:
        await callback.message.edit_text("Вы не зарегестрированы",
                                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                             [InlineKeyboardButton(text="Войти", callback_data="login")],
                                             [InlineKeyboardButton(text="Назад", callback_data="help")]
                                         ]))


@router.callback_query(F.data == "history_tren")
async def callback_history_tren(callback: CallbackQuery) -> None:
    msg = await training_history(callback.message.chat.id)
    await callback.message.edit_text(f"🔗ИСТОРИЯ ТРЕНИРОВОК🔗\n\n %s" % msg,
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
                                     ]))


@router.callback_query(F.data == "ref_bonus")
async def callback_ref_bonus(callback: CallbackQuery) -> None:

    msg = await number_of_referral_points(callback.message.chat.id)
    await callback.message.edit_text("🔗Реферальные бонусы🔗\n\n%s" % msg,
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
                                     ]))


@router.callback_query(F.data == "card")
async def callback_card(callback: CallbackQuery) -> None:
    
    msg = await info_subscription(callback.message.chat.id)
    await callback.message.edit_text(f"🪪АБОНЕМЕНТ🪪\n\n{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
                                     ]))


@router.callback_query(F.data == "normatives")
async def callback_normatives(callback: CallbackQuery) -> None:

    msg = await get_standards_by_id(callback.message.chat.id)
    await callback.message.edit_text(f"📉АНАЛИЗ НОРМАТИВОВ📉\n\n{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
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
            [InlineKeyboardButton(text="2030", callback_data="2030")],
            [InlineKeyboardButton(text="Назад", callback_data='profile')]
        ]
    ))


@router.callback_query(F.data == "logout")
async def logout(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    db_session = Session()
    db_session.query(Profile).filter(Profile.telegram_id == callback.message.chat.id).update({'telegram_status': False})
    db_session.commit()

    await callback.message.edit_text(
        f"Здравствуйте, <i>{get_name(callback.message.chat.id)}</i>, вас приветствует бот спортивного клуба\n\n",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Войти', callback_data='login')],
            [InlineKeyboardButton(text="Помощь", callback_data='help')]
        ]))


@router.callback_query(F.data == "2024")
async def callback_2024(callback: CallbackQuery) -> None:

    msg = await get_statistics_by_user(callback.message.chat.id, '2024')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
                                     ]))


@router.callback_query(F.data == "2025")
async def callback_2024(callback: CallbackQuery) -> None:

    msg = await get_statistics_by_user(callback.message.chat.id, '2025')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
                                     ]))


@router.callback_query(F.data == "2026")
async def callback_2024(callback: CallbackQuery) -> None:
    
    msg = await get_statistics_by_user(callback.message.chat.id, '2026')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
                                     ]))


@router.callback_query(F.data == "2027")
async def callback_2024(callback: CallbackQuery) -> None:

    msg = await get_statistics_by_user(callback.message.chat.id, '2027')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
                                     ]))


@router.callback_query(F.data == "2028")
async def callback_2024(callback: CallbackQuery) -> None:

    msg = await get_statistics_by_user(callback.message.chat.id, '2028')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
                                     ]))


@router.callback_query(F.data == "2029")
async def callback_2024(callback: CallbackQuery) -> None:

    msg = await get_statistics_by_user(callback.message.chat.id, '2029')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
                                     ]))


@router.callback_query(F.data == "2030")
async def callback_2024(callback: CallbackQuery) -> None:
    
    msg = await get_statistics_by_user(callback.message.chat.id, '2030')
    await callback.message.edit_text(f"📊Статистика📊\n\n"
                                     f"{msg}",
                                     reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                         [InlineKeyboardButton(text="Назад в меню", callback_data="profile")]
                                     ]))
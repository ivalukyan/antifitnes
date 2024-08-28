from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, WebAppInfo
from env import Crm
from db.db_profile import Profile
from db.router import Session


router = Router()


@router.callback_query(F.data == "breaktable")
async def schedule(callback: CallbackQuery) -> None:  

    if await check_login(callback.message.chat.id):
        await callback.message.edit_text("<b>ЗАПИСЬ НА ТРЕНИРОВКУ</b>\n\n", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Запись на тренировку', web_app=WebAppInfo(url="https://o770.yclients.com/loyalty"))],
            [InlineKeyboardButton(text="Назад", callback_data="back")]
        ]))
    else:
        await callback.message.edit_text("Вы не зарегестрированы в CRM",
                                        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                        [InlineKeyboardButton(text="Назад", callback_data="help")]
                                        ]))
        

async def check_login(user_id: int) -> bool:
    """Get user login in CRM"""
    db_session = Session()
    res = db_session.query(Profile.telegram_status).filter(Profile.telegram_id == user_id).first()

    if not res:
        return False
    return res

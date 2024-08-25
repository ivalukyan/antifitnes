from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, WebAppInfo)
from env import CRM
from yaclients.yaclients import check_crm
from db.db_profile import crm_eqv

crm = CRM()

router = Router()


@router.callback_query(F.data == "schedule")
async def schedule(callback: CallbackQuery):

    if await check_crm(await crm_eqv(callback.message.chat.id)):
        await callback.message.edit_text("<b>ЗАПИСЬ НА ТРЕНИРОВКУ</b>\n\n", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Запись на тренировку', web_app=WebAppInfo(f"{crm.url_schedule}"))],
            [InlineKeyboardButton(text="Назад", callback_data="back")]
        ]))
    else:
        await callback.message.edit_text("Вы не зарегестрированы в CRM",
                                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                             [InlineKeyboardButton(text="Назад", callback_data="help")]
                                         ]))
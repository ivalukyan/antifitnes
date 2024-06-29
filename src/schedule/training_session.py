from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton,
)
from env import URL_SCHEDULE
from src.srm.srm_bot import check_crm
from src.db.db_profile import crm_eqv

router = Router()


@router.message(Command('schedule'))
async def schedule(message: Message):
    if await check_crm(await crm_eqv(message.from_user.id)):
        await message.answer("<b>ЗАПИСЬ НА ТРЕНИРОВКУ</b>\n\n", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Запись на тренировку', url=f"{URL_SCHEDULE}")]
        ]))
    else:
        await message.answer("Вы не зарегестрированы в CRM")

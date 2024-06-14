from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton,
)

router = Router()


@router.message(Command('schedule'))
async def schedule(message: Message):
    await message.answer("<b>ЗАПИСЬ НА ТРЕНИРОВКУ</b>\n\n", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Запись на тренировку', url="https://n1164665.yclients.com")]
    ]))
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
)

router = Router()


@router.message(Command('schedule'))
async def schedule(message: Message):
    await message.answer("<b>ЗАПИСЬ НА ТРЕНИРОВКУ</b>\n\n"
                         "Данная возможность находиться в разработке...")
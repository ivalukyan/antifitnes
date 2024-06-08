import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)


router = Router()


@router.message(Command('top'))
async def top(message: Message) -> None:
    await message.answer("Выберите норматив: ", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Силовые нормативы", callback_data="power_standards"),
            InlineKeyboardButton(text="Функциональные нормативы", callback_data="fun_standards"),
        ]
    ]), resize_keyboard=True, one_time_keyboard=True)


@router.callback_query(F.data == "power_standards")
async def callback_top(call: CallbackQuery) -> None:
    await call.message.edit_text("📊<i>Силовые нормативы</i>📊", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Гром", callback_data="grom"),
            InlineKeyboardButton(text="Турецкий подъем: Аксель", callback_data="tur_acsel"),
        ],
        [
            InlineKeyboardButton(text="Турецкий подъем: Гиря", callback_data="tur_gir"),
            InlineKeyboardButton(text="Жим лежа 1ПМ", callback_data="bench_press"),
        ],
        [
            InlineKeyboardButton(text="Рывок акселя 1ПМ", callback_data="jerk"),
            InlineKeyboardButton(text="Взятие на грудь акселя 1ПМ", callback_data="jerk_two"),
        ],
        [
            InlineKeyboardButton(text="Ягодичный мостик 1ПМ", callback_data="most"),
            InlineKeyboardButton(text="Становая тяга 1ПМ", callback_data="deadlift"),
        ],
        [
            InlineKeyboardButton(text="Рывок 1ПМ", callback_data="usual_jerk"),
            InlineKeyboardButton(text="Взятие на грудь 1ПМ", callback_data="chest"),
        ],
        [
            InlineKeyboardButton(text="Становая тяга акселя 1ПМ", callback_data="deadlift_jerk"),
            InlineKeyboardButton(text="Присед 1ПМ: Классический", callback_data="squat_classic"),
        ],
        [
            InlineKeyboardButton(text="Присед 1ПМ: Фронтальный", callback_data="squat_front"),
            InlineKeyboardButton(text="Присед 1ПМ: Над головой", callback_data="squat_under_head"),
        ],
        [
            InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")
        ]
    ]))


@router.callback_query(F.data == "fun_standards")
async def callback_functional_standards(call: CallbackQuery) -> None:
    await call.message.edit_text("📊<i>Функциональные нормативы</i>📊", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Скакалка", callback_data="skipping_rope"),
            InlineKeyboardButton(text="Отжимания от пола", callback_data="push_ups"),
        ],
        [
            InlineKeyboardButton(text="Челночный бег", callback_data="shuttle_running"),
            InlineKeyboardButton(text="Прогулка фермера", callback_data="farmer_walk"),
        ],
        [
            InlineKeyboardButton(text="Подтягивания", callback_data="pull_ups"),
            InlineKeyboardButton(text="Прыжок в высоту", callback_data="high_jump"),
        ],
        [
            InlineKeyboardButton(text="Прыжок в длину", callback_data="long_jump"),
            InlineKeyboardButton(text="Удержание акселя", callback_data="holding_axel"),
        ],
        [
            InlineKeyboardButton(text="Стойка на руках", callback_data="handstand"),
            InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")
        ]
    ]))


@router.callback_query(F.data == 'back_norm')
async def back_callback(call: CallbackQuery):
    await call.message.edit_text("Выберите норматив: ", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Силовые нормативы", callback_data="power_standards"),
            InlineKeyboardButton(text="Функциональные нормативы", callback_data="fun_standards")
        ]
    ]))

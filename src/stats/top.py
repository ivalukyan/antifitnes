from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)
from src.db.db_standards import (get_all_thunder, get_all_pull_ups, get_all_jerk, get_all_holding_the_axel,
                                 get_all_taking_on_axel_chest, get_all_axel_jerk, get_all_taking_on_the_chest,
                                 get_all_deadlift, get_all_axel_deadlift, get_all_handstand, get_all_turkish_ascent_axel,
                                 get_all_push_ups, get_all_high_jump, get_all_long_jump, get_all_bench_press,
                                 get_all_turkish_ascent_kettlebell, get_all_farmer_walk,
                                 get_all_front_squat, get_all_classic_squat, get_all_squat_over_the_head,
                                 get_all_gluteal_bridge, get_all_skipping_rope, get_all_shuttle_running)

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
    await call.message.edit_text("📊<i>Функциональные нормативы</i>📊",
                                 reply_markup=InlineKeyboardMarkup(inline_keyboard=[
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


@router.callback_query(F.data == "grom")
async def grom_callback(call: CallbackQuery):
    msg = await get_all_thunder()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "tur_acsel")
async def tur_acsel_callback(call: CallbackQuery):
    msg = await get_all_turkish_ascent_axel()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "tur_gir")
async def tur_gir_callback(call: CallbackQuery):
    msg = await get_all_turkish_ascent_kettlebell()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "bench_press")
async def bench_press_callback(call: CallbackQuery):
    msg = await get_all_bench_press()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "jerk")
async def jerk_callback(call: CallbackQuery):
    msg = await get_all_axel_jerk()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "jerk_two")
async def jerk_two_callback(call: CallbackQuery):
    msg = await get_all_taking_on_axel_chest()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "most")
async def most_callback(call: CallbackQuery):
    msg = await get_all_gluteal_bridge()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "deadlift")
async def deadlift_callback(call: CallbackQuery):
    msg = await get_all_deadlift()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "usual_jerk")
async def usual_jerk_callback(call: CallbackQuery):
    msg = await get_all_jerk()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "chest")
async def chest_callback(call: CallbackQuery):
    msg = await get_all_taking_on_the_chest()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "deadlift_jerk")
async def deadlift_jerk_callback(call: CallbackQuery):
    msg = await get_all_axel_deadlift()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "squat_classic")
async def squat_classic_callback(call: CallbackQuery):
    msg = await get_all_classic_squat()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "squat_front")
async def squat_under_head_callback(call: CallbackQuery):
    msg = await get_all_front_squat()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "squat_under_head")
async def squat_under_head_callback(call: CallbackQuery):
    msg = await get_all_squat_over_the_head()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "skipping_rope")
async def skipping_rope_callback(call: CallbackQuery):
    msg = await get_all_skipping_rope()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "push_ups")
async def push_up_callback(call: CallbackQuery):
    msg = await get_all_push_ups()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "shuttle_running")
async def shuttle_running_callback(call: CallbackQuery):
    msg = await get_all_shuttle_running()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "farmer_walk")
async def farmer_walk_callback(call: CallbackQuery):
    msg = await get_all_farmer_walk()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "pull_ups")
async def pull_up_callback(call: CallbackQuery):
    msg = await get_all_pull_ups()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "high_jump")
async def high_jump_callback(call: CallbackQuery):
    msg = await get_all_high_jump()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "long_jump")
async def long_jump_callback(call: CallbackQuery):
    msg = await get_all_long_jump()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "holding_axel")
async def holding_axel_callback(call: CallbackQuery):
    msg = await get_all_holding_the_axel()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))


@router.callback_query(F.data == "handstand")
async def handstand_callback(call: CallbackQuery):
    msg = await get_all_handstand()
    await call.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_norm")]
    ]))

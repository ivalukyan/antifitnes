import asyncio
from db.router import cursor, conn


async def get_standards_by_id(user_id):
    cursor.execute("""SELECT * FROM sport_bot_standards WHERE id=%s""", (user_id,))
    result = cursor.fetchall()[0]

    conn.commit()

    msg = (f"Гром - {result[1]}\n"
           f"Турецкий подъем: Аксель - {result[2]}\n"
           f"Турецкий подъем: Гиря - {result[3]}\n"
           f"Жим лежа 1ПМ - {result[4]}\n"
           f"Рывок акселя 1ПМ - {result[5]}\n"
           f"Взятие на грудь акселя 1ПМ - {result[6]}\n"
           f"Ягодичный мостик 1ПМ - {result[7]}\n"
           f"Становая тяга 1ПМ - {result[8]}\n"
           f"Рывок 1ПМ - {result[9]}\n"
           f"Взятие на грудь 1ПМ - {result[10]}\n"
           f"Становая тяга акселя 1ПМ - {result[11]}\n"
           f"Присед 1ПМ: Классический - {result[12]}\n"
           f"Присед 1ПМ: Фронтальный - {result[13]}\n"
           f"Присед 1ПМ: Над головой - {result[14]}\n"
           f"Скакалка - {result[15]}\n"
           f"Отжимания от пола - {result[16]}\n"
           f"Челночный бег - {result[17]}\n"
           f"Прогулка фермера - {result[18]}\n"
           f"Подтягивания - {result[19]}\n"
           f"Прыжок в высоту - {result[20]}\n"
           f"Прыжок в длину - {result[21]}\n"
           f"Удержание акселя - {result[22]}\n"
           f"Стойка на руках - {result[23]}\n")

    if result is not None:
        return msg
    else:
        raise ValueError("No standard for user id {}".format(user_id))


async def get_all_thunder():
    cursor.execute("""SELECT thunder FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊ГРОМ📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_turkish_ascent_axel():
    cursor.execute("""SELECT turkish_ascent_axel FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Турецкий подъем: Аксель📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_turkish_ascent_kettlebell():
    cursor.execute("""SELECT turkish_ascent_kettlebell FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Турецкий подъем: Гиря📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_bench_press():
    cursor.execute("""SELECT bench_press FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Жим лежа📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_axel_jerk():
    cursor.execute("""SELECT axel_jerk FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Рывок акселя 1ПМ📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_taking_on_axel_chest():
    cursor.execute("""SELECT taking_on_axel_chest FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Взятие на грудь акселя 1ПМ📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_gluteal_bridge():
    cursor.execute("""SELECT gluteal_bridge FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Ягодичный мостик 1ПМ📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_deadlift():
    cursor.execute("""SELECT deadlift FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Становая тяга 1ПМ📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_jerk():
    cursor.execute("""SELECT jerk FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Рывок 1ПМ📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_taking_on_the_chest():
    cursor.execute("""SELECT taking_on_the_chest FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Взятие на грудь 1ПМ📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_axel_deadlift():
    cursor.execute("""SELECT axel_deadlift FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Становая тяга акселя 1ПМ📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_classic_squat():
    cursor.execute("""SELECT classic_squat FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Присед 1ПМ: Классический📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_front_squat():
    cursor.execute("""SELECT front_squat FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Присед 1ПМ: Фронтальный📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_squat_over_the_head():
    cursor.execute("""SELECT squat_over_the_head FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Присед 1ПМ: Над головой📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_skipping_rope():
    cursor.execute("""SELECT skipping_rope FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Скакалка📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_push_ups():
    cursor.execute("""SELECT push_ups FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Отжимания от пола📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_shuttle_running():
    cursor.execute("""SELECT shuttle_running FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Челночный бег📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_farmer_walk():
    cursor.execute("""SELECT farmer_walk FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Прогулка фермера📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_pull_ups():
    cursor.execute("""SELECT pull_ups FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Подтягивания📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_high_jump():
    cursor.execute("""SELECT high_jump FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Прыжок в высоту📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_long_jump():
    cursor.execute("""SELECT long_jump FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Прыжок в длину📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_holding_the_axel():
    cursor.execute("""SELECT holding_the_axel FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Удержание акселя📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"


async def get_all_handstand():
    cursor.execute("""SELECT handstand FROM sport_bot_standards""")
    result = cursor.fetchall()[0]
    print(result)

    for _ in result:
        _ = int(_)

    sorted(result)

    if result is not None and len(result) > 9:
        msg = (f"📊Стойка на руках📊\n\n"
               f"1. {result[0]}\n"
               f"2. {result[1]}\n"
               f"3. {result[2]}\n"
               f"4. {result[3]}\n"
               f"5. {result[4]}\n"
               f"6. {result[5]}\n"
               f"7. {result[6]}\n"
               f"8. {result[7]}\n"
               f"9. {result[8]}\n"
               f"10. {result[9]}")
        return msg
    else:
        return "Количество заполненных нормативов меньше 10"

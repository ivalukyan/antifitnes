import asyncio

from db.router import cursor, conn


async def insert_standard(user_id, first_name):
    cursor.execute("""INSERT INTO bot_app_standards(telegram_id, first_name,thunder, turkish_ascent_axel, turkish_ascent_kettlebell,
     bench_press, axel_jerk, taking_on_axel_chest, gluteal_bridge, deadlift, jerk, taking_on_the_chest, axel_deadlift,
      classic_squat, front_squat, squat_over_the_head, skipping_rope, push_ups, shuttle_running, farmer_walk, pull_ups,
       high_jump, long_jump, holding_the_axel, handstand) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)""",
                   (user_id, first_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0))
    conn.commit()


async def get_names_standards(name):
    cursor.execute("SELECT first_name FROM bot_app_standards WHERE first_name=%s", (name,))
    rows = cursor.fetchall()

    result = []

    if len(result) != 0:
        for _ in range(len(rows)):
            result.append(rows[_][0])

        print(result)
        return result


async def get_standards_by_id(user_id):
    cursor.execute("""SELECT * FROM bot_app_standards WHERE telegram_id=%s""", (user_id,))
    result = cursor.fetchall()

    if result is not None and len(result) != 0:
        result = result[0]
        conn.commit()

        msg = (f"Гром - {result[3]}\n"
               f"Турецкий подъем: Аксель - {result[4]}\n"
               f"Турецкий подъем: Гиря - {result[5]}\n"
               f"Жим лежа 1ПМ - {result[6]}\n"
               f"Рывок акселя 1ПМ - {result[7]}\n"
               f"Взятие на грудь акселя 1ПМ - {result[8]}\n"
               f"Ягодичный мостик 1ПМ - {result[9]}\n"
               f"Становая тяга 1ПМ - {result[10]}\n"
               f"Рывок 1ПМ - {result[11]}\n"
               f"Взятие на грудь 1ПМ - {result[12]}\n"
               f"Становая тяга акселя 1ПМ - {result[13]}\n"
               f"Присед 1ПМ: Классический - {result[14]}\n"
               f"Присед 1ПМ: Фронтальный - {result[15]}\n"
               f"Присед 1ПМ: Над головой - {result[16]}\n"
               f"Скакалка - {result[17]}\n"
               f"Отжимания от пола - {result[18]}\n"
               f"Челночный бег - {result[19]}\n"
               f"Прогулка фермера - {result[20]}\n"
               f"Подтягивания - {result[21]}\n"
               f"Прыжок в высоту - {result[22]}\n"
               f"Прыжок в длину - {result[23]}\n"
               f"Удержание акселя - {result[24]}\n"
               f"Стойка на руках - {result[25]}\n")

        if result is not None:
            return msg
        else:
            raise ValueError("No standard for user id {}".format(user_id))
    else:
        msg = "У данного пользователя нет нормативов"
        return msg


async def get_all_thunder():
    cursor.execute("""SELECT thunder, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = f"📊ГРОМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_turkish_ascent_axel():
    cursor.execute("""SELECT turkish_ascent_axel, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Турецкий подъем: Аксель📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_turkish_ascent_kettlebell():
    cursor.execute("""SELECT turkish_ascent_kettlebell, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Турецкий подъем: Гиря📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_bench_press():
    cursor.execute("""SELECT bench_press, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Жим лежа📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_axel_jerk():
    cursor.execute("""SELECT axel_jerk, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Рывок акселя 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_taking_on_axel_chest():
    cursor.execute("""SELECT taking_on_axel_chest, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = f"📊Взятие на грудь акселя 1ПМ📊\n\n"
    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_gluteal_bridge():
    cursor.execute("""SELECT gluteal_bridge, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Ягодичный мостик 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_deadlift():
    cursor.execute("""SELECT deadlift, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Становая тяга 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_jerk():
    cursor.execute("""SELECT jerk, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Рывок 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_taking_on_the_chest():
    cursor.execute("""SELECT taking_on_the_chest, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Взятие на грудь 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_axel_deadlift():
    cursor.execute("""SELECT axel_deadlift, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Становая тяга акселя 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_classic_squat():
    cursor.execute("""SELECT classic_squat, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Присед 1ПМ: Классический📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_front_squat():
    cursor.execute("""SELECT front_squat, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Присед 1ПМ: Фронтальный📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_squat_over_the_head():
    cursor.execute("""SELECT squat_over_the_head, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Присед 1ПМ: Над головой📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_skipping_rope():
    cursor.execute("""SELECT skipping_rope, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Скакалка📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_push_ups():
    cursor.execute("""SELECT push_ups, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Отжимания от пола📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_shuttle_running():
    cursor.execute("""SELECT shuttle_running, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Челночный бег📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_farmer_walk():
    cursor.execute("""SELECT farmer_walk, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Прогулка фермера📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_pull_ups():
    cursor.execute("""SELECT pull_ups, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Подтягивания📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_high_jump():
    cursor.execute("""SELECT high_jump, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Прыжок в высоту📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_long_jump():
    cursor.execute("""SELECT long_jump, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = (f"📊Прыжок в длину📊\n\n")

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_holding_the_axel():
    cursor.execute("""SELECT holding_the_axel, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Удержание акселя📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_handstand():
    cursor.execute("""SELECT handstand, first_name FROM bot_app_standards""")
    result = cursor.fetchall()

    msg = "📊Стойка на руках📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(result)):
        standards[_] = result[_][0]
        names[_] = result[_][1]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if result is not None and len(result) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"

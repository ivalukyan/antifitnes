from src.db.router import cursor, conn


async def insert_standard(user_id, first_name):
    cursor.execute("""INSERT INTO bot_app_standards(telegram_id, first_name,thunder, turkish_ascent_axel, turkish_ascent_kettlebell,
     bench_press, axel_jerk, taking_on_axel_chest, gluteal_bridge, deadlift, jerk, taking_on_the_chest, axel_deadlift,
      classic_squat, front_squat, squat_over_the_head, skipping_rope, push_ups, shuttle_running, farmer_walk, pull_ups,
       high_jump, long_jump, holding_the_axel, handstand) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)""", (user_id, first_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
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
    cursor.execute("""SELECT thunder FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = f"📊ГРОМ📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_turkish_ascent_axel():
    cursor.execute("""SELECT turkish_ascent_axel FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Турецкий подъем: Аксель📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_turkish_ascent_kettlebell():
    cursor.execute("""SELECT turkish_ascent_kettlebell FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Турецкий подъем: Гиря📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_bench_press():
    cursor.execute("""SELECT bench_press FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Жим лежа📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_axel_jerk():
    cursor.execute("""SELECT axel_jerk FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Рывок акселя 1ПМ📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_taking_on_axel_chest():
    cursor.execute("""SELECT taking_on_axel_chest FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = f"📊Взятие на грудь акселя 1ПМ📊\n\n"
    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_gluteal_bridge():
    cursor.execute("""SELECT gluteal_bridge FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Ягодичный мостик 1ПМ📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_deadlift():
    cursor.execute("""SELECT deadlift FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Становая тяга 1ПМ📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_jerk():
    cursor.execute("""SELECT jerk FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Рывок 1ПМ📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_taking_on_the_chest():
    cursor.execute("""SELECT taking_on_the_chest FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Взятие на грудь 1ПМ📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_axel_deadlift():
    cursor.execute("""SELECT axel_deadlift FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Становая тяга акселя 1ПМ📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_classic_squat():
    cursor.execute("""SELECT classic_squat FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Присед 1ПМ: Классический📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_front_squat():
    cursor.execute("""SELECT front_squat FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Присед 1ПМ: Фронтальный📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_squat_over_the_head():
    cursor.execute("""SELECT squat_over_the_head FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Присед 1ПМ: Над головой📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_skipping_rope():
    cursor.execute("""SELECT skipping_rope FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Скакалка📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_push_ups():
    cursor.execute("""SELECT push_ups FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Отжимания от пола📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_shuttle_running():
    cursor.execute("""SELECT shuttle_running FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Челночный бег📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_farmer_walk():
    cursor.execute("""SELECT farmer_walk FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Прогулка фермера📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_pull_ups():
    cursor.execute("""SELECT pull_ups FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Подтягивания📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_high_jump():
    cursor.execute("""SELECT high_jump FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Прыжок в высоту📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_long_jump():
    cursor.execute("""SELECT long_jump FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = (f"📊Прыжок в длину📊\n\n")

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_holding_the_axel():
    cursor.execute("""SELECT holding_the_axel FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Удержание акселя📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_handstand():
    cursor.execute("""SELECT handstand FROM bot_app_standards""")
    result = cursor.fetchall()[0]

    msg = "📊Стойка на руках📊\n\n"

    if result is not None and len(result) > 0:
        for _ in range(len(result)):
            msg += f'{_ + 1}. {result[_]}\n'

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"

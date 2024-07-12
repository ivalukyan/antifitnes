from src.db.router import cursor, conn


async def training_history(user_id: int):
    cursor.execute("""SELECT training_history FROM bot_app_profile WHERE telegram_id =%s""", (user_id, ))
    result = cursor.fetchone()[0]
    if result is not None:
        return result
    else:
        return "История тренировок отсутствует"


async def number_of_referral_points(user_id: int):
    cursor.execute("""SELECT number_of_referral_points FROM bot_app_profile WHERE telegram_id =%s""", (user_id, ))
    result = cursor.fetchone()[0]

    if result is not None:
        return result
    else:
        return None


async def info_subscription(user_id: int):
    cursor.execute("""SELECT info_subscription FROM bot_app_profile WHERE telegram_id =%s""", (user_id, ))
    result = cursor.fetchone()[0]

    if result is not None:
        return result
    else:
        return None


async def add_info_profile(user_id, first_name, username, gender, phone_number, training_history,
                           number_of_referral_points, info_subscription, current_standard):
    cursor.execute("""INSERT INTO bot_app_profile(telegram_id, first_name, username, gender, phone_number, training_history, 
    number_of_referral_points, info_subscription, current_standard) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (user_id, first_name, username, gender, phone_number,
                                                     training_history, number_of_referral_points, info_subscription,
                                                     current_standard, ))

    conn.commit()


async def get_name(user_id):
    cursor.execute("""SELECT first_name FROM bot_app_profile WHERE telegram_id = %s""", (user_id,))
    result = cursor.fetchone()[0]
    if result is not None:
        return result
    else:
        raise ValueError("No name")


async def check_login(user_id: int):
    cursor.execute("""SELECT telegram_id FROM bot_app_profile""")
    result = cursor.fetchall()
    res = []
    for i in range(len(result)):
        res.append(result[i][0])
    if user_id in res:
        return False
    else:
        return True


async def get_all_users():
    cursor.execute("""SELECT telegram_id FROM bot_app_profile""")
    result = cursor.fetchall()
    res = []
    for i in range(len(result)):
        res.append(result[i][0])

    return res


async def crm_eqv(user_id):
    if user_id in await get_all_users():
        cursor.execute("""SELECT phone_number FROM bot_app_profile WHERE telegram_id = %s""", (user_id, ))
        result = cursor.fetchone()[0]

        return result
    return None

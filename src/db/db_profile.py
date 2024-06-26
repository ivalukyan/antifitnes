from src.db.router import cursor, conn


async def training_history(user_id: int):
    cursor.execute("""SELECT training_history FROM app_bot_profile WHERE id =%s""", (user_id, ))
    result = cursor.fetchone()[0]
    if result is not None:
        return result
    else:
        return "История тренировок отсутствует"


async def number_of_referral_points(user_id: int):
    cursor.execute("""SELECT number_of_referral_points FROM app_bot_profile WHERE id =%s""", (user_id, ))
    result = cursor.fetchone()[0]

    if result is not None:
        return result
    else:
        return None


async def info_subscription(user_id: int):
    cursor.execute("""SELECT info_subscription FROM app_bot_profile WHERE id =%s""", (user_id, ))
    result = cursor.fetchone()[0]

    if result is not None:
        return result
    else:
        return None


async def add_info_profile(user_id, training_history, number_of_referral_points, info_subscription, current_standard):
    cursor.execute("""INSERT INTO app_bot_profile(id, training_history, number_of_referral_points, info_subscription, current_standard) 
    VALUES (%s, %s, %s, %s, %s)""", (user_id, training_history, number_of_referral_points, info_subscription,
                                     current_standard, ))

    conn.commit()

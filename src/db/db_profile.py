import psycopg2

from env import POSTGRES_DB, POSTGRES_USER, POSTGRES_HOST, POSTGRES_PASSWORD
from src.db.router import cursor, conn


async def training_history(user_id: int):
    cursor.execute("""SELECT training_history FROM bot_app_profile WHERE telegram_id =%s""", (user_id,))
    result = cursor.fetchone()[0]
    if result is not None:
        return result
    else:
        return "История тренировок отсутствует"


async def number_of_referral_points(user_id: int):
    cursor.execute("""SELECT number_of_referral_points FROM bot_app_profile WHERE telegram_id =%s""", (user_id,))
    result = cursor.fetchone()[0]

    if result is not None:
        return result
    else:
        return None


async def info_subscription(user_id: int):
    cursor.execute("""SELECT info_subscription FROM bot_app_profile WHERE telegram_id =%s""", (user_id,))
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
                                                     current_standard,))

    conn.commit()


async def get_name(user_id):
    cursor.execute("""SELECT first_name FROM bot_app_profile WHERE telegram_id = %s""", (user_id,))
    result = cursor.fetchone()
    if result is not None:
        return result[0]
    else:
        raise ValueError("No name")


async def check_login(user_id: int):
    cursor.execute("""SELECT telegram_id FROM bot_app_profile""")
    result = cursor.fetchall()
    res = []
    if result is not None:
        for i in range(len(result)):
            res.append(result[i][0])
        if user_id in res:
            return False
        else:
            return True
    else:
        return True


async def get_all_users():
    cursor.execute("""SELECT telegram_id FROM bot_app_profile""")
    result = cursor.fetchall()
    res = []
    if result is not None:
        for i in range(len(result)):
            res.append(result[i][0])

        return res


async def crm_eqv(user_id):
    if user_id in await get_all_users():
        cursor.execute("""SELECT phone_number FROM bot_app_profile WHERE telegram_id = %s""", (user_id,))
        result = cursor.fetchone()

        return result[0]
    return None


async def update_profile(telegram_id: int, telegram_status: bool, username: str, training_history: str,
                         number_of_referral_points: int, info_subscription: str, current_standard: str,
                         phone_number: str):
    cursor.execute("""UPDATE bot_app_profile SET telegram_id = %s, telegram_status = %s, username = %s,
     training_history = %s, number_of_referral_points = %s, info_subscription = %s, current_standard = %s 
     WHERE phone_number= %s""", (telegram_id, telegram_status, username, training_history, number_of_referral_points,
                                 info_subscription, current_standard, phone_number,))
    conn.commit()


async def get_telegram_status(user_id) -> bool:
    cursor.execute("""SELECT telegram_status FROM bot_app_profile WHERE telegram_id = %s""", (user_id,))
    result = cursor.fetchone()
    if result is not None:
        return result[0]
    else:
        return False


async def get_all_phones(phone_number: str) -> bool:
    cursor.execute("""SELECT phone_number FROM bot_app_profile""")
    result = cursor.fetchall()
    if result is not None:
        print(result[0])
        if phone_number in result[0]:
            return True
        else:
            return False

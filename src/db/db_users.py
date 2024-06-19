from src.db.router import cursor, conn


async def create_users():
    cursor.execute("""CREATE TABLE IF NOT EXISTS app_bot_user(
                ID SERIAL PRIMARY KEY,
                FIRST_NAME TEXT NOT NULL,
                USERNAME TEXT,
                GENDER TEXT NOT NULL,
                PHONE_NUMBER VARCHAR(12),
                CURRENT_STANDARD TEXT);
            """)

    conn.commit()


async def get_phone_number(user_id):
    cursor.execute("""SELECT phone_number FROM app_bot_user WHERE id = %s""", (user_id,))
    result = cursor.fetchone()[0]
    if result is not None:
        return result
    else:
        raise ValueError("No phone number found")


async def get_name(user_id):
    cursor.execute("""SELECT first_name FROM app_bot_user WHERE id = %s""", (user_id,))
    result = cursor.fetchone()[0]
    if result is not None:
        return result
    else:
        raise ValueError("No name")


async def check_login(user_id: int):
    cursor.execute("""SELECT id FROM app_bot_user""")
    result = cursor.fetchall()
    res = []
    for i in range(len(result)):
        res.append(result[i][0])
    if user_id in res:
        return True
    else:
        return False


async def get_all_users():
    cursor.execute("""SELECT id FROM app_bot_user""")
    result = cursor.fetchall()
    res = []
    for i in range(len(result)):
        res.append(result[i][0])

    return res


async def get_current_standards(user_id):
    cursor.execute("""SELECT current_standard FROM app_bot_user WHERE id = %s""", (user_id,))
    result = cursor.fetchone()

    try:
        if result is not None:
            return result[0]
    except TypeError:
        raise TypeError("No result found")


async def add_user(user_id, first_name, username, gender, phone_number):
    cursor.execute("""INSERT INTO app_bot_user(id, first_name, username, gender, phone_number) 
    VALUES (%s, %s, %s, %s, %s)""", (user_id, first_name, username, gender, phone_number, ))

    conn.commit()

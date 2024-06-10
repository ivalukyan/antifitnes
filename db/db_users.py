from db.router import cursor, conn


def create_users():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                ID SERIAL PRIMARY KEY,
                FIRST_NAME TEXT NOT NULL,
                USERNAMES TEXT,
                GENDER TEXT NOT NULL,
                PHONE_NUMBER VARCHAR(12),
                CURRENT_STANDARD TEXT);
            """)

    conn.commit()


def insert_users(id, first_name, username, gender, phone_number):
    cursor.execute(
        """INSERT INTO users(ID, FIRST_NAME, USERNAMES, GENDER, PHONE_NUMBER, CURRENT_STANDARD) VALUES (%s, %s, %s, 
        %s, %s, %s)""",
        (id, first_name, username, gender, phone_number, None,))

    conn.commit()


def update_users_name(id, first_name):
    cursor.execute("""UPDATE users SET first_name = %s WHERE id = %s""", (first_name, id,))
    conn.commit()


def update_user_phone_number(id, phone_number):
    cursor.execute("""UPDATE users SET phone_number = %s WHERE id = %s""", (phone_number, id,))
    conn.commit()


def get_phone_number(id):
    cursor.execute("""SELECT phone_number FROM users WHERE id = %s""", (id,))
    result = cursor.fetchone()[0]
    if result is not None:
        return result
    else:
        return None


def get_name(id):
    cursor.execute("""SELECT first_name FROM users WHERE id = %s""", (id,))
    result = cursor.fetchone()[0]
    if result is not None:
        return result
    else:
        return None


def check_login(id):
    cursor.execute("""SELECT id FROM users""")
    result = cursor.fetchall()
    res = []
    for i in range(len(result)):
        res.append(result[i][0])
    if id in res:
        return True
    else:
        return False


def get_all_users():
    cursor.execute("""SELECT id FROM users""")
    result = cursor.fetchall()
    res = []
    for i in range(len(result)):
        res.append(result[i][0])

    return res


def get_current_standards(id):
    cursor.execute("""SELECT current_standard FROM users WHERE id = %s""", (id,))
    result = cursor.fetchone()

    try:
        if result is not None:
            return result[0]
    except TypeError:
        raise TypeError("No result found")

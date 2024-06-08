from router import cursor, conn


def add_users(id, first_name, username, gender, phone_number):
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                ID SERIAL PRIMARY KEY,
                FIRST_NAME TEXT NOT NULL,
                USERNAME TEXT NOT NULL,
                GENDER TEXT NOT NULL,
                PHONE_NUMBER VARCHAR(12);
            """)

    conn.commit()

    cursor.execute("""INSERT INTO users (ID, FIRST_NAME, USERNAME, GENDER, PHONE_NUMBER) VALUES (%s, %s, %s, %s, %s)""",
                   (id, first_name, username, gender, phone_number))

    conn.commit()
    cursor.close()
    conn.close()


def update_users_name(id, first_name):
    cursor.execute("""UPDATE users SET first_name = %s WHERE id = %s""", (first_name, id))
    conn.commit()


def update_user_phone_number(id, phone_number):
    cursor.execute("""UPDATE users SET phone_number = %s WHERE id = %s""", (phone_number, id))
    conn.commit()


def get_phone_number(id):
    cursor.execute("""SELECT phone_number FROM users WHERE id = %s"""(id,))
    result = cursor.fetchone()
    return result

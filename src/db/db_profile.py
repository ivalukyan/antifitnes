from src.db.router import cursor


async def training_history(user_id: int):
    cursor.execute("""SELECT training_history FROM sport_bot_profile WHERE id =%s""", (user_id, ))
    result = cursor.fetchone()[0]

    if result is not None:
        return result
    else:
        raise ValueError("No training history")


async def number_of_referral_points(user_id: int):
    cursor.execute("""SELECT number_of_referral_points FROM sport_bot_profile WHERE id =%s""", (user_id, ))
    result = cursor.fetchone()[0]

    if result is not None:
        return result
    else:
        raise ValueError("No referral points")


async def info_subscription(user_id: int):
    cursor.execute("""SELECT info_subscription FROM sport_bot_profile WHERE id =%s""", (user_id, ))
    result = cursor.fetchone()[0]

    if result is not None:
        return result
    else:
        raise ValueError("No info subscription")




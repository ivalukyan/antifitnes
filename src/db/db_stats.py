import datetime
import uuid

import psycopg2.extras

from src.db.router import cursor, conn


def definition_month(month):
    if month in ['1', '2', '3']:
        return '1'
    elif month in ['4', '5', '6']:
        return '4'
    elif month in ['7', '8', '9']:
        return '7'
    elif month in ['10', '11', '12']:
        return '10'


async def insert_stats(user_id, user_name):
    dynamic_year = datetime.datetime.now().year
    dynamic_month = str(datetime.datetime.now().month)

    cursor.execute("""INSERT INTO bot_app_statistics(user_id, user_name, thunder, turkish_ascent_axel, turkish_ascent_kettlebell,
     bench_press, axel_jerk, taking_on_axel_chest, gluteal_bridge, deadlift, jerk, taking_on_the_chest, axel_deadlift,
      classic_squat, front_squat, squat_over_the_head, skipping_rope, push_ups, shuttle_running, farmer_walk, pull_ups,
       high_jump, long_jump, holding_the_axel, handstand, month, year) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, 
       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                   (user_id, user_name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    definition_month(dynamic_month), dynamic_year))
    conn.commit()

from db.router import Base, Session, engine
from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime, UUID, Boolean, BIGINT, Text, Float
from datetime import datetime


class Statistics(Base):

    dynamic_month = datetime.now().month
    dynamic_year = datetime.now().year

    __tablename__ = "bot_app_statistics"
    id = Column(UUID, primary_key=True, default=uuid4)
    user_id = Column(BIGINT, nullable=True)
    user_name = Column(Text, nullable=True)
    thunder = Column(Float, nullable=True, default=0)
    turkish_ascent_axel = Column(Float, nullable=True, default=0)
    turkish_ascent_kettlebell = Column(Float, nullable=True, default=0)
    bench_press = Column(Float, nullable=True, default=0)
    axel_jerk = Column(Float, nullable=True, default=0)
    taking_on_axel_chest = Column(Float, nullable=True, default=0)
    gluteal_bridge = Column(Float, nullable=True, default=0)
    deadlift = Column(Float, nullable=True, default=0)
    jerk = Column(Float, nullable=True, default=0)
    taking_on_the_chest = Column(Float, nullable=True, default=0)
    axel_deadlift = Column(Float, nullable=True, default=0)
    classic_squat = Column(Float, nullable=True, default=0)
    front_squat = Column(Float, nullable=True, default=0)
    squat_over_the_head = Column(Float, nullable=True, default=0)
    skipping_rope = Column(Float, nullable=True, default=0)
    push_ups = Column(Float, nullable=True, default=0)
    shuttle_running = Column(Float, nullable=True, default=0)
    farmer_walk = Column(Float, nullable=True, default=0)
    pull_ups = Column(Float, nullable=True, default=0)
    high_jump = Column(Float, nullable=True, default=0)
    long_jump = Column(Float, nullable=True, default=0)
    holding_the_axel = Column(Float, nullable=True, default=0)
    handstand = Column(Float, nullable=True, default=0)
    month = Column(Text, nullable=True, default=dynamic_month)
    year = Column(Text, nullable=True, default=dynamic_year)


async def get_statistics_by_user(user_id, year_id):
    """Get user statistics"""
    db_session = Session()
    result = db_session.query(Statistics).filter(Statistics.user_id == user_id and Statistics.year == year_id).all()

    message = ""
    if result is not None:
        for _ in result:
            if _[26] == '1':
                msg = (f"🤸‍♂️<b>Статистика за Январь</b>🤸‍♂️\n\n"
                       f"Гром - {_[3]}\n"
                       f"Турецкий подъем: Аксель - {_[4]}\n"
                       f"Турецкий подъем: Гиря - {_[5]}\n"
                       f"Жим лежа 1ПМ - {_[6]}\n"
                       f"Рывок акселя 1ПМ - {_[7]}\n"
                       f"Взятие на грудь акселя 1ПМ - {_[8]}\n"
                       f"Ягодичный мостик 1ПМ - {_[9]}\n"
                       f"Становая тяга 1ПМ - {_[10]}\n"
                       f"Рывок 1ПМ - {_[11]}\n"
                       f"Взятие на грудь 1ПМ - {_[12]}\n"
                       f"Становая тяга акселя 1ПМ - {_[13]}\n"
                       f"Присед 1ПМ: Классический - {_[14]}\n"
                       f"Присед 1ПМ: Фронтальный - {_[15]}\n"
                       f"Присед 1ПМ: Над головой - {_[16]}\n"
                       f"Скакалка - {_[17]}\n"
                       f"Отжимания от пола - {_[18]}\n"
                       f"Челночный бег - {_[19]}\n"
                       f"Прогулка фермера - {_[20]}\n"
                       f"Подтягивания - {_[21]}\n"
                       f"Прыжок в высоту - {_[22]}\n"
                       f"Прыжок в длину - {_[23]}\n"
                       f"Удержание акселя - {_[24]}\n"
                       f"Стойка на руках - {_[25]}\n")

                message += msg + "\n\n"

            elif _[26] == '4':
                msg = (f"🏅<b>Статистика за Апрель</b>🏅\n\n"
                       f"Гром - {_[3]}\n"
                       f"Турецкий подъем: Аксель - {_[4]}\n"
                       f"Турецкий подъем: Гиря - {_[5]}\n"
                       f"Жим лежа 1ПМ - {_[6]}\n"
                       f"Рывок акселя 1ПМ - {_[7]}\n"
                       f"Взятие на грудь акселя 1ПМ - {_[8]}\n"
                       f"Ягодичный мостик 1ПМ - {_[9]}\n"
                       f"Становая тяга 1ПМ - {_[10]}\n"
                       f"Рывок 1ПМ - {_[11]}\n"
                       f"Взятие на грудь 1ПМ - {_[12]}\n"
                       f"Становая тяга акселя 1ПМ - {_[13]}\n"
                       f"Присед 1ПМ: Классический - {_[14]}\n"
                       f"Присед 1ПМ: Фронтальный - {_[15]}\n"
                       f"Присед 1ПМ: Над головой - {_[16]}\n"
                       f"Скакалка - {_[17]}\n"
                       f"Отжимания от пола - {_[18]}\n"
                       f"Челночный бег - {_[19]}\n"
                       f"Прогулка фермера - {_[20]}\n"
                       f"Подтягивания - {_[21]}\n"
                       f"Прыжок в высоту - {_[22]}\n"
                       f"Прыжок в длину - {_[23]}\n"
                       f"Удержание акселя - {_[24]}\n"
                       f"Стойка на руках - {_[25]}\n")

                message += msg + "\n\n"

            elif _[26] == '7':
                msg = (f"🏋️‍♀️<b>Статистика за Июль</b>🏋️‍♀️\n\n"
                       f"Гром - {_[3]}\n"
                       f"Турецкий подъем: Аксель - {_[4]}\n"
                       f"Турецкий подъем: Гиря - {_[5]}\n"
                       f"Жим лежа 1ПМ - {_[6]}\n"
                       f"Рывок акселя 1ПМ - {_[7]}\n"
                       f"Взятие на грудь акселя 1ПМ - {_[8]}\n"
                       f"Ягодичный мостик 1ПМ - {_[9]}\n"
                       f"Становая тяга 1ПМ - {_[10]}\n"
                       f"Рывок 1ПМ - {_[11]}\n"
                       f"Взятие на грудь 1ПМ - {_[12]}\n"
                       f"Становая тяга акселя 1ПМ - {_[13]}\n"
                       f"Присед 1ПМ: Классический - {_[14]}\n"
                       f"Присед 1ПМ: Фронтальный - {_[15]}\n"
                       f"Присед 1ПМ: Над головой - {_[16]}\n"
                       f"Скакалка - {_[17]}\n"
                       f"Отжимания от пола - {_[18]}\n"
                       f"Челночный бег - {_[19]}\n"
                       f"Прогулка фермера - {_[20]}\n"
                       f"Подтягивания - {_[21]}\n"
                       f"Прыжок в высоту - {_[22]}\n"
                       f"Прыжок в длину - {_[23]}\n"
                       f"Удержание акселя - {_[24]}\n"
                       f"Стойка на руках - {_[25]}\n")

                message += msg + "\n\n"

            elif _[26] == '10':
                msg = (f"<b>🏆Статистика за Октябрь</b>🏆\n\n"
                       f"Гром - {_[3]}\n"
                       f"Турецкий подъем: Аксель - {_[4]}\n"
                       f"Турецкий подъем: Гиря - {_[5]}\n"
                       f"Жим лежа 1ПМ - {_[6]}\n"
                       f"Рывок акселя 1ПМ - {_[7]}\n"
                       f"Взятие на грудь акселя 1ПМ - {_[8]}\n"
                       f"Ягодичный мостик 1ПМ - {_[9]}\n"
                       f"Становая тяга 1ПМ - {_[10]}\n"
                       f"Рывок 1ПМ - {_[11]}\n"
                       f"Взятие на грудь 1ПМ - {_[12]}\n"
                       f"Становая тяга акселя 1ПМ - {_[13]}\n"
                       f"Присед 1ПМ: Классический - {_[14]}\n"
                       f"Присед 1ПМ: Фронтальный - {_[15]}\n"
                       f"Присед 1ПМ: Над головой - {_[16]}\n"
                       f"Скакалка - {_[17]}\n"
                       f"Отжимания от пола - {_[18]}\n"
                       f"Челночный бег - {_[19]}\n"
                       f"Прогулка фермера - {_[20]}\n"
                       f"Подтягивания - {_[21]}\n"
                       f"Прыжок в высоту - {_[22]}\n"
                       f"Прыжок в длину - {_[23]}\n"
                       f"Удержание акселя - {_[24]}\n"
                       f"Стойка на руках - {_[25]}\n")

                message += msg + "\n\n"

        return message

    else:
        "Cтатистика за выбранный год отсутствует"



async def insert_stats(user_id, user_name):
    """Add new statistic"""
    db_session = Session()
    statistic = Statistics(user_id=user_id, user_name=user_name)
    db_session.add(statistic)
    db_session.commit()

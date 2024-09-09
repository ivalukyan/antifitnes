from db.router import Base, Session, engine
from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime, UUID, Boolean, BIGINT, Text, Float


class Standards(Base):
    __tablename__ = "bot_app_standards"
    id = Column(UUID, primary_key=True, default=uuid4)
    telegram_id = Column(BIGINT, nullable=True)
    first_name = Column(String, nullable=True)
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


Base.metadata.create_all(engine)


async def insert_standard(user_id, first_name):
    db_session = Session()
    standard = Standards(user_id=user_id, first_name=first_name)
    db_session.add(standard)
    db_session.commit()


async def get_standards_by_id(user_id):
    db_session = Session()
    result = db_session.query(Standards).filter(Standards.telegram_id == user_id).first()

    if not result:
        msg = "У данного пользователя нет нормативов"
        return msg
    else:
        msg = (f"Гром - {result.thunder}\n"
               f"Турецкий подъем: Аксель - {result.turkish_ascent_axel}\n"
               f"Турецкий подъем: Гиря - {result.turkish_ascent_kettlebell}\n"
               f"Жим лежа 1ПМ - {result.bench_press}\n"
               f"Рывок акселя 1ПМ - {result.axel_jerk}\n"
               f"Взятие на грудь акселя 1ПМ - {result.taking_on_axel_chest}\n"
               f"Ягодичный мостик 1ПМ - {result.gluteal_bridge}\n"
               f"Становая тяга 1ПМ - {result.deadlift}\n"
               f"Рывок 1ПМ - {result.jerk}\n"
               f"Взятие на грудь 1ПМ - {result.taking_on_the_chest}\n"
               f"Становая тяга акселя 1ПМ - {result.axel_deadlift}\n"
               f"Присед 1ПМ: Классический - {result.classic_squat}\n"
               f"Присед 1ПМ: Фронтальный - {result.front_squat}\n"
               f"Присед 1ПМ: Над головой - {result.squat_over_the_head}\n"
               f"Скакалка - {result.skipping_rope}\n"
               f"Отжимания от пола - {result.push_ups}\n"
               f"Челночный бег - {result.shuttle_running}\n"
               f"Прогулка фермера - {result.farmer_walk}\n"
               f"Подтягивания - {result.pull_ups}\n"
               f"Прыжок в высоту - {result.high_jump}\n"
               f"Прыжок в длину - {result.long_jump}\n"
               f"Удержание акселя - {result.holding_the_axel}\n"
               f"Стойка на руках - {result.handstand}\n")
        return msg


async def get_all_thunder():
    """Get thunder"""
    db_session = Session()
    standard = db_session.query(Standards.thunder).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Гром📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_turkish_ascent_axel():
    """Get turkish ascent axel"""
    db_session = Session()
    standard = db_session.query(Standards.turkish_ascent_axel).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Турецкий подъем: Аксель📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_turkish_ascent_kettlebell():
    """Get turkish ascent kettlebell"""
    db_session = Session()
    standard = db_session.query(Standards.turkish_ascent_kettlebell).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Турецкий подъем: Гиря📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_bench_press():
    """Get bench press"""
    db_session = Session()
    standard = db_session.query(Standards.bench_press).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Жим лежа 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"
    

async def get_all_axel_jerk():
    """Get axel jerk"""
    db_session = Session()
    standard = db_session.query(Standards.bench_press).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Рывок акселя 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_taking_on_axel_chest():
    """Get taking on axel chest"""
    db_session = Session()
    standard = db_session.query(Standards.taking_on_axel_chest).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Взятие на грудь акселя 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"
    

async def get_all_gluteal_bridge():
    """Get gluteal bridge"""
    db_session = Session()
    standard = db_session.query(Standards.gluteal_bridge).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Ягодичный мостик 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_deadlift():
    """Get deadlift"""
    db_session = Session()
    standard = db_session.query(Standards.deadlift).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Становая тяга 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_jerk():
    """Get jerk"""
    db_session = Session()
    standard = db_session.query(Standards.jerk).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Рывок 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_taking_on_the_chest():
    """Get taking on the chest"""
    db_session = Session()
    standard = db_session.query(Standards.taking_on_axel_chest).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Взятие на грудь 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_axel_deadlift():
    """Get deadlift"""
    db_session = Session()
    standard = db_session.query(Standards.deadlift).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Становая тяга акселя 1ПМ📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_classic_squat():
    """Get classic squat"""
    db_session = Session()
    standard = db_session.query(Standards.classic_squat).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Присед 1ПМ: Классический📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_front_squat():
    """Get front squat"""
    db_session = Session()
    standard = db_session.query(Standards.front_squat).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Присед 1ПМ: Фронтальный📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_squat_over_the_head():
    """Get squat over the head"""
    db_session = Session()
    standard = db_session.query(Standards.squat_over_the_head).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Присед 1ПМ: Над головой📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_skipping_rope():
    """Get skipping rope"""
    db_session = Session()
    standard = db_session.query(Standards.skipping_rope).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Скакалка📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_push_ups():
    """Get push ups"""
    db_session = Session()
    standard = db_session.query(Standards.push_ups).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Отжимания от пола📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_shuttle_running():
    """Get shuttle running"""
    db_session = Session()
    standard = db_session.query(Standards.shuttle_running).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Челночный бег📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_farmer_walk():
    """Get farmer walk"""
    db_session = Session()
    standard = db_session.query(Standards.farmer_walk).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Прогулка фермера📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_pull_ups():
    """Get pull ups"""
    db_session = Session()
    standard = db_session.query(Standards.pull_ups).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Подтягивания📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_high_jump():
    """Get high jump"""
    db_session = Session()
    standard = db_session.query(Standards.high_jump).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Прыжок в высоту📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_long_jump():
    """Get long jump"""
    db_session = Session()
    standard = db_session.query(Standards.long_jump).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Прыжок в длину📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_holding_the_axel():
    """holding the axel"""
    db_session = Session()
    standard = db_session.query(Standards.holding_the_axel).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Удержание акселя📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"


async def get_all_handstand():
    """Get handstand"""
    db_session = Session()
    standard = db_session.query(Standards.handstand).all()
    name = db_session.query(Standards.first_name).all()

    msg = f"📊Стойка на руках📊\n\n"

    standards = {}
    names = {}
    count = 1

    for _ in range(len(standard)):
        standards[_] = standard[_][0]
        names[_] = name[_][0]

    sorted_standard = {k: v for k, v in sorted(standards.items(), key=lambda item: item[1])}

    if standard is not None and len(standard) > 0:
        for k in sorted_standard.keys():
            msg += f'{count}. {sorted_standard[k]} - {names[k]}\n'

            count += 1

        return msg
    else:
        return "В выбранном сегменте нормативы отсутствуют!"
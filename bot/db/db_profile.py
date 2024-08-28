from db.router import Base, Session, engine
from uuid import uuid4
from sqlalchemy import Column, String, UUID, Boolean, BIGINT, Text


class Profile(Base):
    __tablename__ = 'bot_app_profile'

    id = Column(UUID, primary_key=True, default=uuid4)
    telegram_id = Column(BIGINT, nullable=True)
    first_name = Column(String, nullable=True, default='')
    username = Column(String, nullable=True)
    gender = Column(String, nullable=True, default='gender')
    phone_number = Column(String, nullable=True, default='')
    training_history = Column(Text, nullable=True, default='-')
    number_of_referral_points = Column(Text, nullable=True, default=0)
    info_subscription = Column(Text, nullable=True, default="-")
    current_standard = Column(Text, nullable=True, default="-")
    telegram_status = Column(Boolean, nullable=True, default=False)


Base.metadata.create_all(engine)


async def update_profile(telegram_id: int, first_name: str, username: str, gender: str, phone: str,
                          history: str, referral: str, subscription: str, standard: str, status: bool) -> None:
    db_session = Session()
    profile = Profile(telegram_id=telegram_id, first_name=first_name, username=username, gender=gender,
                       phone_number=phone, training_history=history, number_of_referral_points=referral,
                       info_subscription=subscription, current_standard=standard, telegram_status=status)
    db_session.add(profile)
    db_session.commit()


async def training_history(user_id: int):
    """Get user traning histoty"""
    db_session = Session()
    result = db_session.query(Profile.training_history).filter(Profile.telegram_id == user_id).first()

    if result is not None:
        return result[0]
    else:
        return "История тренировок отсутствует"


async def number_of_referral_points(user_id: int):
    """Get user number of referal points"""
    db_session = Session()
    result = db_session.query(Profile.number_of_referral_points).filter(Profile.telegram_id == user_id).first()
  
    if result is not None:
        return result[0]
    else:
        return 0


async def info_subscription(user_id: int):
    """Get user info subscription"""
    db_sesion = Session()
    result = db_sesion.query(Profile.info_subscription).filter(Profile.telegram_id == user_id).first()

    if result is not None:
        return result[0]
    else:
        return "Отсутствует"


async def get_name(user_id):
    """Get user name"""
    db_session = Session()
    result = db_session.query(Profile.first_name).filter(Profile.telegram_id == user_id).first()

    if result is not None:
        return result[0]
    else:
        raise ValueError("No name")


async def check_login(user_id: int):
    """Check login"""
    db_session = Session()
    result = db_session.query(Profile.telegram_id).all()
    
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
    """Get all users"""

    db_session = Session()
    result = db_session.query(Profile.telegram_id).all()

    res = []
    print(result)
    if result is not None:
        for i in range(len(result)):
            if result[i][0] is not None:
                res.append(result[i][0])

        print(res)
        return res
    return None


async def crm_eqv(user_id):
    """Get login status in CRM"""
    if user_id in await get_all_users():

        db_session = Session()
        result = db_session.query(Profile.phone_number).filter(Profile.telegram_id == user_id).first()

        return result
    return None


async def get_telegram_status(user_id) -> bool:
    """Get user telegram status"""
    db_session = Session()
    result = db_session.query(Profile.telegram_status).filter(Profile.telegram_id == user_id).first()

    if result is not None:
        return result[0]
    else:
        return False


async def get_all_phones(phone_number: str) -> bool:
    """Get all phones"""
    db_session = Session()
    result = db_session.query(Profile.phone_number).all()

    res = []
    if result is not None:
        for i in range(len(result)):
            res.append(result[i][0][-10:])
        if phone_number in res:
            return True
        return False

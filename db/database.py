from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from config import settings
from db.models import Base


class DbInstance:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DbInstance, cls).__new__(cls)

            connect_url = {
                'drivername': 'postgresql+psycopg2',
                'host': settings.db_host,
                'port': settings.db_port,
                'username': settings.db_user,
                'password': settings.db_password,
                'database': settings.db_name
            }
            echo = settings.log_level == 'debug'
            cls._instance.engine = create_engine(URL.create(**connect_url), echo=echo)
            cls._instance.session_maker = sessionmaker(bind=cls._instance.engine)
            Base.metadata.create_all(cls._instance.engine)
        return cls._instance


def get_db():
    with DbInstance().session_maker() as session:
        yield session

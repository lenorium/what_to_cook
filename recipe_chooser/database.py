from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from config import settings
from models import Base

connect_url = {
    'drivername': 'postgresql+psycopg2',
    'host': settings.db_host,
    'port': settings.db_port,
    'username': settings.db_user,
    'password': settings.db_password,
    'database': settings.db_name
}
echo = settings.log_level == 'debug'
engine = create_engine(URL(**connect_url), echo=echo)
session_maker = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
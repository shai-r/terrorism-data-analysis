import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.postgresql_db.models_postgresql import Base

load_dotenv(verbose=True)


engine = create_engine(os.environ['POSTGRESQL_URL'])
session_maker = sessionmaker(bind=engine)


def init_postgresql():
    Base.metadata.create_all(engine)
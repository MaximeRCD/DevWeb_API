import databases
import sqlalchemy
from config import *

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{API_IP}:3306/{DB_NAME}"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

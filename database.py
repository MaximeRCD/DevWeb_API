import databases
import sqlalchemy
from sqlalchemy_utils import database_exists, create_database
from config import *

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{API_IP}:3306/{DB_NAME}"

database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData()

if not database_exists(engine.url):
    create_database(engine.url)

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("pseudo", sqlalchemy.String(length=30)),
    sqlalchemy.Column("email", sqlalchemy.String(length=100)),
    sqlalchemy.Column("password", sqlalchemy.String(length=35)),
    sqlalchemy.Column("last_updated", sqlalchemy.TIMESTAMP)
)

scans = sqlalchemy.Table(
        "scans",
        metadata,
        sqlalchemy.Column("user_id", sqlalchemy.Integer),
        sqlalchemy.Column("predicted_class", sqlalchemy.String(length=15)),
        sqlalchemy.Column("date", sqlalchemy.TIMESTAMP),
        sqlalchemy.Column("score", sqlalchemy.Float),

)

metadata.create_all(engine)

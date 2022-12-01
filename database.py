import databases
import sqlalchemy

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/garbage_app_db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.config import Settings

# For Postgre SQL
SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# If we don't want to install postgres or any other database, we can use SQLite
# We can uncomment below lines of code

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
        # since sqlite current does not support multile threads , we have to set "check_same_thread= False"
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# Every instance of this session local is an actual database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Function to dynamically select database at different runtime. (i.e for testing and production)
# While testing the below function will be PATCHED in unit test and `test db` will be used instead of `prod db`
# def get_db() -> Generator:
def get_db():

    try:
        # Creating an object of the session local.
        db = SessionLocal()
        yield db
    finally:
        # In any case the database session should be closed
        db.close()

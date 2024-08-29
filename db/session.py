from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


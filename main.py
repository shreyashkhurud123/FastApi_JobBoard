from fastapi import FastAPI
from core.config import Settings
from db.session import engine
from db.base import Base


# Will create tables only
def create_tables():
    # Connects the FASTApi with the database engine
    # So the databse will be created everytime we start this project but the data would not be deleted
    # (i.e db is not completely dropped and reinitialized each time)
    Base.metadata.create_all(bind=engine)


# The below fun will simply start the app
def start_application():
    app = FastAPI(title=Settings.PROJECT_TITLE, version=Settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"details": "Hello World"}

# File for business logic for creating new user

# `Depends` -> for dependencies
from fastapi import APIRouter, Depends

# Importing `Session` just for validating the data type
from sqlalchemy.orm import Session

# To validate the data which would be sent to our API Endpoint
from schemas.user import UserCreate, ShowUser

# To patch the database session so that we can use different database during dev testing and production
from db.session import get_db

# For creating an user
from db.repository.users import create_new_user


# We can use this router for creating new API Endpoints
router = APIRouter()


# Since the user will be sending data which will create a new entry in the database we will use Post
# `response_model` is pydantic model called schema
@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    user = create_new_user(user, db)
    return user

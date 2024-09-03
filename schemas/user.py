# File Restriction and Data Validation


from typing import Optional

# EmailStr -> To enforce email validation
from pydantic import BaseModel, EmailStr


# Schema for data validation for new user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr 
    password: str


# Class for showing only necessary details
class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    # Even if the object is an ORM, below code will convert the ORM to dictionary
    class Config():
        orm_mode = True

# File Restriction and Data Validation


from typing import Optional

# EmailStr -> To enforce email validation
from pydantic import BaseModel, EmailStr


# Schema for data validation for new user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr 
    password: str

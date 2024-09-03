# File for storing ORM logic for creating new user.

# Session will be used as a datatype validator.
from sqlalchemy.orm import Session

# Custom module importing.
# Used for data validation part
from schemas.user import UserCreate

# Actual SQLAlchemy Model
from db.models.users import User

from core.hashing import Hasher


# Below function will be used in API endpoints to create new users
def create_new_user(user: UserCreate, db: Session):
    user = User(username=user.username, email=user.email,
                hashed_password=Hasher.get_password_hash(user.password),
                is_active=True, is_superuser=False)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


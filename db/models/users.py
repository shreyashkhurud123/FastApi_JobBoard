from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)

    # If we want to verify the user by email and if the user should click on the link to activate it, we can make
    # is_active by default = False
    is_active = Column(Boolean, default=True)

    # SuperUser will have control over everything (Admin)
    is_superuser = Column(Boolean, default=False)
    jobs = relationship("Job", back_populates="owner")

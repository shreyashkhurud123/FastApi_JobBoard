from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr


# Parent class for every other sqlalchemy orm class
# Every class which will inherit this Base class will automatically get the below attributes
@as_declarative()
class Base:
    # primary key for every other classes
    id: Any

    # tablename
    __name__: str

    # Function to auto generate table name from the class name
    def __tablename__(cls):
        # returns class name
        return cls.__name__.lower()

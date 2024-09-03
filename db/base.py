# Instead of directly importing the models in main.py file and making the structure of
# main.py file messy, we can create this file for importing all the models


from db.base_class import Base
from db.models.jobs import Job
from db.models.users import User


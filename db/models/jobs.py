from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from Backend_codebase.db.base_class import Base


# The below class will be inheriting Base class for ORM
# The advantage of using ORM is that we have to write different queries for different databases
# Hence SQLAlchemy will manage the translation of queries for different databases
class Job(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    description = Column(String)
    date_posted = Column(Date)
    # For controlling whether to show in FE or not
    is_active = Column(Boolean)

    # Foriegn key
    owner_id = Column(Integer, ForeignKey("user.id"))

    # back_populates basically means that there exists a reverse relation from owner to job
    owner = relationship("User", back_populates="jobs")

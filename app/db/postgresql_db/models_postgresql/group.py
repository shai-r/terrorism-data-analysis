from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.db.postgresql_db.models_postgresql import Base

class Group(Base):
    __tablename__ = 'groups'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    motive = Column(String, nullable=True)
    doubt_terr = Column(Boolean, nullable=True)  # Doubt about group's responsibility

    events = relationship("Event", back_populates="group")
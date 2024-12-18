from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.postgresql_db.models_postgresql import Base

class EventCriteria(Base):
    __tablename__ = 'events_criteria'

    id = Column(String, primary_key=True)
    crit1 = Column(Boolean, nullable=False)
    crit2 = Column(Boolean, nullable=False)
    crit3 = Column(Boolean, nullable=False)

    event_id = Column(String, ForeignKey('events_metadata.id'), nullable=False)
    event = relationship("EventMetadata", back_populates="criteria")

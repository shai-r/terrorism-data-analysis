from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.db.postgresql_db.models_postgresql import Base

class Hostage(Base):
    __tablename__ = 'hostages'

    id = Column(String, primary_key=True)
    is_hostage = Column(Boolean, nullable=False)
    num_hostages = Column(Integer, nullable=True)
    ransom_amount = Column(Float, nullable=True)

    event_id = Column(String, ForeignKey('events_metadata.id'), nullable=False)  # Event Foreign Key
    event = relationship("EventMetadata", back_populates="hostage_info")

    __table_args__ = (
        Index('idx_is_hostage', 'is_hostage'),
        Index('idx_event_id', 'event_id'),
    )

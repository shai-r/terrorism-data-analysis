from sqlalchemy import Column, String, Date, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.db.postgresql_db.models_postgresql import Base
class EventMetadata(Base):
    __tablename__ = 'events_metadata'

    id = Column(String, primary_key=True)
    event_date = Column(Date, nullable=False)
    resolution = Column(String, nullable=True)

    group_id = Column(String, ForeignKey('groups.id'), nullable=True, index=True)
    weapon_id = Column(String, ForeignKey('weapons.id'), nullable=True, index=True)
    location_id = Column(String, ForeignKey('locations.id'), nullable=True, index=True)

    group = relationship("Group", back_populates="events")
    weapon = relationship("Weapon", back_populates="events")
    hostage_info = relationship("Hostage", uselist=False, back_populates="event")
    criteria = relationship("EventCriteria", uselist=False, back_populates="event")
    location = relationship("Location", back_populates="events")

    __table_args__ = (
        Index('ix_event_metadata_event_date', 'event_date'),
    )
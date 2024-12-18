from sqlalchemy import Column, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.db.postgresql_db.models_postgresql import Base

class Weapon(Base):
    __tablename__ = 'weapons'

    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    subtype = Column(String, nullable=True)
    details = Column(String, nullable=True)  # Additional Weapon Details
    property_damage = Column(Boolean, nullable=True)
    property_value = Column(Float, nullable=True)

    events = relationship("Event", back_populates="weapon")
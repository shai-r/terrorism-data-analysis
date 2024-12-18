from sqlalchemy import Column, String, Float, Index
from sqlalchemy.orm import relationship
from app.db.postgresql_db.models_postgresql import Base

class Location(Base):
    __tablename__ = 'locations'

    id = Column(String, primary_key=True)
    country = Column(String, nullable=False)
    city = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    vicinity = Column(String, nullable=True)

    events = relationship("EventMetadata", back_populates="location")

    __table_args__ = (
        Index('ix_location_country_city', 'country', 'city'),
        Index('ix_location_latitude_longitude', 'latitude', 'longitude')
    )

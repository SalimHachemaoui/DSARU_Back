from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from datetime import datetime


class ServiceModel(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    image = Column(String(200))
    description = Column(String(255))
    categorie_id = Column(Integer, ForeignKey("categorie.id"))
    categorie = relationship("CategorieModel", back_populates="services")


    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


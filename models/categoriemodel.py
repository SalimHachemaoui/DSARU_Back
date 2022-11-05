from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from datetime import datetime



class CategorieModel(Base):
    __tablename__ = "categorie"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    image = Column(String(200))
    description = Column(String(255))
    services = relationship("service",back_populates="service")


    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
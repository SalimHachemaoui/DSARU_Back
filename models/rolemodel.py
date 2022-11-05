
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey,Table
from sqlalchemy.orm import relationship

from db.database import Base
from datetime import datetime


class RoleModel(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))

    users = relationship("User", back_populates="role")



    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


roleservice_table = Table("roleservice", Base.metadata,
    Column("role_id", ForeignKey("role.id"),primary_key=True),
    Column("service_id", ForeignKey("service.id"),primary_key=True),
)
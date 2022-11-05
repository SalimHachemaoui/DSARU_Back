from hashlib import sha256
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
import passlib.hash as _hash



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String(200))
    first_name = Column(String(200))
    email = Column(String(200), unique=True, index=True)
    password = Column(String(20))
    is_active = Column(Boolean, default=False)

    role_id = Column(Integer, ForeignKey("role.id"))
    roles = relationship("RoleModel", back_populates="users")


    def __repr__(self):
        return f"<User {self.email}"

    def check_password(self, hashed_password, plain_password) -> bool:
        password, salt = hashed_password.split(':')
        return password == sha256(salt.encode() + plain_password.encode()).hexdigest()

    def verify_password(self, password:str):
        return _hash.bcrypt.verify(password, self.password)

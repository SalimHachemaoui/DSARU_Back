from sqlalchemy import create_engine, Integer, Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as _sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/dsaruapp"
DATABASE_URL ="mysql+mysqlconnector://root@localhost:3306/cerist"
engine =_sql.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


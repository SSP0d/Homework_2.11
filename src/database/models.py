from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True, nullable=False, )
    surname = Column(String(20), index=True, nullable=False)
    email = Column(String(20), unique=True, index=True, nullable=False)
    phone = Column(String(10), unique=True, index=True, nullable=False)
    birthday = Column(DateTime, index=True, nullable=False)
    description = Column(String(255), index=True, nullable=True)
    
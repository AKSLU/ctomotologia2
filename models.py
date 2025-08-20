from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    healing_price = Column(Integer)
    status = Column(Integer)

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    date = Column(Date, default=datetime.date.today)
    client_id = Column(Integer)

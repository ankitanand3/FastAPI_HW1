from database import Base
from sqlalchemy import Column, String, Integer

class Books(Base):
    __tablename__ = 'books'
    id= Column(Integer, primary_key=True, index=True)
    Name= Column(String, index=True)
    Writer= Column(String, index=True)
    Year= Column(Integer, index=True)
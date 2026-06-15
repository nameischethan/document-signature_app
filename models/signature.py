from sqlalchemy import Column, Integer, String
from database import Base

class Signature(Base):
    __tablename__ = "signatures"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    filepath = Column(String)
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String)
    input_text = Column(String)
    output_text = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

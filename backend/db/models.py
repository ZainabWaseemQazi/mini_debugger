from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from datetime import datetime
from db.database import Base

class DebugHistory(Base):
    __tablename__ = "debug_history"

    id = Column(Integer, primary_key=True, index=True)
    original_code = Column(Text)
    final_code = Column(Text)
    iterations = Column(Integer)
    success = Column(Boolean)
    status = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
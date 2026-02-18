from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class TestSession(Base):
    __tablename__ = "test_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    section = Column(String, nullable=False)  # listening, reading, writing, speaking
    mode = Column(String, default="practice")  # practice, mock
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    score = Column(Float, nullable=True)
    raw_score = Column(Integer, nullable=True)
    total_questions = Column(Integer, nullable=True)

    user = relationship("User", back_populates="test_sessions")
    answers = relationship("UserAnswer", back_populates="session")
    writing_responses = relationship("WritingResponse", back_populates="session")
    speaking_responses = relationship("SpeakingResponse", back_populates="session")

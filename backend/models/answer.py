from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class UserAnswer(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("test_sessions.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    answer = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=True)
    time_taken_sec = Column(Float, nullable=True)
    answered_at = Column(DateTime(timezone=True), server_default=func.now())

    session = relationship("TestSession", back_populates="answers")
    question = relationship("Question", back_populates="answers")

from sqlalchemy import Column, Integer, String, Text, JSON, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class SpeakingResponse(Base):
    __tablename__ = "speaking_responses"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("test_sessions.id"), nullable=False)
    task_num = Column(Integer, nullable=False)  # 1–8
    task_type = Column(String, nullable=True)
    prompt_text = Column(Text, nullable=True)
    image_path = Column(String, nullable=True)
    audio_path = Column(String, nullable=True)
    transcript = Column(Text, nullable=True)
    ai_feedback = Column(JSON, nullable=True)
    score = Column(Float, nullable=True)
    # Dimensional scores
    score_content = Column(Float, nullable=True)
    score_vocabulary = Column(Float, nullable=True)
    score_listenability = Column(Float, nullable=True)
    score_task_fulfillment = Column(Float, nullable=True)
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())

    session = relationship("TestSession", back_populates="speaking_responses")

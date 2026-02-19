from sqlalchemy import Column, Integer, String, Text, JSON, Float
from sqlalchemy.orm import relationship
from database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    section = Column(String, nullable=False, index=True)  # listening, reading
    part = Column(Integer, nullable=False, index=True)
    part_title = Column(String, nullable=True)
    question_number = Column(Integer, nullable=True)
    question_type = Column(String, nullable=False)  # multiple_choice, fill_blank, matching
    passage_text = Column(Text, nullable=True)
    audio_script = Column(Text, nullable=True)
    audio_path = Column(String, nullable=True)
    image_path = Column(String, nullable=True)
    question_text = Column(Text, nullable=False)
    options = Column(JSON, nullable=True)  # ["A) ...", "B) ...", "C) ...", "D) ..."]
    correct_answer = Column(String, nullable=False)
    explanation = Column(Text, nullable=True)
    difficulty = Column(Float, default=1.0)
    tags = Column(JSON, nullable=True)

    answers = relationship("UserAnswer", back_populates="question")

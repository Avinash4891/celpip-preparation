from pydantic import BaseModel
from typing import Optional, List, Any


class QuestionOut(BaseModel):
    id: int
    section: str
    part: int
    part_title: Optional[str]
    question_number: Optional[int]
    question_type: str
    passage_text: Optional[str]
    audio_script: Optional[str]
    audio_path: Optional[str]
    image_path: Optional[str]
    question_text: str
    options: Optional[List[str]]
    difficulty: float
    tags: Optional[Any]

    model_config = {"from_attributes": True}


class AnswerSubmit(BaseModel):
    session_id: int
    question_id: int
    answer: str
    time_taken_sec: Optional[float] = None


class AnswerResult(BaseModel):
    question_id: int
    is_correct: bool
    correct_answer: str
    explanation: Optional[str]
    your_answer: str

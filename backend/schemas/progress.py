from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, Any


class ProgressOut(BaseModel):
    id: int
    user_id: int
    date: date
    section: str
    score: Optional[float]
    notes: Optional[str]
    created_at: datetime

    model_config = {"from_attributes": True}


class StudyPlanOut(BaseModel):
    id: int
    user_id: int
    target_score: int
    target_date: Optional[date]
    daily_tasks: Optional[Any]
    created_at: datetime

    model_config = {"from_attributes": True}

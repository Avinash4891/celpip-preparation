from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date, timedelta
from database import get_db
from models.user import User
from models.test_session import TestSession
from models.progress import Progress, StudyPlan
from schemas.progress import ProgressOut, StudyPlanOut
from .deps import get_current_user

router = APIRouter(prefix="/progress", tags=["progress"])


@router.get("/", response_model=List[ProgressOut])
def get_progress(
    section: str = None,
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = db.query(Progress).filter(Progress.user_id == current_user.id)
    if section:
        query = query.filter(Progress.section == section)
    return query.order_by(Progress.date.desc()).limit(limit).all()


@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    sections = ["listening", "reading", "writing", "speaking"]
    summary = {}
    for section in sections:
        sessions = db.query(TestSession).filter(
            TestSession.user_id == current_user.id,
            TestSession.section == section,
            TestSession.score.isnot(None),
        ).order_by(TestSession.completed_at.desc()).limit(5).all()

        scores = [s.score for s in sessions if s.score]
        summary[section] = {
            "latest_score": scores[0] if scores else None,
            "average_score": round(sum(scores) / len(scores), 1) if scores else None,
            "sessions_completed": len(sessions),
            "trend": _calculate_trend(scores),
        }

    return {"status": "success", "data": summary}


@router.get("/history")
def get_history(
    days: int = 30,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    since = date.today() - timedelta(days=days)
    sessions = db.query(TestSession).filter(
        TestSession.user_id == current_user.id,
        TestSession.completed_at.isnot(None),
        TestSession.score.isnot(None),
    ).order_by(TestSession.completed_at.asc()).all()

    history = [
        {
            "session_id": s.id,
            "section": s.section,
            "score": s.score,
            "date": s.completed_at.date().isoformat() if s.completed_at else None,
        }
        for s in sessions
    ]
    return {"status": "success", "data": history}


@router.get("/study-plan", response_model=StudyPlanOut)
def get_study_plan(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    plan = db.query(StudyPlan).filter(StudyPlan.user_id == current_user.id).order_by(StudyPlan.created_at.desc()).first()
    if not plan:
        raise HTTPException(status_code=404, detail="No study plan found")
    return plan


@router.post("/study-plan", response_model=StudyPlanOut, status_code=201)
def create_study_plan(
    target_score: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    today = date.today()
    target_date = today + timedelta(days=14)
    daily_tasks = _generate_14_day_plan()

    plan = StudyPlan(
        user_id=current_user.id,
        target_score=target_score,
        target_date=target_date,
        daily_tasks=daily_tasks,
    )
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan


def _calculate_trend(scores: list) -> str:
    if len(scores) < 2:
        return "insufficient_data"
    if scores[0] > scores[-1]:
        return "improving"
    if scores[0] < scores[-1]:
        return "declining"
    return "stable"


def _generate_14_day_plan() -> list:
    return [
        {"day": 1, "focus": "Orientation", "tasks": ["Take diagnostic test in all sections", "Review test format guide", "Set up study schedule"]},
        {"day": 2, "focus": "Diagnostic Review", "tasks": ["Review diagnostic results", "Identify weak areas", "Study CELPIP scoring rubric"]},
        {"day": 3, "focus": "Listening Parts 1–3", "tasks": ["Practice Listening Parts 1–3", "Listen to 2 Canadian news podcasts", "Dictation exercise (10 min)"]},
        {"day": 4, "focus": "Listening Parts 4–6", "tasks": ["Practice Listening Parts 4–6", "Focus on note-taking strategies", "Review listening vocabulary"]},
        {"day": 5, "focus": "Reading Parts 1–2", "tasks": ["Practice Reading Parts 1–2", "Skim/scan technique drill", "Read one correspondence text"]},
        {"day": 6, "focus": "Reading Parts 3–4", "tasks": ["Practice Reading Parts 3–4", "Opinion text analysis", "Vocabulary building from texts"]},
        {"day": 7, "focus": "Mock Test: L + R", "tasks": ["Full timed Listening mock test", "Full timed Reading mock test", "Review all errors"]},
        {"day": 8, "focus": "Writing Task 1", "tasks": ["Study email structure templates", "Write 2 practice emails (timed)", "Review CELPIP writing rubric"]},
        {"day": 9, "focus": "Writing Task 2", "tasks": ["Study opinion essay structure", "Write 2 survey responses (timed)", "Expand vocabulary lists"]},
        {"day": 10, "focus": "Speaking Tasks 1–4", "tasks": ["Practice Speaking Tasks 1–4", "Record and review responses", "Study PREP structure (Point-Reason-Example-Point)"]},
        {"day": 11, "focus": "Speaking Tasks 5–8", "tasks": ["Practice Speaking Tasks 5–8", "Work on fluency and pacing", "Review feedback from previous recordings"]},
        {"day": 12, "focus": "Full Mock Test", "tasks": ["Complete full 4-section mock test under timed conditions", "No breaks between sections"]},
        {"day": 13, "focus": "Targeted Review", "tasks": ["Focus on weakest section from Day 12", "Redo practice for weak question types", "Review model answers"]},
        {"day": 14, "focus": "Final Diagnostic", "tasks": ["Take final mock test", "Compare scores to Day 1 diagnostic", "Identify remaining gaps for ongoing study"]},
    ]

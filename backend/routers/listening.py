from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.user import User
from models.test_session import TestSession
from models.question import Question
from models.answer import UserAnswer
from schemas.question import QuestionOut, AnswerSubmit, AnswerResult
from schemas.session import SessionCreate, SessionOut
from services.scoring import calculate_listening_score
from .deps import get_current_user
from datetime import datetime

router = APIRouter(prefix="/listening", tags=["listening"])


@router.post("/sessions", response_model=SessionOut, status_code=201)
def start_session(
    payload: SessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = TestSession(
        user_id=current_user.id,
        section="listening",
        mode=payload.mode,
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


@router.get("/sessions/{session_id}/questions", response_model=List[QuestionOut])
def get_questions(
    session_id: int,
    part: int = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = db.query(TestSession).filter(
        TestSession.id == session_id,
        TestSession.user_id == current_user.id,
    ).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    query = db.query(Question).filter(Question.section == "listening")
    if part is not None:
        query = query.filter(Question.part == part)
    return query.order_by(Question.part, Question.question_number).all()


@router.post("/sessions/{session_id}/answers", response_model=AnswerResult)
def submit_answer(
    session_id: int,
    payload: AnswerSubmit,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = db.query(TestSession).filter(
        TestSession.id == session_id,
        TestSession.user_id == current_user.id,
    ).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    question = db.query(Question).filter(Question.id == payload.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    is_correct = payload.answer.strip().upper() == question.correct_answer.strip().upper()
    answer = UserAnswer(
        session_id=session_id,
        question_id=payload.question_id,
        answer=payload.answer,
        is_correct=is_correct,
        time_taken_sec=payload.time_taken_sec,
    )
    db.add(answer)
    db.commit()

    return AnswerResult(
        question_id=question.id,
        is_correct=is_correct,
        correct_answer=question.correct_answer,
        explanation=question.explanation,
        your_answer=payload.answer,
    )


@router.post("/sessions/{session_id}/complete", response_model=SessionOut)
def complete_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = db.query(TestSession).filter(
        TestSession.id == session_id,
        TestSession.user_id == current_user.id,
    ).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    answers = db.query(UserAnswer).filter(UserAnswer.session_id == session_id).all()
    correct = sum(1 for a in answers if a.is_correct)
    total = len(answers)

    session.completed_at = datetime.utcnow()
    session.raw_score = correct
    session.total_questions = total
    session.score = calculate_listening_score(correct)
    db.commit()
    db.refresh(session)
    return session


@router.get("/questions", response_model=List[QuestionOut])
def list_questions(
    part: int = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = db.query(Question).filter(Question.section == "listening")
    if part is not None:
        query = query.filter(Question.part == part)
    return query.order_by(Question.part, Question.question_number).all()

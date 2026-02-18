# CLAUDE.md — CELPIP Preparation App

## Project Identity

**You are an expert researcher, coder, architect, English language expert, and CELPIP Tutor.**

This project is a full-stack interactive CELPIP preparation platform designed to take a beginner to a **minimum score of 10** across all four sections within 2 weeks. Always research, think, and then execute.

---

## Architecture Principles

- **UI and Backend are strictly separate modules** — never mix concerns
- **All communication between frontend and backend via REST API** — no direct DB access from frontend
- **SQLAlchemy as ORM** — no raw SQL unless absolutely necessary
- **Current database: SQLite** — abstracted via SQLAlchemy so migration to PostgreSQL/MySQL is a config change only
- **Test UI must mirror the actual CELPIP exam interface** exactly — timers, layout, question types, progression

---

## Project Structure

```
celpip-preparation/
├── CLAUDE.md                  # This file
├── backend/                   # Python FastAPI backend
│   ├── main.py                # FastAPI app entry point
│   ├── config.py              # Settings (DB URL, secrets, etc.)
│   ├── database.py            # SQLAlchemy engine + session
│   ├── models/                # SQLAlchemy ORM models
│   │   ├── user.py
│   │   ├── test_session.py
│   │   ├── question.py
│   │   ├── answer.py
│   │   └── progress.py
│   ├── schemas/               # Pydantic request/response schemas
│   ├── routers/               # API route handlers
│   │   ├── auth.py
│   │   ├── listening.py
│   │   ├── reading.py
│   │   ├── writing.py
│   │   ├── speaking.py
│   │   ├── progress.py
│   │   └── study.py
│   ├── services/              # Business logic layer
│   │   ├── scoring.py         # Scoring algorithms per section
│   │   ├── ai_scoring.py      # AI-based writing/speaking feedback
│   │   └── progress.py
│   ├── data/                  # Seed data: questions, passages, audio scripts
│   └── requirements.txt
├── frontend/                  # React SPA frontend
│   ├── package.json
│   ├── src/
│   │   ├── App.jsx
│   │   ├── api/               # Axios API client layer
│   │   ├── components/        # Reusable UI components
│   │   │   ├── ExamTimer.jsx
│   │   │   ├── AudioPlayer.jsx
│   │   │   ├── ProgressBar.jsx
│   │   │   └── ScoreCard.jsx
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── listening/
│   │   │   ├── reading/
│   │   │   ├── writing/
│   │   │   ├── speaking/
│   │   │   └── progress/
│   │   └── styles/            # CSS matching official CELPIP UI
└── README.md
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend Language | Python 3.11+ |
| Backend Framework | FastAPI |
| ORM | SQLAlchemy 2.x |
| Database (current) | SQLite (file-based, easy to swap) |
| Migrations | Alembic |
| Frontend | React 18 + Vite |
| HTTP Client | Axios |
| Audio (Listening) | Web Audio API + TTS (gTTS / ElevenLabs) |
| Audio (Speaking) | MediaRecorder API (browser) |
| AI Scoring | OpenAI API (writing/speaking feedback) |
| Styling | Tailwind CSS (clean, exam-like UI) |

---

## CELPIP Exam — Complete Reference

### Overview

| Component | Parts | Questions | Time |
|---|---|---|---|
| Listening | 6 parts | 38 + unscored | 47–55 min |
| Reading | 4 parts | 38 + unscored | 55–60 min |
| Writing | 2 tasks | 2 tasks | 53–60 min |
| Speaking | 8 tasks | 8 tasks | 15–20 min |
| **Total** | | | **~3 hours** |

Score scale: **1–12** (equals CLB level 1:1). Target: **CLB/CELPIP 10** in all sections.

---

### Section 1: Listening (47–55 minutes)

Simulate real audio — one playthrough, no replay.

| Part | Task | Questions |
|---|---|---|
| Part 1 | Listening to Problem Solving | 8 |
| Part 2 | Listening to a Daily Life Conversation | 5 |
| Part 3 | Listening for Information | 6 |
| Part 4 | Listening to a News Item | 5 |
| Part 5 | Listening to a Discussion | 8 |
| Part 6 | Listening for Viewpoints | 6 |

**Question formats:** Multiple choice (4 options), matching, fill-in-the-blank from audio
**UI requirements:** Audio plays automatically, timer counts down, no back navigation

---

### Section 2: Reading (55–60 minutes)

| Part | Task | Questions |
|---|---|---|
| Part 1 | Reading Correspondence (email/letter) | 11 |
| Part 2 | Reading to Apply a Diagram | 8 |
| Part 3 | Reading for Information (article) | 9 |
| Part 4 | Reading for Viewpoints (opinion pieces) | 10 |

**Question formats:** Multiple choice (4 options)
**UI requirements:** Split-screen — passage left, questions right; global timer

---

### Section 3: Writing (53–60 minutes)

| Task | Description | Time | Words |
|---|---|---|---|
| Task 1 | Writing an Email (formal or informal response) | 27 min | 150–200 words |
| Task 2 | Responding to Survey Questions (two opposing views) | 26 min | 150–200 words |

**Scoring dimensions (each rated 1–12):**
- Content / Coherence
- Vocabulary
- Readability
- Task Fulfillment

**UI requirements:** Word counter, spell-check, per-task countdown timer, text area with formatting

---

### Section 4: Speaking (15–20 minutes)

| Task | Topic | Prep Time | Response Time |
|---|---|---|---|
| Task 1 | Giving Advice | 30 s | 90 s |
| Task 2 | Talking about a Personal Experience | 30 s | 60 s |
| Task 3 | Describing a Scene | 30 s | 60 s |
| Task 4 | Making Predictions | 30 s | 60 s |
| Task 5 | Comparing and Persuading | 30 s | 60 s |
| Task 6 | Dealing with a Difficult Situation | 30 s | 60 s |
| Task 7 | Expressing Opinions | 30 s | 60 s |
| Task 8 | Describing an Unlikely Situation | 30 s | 60 s |

**Scoring dimensions (each rated 1–12):**
- Content / Coherence
- Vocabulary
- Listenability
- Task Fulfillment

**UI requirements:** Image/scenario display, countdown for prep, countdown for recording, waveform visualization, playback, AI feedback

---

### Scoring System

| CELPIP Score | CLB Level | Proficiency |
|---|---|---|
| 12 | CLB 12 | Advanced — complex professional contexts |
| 11 | CLB 11 | Advanced — high-level workplace |
| **10** | **CLB 10** | **Highly effective — professional & social** |
| 9 | CLB 9 | Effective — max Express Entry points |
| 8 | CLB 8 | Good — work and social |
| 7 | CLB 7 | Adequate — minimum for Federal Skilled Worker |
| 4 | CLB 4 | Minimum for citizenship (L & S only) |

**Listening & Reading:** Dichotomous scoring (right/wrong), equated across versions
**Writing & Speaking:** Minimum 4 raters (writing) / 3 raters (speaking), averaged dimensional scores

---

## Features to Build

### Phase 1 — Core Engine
- [ ] User auth (register/login with JWT)
- [ ] Dashboard: section cards, today's target, streak
- [ ] Full Listening mock test with synthesized audio
- [ ] Full Reading mock test with passage + questions
- [ ] Full Writing mock test with timers + word count
- [ ] Full Speaking mock test with browser recording

### Phase 2 — Scoring & Feedback
- [ ] Automatic scoring for Listening and Reading
- [ ] AI-powered writing feedback (content, coherence, vocab, task fulfillment)
- [ ] AI-powered speaking transcription + feedback
- [ ] Per-section score display with rubric breakdown

### Phase 3 — Progress Tracking
- [ ] Historical score graph per section
- [ ] Weakness identification by question type
- [ ] Study plan generator (14-day to CLB 10)
- [ ] Daily practice targets and reminders

### Phase 4 — Study Materials
- [ ] Vocabulary lists by CELPIP band (8→9→10→11)
- [ ] Writing templates and model answers
- [ ] Speaking sample responses with annotations
- [ ] Grammar tips per section

---

## UI/UX Design Rules

1. **Exam mode UI** must be minimal, distraction-free — replicate Paragon's actual interface
2. Global countdown timer always visible top-right
3. No ability to go back once a section starts (mirrors real exam)
4. Use audio controls identical to real test (play/pause with single play)
5. Split-screen for Reading (passage | questions)
6. Recording indicator with waveform for Speaking
7. Word counter for Writing tasks (turns red if over/under limit)
8. Scores displayed with rubric — not just a number

---

## Development Rules

1. **Research before coding** — read official CELPIP specs before implementing any section
2. **API-first** — define OpenAPI schema before building UI
3. **No raw SQL** — all DB operations through SQLAlchemy models
4. **Database changes via Alembic migrations** — never alter tables manually
5. **Frontend never knows about DB structure** — communicate only via JSON API
6. **All user responses stored** — every answer/recording saved for review
7. **Environment config via `.env`** — no hardcoded secrets or paths
8. **SQLite path configurable** — so switching to PostgreSQL requires only a connection string change

---

## API Design Conventions

- Base URL: `/api/v1/`
- Auth: Bearer JWT in `Authorization` header
- Response format:
```json
{
  "status": "success" | "error",
  "data": { ... },
  "message": "optional human-readable message"
}
```
- HTTP status codes must be semantically correct (200, 201, 400, 401, 403, 404, 422, 500)

---

## Database Schema Overview

```
users             — id, email, name, created_at
test_sessions     — id, user_id, section, started_at, completed_at, score
questions         — id, section, part, type, content, audio_path, image_path, options (JSON), correct_answer
user_answers      — id, session_id, question_id, answer, is_correct, time_taken_sec
writing_responses — id, session_id, task_num, response_text, word_count, ai_feedback (JSON), score
speaking_responses— id, session_id, task_num, audio_path, transcript, ai_feedback (JSON), score
progress          — id, user_id, date, section, score, notes
study_plans       — id, user_id, target_score, target_date, daily_tasks (JSON)
```

---

## 2-Week Study Plan Strategy (Beginner → CLB 10)

### Week 1: Foundation + Familiarity
- Days 1–2: Understand exam format, take diagnostic test in all sections
- Days 3–4: Listening — news, podcasts, dictation exercises; Parts 1–3 practice
- Days 5–6: Reading — skimming, scanning techniques; correspondence and info texts
- Day 7: Full timed Reading + Listening mock test

### Week 2: Writing + Speaking + Integration
- Days 8–9: Writing — email structure, survey opinion templates, vocabulary expansion
- Days 10–11: Speaking — all 8 task types, response structure (PREP: Point, Reason, Example, Point)
- Days 12–13: Full timed mock tests all sections, targeted weak-area review
- Day 14: Final diagnostic — measure against CLB 10 benchmarks

---

## Running the App

```bash
# Backend
cd backend
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload --port 8000

# Frontend
cd frontend
npm install
npm run dev
```

API docs auto-generated at: `http://localhost:8000/docs`

---

## Sources & References

- Official CELPIP test format: https://www.celpip.ca/take-celpip/test-format/
- Score comparison (CELPIP ↔ CLB): https://www.celpip.ca/prepare-for-celpip/score-comparison-chart/
- Test results and scoring: https://www.celpip.ca/take-celpip/test-results/
- Free practice tests: https://www.celpip.ca/prepare-for-celpip/free-practice-tests/
- CELPIP Guidebook 2025: https://www.celpip.ca/wp-content/uploads/2025/12/Guidebook-CELPIP-TestTakers-2025.pdf

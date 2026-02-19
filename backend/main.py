from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from database import Base, engine
from routers import auth, listening, reading, writing, speaking, progress, study

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CELPIP Preparation API",
    description="Full-stack CELPIP exam preparation platform targeting CLB 10",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static audio files
audio_dir = "./data/audio"
os.makedirs(audio_dir, exist_ok=True)
app.mount("/audio", StaticFiles(directory=audio_dir), name="audio")

images_dir = "./data/images"
os.makedirs(images_dir, exist_ok=True)
app.mount("/images", StaticFiles(directory=images_dir), name="images")

# Register routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(listening.router, prefix="/api/v1")
app.include_router(reading.router, prefix="/api/v1")
app.include_router(writing.router, prefix="/api/v1")
app.include_router(speaking.router, prefix="/api/v1")
app.include_router(progress.router, prefix="/api/v1")
app.include_router(study.router, prefix="/api/v1")


@app.get("/api/v1/health")
def health():
    return {"status": "success", "message": "CELPIP Preparation API is running"}


@app.get("/")
def root():
    return {
        "name": "CELPIP Preparation API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/api/v1/health",
    }

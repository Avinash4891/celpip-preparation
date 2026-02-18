import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../App'
import { getProgressSummary } from '../api/questions'

const SECTIONS = [
  {
    key: 'listening',
    title: 'Listening',
    path: '/listening',
    icon: '🎧',
    desc: '6 parts · 38 questions · 47–55 min',
    color: 'border-blue-400',
  },
  {
    key: 'reading',
    title: 'Reading',
    path: '/reading',
    icon: '📖',
    desc: '4 parts · 38 questions · 55–60 min',
    color: 'border-green-400',
  },
  {
    key: 'writing',
    title: 'Writing',
    path: '/writing',
    icon: '✍️',
    desc: '2 tasks · 150–200 words each · 53 min',
    color: 'border-purple-400',
  },
  {
    key: 'speaking',
    title: 'Speaking',
    path: '/speaking',
    icon: '🎤',
    desc: '8 tasks · 30 s prep · 60–90 s response',
    color: 'border-orange-400',
  },
]

export default function Dashboard() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()
  const [progress, setProgress] = useState(null)

  useEffect(() => {
    getProgressSummary()
      .then((res) => setProgress(res.data.data))
      .catch(() => {})
  }, [])

  const latestScore = (section) =>
    progress?.[section]?.latest_score ?? null

  return (
    <div className="min-h-screen bg-exam-bg">
      {/* Header */}
      <header className="bg-primary-900 text-white px-6 py-4 flex items-center justify-between shadow">
        <div>
          <h1 className="text-xl font-bold">CELPIP Preparation</h1>
          <p className="text-blue-200 text-sm">Target: CELPIP 10 in all sections</p>
        </div>
        <div className="flex items-center gap-4">
          <span className="text-sm text-blue-200">Hello, {user?.name}</span>
          <button onClick={logout} className="text-sm text-blue-200 hover:text-white underline">
            Sign out
          </button>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 py-8">
        {/* Welcome banner */}
        <div className="bg-white rounded-xl shadow p-6 mb-8 border-l-4 border-primary-500">
          <h2 className="text-lg font-bold text-gray-800 mb-1">Your 2-Week Study Plan</h2>
          <p className="text-gray-600 text-sm">
            Practise each section daily. The platform scores Listening and Reading automatically.
            Writing and Speaking are evaluated using AI feedback.
          </p>
          <button
            onClick={() => navigate('/progress')}
            className="mt-3 btn-secondary text-sm"
          >
            View Progress →
          </button>
        </div>

        {/* Section cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          {SECTIONS.map((s) => {
            const score = latestScore(s.key)
            return (
              <div
                key={s.key}
                onClick={() => navigate(s.path)}
                className={`section-card border-l-4 ${s.color}`}
              >
                <div className="flex items-start justify-between">
                  <div>
                    <span className="text-3xl">{s.icon}</span>
                    <h3 className="text-xl font-bold mt-2">{s.title}</h3>
                    <p className="text-gray-500 text-sm mt-1">{s.desc}</p>
                  </div>
                  {score !== null && (
                    <div className="text-right">
                      <div className="text-3xl font-black text-primary-700">{score}</div>
                      <div className="text-xs text-gray-400">Last score</div>
                    </div>
                  )}
                </div>
                <button className="mt-4 btn-primary text-sm w-full">
                  Start Practice
                </button>
              </div>
            )
          })}
        </div>

        {/* CLB target */}
        <div className="mt-8 bg-primary-50 border border-primary-200 rounded-xl p-5 text-sm text-primary-800">
          <strong>Target Score:</strong> CELPIP 10 = CLB 10 — Highly effective professional and social English.
          A score of 10 in all four sections qualifies for top-tier Express Entry immigration points.
        </div>
      </main>
    </div>
  )
}

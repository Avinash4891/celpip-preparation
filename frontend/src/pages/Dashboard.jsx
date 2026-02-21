import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../App'
import { getProgressSummary } from '../api/questions'
import { getLearningPath } from '../api/learning'
import Header from '../components/Header'
import StatsCard from '../components/StatsCard'
import { SkeletonCard, SkeletonStats } from '../components/SkeletonLoader'

const SECTIONS = [
  {
    key: 'listening',
    title: 'Listening',
    path: '/listening',
    icon: '🎧',
    desc: '6 parts · 38 questions · 47–55 min',
    gradient: 'from-blue-400 to-blue-600',
    borderColor: 'border-blue-400',
  },
  {
    key: 'reading',
    title: 'Reading',
    path: '/reading',
    icon: '📖',
    desc: '4 parts · 38 questions · 55–60 min',
    gradient: 'from-green-400 to-green-600',
    borderColor: 'border-green-400',
  },
  {
    key: 'writing',
    title: 'Writing',
    path: '/writing',
    icon: '✍️',
    desc: '2 tasks · 150–200 words each · 53 min',
    gradient: 'from-purple-400 to-purple-600',
    borderColor: 'border-purple-400',
  },
  {
    key: 'speaking',
    title: 'Speaking',
    path: '/speaking',
    icon: '🎤',
    desc: '8 tasks · 30 s prep · 60–90 s response',
    gradient: 'from-orange-400 to-orange-600',
    borderColor: 'border-orange-400',
  },
  {
    key: 'learning',
    title: 'Learning Path',
    path: '/learning',
    icon: '📚',
    desc: 'Personalized modules to reach CLB 10',
    gradient: 'from-indigo-400 to-indigo-600',
    borderColor: 'border-indigo-400',
  },
]

export default function Dashboard() {
  const { user } = useAuth()
  const navigate = useNavigate()
  const [progress, setProgress] = useState(null)
  const [learningProgress, setLearningProgress] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const loadData = async () => {
      try {
        setLoading(true)
        const [progressRes, learningRes] = await Promise.all([
          getProgressSummary().catch(() => ({ data: { data: null } })),
          getLearningPath().catch(() => ({ data: { data: null } })),
        ])
        setProgress(progressRes.data.data)
        setLearningProgress(learningRes.data.data)
      } finally {
        setLoading(false)
      }
    }
    loadData()
  }, [])

  const latestScore = (section) => progress?.[section]?.latest_score ?? null

  const calculateOverallScore = () => {
    const scores = ['listening', 'reading', 'writing', 'speaking']
      .map((s) => latestScore(s))
      .filter((s) => s !== null)
    if (scores.length === 0) return null
    return (scores.reduce((a, b) => a + b, 0) / scores.length).toFixed(1)
  }

  return (
    <div className="min-h-screen">
      <Header />

      <main className="max-w-7xl mx-auto px-4 sm:px-6 py-8 animate-fade-in">
        {/* Welcome Banner */}
        <div className="glass-card p-8 mb-8 border-l-4 border-primary-500 animate-slide-up">
          <div className="flex items-start justify-between">
            <div className="flex-1">
              <h2 className="text-2xl font-bold text-gray-900 mb-2 flex items-center gap-3">
                <span className="text-3xl">👋</span>
                Welcome back, {user?.name}!
              </h2>
              <p className="text-gray-600 mb-4">
                Ready to achieve your CLB 10 target? The platform offers automatic scoring for Listening and Reading,
                plus AI-powered feedback for Writing and Speaking.
              </p>
              <div className="flex items-center gap-3">
                <button
                  onClick={() => navigate('/progress')}
                  className="btn-primary"
                >
                  View Detailed Progress →
                </button>
                <button
                  onClick={() => navigate('/learning')}
                  className="btn-secondary"
                >
                  Continue Learning
                </button>
              </div>
            </div>
            <div className="hidden lg:block">
              <div className="w-32 h-32 bg-gradient-to-br from-primary-400 to-indigo-600 rounded-2xl flex items-center justify-center text-6xl shadow-2xl transform hover:scale-110 transition-transform duration-300">
                🎯
              </div>
            </div>
          </div>
        </div>

        {/* Stats Overview */}
        <div className="mb-8">
          <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
            <span>📊</span>
            <span>Performance Overview</span>
          </h3>
          {loading ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
              {[...Array(5)].map((_, i) => (
                <SkeletonStats key={i} />
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 animate-slide-up">
              <StatsCard
                icon="🎯"
                label="Overall Score"
                value={calculateOverallScore() || 'N/A'}
                variant="primary"
                onClick={() => navigate('/progress')}
              />
              <StatsCard
                icon="🎧"
                label="Listening"
                value={latestScore('listening') || 'N/A'}
                variant="info"
                onClick={() => navigate('/listening')}
              />
              <StatsCard
                icon="📖"
                label="Reading"
                value={latestScore('reading') || 'N/A'}
                variant="success"
                onClick={() => navigate('/reading')}
              />
              <StatsCard
                icon="✍️"
                label="Writing"
                value={latestScore('writing') || 'N/A'}
                variant="purple"
                onClick={() => navigate('/writing')}
              />
              <StatsCard
                icon="🎤"
                label="Speaking"
                value={latestScore('speaking') || 'N/A'}
                variant="warning"
                onClick={() => navigate('/speaking')}
              />
            </div>
          )}
        </div>

        {/* Section Cards */}
        <div>
          <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
            <span>📝</span>
            <span>Practice Sections</span>
          </h3>
          {loading ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {[...Array(5)].map((_, i) => (
                <SkeletonCard key={i} />
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {SECTIONS.map((s, index) => {
                const score = latestScore(s.key)
                const learningPct = learningProgress?.progress?.progress_percentage

                return (
                  <div
                    key={s.key}
                    onClick={() => navigate(s.path)}
                    className="section-card border-l-4 group"
                    style={{ borderLeftColor: `var(--tw-${s.borderColor})` }}
                  >
                    {/* Card Header */}
                    <div className="flex items-start justify-between mb-4">
                      <div className="flex items-center gap-3">
                        <div
                          className={`w-14 h-14 bg-gradient-to-br ${s.gradient} rounded-xl flex items-center justify-center text-3xl shadow-lg group-hover:scale-110 transition-transform duration-300`}
                        >
                          {s.icon}
                        </div>
                        <div>
                          <h3 className="text-xl font-bold text-gray-900 group-hover:text-primary-600 transition-colors">
                            {s.title}
                          </h3>
                          <p className="text-xs text-gray-500 uppercase tracking-wide font-semibold">
                            {s.key === 'learning' ? 'Study Modules' : 'Practice Test'}
                          </p>
                        </div>
                      </div>

                      {/* Score/Progress Display */}
                      {s.key === 'learning' && learningPct !== undefined ? (
                        <div className="text-right">
                          <div className="text-3xl font-black bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
                            {Math.round(learningPct)}%
                          </div>
                          <div className="text-xs text-gray-400 font-medium">Complete</div>
                        </div>
                      ) : score !== null ? (
                        <div className="text-right">
                          <div className={`text-3xl font-black bg-gradient-to-r ${s.gradient} bg-clip-text text-transparent`}>
                            {score}
                          </div>
                          <div className="text-xs text-gray-400 font-medium">Last Score</div>
                        </div>
                      ) : (
                        <div className="text-right">
                          <div className="text-2xl text-gray-300">—</div>
                          <div className="text-xs text-gray-400">Not started</div>
                        </div>
                      )}
                    </div>

                    {/* Description */}
                    <p className="text-gray-600 text-sm mb-4 leading-relaxed">{s.desc}</p>

                    {/* Action Button */}
                    <button className="btn-primary w-full group-hover:shadow-xl transition-shadow">
                      {s.key === 'learning' ? '📚 View Modules' : '▶️ Start Practice'}
                    </button>
                  </div>
                )
              })}
            </div>
          )}
        </div>

        {/* CLB Info Banner */}
        <div className="mt-8 glass-card p-6 border-l-4 border-primary-500">
          <div className="flex items-start gap-4">
            <div className="flex-shrink-0 w-12 h-12 bg-gradient-to-br from-primary-500 to-indigo-600 rounded-xl flex items-center justify-center text-2xl shadow-lg">
              ℹ️
            </div>
            <div className="flex-1">
              <h4 className="font-bold text-gray-900 mb-1">Your Target: CLB 10</h4>
              <p className="text-gray-600 text-sm leading-relaxed">
                <strong className="text-primary-700">CELPIP 10 = CLB 10</strong> — Highly effective professional and social English.
                Achieving a score of 10 in all four sections qualifies you for top-tier Express Entry immigration points
                and demonstrates advanced English proficiency.
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}

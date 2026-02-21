import React, { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { getModule, enrollModule, completeModule } from '../../api/learning'
import Header from '../../components/Header'
import LessonListItem from '../../components/LessonListItem'
import ProgressBar from '../../components/ProgressBar'

const SKILL_COLORS = {
  listening: {
    gradient: 'from-blue-500 to-blue-700',
    badge: 'bg-blue-100 text-blue-800',
    ring: 'ring-blue-200',
    icon: '🎧',
  },
  reading: {
    gradient: 'from-green-500 to-emerald-700',
    badge: 'bg-green-100 text-green-800',
    ring: 'ring-green-200',
    icon: '📖',
  },
  writing: {
    gradient: 'from-purple-500 to-violet-700',
    badge: 'bg-purple-100 text-purple-800',
    ring: 'ring-purple-200',
    icon: '✍️',
  },
  speaking: {
    gradient: 'from-orange-500 to-amber-600',
    badge: 'bg-orange-100 text-orange-800',
    ring: 'ring-orange-200',
    icon: '🗣️',
  },
}

const LEVEL_LABELS = {
  1: { label: 'Beginner', color: 'bg-gray-100 text-gray-700' },
  2: { label: 'Intermediate', color: 'bg-blue-100 text-blue-700' },
  3: { label: 'Advanced', color: 'bg-purple-100 text-purple-700' },
  4: { label: 'Mastery', color: 'bg-yellow-100 text-yellow-700' },
}

export default function ModuleViewer() {
  const { moduleId } = useParams()
  const navigate = useNavigate()
  const [module, setModule] = useState(null)
  const [progress, setProgress] = useState(null)
  const [lessons, setLessons] = useState([])
  const [loading, setLoading] = useState(true)
  const [enrolling, setEnrolling] = useState(false)
  const [completing, setCompleting] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    loadModule()
  }, [moduleId])

  const loadModule = async () => {
    try {
      setLoading(true)
      setError(null)
      const res = await getModule(moduleId)
      setModule(res.data.data.module)
      setProgress(res.data.data.progress)
      setLessons(res.data.data.lessons || [])
    } catch (err) {
      console.error('Error loading module:', err)
      setError(err.response?.data?.detail || 'Failed to load module')
    } finally {
      setLoading(false)
    }
  }

  const handleEnroll = async () => {
    try {
      setEnrolling(true)
      await enrollModule(moduleId)
      await loadModule()
    } catch (err) {
      console.error('Error enrolling:', err)
      alert(err.response?.data?.detail || 'Failed to enroll in module')
    } finally {
      setEnrolling(false)
    }
  }

  const handleComplete = async () => {
    const assessmentScore = prompt(
      'Enter your assessment score (0–100), or leave blank:'
    )
    try {
      setCompleting(true)
      await completeModule(
        moduleId,
        assessmentScore ? parseFloat(assessmentScore) : null
      )
      await loadModule()
      alert('Module completed! Great work!')
    } catch (err) {
      console.error('Error completing module:', err)
      alert(err.response?.data?.detail || 'Failed to complete module')
    } finally {
      setCompleting(false)
    }
  }

  const handleLessonClick = (lessonId) => {
    navigate(`/learning/lesson/${lessonId}`)
  }

  if (loading) {
    return (
      <div className="min-h-screen">
        <Header />
        <div className="flex items-center justify-center h-[calc(100vh-64px)]">
          <div className="text-center">
            <div className="w-16 h-16 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin mx-auto mb-4" />
            <p className="text-gray-600 font-medium">Loading module...</p>
          </div>
        </div>
      </div>
    )
  }

  if (error || !module) {
    return (
      <div className="min-h-screen">
        <Header />
        <div className="flex items-center justify-center h-[calc(100vh-64px)] px-4">
          <div className="glass-card p-10 max-w-md text-center animate-scale-in">
            <div className="text-5xl mb-4">❌</div>
            <h2 className="text-xl font-bold text-gray-800 mb-2">Module Not Found</h2>
            <p className="text-gray-600 mb-6">{error}</p>
            <button onClick={() => navigate('/learning')} className="btn-primary">
              ← Back to Learning Path
            </button>
          </div>
        </div>
      </div>
    )
  }

  const skillConfig = SKILL_COLORS[module.skill] || SKILL_COLORS.reading
  const levelConfig = LEVEL_LABELS[module.level] || LEVEL_LABELS[1]
  const completedLessons = lessons.filter((l) => l.completed).length
  const totalLessons = lessons.length
  const allLessonsCompleted = completedLessons === totalLessons && totalLessons > 0
  const completionPct = totalLessons > 0 ? Math.round((completedLessons / totalLessons) * 100) : 0

  return (
    <div className="min-h-screen animate-fade-in">
      <Header />

      {/* Hero Banner */}
      <div className={`bg-gradient-to-r ${skillConfig.gradient} text-white`}>
        <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
          {/* Breadcrumb */}
          <button
            onClick={() => navigate('/learning')}
            className="flex items-center gap-2 text-white/80 hover:text-white text-sm mb-6 transition-colors group"
          >
            <svg className="w-4 h-4 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
            </svg>
            Back to Learning Path
          </button>

          <div className="flex flex-col sm:flex-row sm:items-start gap-6">
            {/* Icon + Title */}
            <div className="flex items-start gap-4 flex-1">
              <div className="w-16 h-16 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center text-3xl shadow-lg flex-shrink-0">
                {skillConfig.icon}
              </div>
              <div>
                <div className="flex flex-wrap items-center gap-2 mb-3">
                  <span className="bg-white/20 backdrop-blur-sm text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wide">
                    {module.skill}
                  </span>
                  <span className="bg-white/20 backdrop-blur-sm text-white text-xs font-semibold px-3 py-1 rounded-full">
                    {levelConfig.label}
                  </span>
                  {module.category && (
                    <span className="bg-white/15 backdrop-blur-sm text-white/90 text-xs px-3 py-1 rounded-full capitalize">
                      {module.category.replace('_', ' ')}
                    </span>
                  )}
                </div>
                <h1 className="text-2xl sm:text-3xl font-bold leading-tight mb-2">
                  {module.title}
                </h1>
                <p className="text-white/80 text-sm leading-relaxed max-w-xl">
                  {module.description}
                </p>
              </div>
            </div>

            {/* Action Button */}
            <div className="flex-shrink-0">
              {!progress && (
                <button
                  onClick={handleEnroll}
                  disabled={enrolling}
                  className="bg-white text-gray-800 font-bold px-6 py-3 rounded-xl hover:bg-gray-100 transition-all shadow-lg hover:shadow-xl disabled:opacity-60 disabled:cursor-not-allowed whitespace-nowrap"
                >
                  {enrolling ? (
                    <span className="flex items-center gap-2">
                      <span className="w-4 h-4 border-2 border-gray-400 border-t-gray-800 rounded-full animate-spin" />
                      Enrolling...
                    </span>
                  ) : (
                    '🚀 Start Module'
                  )}
                </button>
              )}
              {progress?.status !== 'completed' && allLessonsCompleted && (
                <button
                  onClick={handleComplete}
                  disabled={completing}
                  className="bg-green-400 text-white font-bold px-6 py-3 rounded-xl hover:bg-green-300 transition-all shadow-lg disabled:opacity-60 disabled:cursor-not-allowed whitespace-nowrap"
                >
                  {completing ? 'Completing...' : '🏆 Complete Module'}
                </button>
              )}
              {progress?.status === 'completed' && (
                <div className="bg-green-400/30 border-2 border-white/40 text-white px-6 py-3 rounded-xl font-bold text-center">
                  ✓ Completed!
                </div>
              )}
            </div>
          </div>

          {/* Quick Stats Row */}
          <div className="flex flex-wrap items-center gap-6 mt-6 pt-6 border-t border-white/20 text-sm text-white/80">
            {module.estimated_duration_mins && (
              <div className="flex items-center gap-2">
                <span>⏱️</span>
                <span>{module.estimated_duration_mins} min estimated</span>
              </div>
            )}
            <div className="flex items-center gap-2">
              <span>📚</span>
              <span>{totalLessons} lesson{totalLessons !== 1 ? 's' : ''}</span>
            </div>
            {progress && (
              <div className="flex items-center gap-2">
                <span>✅</span>
                <span>{completedLessons} of {totalLessons} completed</span>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">

          {/* Left: Lessons List */}
          <div className="lg:col-span-2 space-y-6">

            {/* Progress Card (only if enrolled) */}
            {progress && (
              <div className="glass-card p-6 animate-slide-up">
                <h2 className="font-bold text-gray-800 mb-5 flex items-center gap-2">
                  <span className="text-xl">📊</span>
                  <span>Your Progress</span>
                </h2>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-5">
                  <div className="text-center p-3 bg-gray-50 rounded-xl">
                    <p className="text-xs text-gray-500 mb-1 font-medium">Status</p>
                    <p className="font-bold text-gray-800 text-sm capitalize">
                      {progress.status.replace('_', ' ')}
                    </p>
                  </div>
                  <div className="text-center p-3 bg-gray-50 rounded-xl">
                    <p className="text-xs text-gray-500 mb-1 font-medium">Lessons</p>
                    <p className="font-bold text-gray-800 text-sm">
                      {completedLessons}/{totalLessons}
                    </p>
                  </div>
                  <div className="text-center p-3 bg-gray-50 rounded-xl">
                    <p className="text-xs text-gray-500 mb-1 font-medium">Time Spent</p>
                    <p className="font-bold text-gray-800 text-sm">
                      {progress.time_spent_mins || 0} min
                    </p>
                  </div>
                  <div className="text-center p-3 bg-gray-50 rounded-xl">
                    <p className="text-xs text-gray-500 mb-1 font-medium">Mastery</p>
                    <p className="font-bold text-gray-800 text-sm">
                      {progress.mastery_level || 0}%
                    </p>
                  </div>
                </div>
                <ProgressBar
                  current={completedLessons}
                  total={totalLessons}
                  label="Lesson Progress"
                />
              </div>
            )}

            {/* Lessons */}
            <div className="glass-card p-6 animate-slide-up" style={{ animationDelay: '0.1s' }}>
              <h2 className="font-bold text-gray-800 mb-5 flex items-center gap-2">
                <span className="text-xl">📋</span>
                <span>Lessons</span>
                <span className="ml-auto badge badge-primary">{totalLessons}</span>
              </h2>

              {lessons.length === 0 ? (
                <div className="text-center py-10">
                  <div className="text-4xl mb-3">📭</div>
                  <p className="text-gray-500">No lessons available yet.</p>
                </div>
              ) : (
                <div className="space-y-3">
                  {lessons.map((lesson, idx) => (
                    <div
                      key={lesson.id}
                      className="animate-slide-up"
                      style={{ animationDelay: `${idx * 0.05}s` }}
                    >
                      <LessonListItem
                        lesson={lesson}
                        onClick={handleLessonClick}
                        completed={lesson.completed}
                      />
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Right Sidebar */}
          <div className="lg:col-span-1 space-y-6">

            {/* Learning Objectives */}
            {module.learning_objectives && module.learning_objectives.length > 0 && (
              <div className="glass-card p-6 animate-slide-up" style={{ animationDelay: '0.15s' }}>
                <h2 className="font-bold text-gray-800 mb-4 flex items-center gap-2">
                  <span className="text-xl">🎯</span>
                  <span>Learning Goals</span>
                </h2>
                <ul className="space-y-3">
                  {module.learning_objectives.map((obj, idx) => (
                    <li key={idx} className="flex items-start gap-3">
                      <div className="w-5 h-5 bg-green-100 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                        <span className="text-green-600 text-xs font-bold">✓</span>
                      </div>
                      <span className="text-sm text-gray-700 leading-relaxed">{obj}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Module Info */}
            <div className="glass-card p-6 animate-slide-up" style={{ animationDelay: '0.2s' }}>
              <h2 className="font-bold text-gray-800 mb-4 flex items-center gap-2">
                <span className="text-xl">ℹ️</span>
                <span>Module Info</span>
              </h2>
              <div className="space-y-3 text-sm">
                <div className="flex justify-between items-center py-2 border-b border-gray-100">
                  <span className="text-gray-500">Skill</span>
                  <span className={`font-semibold px-2 py-0.5 rounded-full text-xs capitalize ${skillConfig.badge}`}>
                    {skillConfig.icon} {module.skill}
                  </span>
                </div>
                <div className="flex justify-between items-center py-2 border-b border-gray-100">
                  <span className="text-gray-500">Level</span>
                  <span className={`font-semibold px-2 py-0.5 rounded-full text-xs ${levelConfig.color}`}>
                    {levelConfig.label}
                  </span>
                </div>
                {module.category && (
                  <div className="flex justify-between items-center py-2 border-b border-gray-100">
                    <span className="text-gray-500">Category</span>
                    <span className="font-semibold text-gray-700 capitalize">
                      {module.category.replace('_', ' ')}
                    </span>
                  </div>
                )}
                <div className="flex justify-between items-center py-2 border-b border-gray-100">
                  <span className="text-gray-500">Lessons</span>
                  <span className="font-semibold text-gray-700">{totalLessons}</span>
                </div>
                {module.estimated_duration_mins && (
                  <div className="flex justify-between items-center py-2">
                    <span className="text-gray-500">Duration</span>
                    <span className="font-semibold text-gray-700">
                      {module.estimated_duration_mins} min
                    </span>
                  </div>
                )}
              </div>
            </div>

            {/* Enroll CTA for sidebar */}
            {!progress && (
              <div className="glass-card p-6 text-center animate-slide-up bg-gradient-to-br from-primary-50 to-indigo-50" style={{ animationDelay: '0.25s' }}>
                <div className="text-4xl mb-3">🚀</div>
                <h3 className="font-bold text-gray-800 mb-2">Ready to start?</h3>
                <p className="text-sm text-gray-600 mb-4">
                  Enroll to track your progress and unlock all lessons.
                </p>
                <button
                  onClick={handleEnroll}
                  disabled={enrolling}
                  className="btn-primary w-full"
                >
                  {enrolling ? 'Enrolling...' : 'Enroll Now'}
                </button>
              </div>
            )}

            {/* Completion Progress (if enrolled) */}
            {progress && completionPct < 100 && (
              <div className="glass-card p-6 text-center animate-slide-up" style={{ animationDelay: '0.25s' }}>
                <div className="relative w-24 h-24 mx-auto mb-4">
                  <svg className="w-24 h-24 -rotate-90" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="40" fill="none" stroke="#e5e7eb" strokeWidth="8" />
                    <circle
                      cx="50" cy="50" r="40" fill="none"
                      stroke="#2563eb" strokeWidth="8"
                      strokeDasharray={`${2 * Math.PI * 40}`}
                      strokeDashoffset={`${2 * Math.PI * 40 * (1 - completionPct / 100)}`}
                      strokeLinecap="round"
                      className="transition-all duration-700"
                    />
                  </svg>
                  <div className="absolute inset-0 flex items-center justify-center">
                    <span className="text-xl font-bold text-gray-800">{completionPct}%</span>
                  </div>
                </div>
                <p className="text-sm font-semibold text-gray-700">
                  {completedLessons} of {totalLessons} lessons done
                </p>
                {allLessonsCompleted && (
                  <button
                    onClick={handleComplete}
                    disabled={completing}
                    className="btn-success w-full mt-4"
                  >
                    {completing ? 'Completing...' : '🏆 Mark Complete'}
                  </button>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { getLearningPath, getModules, getRecommendations } from '../../api/learning'
import Header from '../../components/Header'
import ModuleCard from '../../components/ModuleCard'
import WeakAreasPanel from '../../components/WeakAreasPanel'
import { SkeletonModuleCard, SkeletonStats } from '../../components/SkeletonLoader'

const SKILL_TABS = [
  { key: 'all', label: 'All', icon: '📚', color: 'blue' },
  { key: 'listening', label: 'Listening', icon: '🎧', color: 'blue' },
  { key: 'reading', label: 'Reading', icon: '📖', color: 'green' },
  { key: 'writing', label: 'Writing', icon: '✍️', color: 'purple' },
  { key: 'speaking', label: 'Speaking', icon: '🗣️', color: 'orange' },
]

export default function LearningPathDashboard() {
  const navigate = useNavigate()
  const [activeTab, setActiveTab] = useState('all')
  const [learningPath, setLearningPath] = useState(null)
  const [modules, setModules] = useState([])
  const [recommendations, setRecommendations] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    loadData()
  }, [activeTab])

  const loadData = async () => {
    try {
      setLoading(true)
      setError(null)

      const pathRes = await getLearningPath()
      setLearningPath(pathRes.data.data)

      const filters = {}
      if (activeTab !== 'all') {
        filters.skill = activeTab
      }
      const modulesRes = await getModules(filters)
      setModules(modulesRes.data)

      try {
        const recsRes = await getRecommendations()
        setRecommendations(recsRes.data.data)
      } catch (err) {
        console.warn('Could not load recommendations:', err)
      }
    } catch (err) {
      console.error('Error loading learning path:', err)
      setError(err.response?.data?.message || 'Failed to load learning path')
    } finally {
      setLoading(false)
    }
  }

  const handleModuleClick = (moduleId) => {
    navigate(`/learning/module/${moduleId}`)
  }

  const recommendedModuleIds =
    recommendations?.recommendations?.map((r) => r.module_id) || []

  if (loading) {
    return (
      <div className="min-h-screen">
        <Header />
        <div className="max-w-7xl mx-auto px-6 py-8">
          {/* Skeleton for progress cards */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
            {[...Array(4)].map((_, i) => (
              <SkeletonStats key={i} />
            ))}
          </div>
          {/* Skeleton for modules */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {[...Array(6)].map((_, i) => (
              <SkeletonModuleCard key={i} />
            ))}
          </div>
        </div>
      </div>
    )
  }

  if (error && !learningPath) {
    return (
      <div className="min-h-screen">
        <Header />
        <div className="min-h-screen flex items-center justify-center px-4">
          <div className="glass-card p-10 max-w-lg text-center animate-scale-in">
            <div className="w-24 h-24 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-full flex items-center justify-center text-5xl mx-auto mb-6 shadow-2xl">
              📚
            </div>
            <h2 className="text-2xl font-bold text-gray-900 mb-3">
              No Learning Path Yet
            </h2>
            <p className="text-gray-600 mb-8 leading-relaxed">
              Complete a diagnostic test to generate your personalized learning path
              tailored to your strengths and areas for improvement.
            </p>
            <button
              onClick={() => navigate('/learning/diagnostic')}
              className="btn-primary"
            >
              🚀 Start Diagnostic Test
            </button>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen">
      <Header />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-8 animate-fade-in">
        {/* Page Title */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 flex items-center gap-3 mb-2">
            <span className="text-4xl">📚</span>
            <span>Learning Path to CLB 10</span>
          </h1>
          <p className="text-gray-600">
            Personalized modules based on your test performance
          </p>
        </div>

        {/* Progress Overview */}
        {learningPath?.learning_path && (
          <div className="glass-card bg-gradient-to-br from-blue-500 via-indigo-600 to-purple-600 p-8 mb-8 text-white shadow-2xl animate-slide-up">
            <h2 className="text-xl font-bold mb-6 flex items-center gap-2">
              <span>📊</span>
              <span>Your Progress Overview</span>
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
              <div className="bg-white/10 backdrop-blur-lg rounded-xl p-5 border border-white/20">
                <p className="text-blue-100 text-sm mb-2 font-medium">Overall Progress</p>
                <p className="text-4xl font-black">
                  {learningPath.progress?.progress_percentage || 0}%
                </p>
                <div className="mt-3 bg-white/20 rounded-full h-2 overflow-hidden">
                  <div
                    className="bg-white h-full rounded-full transition-all duration-500"
                    style={{ width: `${learningPath.progress?.progress_percentage || 0}%` }}
                  />
                </div>
              </div>
              <div className="bg-white/10 backdrop-blur-lg rounded-xl p-5 border border-white/20">
                <p className="text-blue-100 text-sm mb-2 font-medium">Modules Completed</p>
                <p className="text-4xl font-black">
                  {learningPath.progress?.modules_completed || 0}
                  <span className="text-2xl text-blue-200 ml-1">
                    / {learningPath.progress?.modules_total_recommended || 0}
                  </span>
                </p>
              </div>
              <div className="bg-white/10 backdrop-blur-lg rounded-xl p-5 border border-white/20">
                <p className="text-blue-100 text-sm mb-2 font-medium">In Progress</p>
                <p className="text-4xl font-black">
                  {learningPath.progress?.modules_in_progress || 0}
                </p>
              </div>
              <div className="bg-white/10 backdrop-blur-lg rounded-xl p-5 border border-white/20">
                <p className="text-blue-100 text-sm mb-2 font-medium">Study Time</p>
                <p className="text-4xl font-black">
                  {learningPath.progress?.total_study_hours || 0}
                  <span className="text-2xl text-blue-200 ml-1">hrs</span>
                </p>
              </div>
            </div>
          </div>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main content - Modules */}
          <div className="lg:col-span-2">
            {/* Tabs */}
            <div className="glass-card p-3 mb-6 flex gap-2 overflow-x-auto">
              {SKILL_TABS.map((tab) => (
                <button
                  key={tab.key}
                  onClick={() => setActiveTab(tab.key)}
                  className={`
                    flex items-center gap-2 px-5 py-3 rounded-xl whitespace-nowrap font-semibold text-sm
                    transition-all duration-200 transform
                    ${
                      activeTab === tab.key
                        ? 'bg-gradient-to-r from-primary-600 to-indigo-600 text-white shadow-lg scale-105'
                        : 'bg-gray-100 text-gray-700 hover:bg-gray-200 hover:scale-105'
                    }
                  `}
                >
                  <span className="text-lg">{tab.icon}</span>
                  <span>{tab.label}</span>
                </button>
              ))}
            </div>

            {/* Recommended Section */}
            {recommendations?.recommendations &&
              recommendations.recommendations.length > 0 && (
                <div className="mb-8 animate-slide-up">
                  <div className="flex items-center justify-between mb-4">
                    <h2 className="text-xl font-bold text-gray-900 flex items-center gap-2">
                      <span className="text-2xl">⭐</span>
                      <span>Recommended for You</span>
                    </h2>
                    <span className="badge badge-warning">
                      {recommendations.recommendations.length} modules
                    </span>
                  </div>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {recommendations.recommendations.slice(0, 4).map((rec) => {
                      const module = modules.find((m) => m.id === rec.module_id)
                      if (!module) return null
                      return (
                        <ModuleCard
                          key={module.id}
                          module={module}
                          progress={module.progress}
                          recommended={true}
                        />
                      )
                    })}
                  </div>
                </div>
              )}

            {/* All Modules */}
            <div className="animate-slide-up" style={{ animationDelay: '0.1s' }}>
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-xl font-bold text-gray-900">
                  {activeTab === 'all' ? 'All Modules' : `${SKILL_TABS.find((t) => t.key === activeTab)?.label} Modules`}
                </h2>
                <span className="badge badge-primary">
                  {modules.length} modules
                </span>
              </div>
              {modules.length === 0 ? (
                <div className="glass-card p-12 text-center">
                  <div className="text-6xl mb-4">🔍</div>
                  <h3 className="text-xl font-bold text-gray-800 mb-2">No Modules Found</h3>
                  <p className="text-gray-600">
                    No modules available for this skill yet. Try a different category.
                  </p>
                </div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {modules.map((module, index) => (
                    <div
                      key={module.id}
                      style={{ animationDelay: `${index * 0.05}s` }}
                      className="animate-slide-up"
                    >
                      <ModuleCard
                        module={module}
                        progress={module.progress}
                        recommended={recommendedModuleIds.includes(module.id)}
                      />
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Sidebar - Weak Areas */}
          <div className="lg:col-span-1 animate-slide-up" style={{ animationDelay: '0.2s' }}>
            <WeakAreasPanel
              weakAreas={recommendations?.weak_areas || []}
              onModuleClick={handleModuleClick}
            />
          </div>
        </div>
      </div>
    </div>
  )
}

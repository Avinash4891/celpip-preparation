import React from 'react'
import { useNavigate } from 'react-router-dom'
import ProgressRing from './ProgressRing'

const SKILL_COLORS = {
  listening: {
    border: 'border-blue-400',
    bg: 'bg-gradient-to-br from-blue-50 to-blue-100',
    gradient: 'from-blue-400 to-blue-600',
    text: 'text-blue-700',
  },
  reading: {
    border: 'border-green-400',
    bg: 'bg-gradient-to-br from-green-50 to-green-100',
    gradient: 'from-green-400 to-green-600',
    text: 'text-green-700',
  },
  writing: {
    border: 'border-purple-400',
    bg: 'bg-gradient-to-br from-purple-50 to-purple-100',
    gradient: 'from-purple-400 to-purple-600',
    text: 'text-purple-700',
  },
  speaking: {
    border: 'border-orange-400',
    bg: 'bg-gradient-to-br from-orange-50 to-orange-100',
    gradient: 'from-orange-400 to-orange-600',
    text: 'text-orange-700',
  },
}

const SKILL_ICONS = {
  listening: '🎧',
  reading: '📖',
  writing: '✍️',
  speaking: '🗣️',
}

const LEVEL_CONFIG = {
  1: { label: 'Beginner', color: 'bg-gray-100 text-gray-700' },
  2: { label: 'Intermediate', color: 'bg-blue-100 text-blue-700' },
  3: { label: 'Advanced', color: 'bg-purple-100 text-purple-700' },
  4: { label: 'Mastery', color: 'bg-yellow-100 text-yellow-700' },
}

const STATUS_CONFIG = {
  completed: { icon: '✓', label: 'Completed', color: 'text-green-600' },
  in_progress: { icon: '🔄', label: 'In Progress', color: 'text-blue-600' },
  not_started: { icon: '○', label: 'Not Started', color: 'text-gray-400' },
}

export default function ModuleCard({ module, progress, recommended = false }) {
  const navigate = useNavigate()

  const isLocked = module.is_locked || false
  const completionPct = module.lessons_count > 0
    ? (module.completed_lessons_count / module.lessons_count) * 100
    : 0

  const skillColors = SKILL_COLORS[module.skill]
  const levelConfig = LEVEL_CONFIG[module.level]
  const statusConfig = progress ? STATUS_CONFIG[progress.status] : null

  const handleClick = () => {
    if (!isLocked) {
      navigate(`/learning/module/${module.id}`)
    }
  }

  return (
    <div
      onClick={handleClick}
      className={`
        relative bg-white border-2 rounded-2xl p-5 transition-all duration-300 group
        ${skillColors.border}
        ${isLocked
          ? 'opacity-60 cursor-not-allowed grayscale'
          : 'cursor-pointer hover:shadow-2xl hover:-translate-y-2 hover:scale-105'
        }
        ${recommended ? 'ring-4 ring-yellow-300 shadow-lg' : 'shadow-md'}
      `}
    >
      {/* Background gradient overlay */}
      <div className={`absolute inset-0 ${skillColors.bg} rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none`} />

      {/* Lock icon overlay */}
      {isLocked && (
        <div className="absolute top-3 right-3 w-10 h-10 bg-gray-800/80 backdrop-blur-lg rounded-full flex items-center justify-center text-xl shadow-xl">
          🔒
        </div>
      )}

      {/* Recommended badge */}
      {recommended && !isLocked && (
        <div className="absolute -top-3 -right-3 bg-gradient-to-r from-yellow-400 to-orange-400 text-white text-xs font-bold px-3 py-1.5 rounded-full shadow-lg transform group-hover:scale-110 transition-transform">
          ⭐ Recommended
        </div>
      )}

      {/* Header */}
      <div className="relative flex items-start justify-between mb-4">
        <div className="flex-1">
          <div className="flex items-center gap-2 mb-2">
            <div className={`w-10 h-10 bg-gradient-to-br ${skillColors.gradient} rounded-lg flex items-center justify-center text-xl shadow-md group-hover:scale-110 transition-transform`}>
              {SKILL_ICONS[module.skill]}
            </div>
            <div>
              <span className="text-xs font-bold text-gray-500 uppercase tracking-wide">
                {module.skill}
              </span>
              <div className={`${levelConfig.color} text-xs font-semibold px-2 py-0.5 rounded-full inline-block ml-2`}>
                {levelConfig.label}
              </div>
            </div>
          </div>
          <h3 className="font-bold text-gray-900 text-base leading-tight group-hover:text-primary-600 transition-colors">
            {module.title}
          </h3>
        </div>

        {/* Progress ring */}
        {progress && progress.status !== 'not_started' && !isLocked && (
          <div className="ml-3 relative">
            <ProgressRing
              percentage={completionPct}
              size={60}
              strokeWidth={6}
            />
          </div>
        )}
      </div>

      {/* Description */}
      <p className="relative text-sm text-gray-600 mb-4 line-clamp-2 leading-relaxed">
        {module.description}
      </p>

      {/* Learning Objectives Preview */}
      {module.learning_objectives && module.learning_objectives.length > 0 && (
        <div className="relative mb-4 p-3 bg-white/50 backdrop-blur-sm rounded-lg border border-gray-200">
          <p className="text-xs font-semibold text-gray-700 mb-1">Learning Goals:</p>
          <ul className="text-xs text-gray-600 space-y-1">
            {module.learning_objectives.slice(0, 2).map((obj, idx) => (
              <li key={idx} className="flex items-start gap-1">
                <span className="text-green-500 mt-0.5">•</span>
                <span className="line-clamp-1">{obj}</span>
              </li>
            ))}
            {module.learning_objectives.length > 2 && (
              <li className="text-gray-400 italic">+{module.learning_objectives.length - 2} more...</li>
            )}
          </ul>
        </div>
      )}

      {/* Footer */}
      <div className="relative flex items-center justify-between text-xs border-t border-gray-200 pt-3 mb-3">
        <div className="flex items-center gap-2">
          {/* Category badge */}
          <span className="px-2 py-1 bg-gray-100 rounded-lg font-medium text-gray-700 capitalize">
            {module.category.replace('_', ' ')}
          </span>
        </div>

        {/* Duration */}
        {module.estimated_duration_mins && (
          <div className="flex items-center gap-1 text-gray-600">
            <span>⏱️</span>
            <span className="font-semibold">{module.estimated_duration_mins} min</span>
          </div>
        )}
      </div>

      {/* Status indicator */}
      {progress && statusConfig && (
        <div className="relative">
          <div className="flex items-center justify-between">
            <span className={`flex items-center gap-2 text-sm font-semibold ${statusConfig.color}`}>
              <span>{statusConfig.icon}</span>
              <span>{statusConfig.label}</span>
            </span>
            {progress.mastery_level > 0 && (
              <div className="flex items-center gap-2">
                <span className="text-xs text-gray-500">Mastery:</span>
                <span className="text-sm font-bold text-primary-700">
                  {progress.mastery_level}%
                </span>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Locked overlay message */}
      {isLocked && (
        <div className="relative mt-3 p-2 bg-gray-800/90 backdrop-blur-lg rounded-lg text-center">
          <p className="text-xs text-white font-medium">
            🔒 Complete prerequisites to unlock
          </p>
        </div>
      )}

      {/* Hover arrow indicator */}
      {!isLocked && (
        <div className="absolute bottom-4 right-4 text-gray-400 group-hover:text-primary-600 opacity-0 group-hover:opacity-100 transform translate-x-2 group-hover:translate-x-0 transition-all">
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
          </svg>
        </div>
      )}
    </div>
  )
}

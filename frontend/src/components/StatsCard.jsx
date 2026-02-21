import React from 'react'

const STAT_VARIANTS = {
  primary: 'from-blue-500 to-blue-600',
  success: 'from-green-500 to-green-600',
  warning: 'from-amber-500 to-amber-600',
  danger: 'from-red-500 to-red-600',
  info: 'from-indigo-500 to-indigo-600',
  purple: 'from-purple-500 to-purple-600',
}

export default function StatsCard({
  icon,
  label,
  value,
  change,
  variant = 'primary',
  suffix = '',
  onClick,
}) {
  const gradient = STAT_VARIANTS[variant] || STAT_VARIANTS.primary
  const isClickable = !!onClick

  return (
    <div
      onClick={onClick}
      className={`
        stats-card group relative overflow-hidden
        ${isClickable ? 'cursor-pointer hover:shadow-xl transform hover:-translate-y-1' : ''}
        transition-all duration-300
      `}
    >
      {/* Background gradient overlay */}
      <div
        className={`
          absolute top-0 right-0 w-24 h-24 bg-gradient-to-br ${gradient}
          opacity-10 rounded-full blur-2xl transform translate-x-8 -translate-y-8
          group-hover:scale-150 transition-transform duration-500
        `}
      />

      <div className="relative">
        {/* Icon and Label */}
        <div className="flex items-start justify-between mb-3">
          <div>
            <p className="text-sm text-gray-600 font-medium mb-1">{label}</p>
            <div className="flex items-baseline gap-2">
              <p className="text-3xl font-bold text-gray-900">
                {value}
                {suffix && <span className="text-lg text-gray-600 ml-1">{suffix}</span>}
              </p>
            </div>
          </div>
          <div className={`w-12 h-12 bg-gradient-to-br ${gradient} rounded-xl flex items-center justify-center text-white text-2xl shadow-lg`}>
            {icon}
          </div>
        </div>

        {/* Change indicator */}
        {change !== undefined && change !== null && (
          <div className="flex items-center gap-2">
            <div
              className={`
                flex items-center gap-1 text-sm font-semibold px-2 py-1 rounded-full
                ${change >= 0 ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'}
              `}
            >
              {change >= 0 ? (
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 10l7-7m0 0l7 7m-7-7v18" />
                </svg>
              ) : (
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                </svg>
              )}
              <span>{Math.abs(change)}%</span>
            </div>
            <span className="text-xs text-gray-500">vs last test</span>
          </div>
        )}

        {/* Click indicator */}
        {isClickable && (
          <div className="absolute bottom-2 right-2 text-gray-400 group-hover:text-primary-600 transition-colors">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </div>
        )}
      </div>
    </div>
  )
}

// Preset stat cards for common metrics
export function OverallScoreCard({ score, change, onClick }) {
  return (
    <StatsCard
      icon="🎯"
      label="Overall Score"
      value={score || 'N/A'}
      change={change}
      variant="primary"
      onClick={onClick}
    />
  )
}

export function ListeningScoreCard({ score, change, onClick }) {
  return (
    <StatsCard
      icon="🎧"
      label="Listening"
      value={score || 'N/A'}
      change={change}
      variant="info"
      onClick={onClick}
    />
  )
}

export function ReadingScoreCard({ score, change, onClick }) {
  return (
    <StatsCard
      icon="📖"
      label="Reading"
      value={score || 'N/A'}
      change={change}
      variant="success"
      onClick={onClick}
    />
  )
}

export function WritingScoreCard({ score, change, onClick }) {
  return (
    <StatsCard
      icon="✍️"
      label="Writing"
      value={score || 'N/A'}
      change={change}
      variant="purple"
      onClick={onClick}
    />
  )
}

export function SpeakingScoreCard({ score, change, onClick }) {
  return (
    <StatsCard
      icon="🎤"
      label="Speaking"
      value={score || 'N/A'}
      change={change}
      variant="warning"
      onClick={onClick}
    />
  )
}

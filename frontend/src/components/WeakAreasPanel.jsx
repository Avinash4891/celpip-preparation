import React from 'react'
import { useNavigate } from 'react-router-dom'

const SKILL_COLORS = {
  listening: 'bg-blue-100 text-blue-800 border-blue-300',
  reading: 'bg-green-100 text-green-800 border-green-300',
  writing: 'bg-purple-100 text-purple-800 border-purple-300',
  speaking: 'bg-orange-100 text-orange-800 border-orange-300',
}

const getSeverityColor = (severity) => {
  if (severity >= 0.7) return 'bg-red-500'
  if (severity >= 0.4) return 'bg-yellow-500'
  return 'bg-blue-500'
}

const getSeverityLabel = (severity) => {
  if (severity >= 0.7) return 'High'
  if (severity >= 0.4) return 'Medium'
  return 'Low'
}

export default function WeakAreasPanel({ weakAreas = [], onModuleClick }) {
  const navigate = useNavigate()

  if (!weakAreas || weakAreas.length === 0) {
    return (
      <div className="bg-white rounded-lg shadow p-6 border border-gray-200">
        <h2 className="text-lg font-bold text-gray-800 mb-3">
          📊 Weak Areas
        </h2>
        <div className="text-center py-8">
          <p className="text-gray-500 text-sm">
            No weak areas identified yet.
          </p>
          <p className="text-gray-400 text-xs mt-2">
            Complete a diagnostic test to get personalized recommendations.
          </p>
        </div>
      </div>
    )
  }

  return (
    <div className="bg-white rounded-lg shadow p-6 border border-gray-200">
      <h2 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
        <span>📊</span>
        <span>Areas for Improvement</span>
      </h2>

      <div className="space-y-3">
        {weakAreas.slice(0, 5).map((weakArea, index) => (
          <div
            key={weakArea.id || index}
            className="border border-gray-200 rounded-lg p-3 hover:bg-gray-50 transition"
          >
            {/* Header */}
            <div className="flex items-start justify-between mb-2">
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <span
                    className={`
                      text-xs font-semibold px-2 py-1 rounded border
                      ${SKILL_COLORS[weakArea.skill] || 'bg-gray-100 text-gray-800 border-gray-300'}
                    `}
                  >
                    {weakArea.skill?.toUpperCase()}
                  </span>
                  <span
                    className={`
                      text-xs font-medium px-2 py-1 rounded text-white
                      ${getSeverityColor(weakArea.severity)}
                    `}
                  >
                    {getSeverityLabel(weakArea.severity)} Priority
                  </span>
                </div>
                <h3 className="font-semibold text-gray-800 text-sm capitalize">
                  {weakArea.area?.replace(/_/g, ' ')}
                </h3>
              </div>
            </div>

            {/* Severity indicator */}
            <div className="mb-2">
              <div className="w-full bg-gray-200 rounded-full h-1.5">
                <div
                  className={`h-1.5 rounded-full transition-all ${getSeverityColor(weakArea.severity)}`}
                  style={{ width: `${weakArea.severity * 100}%` }}
                />
              </div>
            </div>

            {/* Recommended modules */}
            {weakArea.recommended_modules && weakArea.recommended_modules.length > 0 && (
              <div className="mt-2">
                <p className="text-xs text-gray-500 mb-1">Recommended modules:</p>
                <div className="flex flex-wrap gap-1">
                  {weakArea.recommended_modules.slice(0, 2).map((moduleId) => (
                    <button
                      key={moduleId}
                      onClick={() => {
                        if (onModuleClick) {
                          onModuleClick(moduleId)
                        } else {
                          navigate(`/learning/module/${moduleId}`)
                        }
                      }}
                      className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded hover:bg-blue-200 transition"
                    >
                      Module #{moduleId}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Identified date */}
            {weakArea.identified_at && (
              <p className="text-xs text-gray-400 mt-2">
                Identified: {new Date(weakArea.identified_at).toLocaleDateString()}
              </p>
            )}
          </div>
        ))}
      </div>

      {weakAreas.length > 5 && (
        <div className="mt-3 text-center">
          <p className="text-xs text-gray-500">
            Showing 5 of {weakAreas.length} areas
          </p>
        </div>
      )}
    </div>
  )
}

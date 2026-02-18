import React from 'react'

const SCORE_COLOR = (score) => {
  if (score >= 10) return 'bg-green-500'
  if (score >= 8) return 'bg-blue-500'
  if (score >= 6) return 'bg-yellow-500'
  return 'bg-red-500'
}

const CLB_LABEL = {
  12: 'CLB 12 — Advanced',
  11: 'CLB 11 — Advanced',
  10: 'CLB 10 — Highly Effective',
  9: 'CLB 9 — Effective',
  8: 'CLB 8 — Good',
  7: 'CLB 7 — Adequate',
  6: 'CLB 6 — Developing',
  5: 'CLB 5 — Developing',
  4: 'CLB 4 — Basic',
}

export default function ScoreCard({ section, score, rubric }) {
  return (
    <div className="bg-white rounded-xl border border-gray-200 shadow p-6">
      <div className="flex items-center gap-4 mb-4">
        <div className={`score-badge ${SCORE_COLOR(score)}`}>{score ?? '—'}</div>
        <div>
          <h3 className="font-bold text-lg capitalize">{section}</h3>
          <p className="text-sm text-gray-500">{score ? (CLB_LABEL[Math.round(score)] ?? 'Score') : 'Not attempted'}</p>
        </div>
      </div>

      {rubric && (
        <div className="space-y-2">
          {Object.entries(rubric).map(([dim, val]) => (
            <div key={dim} className="flex items-center gap-3">
              <span className="w-36 text-xs text-gray-600 capitalize shrink-0">{dim.replace(/_/g, ' ')}</span>
              <div className="flex-1 bg-gray-100 rounded-full h-2">
                <div
                  className={`h-2 rounded-full ${SCORE_COLOR(val)}`}
                  style={{ width: `${(val / 12) * 100}%` }}
                />
              </div>
              <span className="text-xs font-bold text-gray-700 w-5 text-right">{val}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

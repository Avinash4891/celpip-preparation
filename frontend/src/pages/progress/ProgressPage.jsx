import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { getProgressSummary, getProgressHistory } from '../../api/questions'
import ScoreCard from '../../components/ScoreCard'

const SECTIONS = ['listening', 'reading', 'writing', 'speaking']

const CLB_LABEL = (score) => {
  if (!score) return '—'
  if (score >= 10) return 'CLB 10+ ✓ Target reached'
  if (score >= 8) return `CLB ${Math.round(score)} — Good`
  return `CLB ${Math.round(score)} — Keep practising`
}

export default function ProgressPage() {
  const navigate = useNavigate()
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    Promise.all([getProgressSummary(), getProgressHistory()])
      .then(([summary, history]) => {
        setData({ summary: summary.data.data, history: history.data.data || [] })
      })
      .catch(() => setData({ summary: {}, history: [] }))
      .finally(() => setLoading(false))
  }, [])

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="w-10 h-10 border-4 border-primary-500 border-t-transparent rounded-full animate-spin" />
      </div>
    )
  }

  // summary shape: { listening: { latest_score, average_score, ... }, reading: { ... }, ... }
  const summary = data?.summary || {}
  const history = data?.history || []
  const latestScore = (section) => summary[section]?.latest_score ?? null

  return (
    <div className="min-h-screen bg-exam-bg pb-16">
      <div className="bg-primary-900 text-white px-6 py-4 flex items-center gap-4">
        <h1 className="text-xl font-bold">Progress & Scores</h1>
        <button onClick={() => navigate('/')} className="ml-auto text-blue-200 hover:text-white text-sm underline">
          ← Dashboard
        </button>
      </div>

      <div className="max-w-4xl mx-auto px-4 pt-6 space-y-6">
        {/* Section score cards */}
        <div>
          <h2 className="text-lg font-bold text-gray-700 mb-3">Latest Scores</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {SECTIONS.map((s) => (
              <ScoreCard key={s} section={s} score={latestScore(s)} rubric={null} />
            ))}
          </div>
        </div>

        {/* CLB summary */}
        <div className="bg-white rounded-xl border border-gray-200 shadow p-5">
          <h2 className="text-lg font-bold text-gray-700 mb-3">CLB Level Summary</h2>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            {SECTIONS.map((s) => (
              <div key={s} className="text-center">
                <p className="text-xs text-gray-400 uppercase mb-1 capitalize">{s}</p>
                <div className="text-3xl font-black text-primary-700">{latestScore(s) ?? '—'}</div>
                <p className="text-xs text-gray-500 mt-1">{CLB_LABEL(latestScore(s))}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Session history */}
        {history.length > 0 && (
          <div className="bg-white rounded-xl border border-gray-200 shadow p-5">
            <h2 className="text-lg font-bold text-gray-700 mb-3">Recent Sessions</h2>
            <table className="w-full text-sm">
              <thead>
                <tr className="text-left text-gray-400 border-b">
                  <th className="pb-2">Section</th>
                  <th className="pb-2">Score</th>
                  <th className="pb-2">Date</th>
                </tr>
              </thead>
              <tbody>
                {history.map((h, i) => (
                  <tr key={i} className="border-b last:border-0">
                    <td className="py-2 capitalize">{h.section}</td>
                    <td className="py-2 font-bold text-primary-700">{h.score ?? '—'}</td>
                    <td className="py-2 text-gray-400">
                      {h.completed_at
                        ? new Date(h.completed_at).toLocaleDateString('en-CA')
                        : 'In progress'}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {/* Study plan tips */}
        <div className="bg-primary-50 border border-primary-200 rounded-xl p-5">
          <h2 className="text-lg font-bold text-primary-800 mb-2">2-Week Study Plan</h2>
          <ul className="text-sm text-primary-700 space-y-1">
            <li>• Days 1–2: Diagnostic test in all 4 sections</li>
            <li>• Days 3–4: Listening — news items, Parts 1–3 practice</li>
            <li>• Days 5–6: Reading — skimming, scanning techniques</li>
            <li>• Day 7: Full timed Listening + Reading mock test</li>
            <li>• Days 8–9: Writing — email structure, survey templates</li>
            <li>• Days 10–11: Speaking — all 8 task types (PREP structure)</li>
            <li>• Days 12–13: Full mock tests, targeted weak-area review</li>
            <li>• Day 14: Final diagnostic — measure against CLB 10</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

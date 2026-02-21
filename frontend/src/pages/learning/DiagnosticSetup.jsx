import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { createLearningPath } from '../../api/learning'

const TEST_SECTIONS = [
  {
    key: 'listening',
    title: 'Listening Test',
    icon: '🎧',
    path: '/listening',
    desc: 'Complete a listening practice test to identify comprehension weak areas',
    color: 'border-blue-400 bg-blue-50',
  },
  {
    key: 'reading',
    title: 'Reading Test',
    icon: '📖',
    path: '/reading',
    desc: 'Complete a reading practice test to identify comprehension weak areas',
    color: 'border-green-400 bg-green-50',
  },
  {
    key: 'writing',
    title: 'Writing Test',
    icon: '✍️',
    path: '/writing',
    desc: 'Complete a writing test to get AI feedback on your responses',
    color: 'border-purple-400 bg-purple-50',
  },
  {
    key: 'speaking',
    title: 'Speaking Test',
    icon: '🗣️',
    path: '/speaking',
    desc: 'Complete a speaking test to get AI feedback on your responses',
    color: 'border-orange-400 bg-orange-50',
  },
]

export default function DiagnosticSetup() {
  const navigate = useNavigate()
  const [generating, setGenerating] = useState(false)
  const [selectedSession, setSelectedSession] = useState(null)
  const [error, setError] = useState(null)
  const [analysisResult, setAnalysisResult] = useState(null)

  const handleGeneratePath = async () => {
    if (!selectedSession) {
      setError('Please enter a test session ID')
      return
    }

    try {
      setGenerating(true)
      setError(null)

      const res = await createLearningPath(parseInt(selectedSession), 10)
      setAnalysisResult(res.data.data)

      // Redirect to dashboard after 3 seconds
      setTimeout(() => {
        navigate('/learning')
      }, 3000)
    } catch (err) {
      console.error('Error generating learning path:', err)
      setError(
        err.response?.data?.detail ||
          'Failed to generate learning path. Please ensure you have completed a test.'
      )
    } finally {
      setGenerating(false)
    }
  }

  if (analysisResult) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center p-6">
        <div className="bg-white rounded-lg shadow-xl p-8 max-w-2xl w-full">
          <div className="text-center mb-6">
            <div className="text-6xl mb-4 animate-bounce">🎯</div>
            <h2 className="text-2xl font-bold text-gray-800 mb-2">
              Learning Path Generated!
            </h2>
            <p className="text-gray-600">
              Your personalized study plan is ready
            </p>
          </div>

          {/* Analysis Summary */}
          <div className="space-y-4 mb-6">
            {/* Weak Areas */}
            {analysisResult.weak_areas && analysisResult.weak_areas.length > 0 && (
              <div className="bg-red-50 border border-red-200 rounded-lg p-4">
                <h3 className="font-semibold text-red-800 mb-2">
                  Areas for Improvement ({analysisResult.weak_areas.length})
                </h3>
                <ul className="list-disc list-inside text-sm text-red-700 space-y-1">
                  {analysisResult.weak_areas.slice(0, 5).map((area, idx) => (
                    <li key={idx}>
                      {area.skill}: {area.area?.replace(/_/g, ' ')}
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Strengths */}
            {analysisResult.strengths && analysisResult.strengths.length > 0 && (
              <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                <h3 className="font-semibold text-green-800 mb-2">
                  Your Strengths ({analysisResult.strengths.length})
                </h3>
                <ul className="list-disc list-inside text-sm text-green-700 space-y-1">
                  {analysisResult.strengths.slice(0, 5).map((strength, idx) => (
                    <li key={idx}>{strength}</li>
                  ))}
                </ul>
              </div>
            )}

            {/* Recommended Modules */}
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
              <h3 className="font-semibold text-blue-800 mb-2">
                Recommended Modules: {analysisResult.recommended_modules?.length || 0}
              </h3>
              <p className="text-sm text-blue-700">
                Estimated completion time:{' '}
                {analysisResult.estimated_completion_hours || 0} hours
              </p>
            </div>
          </div>

          <p className="text-center text-sm text-gray-500">
            Redirecting to your learning path in 3 seconds...
          </p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-5xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-gray-800">
                Generate Your Learning Path
              </h1>
              <p className="text-sm text-gray-600 mt-1">
                Complete a diagnostic test to get personalized module recommendations
              </p>
            </div>
            <button
              onClick={() => navigate('/dashboard')}
              className="text-gray-600 hover:text-gray-800 text-sm"
            >
              ← Back
            </button>
          </div>
        </div>
      </header>

      <div className="max-w-5xl mx-auto px-6 py-8">
        {/* Instructions */}
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 mb-8">
          <h2 className="font-bold text-blue-800 mb-2 flex items-center gap-2">
            <span>💡</span>
            <span>How it Works</span>
          </h2>
          <ol className="list-decimal list-inside text-sm text-blue-700 space-y-2 ml-2">
            <li>
              Complete a practice test in any section (Listening, Reading, Writing, or
              Speaking)
            </li>
            <li>Note your test session ID from the results page</li>
            <li>Enter the session ID below to generate your personalized learning path</li>
            <li>
              Our AI will analyze your performance and recommend modules tailored to your
              weak areas
            </li>
          </ol>
        </div>

        {/* Test Section Cards */}
        <div className="mb-8">
          <h2 className="text-lg font-bold text-gray-800 mb-4">
            Step 1: Take a Diagnostic Test
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {TEST_SECTIONS.map((section) => (
              <div
                key={section.key}
                className={`border-2 rounded-lg p-6 ${section.color} hover:shadow-lg transition cursor-pointer`}
                onClick={() => navigate(section.path)}
              >
                <div className="flex items-center gap-3 mb-3">
                  <span className="text-3xl">{section.icon}</span>
                  <h3 className="font-bold text-gray-800">{section.title}</h3>
                </div>
                <p className="text-sm text-gray-600">{section.desc}</p>
                <div className="mt-4">
                  <button className="text-sm font-medium text-blue-600 hover:text-blue-800">
                    Start Test →
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Generate Path Section */}
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-lg font-bold text-gray-800 mb-4">
            Step 2: Generate Your Learning Path
          </h2>
          <p className="text-sm text-gray-600 mb-4">
            After completing a test, enter your test session ID to generate a
            personalized learning path.
          </p>

          <div className="flex gap-3">
            <input
              type="number"
              placeholder="Enter test session ID (e.g., 123)"
              value={selectedSession || ''}
              onChange={(e) => setSelectedSession(e.target.value)}
              className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              onClick={handleGeneratePath}
              disabled={generating || !selectedSession}
              className={`
                px-6 py-2 rounded-lg font-medium transition
                ${
                  generating || !selectedSession
                    ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                    : 'bg-blue-600 text-white hover:bg-blue-700'
                }
              `}
            >
              {generating ? 'Analyzing...' : 'Generate Path'}
            </button>
          </div>

          {error && (
            <div className="mt-4 bg-red-50 border border-red-200 rounded-lg p-4">
              <p className="text-sm text-red-700">{error}</p>
            </div>
          )}

          <div className="mt-6 bg-gray-50 rounded-lg p-4 border border-gray-200">
            <p className="text-xs text-gray-600">
              <strong>Tip:</strong> You can find your test session ID on the results page
              after completing any test. The learning path will be customized based on
              your performance in that test.
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}

import React, { useEffect, useState, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import ExamTimer from '../../components/ExamTimer'
import ProgressBar from '../../components/ProgressBar'
import {
  startReadingSession,
  getReadingQuestions,
  submitReadingAnswer,
  completeReadingSession,
} from '../../api/questions'

const PARTS = [1, 2, 3, 4]
const PART_TITLES = {
  1: 'Reading Correspondence',
  2: 'Reading to Apply a Diagram',
  3: 'Reading for Information',
  4: 'Reading for Viewpoints',
}
const TOTAL_SECONDS = 55 * 60
const OPTION_LETTERS = ['A', 'B', 'C', 'D']

export default function ReadingTest() {
  const navigate = useNavigate()
  const [phase, setPhase] = useState('intro')
  const sessionIdRef = useRef(null)
  const [questions, setQuestions] = useState([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [answerResults, setAnswerResults] = useState({})
  const [pending, setPending] = useState(null)
  const [finalScore, setFinalScore] = useState(null)
  const [loadError, setLoadError] = useState('')
  const startTimeRef = useRef(Date.now())

  const currentQ = questions[currentIndex]

  useEffect(() => {
    if (phase !== 'test') return
    const load = async () => {
      try {
        const all = []
        for (const part of PARTS) {
          const res = await getReadingQuestions(part)
          all.push(...(res.data || []))
        }
        setQuestions(all)
      } catch {
        setLoadError('Could not load questions. Is the backend running?')
      }
    }
    load()
  }, [phase])

  useEffect(() => {
    if (phase === 'test') startTimeRef.current = Date.now()
  }, [currentIndex, phase])

  const start = async () => {
    try {
      const res = await startReadingSession()
      sessionIdRef.current = res.data.id
    } catch {}
    setPhase('test')
  }

  const selectOption = async (letter) => {
    if (pending || answerResults[currentQ.id]) return
    setPending(letter)
    const timeTaken = (Date.now() - startTimeRef.current) / 1000
    try {
      if (sessionIdRef.current) {
        const res = await submitReadingAnswer(sessionIdRef.current, currentQ.id, letter, timeTaken)
        setAnswerResults((prev) => ({ ...prev, [currentQ.id]: { ...res.data, selected: letter } }))
      } else {
        setAnswerResults((prev) => ({ ...prev, [currentQ.id]: { selected: letter, offline: true } }))
      }
    } catch {
      setAnswerResults((prev) => ({ ...prev, [currentQ.id]: { selected: letter, offline: true } }))
    } finally {
      setPending(null)
    }
  }

  const next = () => {
    if (currentIndex < questions.length - 1) setCurrentIndex((i) => i + 1)
    else finish()
  }

  const finish = async () => {
    let score = null
    if (sessionIdRef.current) {
      try {
        const res = await completeReadingSession(sessionIdRef.current)
        score = res.data.score
      } catch {}
    }
    if (score === null) {
      const correct = Object.values(answerResults).filter((r) => r.is_correct).length
      score = Math.round((correct / Math.max(questions.length, 1)) * 12)
    }
    setFinalScore(score)
    setPhase('results')
  }

  if (phase === 'intro') {
    return (
      <div className="min-h-screen flex items-center justify-center bg-exam-bg">
        <div className="bg-white rounded-2xl shadow-lg p-8 max-w-lg w-full">
          <h1 className="text-2xl font-bold text-primary-900 mb-3">Reading Test</h1>
          <ul className="text-sm text-gray-600 space-y-2 mb-6">
            <li>• 4 parts — 38 questions total</li>
            <li>• Total time: 55–60 minutes</li>
            <li>• Passage appears on the left, questions on the right</li>
            <li>• All questions are multiple choice (4 options)</li>
          </ul>
          <button onClick={start} className="btn-primary w-full">Begin Reading Test</button>
          <button onClick={() => navigate('/')} className="btn-secondary w-full mt-2">Back to Dashboard</button>
        </div>
      </div>
    )
  }

  if (phase === 'results') {
    const correct = Object.values(answerResults).filter((r) => r.is_correct).length
    return (
      <div className="min-h-screen flex items-center justify-center bg-exam-bg">
        <div className="bg-white rounded-2xl shadow-lg p-8 max-w-md w-full text-center">
          <h2 className="text-2xl font-bold mb-2">Reading Complete</h2>
          <div className="text-6xl font-black text-primary-700 my-4">{finalScore ?? '—'}</div>
          <p className="text-gray-600 mb-2">Estimated CELPIP Score (1–12)</p>
          <p className="text-gray-500 text-sm mb-6">{correct} correct out of {questions.length}</p>
          <button onClick={() => navigate('/')} className="btn-primary w-full">Back to Dashboard</button>
        </div>
      </div>
    )
  }

  if (!currentQ) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        {loadError
          ? <p className="text-red-600">{loadError}</p>
          : <div className="w-10 h-10 border-4 border-primary-500 border-t-transparent rounded-full animate-spin" />
        }
      </div>
    )
  }

  const result = answerResults[currentQ.id]
  const answered = Boolean(result)
  const options = currentQ.options || []

  return (
    <div className="min-h-screen bg-exam-bg pb-10">
      <ExamTimer totalSeconds={TOTAL_SECONDS} onExpire={finish} />

      <div className="bg-primary-900 text-white px-6 py-3 flex items-center gap-4">
        <span className="font-bold">Reading — Part {currentQ.part}: {PART_TITLES[currentQ.part]}</span>
        <div className="ml-auto text-sm text-blue-200">Question {currentIndex + 1} / {questions.length}</div>
      </div>

      <div className="max-w-7xl mx-auto px-4 pt-4">
        <ProgressBar current={currentIndex + 1} total={questions.length} />

        <div className="mt-4 grid grid-cols-1 lg:grid-cols-2 gap-4" style={{ minHeight: '70vh' }}>
          {/* Passage */}
          <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-5 overflow-y-auto" style={{ maxHeight: '75vh' }}>
            <p className="text-xs text-gray-400 uppercase tracking-wide mb-3 font-semibold">
              Part {currentQ.part} — {PART_TITLES[currentQ.part]}
            </p>
            <div className="text-sm text-gray-700 leading-relaxed whitespace-pre-wrap">
              {currentQ.passage_text}
            </div>
          </div>

          {/* Question panel */}
          <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-5 overflow-y-auto" style={{ maxHeight: '75vh' }}>
            <p className="text-xs text-gray-400 uppercase tracking-wide mb-2 font-semibold">
              Question {currentQ.question_number}
            </p>
            <p className="text-gray-800 font-medium mb-4">{currentQ.question_text}</p>

            <div className="space-y-2">
              {options.map((opt, i) => {
                const letter = OPTION_LETTERS[i]
                const isSelected = result?.selected === letter
                const isCorrect = answered && !result?.offline && letter === result?.correct_answer
                const isWrong = answered && isSelected && !result?.offline && !result?.is_correct
                return (
                  <button
                    key={letter}
                    onClick={() => selectOption(letter)}
                    disabled={answered || Boolean(pending)}
                    className={`option-btn ${isSelected ? 'selected' : ''} ${isCorrect ? 'correct' : ''} ${isWrong ? 'incorrect' : ''}`}
                  >
                    {pending === letter && (
                      <span className="inline-block w-3 h-3 mr-2 border-2 border-blue-500 border-t-transparent rounded-full animate-spin align-middle" />
                    )}
                    <span className="font-bold mr-2">{letter})</span> {opt}
                  </button>
                )
              })}
            </div>

            {answered && result?.explanation && (
              <div className="mt-4 bg-blue-50 border border-blue-200 rounded p-3 text-sm text-blue-800">
                <strong>Explanation:</strong> {result.explanation}
              </div>
            )}

            {answered && (
              <button onClick={next} className="btn-primary mt-4 w-full">
                {currentIndex < questions.length - 1 ? 'Next Question →' : 'Finish Test'}
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

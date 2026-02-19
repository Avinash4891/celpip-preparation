import React, { useEffect, useState, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import ExamTimer from '../../components/ExamTimer'
import {
  startWritingSession,
  getWritingPrompt,
  submitWritingResponse,
} from '../../api/questions'

const TASK_TIMES = { 1: 27 * 60, 2: 26 * 60 }
const MIN_WORDS = 150
const MAX_WORDS = 200
const TASK_NUMS = [1, 2]

function countWords(text) {
  return text.trim().split(/\s+/).filter(Boolean).length
}

export default function WritingTest() {
  const navigate = useNavigate()
  const [phase, setPhase] = useState('intro')
  const sessionIdRef = useRef(null)
  const [prompts, setPrompts] = useState({})       // { 1: {...}, 2: {...} }
  const [taskIndex, setTaskIndex] = useState(0)    // 0 or 1
  const [text, setText] = useState('')
  const [submitted, setSubmitted] = useState([])
  const [loadError, setLoadError] = useState('')

  const taskNum = TASK_NUMS[taskIndex]
  const currentPrompt = prompts[taskNum]
  const wordCount = countWords(text)
  const isUnder = wordCount < MIN_WORDS
  const isOver = wordCount > MAX_WORDS
  const counterClass = isOver ? 'over' : isUnder ? 'under' : 'ok'

  useEffect(() => {
    if (phase !== 'task') return
    const load = async () => {
      try {
        const [p1, p2] = await Promise.all([getWritingPrompt(1), getWritingPrompt(2)])
        setPrompts({ 1: p1.data.data, 2: p2.data.data })
      } catch {
        setLoadError('Could not load writing prompts. Is the backend running?')
      }
    }
    load()
  }, [phase])

  const start = async () => {
    try {
      const res = await startWritingSession()
      sessionIdRef.current = res.data.id
    } catch {}
    setPhase('task')
  }

  const submitTask = async () => {
    if (sessionIdRef.current) {
      try {
        await submitWritingResponse(sessionIdRef.current, taskNum, text)
      } catch {}
    }
    setSubmitted((prev) => [...prev, { taskNum, text, wordCount }])

    if (taskIndex < TASK_NUMS.length - 1) {
      setTaskIndex((i) => i + 1)
      setText('')
    } else {
      setPhase('results')
    }
  }

  if (phase === 'intro') {
    return (
      <div className="min-h-screen flex items-center justify-center bg-exam-bg">
        <div className="bg-white rounded-2xl shadow-lg p-8 max-w-lg w-full">
          <h1 className="text-2xl font-bold text-primary-900 mb-3">Writing Test</h1>
          <ul className="text-sm text-gray-600 space-y-2 mb-6">
            <li>• Task 1: Write an email (27 minutes)</li>
            <li>• Task 2: Respond to a survey question (26 minutes)</li>
            <li>• Each task: 150–200 words</li>
            <li>• Word counter turns amber (under) or red (over limit)</li>
            <li>• AI feedback provided after submission</li>
          </ul>
          <button onClick={start} className="btn-primary w-full">Begin Writing Test</button>
          <button onClick={() => navigate('/')} className="btn-secondary w-full mt-2">Back to Dashboard</button>
        </div>
      </div>
    )
  }

  if (phase === 'results') {
    return (
      <div className="min-h-screen flex items-center justify-center bg-exam-bg">
        <div className="bg-white rounded-2xl shadow-lg p-8 max-w-lg w-full">
          <h2 className="text-2xl font-bold mb-4 text-center">Writing Submitted</h2>
          {submitted.map((s) => (
            <div key={s.taskNum} className="mb-4 border border-gray-200 rounded-lg p-4">
              <p className="text-sm font-bold text-gray-500 mb-1">Task {s.taskNum}</p>
              <p className="text-sm text-gray-700 whitespace-pre-wrap line-clamp-4">{s.text}</p>
              <p className="text-xs text-gray-400 mt-2">{s.wordCount} words</p>
            </div>
          ))}
          <p className="text-sm text-gray-500 text-center mb-4">
            AI scoring and feedback will appear in your Progress page once processed.
          </p>
          <button onClick={() => navigate('/')} className="btn-primary w-full">Back to Dashboard</button>
        </div>
      </div>
    )
  }

  if (!currentPrompt) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        {loadError
          ? <p className="text-red-600">{loadError}</p>
          : <div className="w-10 h-10 border-4 border-primary-500 border-t-transparent rounded-full animate-spin" />
        }
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-exam-bg pb-10">
      <ExamTimer
        totalSeconds={TASK_TIMES[taskNum] || 27 * 60}
        onExpire={submitTask}
        warningSeconds={120}
      />

      <div className="bg-primary-900 text-white px-6 py-3 flex items-center gap-4">
        <span className="font-bold">Writing — Task {taskNum}</span>
        <span className="ml-2 text-blue-200 text-sm">
          {taskNum === 1 ? 'Writing an Email' : 'Survey Response'}
        </span>
      </div>

      <div className="max-w-5xl mx-auto px-4 pt-6 grid grid-cols-1 lg:grid-cols-2 gap-4">
        {/* Prompt panel */}
        <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-5">
          <p className="text-xs text-gray-400 uppercase tracking-wide mb-3 font-semibold">Task Instructions</p>
          <p className="text-gray-800 text-sm leading-relaxed whitespace-pre-wrap">
            {currentPrompt.prompt}
          </p>
          <div className="mt-4 bg-blue-50 border border-blue-100 rounded p-3">
            <p className="text-xs font-bold text-blue-700 mb-1 uppercase">Scoring Dimensions</p>
            <ul className="text-xs text-blue-800 space-y-1">
              <li>• Content &amp; Coherence</li>
              <li>• Vocabulary</li>
              <li>• Readability</li>
              <li>• Task Fulfillment</li>
            </ul>
          </div>
        </div>

        {/* Writing panel */}
        <div className="flex flex-col">
          <div className="bg-white rounded-xl border border-gray-200 shadow-sm p-5 flex-1 flex flex-col">
            <div className="flex justify-between items-center mb-2">
              <p className="text-xs text-gray-400 uppercase tracking-wide font-semibold">Your Response</p>
              <span className={`word-counter ${counterClass}`}>
                {wordCount} / {MIN_WORDS}–{MAX_WORDS} words
              </span>
            </div>
            <textarea
              className="flex-1 w-full border border-gray-300 rounded p-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-primary-400"
              style={{ minHeight: '320px' }}
              placeholder="Begin writing your response here…"
              value={text}
              onChange={(e) => setText(e.target.value)}
              spellCheck
            />
          </div>
          <button
            onClick={submitTask}
            disabled={wordCount < 1}
            className="btn-primary mt-3 w-full"
          >
            {taskIndex < TASK_NUMS.length - 1 ? 'Submit & Go to Next Task →' : 'Submit Final Task'}
          </button>
          {(isUnder || isOver) && (
            <p className={`text-xs text-center mt-1 ${isOver ? 'text-red-600' : 'text-amber-600'}`}>
              {isOver
                ? `You are ${wordCount - MAX_WORDS} word(s) over the limit.`
                : `You need at least ${MIN_WORDS - wordCount} more word(s).`
              }
            </p>
          )}
        </div>
      </div>
    </div>
  )
}

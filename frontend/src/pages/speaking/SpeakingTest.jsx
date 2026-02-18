import React, { useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  startSpeakingSession,
  getSpeakingTasks,
  submitSpeakingAudio,
} from '../../api/questions'

const TASK_NUMS = [1, 2, 3, 4, 5, 6, 7, 8]

function Countdown({ seconds, label, onDone }) {
  const [remaining, setRemaining] = useState(seconds)
  useEffect(() => {
    if (remaining <= 0) { onDone?.(); return }
    const t = setTimeout(() => setRemaining((r) => r - 1), 1000)
    return () => clearTimeout(t)
  }, [remaining])

  return (
    <div className="flex flex-col items-center gap-2">
      <div className="text-5xl font-black text-primary-700 font-mono">{remaining}</div>
      <div className="text-sm text-gray-500">{label}</div>
      <div className="w-48 bg-gray-200 rounded-full h-2">
        <div
          className="bg-primary-500 h-2 rounded-full transition-all duration-1000"
          style={{ width: `${(remaining / seconds) * 100}%` }}
        />
      </div>
    </div>
  )
}

function WaveformVisualizer({ stream }) {
  const canvasRef = useRef(null)
  const animRef = useRef(null)

  useEffect(() => {
    if (!stream) return
    const ctx = new (window.AudioContext || window.webkitAudioContext)()
    const source = ctx.createMediaStreamSource(stream)
    const analyser = ctx.createAnalyser()
    analyser.fftSize = 256
    source.connect(analyser)
    const buf = new Uint8Array(analyser.frequencyBinCount)

    const draw = () => {
      animRef.current = requestAnimationFrame(draw)
      analyser.getByteFrequencyData(buf)
      const canvas = canvasRef.current
      if (!canvas) return
      const c = canvas.getContext('2d')
      c.clearRect(0, 0, canvas.width, canvas.height)
      const barW = canvas.width / buf.length
      buf.forEach((val, i) => {
        const h = (val / 255) * canvas.height
        c.fillStyle = `hsl(${210 + i}, 70%, 55%)`
        c.fillRect(i * barW, canvas.height - h, barW - 1, h)
      })
    }
    draw()
    return () => { cancelAnimationFrame(animRef.current); ctx.close() }
  }, [stream])

  return <canvas ref={canvasRef} width={320} height={64} className="rounded bg-gray-900 w-full" />
}

export default function SpeakingTest() {
  const navigate = useNavigate()
  const [phase, setPhase] = useState('intro')   // intro | prep | record | review | results
  const sessionIdRef = useRef(null)
  const [tasks, setTasks] = useState({})         // { 1: {...}, 2: {...}, ... }
  const [taskIndex, setTaskIndex] = useState(0)
  const [stream, setStream] = useState(null)
  const [recorder, setRecorder] = useState(null)
  const [audioURL, setAudioURL] = useState(null)
  const [audioBlob, setAudioBlob] = useState(null)
  const [loadError, setLoadError] = useState('')
  const chunksRef = useRef([])

  const taskNum = TASK_NUMS[taskIndex]
  const currentTask = tasks[taskNum]

  useEffect(() => {
    if (phase !== 'prep') return
    getSpeakingTasks()
      .then((res) => setTasks(res.data.data || {}))
      .catch(() => setLoadError('Could not load speaking tasks. Is the backend running?'))
  }, [phase])

  const start = async () => {
    try {
      const res = await startSpeakingSession()
      sessionIdRef.current = res.data.id
    } catch {}
    setPhase('prep')
  }

  const startRecording = async () => {
    try {
      const s = await navigator.mediaDevices.getUserMedia({ audio: true })
      setStream(s)
      const r = new MediaRecorder(s)
      chunksRef.current = []
      r.ondataavailable = (e) => chunksRef.current.push(e.data)
      r.onstop = () => {
        const blob = new Blob(chunksRef.current, { type: 'audio/webm' })
        setAudioBlob(blob)
        setAudioURL(URL.createObjectURL(blob))
        s.getTracks().forEach((t) => t.stop())
        setStream(null)
        setPhase('review')
      }
      r.start()
      setRecorder(r)
      setPhase('record')
    } catch {
      alert('Microphone access is required for the Speaking test. Please allow microphone access in your browser settings.')
    }
  }

  const stopRecording = () => recorder?.stop()

  const submitRecording = async () => {
    if (audioBlob && sessionIdRef.current) {
      try {
        await submitSpeakingAudio(sessionIdRef.current, taskNum, audioBlob)
      } catch {}
    }
    setAudioURL(null)
    setAudioBlob(null)

    if (taskIndex < TASK_NUMS.length - 1) {
      setTaskIndex((i) => i + 1)
      setPhase('prep')
    } else {
      setPhase('results')
    }
  }

  if (phase === 'intro') {
    return (
      <div className="min-h-screen flex items-center justify-center bg-exam-bg">
        <div className="bg-white rounded-2xl shadow-lg p-8 max-w-lg w-full">
          <h1 className="text-2xl font-bold text-primary-900 mb-3">Speaking Test</h1>
          <ul className="text-sm text-gray-600 space-y-2 mb-6">
            <li>• 8 tasks covering different speaking types</li>
            <li>• 30 seconds preparation time per task</li>
            <li>• 60–90 seconds response time per task</li>
            <li>• Microphone access required</li>
            <li>• AI feedback provided after submission</li>
          </ul>
          <button onClick={start} className="btn-primary w-full">Begin Speaking Test</button>
          <button onClick={() => navigate('/')} className="btn-secondary w-full mt-2">Back to Dashboard</button>
        </div>
      </div>
    )
  }

  if (phase === 'results') {
    return (
      <div className="min-h-screen flex items-center justify-center bg-exam-bg">
        <div className="bg-white rounded-2xl shadow-lg p-8 max-w-md w-full text-center">
          <h2 className="text-2xl font-bold mb-4">Speaking Complete</h2>
          <p className="text-gray-500 text-sm mb-6">
            All {TASK_NUMS.length} tasks recorded. AI feedback will appear in your Progress page.
          </p>
          <button onClick={() => navigate('/')} className="btn-primary w-full">Back to Dashboard</button>
        </div>
      </div>
    )
  }

  if (!currentTask && phase === 'prep') {
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
      <div className="bg-primary-900 text-white px-6 py-3 flex items-center gap-4">
        <span className="font-bold">Speaking — Task {taskNum} of {TASK_NUMS.length}</span>
        <span className="ml-2 text-blue-200 text-sm">{currentTask?.title || ''}</span>
      </div>

      <div className="max-w-2xl mx-auto px-4 pt-8">
        {/* Task prompt */}
        {currentTask && (
          <div className="bg-white rounded-xl border border-gray-200 shadow p-6 mb-6">
            {currentTask.image_url && (
              <img src={currentTask.image_url} alt="Scene" className="w-full rounded-lg mb-4 object-cover max-h-48" />
            )}
            <p className="text-xs text-gray-400 uppercase tracking-wide mb-2 font-semibold">
              Task {taskNum}: {currentTask.title}
            </p>
            <p className="text-gray-800 text-base leading-relaxed">{currentTask.prompt}</p>
            <div className="mt-3 flex gap-4 text-xs text-gray-400">
              <span>Prep: {currentTask.prep_time ?? 30}s</span>
              <span>Response: {currentTask.response_time ?? 60}s</span>
            </div>
          </div>
        )}

        {/* Prep phase */}
        {phase === 'prep' && currentTask && (
          <div className="bg-white rounded-xl border border-gray-200 shadow p-6 text-center">
            <p className="text-gray-600 mb-4 font-medium">Preparation Time</p>
            <Countdown seconds={currentTask.prep_time ?? 30} label="seconds to prepare" onDone={startRecording} />
            <button onClick={startRecording} className="btn-primary mt-6">
              Skip Prep &amp; Record Now
            </button>
          </div>
        )}

        {/* Record phase */}
        {phase === 'record' && (
          <div className="bg-white rounded-xl border border-gray-200 shadow p-6 text-center">
            <div className="flex items-center justify-center gap-2 mb-4">
              <span className="w-3 h-3 bg-red-500 rounded-full animate-pulse" />
              <span className="font-bold text-red-600">Recording…</span>
            </div>
            <WaveformVisualizer stream={stream} />
            <div className="mt-4">
              <Countdown
                seconds={currentTask?.response_time ?? 60}
                label="seconds remaining"
                onDone={stopRecording}
              />
            </div>
            <button onClick={stopRecording} className="btn-danger mt-6">Stop Recording</button>
          </div>
        )}

        {/* Review phase */}
        {phase === 'review' && (
          <div className="bg-white rounded-xl border border-gray-200 shadow p-6">
            <p className="font-semibold mb-3">Review Your Recording</p>
            {audioURL && <audio controls src={audioURL} className="w-full mb-4" />}
            <div className="flex gap-3">
              <button onClick={startRecording} className="btn-secondary flex-1">Re-record</button>
              <button onClick={submitRecording} className="btn-primary flex-1">
                {taskIndex < TASK_NUMS.length - 1 ? 'Submit & Next Task →' : 'Submit Final Task'}
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

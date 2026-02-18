import client from './client'

// ── Listening ─────────────────────────────────────────────────────────────
export const startListeningSession = () =>
  client.post('/listening/sessions', { section: 'listening', mode: 'practice' })

export const getListeningQuestions = (part) =>
  client.get('/listening/questions', { params: { part } })

export const submitListeningAnswer = (sessionId, questionId, answer, timeTaken) =>
  client.post(`/listening/sessions/${sessionId}/answers`, {
    session_id: sessionId,
    question_id: questionId,
    answer,
    time_taken_sec: timeTaken ?? 0,
  })

export const completeListeningSession = (sessionId) =>
  client.post(`/listening/sessions/${sessionId}/complete`)

// ── Reading ───────────────────────────────────────────────────────────────
export const startReadingSession = () =>
  client.post('/reading/sessions', { section: 'reading', mode: 'practice' })

export const getReadingQuestions = (part) =>
  client.get('/reading/questions', { params: { part } })

export const submitReadingAnswer = (sessionId, questionId, answer, timeTaken) =>
  client.post(`/reading/sessions/${sessionId}/answers`, {
    session_id: sessionId,
    question_id: questionId,
    answer,
    time_taken_sec: timeTaken ?? 0,
  })

export const completeReadingSession = (sessionId) =>
  client.post(`/reading/sessions/${sessionId}/complete`)

// ── Writing ───────────────────────────────────────────────────────────────
export const startWritingSession = () =>
  client.post('/writing/sessions', { section: 'writing', mode: 'practice' })

export const getWritingPrompt = (taskNum) =>
  client.get(`/writing/prompts/${taskNum}`)

export const submitWritingResponse = (sessionId, taskNum, responseText) =>
  client.post(`/writing/sessions/${sessionId}/responses`, {
    task_num: taskNum,
    response_text: responseText,
  })

// ── Speaking ──────────────────────────────────────────────────────────────
export const startSpeakingSession = () =>
  client.post('/speaking/sessions', { section: 'speaking', mode: 'practice' })

export const getSpeakingTasks = () =>
  client.get('/speaking/tasks')

export const submitSpeakingAudio = (sessionId, taskNum, audioBlob) => {
  const form = new FormData()
  form.append('task_num', taskNum)
  form.append('audio_file', audioBlob, 'recording.webm')
  return client.post(`/speaking/sessions/${sessionId}/responses`, form, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
}

// ── Progress ──────────────────────────────────────────────────────────────
export const getProgressSummary = () =>
  client.get('/progress/summary')

export const getProgressHistory = (days = 30) =>
  client.get('/progress/history', { params: { days } })

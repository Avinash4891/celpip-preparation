import React, { createContext, useContext, useState, useEffect } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { getMe } from './api/auth'

import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import ListeningTest from './pages/listening/ListeningTest'
import ReadingTest from './pages/reading/ReadingTest'
import WritingTest from './pages/writing/WritingTest'
import SpeakingTest from './pages/speaking/SpeakingTest'
import ProgressPage from './pages/progress/ProgressPage'
import LearningPathDashboard from './pages/learning/LearningPathDashboard'
import DiagnosticSetup from './pages/learning/DiagnosticSetup'
import ModuleViewer from './pages/learning/ModuleViewer'
import LessonPlayer from './pages/learning/LessonPlayer'

// ── Auth context ────────────────────────────────────────────────────────────
export const AuthContext = createContext(null)
export const useAuth = () => useContext(AuthContext)

function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const token = localStorage.getItem('access_token')
    if (!token) { setLoading(false); return }
    getMe()
      .then((res) => setUser(res.data))
      .catch(() => localStorage.removeItem('access_token'))
      .finally(() => setLoading(false))
  }, [])

  const logout = () => {
    localStorage.removeItem('access_token')
    setUser(null)
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="w-10 h-10 border-4 border-primary-500 border-t-transparent rounded-full animate-spin" />
      </div>
    )
  }

  return (
    <AuthContext.Provider value={{ user, setUser, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

// ── Protected route ──────────────────────────────────────────────────────────
function Protected({ children }) {
  const { user } = useAuth()
  return user ? children : <Navigate to="/login" replace />
}

// ── App ──────────────────────────────────────────────────────────────────────
export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/" element={<Protected><Dashboard /></Protected>} />
          <Route path="/listening" element={<Protected><ListeningTest /></Protected>} />
          <Route path="/reading" element={<Protected><ReadingTest /></Protected>} />
          <Route path="/writing" element={<Protected><WritingTest /></Protected>} />
          <Route path="/speaking" element={<Protected><SpeakingTest /></Protected>} />
          <Route path="/progress" element={<Protected><ProgressPage /></Protected>} />
          <Route path="/learning" element={<Protected><LearningPathDashboard /></Protected>} />
          <Route path="/learning/diagnostic" element={<Protected><DiagnosticSetup /></Protected>} />
          <Route path="/learning/module/:moduleId" element={<Protected><ModuleViewer /></Protected>} />
          <Route path="/learning/lesson/:lessonId" element={<Protected><LessonPlayer /></Protected>} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  )
}

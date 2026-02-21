import client from './client'

// ============================================================================
// Learning Path Management
// ============================================================================

export const createLearningPath = (sessionId, targetLevel = 10) =>
  client.post('/learning-path/diagnostic', {
    session_id: sessionId,
    target_level: targetLevel,
  })

export const getLearningPath = () => client.get('/learning-path/current')

export const refreshLearningPath = () => client.patch('/learning-path/refresh')

// ============================================================================
// Module Management
// ============================================================================

export const getModules = (filters = {}) =>
  client.get('/modules', { params: filters })

export const getModule = (moduleId) => client.get(`/modules/${moduleId}`)

export const enrollModule = (moduleId) =>
  client.post(`/modules/${moduleId}/enroll`)

export const completeModule = (moduleId, assessmentScore = null) =>
  client.post(`/modules/${moduleId}/complete`, {
    assessment_score: assessmentScore,
  })

// ============================================================================
// Lesson Management
// ============================================================================

export const getLesson = (lessonId) => client.get(`/lessons/${lessonId}`)

export const completeLesson = (lessonId, data) =>
  client.post(`/lessons/${lessonId}/complete`, data)

// ============================================================================
// AI Recommendations
// ============================================================================

export const analyzePerformance = (sessionId) =>
  client.post('/ai/analyze-performance', { session_id: sessionId })

export const getRecommendations = () => client.get('/ai/recommendations')

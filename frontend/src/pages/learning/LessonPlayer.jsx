import React, { useEffect, useState, useRef } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { getLesson, completeLesson } from '../../api/learning'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import Header from '../../components/Header'

// Custom renderers for rich, educational markdown display
const markdownComponents = {
  // Headings with visual hierarchy
  h1: ({ children }) => (
    <h1 className="text-2xl font-bold text-gray-900 mt-8 mb-4 pb-3 border-b-2 border-primary-200 flex items-center gap-2">
      {children}
    </h1>
  ),
  h2: ({ children }) => (
    <h2 className="text-xl font-bold text-gray-800 mt-8 mb-3 pb-2 border-b border-gray-200">
      {children}
    </h2>
  ),
  h3: ({ children }) => (
    <h3 className="text-base font-bold text-gray-800 mt-6 mb-2 flex items-center gap-2">
      <span className="w-1 h-5 bg-primary-500 rounded-full inline-block flex-shrink-0" />
      {children}
    </h3>
  ),
  h4: ({ children }) => (
    <h4 className="text-sm font-bold text-gray-700 mt-4 mb-2 uppercase tracking-wide">
      {children}
    </h4>
  ),

  // Paragraphs
  p: ({ children }) => (
    <p className="text-gray-700 leading-relaxed mb-4 text-[15px]">{children}</p>
  ),

  // Strong/bold
  strong: ({ children }) => (
    <strong className="font-bold text-gray-900">{children}</strong>
  ),

  // Lists with better styling
  ul: ({ children }) => (
    <ul className="space-y-2 mb-4 ml-2">{children}</ul>
  ),
  ol: ({ children }) => (
    <ol className="space-y-2 mb-4 ml-2">{children}</ol>
  ),
  li: ({ children, ordered, index }) => (
    <li className="flex items-start gap-2.5 text-gray-700 text-[15px]">
      {ordered ? (
        <span className="mt-0.5 w-5 h-5 bg-primary-100 text-primary-700 rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0">
          {(index ?? 0) + 1}
        </span>
      ) : (
        <span className="mt-2 w-2 h-2 rounded-full bg-primary-400 flex-shrink-0" />
      )}
      <span className="flex-1">{children}</span>
    </li>
  ),

  // Code blocks
  code: ({ inline, children }) => {
    if (inline) {
      return (
        <code className="bg-primary-50 text-primary-800 text-sm font-mono px-1.5 py-0.5 rounded border border-primary-200">
          {children}
        </code>
      )
    }
    return (
      <div className="my-4">
        <div className="bg-gray-800 rounded-t-lg px-4 py-2 flex items-center gap-2">
          <div className="w-3 h-3 rounded-full bg-red-400" />
          <div className="w-3 h-3 rounded-full bg-yellow-400" />
          <div className="w-3 h-3 rounded-full bg-green-400" />
          <span className="text-gray-400 text-xs ml-2">Example</span>
        </div>
        <pre className="bg-gray-900 text-green-300 text-sm font-mono p-5 rounded-b-lg overflow-x-auto leading-relaxed whitespace-pre-wrap">
          {children}
        </pre>
      </div>
    )
  },

  // Tables — beautifully styled for learning
  table: ({ children }) => (
    <div className="my-6 overflow-x-auto rounded-xl border border-gray-200 shadow-sm">
      <table className="w-full text-sm">{children}</table>
    </div>
  ),
  thead: ({ children }) => (
    <thead className="bg-gradient-to-r from-primary-600 to-indigo-600 text-white">
      {children}
    </thead>
  ),
  tbody: ({ children }) => (
    <tbody className="divide-y divide-gray-100">{children}</tbody>
  ),
  tr: ({ children }) => (
    <tr className="hover:bg-primary-50 transition-colors even:bg-gray-50">{children}</tr>
  ),
  th: ({ children }) => (
    <th className="px-4 py-3 text-left font-semibold text-sm">{children}</th>
  ),
  td: ({ children }) => (
    <td className="px-4 py-3 text-gray-700">{children}</td>
  ),

  // Blockquote — for tips/callouts
  blockquote: ({ children }) => (
    <blockquote className="my-4 pl-4 border-l-4 border-primary-400 bg-primary-50 py-3 pr-4 rounded-r-lg">
      <div className="text-primary-800 italic">{children}</div>
    </blockquote>
  ),

  // Horizontal rule — section divider
  hr: () => (
    <div className="my-8 flex items-center gap-3">
      <div className="flex-1 h-px bg-gradient-to-r from-transparent to-gray-300" />
      <div className="w-2 h-2 rounded-full bg-gray-400" />
      <div className="flex-1 h-px bg-gradient-to-l from-transparent to-gray-300" />
    </div>
  ),

  // Links
  a: ({ href, children }) => (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className="text-primary-600 hover:text-primary-800 underline underline-offset-2"
    >
      {children}
    </a>
  ),
}

export default function LessonPlayer() {
  const { lessonId } = useParams()
  const navigate = useNavigate()
  const [lesson, setLesson] = useState(null)
  const [completion, setCompletion] = useState(null)
  const [loading, setLoading] = useState(true)
  const [notes, setNotes] = useState('')
  const [timeSpent, setTimeSpent] = useState(0)
  const [completing, setCompleting] = useState(false)
  const [readingProgress, setReadingProgress] = useState(0)
  const startTimeRef = useRef(Date.now())
  const contentRef = useRef(null)

  useEffect(() => {
    loadLesson()

    const interval = setInterval(() => {
      const elapsed = Math.floor((Date.now() - startTimeRef.current) / 1000 / 60)
      setTimeSpent(elapsed)
    }, 30000)

    return () => clearInterval(interval)
  }, [lessonId])

  // Reading progress scroll tracker
  useEffect(() => {
    const handleScroll = () => {
      if (!contentRef.current) return
      const el = contentRef.current
      const scrollTop = window.scrollY - el.offsetTop + 200
      const scrollHeight = el.scrollHeight
      const pct = Math.min(100, Math.max(0, Math.round((scrollTop / scrollHeight) * 100)))
      setReadingProgress(pct)
    }
    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  }, [lesson])

  const loadLesson = async () => {
    try {
      setLoading(true)
      const res = await getLesson(lessonId)
      setLesson(res.data.data.lesson)
      setCompletion(res.data.data.completion)
      setNotes(res.data.data.completion?.notes || '')
    } catch (err) {
      console.error('Error loading lesson:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleComplete = async () => {
    try {
      setCompleting(true)
      const finalTime = Math.max(1, Math.floor((Date.now() - startTimeRef.current) / 1000 / 60))
      await completeLesson(lessonId, {
        time_spent_mins: finalTime,
        quiz_score: null,
        notes: notes,
      })
      alert('Lesson completed! Great work!')
      navigate(`/learning/module/${lesson.module_id}`)
    } catch (err) {
      console.error('Error completing lesson:', err)
      alert(err.response?.data?.detail || 'Failed to complete lesson')
    } finally {
      setCompleting(false)
    }
  }

  const handleBack = () => {
    if (lesson) {
      navigate(`/learning/module/${lesson.module_id}`)
    } else {
      navigate('/learning')
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen">
        <Header />
        <div className="flex items-center justify-center h-[calc(100vh-64px)]">
          <div className="text-center">
            <div className="w-16 h-16 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin mx-auto mb-4" />
            <p className="text-gray-600 font-medium">Loading lesson...</p>
          </div>
        </div>
      </div>
    )
  }

  if (!lesson) {
    return (
      <div className="min-h-screen">
        <Header />
        <div className="flex items-center justify-center h-[calc(100vh-64px)] px-4">
          <div className="glass-card p-10 max-w-md text-center animate-scale-in">
            <div className="text-5xl mb-4">❌</div>
            <h2 className="text-xl font-bold text-gray-800 mb-2">Lesson Not Found</h2>
            <button onClick={() => navigate('/learning')} className="btn-primary mt-4">
              ← Back to Learning Path
            </button>
          </div>
        </div>
      </div>
    )
  }

  const LESSON_TYPE_INFO = {
    text: { icon: '📝', label: 'Text Lesson', color: 'bg-blue-100 text-blue-800' },
    video: { icon: '🎥', label: 'Video Lesson', color: 'bg-purple-100 text-purple-800' },
    model_answer: { icon: '⭐', label: 'Model Answer', color: 'bg-amber-100 text-amber-800' },
    interactive: { icon: '🎯', label: 'Interactive', color: 'bg-green-100 text-green-800' },
  }
  const typeInfo = LESSON_TYPE_INFO[lesson.lesson_type] || LESSON_TYPE_INFO.text

  return (
    <div className="min-h-screen animate-fade-in">
      <Header />

      {/* Reading Progress Bar — fixed just below header */}
      <div className="fixed top-[64px] left-0 right-0 h-1 bg-gray-200 z-40">
        <div
          className="h-full bg-gradient-to-r from-primary-500 to-indigo-500 transition-all duration-300"
          style={{ width: `${readingProgress}%` }}
        />
      </div>

      {/* Sticky Lesson Toolbar */}
      <div className="sticky top-[65px] z-30 bg-white/90 backdrop-blur-md border-b border-gray-200 shadow-sm">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 py-3">
          <div className="flex items-center justify-between gap-4">
            <div className="flex items-center gap-3 min-w-0">
              <button
                onClick={handleBack}
                className="flex items-center gap-1.5 text-gray-500 hover:text-gray-800 text-sm transition-colors group flex-shrink-0"
              >
                <svg className="w-4 h-4 group-hover:-translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                </svg>
                <span className="hidden sm:inline">Back to Module</span>
              </button>
              <div className="w-px h-5 bg-gray-300 flex-shrink-0" />
              <div className="min-w-0">
                <p className="font-semibold text-gray-900 text-sm truncate">{lesson.title}</p>
                <div className="flex items-center gap-2 text-xs text-gray-500 mt-0.5">
                  <span className={`px-2 py-0.5 rounded-full font-medium ${typeInfo.color}`}>
                    {typeInfo.icon} {typeInfo.label}
                  </span>
                  {lesson.estimated_duration_mins && (
                    <span>⏱️ {lesson.estimated_duration_mins} min</span>
                  )}
                  <span className="hidden sm:inline">🕐 {timeSpent} min spent</span>
                </div>
              </div>
            </div>

            <div className="flex items-center gap-3 flex-shrink-0">
              <span className="text-xs text-gray-500 hidden sm:block">{readingProgress}% read</span>
              {!completion?.completed ? (
                <button
                  onClick={handleComplete}
                  disabled={completing}
                  className="btn-success text-sm py-2 px-4"
                >
                  {completing ? 'Saving...' : '✓ Mark Complete'}
                </button>
              ) : (
                <div className="flex items-center gap-2 bg-green-50 border border-green-300 text-green-700 px-4 py-2 rounded-lg text-sm font-semibold">
                  <span>✓</span>
                  <span>Completed</span>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-4xl mx-auto px-4 sm:px-6 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">

          {/* Lesson Content — 3 of 4 columns */}
          <div className="lg:col-span-3" ref={contentRef}>

            {/* Text Lesson */}
            {lesson.lesson_type === 'text' && lesson.content && (
              <div className="glass-card p-8 animate-slide-up">
                <ReactMarkdown components={markdownComponents} remarkPlugins={[remarkGfm]}>
                  {lesson.content}
                </ReactMarkdown>
              </div>
            )}

            {/* Video Lesson */}
            {lesson.lesson_type === 'video' && lesson.video_url && (
              <div className="space-y-6 animate-slide-up">
                <div className="glass-card overflow-hidden">
                  <div className="aspect-video bg-gray-900 rounded-t-2xl">
                    <iframe
                      src={lesson.video_url}
                      title={lesson.title}
                      className="w-full h-full"
                      allowFullScreen
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    />
                  </div>
                  {lesson.content && (
                    <div className="p-8">
                      <ReactMarkdown components={markdownComponents} remarkPlugins={[remarkGfm]}>
                        {lesson.content}
                      </ReactMarkdown>
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* Model Answer */}
            {lesson.lesson_type === 'model_answer' && (
              <div className="space-y-6 animate-slide-up">
                {lesson.content && (
                  <div className="glass-card p-8">
                    <ReactMarkdown components={markdownComponents} remarkPlugins={[remarkGfm]}>
                      {lesson.content}
                    </ReactMarkdown>
                  </div>
                )}

                <div className="glass-card p-6">
                  <div className="flex items-center gap-3 mb-5">
                    <div className="w-10 h-10 bg-amber-100 rounded-xl flex items-center justify-center text-xl">
                      ⭐
                    </div>
                    <div>
                      <h3 className="font-bold text-gray-800">Model Answer</h3>
                      <p className="text-xs text-gray-500">Study this response carefully</p>
                    </div>
                  </div>
                  <div className="bg-amber-50 border border-amber-200 rounded-xl p-6 font-serif text-gray-800 leading-relaxed whitespace-pre-wrap text-[15px]">
                    {lesson.model_answer_text}
                  </div>

                  {lesson.annotations && lesson.annotations.length > 0 && (
                    <div className="mt-6">
                      <h4 className="font-bold text-gray-800 mb-4 flex items-center gap-2">
                        <span>📝</span>
                        <span>Expert Annotations</span>
                      </h4>
                      <div className="space-y-3">
                        {lesson.annotations.map((annotation, idx) => (
                          <div
                            key={idx}
                            className="border border-yellow-200 rounded-xl p-4 bg-yellow-50 animate-slide-up"
                            style={{ animationDelay: `${idx * 0.05}s` }}
                          >
                            <div className="flex items-start gap-3">
                              <div className="w-7 h-7 bg-yellow-400 rounded-full flex items-center justify-center text-xs font-bold text-white flex-shrink-0">
                                {idx + 1}
                              </div>
                              <div>
                                <p className="font-semibold text-gray-800 mb-1 italic text-sm">
                                  "{annotation.highlighted_text}"
                                </p>
                                <p className="text-sm text-gray-700 mb-2">
                                  {annotation.explanation}
                                </p>
                                <div className="flex items-center gap-2">
                                  <span className="px-2 py-0.5 bg-blue-100 text-blue-700 rounded-full text-xs font-medium">
                                    {annotation.category}
                                  </span>
                                  <span className="text-xs text-gray-500">
                                    {annotation.band_relevance}
                                  </span>
                                </div>
                              </div>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* Interactive Lesson */}
            {lesson.lesson_type === 'interactive' && (
              <div className="glass-card p-8 animate-slide-up">
                <div className="flex items-center gap-3 mb-6 p-4 bg-green-50 border border-green-200 rounded-xl">
                  <span className="text-2xl">🎯</span>
                  <div>
                    <p className="font-semibold text-green-800">Interactive Quiz Coming Soon</p>
                    <p className="text-sm text-green-600">Review the content below to prepare.</p>
                  </div>
                </div>
                {lesson.content && (
                  <ReactMarkdown components={markdownComponents} remarkPlugins={[remarkGfm]}>
                    {lesson.content}
                  </ReactMarkdown>
                )}
              </div>
            )}

            {/* Notes Section */}
            <div className="glass-card p-6 mt-6 animate-slide-up" style={{ animationDelay: '0.15s' }}>
              <h3 className="font-bold text-gray-800 mb-3 flex items-center gap-2">
                <span className="text-xl">📝</span>
                <span>Your Notes</span>
                <span className="ml-auto text-xs text-gray-400 font-normal">
                  Saved when you complete the lesson
                </span>
              </h3>
              <textarea
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                placeholder="Write your key takeaways, questions, or anything you want to remember..."
                className="w-full h-36 px-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-primary-300 focus:border-primary-400 resize-none text-sm text-gray-700 leading-relaxed bg-gray-50"
              />
            </div>

            {/* Complete Button */}
            {!completion?.completed && (
              <div className="mt-6 text-center animate-slide-up" style={{ animationDelay: '0.2s' }}>
                <button
                  onClick={handleComplete}
                  disabled={completing}
                  className="btn-success px-10 py-4 text-base"
                >
                  {completing ? (
                    <span className="flex items-center gap-2">
                      <span className="w-4 h-4 border-2 border-white/40 border-t-white rounded-full animate-spin" />
                      Saving progress...
                    </span>
                  ) : (
                    '🎉 Complete Lesson & Continue'
                  )}
                </button>
                <p className="text-xs text-gray-400 mt-2">Your notes and time spent will be saved</p>
              </div>
            )}

            {completion?.completed && (
              <div className="mt-6 glass-card p-6 text-center bg-gradient-to-br from-green-50 to-emerald-50 border border-green-200 animate-scale-in">
                <div className="text-4xl mb-3">🏆</div>
                <h3 className="font-bold text-green-800 mb-1">Lesson Complete!</h3>
                <p className="text-sm text-green-600 mb-4">
                  You finished this lesson.
                  {completion.time_spent_mins > 0 && ` Time spent: ${completion.time_spent_mins} min.`}
                </p>
                <button onClick={handleBack} className="btn-primary">
                  ← Back to Module
                </button>
              </div>
            )}
          </div>

          {/* Right Sidebar — sticky on desktop */}
          <div className="lg:col-span-1">
            <div className="lg:sticky lg:top-[130px] space-y-4">

              {/* Reading Progress */}
              <div className="glass-card p-4 animate-slide-up">
                <h4 className="font-semibold text-gray-700 text-sm mb-3 flex items-center gap-2">
                  <span>📖</span> Reading Progress
                </h4>
                <div className="relative w-full bg-gray-100 rounded-full h-2 mb-2">
                  <div
                    className="absolute inset-y-0 left-0 bg-gradient-to-r from-primary-500 to-indigo-500 rounded-full transition-all duration-300"
                    style={{ width: `${readingProgress}%` }}
                  />
                </div>
                <p className="text-xs text-gray-500 text-right">{readingProgress}% read</p>
              </div>

              {/* Lesson Meta */}
              <div className="glass-card p-4 animate-slide-up" style={{ animationDelay: '0.05s' }}>
                <h4 className="font-semibold text-gray-700 text-sm mb-3 flex items-center gap-2">
                  <span>ℹ️</span> Lesson Details
                </h4>
                <div className="space-y-2 text-xs">
                  <div className="flex justify-between">
                    <span className="text-gray-500">Type</span>
                    <span className={`font-medium px-2 py-0.5 rounded-full ${typeInfo.color}`}>
                      {typeInfo.label}
                    </span>
                  </div>
                  {lesson.estimated_duration_mins && (
                    <div className="flex justify-between">
                      <span className="text-gray-500">Estimated</span>
                      <span className="font-medium text-gray-700">{lesson.estimated_duration_mins} min</span>
                    </div>
                  )}
                  <div className="flex justify-between">
                    <span className="text-gray-500">Time spent</span>
                    <span className="font-medium text-gray-700">{timeSpent} min</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-500">Status</span>
                    <span className={`font-medium ${completion?.completed ? 'text-green-600' : 'text-amber-600'}`}>
                      {completion?.completed ? '✓ Done' : 'In Progress'}
                    </span>
                  </div>
                </div>
              </div>

              {/* Quick Actions */}
              <div className="glass-card p-4 animate-slide-up" style={{ animationDelay: '0.1s' }}>
                <h4 className="font-semibold text-gray-700 text-sm mb-3 flex items-center gap-2">
                  <span>⚡</span> Quick Actions
                </h4>
                <div className="space-y-2">
                  <button
                    onClick={handleBack}
                    className="w-full text-left text-xs text-gray-600 hover:text-primary-600 flex items-center gap-2 p-2 rounded-lg hover:bg-primary-50 transition-colors"
                  >
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                    </svg>
                    Back to Module
                  </button>
                  <button
                    onClick={() => navigate('/learning')}
                    className="w-full text-left text-xs text-gray-600 hover:text-primary-600 flex items-center gap-2 p-2 rounded-lg hover:bg-primary-50 transition-colors"
                  >
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                    </svg>
                    Learning Path
                  </button>
                  {!completion?.completed && (
                    <button
                      onClick={handleComplete}
                      disabled={completing}
                      className="w-full text-left text-xs text-green-700 hover:text-green-800 flex items-center gap-2 p-2 rounded-lg hover:bg-green-50 transition-colors font-medium disabled:opacity-50"
                    >
                      <span>✓</span>
                      Mark as Complete
                    </button>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

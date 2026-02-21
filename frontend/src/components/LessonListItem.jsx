import React from 'react'

const LESSON_TYPE_ICONS = {
  text: '📝',
  video: '🎥',
  model_answer: '⭐',
  interactive: '🎯',
}

const LESSON_TYPE_LABELS = {
  text: 'Text Lesson',
  video: 'Video',
  model_answer: 'Model Answer',
  interactive: 'Interactive',
}

export default function LessonListItem({ lesson, onClick, completed = false }) {
  return (
    <div
      onClick={() => onClick(lesson.id)}
      className={`
        flex items-center justify-between p-4 border rounded-lg transition-all
        cursor-pointer hover:shadow-md hover:border-blue-400
        ${completed ? 'bg-green-50 border-green-300' : 'bg-white border-gray-200'}
      `}
    >
      {/* Left section */}
      <div className="flex items-center gap-3 flex-1">
        {/* Type icon */}
        <div className="text-2xl">
          {LESSON_TYPE_ICONS[lesson.lesson_type] || '📄'}
        </div>

        {/* Lesson info */}
        <div className="flex-1">
          <div className="flex items-center gap-2">
            <h4 className="font-semibold text-gray-800 text-sm">
              {lesson.title}
            </h4>
            {completed && (
              <span className="text-green-600 text-sm">✓</span>
            )}
          </div>
          <div className="flex items-center gap-3 mt-1">
            <span className="text-xs text-gray-500">
              {LESSON_TYPE_LABELS[lesson.lesson_type]}
            </span>
            {lesson.estimated_duration_mins && (
              <span className="text-xs text-gray-500">
                ⏱️ {lesson.estimated_duration_mins} min
              </span>
            )}
          </div>
        </div>
      </div>

      {/* Right section - Progress info */}
      <div className="flex flex-col items-end gap-1">
        {completed && lesson.time_spent_mins > 0 && (
          <span className="text-xs text-gray-500">
            Spent: {lesson.time_spent_mins} min
          </span>
        )}
        {completed && lesson.quiz_score !== null && lesson.quiz_score !== undefined && (
          <span className="text-xs font-medium text-green-600">
            Quiz: {Math.round(lesson.quiz_score)}%
          </span>
        )}
        {!completed && (
          <span className="text-xs text-blue-600 font-medium">
            Start →
          </span>
        )}
      </div>
    </div>
  )
}

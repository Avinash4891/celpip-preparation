import React, { useEffect } from 'react'

const TOAST_TYPES = {
  success: {
    icon: '✓',
    bgClass: 'bg-green-500',
    borderClass: 'border-green-600',
  },
  error: {
    icon: '✕',
    bgClass: 'bg-red-500',
    borderClass: 'border-red-600',
  },
  info: {
    icon: 'ℹ',
    bgClass: 'bg-blue-500',
    borderClass: 'border-blue-600',
  },
  warning: {
    icon: '⚠',
    bgClass: 'bg-amber-500',
    borderClass: 'border-amber-600',
  },
}

export default function Toast({ message, type = 'info', onClose, duration = 5000 }) {
  const config = TOAST_TYPES[type] || TOAST_TYPES.info

  useEffect(() => {
    if (duration > 0) {
      const timer = setTimeout(onClose, duration)
      return () => clearTimeout(timer)
    }
  }, [duration, onClose])

  return (
    <div className="fixed bottom-6 right-6 z-50 animate-slide-up">
      <div
        className={`
          ${config.bgClass} ${config.borderClass}
          text-white px-6 py-4 rounded-lg shadow-2xl border-l-4
          flex items-center gap-4 max-w-md backdrop-blur-lg
        `}
      >
        <div className="flex-shrink-0 w-8 h-8 rounded-full bg-white/20 flex items-center justify-center text-xl font-bold">
          {config.icon}
        </div>
        <div className="flex-1">
          <p className="font-medium">{message}</p>
        </div>
        <button
          onClick={onClose}
          className="flex-shrink-0 text-white/80 hover:text-white transition-colors"
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>
  )
}

// Toast container component for managing multiple toasts
export function ToastContainer({ toasts, removeToast }) {
  return (
    <div className="fixed bottom-6 right-6 z-50 space-y-3">
      {toasts.map((toast) => (
        <Toast
          key={toast.id}
          message={toast.message}
          type={toast.type}
          onClose={() => removeToast(toast.id)}
          duration={toast.duration}
        />
      ))}
    </div>
  )
}

// Hook to use toasts
export function useToast() {
  const [toasts, setToasts] = React.useState([])

  const showToast = React.useCallback((message, type = 'info', duration = 5000) => {
    const id = Date.now()
    setToasts((prev) => [...prev, { id, message, type, duration }])
  }, [])

  const removeToast = React.useCallback((id) => {
    setToasts((prev) => prev.filter((toast) => toast.id !== id))
  }, [])

  return { toasts, showToast, removeToast }
}

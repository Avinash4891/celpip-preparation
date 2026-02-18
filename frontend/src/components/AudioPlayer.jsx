import React, { useRef, useState, useEffect } from 'react'

/**
 * AudioPlayer — single-play audio (mirrors the real CELPIP exam).
 * If `script` is provided (for TTS fallback), shows the script after playback ends.
 * If `src` is a URL, plays the audio file.
 * If neither, uses Web Speech API TTS.
 */
export default function AudioPlayer({ src, script, onEnded, autoPlay = false }) {
  const audioRef = useRef(null)
  const [status, setStatus] = useState('idle') // idle | playing | done
  const [hasPlayed, setHasPlayed] = useState(false)
  const [ttsReady, setTtsReady] = useState(false)

  // Determine mode
  const useFile = Boolean(src)
  const useTTS = !useFile && Boolean(script)

  useEffect(() => {
    if (useTTS) setTtsReady(typeof window.speechSynthesis !== 'undefined')
  }, [useTTS])

  const play = () => {
    if (hasPlayed) return
    setHasPlayed(true)
    setStatus('playing')

    if (useFile) {
      audioRef.current?.play()
    } else if (useTTS && ttsReady) {
      const utt = new SpeechSynthesisUtterance(script)
      utt.rate = 0.95
      utt.onend = () => { setStatus('done'); onEnded?.() }
      window.speechSynthesis.speak(utt)
    }
  }

  useEffect(() => {
    if (autoPlay) play()
  }, [autoPlay])

  return (
    <div className="flex flex-col items-start gap-3 my-4">
      {useFile && (
        <audio
          ref={audioRef}
          src={src}
          onEnded={() => { setStatus('done'); onEnded?.() }}
          className="hidden"
        />
      )}

      <div className="flex items-center gap-4">
        <button
          onClick={play}
          disabled={hasPlayed}
          className={`flex items-center gap-2 px-5 py-2 rounded-lg font-semibold transition-colors ${
            hasPlayed
              ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
              : 'bg-primary-600 hover:bg-primary-700 text-white'
          }`}
        >
          {status === 'playing' ? (
            <>
              <span className="relative flex h-3 w-3">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75" />
                <span className="relative inline-flex rounded-full h-3 w-3 bg-white" />
              </span>
              Playing…
            </>
          ) : status === 'done' ? (
            '✓ Audio Played'
          ) : (
            '▶ Play Audio'
          )}
        </button>

        {!hasPlayed && (
          <span className="text-xs text-amber-700 bg-amber-50 border border-amber-200 rounded px-2 py-1">
            Audio plays once only
          </span>
        )}
      </div>

      {status === 'done' && script && (
        <details className="mt-2 text-sm text-gray-600 w-full">
          <summary className="cursor-pointer text-primary-600 font-medium">
            Show audio transcript (practice only)
          </summary>
          <p className="mt-2 bg-gray-50 rounded p-3 whitespace-pre-wrap border border-gray-200">
            {script}
          </p>
        </details>
      )}
    </div>
  )
}

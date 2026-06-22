import React from 'react'
import { useAppContext } from '../context/AppContext'
import { generateConfig } from '../services/api'

export default function PromptInput() {
  const {
    promptText, setPromptText,
    isLoading, setIsLoading,
    setPipelineStage,
    setGeneratedJson,
    setMetrics,
    setErrorMessages
  } = useAppContext()

  const quickFillPrompts = [
    'Build a SaaS CRM',
    'Create an e-commerce platform with Stripe integration',
    'Design a social media app with real-time chat'
  ]

  const handleSubmit = async () => {
    setIsLoading(true)
    setPipelineStage(0)
    setGeneratedJson(null)
    setErrorMessages(null)
    
    try {
      const stages = ['intent', 'design', 'schema', 'refinement']
      const data = await generateConfig(promptText)
      for (let i = 0; i < stages.length; i++) {
        setPipelineStage(i + 1)
        await new Promise(r => setTimeout(r, 300))
      }
      setGeneratedJson(data.config)
      setMetrics({
        latency: data.metrics?.latency ?? 0,
        retries: data.metrics?.retries ?? 0,
        tokenCost: data.metrics?.token_cost ?? 0
      })
    } catch (error) {
      setErrorMessages(error.response?.data?.error || error.message)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="prompt-input space-y-3">
      <textarea
        value={promptText}
        onChange={(e) => setPromptText(e.target.value)}
        placeholder="Enter your app requirements..."
        className="w-full min-h-[200px] p-3 border border-slate-600 rounded-lg bg-slate-800 text-slate-100 font-mono resize-none focus:ring-2 focus:ring-blue-500 focus:outline-none disabled:opacity-50"
        disabled={isLoading}
      />
      <div className="flex flex-wrap gap-2">
        {quickFillPrompts.map((prompt, i) => (
          <button
            key={i}
            onClick={() => setPromptText(prompt)}
            disabled={isLoading}
            className="px-3 py-1 text-sm bg-slate-700 hover:bg-slate-600 text-slate-200 rounded-md transition-colors disabled:opacity-50"
          >
            {prompt}
          </button>
        ))}
      </div>
      <button
        onClick={handleSubmit}
        disabled={isLoading || !promptText.trim()}
        className="w-full py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
      >
        {isLoading ? (
          <>
            <span className="animate-spin">⋯</span>
            Generating...
          </>
        ) : 'Compile'}
      </button>
    </div>
  )
}
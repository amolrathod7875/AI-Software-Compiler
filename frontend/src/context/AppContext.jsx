import React, { createContext, useContext, useState } from 'react'

const AppContext = createContext()

export function AppProvider({ children }) {
  const [promptText, setPromptText] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [pipelineStage, setPipelineStage] = useState(0)
  const [generatedJson, setGeneratedJson] = useState(null)
  const [metrics, setMetrics] = useState({ latency: 0, retries: 0, tokenCost: 0 })
  const [errorMessages, setErrorMessages] = useState(null)

  return (
    <AppContext.Provider value={{
      promptText, setPromptText,
      isLoading, setIsLoading,
      pipelineStage, setPipelineStage,
      generatedJson, setGeneratedJson,
      metrics, setMetrics,
      errorMessages, setErrorMessages
    }}>
      {children}
    </AppContext.Provider>
  )
}

export const useAppContext = () => {
  const context = useContext(AppContext)
  if (!context) throw new Error('useAppContext must be used within AppProvider')
  return context
}
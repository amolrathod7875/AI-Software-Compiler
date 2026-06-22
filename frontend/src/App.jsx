import React from 'react'
import { AppProvider } from './context/AppContext'
import PromptInput from './components/PromptInput'
import PipelineVisualizer from './components/PipelineVisualizer'
import JsonViewer from './components/JsonViewer'
import MetricsPanel from './components/MetricsPanel'
import './styles/main.css'

function App() {
  return (
    <AppProvider>
      <div className="min-h-screen bg-slate-900 text-slate-100 p-6">
        <h1 className="text-2xl font-bold mb-6 text-center text-slate-100">AI Software Compiler</h1>
        <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="space-y-6">
            <PromptInput />
            <MetricsPanel />
          </div>
          <div className="space-y-6">
            <PipelineVisualizer />
            <JsonViewer />
          </div>
        </div>
      </div>
    </AppProvider>
  )
}

export default App
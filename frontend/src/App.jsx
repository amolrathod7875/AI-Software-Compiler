import React from 'react'
import PromptInput from './components/PromptInput'
import PipelineVisualizer from './components/PipelineVisualizer'
import JsonViewer from './components/JsonViewer'
import MetricsPanel from './components/MetricsPanel'
import './styles/main.css'

function App() {
  return (
    <div className="app">
      <h1>AI Software Compiler</h1>
      <PromptInput />
      <PipelineVisualizer />
      <JsonViewer />
      <MetricsPanel />
    </div>
  )
}

export default App
import React from 'react'
import { useAppContext } from '../context/AppContext'

export default function PipelineVisualizer() {
  const { pipelineStage } = useAppContext()
  const stages = ['Intent', 'Design', 'Schema', 'Refinement']

  return (
    <div className="pipeline-visualizer">
      <h3 className="text-lg font-semibold mb-4 text-slate-200">Pipeline Progress</h3>
      <div className="flex items-center justify-between">
        {stages.map((stage, i) => {
          const isActive = pipelineStage === i + 1
          const isCompleted = pipelineStage > i + 1
          return (
            <div key={stage} className="flex items-center">
              <div className={`flex items-center justify-center w-10 h-10 rounded-full font-medium
                ${isCompleted ? 'bg-green-600 text-white' : isActive ? 'bg-blue-600 text-white animate-pulse' : 'bg-slate-700 text-slate-400'}`}>
                {isCompleted ? '✓' : i + 1}
              </div>
              <span className={`ml-2 text-sm ${isActive ? 'text-blue-400' : isCompleted ? 'text-green-400' : 'text-slate-500'}`}>
                {stage}
              </span>
              {i < stages.length - 1 && (
                <div className={`w-12 h-0.5 mx-4 ${isCompleted ? 'bg-green-600' : 'bg-slate-700'}`} />
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}
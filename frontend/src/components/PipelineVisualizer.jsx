import React from 'react'

export default function PipelineVisualizer() {
  const stages = ['Intent', 'Design', 'Schema', 'Refinement']
  return (
    <div className="pipeline-visualizer">
      <h3>Pipeline Progress</h3>
      <div className="stages">
        {stages.map((stage, i) => (
          <div key={stage} className="stage">{i + 1}. {stage}</div>
        ))}
      </div>
    </div>
  )
}
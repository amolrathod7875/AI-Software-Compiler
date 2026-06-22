import React from 'react'
import { useAppContext } from '../context/AppContext'

export default function MetricsPanel() {
  const { metrics } = useAppContext()

  return (
    <div className="metrics-panel bg-slate-800 rounded-lg p-4 border border-slate-700">
      <h3 className="text-lg font-semibold mb-3 text-slate-200">Metrics</h3>
      <div className="space-y-2 text-sm">
        <div className="flex justify-between">
          <span className="text-slate-400">Latency:</span>
          <span className="text-slate-200 font-mono">{metrics.latency}ms</span>
        </div>
        <div className="flex justify-between">
          <span className="text-slate-400">Retries:</span>
          <span className="text-slate-200 font-mono">{metrics.retries}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-slate-400">Token Cost:</span>
          <span className="text-slate-200 font-mono">${metrics.tokenCost}</span>
        </div>
      </div>
    </div>
  )
}
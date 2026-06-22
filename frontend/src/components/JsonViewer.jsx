import React from 'react'
import ReactJson from 'react-json-view'
import { useAppContext } from '../context/AppContext'

export default function JsonViewer() {
  const { generatedJson, isLoading } = useAppContext()

  const copyToClipboard = () => {
    if (generatedJson) {
      navigator.clipboard.writeText(JSON.stringify(generatedJson, null, 2))
    }
  }

  return (
    <div className="json-viewer bg-slate-800 rounded-lg p-4 border border-slate-700">
      <div className="flex justify-between items-center mb-3">
        <h3 className="text-lg font-semibold text-slate-200">Generated Config</h3>
        {generatedJson && (
          <button
            onClick={copyToClipboard}
            className="px-3 py-1 text-xs bg-slate-700 hover:bg-slate-600 text-slate-200 rounded transition-colors"
          >
            Copy
          </button>
        )}
      </div>
      {generatedJson ? (
        <div className="bg-slate-900 rounded-lg p-3 overflow-auto max-h-96">
          <ReactJson
            src={generatedJson}
            theme="monokai"
            name={false}
            displayObjectSize={false}
            displayDataTypes={false}
            collapsed={false}
            style={{ fontFamily: 'JetBrains Mono, monospace' }}
          />
        </div>
      ) : (
        <div className="text-slate-500 italic py-8 text-center">
          {isLoading ? 'Compiling...' : 'Awaiting Compilation...'}
        </div>
      )}
    </div>
  )
}
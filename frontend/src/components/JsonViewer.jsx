import React from 'react'

export default function JsonViewer({ config }) {
  return (
    <div className="json-viewer">
      <h3>Generated Config</h3>
      <pre>{JSON.stringify(config, null, 2)}</pre>
    </div>
  )
}
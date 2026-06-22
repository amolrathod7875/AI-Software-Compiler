import React, { useState } from 'react'

export default function PromptInput() {
  const [prompt, setPrompt] = useState('')

  const handleSubmit = async () => {
    const response = await fetch('/api/compile', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    })
    const config = await response.json()
  }

  return (
    <div className="prompt-input">
      <textarea 
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your app requirements..."
      />
      <button onClick={handleSubmit}>Compile</button>
    </div>
  )
}
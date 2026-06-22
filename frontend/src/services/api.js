import axios from 'axios'

const API_BASE = '/api'

export async function generateConfig(prompt) {
  const response = await axios.post(`${API_BASE}/generate`, { prompt })
  return response.data
}
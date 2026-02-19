import axios from 'axios'

const apiUrl = import.meta.env.VITE_API_URL
if (!apiUrl) {
  console.error(
    '[client] VITE_API_URL is not set. ' +
    'Requests will be sent to the current origin, which is wrong in production. ' +
    'Set the VITE_API_URL GitHub secret to your Render backend URL.'
  )
}

const client = axios.create({
  baseURL: (apiUrl || '') + '/api/v1',
  headers: { 'Content-Type': 'application/json' },
})

// Attach JWT on every request
client.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

// Redirect to login on 401
client.interceptors.response.use(
  (res) => res,
  (err) => {
    if (err.response?.status === 401) {
      localStorage.removeItem('access_token')
      window.location.href = '/login'
    }
    return Promise.reject(err)
  }
)

export default client

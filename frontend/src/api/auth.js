import client from './client'

export const register = (name, email, password) =>
  client.post('/auth/register', { name, email, password })

export const login = async (email, password) => {
  // FastAPI OAuth2 expects form data
  const params = new URLSearchParams()
  params.append('username', email)
  params.append('password', password)
  const res = await client.post('/auth/login', params, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  })
  return res.data
}

export const getMe = () => client.get('/auth/me')

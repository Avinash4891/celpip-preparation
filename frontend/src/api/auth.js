import client from './client'

export const register = (name, email, password) =>
  client.post('/auth/register', { name, email, password })

export const login = async (email, password) => {
  const res = await client.post('/auth/login', { email, password })
  return res.data
}

export const getMe = () => client.get('/auth/me')

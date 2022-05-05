import { ENV } from './utils'

async function send({ method, path, token = null, data = null }) {
	const opts = {
		method,
		headers: {}
	}

	if (data) {
		opts.headers['Content-Type'] = 'application/x-www-form-urlencoded'
		opts.body = JSON.stringify(data)
	}

	if (token) {
		opts.headers['Content-type'] = 'application/json'
		opts.headers['Authorization'] = `Bearer ${token}`
	}
	return fetch(`${ENV.VITE_FINDCARE_API_BASE_URL}/${path}`, opts)
		.then((r) => r.json())
		.then((json) => {
			try {
				return JSON.parse(json)
			} catch (err) {
				return json
			}
		})
}

export function get(path, token) {
	return send({ method: 'GET', path, token })
}

export function del(path, token = null) {
	return send({ method: 'DELETE', path, token })
}

export function post(path, data, token = null) {
	return send({ method: 'POST', path, data, token })
}

export function put(path, data, token = null) {
	return send({ method: 'PUT', path, data, token })
}

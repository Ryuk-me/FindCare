import * as api from '$lib/api.js'
import { respond } from './_respond'

export async function post({ request }) {
	const json = await request.json()
	const body = await api.post('api/v1/auth/user', {
		body: json
	})

	return respond(body)
}

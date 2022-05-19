import * as api from '$lib/api.js'
import { respond } from './_respond'

export async function post({ request }) {
	const json = await request.json()
	let url = 'api/v1/auth/user'
	if (json.isDoctor) url = 'api/v1/auth/doctor'
	if(json.isAdmin) url = 'api/v1/auth/admin'
	const body = await api.post(url, {
		body: JSON.stringify(
			`grant_type=&username=${json.username}&password=${json.password}&scope=&client_id=&client_secret=`
		)
	})

	return respond(body)
}

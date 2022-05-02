import 'dotenv/config'
import type { RequestHandler } from '@sveltejs/kit'

export const post: RequestHandler = async ({ request }) => {
	const body = await request.json()
	const response = await fetch('https://nextcare-api-ryuk-me.cloud.okteto.net/api/v1/auth/user', {
		method: 'POST',
		headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
		credentials: 'include',
		body: body
	})
	let ACCESS_TOKEN_EXPIRE_SECONDS: number = parseInt(process.env.ACCESS_TOKEN_EXPIRE_MINUTES) * 60
	let data = await response.json()
	if ('access_token' in data) {

		let headers = {
			'set-cookie': `session=${data.access_token}; Path=/; HttpOnly; Secure; SameSite=Strict;max-age=${ACCESS_TOKEN_EXPIRE_SECONDS}`
		}
		return {
			body: data,
			headers,
		}
	}

	return {
		body: data
	}
}

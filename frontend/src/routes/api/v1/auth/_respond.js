import { ENV } from '$lib/utils'

export function respond(body) {
	if (!body.access_token) {
		return { status: 400, body }
	}

	const access_token = body.access_token
	return {
		headers: {
			'set-cookie': [
				// @ts-ignore
				`session=${access_token}; Path=/; max-age=${
					ENV.VITE_ACCESS_TOKEN_EXPIRE_MINUTES * 60
				}; HttpOnly;`
			]
		},
		body
	}
}

import jwt_decode from 'jwt-decode'

export function respond(body) {
	if (!body.access_token) {
		return { status: 400, body }
	}

	const access_token = body.access_token
	const ACCESS_TOKEN_EXPIRE_MINUTES =
		parseInt(import.meta.env.VITE_ACCESS_TOKEN_EXPIRE_MINUTES) * 60
	return {
		headers: {
			'set-cookie': [
				// @ts-ignore
				`session=${access_token}; Path=/; max-age=${ACCESS_TOKEN_EXPIRE_MINUTES}; HttpOnly;`
			]
		},
		body
	}
}

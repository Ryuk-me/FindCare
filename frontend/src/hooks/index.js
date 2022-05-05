import * as cookie from 'cookie'
import jwt_decode from 'jwt-decode'

const getJWTExp = (token) => {
	const t = jwt_decode(token)
	// @ts-ignore
	return t
}

export async function handle({ event, resolve }) {
	const cookies = cookie.parse(event.request.headers.get('cookie') || '')
	event.locals.session = cookies.session
	const response = await resolve(event)
	const ACCESS_TOKEN_EXPIRE_MINUTES =
		parseInt(import.meta.env.VITE_ACCESS_TOKEN_EXPIRE_MINUTES) * 60
	response.headers['set-cookie'] = `session=${
		event.locals.session || ''
	}; Path=/; max-age=${ACCESS_TOKEN_EXPIRE_MINUTES}; HttpOnly;`
	return response
}

export function getSession({ locals }) {
	if (locals.session) {
		let session = locals.session
		let details = getJWTExp(session)
		return {
			session: session,
            //@ts-ignore
			status: details.status
		}
	}

	return null
}

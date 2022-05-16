import { ENV } from '$lib/utils'
import * as cookie from 'cookie'
import jwt_decode from 'jwt-decode'

const getJWTExp = (token) => {
	const cookie = jwt_decode(token)
	// @ts-ignore
	return cookie
}

export async function handle({ event, resolve }) {
	const cookies = cookie.parse(event.request.headers.get('cookie') || '')
	event.locals.session = cookies.session
	const response = await resolve(event)
	response.headers['set-cookie'] = `session=${event.locals.session || ''}; Path=/; max-age=${
		ENV.VITE_ACCESS_TOKEN_EXPIRE_MINUTES * 60
	}; HttpOnly;`
	return response
}

export function getSession({ locals }) {
	if (locals.session) {
		let session = locals.session
		let details = getJWTExp(session)
		return {
			session: session,
			//@ts-ignore
			status: details.status,
			//@ts-ignore
			profile_image: 'https://cdn-icons-png.flaticon.com/512/3237/3237472.png'
		}
	}

	return null
}

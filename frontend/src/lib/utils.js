export function post(endpoint, data) {
	return fetch(endpoint, {
		method: 'POST',
		credentials: 'include',
		body: JSON.stringify(
			`grant_type=&username=${data.username}&password=${data.password}&scope=&client_id=&client_secret=`
		),
		headers: {
			'Content-Type': 'application/json'
		}
	}).then((r) => r.json())
}

export function capitalize(text) {
	return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase()
}

export const ENV = {
	VITE_ACCESS_TOKEN_EXPIRE_MINUTES: parseInt(import.meta.env.VITE_ACCESS_TOKEN_EXPIRE_MINUTES),
	VITE_FINDCARE_API_BASE_URL: import.meta.env.VITE_FINDCARE_API_BASE_URL
}

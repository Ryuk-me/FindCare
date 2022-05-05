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

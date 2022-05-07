export async function get() {
	return {
		status: 302,
		headers: {
			'set-cookie': `session=; Path=/; Max-Age=-1; HttpOnly`
		}
	}
}

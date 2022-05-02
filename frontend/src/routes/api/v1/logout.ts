import type { RequestHandler } from '@sveltejs/kit'

export const get: RequestHandler = async ({ request }) => {
    return {
        status: 302,
        headers: {
            'set-cookie': `session=; expires=Thu, 18 Dec 2013 12:00:00 UTC; Path=/; HttpOnly`
        },
    };
}

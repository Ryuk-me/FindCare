import * as cookie from 'cookie';

export async function handle({ event, resolve }) {
    const cookies = cookie.parse(event.request.headers.get('cookie') || '');
    event.locals.session = cookies.session;
    const response = await resolve(event);
    response.headers['set-cookie'] = `session=${event.locals.session || ''}; Path=/; HttpOnly`;
    return response;
}
export function getSession(event) {
    return event.locals.session
        ? {
            session: event.locals.session
        }
        : null;
}
import * as cookie from 'cookie';
import jwtDecode from 'jwt-decode';

export async function handle({ event, resolve }) {
    const cookies = cookie.parse(event.request.headers.get('cookie') || '');
    event.locals.session = cookies.session;
    const response = await resolve(event);
    response.headers['set-cookie'] = `session=${event.locals.session || ''}; Path=/; HttpOnly`;
    return response;
}
export function getSession(event) {
    if (event.locals.session) {
        var decoded = jwtDecode(event.locals.session);
        // console.log(decoded);
    }
    return event.locals.session
        ? {
            session: event.locals.session
        }
        : null;
}
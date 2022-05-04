export const check_auth_status_profile = (session, status, redirect) => {
    if (!session) {
        return {
            status: status,
            redirect: redirect
        }
    }
    return {
        props: {
            session: session.session
        }
    }
}

export const check_auth_status_login = (session, status, redirect) => {
    if (session) {
        return {
            status: status,
            redirect: redirect
        }
    }
    return {
        props: {}
    }
}
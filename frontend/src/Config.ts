export const Config = {
    ACCESS_TOKEN_EXPIRE_MINUTES: parseInt(import.meta.env.VITE_ACCESS_TOKEN_EXPIRE_MINUTES as string),
    FINDCARE_API_BASE_URL: import.meta.env.VITE_FINDCARE_API_BASE_URL
}
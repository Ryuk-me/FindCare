import 'dotenv/config'

export const Config = {
    ACCESS_TOKEN_EXPIRE_MINUTES: parseInt(process.env.ACCESS_TOKEN_EXPIRE_MINUTES),
    FINDCARE_API_BASE_URL: process.env.FINDCARE_API_BASE_URL
}
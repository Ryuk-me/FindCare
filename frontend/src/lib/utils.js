export function post(endpoint, data) {
	return fetch(endpoint, {
		method: 'POST',
		credentials: 'include',
		body: JSON.stringify(data),
		headers: {
			'Content-Type': 'application/json'
		}
	}).then((r) => r.json())
}

export function capitalize(text) {
	return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase()
}

export function titleCase(str) {
	var splitStr = str.toLowerCase().split(' ')
	for (var i = 0; i < splitStr.length; i++) {
		splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1)
	}
	return splitStr.join(' ')
}

export function checkUserType(session) {
	if (session?.status === 'user') {
		return {
			status: 302,
			redirect: '/profile'
		}
	} else if (session?.status === 'doctor') {
		return {
			status: 302,
			redirect: '/doctor'
		}
	}
	return {
		status: 302,
		redirect: '/admin/dashboard'
	}
}

export function getFormattedDate(d = null, only_date = false) {
	if (d) var date = new Date(d)
	else var date = new Date()

	var month = date.getMonth() + 1
	var day = date.getDate()
	var hour = date.getHours()
	var min = date.getMinutes()
	const ampm = hour >= 12 ? 'pm' : 'am'
	//@ts-ignore
	month = (month < 10 ? '0' : '') + month
	//@ts-ignore
	day = (day < 10 ? '0' : '') + day
	//@ts-ignore
	hour = (hour < 10 ? '0' : '') + hour
	//@ts-ignore
	min = (min < 10 ? '0' : '') + min

	if (only_date || d) var str = date.getFullYear() + '-' + month + '-' + day
	else var str = date.getFullYear() + '-' + month + '-' + day + ' ' + hour + ':' + min + ' ' + ampm
	return str
}

export function get_am_pm_from_time(time) {
	let new_time = parseInt(time.slice(0, 2))
	let last_two = time.slice(2, 5)
	if (new_time > 12) {
		time = '0' + (new_time - 12 + last_two + ' PM')
	} else if (new_time == 12) {
		time = new_time + time.slice(2, 5) + ' PM'
	} else {
		time = time + ' AM'
	}
	return time
}

export function getFormattedDateDashBoard(d) {
	var date = new Date(d)

	var month = date.getMonth() + 1
	var day = date.getDate()
	var hour = date.getHours()
	var min = date.getMinutes()
	const ampm = hour >= 12 ? 'pm' : 'am'
	//@ts-ignore
	month = (month < 10 ? '0' : '') + month
	//@ts-ignore
	day = (day < 10 ? '0' : '') + day
	//@ts-ignore
	hour = (hour < 10 ? '0' : '') + hour
	//@ts-ignore
	min = (min < 10 ? '0' : '') + min

	var str = date.getFullYear() + '-' + month + '-' + day + ' ' + hour + ':' + min + ' ' + ampm
	return str
}

export const removeAlpha = (event) => {
	const allowedRegex = /[0-9]/g
	if (!event.key.match(allowedRegex)) {
		event.preventDefault()
	}
}

export const removeSpecialCharacters = (event) => {
	const allowedRegex = /[A-Za-z .]/g
	if (!event.key.match(allowedRegex)) {
		event.preventDefault()
	}
}

export const ENV = {
	VITE_ACCESS_TOKEN_EXPIRE_MINUTES: parseInt(import.meta.env.VITE_ACCESS_TOKEN_EXPIRE_MINUTES),
	VITE_FINDCARE_API_BASE_URL: import.meta.env.VITE_FINDCARE_API_BASE_URL
}

export const specialityList = [
	{
		speciality: 'General Physician',
		symptom: 'Fever'
	},
	{
		speciality: 'Cardiologist',
		symptom: 'Fatigue'
	}
	// ,
	// {
	// 	speciality: 'General Physician',
	// 	symptom: 'Nausea'
	// },
	// {
	// 	speciality: 'General Physician',
	// 	symptom: 'Vomiting'
	// },
	// {
	// 	speciality: 'General Physician',
	// 	symptom: 'Back pain'
	// }
]

export const month_name = {
	1: 'Jan',
	2: 'Feb',
	3: 'Mar',
	4: 'Apr',
	5: 'May',
	6: 'Jun',
	7: 'Jul',
	8: 'Aug',
	9: 'Sep',
	10: 'Oct',
	11: 'Nov',
	12: 'Dec'
}

export const status_code = {
	HTTP_100_CONTINUE: 100,
	HTTP_101_SWITCHING_PROTOCOLS: 101,
	HTTP_102_PROCESSING: 102,
	HTTP_103_EARLY_HINTS: 103,
	HTTP_200_OK: 200,
	HTTP_201_CREATED: 201,
	HTTP_202_ACCEPTED: 202,
	HTTP_203_NON_AUTHORITATIVE_INFORMATION: 203,
	HTTP_204_NO_CONTENT: 204,
	HTTP_205_RESET_CONTENT: 205,
	HTTP_206_PARTIAL_CONTENT: 206,
	HTTP_207_MULTI_STATUS: 207,
	HTTP_208_ALREADY_REPORTED: 208,
	HTTP_226_IM_USED: 226,
	HTTP_300_MULTIPLE_CHOICES: 300,
	HTTP_301_MOVED_PERMANENTLY: 301,
	HTTP_302_FOUND: 302,
	HTTP_303_SEE_OTHER: 303,
	HTTP_304_NOT_MODIFIED: 304,
	HTTP_305_USE_PROXY: 305,
	HTTP_306_RESERVED: 306,
	HTTP_307_TEMPORARY_REDIRECT: 307,
	HTTP_308_PERMANENT_REDIRECT: 308,
	HTTP_400_BAD_REQUEST: 400,
	HTTP_401_UNAUTHORIZED: 401,
	HTTP_402_PAYMENT_REQUIRED: 402,
	HTTP_403_FORBIDDEN: 403,
	HTTP_404_NOT_FOUND: 404,
	HTTP_405_METHOD_NOT_ALLOWED: 405,
	HTTP_406_NOT_ACCEPTABLE: 406,
	HTTP_407_PROXY_AUTHENTICATION_REQUIRED: 407,
	HTTP_408_REQUEST_TIMEOUT: 408,
	HTTP_409_CONFLICT: 409,
	HTTP_410_GONE: 410,
	HTTP_411_LENGTH_REQUIRED: 411,
	HTTP_412_PRECONDITION_FAILED: 412,
	HTTP_413_REQUEST_ENTITY_TOO_LARGE: 413,
	HTTP_414_REQUEST_URI_TOO_LONG: 414,
	HTTP_415_UNSUPPORTED_MEDIA_TYPE: 415,
	HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE: 416,
	HTTP_417_EXPECTATION_FAILED: 417,
	HTTP_418_IM_A_TEAPOT: 418,
	HTTP_421_MISDIRECTED_REQUEST: 421,
	HTTP_422_UNPROCESSABLE_ENTITY: 422,
	HTTP_423_LOCKED: 423,
	HTTP_424_FAILED_DEPENDENCY: 424,
	HTTP_425_TOO_EARLY: 425,
	HTTP_426_UPGRADE_REQUIRED: 426,
	HTTP_428_PRECONDITION_REQUIRED: 428,
	HTTP_429_TOO_MANY_REQUESTS: 429,
	HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE: 431,
	HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS: 451,
	HTTP_500_INTERNAL_SERVER_ERROR: 500,
	HTTP_501_NOT_IMPLEMENTED: 501,
	HTTP_502_BAD_GATEWAY: 502,
	HTTP_503_SERVICE_UNAVAILABLE: 503,
	HTTP_504_GATEWAY_TIMEOUT: 504,
	HTTP_505_HTTP_VERSION_NOT_SUPPORTED: 505,
	HTTP_506_VARIANT_ALSO_NEGOTIATES: 506,
	HTTP_507_INSUFFICIENT_STORAGE: 507,
	HTTP_508_LOOP_DETECTED: 508,
	HTTP_510_NOT_EXTENDED: 510,
	HTTP_511_NETWORK_AUTHENTICATION_REQUIRED: 511
}

import Toastify from 'toastify-js'
import 'toastify-js/src/toastify.css'

export function notificationToast(
	text,
	close = false,
	duration = 5000,
	type = null,
	gravity = 'top',
	position = 'right',
	newWindow = true,
	stopOnFocus = true,
	offset = {
		x: 10,
		y: 10
	},
	style = {
		background: '#35baf6'
	}
) {
	if (type == 'success') {
		style = {
			background: '#48BB78'
		}
	}
	if (type == 'error') {
		style = {
			background: '#F56565'
		}
	}
	Toastify({
		text,
		close,
		duration,
		newWindow,
		//@ts-ignore
		gravity,
		//@ts-ignore
		position,
		stopOnFocus,
		offset,
		style
	}).showToast()
}

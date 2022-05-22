<script>
	import { session } from '$app/stores'

	import TableDropdown from '$lib/components/TableDropdown.svelte'
	import { capitalize, ENV, status_code, get_am_pm_from_time } from '$lib/utils'
	import { notificationToast } from '$lib/NotificationToast'
	export let doctorImg
	export let doctorName
	export let clinicAddress
	export let dateOfAppointment
	export let status
	export let color = 'light'
	export let slug
	export let appointment_id
	let city = capitalize(clinicAddress.city)
	let state = capitalize(clinicAddress.state)
	let address = clinicAddress.address
	let is_loading_cancel = false
	const cancelAppointment = async () => {
		is_loading_cancel = true
		const res = await fetch(
			ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/user/appointment/cancel?id=' + appointment_id,
			{
				headers: {
					'Content-type': 'application/json',
					//@ts-ignore
					Authorization: `Bearer ${$session.session}`
				}
			}
		)
		const data = await res.json()
		is_loading_cancel = false
		if (res.status == status_code.HTTP_202_ACCEPTED) {
			notificationToast(data?.detail, true, 2000, 'error')
			status = 'cancelled'
		} else if (res.status == status_code.HTTP_409_CONFLICT)
			notificationToast(data?.detail, false, 2000, 'error')
		else notificationToast('Some unknown error occured', false, 2000, 'error')
	}
</script>

<tr>
	<th
		class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center"
	>
		<img src={doctorImg} class="h-12 w-12 bg-white rounded-full border" alt="..." />
		<a href={'/search/doctor/' + slug}
			><span
				class="ml-3 font-bold {color === 'light'
					? 'text-gray-800'
					: 'text-white'} hover:text-[#0f02fa]"
			>
				{doctorName}
			</span></a
		>
	</th>
	<td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		{dateOfAppointment.split(' ').at(0)}
		{get_am_pm_from_time(dateOfAppointment.split(' ').at(-2))}
	</td>
	<td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		{#if status == 'completed'}
			<i class="fas fa-circle text-teal-500 mr-2" /> {capitalize(status)}
		{/if}
		{#if status == 'cancelled'}
			<i class="fas fa-circle text-red-500 mr-2" /> {capitalize(status)}
		{/if}
		{#if status == 'upcoming'}
			<i class="fas fa-circle text-orange-500 mr-2" /> {capitalize(status)}
		{/if}
	</td>

	<td
		class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 capitalize"
	>
		<span class="capitalize break-words">{address}, {city}, {state}</span>
	</td>
	<td>
		<button
			id={appointment_id}
			disabled={status == 'completed' || status == 'cancelled' || is_loading_cancel ? true : false}
			type="button"
			on:click|preventDefault={cancelAppointment}
			class="text-white  focus:ring-2 focus:outline-none  font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2  {status ==
			'cancelled'
				? 'bg-red-900 cursor-not-allowed'
				: status == 'completed'
				? 'bg-green-700 cursor-not-allowed'
				: 'bg-red-700 hover:bg-red-800 focus:ring-red-300 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800'}"
		>
			<i
				class="{is_loading_cancel
					? 'loading fa fa-spinner fa-spin'
					: status == 'completed' || status == 'cancelled'
					? ''
					: 'fas fa-xmark'} mr-2"
			/>
			{status == 'cancelled' ? 'Cancelled' : status == 'completed' ? 'Completed' : 'Cancel'}
		</button>
	</td>
</tr>

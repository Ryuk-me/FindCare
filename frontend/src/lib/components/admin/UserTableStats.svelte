<script>
	import { session } from '$app/stores'

	import TableDropdown from '$lib/components/TableDropdown.svelte'
	import { notificationToast } from '$lib/NotificationToast'
	import { capitalize, ENV, status_code } from '$lib/utils'

	export let patientImg
	export let patientName
	export let numberOfAppointment
	export let status
	export let id
	export let email
	export let color = 'light'
	let is_loading = false
	const banOrUnbanUser = (is_ban = true) => {
		is_loading = true
		let url = ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/admin/deactivate/user?id=' + id
		if (!is_ban) {
			url = ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/admin/activate/user?id=' + id
		}
		fetch(url, {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
				//@ts-ignore
				Authorization: `Bearer ${$session.session}`
			}
		})
			.then((r) => r.json().then((data) => ({ status_cod: r.status, data })))
			.then((obj) => {
				if (obj.status_cod === status_code.HTTP_200_OK) {
					is_loading = false
					if (!is_ban) {
						notificationToast(obj.data.detail, false, 2000, 'success')
						status = 'active'
					} else {
						notificationToast(obj.data.detail, false, 2000, 'error')
						status = 'banned'
					}
				} else {
					notificationToast(obj.data.detail, false, 2000, 'error')
				}
			})
	}
</script>

<tr>
	<th
		class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center"
	>
		<img src={patientImg} class="h-12 w-12 bg-white rounded-full border" alt="..." />
		<span class="ml-3 font-bold {color === 'light' ? 'btext-blueGray-600' : 'text-whit'}">
			{patientName}
		</span>
	</th><td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		{email}
	</td>
	<td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		{numberOfAppointment}
	</td>
	<td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		{#if status == 'active'}
			<i class="fas fa-circle text-teal-500 mr-2" /> {capitalize(status)}
		{/if}
		{#if status == 'banned'}
			<i class="fas fa-circle text-red-500 mr-2" /> {capitalize(status)}
		{/if}
		{#if status == 'pending'}
			<i class="fas fa-circle text-orange-500 mr-2" /> {capitalize(status)}
		{/if}
	</td>

	<td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		<div class="flex items-center">
			{#if status === 'active' || status === 'pending'}
				<button
					on:click={() => banOrUnbanUser()}
					type="button"
					class="text-white bg-red-700 hover:bg-red-800 focus:ring-2 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800"
				>
					<i class="{is_loading ? 'loading fa fa-spinner fa-spin' : 'fas fa-xmark'} mr-2" /> Ban
				</button>
			{:else}
				<button
					on:click={() => banOrUnbanUser(false)}
					type="button"
					class="text-white bg-green-700-700 hover:bg-green-800 focus:ring-2 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
				>
					<i class="{is_loading ? 'loading fa fa-spinner fa-spin' : 'fas fa-check'}  mr-2" />Unban
				</button>
			{/if}
		</div>
	</td>
</tr>

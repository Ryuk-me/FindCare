<script>
	import { session } from '$app/stores'

	import TableDropdown from '$lib/components/TableDropdown.svelte'
	import { capitalize, ENV, status_code } from '$lib/utils'
	import { notificationToast } from '$lib/NotificationToast'
	export let doctorImg
	export let doctorName
	export let numberOfAppointment
	export let numberOfPatients
	export let doctor_id
	export let status
	export let slug
	export let color = 'light'
	let is_verification_loading = false
	let is_loading = false
	const verifyDoctor = async () => {
		is_verification_loading = true
		const res = await fetch(
			ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/admin/doctor/verify?id=' + doctor_id,
			{
				method: 'POST',
				headers: {
					'Content-type': 'application/json',
					//@ts-ignore
					Authorization: `Bearer ${$session.session}`
				}
			}
		)
		const data = await res.json()
		is_verification_loading = false
		if (res.ok) {
			notificationToast(data.detail, false, 2000, 'success')
			status = 'verified'
		} else {
			notificationToast(data.detail, false, 2000, 'error')
		}
	}
	const banOrUnbanDoctor = (is_ban = true) => {
		is_loading = true
		let url = ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/admin/deactivate/doctor?id=' + doctor_id
		if (!is_ban) {
			url = ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/admin/activate/doctor?id=' + doctor_id
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
						status = 'pending'
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
		<img src={doctorImg} class="h-12 w-12 bg-white rounded-full border" alt="..." />
		<a href={'/search/doctor/' + slug}>
			<span
				class="ml-3 font-bold {color === 'light'
					? 'btext-blueGray-600'
					: 'text-whit'} hover:text-[#0f02fa]"
			>
				{doctorName}
			</span>
		</a>
	</th>
	<td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		{numberOfAppointment}
	</td>
	<td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		{numberOfPatients}
	</td>
	<td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		{#if status == 'verified'}
			<i class="fas fa-circle text-blue-500 mr-2" /> {capitalize(status)}
		{/if}
		{#if status == 'pending'}
			<i class="fas fa-circle text-orange-500 mr-2" /> {capitalize(status)}
		{/if}
		{#if status == 'banned'}
			<i class="fas fa-circle text-red-500 mr-2" /> {capitalize(status)}
		{/if}
	</td>
	<td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		<div class="flex">
			<button
				disabled={status == 'verified' ? true : false}
				type="button"
				on:click={verifyDoctor}
				class="text-white {status == 'verified' || status == 'banned'
					? 'bg-green-900 cursor-not-allowed'
					: 'bg-green-700 hover:bg-green-800 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800'}  focus:ring-2 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2"
			>
				<i
					class="{status == 'verified' ? '' : 'fas fa-check mr-2'} {is_verification_loading
						? 'loading fa fa-spinner fa-spin mr-2'
						: ''}"
				/>
				{status == 'verified' ? 'Verified' : 'Verify'}
			</button>
		</div>
	</td>
	<td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
		<div class="flex items-center">
			<div class="flex items-center">
				{#if status === 'pending' || status === 'verified'}
					<button
						on:click={() => banOrUnbanDoctor()}
						type="button"
						class="text-white bg-red-700 hover:bg-red-800 focus:ring-2 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800"
					>
						<i class="{is_loading ? 'loading fa fa-spinner fa-spin' : 'fas fa-xmark'} mr-2" /> Ban
					</button>
				{:else}
					<button
						on:click={() => banOrUnbanDoctor(false)}
						type="button"
						class="text-white bg-green-700-700 hover:bg-green-800 focus:ring-2 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
					>
						<i class="{is_loading ? 'loading fa fa-spinner fa-spin' : 'fas fa-check'}  mr-2" />Unban
					</button>
				{/if}
			</div>
		</div>
	</td>
</tr>

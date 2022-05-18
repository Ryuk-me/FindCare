<script>
	import { session } from '$app/stores'
	import { capitalize, ENV, status_code, titleCase } from '$lib//utils'
	import { notificationToast } from '../NotificationToast'
	export let response
	let name = ''
	let address = ''
	let fees = ''
	let opens_at = ''
	let closes_at = ''
	let session_time = ''
	let show = false
	let city = response?.address?.city
	let state = response?.address?.state
	let pincode = response?.address?.pincode
	if (response) {
		show = false
		name = response?.name
		address = response?.address?.address
		fees = response?.fees
		opens_at = response?.opens_at
		closes_at = response?.closes_at
		session_time = response?.session_time
	}
	let is_loading = false
	async function addClinic() {
		is_loading = true
		const res = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/doctor/clinic/', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
				//@ts-ignore
				Authorization: `Bearer ${$session.session}`
			},
			body: JSON.stringify({
				name: titleCase(name),
				fees,
				session_time,
				opens_at,
				closes_at,
				is_open: true,
				address: {
					pincode,
					address: titleCase(address),
					city: titleCase(city),
					state: titleCase(state)
				}
			})
		})
		const data = await res.json()
		is_loading = false
		const toastCallBackReload = () => location.reload()
		if (res.status === status_code.HTTP_201_CREATED) {
			notificationToast('Clinic Created', false, 2000, 'success', toastCallBackReload)
			response = data
			show = false
		} else {
			notificationToast(data?.detail, false, 2000, 'error')
		}
	}
</script>

<!--! Clinic data will not be updated -->
{#if response || show}
	<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">Clinic Details</div>
	<div class="form w-full">
		<div class="relative w-full mb-4">
			<label for="name" class="">Clinic Name</label>
			<input
				type="text"
				disabled={show ? false : true}
				bind:value={name}
				class="block border {show
					? ''
					: 'cursor-not-allowed text-gray-400'}  rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="Findcare Clinic"
				autocomplete="on"
			/>
		</div>

		<div class="relative w-full mb-4">
			<label for="about">Addresss</label>
			<input
				type="text"
				disabled={show ? false : true}
				bind:value={address}
				name="about"
				placeholder="Street Number 14"
				title="Enter Address"
				id="about"
				class="block border {show
					? ''
					: 'cursor-not-allowed text-gray-400'}  rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				required
				autocomplete="off"
			/>
		</div>
		<div class="relative w-full mb-4">
			<label for="pincode" class="">Pincode</label>
			<input
				type="number"
				disabled={show ? false : true}
				maxlength="6"
				minlength="6"
				bind:value={pincode}
				class="block border {show
					? ''
					: 'cursor-not-allowed text-gray-400'} rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="800012"
				autocomplete="on"
				required
			/>
		</div>
		<div class="relative w-full mb-4">
			<label for="city" class="">City</label>
			<input
				type="text"
				disabled={show ? false : true}
				bind:value={city}
				class="block border {show
					? ''
					: 'cursor-not-allowed text-gray-400'}  rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="Patna"
				autocomplete="on"
				required
			/>
		</div>
		<div class="relative w-full mb-4">
			<label for="state" class="">State</label>
			<input
				type="text"
				disabled={show ? false : true}
				bind:value={state}
				class="block border {show
					? ''
					: 'cursor-not-allowed text-gray-400'} rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="Bihar"
				autocomplete="on"
				required
			/>
		</div>

		<div class="relative w-full mb-4">
			<label for="fees" class="">Fees (Rs.)</label>
			<input
				type="text"
				disabled={show ? false : true}
				bind:value={fees}
				class="block border {show
					? ''
					: 'cursor-not-allowed text-gray-400'}  rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="Rs.300"
				autocomplete="on"
				required
			/>
		</div>

		<div class="relative w-full mb-4">
			<label for="opens_at" class="">Opens At</label>
			<input
				type="time"
				disabled={show ? false : true}
				bind:value={opens_at}
				class="block border {show
					? ''
					: 'cursor-not-allowed text-gray-400'}  rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="10:00 AM"
				autocomplete="on"
				required
			/>
		</div>

		<div class="relative w-full mb-4">
			<label for="closes_at" class="">Closes At</label>
			<input
				type="time"
				disabled={show ? false : true}
				bind:value={closes_at}
				class="block border {show
					? ''
					: 'cursor-not-allowed text-gray-400'}  rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="04:00 PM"
				autocomplete="on"
				required
			/>
		</div>

		<div class="relative w-full mb-4">
			<label for="session_time" class="">Session Time (in minutes)</label>
			<input
				type="text"
				disabled={show ? false : true}
				bind:value={session_time}
				class="block border {show
					? ''
					: 'cursor-not-allowed text-gray-400'}  rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="20"
				autocomplete="on"
				required
			/>
		</div>

		<div class="relative w-full mb-4 mt-3">
			{#if !response}
				<button
					on:click={addClinic}
					class="{show ? 'bg-primary' : ''}  tracking-wider text-lg {is_loading
						? 'cursor-not-allowed bg-[#7069f5]'
						: ''} w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
					><i class={is_loading ? 'loading fa fa-spinner fa-spin relative right-2' : ''} />Save
					Changes</button
				>
			{/if}
		</div>
	</div>
{:else}
	<div class="flex justify-center mt-48 mb-48 ">
		<button
			class="bg-primary p-4 rounded-sm text-white hover:bg-blue-700"
			on:click={() => (show = true)}
		>
			ADD CLINIC
		</button>
	</div>
{/if}

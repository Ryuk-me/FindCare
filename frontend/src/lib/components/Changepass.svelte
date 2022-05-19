<script>
	import { session } from '$app/stores'
	import { ENV, status_code } from '$lib/utils'
	import { notificationToast } from '$lib/NotificationToast'
	let show = false
	let password = ''
	let confirmPassword = ''
	const handleInput = (event) => {
		password = event.target.value
	}
	let is_loading = false
	const changePassword = async () => {
		is_loading = true
		if (!password || !confirmPassword) {
			notificationToast('Password field cannot be empty', false, 2000, 'error')
			is_loading = false
			return
		}
		if (password !== confirmPassword) {
			notificationToast('Password do not match !', false, 2000, 'error')
			is_loading = false
			return
		}
		const res = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/doctor/change-password', {
			method: 'PUT',
			headers: {
				'Content-type': 'application/json',
				//@ts-ignore
				Authorization: `Bearer ${$session.session}`
			},
			body: JSON.stringify({
				password
			})
		})
		const data = await res.json()
		is_loading = false
		if (res.status === status_code.HTTP_202_ACCEPTED) {
			notificationToast(data?.detail, false, 3000, 'success')
			confirmPassword = ''
		} else {
			notificationToast(data?.detail, false, 3000, 'error')
		}
	}
</script>

<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">Change Password</div>
<div class="form w-full">
	<div class="relative w-full mb-4">
		<label for="changepass" class="">Change Passowrd</label>
		<div class="relative">
			<input
				type={show ? 'text' : 'password'}
				placeholder="********"
				class="block border rounded py-2 pt-3 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				id="password"
				required
				on:input={handleInput}
			/>
			<span>
				<i
					class="fa {show ? 'fa-eye-slash' : 'fa-eye'} hover:cursor-pointer text-slate-600"
					aria-hidden="true"
					id="eye"
					on:click|preventDefault={() => (show = !show)}
				/>
			</span>
		</div>
	</div>
	<div class="relative w-full mb-4">
		<label for="confirmpass" class="">Confirm Password</label>
		<input
			type="password"
			placeholder="********"
			class="block border rounded py-2 pt-3 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			id="password"
			bind:value={confirmPassword}
			autocomplete="off"
			required
		/>
	</div>
	{#if is_loading}
		<button
			on:click={changePassword}
			class="bg-[#7069f5] tracking-wider text-lg cursor-not-allowed w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
			><i class="loading fa fa-spinner fa-spin relative right-2" />Save Changes</button
		>
	{:else}
		<button
			on:click={changePassword}
			class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
			>Save Changes</button
		>
	{/if}
</div>

<style>
	#eye {
		position: absolute;
		right: 14px;
		transform: translate(0, -50%);
		top: 50%;
	}
</style>

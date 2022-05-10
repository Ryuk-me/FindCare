<script context="module">
	import { ENV, status_code } from '$lib/utils'
	export async function load({ params, fetch, session }) {
		const token = params.token
		const resp = await fetch(
			ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/email/verify-password-reset-token?token=' + token
		)
		const data = await resp.json()
		return {
			props: {
				status: resp.status,
				msg: data.detail,
				token: token
			}
		}
	}
</script>

<script>
	export let msg
	export let status
	export let token
	import { notificationToast } from '$lib/NotificationToast'
	import { goto } from '$app/navigation'
	import { session } from '$app/stores'
	let password = ''
	let show = false
	let confirmPassword = ''
	let is_loading = false

	const handleInput = (event) => {
		password = event.target.value
	}
	async function changePassword() {
		is_loading = true
		if (password !== confirmPassword) {
			notificationToast('Password do not match !', false, 2000, 'error')
			is_loading = false
			return
		}
		const resp = await fetch(
			ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/email/change-password-from-reset-token',
			{
				method: 'post',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({
					token,
					password
				})
			}
		)
		const data = await resp.json()
		if (resp.status === status_code.HTTP_202_ACCEPTED) {
			const toastCallbackToLogin = () => {
				$session = null
				goto('/login')
			}
			await fetch('../../auth/logout')
			notificationToast(data.detail, false, 3000, 'success', toastCallbackToLogin)
		} else {
			notificationToast(data.detail, false, 3000, 'error')
		}
		is_loading = false
	}
</script>

<svelte:head>
	<title>Change Password</title>
</svelte:head>

{#if status === status_code.HTTP_202_ACCEPTED}
	<div class="h-screen w-screen flex items-center justify-center">
		<div class="font-maven">
			<h1 class="text-primary text-4xl font-bold font-poppins mb-2">FindCare</h1>
			<div class="border border-primary p-8 rounded">
				<h2 class="text-2xl font-bold mb-2">Change password</h2>
				<form class="">
					<div class="">
						<label for="password">Password</label>
						<input
							type={show ? 'text' : 'password'}
							name="password"
							placeholder="***********"
							title="Enter Your Password"
							id="password"
							class="block border rounded py-2 px-3 w-96 my-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							required
							on:input={handleInput}
							autocomplete="off"
						/>
						<span>
							<i
								class="fa {show
									? 'fa-eye-slash'
									: 'fa-eye'} hover:cursor-pointer text-slate-600 float-right relative bottom-11 right-3"
								aria-hidden="true"
								id="eye"
								on:click|preventDefault={() => (show = !show)}
							/>
						</span>
					</div>
					<div class="">
						<label for="confirmPassword">Confirm Password</label>
						<input
							type="password"
							name="confirmPassword"
							placeholder="***********"
							title="Enter Your Password Again"
							id="confirmPassword"
							class="block border rounded py-2 px-3 w-96 mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							required
							autocomplete="off"
							bind:value={confirmPassword}
						/>
					</div>
					<button
						on:click|preventDefault={changePassword}
						class="mt-4 bg-primary hover:bg-[#524af4] py-2 text-white rounded w-full font-medium"
						>Submit</button
					>
				</form>
			</div>
		</div>
	</div>
{:else}
	<div class="h-screen w-screen flex items-center justify-center">
		<p class="text-5xl">{msg}</p>
	</div>
{/if}

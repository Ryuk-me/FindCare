<script context="module">
	import { checkUserType } from '$lib/utils.js'
	export async function load({ session }) {
		if (session) {
			// This function will check for route access and redirect user to their appropriate routes accordingly
			return checkUserType(session)
		}
		return {}
	}
</script>

<script>
	import { notificationToast } from '$lib/NotificationToast'
	import { session, navigating } from '$app/stores'
	import { goto } from '$app/navigation'
	import { post, capitalize } from '$lib/utils.js'
	import jwt_decode from 'jwt-decode'
	import Loading from '$root/lib/components/Loading.svelte'
	let username = ''
	let password = ''

	let is_loading = false
	async function handleLogin() {
		is_loading = true
		const response = await post(`api/v1/auth/login`, {
			username,
			password,
			isDoctor: false,
			isAdmin: true
		})

		is_loading = false
		if (response?.access_token) {
			const cookie = jwt_decode(response.access_token)
			$session = {
				session: response.access_token,
				//@ts-ignore
				status: cookie.status
			}
			//@ts-ignore
			if ($session.status == 'doctor') goto('/doctor')
			//@ts-ignore
			else if ($session.status == 'admin') goto('/admin/dashboard')
			else goto('/profile')
		} else {
			if (response?.detail[0]?.msg) {
				notificationToast(
					capitalize(response.detail[0].loc?.slice(1).join(', ')).replace(
						/username|Username/gm,
						'Email'
					) +
						' ' +
						response?.detail[0]?.msg,
					false,
					2000,
					'error'
				)
			} else {
				notificationToast(response?.detail, false, 2000, 'error')
			}
		}
	}
</script>

<svelte:head>
	<title>Findcare Admin Login</title>
</svelte:head>

{#if !$navigating}
	<div class="w-screen h-screen flex flex-col justify-center items-center font-maven">
		<div
			class="flex flex-col justify-center items-center w-[90vw] lg:w-[30rem] bg-white rounded drop-shadow-xl mb-8 px-8 py-7"
		>
			<div id="header" class="flex flex-col justify-center items-center">
				<div>
					<img
						src="https://img.icons8.com/external-icongeek26-flat-icongeek26/344/external-admin-project-work-icongeek26-flat-icongeek26.png"
						alt="lock svg"
						class="w-32"
					/>
					<!-- <Locked fill="#635bff" class="w-32 h-32" /> -->
				</div>
				<div>
					<h2 class="text-2xl font-semibold mt-6">Admin Panel</h2>
				</div>
			</div>
			<hr class="h-2" />
			<div id="body" class="flex flex-col w-full justify-center items-center">
				<form class="w-full mt-3 mb-2" on:submit|preventDefault={handleLogin}>
					<label for="email" class="font-bold">Email</label>
					<input
						bind:value={username}
						type="email"
						id="email"
						placeholder="your@domain.com"
						required
						class="block border rounded py-2 px-3 w-full mt-3 mb-4 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
					/>
					<label for="password" class="font-bold">Password</label>
					<input
						bind:value={password}
						type="password"
						id="password"
						placeholder="************"
						required
						class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
					/>
					{#if is_loading}
						<button
							disabled
							class="bg-[#7069f5] cursor-not-allowed text-white mb-3 font-medium py-2 mt-5 w-full rounded focus:outline-none focus:shadow-outline"
							><i class="loading fa fa-spinner fa-spin relative right-2" />Login as Admin</button
						>
					{:else}
						<button
							class="bg-primary hover:bg-[#524af4] text-white mb-3 font-medium py-2 mt-5 w-full rounded focus:outline-none focus:shadow-outline"
							>Login as Admin</button
						>
					{/if}
				</form>
				<div>
					<p>
						Return to <a href="/login" class="text-primary hover:font-semibold font-medium"
							>Login as User</a
						>
					</p>
				</div>
			</div>
		</div>
		<p class="text-center">
			&copy;2022 <a href="./" class="text-primary font-semibold">FindCare</a>. All rights reserved.
		</p>
	</div>
{:else}
	<Loading />
{/if}

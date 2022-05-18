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
	import { session, navigating } from '$app/stores'
	import { goto } from '$app/navigation'
	import { post, capitalize } from '$lib/utils.js'
	import { notificationToast } from '$lib/NotificationToast'
	import shape_png from '$lib/assets/login/shape.png'
	import medical_team_png from '$lib/assets/login/medical-team.png'
	import jwt_decode from 'jwt-decode'
	import Loading from '$lib/components/Loading.svelte'
	import Logo from '$lib/components/Logo.svelte'
	let username = ''
	let password = ''
	let show = false
	let isDoctor = false

	let is_loading = false
	const handleInput = (event) => {
		password = event.target.value
	}
	async function handleLogin() {
		is_loading = true
		const response = await post(`api/v1/auth/login`, { username, password, isDoctor })

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
			else if ($session.status == 'admin') goto('/admin')
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
	<title>Findcare Login | Sign</title>
</svelte:head>

{#if !$navigating}
	<img src={shape_png} alt="shape.png" class="fixed hidden lg:block w-96 bottom-0 left-0" />

	<div
		class="w-screen h-screen flex flex-col justify-center items-center lg:grid lg:grid-cols-2 bg-[#ecf7ff]"
	>
		<div class="flex justify-center items-center lg:ml-48 font-maven">
			<div class="">
				<Logo/>
				<form
					on:submit|preventDefault={handleLogin}
					class="flex flex-col justify-center items-start w-[90vw] lg:w-[35rem] bg-white rounded drop-shadow-xl mb-6 px-8 py-7"
				>
					<h2 class="font-bold my-3 mb-9 text-xl">Sign in to your account</h2>
					<div class="relative w-full mb-4">
						<label for="email" class="">Email</label>
						<input
							type="email"
							class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							placeholder="your@domain.com"
							autocomplete="on"
							bind:value={username}
						/>
					</div>
					<div class="w-full mb-3">
						<div class="flex justify-between">
							<label for="password">Password</label>
							<a href="reset" class="text-primary cursor-pointer hover:font-semibold font-medium"
								>Forgot Password?</a
							>
						</div>
						<div class="relative">
							<input
								type={show ? 'text' : 'password'}
								placeholder="********"
								class="block border rounded py-2 pt-3 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
								id="password"
								autocomplete="off"
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
					<div class="flex flex-col justify-center items-center w-full my-3">
						{#if is_loading}
							<button
								disabled
								class="bg-[#7069f5] cursor-not-allowed tracking-wider text-lg w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
								><i class="loading fa fa-spinner fa-spin relative right-2" />Login</button
							>
						{:else}
							<button
								class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
								>Login</button
							>
						{/if}

						<div class="">
							<label
								for="toggle-example"
								class="flex  flex-row  items-center cursor-pointer relative mb-4"
							>
								<input
									type="checkbox"
									id="toggle-example"
									class="sr-only"
									bind:checked={isDoctor}
								/>
								<div class="toggle-bg bg-gray-200 border-2 border-gray-200 h-6 w-11 rounded-full" />
								<p class="ml-3">Are you a Doctor?</p>
							</label>
						</div>
						<p>
							Don't Have An Account? <a
								href="./signup"
								class="text-primary hover:font-semibold font-medium">Sign Up</a
							>
						</p>
					</div>
				</form>

				<p class="text-center">
					&copy;2022 <a href="./" class="text-primary font-semibold">FindCare</a>. All rights
					reserved.
				</p>
			</div>
		</div>
		<div class="hidden w-full h-screen lg:flex items-end flex-col">
			<img src={medical_team_png} class="hidden lg:block max-h-full" alt="medical-team.png" />
		</div>
	</div>
{:else}
	<Loading />
{/if}

<style>
	#eye {
		position: absolute;
		right: 14px;
		transform: translate(0, -50%);
		top: 50%;
	}
	.toggle-bg:after {
		content: '';
		@apply absolute top-0.5 left-0.5 bg-white border border-gray-300 rounded-full h-5 w-5 transition shadow-sm;
	}

	input:checked + .toggle-bg:after {
		transform: translateX(100%);
		@apply border-white;
	}

	input:checked + .toggle-bg {
		@apply bg-blue-600 border-blue-600;
	}
</style>

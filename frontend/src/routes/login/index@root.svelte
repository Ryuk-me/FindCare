<script context="module">
	export async function load({ session }) {
		if (session) {
			return {
				status: 302,
				redirect: '/profile'
			}
		}
		return {}
	}
</script>

<script>
	import { session } from '$app/stores'
	import { goto } from '$app/navigation'
	import { post, capitalize } from '$lib/utils.js'
	import { notificationToast } from '$lib/NotificationToast'
	import shape_png from '$lib/assets/login/shape.png'
	import medical_team_png from '$lib/assets/login/medical-team.png'
	import jwt_decode from 'jwt-decode'
	let username = ''
	let password = ''
	let show = false
	const handleInput = (event) => {
		password = event.target.value
	}
	async function handleLogin() {
		const response = await post(`api/v1/auth/login`, { username, password })
		if (response?.access_token) {
			const t = jwt_decode(response.access_token)
			$session = {
				session: response.access_token,
				//@ts-ignore
				status: t.status
			}
			//@ts-ignore
			if ($session.status == 'admin') goto('/admin')
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

<img src={shape_png} alt="shape.png" class="fixed hidden lg:block w-96 bottom-0 left-0" />

<div
	class="w-screen h-screen flex flex-col justify-center items-center lg:grid lg:grid-cols-2 bg-[#ecf7ff]"
>
	<div class="flex justify-center items-center lg:ml-48 font-maven">
		<div class="">
			<h2 class="text-primary font-bold font-poppins text-3xl my-4 text-left">FindCare</h2>
			<form
				on:submit|preventDefault={handleLogin}
				class="flex flex-col justify-center items-start w-96 lg:w-[30rem] bg-white rounded drop-shadow-xl mb-6 px-8 py-7"
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
					<button
						class="bg-primary hover:bg-[#524af4] text-white mb-3 font-medium py-2 px-28 rounded focus:outline-none focus:shadow-outline"
						>Login</button
					>
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

<style>
	span {
		position: absolute;
		right: 14px;
		transform: translate(0, -50%);
		top: 50%;
	}
</style>

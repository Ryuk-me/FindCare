<script context="module">
	export const prerender = true
</script>

<script>
	import { notificationToast } from '$lib/NotificationToast'
	import lock_svg from '$lib/assets/reset/lock.svg'
	import { ENV, status_code } from '$lib/utils'
	// import Locked from 'carbon-icons-svelte/lib/Locked.svelte'

	let email = ''
    let password = ''

	let is_loading = false
	
</script>

<svelte:head>
	<title>Findcare Admin Login</title>
</svelte:head>

<div class="w-screen h-screen flex flex-col justify-center items-center font-maven">
	<div
		class="flex flex-col justify-center items-center w-[90vw] lg:w-[30rem] bg-white rounded drop-shadow-xl mb-8 px-8 py-7"
	>
		<div id="header" class="flex flex-col justify-center items-center">
			<div>
				<img src="https://img.icons8.com/external-icongeek26-flat-icongeek26/344/external-admin-project-work-icongeek26-flat-icongeek26.png" alt="lock svg" class="w-32" />
				<!-- <Locked fill="#635bff" class="w-32 h-32" /> -->
			</div>
			<div>
				<h2 class="text-2xl font-semibold mt-6">Admin Panel</h2>
			</div>
		</div>
		<hr class="h-2" />
		<div id="body" class="flex flex-col w-full justify-center items-center">
			<form class="w-full mt-3 mb-2">
				<label for="email" class="font-bold">Email</label>
				<input
					bind:value={email}
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
					Return to <a href="/login" class="text-primary hover:font-semibold font-medium">Login as User</a>
				</p>
			</div>
		</div>
	</div>
	<p class="text-center">
		&copy;2022 <a href="./" class="text-primary font-semibold">FindCare</a>. All rights reserved.
	</p>
</div>

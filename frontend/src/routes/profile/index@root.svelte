<script context="module">
	// export async function load({ session }) {
	// 	if (session?.status === 'admin') {
	// 		return {
	// 			status: 302,
	// 			redirect: '/dashboard'
	// 		}
	// 	}
	// 	if (!session) {
	// 		return {
	// 			status: 302,
	// 			redirect: '/login'
	// 		}
	// 	}
	// 	return {
	// 		props: {
	// 			session
	// 		}
	// 	}
	// }
</script>

<script>
	import Footer from '$lib/components/Footer.svelte'
	import Navbar from '$lib/components/Navbar.svelte'
	// import { goto } from '$app/navigation'
	// import { onMount } from 'svelte'
	// import Loading from '$lib/components/Loading.svelte'
	// import { session as sessionStore } from '$app/stores'
	// import { ENV } from '$lib/utils'
	// export let session

	// async function getUser() {
	// 	const res = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/user/', {
	// 		method: 'GET',
	// 		headers: {
	// 			'Content-type': 'application/json',
	// 			Authorization: `Bearer ${session.session}`
	// 		}
	// 	})
	// 	const data = await res.json()
	// 	await new Promise((r) => setTimeout(r, 5000))
	// 	return data
	// }
	// let isLoading = true
	// let user = null
	// onMount(async () => {
	// 	user = await getUser()
	// 	isLoading = false
	// })

	let title = 'Account Details'
	let show = false
</script>

<svelte:head>
	<title>Profile Page</title>
</svelte:head>
<!-- 
{#if isLoading}
	<Loading />
{:else}

	<p>User profile route</p>
	{#if user}
		{#each Object.entries(user) as [key, value]}
			<p>{key} : {value}</p>
		{/each} -->

<!-- Navbar -->

<Navbar/>

<!-- Profile Page -->

<div class="overflow-hidden ">
	<div
		class="lg:h-screen h-full flex justify-center mx-2 lg:my-0 my-3 lg:flex-row flex-col items-center"
	>
		<div class="navigation px-6 border-2 mb-4 lg:mb-0 rounded-lg pb-7 lg:mr-6">
			<div class="photo flex flex-col justify-center items-center py-7">
				<img
					class="object-cover w-28 h-28 m-6 rounded-full"
					src="https://cdn-icons-png.flaticon.com/512/4825/4825038.png"
					alt=""
				/>
				<!-- <button
							class="bg-primary hover:bg-[#524af4] text-white rounded-md w-full px-7 py-1 font-medium"
							>Change Profile Photo</button
						> -->
				<input
					type="file"
					class="block w-full center text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-primary file:text-white hover:file:bg-[#524af4]"
				/>
			</div>
			<aside class="w-64" aria-label="Sidebar">
				<div class="overflow-y-auto py-4 px-3 bg-primary rounded">
					<ul class="space-y-2">
						<li class="">
							<button
								class=" flex items-center p-2 w-full text-base font-normal text-white rounded-lg  hover:bg-gray-800 "
								on:click={() => (title = 'Account Details')}
								class:active={title == 'Account Details'}
							>
								<svg
									class="w-6 h-6 mr-3"
									aria-hidden="true"
									fill="none"
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									viewBox="0 0 24 24"
									stroke="#FFFFFF"
								>
									<path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
								</svg>
								<span>Profile</span>
							</button>
						</li>
						<li>
							<button
								class="flex items-center p-2 w-full text-base font-normal text-white rounded-lg  hover:bg-gray-800 "
								on:click={() => (title = 'Change Password')}
								class:active={title == 'Change Password'}
							>
								<svg
									x="0"
									y="0"
									viewBox="0 0 512 512"
									style="enable-background:new 0 0 512 512"
									xml:space="preserve"
									class="w-6 h-6 mr-3"
									><g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M463.743,48.257c-64.343-64.343-169.037-64.342-233.38,0c-43.946,43.946-59.206,108.725-40.185,167.483L4.395,401.524    C1.581,404.337,0,408.153,0,412.132v84.866C0,505.284,6.717,512,15.002,512h84.866c3.98,0,7.794-1.581,10.609-4.395l21.22-21.22    c3.241-3.242,4.823-7.787,4.293-12.341l-2.648-22.783l31.584-2.977c7.172-0.676,12.852-6.355,13.528-13.527l2.979-31.588    l22.785,2.648c4.254,0.497,8.512-0.851,11.71-3.698c3.196-2.846,5.025-6.923,5.025-11.204v-27.938h27.43    c3.949,0,7.738-1.557,10.547-4.333l37.272-36.842c58.772,19.051,123.583,3.794,167.542-40.166    C528.085,217.294,528.085,112.599,463.743,48.257z M442.527,260.421c-37.866,37.865-94.666,49.684-144.703,30.114    c-5.522-2.159-11.796-0.865-16.011,3.302l-39.593,39.136H205.95c-8.285,0-15.002,6.717-15.002,15.002v26.093l-21.28-2.473    c-4.009-0.465-8.035,0.703-11.172,3.241c-3.136,2.539-5.118,6.234-5.497,10.252l-3.253,34.489l-34.486,3.25    c-4.018,0.379-7.713,2.36-10.253,5.497c-2.539,3.136-3.708,7.164-3.242,11.172l3.582,30.804l-11.694,11.697h-63.65v-63.649    l188.097-188.097c4.214-4.214,5.535-10.523,3.364-16.073c-19.572-50.038-7.751-106.836,30.114-144.703    c52.646-52.644,138.304-52.644,190.948,0C495.17,122.118,495.17,207.777,442.527,260.421z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M421.309,90.69c-17.548-17.549-46.102-17.548-63.649,0c-17.548,17.548-17.548,46.101,0,63.649    c17.547,17.548,46.101,17.55,63.649,0C438.857,136.791,438.857,108.238,421.309,90.69z M400.093,133.123    c-5.849,5.849-15.366,5.85-21.216,0c-5.849-5.849-5.849-15.366,0-21.216c5.865-5.864,15.352-5.864,21.216,0    C405.957,117.771,405.956,127.259,400.093,133.123z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
									</g></svg
								>
								<span class="">Change Password</span>
							</button>
						</li>
						<li>
							<a href="/logout">
								<button
									class="flex items-center w-full p-2 text-base font-normal text-white rounded-lg  hover:bg-gray-800 "
								>
									<svg
										class="w-6 h-6 mr-3"
										aria-hidden="true"
										fill="none"
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										viewBox="0 0 24 24"
										stroke="#FFFFFF"
									>
										<path
											d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"
										/>
									</svg>
									<span>Log out</span>
								</button>
							</a>
						</li>
					</ul>
				</div>
			</aside>
		</div>

		<div
			class="data border-2 flex flex-col justify-center items-start w-[90vw] lg:w-[35rem] bg-white rounded px-8 py-7"
		>
			{#if title == 'Account Details'}
				<div class="text-xl text-center border-b p-3 w-full mb-4 font-bold">
					{title}
				</div>
				<div class="form w-full">
					<div class="relative w-full mb-4">
						<label for="name" class="">Name</label>
						<input
							type="text"
							class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							placeholder="your@domain.com"
							autocomplete="on"
						/>
					</div>
					<div class="relative w-full mb-4">
						<label for="email" class="">Email</label>
						<input
							type="email"
							class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							placeholder="your@domain.com"
							autocomplete="on"
						/>
					</div>
					<div class="relative w-full mb-4">
						<label for="phone" class="">Phone Number</label>
						<input
							type="number"
							class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							placeholder="your@domain.com"
							autocomplete="on"
						/>
					</div>
					<div class="relative w-full mb-4">
						<label for="dob" class="">Date Of Birth</label>
						<input
							type="date"
							class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							placeholder="your@domain.com"
							autocomplete="on"
						/>
					</div>
					<button
						class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
						>Save Changes</button
					>
				</div>
			{/if}

			{#if title == 'Change Password'}
				<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">
					{title}
				</div>
				<div class="form w-full">
					<div class="relative w-full mb-4">
						<label for="changepass" class="">Change Passowrd</label>
						<div class="relative">
							<input
								type={show ? 'text' : 'password'}
								placeholder="********"
								class="block border rounded py-2 pt-3 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
								id="password"
								autocomplete="off"
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
							autocomplete="off"
						/>
					</div>
					<button
						class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
						>Save Changes</button
					>
				</div>
			{/if}
		</div>
	</div>
</div>

<!-- Footer -->

<Footer/>

<!-- 
	{/if}
	<button
		class="bg-orange-500 text-black"
		on:click={() => {
			$sessionStore = null
			goto('/logout')
		}}
	>
		Logout
	</button>
{/if} -->
<style>
	button.active {
		background-color: rgb(31 41 55);
	}
	#eye {
		position: absolute;
		right: 14px;
		transform: translate(0, -50%);
		top: 50%;
	}
</style>

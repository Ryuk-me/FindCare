<script context="module">
	export async function load({ session }) {
		if (!session) {
			return {
				status: 302,
				redirect: '/login'
			}
		}
		if (session?.status === 'user') {
			const res = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/user/', {
				method: 'GET',
				headers: {
					'Content-type': 'application/json',
					Authorization: `Bearer ${session.session}`
				}
			})
			const user = await res.json()
			return {
				props: {
					session,
					user
				}
			}
		} else {
			if (session?.status === 'admin') {
				return {
					status: 302,
					redirect: '/admin'
				}
			} else {
				return {
					status: 302,
					redirect: '/doctor'
				}
			}
		}
	}
</script>

<script>
	import Footer from '$lib/components/Footer.svelte'
	import Navbar from '$lib/components/Navbar.svelte'
	import UserAvatar from 'carbon-icons-svelte/lib/UserAvatar.svelte'
	import Password from 'carbon-icons-svelte/lib/Password.svelte'
	import Logout from 'carbon-icons-svelte/lib/Logout.svelte'
	import { goto } from '$app/navigation'
	import { session as sessionStore } from '$app/stores'
	import { user as userProfileStore } from '../../stores'
	import { ENV, removeAlpha, removeSpecialCharacters } from '$lib/utils'
	export let user, session

	let title = 'Account Details'
	let show = false

	// USER DETAILS UPDATE
	let name = user?.name
	let email = user?.email
	let dob = user?.dob
	let phone = user?.phone
	let gender = user?.gender
	let profile_image = user?.profile_image
	let password = ''
	let confirmPassword = ''
	$userProfileStore = {
		profile_image: profile_image
	}
	const handleInput = (event) => {
		password = event.target.value
	}
	let isSomethingChanged = false
	$: if (
		!(user?.name === name) ||
		!(user?.email === email) ||
		!(user?.dob === dob) ||
		!(user?.phone === phone && phone?.length === 10) ||
		(password && confirmPassword)
	) {
		isSomethingChanged = true
	} else {
		isSomethingChanged = false
	}
</script>

<svelte:head>
	<title>{user.name}</title>
</svelte:head>

<Navbar />

<!-- Profile Page -->

<div class="overflow-hidden ">
	<div
		class="lg:h-screen h-full flex justify-center mx-2 lg:my-0 my-3 lg:flex-row flex-col items-center"
	>
		<div class="navigation px-6 border-2 mb-4 lg:mb-0 rounded-lg pb-7 lg:mr-6">
			<div class="photo flex flex-col justify-center items-center py-7">
				<img
					class="object-cover w-28 h-28 m-6 rounded-full"
					src={profile_image}
					alt="user profile"
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
				<div class="overflow-y-auto py-4 px-3 rounded">
					<ul class="space-y-2">
						<li class="">
							<button
								class=" flex items-center p-2 w-full text-base font-normal rounded-lg  "
								on:click={() => (title = 'Account Details')}
								class:active={title == 'Account Details'}
							>
								{#if title == 'Account Details'}
									<UserAvatar fill="#FFFFFF" class="w-6 h-6 mr-3" />
								{:else}
									<UserAvatar fill="#635bff" class="w-6 h-6 mr-3" />
								{/if}
								<span>Profile</span>
							</button>
						</li>
						<li>
							<button
								class="flex items-center p-2 w-full text-base font-normal rounded-lg  "
								on:click={() => (title = 'Change Password')}
								class:active={title == 'Change Password'}
							>
								{#if title == 'Change Password'}
									<Password fill="#FFFFFF" class="w-6 h-6 mr-3" />
								{:else}
									<Password fill="#635bff" class="w-6 h-6 mr-3" />
								{/if}
								<span>Change Password</span>
							</button>
						</li>
						<li>
							<button
								class="flex items-center w-full p-2 text-base font-normal rounded-lg"
								on:click={() => {
									$sessionStore = null
									$userProfileStore = null
									goto('/logout')
								}}
							>
								{#if title == 'Log out'}
									<Logout fill="#FFFFFF" class="w-6 h-6 mr-3" />
								{:else}
									<Logout fill="#635bff" class="w-6 h-6 mr-3" />
								{/if}
								<span>Log out</span>
							</button>
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
							bind:value={name}
							on:keypress={removeSpecialCharacters}
							autocomplete="off"
							required
						/>
					</div>
					<div class="relative w-full mb-4">
						<label for="email" class="">Email</label>
						<input
							type="email"
							class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							bind:value={email}
							autocomplete="on"
						/>
					</div>
					<div class="relative w-full mb-4">
						<label for="phone" class="">Phone Number</label>
						<input
							type="tel"
							class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							bind:value={phone}
							maxlength="10"
							minlength="10"
							on:keypress={removeAlpha}
							autocomplete="off"
						/>
					</div>

					<div class="relative w-full mb-4">
						<label for="gender" class="">Gender</label>
						<input
							type="text"
							class="block border capitalize rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary text-gray-400"
							bind:value={gender}
							disabled
						/>
					</div>
					<div class="relative w-full mb-4">
						<label for="dob" class="">Date Of Birth</label>
						<input
							type="date"
							class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							bind:value={dob}
							placeholder={dob}
							autocomplete="off"
							min="1950-01-01"
							max={`${new Date().getFullYear()}-01-01`}
						/>
					</div>
					{#if isSomethingChanged}
						<button
							class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
							>Save Changes</button
						>{:else}
						<button
							disabled
							class="bg-[#7069f5] tracking-wider text-lg cursor-not-allowed w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
							>Save Changes</button
						>
					{/if}
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
								on:input={handleInput}
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
							bind:value={confirmPassword}
						/>
					</div>
					{#if isSomethingChanged}
						<button
							class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
							>Save Changes</button
						>{:else}
						<button
							disabled
							class="bg-[#7069f5] tracking-wider text-lg cursor-not-allowed w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
							>Save Changes</button
						>
					{/if}
				</div>
			{/if}
		</div>
	</div>
</div>

<!-- Footer -->

<Footer />

<style>
	button.active {
		background-color: #635bff;
		color: white;
	}
	#eye {
		position: absolute;
		right: 14px;
		transform: translate(0, -50%);
		top: 50%;
	}
</style>

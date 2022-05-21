<script>
	import { goto } from '$app/navigation'
	import { session } from '$app/stores'
	import { user as userProfileStore } from '../../stores'
	import Login from 'carbon-icons-svelte/lib/Login.svelte'
	import Logo from '$lib/components/Logo.svelte'
	import jwt_decode from 'jwt-decode'
	let user = $session ? true : false
	let userType = null
	if ($session) {
		//@ts-ignore
		const cookie = jwt_decode($session.session)
		//@ts-ignore
		userType = cookie.status
	}

	let menu = true
	let profileMenu = true
	$: profile = $userProfileStore?.profile_image
		? $userProfileStore?.profile_image
		: 'https://cdn-icons-png.flaticon.com/512/3135/3135715.png'
</script>

<nav class="bg-white border-black px-2 sm:px-4 py-2.5 rounded">
	<div class="container flex flex-wrap justify-between items-center mx-auto">
		<Logo />
		{#if !user}
			<div class="flex-col lg:flex hidden lg:flex-row mx-6 md:order-2 justify-center items-center">
				<a href="/login" class="font-semibold mr-7 hover:text-[#524af4]">Login</a>
				<a href="/signup"
					><button
						class="bg-primary hover:bg-[#524af4] text-white rounded-full w-full px-7 py-1 font-medium"
						>Sign up</button
					></a
				>
			</div>
			<div class="flex relative items-center md:order-2 lg:hidden">
				<a href="/login"><Login class="text-lg hover:color-[#524af4] w-6 h-6" /></a>
			</div>
		{/if}

		{#if user}
			<div class="flex relative items-center md:order-2">
				<button
					type="button"
					class="flex  mr-3 text-sm rounded-full md:mr-0 focus:ring-2  focus:ring-sky-200"
					id="user-menu-button"
					aria-expanded="false"
					data-dropdown-toggle="dropdown"
					on:click|preventDefault={() => (profileMenu = !profileMenu)}
				>
					<span class="sr-only">Open user menu</span>
					<img class="w-10 h-10 rounded-full" src={profile} alt="" />
				</button>

				<div
					class="{profileMenu
						? 'hidden'
						: ''} absolute right-0 top-8 z-50 my-4 w-40 text-base list-none text-black bg-white border border-gray-100 rounded divide-y  "
					id="dropdown"
					data-popper-placement="bottom"
				>
					<ul
						class="absolute right-0 w-40 p-2 mt-2 space-y-2 text-white bg-white border border-gray-100 rounded-md shadow-md  dark:border-indigo-700 dark:text-white dark:bg-indigo-700"
						aria-label="submenu"
					>
						{#if userType === 'user'}
							<li class="flex">
								<a
									class="inline-flex items-center w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
									href="/profile"
								>
									<svg
										class="w-4 h-4 mr-3"
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
								</a>
							</li>
						{/if}

						<li class="flex">
							<a
								class="inline-flex items-center w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
								href="/"
							>
								<svg
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									stroke="currentColor"
									width="16"
									height="16"
									x="0"
									y="0"
									viewBox="0 0 512 512"
									style="enable-background:new 0 0 512 512"
									xml:space="preserve"
									class="w-4 h-4 mr-3"
									><g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M462,44h-47.667V30c0-16.542-13.458-30-30-30s-30,13.458-30,30v14h-168V30c0-16.542-13.458-30-30-30s-30,13.458-30,30    v14.37c-0.85-0.235-1.741-0.37-2.666-0.37H83.823c-27.57,0-50,22.43-50,50v170.333c0,5.523,4.478,10,10,10s10-4.477,10-10V147    h360.51c5.522,0,10-4.477,10-10s-4.478-10-10-10H53.823V94c0-16.542,13.458-30,30-30h39.844c0.925,0,1.816-0.136,2.666-0.37V76.5    c0,16.542,13.458,30,30,30s30-13.458,30-30V64h168v12.5c0,16.542,13.458,30,30,30s30-13.458,30-30V64H462    c16.542,0,30,13.458,30,30v379.994c0,9.928-8.077,18.006-18.006,18.006s-18.006-8.078-18.006-18.006v-25.869    c0-5.523-4.478-10-10-10H329.667c-5.522,0-10,4.477-10,10s4.478,10,10,10h106.321v15.869c0,6.511,1.648,12.643,4.545,18.006H38    c-9.925,0-18-8.075-18-18v-15.875h223.825c5.522,0,10-4.477,10-10s-4.478-10-10-10h-99.916    c17.474-15.049,28.57-37.309,28.57-62.125c0-45.215-36.785-82-82-82c-45.215,0-82,36.785-82,82    c0,24.816,11.096,47.076,28.57,62.125H10c-5.522,0-10,4.477-10,10V474c0,20.953,17.047,38,38,38h435.994    C494.95,512,512,494.951,512,473.994V94C512,66.43,489.57,44,462,44z M166.333,76.5c0,5.514-4.486,10-10,10s-10-4.486-10-10V30    c0-5.514,4.486-10,10-10s10,4.486,10,10V76.5z M394.333,76.5c0,5.514-4.486,10-10,10c-5.514,0-10-4.486-10-10V30    c0-5.514,4.486-10,10-10c5.514,0,10,4.486,10,10V76.5z M28.479,376c0-34.187,27.813-62,62-62s62,27.813,62,62s-27.813,62-62,62    S28.479,410.187,28.479,376z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M468.309,129.93c-1.859-1.86-4.439-2.93-7.069-2.93c-2.631,0-5.21,1.07-7.07,2.93c-1.86,1.86-2.93,4.44-2.93,7.07    s1.069,5.21,2.93,7.07c1.861,1.86,4.439,2.93,7.07,2.93c2.63,0,5.21-1.07,7.069-2.93c1.86-1.86,2.931-4.44,2.931-7.07    S470.17,131.79,468.309,129.93z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M298.649,441.05c-1.859-1.86-4.439-2.92-7.069-2.92s-5.21,1.06-7.07,2.92c-1.86,1.87-2.93,4.44-2.93,7.07    c0,2.64,1.069,5.21,2.93,7.08c1.86,1.86,4.44,2.92,7.07,2.92s5.21-1.06,7.069-2.92c1.86-1.87,2.931-4.45,2.931-7.08    C301.58,445.49,300.51,442.92,298.649,441.05z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M226.245,304c-20.953,0-38,17.047-38,38s17.047,38,38,38s38-17.047,38-38S247.198,304,226.245,304z M226.245,360    c-9.925,0-18-8.075-18-18s8.075-18,18-18s18,8.075,18,18S236.17,360,226.245,360z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M319.578,304c-20.953,0-38,17.047-38,38s17.047,38,38,38s38-17.047,38-38S340.531,304,319.578,304z M319.578,360    c-9.925,0-18-8.075-18-18s8.075-18,18-18s18,8.075,18,18S329.503,360,319.578,360z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M412.912,304c-20.953,0-38,17.047-38,38s17.047,38,38,38c20.953,0,38-17.047,38-38S433.865,304,412.912,304z M412.912,360    c-9.925,0-18-8.075-18-18s8.075-18,18-18s18,8.075,18,18S422.837,360,412.912,360z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M132.912,200c-20.953,0-38,17.047-38,38s17.047,38,38,38s38-17.047,38-38S153.865,200,132.912,200z M132.912,256    c-9.925,0-18-8.075-18-18s8.075-18,18-18c9.925,0,18,8.075,18,18S142.837,256,132.912,256z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M319.578,200c-20.953,0-38,17.047-38,38s17.047,38,38,38s38-17.047,38-38S340.531,200,319.578,200z M319.578,256    c-9.925,0-18-8.075-18-18s8.075-18,18-18s18,8.075,18,18S329.503,256,319.578,256z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M412.912,200c-20.953,0-38,17.047-38,38s17.047,38,38,38c20.953,0,38-17.047,38-38S433.865,200,412.912,200z M412.912,256    c-9.925,0-18-8.075-18-18s8.075-18,18-18s18,8.075,18,18S422.837,256,412.912,256z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M226.245,200c-20.953,0-38,17.047-38,38s17.047,38,38,38s38-17.047,38-38S247.198,200,226.245,200z M226.245,256    c-9.925,0-18-8.075-18-18s8.075-18,18-18s18,8.075,18,18S236.17,256,226.245,256z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
										<g xmlns="http://www.w3.org/2000/svg">
											<g>
												<path
													d="M126.104,351.629c-3.906-3.905-10.236-3.905-14.143,0l-32.566,32.567l-11.129-11.129c-3.906-3.905-10.236-3.905-14.143,0    c-3.905,3.905-3.905,10.237,0,14.143l18.201,18.199c1.876,1.875,4.419,2.929,7.071,2.929c2.652,0,5.195-1.054,7.071-2.929    l39.638-39.638C130.009,361.866,130.009,355.534,126.104,351.629z"
													fill="#FFFFFF"
													data-original="#000000"
													class=""
												/>
											</g>
										</g>
									</g></svg
								>

								{#if userType === 'user'}
									<a href="/profile/appointment"> <span>Appointments</span></a>
								{:else if userType === 'doctor'}
									<a href="/doctor"> <span>Dashboard</span></a>
								{:else}
									<a href="/admin/dashboard"> <span>Dashboard</span></a>
								{/if}
							</a>
						</li>

						<li class="flex">
							<!-- svelte-ignore a11y-invalid-attribute -->
							<a
								href="#"
								class="inline-flex items-center w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
								on:click={() => {
									$session = null
									$userProfileStore = null
									goto('/logout')
								}}
							>
								<svg
									class="w-4 h-4 mr-3"
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
							</a>
						</li>
					</ul>
				</div>
			</div>
		{/if}
		<button
			data-collapse-toggle="mobile-menu-2"
			type="button"
			class="inline-flex items-center p-2 ml-1 text-sm text-black rounded-lg md:hidden hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-sky-200"
			aria-controls="mobile-menu-2"
			aria-expanded="false"
			on:click|preventDefault={() => (menu = !menu)}
		>
			<span class="sr-only">Open main menu</span>
			<svg
				class="w-6 h-6"
				fill="currentColor"
				viewBox="0 0 20 20"
				xmlns="http://www.w3.org/2000/svg"
				><path
					fill-rule="evenodd"
					d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
					clip-rule="evenodd"
				/></svg
			>
			<svg
				class="hidden w-6 h-6"
				fill="currentColor"
				viewBox="0 0 20 20"
				xmlns="http://www.w3.org/2000/svg"
				><path
					fill-rule="evenodd"
					d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
					clip-rule="evenodd"
				/></svg
			>
		</button>
		<div
			class="{menu
				? 'hidden'
				: ''} justify-between items-center w-full md:flex md:w-auto md:order-1"
			id="mobile-menu-2"
		>
			<ul class="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-semibold">
				<li>
					<a href="/" class="block px-3 py-2 pr-4 pl-3 mx-3 hover:text-[#fb3434]">Home</a>
				</li>
				<li>
					<a href="/about-us" class="block px-3 py-2 pr-4 pl-3 mx-3 hover:text-[#fb3434]">About</a>
				</li>
				<li>
					<a href="/support" class="block px-3 py-2 pr-4 pl-3 mx-3 hover:text-[#fb3434]">Support</a>
				</li>
				<li>
					<a href="/contact" class="block px-3 py-2 pr-4 pl-3 mx-3 hover:text-[#fb3434]">Contact</a>
				</li>
			</ul>
		</div>
	</div>
</nav>

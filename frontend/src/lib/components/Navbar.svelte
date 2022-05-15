<script>
	let menu = false
	let isProfileMenuOpen = false
	let isLoggedIn = false
</script>

<div
	class="navbar flex items-center lg:justify-between p-4 lg:px-24 lg:w-auto w-screen"
>
	<div class="flex justify-between lg:w-auto w-full items-center">
		<div class="flex flex-row w-full lg:w-auto">
			<div>
				<i
					class="fa-solid {menu
						? 'fa-times'
						: 'fa-bars'} text-primary p-2 mt-2 inline-flex rounded ml-auto lg:hidden md:hidden"
					id="menu"
					on:click|preventDefault={() => (menu = !menu)}
				/>
			</div>
			<div class="p-2 mr-4 text-primary text-3xl font-bold tracking-wide font-poppins">
				<a href="/">Find<span class="text-[#fb3434]">Care</span></a>
			</div>
		</div>
        {#if !isLoggedIn}
		<div class="lg:hidden">
			<a href="/login"
				><button
					class="bg-primary hover:bg-[#524af4] text-white rounded-full w-full px-5 py-1.5 font-light"
					>Login</button
				></a
			>
		</div>
        {/if}
	</div>

	<div
		class="lg:w-auto {menu
			? 'block'
			: 'hidden'} lg:flex md:flex lg:flex-row flex-col flex mb-5 lg:mb-0 font-semibold"
	>
		<a href="/" class="px-3 mx-3 hover:text-[#fb3434]">Home</a>
		<a href="/about-us" class="px-3 mx-3 hover:text-[#fb3434]">About</a>
		<a href="/support" class="px-3 mx-3 hover:text-[#fb3434]">Support</a>
		<a href="/contact" class="px-3 mx-3 hover:text-[#fb3434]">Contact</a>
	</div>
	{#if !isLoggedIn}
		<div class="flex-col lg:flex hidden lg:flex-row mx-6 justify-center items-center">
			<a href="/login" class="font-semibold mr-7 hover:text-[#524af4]">Login</a>
			<a href="/signup"
				><button
					class="bg-primary hover:bg-[#524af4] text-white rounded-full w-full px-7 py-1 font-medium"
					>Sign up</button
				></a
			>
		</div>
	{/if}
    {#if isLoggedIn}
	<div>
		<ul>
			<li class="relative">
				<button
					id="nav-profile-photo"
					class="align-middle rounded-full focus:shadow-outline-purple focus:outline-none"
					on:mouseover={() => (isProfileMenuOpen = !isProfileMenuOpen)}
					
					on:click|preventDefault={() => (isProfileMenuOpen = !isProfileMenuOpen)}
                    on:focus={() => (console.log("menu opened")
                    )}
                   
					aria-label="Account"
					aria-haspopup="true"
				>
					<img
						class="object-cover w-8 h-8 rounded-full"
						src="https://cdn-icons-png.flaticon.com/512/4825/4825038.png"
						aria-hidden="true"
						alt=""
					/>
				</button>
				{#if isProfileMenuOpen}
					<ul
						class="absolute right-0 w-40 p-2 mt-2 space-y-2 text-white bg-white border border-gray-100 rounded-md shadow-md  dark:border-indigo-700 dark:text-white dark:bg-indigo-700"
						aria-label="submenu"
					>
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

								<span>Appointments</span>
							</a>
						</li>

						<li class="flex">
							<a
								class="inline-flex items-center w-full px-2 py-1 text-sm font-semibold transition-colors duration-150 rounded-md hover:bg-gray-100 hover:text-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200"
								href="/logout"
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
				{/if}
			</li>
		</ul>
	</div>
    {/if}
</div>

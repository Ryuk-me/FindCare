<script>
	let menu = false
	import homepage_doctor from '$lib/assets/homepage/homepage-doctor.png'
	import appointment from '$lib/assets/homepage/appointment.png'
	import livechat from '$lib/assets/homepage/livechat.png'
	import live_chat_icon from '$lib/assets/homepage/live-chat.svg'
	import hour24_icon from '$lib/assets/homepage/24hour.svg'
	import appointment_icon from '$lib/assets/homepage/appointment.svg'
	import onlineConsultation_icon from '$lib/assets/homepage/onlineConsultation.svg'
	import medical_assistance from '$lib/assets/homepage/medical-assistance.png'
	import Footer from '$lib/components/Footer.svelte'
</script>

<svelte:head>
	<title>Findcare</title>
</svelte:head>

<div class="">
	<!-- Navbar -->

	<div
		class="navbar flex items-center flex-wrap lg:justify-between p-4 lg:px-24 lg:w-auto w-screen"
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
			<div class="lg:hidden">
				<a href="/login"
					><button
						class="bg-primary hover:bg-[#524af4] text-white rounded-full w-full px-5 py-1.5 font-light"
						>Login</button
					></a
				>
			</div>
		</div>
		<div
			class="lg:w-auto {menu
				? 'block'
				: 'hidden'} lg:flex md:flex lg:flex-row flex-col flex mb-5 lg:mb-0 font-semibold"
		>
			<a href="/" class="px-3 mx-3 hover:text-[#fb3434]">Home</a>
			<a href="/about" class="px-3 mx-3 hover:text-[#fb3434]">About</a>
			<a href="/support" class="px-3 mx-3 hover:text-[#fb3434]">Support</a>
			<a href="/contact" class="px-3 mx-3 hover:text-[#fb3434]">Contact</a>
		</div>
		<div class="flex-col lg:flex hidden lg:flex-row mx-6 justify-center items-center">
			<a href="/login" class="font-semibold mr-7 hover:text-[#524af4]">Login</a>
			<a href="/signup"
				><button
					class="bg-primary hover:bg-[#524af4] text-white rounded-full w-full px-7 py-1 font-medium"
					>Sign up</button
				></a
			>
		</div>
	</div>

	<!-- hero section -->

	<section class="text-gray-600 lg:px-24">
		<div
			class="container mx-auto flex px-5 py-16 font-['Open_Sans'] md:flex-row flex-col items-center"
		>
			<div
				class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center"
			>
				<h1 id="hero" class="title-font lg:text-5xl text-4xl mb-4 font-bold text-black">
					Let's find your
					<br class="hidden lg:inline-block" /><span class="text-[#fb3434] lg:text-6xl text-5xl"
						>Doctor</span
					>
				</h1>
				<p class="mb-8 leading-relaxed">
					Get appointment with your doctor to get <br />personalized care
				</p>
				<div class="flex justify-center relative lg:w-[30vw] w-[90vww]">
					<input
						type="text"
						class="block border rounded-full py-2 pl-3 pr-10 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary  border-primary"
						placeholder="Search Doctor or Symptoms..."
						autocomplete="on"
						id="search"
					/>
					<span class="search-glass">
						<i class="fa-solid fa-magnifying-glass" />
					</span>
				</div>
			</div>
			<div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
				<img class="object-cover object-center rounded" alt="hero" src={homepage_doctor} />
			</div>
		</div>
	</section>

	<!-- Features -->

	<div
		class="px-4 py-16 mx-auto sm:max-w-xl font-['Open_Sans'] md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-24 lg:py-20"
	>
		<div class="max-w-xl mb-10 md:mx-auto sm:text-center lg:max-w-2xl md:mb-12">
			<h2
				class="max-w-lg mb-6 font-sans text-3xl font-bold leading-none tracking-tight text-gray-900 sm:text-4xl md:mx-auto"
			>
				<span class="relative">Our Medical Services</span>
			</h2>
			<p class="text-base text-gray-700 md:text-lg">
				Lorem, ipsum dolor sit amet consectetur adipisicing elit. Exercitationem, ipsum est
				blanditiis, totam culpa id repellendus nesciunt possimus tempore a, quis molestias nam animi
				cumque maxime commodi ea ad. Accusantium?
			</p>
		</div>
		<div class="upper-feature">
			<div class="grid gap-4 row-gap-5 sm:grid-cols-2 lg:grid-cols-4">
				<div class="flex flex-col justify-center items-center p-5 border rounded shadow-sm">
					<div>
						<div class="flex items-center justify-center w-16 h-16 ">
							<img src={onlineConsultation_icon} alt="" />
							<h6 class="mb-2 font-semibold pl-4 text-center leading-5">Online Consultation</h6>
						</div>
					</div>
				</div>
				<div class="flex flex-col justify-center items-center p-5 border rounded shadow-sm">
					<div>
						<div class="flex items-center justify-center w-16 h-16  ">
							<img src={live_chat_icon} alt="" />
							<h6 class="mb-2 font-semibold pl-4 text-center leading-5">Live Chat</h6>
						</div>
					</div>
				</div>
				<div class="flex flex-col justify-center items-center p-5 border rounded shadow-sm">
					<div>
						<div class="flex items-center justify-center w-16 h-16 ">
							<img src={hour24_icon} alt="" />
							<h6 class="mb-2 font-semibold pl-4 text-center leading-5">24 Hour Service</h6>
						</div>
					</div>
				</div>
				<div class="flex flex-col justify-center items-center p-5 border rounded shadow-sm">
					<div>
						<div class="flex items-center justify-center w-16 h-16 ">
							<img src={appointment_icon} alt="" />
							<h6 class="mb-2 font-semibold pl-4 text-center leading-5">Appointment</h6>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

	<!-- Online Consultation -->

	<section class="text-gray-600 font-['Open_Sans'] lg:px-24 bg-[#f1f0ff]">
		<div
			class="container mx-auto flex px-5 py-16 md:flex-row flex-col justify-between items-center"
		>
			<div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 lg:pr-24 lg:pl-16 md:pr-16">
				<img class="object-cover object-center w-3/5 rounded" alt="hero" src={medical_assistance} />
			</div>
			<div class="lg:max-w-lg lg:w-full lg:text-right md:w-1/2 lg:pt-0 pt-5 w-5/6">
				<h1 class="title-font lg:text-5xl text-4xl mb-4 font-bold text-black">
					Online Consultation
				</h1>
				<p class="mb-8 leading-relaxed">
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque libero est exercitationem
					asperiores rerum eius amet. Sunt suscipit amet cum ducimus hic iure eos. Dolorum quidem
					explicabo mollitia temporibus atque unde animi!
				</p>
			</div>
		</div>
	</section>

	<!-- Live Chat -->

	<section class="text-gray-600 font-['Open_Sans'] lg:px-24">
		<div
			class="container mx-auto flex px-5 py-16 md:flex-row flex-col justify-between items-center"
		>
			<div class="lg:max-w-lg lg:w-full lg:text-right md:w-1/2 lg:pt-0 pt-5 w-5/6">
				<h1 class="title-font lg:text-5xl text-4xl mb-4 font-bold text-black">Live Chat</h1>
				<p class="mb-8 leading-relaxed">
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque libero est exercitationem
					asperiores rerum eius amet. Sunt suscipit amet cum ducimus hic iure eos. Dolorum quidem
					explicabo mollitia temporibus atque unde animi!
				</p>
			</div>
			<div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 lg:pl-24 lg:pr-16 md:pl-16">
				<img class="object-cover object-center w-3/4 rounded" alt="hero" src={livechat} />
			</div>
		</div>
	</section>

	<!-- Appointment -->

	<section class="text-gray-600 font-['Open_Sans'] lg:px-24 bg-[#f1f0ff]">
		<div
			class="container mx-auto flex px-5 py-16 md:flex-row flex-col justify-between items-center"
		>
			<div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 lg:pr-24 lg:pl-16 md:pr-16">
				<img class="object-cover object-center w-3/4 rounded" alt="hero" src={appointment} />
			</div>
			<div class="lg:max-w-lg lg:w-full lg:text-right md:w-1/2 lg:pt-0 pt-5 w-5/6">
				<h1 class="title-font lg:text-5xl text-4xl mb-4 font-bold text-black">Appointment</h1>
				<p class="mb-8 leading-relaxed">
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque libero est exercitationem
					asperiores rerum eius amet. Sunt suscipit amet cum ducimus hic iure eos. Dolorum quidem
					explicabo mollitia temporibus atque unde animi!
				</p>
			</div>
		</div>
	</section>

	<!-- Team -->

	<section class="text-gray-600 font-['Open_Sans'] lg:px-24">
		<div class="container px-5 py-24 mx-auto">
			<div class="flex flex-col text-center w-full mb-20">
				<h1 class="text-3xl font-bold title-font mb-4 text-gray-900">OUR TEAM</h1>
				<p class="lg:w-2/3 mx-auto leading-relaxed text-base">
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis voluptate, blanditiis
					inventore quidem consectetur recusandae quibusdam. Nisi impedit natus veritatis, quas
					quasi a totam tempora accusamus sapiente, modi officiis molestias.
				</p>
			</div>
			<div class="flex flex-wrap -m-4">
				<div class="p-4 lg:w-1/4 md:w-1/2">
					<div class="h-full flex flex-col items-center text-center">
						<img
							alt="team"
							class="flex-shrink-0 rounded-lg w-full h-56 object-cover object-center mb-4"
							src="https://img.freepik.com/free-vector/young-anonymous-hacker-with-flat-design_23-2147879457.jpg?t=st=1652263532~exp=1652264132~hmac=5945e992471fbd1678a5e0813e946f1036c9890f3a2e7d8ce146af371f1c275b&w=740hacker-using-laptop_4090770.htm#query=coder&position=5&from_view=search"
						/>
						<div class="w-full">
							<h2 class="title-font font-semibold text-lg text-gray-900">Aman Sharma</h2>
							<h3 class="text-gray-500 mb-3">Frontend Developer</h3>
							<p class="mb-4">To develop website features that can enhance the user experience.</p>
							<span class="inline-flex">
								<a href="https://github.com/adgamerx" class="text-gray-500">
									<svg
										xmlns="http://www.w3.org/2000/svg"
										width="24"
										height="24"
										shape-rendering="geometricPrecision"
										text-rendering="geometricPrecision"
										image-rendering="optimizeQuality"
										fill-rule="evenodd"
										clip-rule="evenodd"
										viewBox="0 0 640 640"
										><path
											d="M319.988 7.973C143.293 7.973 0 151.242 0 327.96c0 141.392 91.678 261.298 218.826 303.63 16.004 2.964 21.886-6.957 21.886-15.414 0-7.63-.319-32.835-.449-59.552-89.032 19.359-107.8-37.772-107.8-37.772-14.552-36.993-35.529-46.831-35.529-46.831-29.032-19.879 2.209-19.442 2.209-19.442 32.126 2.245 49.04 32.954 49.04 32.954 28.56 48.922 74.883 34.76 93.131 26.598 2.882-20.681 11.15-34.807 20.315-42.803-71.08-8.067-145.797-35.516-145.797-158.14 0-34.926 12.52-63.485 32.965-85.88-3.33-8.078-14.291-40.606 3.083-84.674 0 0 26.87-8.61 88.029 32.8 25.512-7.075 52.878-10.642 80.056-10.76 27.2.118 54.614 3.673 80.162 10.76 61.076-41.386 87.922-32.8 87.922-32.8 17.398 44.08 6.485 76.631 3.154 84.675 20.516 22.394 32.93 50.953 32.93 85.879 0 122.907-74.883 149.93-146.117 157.856 11.481 9.921 21.733 29.398 21.733 59.233 0 42.792-.366 77.28-.366 87.804 0 8.516 5.764 18.473 21.992 15.354 127.076-42.354 218.637-162.274 218.637-303.582 0-176.695-143.269-319.988-320-319.988l-.023.107z"
										/></svg
									>
								</a>
							</span>
						</div>
					</div>
				</div>
				<div class="p-4 lg:w-1/4 md:w-1/2">
					<div class="h-full flex flex-col items-center text-center">
						<img
							alt="team"
							class="flex-shrink-0 rounded-lg w-full h-56 object-cover object-center mb-4"
							src="https://img.freepik.com/free-vector/young-anonymous-hacker-with-flat-design_23-2147879457.jpg?t=st=1652263532~exp=1652264132~hmac=5945e992471fbd1678a5e0813e946f1036c9890f3a2e7d8ce146af371f1c275b&w=740"
						/>
						<div class="w-full">
							<h2 class="title-font font-semibold text-lg text-gray-900">Amardeep Anand</h2>
							<h3 class="text-gray-500 mb-3">UI/UX Developer</h3>
							<p class="mb-4">To plan and design the structure and design of web pages</p>
							<span class="inline-flex">
								<a href="/" class="text-gray-500">
									<svg
										xmlns="http://www.w3.org/2000/svg"
										width="24"
										height="24"
										shape-rendering="geometricPrecision"
										text-rendering="geometricPrecision"
										image-rendering="optimizeQuality"
										fill-rule="evenodd"
										clip-rule="evenodd"
										viewBox="0 0 640 640"
										><path
											d="M319.988 7.973C143.293 7.973 0 151.242 0 327.96c0 141.392 91.678 261.298 218.826 303.63 16.004 2.964 21.886-6.957 21.886-15.414 0-7.63-.319-32.835-.449-59.552-89.032 19.359-107.8-37.772-107.8-37.772-14.552-36.993-35.529-46.831-35.529-46.831-29.032-19.879 2.209-19.442 2.209-19.442 32.126 2.245 49.04 32.954 49.04 32.954 28.56 48.922 74.883 34.76 93.131 26.598 2.882-20.681 11.15-34.807 20.315-42.803-71.08-8.067-145.797-35.516-145.797-158.14 0-34.926 12.52-63.485 32.965-85.88-3.33-8.078-14.291-40.606 3.083-84.674 0 0 26.87-8.61 88.029 32.8 25.512-7.075 52.878-10.642 80.056-10.76 27.2.118 54.614 3.673 80.162 10.76 61.076-41.386 87.922-32.8 87.922-32.8 17.398 44.08 6.485 76.631 3.154 84.675 20.516 22.394 32.93 50.953 32.93 85.879 0 122.907-74.883 149.93-146.117 157.856 11.481 9.921 21.733 29.398 21.733 59.233 0 42.792-.366 77.28-.366 87.804 0 8.516 5.764 18.473 21.992 15.354 127.076-42.354 218.637-162.274 218.637-303.582 0-176.695-143.269-319.988-320-319.988l-.023.107z"
										/></svg
									>
								</a>
							</span>
						</div>
					</div>
				</div>
				<div class="p-4 lg:w-1/4 md:w-1/2">
					<div class="h-full flex flex-col items-center text-center">
						<img
							alt="team"
							class="flex-shrink-0 rounded-lg w-full h-56 object-cover object-center mb-4"
							src="https://img.freepik.com/free-vector/young-anonymous-hacker-with-flat-design_23-2147879457.jpg?t=st=1652263532~exp=1652264132~hmac=5945e992471fbd1678a5e0813e946f1036c9890f3a2e7d8ce146af371f1c275b&w=740"
						/>
						<div class="w-full">
							<h2 class="title-font font-semibold text-lg text-gray-900">Neeraj Kumar</h2>
							<h3 class="text-gray-500 mb-3">Backend Developer</h3>
							<p class="mb-4">
								Participate in the entire application by doing coding and debugging.
							</p>
							<span class="inline-flex">
								<a href="https://github.com/Ryuk-me" class="text-gray-500">
									<svg
										xmlns="http://www.w3.org/2000/svg"
										width="24"
										height="24"
										shape-rendering="geometricPrecision"
										text-rendering="geometricPrecision"
										image-rendering="optimizeQuality"
										fill-rule="evenodd"
										clip-rule="evenodd"
										viewBox="0 0 640 640"
										><path
											d="M319.988 7.973C143.293 7.973 0 151.242 0 327.96c0 141.392 91.678 261.298 218.826 303.63 16.004 2.964 21.886-6.957 21.886-15.414 0-7.63-.319-32.835-.449-59.552-89.032 19.359-107.8-37.772-107.8-37.772-14.552-36.993-35.529-46.831-35.529-46.831-29.032-19.879 2.209-19.442 2.209-19.442 32.126 2.245 49.04 32.954 49.04 32.954 28.56 48.922 74.883 34.76 93.131 26.598 2.882-20.681 11.15-34.807 20.315-42.803-71.08-8.067-145.797-35.516-145.797-158.14 0-34.926 12.52-63.485 32.965-85.88-3.33-8.078-14.291-40.606 3.083-84.674 0 0 26.87-8.61 88.029 32.8 25.512-7.075 52.878-10.642 80.056-10.76 27.2.118 54.614 3.673 80.162 10.76 61.076-41.386 87.922-32.8 87.922-32.8 17.398 44.08 6.485 76.631 3.154 84.675 20.516 22.394 32.93 50.953 32.93 85.879 0 122.907-74.883 149.93-146.117 157.856 11.481 9.921 21.733 29.398 21.733 59.233 0 42.792-.366 77.28-.366 87.804 0 8.516 5.764 18.473 21.992 15.354 127.076-42.354 218.637-162.274 218.637-303.582 0-176.695-143.269-319.988-320-319.988l-.023.107z"
										/></svg
									>
								</a>
							</span>
						</div>
					</div>
				</div>
				<div class="p-4 lg:w-1/4 md:w-1/2">
					<div class="h-full flex flex-col items-center text-center">
						<img
							alt="team"
							class="flex-shrink-0 rounded-lg w-full h-56 object-cover object-center mb-4"
							src="https://img.freepik.com/free-vector/young-anonymous-hacker-with-flat-design_23-2147879457.jpg?t=st=1652263532~exp=1652264132~hmac=5945e992471fbd1678a5e0813e946f1036c9890f3a2e7d8ce146af371f1c275b&w=740"
						/>
						<div class="w-full">
							<h2 class="title-font font-semibold text-lg text-gray-900">Nitin Shivam</h2>
							<h3 class="text-gray-500 mb-3">Database Administrator</h3>
							<p class="mb-4">Creating database design, creation, and testing activities.</p>
							<span class="inline-flex">
								<a href="https://github.com/nitinshivam" class="text-gray-500">
									<svg
										xmlns="http://www.w3.org/2000/svg"
										width="24"
										height="24"
										shape-rendering="geometricPrecision"
										text-rendering="geometricPrecision"
										image-rendering="optimizeQuality"
										fill-rule="evenodd"
										clip-rule="evenodd"
										viewBox="0 0 640 640"
										><path
											d="M319.988 7.973C143.293 7.973 0 151.242 0 327.96c0 141.392 91.678 261.298 218.826 303.63 16.004 2.964 21.886-6.957 21.886-15.414 0-7.63-.319-32.835-.449-59.552-89.032 19.359-107.8-37.772-107.8-37.772-14.552-36.993-35.529-46.831-35.529-46.831-29.032-19.879 2.209-19.442 2.209-19.442 32.126 2.245 49.04 32.954 49.04 32.954 28.56 48.922 74.883 34.76 93.131 26.598 2.882-20.681 11.15-34.807 20.315-42.803-71.08-8.067-145.797-35.516-145.797-158.14 0-34.926 12.52-63.485 32.965-85.88-3.33-8.078-14.291-40.606 3.083-84.674 0 0 26.87-8.61 88.029 32.8 25.512-7.075 52.878-10.642 80.056-10.76 27.2.118 54.614 3.673 80.162 10.76 61.076-41.386 87.922-32.8 87.922-32.8 17.398 44.08 6.485 76.631 3.154 84.675 20.516 22.394 32.93 50.953 32.93 85.879 0 122.907-74.883 149.93-146.117 157.856 11.481 9.921 21.733 29.398 21.733 59.233 0 42.792-.366 77.28-.366 87.804 0 8.516 5.764 18.473 21.992 15.354 127.076-42.354 218.637-162.274 218.637-303.582 0-176.695-143.269-319.988-320-319.988l-.023.107z"
										/></svg
									>
								</a>
							</span>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- CTA -->

	<section class="bg-[#f1f0ff]">
		<div class="flex flex-col justify-center items-center px-5 py-4">
			<div>
				<h1
					class="flex-grow lg:pr-0 sm:pr-16 lg:text-4xl text-3xl  font-medium title-font my-4 text-gray-900"
				>
					Need a Doctor for checkup?
				</h1>
			</div>
			<div>
				<h1
					class="flex-grow lg:pr-0 sm:pr-16 lg:text-2xl text-xl  font-medium title-font my-4 text-gray-900"
				>
					Just make an appointment and you are done!
				</h1>
			</div>
			<div>
				<a href="#hero"
					><button
						class="bg-primary block hover:bg-[#524af4] my-4 text-white w-full lg:px-24 px-14 rounded-md py-3 font-light"
						>Get an appointment <i class="fa-solid fa-arrow-right" /></button
					></a
				>
			</div>
		</div>
	</section>

	<!-- Footer -->

	<Footer />
</div>

<style>
	.search-glass {
		position: absolute;
		right: 16px;
		transform: translate(0, -50%);
		top: 60%;
	}
</style>

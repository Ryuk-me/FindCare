<script>
	import Footer from '$lib/components/Footer.svelte'
	import Navbar from '$lib/components/Navbar.svelte'
	import Loading from '$lib/components/Loading.svelte'
	import { navigating } from '$app/stores'
</script>

<svelte:head>
	<title>About us</title>
</svelte:head>
{#if $navigating}
	<Loading />
{:else}
	<!-- Navbar -->

	<Navbar />

	<!-- Body -->

	<div>
		<section class="text-gray-600 body-font">
			<div class="container px-5 pb-18 pt-12 mx-auto flex flex-col">
				<div class="lg:w-4/6 mx-auto">
					<h1 class="text-center text-6xl mb-6 font-bold">About Us</h1>
					<div class="rounded-lg h-80 overflow-hidden">
						<img
							alt="content"
							class="object-cover object-center h-full w-full"
							src="https://img.freepik.com/free-photo/young-handsome-physician-medical-robe-with-stethoscope_1303-17818.jpg?t=st=1652272465~exp=1652273065~hmac=75eba2804f2ec33fb9d12688667388a334990196d37f31de6ccbd2e542be36ec&w=996"
						/>
					</div>
					<div class="flex flex-col sm:flex-row mt-10">
						<div
							class="sm:w-2/3 sm:pl-8 sm:py-8 sm:border-l border-gray-200 sm:border-t-0 border-t mt-4 pt-4 sm:mt-0 text-center sm:text-left"
						>
							<p class="leading-relaxed text-lg mb-4">
								<b>FindCare</b> is an online platform to bridge the gap between patients and doctors by offering efficient, convenient and affordable way of booking appointments with the best doctors, consult them. 
								This idea is not new in urban areas since other firms are already active there, but they are not so active in small cities and rural areas. Since, about 70% of India resides in the villages a vast population are unable to avail these kinds of online facilities due to illiteracy, lack of awareness and communication gap.
								Moreover, a huge bunch of people are unaware of good doctors and healthcare facilities. So, our main aim is to cover these rural areas and fix the health problems in a very holistic manner by increasing the accessibility of doctors and enhancing the ability of users to communicate with doctors anytime anywhere.
								FindCare will act as a link between the people and the doctors with ease. People can book appointments through our website with just at a click. They would not have to waste their time and money on transportations, lodging and fooding in case those people must go outstations for taking appointments.
							</p>
						</div>
					</div>
				</div>

				<!-- Our Motive -->

				<!-- Our Team -->

				<section class="text-gray-600 font-['Open_Sans'] lg:px-24">
					<div class="container px-5 py-24 mx-auto">
						<div class="flex flex-col text-center w-full mb-20">
							<h1 class="text-3xl font-bold title-font mb-4 text-gray-900">OUR TEAM</h1>
							<p class="lg:w-2/3 mx-auto leading-relaxed text-base">
								We are a team of young professionals who have put in efforts to solve social challenges.
							</p>
						</div>
						<div class="flex flex-wrap -m-4">
							<div class="p-4 lg:w-1/4 md:w-1/2">
								<div class="h-full flex flex-col items-center text-center">
									<img
										alt="team"
										class="flex-shrink-0 rounded-lg w-full h-56 object-cover object-center mb-4"
										src="https://avatars.githubusercontent.com/u/48490538?v=4"
									/>
									<div class="w-full">
										<h2 class="title-font font-semibold text-lg text-gray-900">Aman Sharma</h2>
										<h3 class="text-gray-500 mb-3">Frontend Developer</h3>
										<p class="mb-4">
											To develop website features that can enhance the user experience.
										</p>
										<span class="inline-flex">
											<a href="https://github.com/adgamerx" target="_blank" class="text-gray-500">
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
										src="https://findcare-ryuk-me.cloud.okteto.net/dev/nitin.jpg"
									/>
									<div class="w-full">
										<h2 class="title-font font-semibold text-lg text-gray-900">Nitin Shivam</h2>
										<h3 class="text-gray-500 mb-3">Frontend Developer</h3>
										<p class="mb-4">To develop website features that can enhance the user experience.</p>
										<span class="inline-flex">
											<a
												href="https://github.com/nitinshivam"
												target="_blank"
												class="text-gray-500"
											>
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
										src="https://findcare-ryuk-me.cloud.okteto.net/dev/amardeep.jpg"
									/>
									<div class="w-full">
										<h2 class="title-font font-semibold text-lg text-gray-900">Amardeep Anand</h2>
										<h3 class="text-gray-500 mb-3">UI/UX Developer</h3>
										<p class="mb-4">To plan and design the structure and design of web pages</p>
										<span class="inline-flex">
											<a href="/" target="_blank" class="text-gray-500">
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
										src="https://findcare-ryuk-me.cloud.okteto.net/dev/neeraj.jpg"
									/>
									<div class="w-full">
										<h2 class="title-font font-semibold text-lg text-gray-900">Neeraj Kumar</h2>
										<h3 class="text-gray-500 mb-3">Backend Developer</h3>
										<p class="mb-4">
											Participate in the entire application by doing coding and debugging.
										</p>
										<span class="inline-flex">
											<a href="https://github.com/Ryuk-me" target="_blank" class="text-gray-500">
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
			</div>
		</section>
	</div>

	<!-- Footer -->

	<Footer />
{/if}

<script>
	import homepage_doctor from '$lib/assets/homepage/homepage-doctor.png'
	import appointment from '$lib/assets/homepage/appointment.png'
	import livechat from '$lib/assets/homepage/livechat.png'
	import live_chat_icon from '$lib/assets/homepage/live-chat.svg'
	import hour24_icon from '$lib/assets/homepage/24hour.svg'
	import appointment_icon from '$lib/assets/homepage/appointment.svg'
	import onlineConsultation_icon from '$lib/assets/homepage/onlineConsultation.svg'
	import medical_assistance from '$lib/assets/homepage/medical-assistance.png'
	import ellipse1 from '$lib/assets/homepage/Ellipse1.png'
	import ellipse2 from '$lib/assets/homepage/Ellipse2.png'
	import ellipse3 from '$lib/assets/homepage/Ellipse3.png'
	import Footer from '$lib/components/Footer.svelte'
	import Navbar from '$lib/components/Navbar.svelte'


</script>

<svelte:head>
	<title>Findcare</title>
</svelte:head>

<div class="relative">
	<img src={ellipse1} alt="" class="lg:block absolute hidden w-56 top-[85vh] left-0" />

	<!-- Navbar -->

	<Navbar />

	<!-- hero section -->

	<section class="text-gray-600 lg:px-24">
		<div
			class="container mx-auto flex px-5 py-16 font-sans md:flex-row flex-col items-center"
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
		class="px-4 py-16 mx-auto sm:max-w-xl font-sans md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-24 lg:py-20"
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

	<section class="text-gray-600 font-sans relative lg:px-24 bg-[#f1f0ff]">
		<img src={ellipse2} alt="" class="lg:block absolute hidden w-24 top-6 right-0" />
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

	<section class="text-gray-600 font-sans relative lg:px-24">
		<img src={ellipse3} alt="" class="lg:block absolute hidden w-24 top-6 left-0" />
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

	<section class="text-gray-600 font-sans relative lg:px-24 bg-[#f1f0ff]">
		<img src={ellipse2} alt="" class="lg:block absolute hidden w-24 top-6 right-0" />
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

	<!-- CTA -->

	<section class="">
		<div class="flex flex-col justify-center items-center px-5 py-16">
			<div>
				<h1
					class="flex-grow lg:pr-0 lg:text-2xl text-3xl font-medium title-font mt-4 text-gray-900"
				>
					Need a Doctor for checkup?
				</h1>
			</div>
			<div>
				<h1
					class="flex-grow lg:pr-0 lg:text-3xl text-xl  font-medium title-font my-4 text-gray-900"
				>
					Just make an appointment and you are done!
				</h1>
			</div>
			<div>
				<a href="#hero"
					><button
						class="bg-primary block hover:bg-[#524af4] my-4 text-white w-full lg:px-24 px-14 rounded-md py-3 font-light"
						>Get an appointment<svg
							fill="none"
							stroke="currentColor"
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							class="w-4 h-4 ml-2 inline-block"
							viewBox="0 0 24 24"
						>
							<path d="M5 12h14M12 5l7 7-7 7" />
						</svg></button
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

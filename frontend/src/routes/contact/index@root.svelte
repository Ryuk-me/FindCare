<script>
	import Footer from '$lib/components/Footer.svelte'
	import Navbar from '$lib/components/Navbar.svelte'
	var Tawk_API = Tawk_API || {},
		Tawk_LoadStart = new Date()
	;(function () {
		var s1 = document.createElement('script'),
			s0 = document.getElementsByTagName('script')[0]
		s1.async = true
		s1.src = 'https://embed.tawk.to/627bb66d7b967b11798ed7c4/1g2pk1831'
		s1.charset = 'UTF-8'
		s1.setAttribute('crossorigin', '*')
		s0.parentNode.insertBefore(s1, s0)
	})()
</script>

<!-- Navbar -->

<Navbar />

<!-- Body -->

<section class="text-gray-600 body-font relative">
	<h1 class="text-center text-6xl mt-6 font-bold">Contact</h1>
	<div class="container px-5 py-24 mx-auto flex sm:flex-nowrap flex-wrap">
		<div
			class="lg:w-2/3 md:w-1/2 bg-gray-300 rounded-lg overflow-hidden sm:mr-10 p-10 flex items-end justify-start relative"
		>
			<iframe
				width="100%"
				height="100%"
				class="absolute inset-0"
				frameborder="0"
				title="map"
				marginheight="0"
				marginwidth="0"
				scrolling="no"
				loading="lazy"
				referrerpolicy="no-referrer-when-downgrade"
				src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3597.8465751033054!2d85.11168141482352!3d25.610013983705933!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39ed58239b8cea0b%3A0x2a46edc4b8ee1b11!2sSona%20Enclave!5e0!3m2!1sen!2sin!4v1652273595706!5m2!1sen!2sin"
				style="filter: opacity(0.7);"
			/>
			<div class="bg-white relative flex flex-wrap py-6 rounded shadow-md">
				<div class="lg:w-1/2 px-6">
					<h2 class="title-font font-semibold text-gray-900 tracking-widest text-xs">ADDRESS</h2>
					<p class="mt-1">Sona Enclave, MohanPur, Rajbansi Nagar, Patna, Bihar 800023</p>
				</div>
				<div class="lg:w-1/2 px-6 mt-4 lg:mt-0">
					<h2 class="title-font font-semibold text-gray-900 tracking-widest text-xs">EMAIL</h2>
					<a href="mailto:support@findcare.in" class="text-indigo-500 leading-relaxed">support@findcare.in</a>
					<h2 class="title-font font-semibold text-gray-900 tracking-widest text-xs mt-4">PHONE</h2>
					<p class="leading-relaxed">123-456-7890</p>
				</div>
			</div>
		</div>
		<div class="lg:w-1/3 md:w-1/2 bg-white flex flex-col md:ml-auto w-full md:py-8 mt-8 md:mt-0">
			<h2 class="text-gray-900 text-xl mb-1 font-medium title-font">Get In Touch</h2>
			<p class="leading-relaxed mb-5 text-gray-600">
				So many ways to Reach Us from wherever you are - online, by email, over a call, in your
				city, or even on social media.
			</p>
			<div class="relative mb-4">
				<label for="name" class="leading-7 text-sm text-gray-600">Name</label>
				<input
					type="text"
					id="name"
					name="name"
					class="w-full bg-white rounded border border-gray-300 focus:border-primary focus:ring-1 focus:ring-primary text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
				/>
			</div>
			<div class="relative mb-4">
				<label for="email" class="leading-7 text-sm text-gray-600">Email</label>
				<input
					type="email"
					id="email"
					name="email"
					class="w-full bg-white rounded border border-gray-300 focus:border-primary focus:ring-1 focus:ring-primary text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
				/>
			</div>
			<div class="relative mb-4">
				<label for="message" class="leading-7 text-sm text-gray-600">Message</label>
				<textarea
					id="message"
					name="message"
					class="w-full bg-white rounded border border-gray-300 focus:border-primary focus:ring-1 focus:ring-primary h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
				/>
			</div>
			<button
				class="text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-[#524af4] rounded text-lg"
				>Submit</button
			>
		</div>
	</div>
</section>
<!--Start of Tawk.to Script-->
	<!--End of Tawk.to Script-->
<!-- Footer -->

<Footer />

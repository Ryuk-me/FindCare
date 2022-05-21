<script>
	import Footer from '$lib/components/Footer.svelte'
	import Navbar from '$lib/components/Navbar.svelte'
	import Loading from '$lib/components/Loading.svelte'
	import { navigating } from '$app/stores'
	import { ENV, status_code } from '$lib/utils'
	import { notificationToast } from '$lib/NotificationToast'

	let name
	let email
	let message
	let is_loading = false

	const sendEmail = () => {
		is_loading = true
		fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/search/contact-mail', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json'
			},
			body: JSON.stringify({
				name,
				email,
				message
			})
		})
			.then((r) => r.json().then((data) => ({ status_cod: r.status, data })))
			.then((obj) => {
				is_loading = false
				if (obj.status_cod === status_code.HTTP_200_OK) {
					notificationToast(obj.data.detail, true, 3000, 'success')
				}
			})
	}
</script>

<svelte:head>
	<title>Contact</title>
</svelte:head>

{#if !$navigating}
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
						<a href="mailto:support@findcare.in" class="text-indigo-500 leading-relaxed"
							>support@findcare.in</a
						>
						<h2 class="title-font font-semibold text-gray-900 tracking-widest text-xs mt-4">
							PHONE
						</h2>
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
						bind:value={name}
						required
						type="text"
						id="name"
						name="name"
						class="w-full bg-white rounded border border-gray-300 focus:border-primary focus:ring-1 focus:ring-primary text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
					/>
				</div>
				<div class="relative mb-4">
					<label for="email" class="leading-7 text-sm text-gray-600">Email</label>
					<input
						bind:value={email}
						required
						type="email"
						id="email"
						name="email"
						class="w-full bg-white rounded border border-gray-300 focus:border-primary focus:ring-1 focus:ring-primary text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
					/>
				</div>
				<div class="relative mb-4">
					<label for="message" class="leading-7 text-sm text-gray-600">Message</label>
					<textarea
						bind:value={message}
						required
						id="message"
						name="message"
						class="w-full bg-white rounded border border-gray-300 focus:border-primary focus:ring-1 focus:ring-primary h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
					/>
				</div>
				<button
					disabled={is_loading ? true : false}
					on:click={sendEmail}
					class="text-white {is_loading
						? 'bg-[#7069f5] cursor-not-allowed'
						: 'bg-indigo-500 hover:bg-[#524af4]'}  border-0 py-2 px-6 focus:outline-none rounded text-lg"
					><i
						class={is_loading ? 'loading fa fa-spinner fa-spin relative right-2' : ''}
					/>Submit</button
				>
			</div>
		</div>
	</section>
	<Footer />
{:else}
	<Loading />
{/if}

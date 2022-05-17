<script>
	import Footer from '$lib/components/Footer.svelte'
	import Navbar from '$lib/components/Navbar.svelte'
	import Loading from '$lib/components/Loading.svelte'
	import { navigating } from '$app/stores'
</script>

{#if !$navigating}
	<div class="h-screen w-screen">
		<Navbar />
		<h1 class="text-center text-6xl my-6 text-gray-600 font-bold">Live Chat</h1>
		<div
			class="w-full justify-center items-center flex-col rounded-lg h-[75vh] overflow-hidden sm:mr-10 p-10 flex  relative"
		>
			<iframe
				width="100%"
				height="100%"
				class="absolute inset-0"
				frameborder="0"
				title="live-chat"
				marginheight="0"
				marginwidth="0"
				scrolling="no"
				loading="lazy"
				referrerpolicy="no-referrer-when-downgrade"
				src="https://tawk.to/findcare"
			/>
		</div>

		<Footer />
	</div>
{:else}
	<Loading />
{/if}

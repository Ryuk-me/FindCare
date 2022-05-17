<script>
	import { Circle } from 'svelte-loading-spinners'
	import logo_png from '$lib/assets/logo.png'
</script>

<div class="min-h-screen flex flex-col items-center justify-center relative">
	<img src={logo_png} alt="logo" class="mb-4 w-32" />
	<Circle size="2" color="rgb(239, 68, 68)" unit="rem" duration="1.5s" />
</div>

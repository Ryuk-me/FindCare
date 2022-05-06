<script context="module">
	export const prerender = true
</script>

<script>
	let email = ''
	function passwordsent() {
		alert('check your email')
	}
	async function sendResetPassword() {}
</script>

<svelte:head>
	<title>Findcare Password Recovery</title>
</svelte:head>

<div class="w-screen h-screen flex flex-col justify-center items-center ">
	<div
		class="flex flex-col justify-center items-center w-96 lg:w-[30rem] bg-white rounded drop-shadow-xl mb-8 px-8 py-7"
	>
		<div id="header" class="flex flex-col justify-center items-center">
			<div>
				<img src="lock.svg" alt="lock svg" class="w-32" />
			</div>
			<div>
				<h2 class="text-2xl font-semibold">Trouble Logging In?</h2>
			</div>
		</div>
		<hr class="h-2" />
		<div id="body" class="flex flex-col justify-center items-center">
			<div class="flex flex-col justify-center items-center">
				<p class="font-light text-sm">
					Enter your email address associated with your account and we'll send you instruction to
					get back into your account.
				</p>
			</div>
			<form class="w-full mt-3 mb-2" on:submit={passwordsent}>
				<label for="email" class="font-medium">Email</label>
				<input
					bind:value={email}
					type="email"
					id="email"
					placeholder="your@domain.com"
					class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				/>
				<button
					class="bg-primary hover:bg-[#524af4] text-white mb-3 font-bold py-2 mt-5 w-full rounded focus:outline-none focus:shadow-outline"
					on:click={sendResetPassword}>Reset Password</button
				>
			</form>
			<div>
				<p>Return to <a href="./login" class="text-primary">Login</a></p>
			</div>
		</div>
	</div>
	<p class="text-center">
		&copy;2022 <a href="./" class="text-primary">FindCare</a>. All rights reserved.
	</p>
</div>

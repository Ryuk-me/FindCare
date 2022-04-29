<script>
	var pass = false
	function showpass() {
		if (pass) {
			document.getElementById('password').setAttribute('type', 'password')
			document.getElementById('eye').classList.add('fa-eye-slash')
			document.getElementById('eye').classList.remove('fa-eye')
			pass = false
		} else {
			document.getElementById('eye').classList.remove('fa-eye-slash')
			document.getElementById('eye').classList.add('fa-eye')
			document.getElementById('password').setAttribute('type', 'text')
			pass = true
		}
	}
</script>

<img src="shape.png" alt="" class="fixed hidden lg:block w-96 bottom-0 left-0" />

<div class="w-screen h-screen flex flex-col justify-center items-center lg:grid lg:grid-cols-2 ">
	<div class="flex justify-center items-center lg:ml-14">
		<div class="">
			<h2 class="text-primary font-bold font-display text-3xl text-left">nextcare</h2>
			<form
				action=""
				class="flex flex-col justify-center items-start w-96 lg:w-[30rem] bg-white rounded drop-shadow-xl mb-8 px-8 py-7"
			>
				<h2 class="font-bold my-3 mb-9 text-xl">Sign in to your account</h2>
				<div class="relative w-full mb-4">
					<label for="email" class="">Email</label>
					<input
						type="email"
						class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
						placeholder="your@domain.com"
						autocomplete="on"
					/>
				</div>
				<div class="w-full mb-3">
					<div class="flex justify-between">
						<label for="password">Password</label>
						<a href="reset" class="text-primary cursor-pointer">Forgot Password?</a>
					</div>
					<div class="relative">
						<input
							type="password"
							placeholder="********"
							class="block border rounded py-2 pt-3 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							id="password"
							autocomplete="off"
						/>
						<span>
							<i
								class="fa fa-eye-slash hover:cursor-pointer"
								aria-hidden="true"
								id="eye"
								on:click={showpass}
							/>
						</span>
					</div>
				</div>
				<div class="flex flex-col justify-center items-center w-full my-3">
					<button
						class="bg-primary hover:bg-blue-700 text-white mb-3 font-bold py-2 px-28 rounded focus:outline-none focus:shadow-outline"
						>Login</button
					>
					<p>Don't Have An Account? <a href="./signup" class="text-primary">Sign Up</a></p>
				</div>
			</form>

			<p class="text-center">&copy;2022 NextCare. All rights reserved.</p>
		</div>
	</div>
	<div class="hidden w-full h-screen lg:flex items-end flex-col">
		<img src="medical-team.png" class="hidden lg:block max-h-full" alt="" />
	</div>
</div>

<style>
	span {
		position: absolute;
		right: 14px;
		transform: translate(0, -50%);
		top: 50%;
	}
</style>

<script>
	import doctor_png from '$lib/assets/doctor/doctor.png'
	import lower_png from '$lib/assets/doctor/lower.png'
	import upper_png from '$lib/assets/doctor/upper.png'
</script>

<svelte:head>
	<title>Findcare Register As Doctor</title>
</svelte:head>
<div class="w-full h-screen">
	<img src={doctor_png} alt="doctor.png" class="fixed hidden lg:block bottom-0 ml-7 left-0 w-40" />
	<img src={upper_png} alt="upper.png" class="fixed hidden lg:block right-0 top-0" />
	<img src={lower_png} alt="lower.png" class="fixed hidden lg:block right-0 bottom-0" />
	<div class="flex justify-center items-center h-full">
		<div class="my-2">
			<div class="text-primary font-bold font-poppins text-4xl">Findcare</div>
			<div class="flex justify-center items-center">
				<form
					action=""
					class="flex flex-col justify-center items-start w-[90vw] lg:w-[70vw] md:w-[70vw] bg-white rounded drop-shadow-xl mb-8 px-4 py-7"
				>
					<div class=" w-full">
						<div class="font-bold my-3 text-2xl">
							Register as <span class="text-primary">Doctor</span>
						</div>
						<div class="text-sm">
							Let's get you all set up so you can verify your personal account and begin setting up
							your profile
						</div>
						<div class="w-full border-t-[2px] my-4 border-[#BABABA]" />
					</div>
					<div class="">
						<div class="w-full block border-t-[2px] border-black" />
					</div>
					<div class="w-full lg:flex lg:justify-center">
						<div class="relative w-full mb-4">
							<label for="firstName">First Name</label>
							<input
								type="text"
								name="firstName"
								id="firstName"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
						<div class="relative w-full mb-4 lg:mx-4">
							<label for="lastName">Last Name</label>
							<input
								type="text"
								name="lastName"
								id="lastName"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
						<div class="relative w-full mb-4">
							<label for="registrationNumber">Registration Number</label>
							<input
								type="text"
								name="registrationNumber"
								id="registrationNumber"
								class="block appearance-none border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
					</div>
					<div class="w-full lg:flex lg:justify-center">
						<div class="relative w-full mb-4">
							<label for="phoneNumber">Phone Number</label>
							<input
								type="number"
								name="phoneNumber"
								id="phoneNumber"
								class="block appearance-none border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
						<div class="relative w-full mb-4 lg:mx-4">
							<label for="email">Email</label>
							<input
								type="email"
								name="email"
								id="email"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
						<div class="relative w-full mb-4">
							<label for="speciality">Speciality</label>
							<input
								type="text"
								name="speciality"
								id="speciality"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
					</div>
					<div class="w-full lg:flex lg:justify-center">
						<div class="relative w-full mb-4">
							<label for="dob">Date Of Birth</label>
							<input
								type="date"
								name="dob"
								id="dob"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
						<div class="relative w-full mb-4 lg:mx-4">
							<label for="gender">Gender</label>
							<div class="flex items-center pt-2 lg:pt-5">
								<div class="flex items-center mr-5">
									<input id="male" type="radio" name="gender" class="mr-2" />
									<label class="form-check-label inline-block text-gray-800" for="male" value="male"
										>Male</label
									>
								</div>
								<div class="flex items-center">
									<input id="female" type="radio" name="gender" class="mr-2" />
									<label
										class="form-check-label inline-block text-gray-800"
										for="female"
										value="female">Female</label
									>
								</div>
							</div>
						</div>
						<div class="relative w-full mb-4">
							<label for="expYear">Experience year</label>
							<input
								type="number"
								name="expYear"
								id="expYear"
								class="block appearance-none border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
					</div>
					<div class="w-full lg:flex lg:justify-center">
						<div class="relative w-full mb-4">
							<label for="password">Password</label>
							<input
								type="password"
								name="password"
								id="password"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
						<div class="relative w-full mb-4 lg:mx-4">
							<label for="confirmPassword">Confirm Password</label>
							<input
								type="password"
								name="confirmPassword"
								id="confirmPassword"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
						<div class="relative w-full mb-4">
							<label for="about">About</label>
							<input
								type="text"
								name="about"
								id="about"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							/>
						</div>
					</div>
					<div class="w-full">
						<div class="w-full">
							<button
								class="bg-primary hover:bg-[#524af4] lg:w-[16vw] text-white mb-3 font-bold py-2 w-full rounded focus:outline-none focus:shadow-outline"
								>create account</button
							>
						</div>
						<div>
							Already have an account? <a href="./login" class="text-primary">Login</a>
						</div>
					</div>
				</form>
			</div>
		</div>
	</div>
</div>

<style>
	input::-webkit-outer-spin-button,
	input::-webkit-inner-spin-button {
		-webkit-appearance: none;
		margin: 0;
	}
	img {
		-webkit-user-drag: none;
		-khtml-user-drag: none;
		-moz-user-drag: none;
		-o-user-drag: none;
		/* user-drag: none; */
	}
</style>

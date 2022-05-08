<script>
	import doctor_png from '$lib/assets/doctor/doctor.png'
	import lower_png from '$lib/assets/doctor/lower.png'
	import upper_png from '$lib/assets/doctor/upper.png'
	let show = false
</script>

<svelte:head>
	<title>Findcare Register As Doctor</title>
</svelte:head>
<div class="w-full h-full">
	<img src={doctor_png} alt="doctor.png" class="fixed hidden lg:block bottom-0 ml-7 left-0 w-40" />
	<img src={upper_png} alt="upper.png" class="fixed lg:block right-0 top-0" />
	<img src={lower_png} alt="lower.png" class="fixed hidden lg:block right-0 bottom-0" />
	<img src={lower_png} alt="lower.png" class="fixed block lg:hidden left-0 bottom-0 scale-x-[-1]" />
	<div class="flex justify-center items-center">
		<div class="my-2">
			<div class="text-primary font-bold font-poppins text-4xl mb-2 lg:pl-7">FindCare</div>
			<div class="flex justify-center items-center font-medium font-maven">
				<form
					action=""
					class="flex flex-col justify-center items-start w-[90vw] lg:w-[75vw] md:w-[70vw] bg-white lg:bg-transparent  rounded drop-shadow-xl mb-8 px-7 pb-7 pt-4 lg:border-none border border-primary"
				>
					<div class=" w-full">
						<div class="font-bold mb-3 text-2xl">
							Register as <span class="text-primary font-extrabold">Doctor</span>
						</div>
						<div class="text-sm font-normal">
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
								title="Enter Your First Name"
								placeholder="Dr. Neeraj"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
							/>
						</div>
						<div class="relative w-full mb-4 lg:mx-4">
							<label for="lastName">Last Name</label>
							<input
								type="text"
								name="lastName"
								placeholder="Kumar"
								id="lastName"
								title="Enter Your Last Name"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
							/>
						</div>
						<div class="relative w-full mb-4">
							<label for="registrationNumber">Registration Number</label>
							<input
								type="text"
								placeholder="AQ-15-XXXXX"
								name="registrationNumber"
								title="Enter Your Registration Number"
								id="registrationNumber"
								class="block appearance-none border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
							/>
						</div>
					</div>
					<div class="w-full lg:flex lg:justify-center">
						<div class="relative w-full mb-4">
							<label for="phoneNumber">Phone Number</label>
							<input
								type="number"
								placeholder="98765XXXXX"
								name="phoneNumber"
								id="phoneNumber"
								title="Enter Your Phone Number"
								class="block appearance-none border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
							/>
						</div>
						<div class="relative w-full mb-4 lg:mx-4">
							<label for="email">Email</label>
							<input
								type="email"
								placeholder="your@domain.com"
								name="email"
								id="email"
								title="Enter Your Email"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
							/>
						</div>
						<div class="relative w-full mb-4">
							<label for="speciality">Speciality</label>
							<input
								type="text"
								name="speciality"
								id="speciality"
								title="Enter Your Speciality"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
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
								title="Enter Your Date Of Birth"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
							/>
						</div>
						<div class="relative w-full mb-4 lg:mx-4">
							<label for="gender">Gender</label>
							<div class="flex items-center pt-2 lg:pt-5">
								<div class="flex items-center ">
									<input id="male" type="radio" name="gender" class="mr-2" checked />
									<label class="form-check-label inline-block text-gray-800" for="male" value="male"
										>Male</label
									>
								</div>
								<div class="flex items-center mx-5">
									<input id="female" type="radio" name="gender" class="mr-2" />
									<label
										class="form-check-label inline-block text-gray-800"
										for="female"
										value="female">Female</label
									>
								</div>
								<div class="flex items-center">
									<input id="other" type="radio" name="gender" class="mr-2" />
									<label
										class="form-check-label inline-block text-gray-800"
										for="other"
										value="other">Other</label
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
								title="Enter Your Experience Year"
								min="1"
								max="70"
								placeholder="20"
								class="block appearance-none border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
							/>
						</div>
					</div>
					<div class="w-full lg:flex lg:justify-center">
						<div class="relative w-full mb-4">
							<label for="password">Password</label>
							<div class="relative">
								<input
									type={show ? 'text' : 'password'}
									name="password"
									placeholder="***********"
									title="Enter Your Password"
									id="password"
									class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
								/>
								<span>
									<i
										class="fa {show
											? 'fa-eye-slash'
											: 'fa-eye'} hover:cursor-pointer text-slate-600"
										aria-hidden="true"
										id="eye"
										on:click|preventDefault={() => (show = !show)}
									/>
								</span>
							</div>
						</div>
						<div class="relative w-full mb-4 lg:mx-4">
							<label for="confirmPassword">Confirm Password</label>
							<input
								type="password"
								name="confirmPassword"
								placeholder="***********"
								title="Enter Your Password Again"
								id="confirmPassword"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
							/>
						</div>
						<div class="relative w-full mb-4">
							<label for="about">About</label>
							<input
								type="text"
								name="about"
								placeholder="Tell us about yourself"
								title="Enter About Yourself"
								id="about"
								class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary" required
							/>
						</div>
					</div>
					<div class="w-full">
						<div class="w-full">
							<button
								class="bg-primary hover:bg-[#524af4] lg:w-[16vw] text-white my-3 py-2 w-full rounded focus:outline-none focus:shadow-outline font-medium"
								>CREATE ACCOUNT</button
							>
						</div>
						<div>
							Already have an account? <a href="./login" class="text-primary hover:font-semibold">Login</a>
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
	#eye {
		position: absolute;
		right: 14px;
		transform: translate(0, -50%);
		top: 50%;
	}

</style>

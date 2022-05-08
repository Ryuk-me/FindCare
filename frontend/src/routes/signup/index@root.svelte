<script>
	import doctor_img from '$lib/assets/signup/doctor.png'
</script>

<svelte:head>
	<title>Signup</title>
</svelte:head>
<div class="w-screen h-screen flex flex-row font-maven">
	<div class="bg-primary h-screen lg:w-1/3 flex flex-col w-0">
		<h1 class="text-[3.5vw] mt-4 ml-[7vw] text-white font-poppins font-bold">Findcare</h1>
		<img
			src={doctor_img}
			alt="doctor.png"
			class="h-[64vh] w-10/12 relative left-[10vw] top-[6vh]"
		/>
	</div>
	<div class="lg:mt-10 lg:ml-32 lg:p-0 flex flex-col text-lg p-10">
		<h1 class="text-4xl font-bold">Register</h1>
		<p class="mt-[5vh] text-lg">
			Let's get you all set up so you can verify your personal account and begin setting up your
			profile.
		</p>
		<div class="py-6">
			<div class="w-full border-t-[2px] border-[#BABABA]" />
		</div>

		<form action="">
			<div class="flex lg:flex-row flex-col">
				<div class="flex flex-col lg:w-1/2 pr-2 w-full">
					<label for="firstName">First Name</label>
					<input
						type="text"
						name="firstName"
						class="block border rounded px-3 py-1 w-full my-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
					/>
					<label for="phoneNumber">Phone Number</label>
					<input
						type="text"
						name="phoneNumber"
						class="block border rounded px-3 py-1 w-full my-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
					/>
					<label for="dob">Date of birth</label>
					<input
						type="date"
						name="dob"
						class="block border rounded px-3 py-1 w-full my-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
					/>
					<label for="password">Password</label>
					<input
						type="password"
						placeholder="********"
						name="firstName"
						autocomplete="off"
						class="block border rounded px-3 py-1 w-full my-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
					/>
				</div>
				<div class="flex flex-col lg:w-1/2 lg:pl-5 w-full">
					<label for="lastName">Last Name</label>
					<input
						type="text"
						name="lastName"
						class="block border rounded px-3 py-1 w-full my-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
					/>
					<label for="email">Email</label>
					<input
						type="email"
						name="email"
						class="block border rounded px-3 py-1 w-full my-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
						placeholder="your@domain.com"
						autocomplete="on"
					/>
					<label for="gender">Gender</label>
					<div class="flex flex-row w-full">
						<div class="flex justify-center items-center my-1">
							<input
								type="radio"
								name="gender"
								value="male"
								class="my-5 border-0 h-4 w-4 rounded-full text-blue-600"
							/>
							<label for="male" class="mx-3">Male</label>
						</div>
						<div class="flex justify-center items-center">
							<input type="radio" name="gender" value="female" class="my-5 border-0 h-4 w-4" />
							<label for="female" class="mx-3">Female</label>
						</div>
					</div>
					<label for="confirmPassword">Confirm Password</label>
					<input
						type="password"
						placeholder="********"
						name="confirmPassword"
						autocomplete="off"
						class="block border rounded px-3 py-1 w-full my-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
					/>
				</div>
			</div>
		</form>
		<button
			class="mt-6 bg-primary hover:bg-[#524af4] lg:w-64 h-12 text-white rounded w-full lg:p-0 p-2 font-medium"
			>CREATE ACCOUNT</button
		>
		<p class="mt-4 text-center lg:text-left">
			Already have an account? <a href="/login" class="text-primary hover:font-semibold font-medium"
				>Log in</a
			>
		</p>
	</div>
</div>

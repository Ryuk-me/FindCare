<script>
	import doctor_img from '$lib/assets/signup/doctor.png'
	import { ENV, status_code, capitalize } from '$lib/utils'
	import { notificationToast } from '$lib/NotificationToast'
	import { goto } from '$app/navigation'

	let show = false
	let firstName = ''
	let lastName = ''
	let email = ''.trim()
	let password = ''
	let confirmPassword = ''
	let phoneNumber = ''
	let gender = ''
	let dob = ''.split('-')
	// $: firstName =
	const handleInput = (event) => {
		password = event.target.value
	}
	const removeAlpha = (event) => {
		const allowedRegex = /[0-9]/g
		if (!event.key.match(allowedRegex)) {
			event.preventDefault()
		}
	}

	const removeSpecialCharacters = (event) => {
		const allowedRegex = /[A-Za-z ]/g
		if (!event.key.match(allowedRegex)) {
			event.preventDefault()
		}
	}

	const signUpUser = async () => {
		if (password !== confirmPassword) {
			notificationToast('Password do not match !', false, 2000, 'error')
			return
		}
		const resp = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/user/', {
			method: 'post',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				name:
					firstName.replace(/[^A-Za-z ]/g, '').trim() +
					' ' +
					lastName.replace(/[^A-Za-z ]/g, '').trim(),
				email: email.trim(),
				phone: phoneNumber,
				gender,
				dob,
				password
			})
		})
		const data = await resp.json()
		console.log(data)
		if (resp.status === status_code.HTTP_201_CREATED) {
			const toastCallbackToLogin = () => goto('/login')
			if (data?.detail)
				notificationToast(data?.detail, false, 3000, 'success', toastCallbackToLogin)
		} else {
			if (data?.detail[0]?.msg) {
				notificationToast(
					data.detail[0].loc?.slice(1).join(', ') + ' ' + data?.detail[0]?.msg,
					false,
					3000,
					'error'
				)
			} else {
				notificationToast(data?.detail, false, 3000, 'error')
			}
		}
	}
</script>

<svelte:head>
	<title>Signup</title>
</svelte:head>
<div class="w-full lg:h-screen h-full flex flex-row font-maven">
	<div class="bg-primary h-screen lg:w-1/3 flex flex-col w-0">
		<h1 class="text-[3.5vw] mt-4 text-center text-white font-poppins font-bold">FindCare</h1>
		<img
			src={doctor_img}
			alt="doctor.png"
			class="h-[60vh] w-[26vw] relative left-[10vw] top-[6vh]"
		/>
	</div>
	<form
		on:submit|preventDefault={signUpUser}
		class="lg:mt-5 lg:ml-32 lg:p-0 flex flex-col p-5 lg:w-auto w-full"
	>
		<h1 class="text-4xl text-primary font-poppins font-bold mb-4 lg:hidden">FindCare</h1>
		<div class="border border-primary p-4 rounded lg:border-0 mb-8">
			<h1 class="lg:text-4xl text-3xl font-bold">Register</h1>
			<p class="lg:mt-[5vh] mt-[2vh] text-sm lg:text-base">
				Let's get you all set up so you can verify your personal account and begin setting up your
				profile.
			</p>
			<div class="py-6">
				<div class="w-full border-t-[2px] border-[#BABABA]" />
			</div>

			<div class="w-full lg:flex lg:justify-center">
				<div class="relative w-full mb-4">
					<label for="firstName">First Name</label>
					<input
						type="text"
						name="firstName"
						id="firstName"
						title="Enter Your First Name"
						placeholder="Neeraj"
						class="block border capitalize rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
						required
						on:keypress={removeSpecialCharacters}
						bind:value={firstName}
						autocomplete="off"
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
						class="block border rounded capitalize py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
						required
						on:keypress={removeSpecialCharacters}
						bind:value={lastName}
						autocomplete="off"
					/>
				</div>
			</div>
			<div class="w-full lg:flex lg:justify-center">
				<div class="relative w-full mb-4">
					<label for="phoneNumber">Phone Number</label>
					<input
						type="text"
						placeholder="98765XXXXX"
						name="phoneNumber"
						id="phoneNumber"
						maxlength="10"
						minlength="10"
						on:keypress={removeAlpha}
						title="Enter Your Phone Number"
						class="block appearance-none border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
						required
						bind:value={phoneNumber}
						autocomplete="off"
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
						class="block border lowercase rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
						required
						autocomplete="off"
						bind:value={email}
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
						min="1950-01-01"
						max={`${new Date().getFullYear()}-01-01`}
						title="Enter Your Date Of Birth"
						class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
						required
						autocomplete="off"
						bind:value={dob}
					/>
				</div>
				<div class="relative w-full mb-4 lg:mx-4">
					<label for="gender">Gender</label>
					<div class="flex items-center pt-2 lg:pt-5">
						<div class="flex items-center ">
							<input
								id="male"
								type="radio"
								name="gender"
								value="male"
								class="h-4 w-4 mr-2"
								required
								bind:group={gender}
								autocomplete="off"
							/>
							<label class="form-check-label inline-block text-gray-800" for="male" value="male"
								>Male</label
							>
						</div>
						<div class="flex items-center mx-5">
							<input
								id="female"
								type="radio"
								value="female"
								name="gender"
								class="h-4 w-4 mr-2"
								required
								bind:group={gender}
								autocomplete="off"
							/>
							<label class="form-check-label inline-block text-gray-800" for="female" value="female"
								>Female</label
							>
						</div>
						<div class="flex items-center">
							<input
								id="other"
								type="radio"
								name="gender"
								value="other"
								class="h-4 w-4 mr-2"
								autocomplete="off"
								required
								bind:group={gender}
							/>
							<label class="form-check-label inline-block text-gray-800" for="other" value="other"
								>Other</label
							>
						</div>
					</div>
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
							class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
							required
							on:input={handleInput}
							autocomplete="off"
						/>
						<span>
							<i
								class="fa {show
									? 'fa-eye-slash'
									: 'fa-eye'} hover:cursor-pointer text-slate-600 float-right relative bottom-7 right-3"
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
						class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
						required
						autocomplete="off"
						bind:value={confirmPassword}
					/>
				</div>
			</div>
			<button
				class="mt-2 bg-primary hover:bg-[#524af4] lg:w-64 h-12 text-white rounded w-full lg:p-0 p-2 font-medium"
				>CREATE ACCOUNT</button
			>
			<p class="mt-4 text-center lg:text-left">
				Already have an account? <a
					href="/login"
					class="text-primary hover:font-semibold font-medium">Log in</a
				>
			</p>
			<p class="mb-5 text-center lg:text-left ">
				Are You A Doctor? <a
					href="/register-doctor"
					class="text-primary hover:font-semibold font-medium">Sign Up Here</a
				>
			</p>
		</div>
	</form>
</div>

<style>
	input::-webkit-outer-spin-button,
	input::-webkit-inner-spin-button {
		-webkit-appearance: none;
		margin: 0;
	}
</style>

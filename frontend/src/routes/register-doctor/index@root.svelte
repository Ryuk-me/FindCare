<script>
	import doctor_png from '$lib/assets/doctor/doctor.png'
	import lower_png from '$lib/assets/doctor/lower.png'
	import upper_png from '$lib/assets/doctor/upper.png'
	import { titleCase, status_code, ENV, removeAlpha, removeSpecialCharacters } from '$lib/utils'
	import { notificationToast } from '$lib/NotificationToast'
	import { goto } from '$app/navigation'
	import Loading from '$lib/components/Loading.svelte'

	let show = false
	let firstName = ''
	let lastName = ''
	let email = ''
	let password = ''
	let confirmPassword = ''
	let phoneNumber = ''
	let gender = ''
	let dob = ''.split('-')
	let experienceYears = ''
	let speciality = ''
	let about = ''
	let registrationNumber = ''.toUpperCase()

	const handleInput = (event) => {
		password = event.target.value
	}

	let is_loading = false
	async function signUpDoctor() {
		is_loading = true
		// await new Promise((r) => setTimeout(r, 5000))
		if (!phoneNumber.match(/^[6-9]\d{9}$/gm)) {
			notificationToast('Invalid Phone Number !', false, 2000, 'error')
			is_loading = false
			return
		}
		if (password !== confirmPassword) {
			notificationToast('Password do not match !', false, 2000, 'error')
			is_loading = false
			return
		}
		let name = titleCase(
			firstName.replace(/[^A-Za-z .]/g, '').trim() +
				' ' +
				lastName.replace(/[^A-Za-z ]/g, '').trim()
		)
		const resp = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/doctor/', {
			method: 'post',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				name,
				email,
				phone: phoneNumber,
				password,
				gender,
				dob,
				experience_year: experienceYears,
				speciality: titleCase(speciality.trim()),
				about: about.trim(),
				registration_number: registrationNumber.toLocaleUpperCase()
			})
		})
		const data = await resp.json()
		is_loading = false
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
	<title>Findcare Register As Doctor</title>
</svelte:head>
{#if is_loading}
	<Loading />
{:else}
	<div class="w-full h-full">
		<img
			src={doctor_png}
			alt="doctor.png"
			class="fixed hidden lg:block bottom-0 ml-7 left-0 w-40"
		/>
		<img src={upper_png} alt="upper.png" class="fixed lg:block right-0 top-0" />
		<img src={lower_png} alt="lower.png" class="fixed hidden lg:block right-0 bottom-0" />
		<img
			src={lower_png}
			alt="lower.png"
			class="fixed block lg:hidden left-0 bottom-0 scale-x-[-1]"
		/>
		<div class="flex justify-center items-center">
			<div class="my-2">
				<div class="text-primary font-bold font-poppins text-4xl mb-2 lg:pl-7">FindCare</div>
				<div class="flex justify-center items-center font-medium font-maven">
					<form
						on:submit|preventDefault={signUpDoctor}
						class="flex flex-col justify-center items-start w-[90vw] lg:w-[75vw] md:w-[70vw] bg-white lg:bg-transparent  rounded drop-shadow-xl mb-8 px-7 pb-7 pt-4 lg:border-none border border-primary"
					>
						<div class=" w-full">
							<div class="font-bold mb-3 text-2xl">
								Register as <span class="text-primary font-extrabold">Doctor</span>
							</div>
							<div class="text-sm font-normal">
								Let's get you all set up so you can verify your personal account and begin setting
								up your profile
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
									class="block border capitalize rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
									required
									on:keypress={removeSpecialCharacters}
									bind:value={firstName}
									autocapitalize="on"
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
									class="block border capitalize rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
									required
									on:keypress={removeSpecialCharacters}
									bind:value={lastName}
									autocomplete="off"
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
									class="block uppercase appearance-none border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
									required
									bind:value={registrationNumber}
									autocomplete="off"
								/>
							</div>
						</div>
						<div class="w-full lg:flex lg:justify-center">
							<div class="relative w-full mb-4">
								<label for="phoneNumber">Phone Number</label>
								<input
									type="tel"
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
							<div class="relative w-full mb-4">
								<label for="speciality">Speciality</label>
								<input
									type="text"
									name="speciality"
									id="speciality"
									title="Enter Your Speciality"
									class="block border capitalize rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
									required
									autocomplete="off"
									bind:value={speciality}
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
									class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
									required
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
											class="mr-2"
											value="male"
											bind:group={gender}
											required
											autocomplete="off"
										/>
										<label
											class="form-check-label inline-block text-gray-800"
											for="male"
											value="male">Male</label
										>
									</div>
									<div class="flex items-center mx-5">
										<input
											id="female"
											type="radio"
											name="gender"
											class="mr-2"
											value="female"
											bind:group={gender}
											required
											autocomplete="off"
										/>
										<label
											class="form-check-label inline-block text-gray-800"
											for="female"
											value="female">Female</label
										>
									</div>
									<div class="flex items-center">
										<input
											id="other"
											type="radio"
											name="gender"
											class="mr-2"
											value="other"
											bind:group={gender}
											required
											autocomplete="off"
										/>
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
									class="block appearance-none border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
									required
									autocomplete="off"
									bind:value={experienceYears}
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
										class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
										required
										autocomplete="off"
										on:input={handleInput}
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
									class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
									required
									autocomplete="off"
									bind:value={confirmPassword}
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
									class="block border text rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
									required
									autocomplete="off"
									bind:value={about}
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
								Already have an account? <a href="./login" class="text-primary hover:font-semibold"
									>Login</a
								>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
{/if}

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

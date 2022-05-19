<script>
	import { titleCase, status_code, ENV, removeAlpha, removeSpecialCharacters } from '$lib/utils'
	import { notificationToast } from '$lib/NotificationToast'
	import { session } from '$app/stores'
	let firstName = ''
	let lastName = ''
	let email = ''
	let phoneNumber = ''
	let gender = ''
	let dob = ''.split('-')
	let experienceYears = ''
	let speciality = ''
	let about = ''
	let registrationNumber = ''.toUpperCase()
	let is_loading = false
	async function signUpDoctor() {
		is_loading = true
		if (!phoneNumber.match(/^[6-9]\d{9}$/gm)) {
			notificationToast('Invalid Phone Number !', false, 2000, 'error')
			is_loading = false
			return
		}
		let name = titleCase(
			firstName.replace(/[^A-Za-z .]/g, '').trim() +
				' ' +
				lastName.replace(/[^A-Za-z ]/g, '').trim()
		)
		const resp = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/admin/create/doctor', {
			method: 'post',
			headers: {
				'Content-Type': 'application/json',
				//@ts-ignore
				Authorization: `Bearer ${$session.session}`
			},
			body: JSON.stringify({
				name,
				email,
				phone: phoneNumber,
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
			if (data?.detail) notificationToast(data?.detail, false, 2000, 'success')
		} else {
			if (data?.detail[0]?.msg) {
				notificationToast(
					data.detail[0].loc?.slice(1).join(', ') + ' ' + data?.detail[0]?.msg,
					false,
					2000,
					'error'
				)
			} else {
				notificationToast(data?.detail, false, 2000, 'error')
			}
		}
	}
</script>

<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">Add Doctor</div>
<div class="form w-full">
	<div class="relative w-full mb-4">
		<label for="name" class="">First Name</label>
		<input
			type="text"
			class="block border rounded capitalize py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			placeholder="Dr. Neeraj"
			autocomplete="on"
			on:keypress={removeSpecialCharacters}
			bind:value={firstName}
			autocapitalize="on"
			required
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="name" class="">Last Name</label>
		<input
			type="text"
			class="block border rounded capitalize py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			placeholder="Kumar"
			autocomplete="on"
			on:keypress={removeSpecialCharacters}
			bind:value={lastName}
			required
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="email" class="">Email</label>
		<input
			type="email"
			class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			placeholder="your@domain.com"
			autocomplete="on"
			bind:value={email}
			required
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="phone" class="">Phone Number</label>
		<input
			type="tel"
			maxlength="10"
			minlength="10"
			on:keypress={removeAlpha}
			bind:value={phoneNumber}
			class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			placeholder="9876xxxxxx"
			autocomplete="on"
			required
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="dob" class="">Date Of Birth</label>
		<input
			type="date"
			class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			placeholder="your@domain.com"
			autocomplete="on"
			required
			bind:value={dob}
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
			autocomplete="off"
			bind:value={registrationNumber}
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
			bind:value={experienceYears}
			autocomplete="off"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="gender">Gender</label>
		<div class="flex items-center pt-2 lg:pt-5">
			<div class="flex items-center ">
				<input
					id="male"
					type="radio"
					name="gender"
					class="mr-2"
					value="male"
					required
					autocomplete="off"
					bind:group={gender}
				/>
				<label class="form-check-label inline-block text-gray-800" for="male" value="male"
					>Male</label
				>
			</div>
			<div class="flex items-center mx-5">
				<input
					id="female"
					type="radio"
					name="gender"
					class="mr-2"
					value="female"
					required
					autocomplete="off"
					bind:group={gender}
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
					class="mr-2"
					value="other"
					required
					autocomplete="off"
					bind:group={gender}
				/>
				<label class="form-check-label inline-block text-gray-800" for="other" value="other"
					>Other</label
				>
			</div>
		</div>
	</div>
	<div class="relative w-full mb-4">
		<label for="about">About</label>
		<textarea
			type="textarea"
			rows="3"
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
	<div class="relative w-full mb-4" />
	<button
		on:click={signUpDoctor}
		disabled={is_loading ? true : false}
		class="{is_loading
			? 'bg-[#7069f5] cursor-not-allowed'
			: 'bg-primary hover:bg-[#524af4]'}  tracking-wider text-lg w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
		><i class={is_loading ? 'loading fa fa-spinner fa-spin relative right-2' : ''} />Add Doctor</button
	>
</div>

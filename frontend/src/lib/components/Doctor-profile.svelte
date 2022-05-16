<script>
	import { session } from '$app/stores'
	import { ENV, status_code } from '$lib/utils'
	import { notificationToast } from '$lib/NotificationToast'
	export let response
	export let doctor_profile
	let doctor = null
	if (response) doctor = response.doctor
	else doctor = doctor_profile
	let email = doctor.email
	let phone = doctor.phone
	let about = doctor.about
	let profile_image = doctor.profile_image
	let isSomethingChanged = false
	$: if (!(doctor.email === email) || !(doctor.phone === phone) || !(doctor.about === about))
		isSomethingChanged = true
	else isSomethingChanged = false
	let is_loading = false
	async function updateDoctorProfile() {
		is_loading = true
		const res = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/doctor/', {
			method: 'PUT',
			headers: {
				'Content-type': 'application/json',
				//@ts-ignore
				Authorization: `Bearer ${$session.session}`
			},
			body: JSON.stringify({
				email,
				phone,
				about,
				profile_image
			})
		})
		const data = await res.json()
		is_loading = false
		if (res.status === status_code.HTTP_202_ACCEPTED) {
			notificationToast('Profile Updated Successfully', false, 2000, 'success')
			email = data.email
			phone = data.phone
			about = data.about
			profile_image = data.profile_image
			isSomethingChanged = false
		} else if (res.status === status_code.HTTP_304_NOT_MODIFIED) {
			notificationToast('Not Modified', false, 2000, 'error')
		} else notificationToast(data?.detail, false, 2000, 'error')
	}

	// PROFILE IMAGE UPLOAD
	let fileinput
	const onFileSelected = (e) => {
		let image = e.target.files[0]
		let reader = new FileReader()
		reader.readAsDataURL(image)
		reader.onload = (e) => {
			profile_image = e.target.result
		}
	}
	$: if (profile_image !== doctor.profile_image) {
		let stringLength = profile_image.length - 'data:image/png;base64,'.length

		let sizeInBytes = 4 * Math.ceil(stringLength / 3) * 0.5624896334383812
		let sizeInKb = sizeInBytes / 1000
		if (sizeInKb < 500) {
			fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/doctor/', {
				method: 'PUT',
				headers: {
					'Content-type': 'application/json',
					//@ts-ignore
					Authorization: `Bearer ${$session.session}`
				},
				body: JSON.stringify({
					profile_image
				})
			})
				.then((res) => {
					if (res.status === status_code.HTTP_202_ACCEPTED) {
						notificationToast('Profile Image Updated', false, 2000, 'success')
					}
				})
				.catch((error) => {})
		} else {
			notificationToast('Image size must be less than 500kb', false, 2000, 'error')
			profile_image = doctor.profile_image
		}
	}
</script>

<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">Edit Profile</div>
<div class="form w-full">
	<div class="relative w-full mb-4">
		<div class="navigation px-6 mb-4 lg:mb-0 rounded-lg lg:mr-6">
			<div class="photo flex justify-center flex-col lg:flex-row items-center py-4">
				<img class="object-cover w-28 h-28 m-6 rounded-full" src={profile_image} alt="" />
				<!-- <button
						class="bg-primary hover:bg-[#524af4] text-white rounded-md w-full px-7 py-1 font-medium"
						>Change Profile Photo</button
					> -->
				<input
					type="file"
					accept=".jpg, .jpeg, .png"
					on:change={(e) => onFileSelected(e)}
					bind:this={fileinput}
					class="block w-full center text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-primary file:text-white hover:file:bg-[#524af4]"
				/>
			</div>
		</div>
	</div>
	<div class="relative w-full mb-4">
		<label for="name" class="">Name</label>
		<input
			disabled
			bind:value={doctor.name}
			type="text"
			class="block border rounded py-2 text-gray-400 cursor-not-allowed px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			placeholder="your@domain.com"
			autocomplete="on"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="email" class="">Email</label>
		<input
			bind:value={email}
			type="email"
			class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			placeholder="your@domain.com"
			autocomplete="on"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="phone" class="">Phone Number</label>
		<input
			bind:value={phone}
			type="number"
			class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			placeholder="your@domain.com"
			autocomplete="on"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="dob" class="">Date Of Birth</label>
		<input
			disabled
			bind:value={doctor.dob}
			type="date"
			class="block border rounded py-2 px-3 text-gray-500 cursor-not-allowed w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			placeholder={doctor.dob}
			autocomplete="on"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="age" class="">Age</label>
		<input
			disabled
			bind:value={doctor.age}
			type="text"
			class="block border rounded py-2 text-gray-400 cursor-not-allowed px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			autocomplete="on"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="registrationNumber">Registration Number</label>
		<input
			type="text"
			disabled
			bind:value={doctor.registration_number}
			name="registrationNumber"
			title="Enter Your Registration Number"
			id="registrationNumber"
			class="block uppercase appearance-none text-gray-500 cursor-not-allowed border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			autocomplete="off"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="speciality">Speciality</label>
		<input
			disabled
			type="text"
			name="speciality"
			id="speciality"
			bind:value={doctor.speciality}
			class="block border capitalize rounded py-2 text-gray-500 cursor-not-allowed px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			required
			autocomplete="off"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="expYear">Experience year</label>
		<input
			disabled
			type="number"
			name="expYear"
			id="expYear"
			title="Enter Your Experience Year"
			min="1"
			max="70"
			placeholder="20"
			bind:value={doctor.experience_year}
			class="block appearance-none border text-gray-500 cursor-not-allowed rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			required
			autocomplete="off"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="gender">Gender</label>
		<input
			type="text"
			bind:value={doctor.gender}
			disabled
			class="block appearance-none capitalize text-gray-500 cursor-not-allowed border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			autocomplete="off"
		/>
	</div>

	<div class="relative w-full mb-4">
		<label for="about">About</label>
		<textarea
			type="textarea"
			rows="3"
			name="about"
			bind:value={about}
			id="about"
			class="block border text rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			required
			autocomplete="off"
		/>
	</div>
	<div class="relative w-full mb-4" />
	{#if isSomethingChanged}
		{#if !is_loading}
			<button
				on:click={updateDoctorProfile}
				class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
				>Save Changes</button
			>
		{:else}
			<button
				disabled
				on:click={updateDoctorProfile}
				class="bg-[#7069f5] tracking-wider text-lg cursor-not-allowed w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
				><i class="loading fa fa-spinner fa-spin relative right-2" />Save Changes</button
			>
		{/if}
	{:else}
		<button
			disabled
			class="bg-[#7069f5] cursor-not-allowed tracking-wider text-lg w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
			>Save Changes</button
		>
	{/if}
</div>

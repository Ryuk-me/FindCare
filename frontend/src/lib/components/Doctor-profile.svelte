<script>
	export let response
	export let doctor_profile
	let doctor = null
	if (response) doctor = response.doctor
	else doctor = doctor_profile
</script>

<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">Edit Profile</div>
<div class="form w-full">
	<div class="relative w-full mb-4">
		<div class="navigation px-6 mb-4 lg:mb-0 rounded-lg lg:mr-6">
			<div class="photo flex justify-center flex-col lg:flex-row items-center py-4">
				<img class="object-cover w-28 h-28 m-6 rounded-full" src={doctor.profile_image} alt="" />
				<!-- <button
						class="bg-primary hover:bg-[#524af4] text-white rounded-md w-full px-7 py-1 font-medium"
						>Change Profile Photo</button
					> -->
				<input
					type="file"
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
			bind:value={doctor.email}
			type="email"
			class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			placeholder="your@domain.com"
			autocomplete="on"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="phone" class="">Phone Number</label>
		<input
			bind:value={doctor.phone}
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
			type="number"
			name="expYear"
			id="expYear"
			title="Enter Your Experience Year"
			min="1"
			max="70"
			placeholder="20"
			bind:value={doctor.experience_year}
			class="block appearance-none border  rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
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
			bind:value={doctor.about}
			id="about"
			class="block border text rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			required
			autocomplete="off"
		/>
	</div>
	<div class="relative w-full mb-4" />
	<button
		class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
		>Save Changes</button
	>
</div>

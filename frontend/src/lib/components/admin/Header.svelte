<script>
	import CardStats from '$lib/components/cardStats.svelte'
	export let clinics
	let totalClinics = 0
	let total_patients = 0
	let total_appointments = 0
	let completed_appointments = 0
	let pending_appointments = 0
	let cancelled_appointments_by_user = 0
	let cancelled_appointments_by_doctor = 0
	for (let index = 0; index < clinics.length; index++) {
		const element = clinics[index]
		totalClinics += index
		total_patients += element.total_patients
		completed_appointments += element.completed_appointments
		pending_appointments += element.pending_appointments
		total_appointments += element.total_appointments
		cancelled_appointments_by_user += element.cancelled_appointments_by_user
		cancelled_appointments_by_doctor += element.cancelled_appointments_by_doctor
	}
</script>

<!-- Header -->
<div class="relative bg-red-500 md:pt-28 pb-12 pt-12">
	<div class="px-4 md:px-10 mx-auto w-full">
		<div>
			<!-- Card stats -->
			<div class="flex flex-wrap">
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Total Clinic/Doctor"
						statTitle={totalClinics.toLocaleString()}
						statIconName="fas fa-house-medical"
						statIconColor="bg-red-500"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Total Patients"
						statTitle={total_patients.toLocaleString()}
						statIconName="fas fa-users"
						statIconColor="bg-pink-500"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Total Appointments"
						statTitle={total_appointments.toLocaleString()}
						statIconName="fas fa-calendar-plus"
						statIconColor="bg-emerald-500"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Completed Appointments"
						statTitle={completed_appointments.toLocaleString()}
						statIconName="fa-solid fa-calendar-check"
						statIconColor="bg-orange-500"
					/>
				</div>

				<div class="w-full lg:w-6/12 xl:w-3/12 px-4 sm:mt-4">
					<CardStats
						statSubtitle="Pending Appointments"
						statTitle={pending_appointments.toLocaleString()}
						statIconName="fa-solid fa-clock-rotate-left"
						statIconColor="bg-[#F29339]"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4 sm:mt-4">
					<CardStats
						statSubtitle="Cancelled Appointments"
						statTitle={(
							cancelled_appointments_by_user + cancelled_appointments_by_doctor
						).toLocaleString()}
						statIconName="fa-solid fa-xmark"
						statIconColor="bg-[#D9512C]"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4 sm:mt-4">
					<CardStats
						statSubtitle="Cancelled Appointments By Doctor"
						statTitle={cancelled_appointments_by_doctor.toLocaleString()}
						statIconName="fa-solid fa-xmark"
						statIconColor="bg-[#D9512C]"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4 sm:mt-4">
					<CardStats
						statSubtitle="Cancelled Appointments By User"
						statTitle={cancelled_appointments_by_user.toLocaleString()}
						statIconName="fa-solid fa-xmark"
						statIconColor="bg-[#D9512C]"
					/>
				</div>
			</div>
		</div>
	</div>
</div>

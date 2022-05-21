<script>
	import CardStats from '$lib/components/cardStats.svelte'
	export let response
</script>

<!-- Header -->
<div class="relative bg-red-500 md:pt-28 pb-12 pt-12">
	<div class="px-4 md:px-10 mx-auto w-full">
		<div>
			<!-- Card stats -->
			<div class="flex flex-wrap">
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Total Appointments"
						statTitle={response ? response.total_appointments.toLocaleString() : 0}
						statIconName="far fa-chart-bar"
						statIconColor="bg-red-500"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Completed Appointments"
						statTitle={response ? response.completed_appointments.toLocaleString() : 0}
						statIconName="fa-solid fa-calendar-check"
						statIconColor="bg-orange-500"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Pending Appointments"
						statTitle={response ? response.pending_appointments.toLocaleString() : 0}
						statIconName="fa-solid fa-clock-rotate-left"
						statIconColor="bg-[#F29339]"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Today's Appointment"
						statTitle={response ? response.today_appointments.toLocaleString() : 0}
						statIconName="fas fa-calendar-plus"
						statIconColor="bg-emerald-500"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4 sm:mt-4">
					<CardStats
						statSubtitle="Total Patient"
						statTitle={response ? response.total_patients.toLocaleString() : 0}
						statIconName="fas fa-users"
						statIconColor="bg-pink-500"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4 sm:mt-4">
					<CardStats
						statSubtitle="Appointments Cancelled By User"
						statTitle={response ? response.cancelled_appointments_by_user.toLocaleString() : 0}
						statIconName="fa-solid fa-xmark"
						statIconColor="bg-[#D9512C]"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4 sm:mt-4">
					<CardStats
						statSubtitle="Appointments Cancelled By You"
						statTitle={response ? response.cancelled_appointments_by_doctor.toLocaleString() : 0}
						statIconName="fa-solid fa-xmark"
						statIconColor="bg-[#D9512C]"
					/>
				</div>
			</div>
		</div>
	</div>
</div>

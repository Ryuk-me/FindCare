<script>
	import CardStats from '$lib/components/cardStats.svelte'
</script>

<!-- Header -->
<div class="relative bg-red-500 md:pt-28 pb-12 pt-12">
	<div class="px-4 md:px-10 mx-auto w-full">
		<div>
			<!-- Card stats -->
			<div class="flex flex-wrap">
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Total Clinics"
						statTitle="350"
						statIconName="fas fa-house-medical"
						statIconColor="bg-red-500"
					/>
				</div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Total Doctors"
						statTitle="2,356"
						statIconName="fas fa-user-doctor"
						statIconColor="bg-orange-500"
					/>
				</div>
                <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
                    <CardStats
                        statSubtitle="Total Appointments"
                        statTitle="2433"
                        statIconName="fas fa-calendar-plus"
                        statIconColor="bg-emerald-500"
                    />
                </div>
				<div class="w-full lg:w-6/12 xl:w-3/12 px-4">
					<CardStats
						statSubtitle="Total Patients"
						statTitle="244"
						statIconName="fas fa-users"
						statIconColor="bg-pink-500"
					/>
				</div>
			</div>
		</div>
	</div>
</div>

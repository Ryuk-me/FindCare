<script>
	// core components
	import UserTableStats from '$lib/components/admin/UserTableStats.svelte';
import AppointmentTableStats from './AppointmentTableStats.svelte';
	// can be one of light or dark
	export let color = 'light'
</script>

<div
	class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded {color === 'light'
		? 'bg-white'
		: 'bg-red-800 text-white'}"
>
	<div class="rounded-t mb-0 px-4 py-3 border-0">
		<div class="flex flex-wrap items-center">
			<div class="relative w-full px-4 max-w-full flex-grow flex-1">
				<h3 class="font-semibold text-lg {color === 'light' ? 'text-blueGray-700' : 'text-white'}">
					Appointments Details
				</h3>
			</div>
		</div>
	</div>
	<div class="block w-full overflow-x-auto">
		<!-- Projects table -->
		<table class="items-center w-full bg-transparent border-collapse">
			<thead>
				<tr>
					<th
						class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left {color ===
						'light'
							? 'bg-blueGray-50 text-blueGray-500 border-blueGray-100'
							: 'bg-red-700 text-red-200 border-red-600'}"
					>
						Doctor's Name
					</th>
					<th
						class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left {color ===
						'light'
							? 'bg-blueGray-50 text-blueGray-500 border-blueGray-100'
							: 'bg-red-700 text-red-200 border-red-600'}"
					>
						Date Of Appointment
					</th>
					<th
						class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left {color ===
						'light'
							? 'bg-blueGray-50 text-blueGray-500 border-blueGray-100'
							: 'bg-red-700 text-red-200 border-red-600'}"
					>
						Status
					</th>
					
					<th
						class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left {color ===
						'light'
							? 'bg-blueGray-50 text-blueGray-500 border-blueGray-100'
							: 'bg-red-700 text-red-200 border-red-600'}"
					>
						Clinic Address
					</th>
				</tr>
			</thead>
			<tbody>
				<AppointmentTableStats />
				<AppointmentTableStats doctorName="Nitin Shivam" dateOfAppointment="22-05-2022" status="cancelled" clinicAddress="Boring Road, Patna" />
				<AppointmentTableStats doctorName="Amardeep" dateOfAppointment="12-04-2022" status="completed" clinicAddress="Gandhi Maidan, Patna" />
				
			</tbody>
		</table>
	</div>
</div>

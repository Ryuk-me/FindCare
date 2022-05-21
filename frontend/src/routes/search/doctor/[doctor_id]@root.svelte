<script context="module">
	import { capitalize, ENV, getFormattedDate, status_code, month_name } from '$lib/utils'
	export async function load({ params, fetch, session }) {
		const slug = params.doctor_id
		const resp = await fetch(
			ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/search/doctors/profile?slug=' + slug,
			{
				method: 'GET',
				headers: {
					'Content-type': 'application/json'
				}
			}
		)

		const data = await resp.json()
		if (resp.status !== status_code.HTTP_200_OK) {
			return {
				status: 302,
				redirect: '/error404'
			}
		}
		const appoint_details = await fetch(
			ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/search/slots?clinic_id=' + data.id
		)
		let slots = null
		if (appoint_details.ok) {
			slots = await appoint_details.json()
		}
		return {
			props: {
				status: resp.status,
				clinic: data,
				slots,
				session
			}
		}
	}
</script>

<script>
	import Navbar from '$lib/components/Navbar.svelte'
	import verified_img from '$lib/assets/book/correct.png'
	import { navigating } from '$app/stores'
	import Loading from '$lib/components/Loading.svelte'
	import { goto } from '$app/navigation'
	import { notificationToast } from '$lib/NotificationToast'
	export let clinic
	export let status
	export let slots
	export let session
	let session_time = parseInt(clinic.session_time)
	let opens_at = clinic.opens_at.slice(0, 5)
	let closes_at = clinic.closes_at.slice(0, 5)
	let date_today = getFormattedDate(null, true)
	let booked_timings
	let morningSlots = []
	let afternoonSlots = []
	let eveningSlots = []
	let slot_time = []
	let selected = null
	function get_am_pm_from_time(time) {
		let new_time = parseInt(time.slice(0, 2))
		let last_two = time.slice(2, 5)
		if (new_time > 12) {
			time = new_time - 12 + last_two + ' pm'
		} else if (new_time == 12) {
			time = new_time + time.slice(2, 5) + 'pm'
		} else {
			time = time + ' am'
		}
		return time
	}

	function incrementDate(dateInput, increment) {
		var dateFormatTotime = new Date(dateInput)
		var increasedDate = new Date(dateFormatTotime.getTime() + increment * 86400000)
		return getFormattedDate(increasedDate, false)
	}

	function get_day_and_month_name(date_today) {
		date_today = date_today.split('-')
		let date = date_today.at(-1)
		let month = parseInt(date_today.at(-2))
		let name_of_month = month_name[month]
		return date + ' ' + name_of_month
	}

	function addMinutesSlot(time, minsToAdd) {
		function D(J) {
			return (J < 10 ? '0' : '') + J
		}
		var piece = time.split(':')
		var mins = piece[0] * 60 + +piece[1] + +minsToAdd
		let addedtime = D(((mins % (24 * 60)) / 60) | 0) + ':' + D(mins % 60)
		if (addedtime < closes_at) {
			slot_time.push(addedtime)
			addMinutesSlot(addedtime, session_time)
		}
	}
	addMinutesSlot(opens_at, 0)
	if (slots) {
		for (let index = 0; index < slots.length; index++) {
			const element = slots[index]
			if (Object.keys(element)[0] == date_today) {
				let booked_slot
				booked_slot = element[Object.keys(element)[0]].length
				booked_timings = element[Object.keys(element)[0]]
				clinic.slots = clinic.slots >= 1 ? clinic.slots - booked_slot : clinic.slots
			}
		}
		for (let index = 0; index < slot_time.length; index++) {
			const time = parseInt(slot_time[index].slice(0, 2))
			if (time < 12) morningSlots.push(slot_time[index])
			if (time >= 12 && time < 17) afternoonSlots.push(slot_time[index])
			if (time > 17) eveningSlots.push(slot_time[index])
		}
	}
	function am_pm_to_full_hour(selected_time) {
		let splitted = selected_time.split(' ')
		let minutes = splitted.at(0).split(':').at(-1)
		let hour = parseInt(splitted.at(0).split(':').at(0))
		let am_or_pm = splitted.at(-1)
		if (am_or_pm === 'pm') {
			hour += 12
		}
		return hour.toLocaleString() + ':' + minutes
	}
	let doctor = clinic.doctor
	let searchQuery
	async function submitSearch(event) {
		if (event.key === 'Enter') {
			if (searchQuery) {
				goto('/search/' + searchQuery)
			}
		}
	}
	let is_loading = false
	const bookAppointment = () => {
		is_loading = true
		if (!session) {
			is_loading = false
			notificationToast('Please login to book appointment', false, 3000, 'error', goto('/login'))
			return
		}
		if (session.status !== 'user') {
			is_loading = false
			notificationToast(
				'Only users can book appointment you are a ' + session.status,
				false,
				3000,
				'error'
			)
			return
		}
		let slot_time = am_pm_to_full_hour(selected)
		let appointment_schedule = date_today + ' ' + slot_time
		const toastCallBackToreload = () => location.reload()
		fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/user/appointment/', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
				Authorization: `Bearer ${session.session}`
			},
			body: JSON.stringify({
				clinic_id: clinic.id,
				schedule: appointment_schedule,
				fees_paid: false
			})
		})
			.then((r) => r.json().then((data) => ({ status_cod: r.status, data })))
			.then((obj) => {
				if (obj.status_cod === status_code.HTTP_201_CREATED) {
					is_loading = false
					notificationToast(
						'Appointment Booked Successfully',
						true,
						2000,
						'success',
						toastCallBackToreload
					)
				} else {
					notificationToast(obj.data.detail, false, 2000, 'error', toastCallBackToreload)
				}
			})
	}
</script>

<svelte:head>
	<title>{doctor.name}</title>
</svelte:head>
{#if !$navigating}
	<div class="h-screen w-screen flex flex-col overflow-x-hidden">
		<div class="w-screen">
			<Navbar />
		</div>

		<div class="w-full lg:px-24 px-4 ">
			<input
				type="text"
				class="w-full rounded-full px-6 py-3 mt-8 drop-shadow-md focus:outline-none border border-primary"
				placeholder="Search Doctor or Symptoms..."
				bind:value={searchQuery}
				on:keydown={submitSearch}
			/>
		</div>

		<div class="h-full w-full flex lg:flex-row flex-col justify-between lg:px-24 mt-8">
			<!-- left div -->
			<div class="lg:w-[65%] flex flex-col mx-4 lg:mx-0">
				<!-- first card  -->
				<div class="w-full flex bg-white rounded-xl drop-shadow-md p-8 mb-8">
					<!-- img div -->
					<img src={doctor.profile_image} alt="doctor.png" class="rounded-[50%] h-32 mr-8" />
					<!-- info div -->
					<div>
						<h1 class="font-bold text-2xl">{doctor.name}</h1>
						<p>{doctor.speciality}</p>
						<p>
							{doctor.experience_year}
							{doctor.experience_year > 1 ? 'years' : 'year'} experience
						</p>
						<div class="flex mt-2">
							<img src={verified_img} alt="verified.png" class="mr-2" />
							Verified
						</div>
						<p class="lg:block hidden">
							{doctor.about.trim()}
						</p>
					</div>
				</div>

				<!-- second card  -->
				<div class="w-full lg:flex bg-white rounded-xl drop-shadow-md p-8 hidden">
					<div class="w-full flex flex-col">
						<p class="capitalize">{clinic.address.address}</p>
						<div class="flex w-full justify-between mt-4">
							<div class="w-40">
								<p class="text-primary font-bold">{clinic.name}</p>
							</div>
							<div>
								<p>Mon-Sun</p>
								<p>{get_am_pm_from_time(opens_at)} to {get_am_pm_from_time(closes_at)}</p>
							</div>
							<div>
								<p>Rs {clinic.fees}</p>
							</div>
						</div>
						<div class="flex w-full justify-between mt-4">
							<div class="w-40">
								<p>
									{capitalize(clinic.address.city) + ', ' + capitalize(clinic.address.state)} ({clinic
										.address.pincode})
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- right div  -->
			<div class="lg:w-[30%] flex flex-col mx-4 lg:mx-0">
				<div class="w-full flex flex-col bg-white rounded-xl drop-shadow-md p-8">
					<div class="flex">
						<div class="line-none flex overflow-auto whitespace-nowrap p-2">
							<button
								class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary"
							>
								<p class="text-primary text-sm font-semibold">
									{get_day_and_month_name(date_today)}
								</p>
								<p class="text-green-500 text-sm text-center">
									{clinic.slots > 1 ? clinic.slots + ' slots' : clinic.slots + ' slot'}
								</p>
							</button>
						</div>
					</div>
				</div>
				<div class="w-full flex flex-col bg-white rounded-xl drop-shadow-md p-1 py-6 mt-8">
					{#if morningSlots.length > 1}
						<p class="pb-4 ml-6 font-bold">Morning</p>
						<div class="flex flex-wrap gap-2 w-auto justify-center">
							{#each morningSlots as slot}
								<button
									disabled={booked_timings && booked_timings.includes(slot) ? true : false}
									class:select={selected === get_am_pm_from_time(slot)}
									on:click={() => (selected = get_am_pm_from_time(slot))}
									class="text-center rounded border-2 border-solid text-primary uppercase p-2 text-sm {booked_timings &&
									booked_timings.includes(slot)
										? 'bg-red-900 cursor-not-allowed border-red-900'
										: 'border-primary'}"
								>
									<span class={booked_timings && booked_timings.includes(slot) ? 'text-white' : ''}
										>{get_am_pm_from_time(slot)}</span
									>
								</button>
							{/each}
						</div>
					{/if}
					{#if afternoonSlots.length > 1}
						<p class="pb-4 ml-6 font-bold">Afternoon</p>
						<div class="flex flex-wrap gap-2 w-auto justify-center">
							{#each afternoonSlots as slot}
								<button
									disabled={booked_timings && booked_timings.includes(slot) ? true : false}
									class:select={selected === get_am_pm_from_time(slot)}
									on:click={() => (selected = get_am_pm_from_time(slot))}
									class="text-center rounded border-2 border-solid text-primary uppercase p-2 text-sm {booked_timings &&
									booked_timings.includes(slot)
										? 'bg-red-900 cursor-not-allowed border-red-900'
										: 'border-primary'}"
								>
									<span class={booked_timings && booked_timings.includes(slot) ? 'text-white' : ''}
										>{get_am_pm_from_time(slot)}</span
									>
								</button>
							{/each}
						</div>
					{/if}
					{#if eveningSlots.length > 0}
						<p class="pb-4 ml-6 font-bold">Evening</p>
						<div class="flex flex-wrap gap-2 w-auto justify-center">
							{#each eveningSlots as slot}
								<button
									disabled={booked_timings && booked_timings.includes(slot) ? true : false}
									class:select={selected === get_am_pm_from_time(slot)}
									on:click={() => (selected = get_am_pm_from_time(slot))}
									class="text-center rounded border-2 border-solid text-primary uppercase p-2 text-sm {booked_timings &&
									booked_timings.includes(slot)
										? 'bg-red-900 cursor-not-allowed border-red-900'
										: 'border-primary'}"
								>
									<span class={booked_timings && booked_timings.includes(slot) ? 'text-white' : ''}
										>{get_am_pm_from_time(slot)}</span
									>
								</button>
							{/each}
						</div>
					{/if}
				</div>
				<div class="w-full flex justify-center items-center py-6">
					<button
						disabled={selected ? false : true}
						on:click={bookAppointment}
						class="w-full {selected
							? 'bg-primary hover:bg-[#524af4]'
							: 'bg-[#7069f5] cursor-not-allowed'}  py-4 rounded text-white"
						><i class="{is_loading ? 'loading fa fa-spinner fa-spin' : ''}  mr-2" />Book Appointment</button
					>
				</div>
			</div>
		</div>
	</div>
{:else}
	<Loading />
{/if}

<style>
	.select {
		background-color: #524af4;
		color: white;
	}
</style>

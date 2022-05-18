<script context="module">
	import { capitalize, ENV, status_code } from '$lib/utils'
	export async function load({ params, fetch, session }) {
		const speciality = params.speciality
		const resp = await fetch(
			ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/search/doctors?speciality=' + speciality,
			{
				method: 'GET',
				headers: {
					'Content-type': 'application/json'
				}
			}
		)
		if (resp.status !== status_code.HTTP_200_OK) {
			return {
				status: 302,
				redirect: '/error404'
			}
		}
		const data = await resp.json()
		return {
			props: {
				status: resp.status,
				doctors: data,
				speciality
			}
		}
	}
</script>

<script>
	import Navbar from '$lib/components/Navbar.svelte'
	import Card from '$lib/components/doctor-card.svelte'
	import { navigating } from '$app/stores'
	import Loading from '$lib/components/Loading.svelte'
	export let speciality
	export let status
	export let doctors
	let searchQuery
	let genderFilter
	let filteredDoctorList = []
	$: if (genderFilter && genderFilter !== 'anyone') {
		filteredDoctorList = doctors.filter(
			(data) => data.doctor.gender.toLowerCase() == genderFilter.toLowerCase()
		)
	} else {
		filteredDoctorList = [...doctors]
	}
	async function submitSearch(event) {
		if (event.key === 'Enter') {
			if (searchQuery) {
				const res = await fetch(
					ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/search/doctors?speciality=' + searchQuery,
					{
						method: 'GET',
						headers: {
							'Content-type': 'application/json'
						}
					}
				)
				const data = await res.json()
				if (res.status === status_code.HTTP_200_OK) {
					status = res.status
					speciality = capitalize(searchQuery)
					filteredDoctorList = [...data]
				} else {
					status = res.status
					filteredDoctorList = []
				}
			}
		}
	}
</script>

<svelte:head>
	<title>{capitalize(speciality)}</title>
</svelte:head>

{#if !$navigating}
	<div class="h-screen w-screen flex flex-col overflow-x-hidden">
		<div class="w-screen">
			<Navbar />
		</div>

		<div class="w-full lg:px-24 px-4">
			<input
				type="text"
				bind:value={searchQuery}
				on:keydown={submitSearch}
				class="w-full rounded-full px-8 py-3 mt-8 drop-shadow-md focus:outline-none border border-primary"
				placeholder="lorem ipsum"
				autocomplete="on"
			/>
		</div>
		{#if status === status_code.HTTP_200_OK}
			<div class="flex w-full font-semibold text-2xl py-8 lg:px-24 px-4">
				<p>{doctors.length} {doctors.length > 1 ? 'doctors' : 'doctor'} availiable in Patna</p>
			</div>
		{/if}
		<div class="w-full flex">
			<!-- lg:px-20 -->
			<div class="lg:flex flex-col lg:w-80 p-4 hidden ml-20">
				<div class="flex flex-col bg-white h-64 rounded-xl drop-shadow-md p-4 ">
					<div class="flex justify-between">
						<p class="font-bold">Filter</p>
						<button class="text-blue-700 font-bold">clear all</button>
					</div>
					<div class="flex flex-col mt-6">
						<p>Availiability</p>
						<div class="mt-4">
							<input type="radio" name="avail" id="today" value="today" class="mr-2" checked />
							<label for="today">Today</label>
						</div>
						<div class="mt-4">
							<input type="radio" name="avail" id="tomorrow" value="tomorrow" class="mr-2" />
							<label for="tomorrow">Tomorrow</label>
						</div>
						<div class="mt-4">
							<input type="radio" name="avail" id="next7days" value="next7days" class="mr-2" />
							<label for="next7days">Next 7 Days</label>
						</div>
					</div>
				</div>
				<div class="flex flex-col bg-white h-64 rounded-xl drop-shadow-md p-4 mt-12">
					<div class="flex justify-between">
						<p class="font-bold">Gender</p>
						<button class="text-blue-700 font-bold">clear all</button>
					</div>
					<div class="flex flex-col mt-6">
						<div class="mt-4">
							<input
								type="radio"
								name="gender"
								id="anyone"
								value="anyone"
								class="mr-2"
								checked
								bind:group={genderFilter}
							/>
							<label for="anyone">Any one</label>
						</div>
						<div class="mt-4">
							<input
								type="radio"
								name="gender"
								id="male"
								value="male"
								class="mr-2"
								bind:group={genderFilter}
							/>
							<label for="male">Male</label>
						</div>
						<div class="mt-4">
							<input
								type="radio"
								name="gender"
								id="female"
								value="female"
								class="mr-2"
								bind:group={genderFilter}
							/>
							<label for="female">Female</label>
						</div>
					</div>
				</div>
			</div>
			{#if status === status_code.HTTP_200_OK}
				<div class="w-full flex flex-wrap justify-between lg:mx-24 mx-4">
					{#each filteredDoctorList as doctor}
						<Card
							name={doctor.doctor.name}
							address={doctor.address}
							experience={doctor.doctor.experience_year}
							fees={doctor.fees}
							speciality={doctor.doctor.speciality}
							slug={doctor.doctor.slug}
							profile_img={doctor.doctor.profile_image}
						/>
					{/each}
				</div>
			{:else}
				<div class="flex w-full justify-center ">
					<p class="sm:mt-60 mt-32 text-3xl sm:text-6xl text-center font-bold">No result found</p>
				</div>
			{/if}
		</div>
	</div>
{:else}
	<Loading />
{/if}

<script context="module">
	import { capitalize, ENV, status_code } from '$lib/utils'
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
		return {
			props: {
				status: resp.status,
				clinic: data
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
import Footer from '$lib/components/Footer.svelte'
	export let clinic
	export let status
	let doctor = clinic.doctor
	let searchQuery
	async function submitSearch(event) {
		if (event.key === 'Enter') {
			if (searchQuery) {
				goto('/search/' + searchQuery)
			}
		}
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
					<img src={doctor.profile_image} alt="doctor.png" class="rounded-[50%] h-32 mr-8"/>
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
								<p>Mon-Sat</p>
								<p>9:00 am to 6:00 pm</p>
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
							<div>
								<p>Mon-Sat</p>
								<p>9:00 am to 6:00 pm</p>
							</div>
							<div>
								<p>Rs {clinic.fees}</p>
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
								<p class="text-primary text-sm font-semibold">13 May</p>
								<p class="text-green-500 text-sm text-center">15 Slots</p>
							</button>
							<button
								class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary"
							>
								<p class="text-primary text-sm font-semibold">14 May</p>
								<p class="text-green-500 text-sm text-center">15 Slots</p>
							</button>
							<button
								class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary"
							>
								<p class="text-primary text-sm font-semibold">15 May</p>
								<p class="text-green-500 text-sm text-center">15 Slots</p>
							</button>
							<button
								class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary"
							>
								<p class="text-primary text-sm font-semibold">16 May</p>
								<p class="text-green-500 text-sm text-center">15 Slots</p>
							</button>
							<button
								class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary"
							>
								<p class="text-primary text-sm font-semibold">17 May</p>
								<p class="text-green-500 text-sm text-center">15 Slots</p>
							</button>
							<button
								class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary"
							>
								<p class="text-primary text-sm font-semibold">18 May</p>
								<p class="text-green-500 text-sm text-center">15 Slots</p>
							</button>
							<button
								class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary"
							>
								<p class="text-primary text-sm font-semibold">19 May</p>
								<p class="text-green-500 text-sm text-center">15 Slots</p>
							</button>
						</div>
					</div>
				</div>
				<div class="w-full flex flex-col bg-white rounded-xl drop-shadow-md p-1 py-6 mt-8">
					<p class="pb-4 ml-6 font-bold">Morning</p>
					<div class="flex flex-wrap gap-2 w-auto justify-center">
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
					</div>
					<p class="py-4 ml-6 font-bold">Afternoon</p>
					<div class="flex flex-wrap gap-2 w-auto justify-center">
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
					</div>
					<p class="py-4 ml-6 font-bold">Evening</p>
					<div class="flex flex-wrap gap-2 w-auto justify-center">
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
						<button
							class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm"
						>
							10:40 AM
						</button>
					</div>
				</div>
				<div class="w-full flex justify-center items-center py-6">
					<button class="w-full bg-primary hover:bg-[#524af4] py-4 rounded text-white">Book Appointment</button>
				</div>
			</div>
		</div>
		<Footer/>
	</div>
{:else}
	<Loading />
{/if}

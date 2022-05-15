<script context="module">
	export async function load({ session }) {
		if (!session) {
			return {
				status: 302,
				redirect: '/login'
			}
		}
		if (session?.status === 'doctor') {
			// FETCH PATIENT DETAILS HERE
			const response = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/doctor/clinic/', {
				method: 'GET',
				headers: {
					'Content-type': 'application/json',
					Authorization: `Bearer ${session.session}`
				}
			})
			const data = await response.json()
			return {
				props: {
					response: data
				}
			}
		} else {
			if (session?.status === 'admin') {
				return {
					status: 302,
					redirect: '/admin'
				}
			} else {
				return {
					status: 302,
					redirect: '/profile'
				}
			}
		}
	}
</script>

<script>
	import Footer from '$lib/components/dashboard-footer.svelte'
	import Sidebar from '$lib/components/sidebar.svelte'
	import Navbar from '$lib/components/Navbar.svelte'
	import Header from '$lib/components/dashboard-stats.svelte'
	import DashboardFooter from '$lib/components/dashboard-footer.svelte'
	import Changepass from '$lib/components/Changepass.svelte'
	import { ENV } from '$lib/utils'

	import DashboardTable from '$lib/components/DashboardTable.svelte'
	import DoctorProfile from '$lib/components/Doctor-profile.svelte'
	import ClinicDetails from '$lib/components/ClinicDetails.svelte'

	function toggleCollapseShow(classes) {
		collapseShow = classes
	}
	let collapseShow = 'hidden'
	let show = false
	let selected = 'dashboard'
	export let response
</script>

<!-- Navbar -->

<div class="h-screen w-screen overflow-x-hidden">
	<!-- Sidebar -->

	<nav
		class="md:left-0 md:block md:fixed md:top-0 md:bottom-0 md:overflow-y-auto md:flex-row md:flex-nowrap md:overflow-hidden shadow-xl bg-white flex flex-wrap items-center justify-between relative md:w-64 z-10 py-4 px-6"
	>
		<div
			class="md:flex-col md:items-stretch md:min-h-full md:flex-nowrap px-0 flex flex-wrap items-center justify-between w-full mx-auto"
		>
			<!-- Toggler -->
			<button
				class="cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
				type="button"
				on:click={() => toggleCollapseShow('bg-white m-2 py-3 px-6')}
			>
				<i class="fas fa-bars" />
			</button>
			<!-- Brand -->
			<a
				class="md:block text-left md:pb-2 text-blueGray-600 mr-0 inline-block whitespace-nowrap text-sm font-bold p-4 px-0"
				href="/"
			>
				<div class="p-2 text-primary text-3xl font-bold tracking-wide font-poppins">
					<a href="/">Find<span class="text-[#fb3434]">Care</span></a>
				</div>
			</a>
			<!-- User -->
			<ul class="md:hidden items-center flex flex-wrap list-none">
				<li class="inline-block relative" />
				<li class="inline-block relative" />
			</ul>
			<!-- Collapse -->
			<div
				class="md:flex md:flex-col md:items-stretch md:opacity-100 md:relative md:mt-4 md:shadow-none shadow absolute top-0 left-0 right-0 z-40 overflow-y-auto overflow-x-hidden h-auto items-center flex-1 rounded {collapseShow}"
			>
				<!-- Collapse header -->
				<div
					class="md:min-w-full md:hidden block pb-4 mb-4 border-b border-solid border-blueGray-200"
				>
					<div class="flex flex-wrap">
						<div class="w-6/12">
							<a
								class="md:block text-left md:pb-2 text-blueGray-600 mr-0 inline-block whitespace-nowrap text-sm uppercase font-bold p-2 px-0"
								href="/"
							>
								<div class=" text-primary text-3xl font-bold tracking-wide font-poppins">
									<a href="/">Find<span class="text-[#fb3434]">Care</span></a>
								</div>
							</a>
						</div>
						<div class="w-6/12 flex justify-end">
							<button
								type="button"
								class="cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
								on:click={() => toggleCollapseShow('hidden')}
							>
								<i class="fas fa-times" />
							</button>
						</div>
					</div>
				</div>
				<!-- Divider -->
				<hr class="mb-4 md:min-w-full" />
				<!-- Heading -->
				<h6
					class="md:min-w-full text-blueGray-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline"
				>
					Doctor's Admin Panel
				</h6>
				<!-- Navigation -->

				<ul class="md:flex-col md:min-w-full flex flex-col list-none">
					<li class="items-center">
						<button
							class="text-xs uppercase py-3 font-bold block  "
							on:click={() => (selected = 'dashboard')}
						>
							<i class="fas fa-tv mr-2 text-sm text-blueGray-300 " />
							Dashboard
						</button>
					</li>

					<li class="items-center">
						<button
							class="text-blueGray-700 hover:text-blueGray-500 text-xs uppercase py-3 font-bold block"
							on:click={() => (selected = 'Account Setting')}
						>
							<i class="fas fa-user-circle text-blueGray-300 mr-2 text-sm" />
							Account Setting
						</button>
					</li>
					<li class="items-center">
						<button
							class="text-xs uppercase py-3 font-bold block"
							on:click={() => (selected = 'clinic')}
						>
							<i class="fas fa-hospital mr-2 text-sm " />
							Clinic
						</button>
					</li>
					<li class="items-center">
						<button
							class="text-xs uppercase py-3 font-bold block "
							on:click={() => (selected = 'changepass')}
						>
							<i class="fas fa-key mr-2 text-sm " />
							Change Password
						</button>
					</li>
					<li class="items-center">
						<a href="/logout" class="text-xs uppercase py-3 font-bold block ">
							<i class="fas fa-arrow-right-from-bracket mr-2 text-sm " />
							Logout
						</a>
					</li>
				</ul>

				<!-- Divider -->
				<hr class="my-4 md:min-w-full" />
			</div>
		</div>
	</nav>

	<!-- Body -->
	<div class="relative md:ml-64 bg-blueGray-100">
		<Header {response} />

		<div class="px-4 md:px-10 mx-auto w-full m-24 mt-3">
			{#if selected == 'dashboard'}
				<DashboardTable {response} />
			{/if}
			{#if selected == 'Account Setting'}
				<DoctorProfile {response} />
			{/if}
			{#if selected == 'changepass'}
				<Changepass />
			{/if}
			{#if selected == 'clinic'}
				<ClinicDetails />
			{/if}

			<Footer />
		</div>
	</div>
</div>

<!-- Footer -->

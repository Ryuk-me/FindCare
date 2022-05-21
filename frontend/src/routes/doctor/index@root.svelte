<script context="module">
	export async function load({ session, fetch }) {
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
			if (
				response.status === status_code.HTTP_422_UNPROCESSABLE_ENTITY ||
				response.status === status_code.HTTP_403_FORBIDDEN ||
				response.status === status_code.HTTP_401_UNAUTHORIZED
			) {
				await fetch('api/v1/auth/logout')
				return {
					status: 302,
					redirect: '/login'
				}
			}
			let data = await response.json()
			let doctor_profile = null
			if (response.status == status_code.HTTP_404_NOT_FOUND) {
				data = null
				let response = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/doctor/', {
					method: 'GET',
					headers: {
						'Content-type': 'application/json',
						Authorization: `Bearer ${session.session}`
					}
				})
				if (
					response.status === status_code.HTTP_422_UNPROCESSABLE_ENTITY ||
					response.status === status_code.HTTP_403_FORBIDDEN ||
					response.status === status_code.HTTP_401_UNAUTHORIZED
				) {
					await fetch('api/v1/auth/logout')
					return {
						status: 302,
						redirect: '/login'
					}
				}
				doctor_profile = await response.json()
			}
			return {
				props: {
					response: data,
					doctor_profile
				}
			}
		} else {
			if (session?.status === 'admin') {
				return {
					status: 302,
					redirect: '/admin/dashboard'
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
	import { ENV, status_code } from '$lib/utils'
	import DashboardTable from '$lib/components/DashboardTable.svelte'
	import DoctorProfile from '$lib/components/Doctor-profile.svelte'
	import ClinicDetails from '$lib/components/ClinicDetails.svelte'
	import { navigating, session } from '$app/stores'
	import { goto } from '$app/navigation'
	import { user as userProfileStore, doctorDashBoardHeader } from '../../stores'
	import Loading from '$lib/components/Loading.svelte'

	function toggleCollapseShow(classes) {
		collapseShow = classes
	}
	let collapseShow = 'hidden'
	let show = false
	let selected = 'dashboard'
	export let response
	export let doctor_profile
	if (response)
		$userProfileStore = {
			profile_image: response?.doctor?.profile_image
		}
	else
		$userProfileStore = {
			profile_image: doctor_profile?.profile_image
		}
	let is_dashboard_loading = false
	async function doctorDashboardHandler() {
		is_dashboard_loading = true
		const resp = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/doctor/clinic/', {
			method: 'GET',
			headers: {
				'Content-type': 'application/json',
				//@ts-ignore
				Authorization: `Bearer ${$session.session}`
			}
		})
		if (resp.ok) {
			response = await resp.json()
		}
		is_dashboard_loading = false
		selected = 'dashboard'
	}
	$: if ($doctorDashBoardHeader) response = $doctorDashBoardHeader
</script>

<!-- Navbar -->
<svelte:head>
	<title>{doctor_profile ? doctor_profile?.name : response?.doctor?.name}</title>
</svelte:head>
{#if !$navigating}
	<div class="h-screen w-screen overflow-x-hidden font-maven">
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
								on:click={doctorDashboardHandler}
							>
								<i
									class="{is_dashboard_loading
										? 'loading fa fa-spinner fa-spin ml-2 mr-2'
										: 'fas fa-tv ml-2 mr-2'} text-sm text-primary "
								/>
								Dashboard
							</button>
							{#if selected == 'dashboard'}
								<hr class="border-[1px] border-primary bg-primary" />
							{/if}
						</li>

						<li class="items-center">
							<button
								class="text-blueGray-700 hover:text-blueGray-500 text-xs uppercase py-3 font-bold block"
								on:click={() => (selected = 'Account Setting')}
							>
								<i class="fas fa-user-circle text-primary ml-2 mr-2 text-sm" />
								Account Setting
							</button>
							{#if selected == 'Account Setting'}
								<hr class="border-[1px] border-primary bg-primary" />
							{/if}
						</li>
						<li class="items-center">
							<button
								class="text-xs uppercase py-3 font-bold block"
								on:click={() => (selected = 'clinic')}
							>
								<i class="fas fa-hospital ml-2 mr-2 text-primary text-sm " />
								Clinic
							</button>
							{#if selected == 'clinic'}
								<hr class="border-[1px] border-primary bg-primary" />
							{/if}
						</li>
						<li class="items-center">
							<button
								class="text-xs uppercase py-3  font-bold block"
								on:click={() => (selected = 'changepass')}
							>
								<i class="fas fa-key ml-2 mr-2 text-sm text-primary" />
								Change Password
							</button>
							{#if selected == 'changepass'}
								<hr class="border-[1px] border-primary bg-primary" />
							{/if}
						</li>
						<li class="items-center">
							<button
								class="text-xs uppercase py-3 font-bold block"
								on:click={() => {
									$session = null
									$userProfileStore = null
									goto('/logout')
								}}
							>
								<i class="fas fa-arrow-right-from-bracket ml-2 mr-2 text-sm text-primary" />
								Logout
							</button>
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
					<DoctorProfile {response} {doctor_profile} />
				{/if}
				{#if selected == 'changepass'}
					<Changepass />
				{/if}
				{#if selected == 'clinic'}
					<ClinicDetails {response} />
				{/if}

				<Footer />
			</div>
		</div>
	</div>

	<!-- Footer -->
{:else}
	<Loading />
{/if}

<script context="module">
	export async function load({ session, fetch }) {
		if (!session) {
			return {
				status: 302,
				redirect: '/login'
			}
		}
		if (session?.status === 'user') {
			const res = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/user/appointment/', {
				method: 'GET',
				headers: {
					'Content-type': 'application/json',
					Authorization: `Bearer ${session.session}`
				}
			})
			if (
				res.status === status_code.HTTP_422_UNPROCESSABLE_ENTITY ||
				res.status === status_code.HTTP_403_FORBIDDEN ||
				res.status === status_code.HTTP_401_UNAUTHORIZED
			) {
				await fetch('api/v1/auth/logout')
				return {
					status: 302,
					redirect: '/login'
				}
			}
			const appointments = await res.json()
			return {
				props: {
					status: res.status,
					session,
					appointments
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
					redirect: '/doctor'
				}
			}
		}
	}
</script>

<script>
	import { ENV, status_code } from '$lib/utils'
	import Footer from '$lib/components/Footer.svelte'
	import Navbar from '$lib/components/Navbar.svelte'
	import AppointmentTable from '$lib/components/admin/AppointmentTable.svelte'
	import { navigating } from '$app/stores'
	import Loading from '$lib/components/Loading.svelte'
	export let session, appointments, status
</script>

<Navbar />
{#if !$navigating}
	<div class="md:m-6 md:p-6 m-1 p-1">
		<!-- <AppointmentTable {appointments} {session} /> -->
		{#if status === status_code.HTTP_404_NOT_FOUND}
			<h2>No appointment Available</h2>
		{:else}
			<AppointmentTable {appointments} {session} />
		{/if}
	</div>

	<Footer />
{:else}
	<Loading />
{/if}

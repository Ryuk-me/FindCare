<script context="module">
	export async function load({ session }) {
		if (!session) {
			return {
				status: 302,
				redirect: '/login'
			}
		}
		return {
			props: {
				session
			}
		}
	}
</script>

<script>
	import { goto } from '$app/navigation'
	import { onMount } from 'svelte'
	import Loading from '$lib/components/Loading.svelte'
	import { session as sessionStore } from '$app/stores'
	import { ENV } from '$lib/utils'
	export let session

	async function getUser() {
		const res = await fetch(ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/user/', {
			method: 'GET',
			headers: {
				'Content-type': 'application/json',
				Authorization: `Bearer ${session.session}`
			}
		})
		const data = await res.json()
		await new Promise((r) => setTimeout(r, 5000))
		return data
	}
	let isLoading = true
	let user = null
	onMount(async () => {
		user = await getUser()
		isLoading = false
	})
</script>

<svelte:head>
	<title>Profile</title>
</svelte:head>
{#if isLoading}
	<Loading />
{:else}
	<p>User profile route</p>
	{#if user}
		{#each Object.entries(user) as [key, value]}
			<p>{key} : {value}</p>
		{/each}
	{/if}
	<button
		class="bg-orange-500 text-black"
		on:click={() => {
			$sessionStore = null
			goto('/logout')
		}}
	>
		Logout
	</button>
{/if}

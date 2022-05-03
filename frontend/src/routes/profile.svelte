<script context="module">
	import { check_auth_status_profile } from '$root/utils'
	export const load = ({ session }) => {
		return check_auth_status_profile(session, 302, '/login')
	}
</script>

<script>
	import { goto } from '$app/navigation'
	import { session as st } from '$app/stores'
	import { Config } from '$root/Config'
	import { onMount } from 'svelte'
	export let session
	let user = null
	onMount(async () => {
		const resp = await fetch(Config.FINDCARE_API_BASE_URL + '/api/v1/user', {
			method: 'GET',
			mode: 'cors',
			headers: {
				'Content-type': 'application/json',
				Authorization: `Bearer ${session}`
			}
		})
		const data = await resp.json()
		user = data
	})
	async function logout() {
		await fetch('api/v1/logout', {
			method: 'GET'
		})
		$st = null
		await goto('/login')
	}
</script>

<p>User profile route {JSON.stringify(session)}</p>
{#if user}
	{#each Object.entries(user) as [key, value]}
		<p>{key} : {value}</p>
	{/each}
{/if}
<button class="bg-orange-500 text-black" on:click={logout}> Logout </button>

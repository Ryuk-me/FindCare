<script context="module">
	export const load = ({ session }) => {
		if (!session) {
			return {
				status: 302,
				redirect: '/login'
			}
		}
		return {
			props: {
				session: session
			}
		}
	}
</script>

<script>
	import { onMount } from 'svelte'

	export let session
	let user = null
	onMount(async () => {
		const resp = await fetch('https://nextcare-api-ryuk-me.cloud.okteto.net/api/v1/user', {
			headers: {
				'Content-type': 'application/json',
				Authorization: `Bearer ${session.session}` // notice the Bearer before your token
			}
		})
		const data = await resp.json()
		user = data
	})
	async function logout() {
		await fetch('api/v1/logout', {
			method: 'GET'
		})
		location.reload()
	}
</script>

<p>User profile route {JSON.stringify(session)}</p>
{#if user}
	{#each Object.entries(user) as [key, value]}
		<p>{key} : {value}</p>
	{/each}
{/if}
<button class="bg-orange-500 text-black" on:click={logout}> Logout </button>

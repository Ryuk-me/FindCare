<script context="module">
	import * as api from '$lib/api.js'
	export async function load({ session }) {
		if (!session) {
			return {
				status: 302,
				redirect: '/login'
			}
		}
		const resp = await api.get('api/v1/user/', session.session)
		return {
			props: {
				user: resp
			}
		}
	}
</script>

<script>
	import { goto } from '$app/navigation'
import { session } from '$app/stores';
	export let user
</script>

<svelte:head>
	<title>Profile</title>
</svelte:head>

<p>User profile route</p>
{#if user}
	{#each Object.entries(user) as [key, value]}
		<p>{key} : {value}</p>
	{/each}
{/if}
<button
	class="bg-orange-500 text-black"
	on:click={() => {
		$session = null
		goto('/logout')
	}}
>
	Logout
</button>

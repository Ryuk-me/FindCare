<script context="module">
	export async function load({ params, fetch, session, stuff }) {
		if (!session) {
			return {
				status: 302,
				redirect: '/login'
			}
		}
		const resp = await fetch('https://findcare-api-ryuk-me.cloud.okteto.net' + '/api/v1/user', {
			method: 'GET',
			headers: {
				'Content-type': 'application/json',
				Authorization: `Bearer ${session.session}`
			}
		})

		return {
			status: resp.status,
			props: {
				user: resp.ok && (await resp.json())
			}
		}
	}
</script>

<script>
	export let user
</script>

<p>User profile route</p>
{#if user}
	{#each Object.entries(user) as [key, value]}
		<p>{key} : {value}</p>
	{/each}
{/if}
<!-- {#if user}
	{user.count}
{/if} -->
<button class="bg-orange-500 text-black"> Logout </button>

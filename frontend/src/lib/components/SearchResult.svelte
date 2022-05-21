<script>
	import { goto } from '$app/navigation'
	export let name
	export let searchType
	const searchForDoctor = () => goto('/search/' + name)
</script>

{#if searchType !== 'error'}
	<div
		class="results flex flex-row justify-between rounded-md hover:text-primary py-2 px-3"
		on:click={searchForDoctor}
	>
		<p class="">{name}</p>
		<span class="">{searchType}</span>
	</div>
{:else}
	<div class="results flex flex-row justify-between rounded-md py-2 px-3">
		<p class="text-black">{name}</p>
	</div>
{/if}

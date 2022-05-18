<script>
	export let response
	let name = ''
	let address = ''
	let fees = ''
	let opens_at = ''
	let closes_at = ''
	let session_time = ''

	if (response) {
		name = response?.name
		address =
			response?.address?.address +
			', ' +
			response?.address?.city +
			', ' +
			response?.address?.state +
			', ' +
			response?.address?.pincode
		fees = response?.fees
		opens_at = response?.opens_at
		closes_at = response?.closes_at
		session_time =  response?.session_time
	}
</script>

<!--! Clinic data will not be updated -->
{#if response}
	<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">Clinic Details</div>
	<div class="form w-full">
		<div class="relative w-full mb-4">
			<label for="name" class="">Clinic Name</label>
			<input
				type="text"
				disabled
				bind:value={name}
				class="block border cursor-not-allowed text-gray-400 rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="your@domain.com"
				autocomplete="on"
			/>
		</div>

		<div class="relative w-full mb-4">
			<label for="about">Addresss</label>
			<textarea
				type="textarea"
				disabled
				rows="3"
				bind:value={address}
				name="about"
				placeholder="Tell us about yourself"
				title="Enter Address"
				id="about"
				class="block border cursor-not-allowed text-gray-400 text rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				required
				autocomplete="off"
			/>
		</div>

		<div class="relative w-full mb-4">
			<label for="fees" class="">Fees (Rs.)</label>
			<input
				type="number"
				disabled
				bind:value={fees}
				class="block border cursor-not-allowed text-gray-400 rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="Rs.300"
				autocomplete="on"
			/>
		</div>

		<div class="relative w-full mb-4">
			<label for="opens_at" class="">Opens At</label>
			<input
				type="time"
				disabled
				bind:value={opens_at}
				class="block border cursor-not-allowed text-gray-400 rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="10:00 AM"
				autocomplete="on"
			/>
		</div>

		<div class="relative w-full mb-4">
			<label for="closes_at" class="">Closes At</label>
			<input
				type="time"
				disabled
				bind:value={closes_at}
				class="block border cursor-not-allowed text-gray-400 rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="04:00 PM"
				autocomplete="on"
			/>
		</div>

		<div class="relative w-full mb-4">
			<label for="session_time" class="">Session Time (in minutes)</label>
			<input
				type="text"
				disabled
				bind:value={session_time}
				class="block border cursor-not-allowed text-gray-400 rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
				placeholder="10:00 AM"
				autocomplete="on"
			/>
		</div>
		
	</div>
{:else}
	<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">
		Add clinic Button here if there is no clinic added by dr
	</div>
	<div class="flex justify-center mt-48 mb-48 ">
		<button class="bg-primary p-4 rounded-sm text-white hover:bg-blue-700"> ADD CLINIC </button>
	</div>
{/if}

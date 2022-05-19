<script>
	export let accountSettingJson
</script>

<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">Profile</div>
<div class="form w-full">
	<div class="relative w-full mb-4">
		<label for="name" class="">Name</label>
		<input
			disabled
			bind:value={accountSettingJson.name}
			class="block border rounded py-2 px-3 w-full mt-3 text-gray-400 cursor-not-allowed focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			autocomplete="on"
		/>
	</div>
	<div class="relative w-full mb-4">
		<label for="email" class="">Email</label>
		<input
			disabled
			bind:value={accountSettingJson.email}
			type="email"
			class="block border rounded py-2 px-3 w-full mt-3 text-gray-400 cursor-not-allowed focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
			autocomplete="on"
		/>
	</div>
</div>

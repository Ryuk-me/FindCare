<script>
	import verified_img from '$lib/assets/book/correct.png'
	import { capitalize } from '../utils'
	export let name
	export let experience
	export let speciality
	export let fees
	export let address
	export let slug
	export let profile_img
</script>

<div class="flex flex-col lg:w-[30vw] w-full h-64 bg-white rounded-2xl drop-shadow-xl my-4">
	<div class="flex h-[75%] px-4">
		<div class="flex w-36 justify-center items-center">
			<img src={profile_img} alt="doctor.png" class="w-24 rounded-[50%]" />
			<img src={verified_img} alt="correct.png" class="relative right-5 top-5" />
		</div>
		<div class="pt-6">
			<a href={'/search/doctor/' + slug}
				><h2 class="text-blue-600 font-bold hover:text-[#0f02fa]">{name}</h2></a
			>
			<p class="capitalize mt-[2px]">{speciality}</p>
			<p class="mt-[2px]">{experience} {experience > 1 ? 'years' : 'year'} experience</p>
			<p class="mt-[2px]">
				{capitalize(address.address) +
					', ' +
					capitalize(address.city) +
					', ' +
					capitalize(address.state)}
			</p>
			<p class="mt-[2px]">₹ {fees} consultation fee at clinic</p>
		</div>
	</div>
	<div class="flex justify-center items-center">
		<a
			class="bg-blue-600 text-white font-semibold rounded-full px-8 py-2 hover:bg-[#0f02fa]"
			href={'/search/doctor/' + slug}>Book now</a
		>
	</div>
</div>

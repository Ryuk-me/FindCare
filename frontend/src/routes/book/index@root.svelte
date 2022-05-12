<script>
	import Navbar from '$lib/components/Navbar.svelte'
	import Card from '$lib/components/doctor-card.svelte'
</script>

<div class="h-screen w-screen flex flex-col overflow-x-hidden">

	<div class="w-screen">
		<Navbar />
	</div>

	<div class="w-full lg:px-24">
		<input type="text" class="w-full rounded-full px-8 py-3 mt-8 drop-shadow-md focus:outline-none border border-primary" placeholder="lorem ipsum"/>
	</div>
	<div class="flex w-full items-center font-semibold text-2xl py-8 px-24">
		<p>16 doctors availiable in Patna</p>
	</div>
	<div class="w-full flex">
		<!-- lg:px-20 -->
		<div class="lg:flex flex-col lg:w-80 p-4 hidden ml-20">
			<div class="flex flex-col bg-white h-64 rounded-xl drop-shadow-md p-4 ">
				<div class="flex justify-between">
					<p class="font-bold">Filter</p>
					<button class="text-blue-700 font-bold">clear all</button>
				</div>
				<div class="flex flex-col mt-6">
					<p>Availiability</p>
					<div class="mt-4">
						<input type="radio" name="avail" id="today" value="today" class="mr-2" checked/>
						<label for="today">Today</label>
					</div>
					<div class="mt-4">
						<input type="radio" name="avail" id="tomorrow" value="tomorrow" class="mr-2"/>
						<label for="tomorrow">Tomorrow</label>
					</div>
					<div class="mt-4">
						<input type="radio" name="avail" id="next7days" value="next7days" class="mr-2"/>
						<label for="next7days">Next 7 Days</label>
					</div>
				</div>
			</div>
			<div class="flex flex-col bg-white h-64 rounded-xl drop-shadow-md p-4 mt-12">
				<div class="flex justify-between">
					<p class="font-bold">Gender</p>
					<button class="text-blue-700 font-bold">clear all</button>
				</div>
				<div class="flex flex-col mt-6">
					<div class="mt-4">
						<input type="radio" name="gender" id="anyone" value="anyone" class="mr-2" checked/>
						<label for="anyone">Any one</label>
					</div>
					<div class="mt-4">
						<input type="radio" name="gender" id="male" value="male" class="mr-2"/>
						<label for="male">Male</label>
					</div>
					<div class="mt-4">
						<input type="radio" name="gender" id="female" value="female" class="mr-2"/>
						<label for="female">Female</label>
					</div>
				</div>
			</div>
		</div>
			<div class="w-full flex flex-wrap justify-between mx-24">
				<Card/>
				<Card/>
				<Card/>
				<Card/>
			</div>
	</div>

</div>

<!-- <h1 class="text-blue-600 text-4xl font-bold font-poppins pb-2 text-center mt-4">
	Find<span class="text-red-500">Care</span>
</h1> -->

<!-- <h2 class="text-blue-600 font-bold text-xl py-2">| Book your Appointment</h2>
<h2 class="text-black text-xl font-medium pt-4 pb-6">Find your doctor</h2> -->
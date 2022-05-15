<script>
	import Navbar from '$lib/components/Navbar.svelte'
    import doctor_img from '$lib/assets/book/doctor.png'
    import verified_img from '$lib/assets/book/correct.png'
</script>

<div class="h-screen w-screen flex flex-col overflow-x-hidden">
	<div class="w-screen">
		<Navbar />
	</div>

	<div class="w-full lg:px-24 px-4 ">
		<input
			type="text"
			class="w-full rounded-full px-8 py-3 mt-8 drop-shadow-md focus:outline-none border border-primary"
			placeholder="lorem ipsum"
		/>
	</div>

    <div class="h-full w-screen flex lg:flex-row flex-col justify-between lg:px-24 mt-8">
        <!-- left div -->
        <div class="lg:w-[65%] flex flex-col">
            <!-- first card  -->
            <div class="w-full flex bg-white rounded-xl drop-shadow-md p-8 mb-8">
                <!-- img div -->
                <div class="lg:w-full w-1/4 mr-8">
                    <img src="{doctor_img}" alt="doctor.png">
                </div>
                <!-- info div -->
                <div>
                    <h1 class="font-bold text-2xl">Dr. Manav Singh</h1>
                    <p>MDS Orthopedic</p>
                    <p>12 years experience</p>
                    <div class="flex mt-2">
                        <img src="{verified_img}" alt="verified.png" class="mr-2">
                        Verified
                    </div>
                    <p class="lg:block hidden">
                        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Voluptatibus vero distinctio obcaecati laborum ut dolores eius expedita, maxime molestiae suscipit sequi doloremque. Magnam consequatur dolor, repudiandae libero consequuntur ut repellat!
                        Eligendi dignissimos ipsum maxime, eos deleniti expedita perferendis mollitia natus ab, rem explicabo quasi ullam quam nostrum nulla aperiam repellendus. Maiores voluptates vel odit impedit, non aperiam voluptatem voluptate error.
                    </p>
                </div>
            </div>

            <!-- second card  -->
            <div class="w-full lg:flex bg-white rounded-xl drop-shadow-md p-8 hidden">
                <div class="w-full flex flex-col">
                    <p>Sri Krishnapuri, Patna</p>
                    <div class="flex w-full justify-between mt-4">
                        <div class="w-40">
                            <p class="text-primary font-bold">Harihar dental clinic</p>
                        </div>
                        <div>
                            <p>Mon-Sat</p>
                            <p>9:00 am to 6:00 pm</p>
                        </div>
                        <div>
                            <p>Rs 300</p>
                        </div>
                    </div>
                    <div class="flex w-full justify-between mt-4">
                        <div class="w-40">
                            <p>Boring road</p>
                        </div>
                        <div>
                            <p>Mon-Sat</p>
                            <p>9:00 am to 6:00 pm</p>
                        </div>
                        <div>
                            <p>Rs 300</p>
                        </div>
                    </div>
                    
                </div>

            </div>


        </div>
        <!-- right div  -->
        <div class="lg:w-[30%] flex flex-col">
            <div class="w-full flex flex-col bg-white rounded-xl drop-shadow-md p-8">
                <div class="flex">
                    <div class="line-none flex overflow-auto whitespace-nowrap p-2">
                        <button class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary">
                            <p class="text-primary text-sm font-semibold">13 May</p>
                            <p class="text-green-500 text-sm text-center">15 Slots</p>         
                        </button>
                        <button class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary">
                            <p class="text-primary text-sm font-semibold">14 May</p>
                            <p class="text-green-500 text-sm text-center">15 Slots</p>         
                        </button>
                        <button class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary">
                            <p class="text-primary text-sm font-semibold">15 May</p>
                            <p class="text-green-500 text-sm text-center">15 Slots</p>         
                        </button>
                        <button class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary">
                            <p class="text-primary text-sm font-semibold">16 May</p>
                            <p class="text-green-500 text-sm text-center">15 Slots</p>         
                        </button>
                        <button class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary">
                            <p class="text-primary text-sm font-semibold">17 May</p>
                            <p class="text-green-500 text-sm text-center">15 Slots</p>         
                        </button>
                        <button class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary">
                            <p class="text-primary text-sm font-semibold">18 May</p>
                            <p class="text-green-500 text-sm text-center">15 Slots</p>         
                        </button>
                        <button class=" flex flex-col px-4 py-2 mx-1 rounded border-2 border-solid text-white border-primary">
                            <p class="text-primary text-sm font-semibold">19 May</p>
                            <p class="text-green-500 text-sm text-center">15 Slots</p>         
                        </button>
                   
                    </div>
                </div>
            </div>
            <div class="w-full flex flex-col bg-white rounded-xl drop-shadow-md p-1 py-6 mt-8">

                <p class="pb-4 ml-6 font-bold">Morning</p>
                <div class="flex flex-wrap gap-2 w-auto justify-center">

                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                </div>
                <p class="py-4 ml-6 font-bold">Afternoon</p>
                <div class="flex flex-wrap gap-2 w-auto justify-center">

                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                </div>
                <p class="py-4 ml-6 font-bold">Evening</p>
                <div class="flex flex-wrap gap-2 w-auto justify-center">

                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                    <button class="text-center rounded border-2 border-solid text-primary border-primary p-2 text-sm">
                        10:40 AM
                    </button>
                </div>
            </div>
            <div class="w-full flex justify-center items-center py-6">
                <button class="w-full bg-primary py-4 rounded text-white">Book Appointment</button>
            </div>
        </div>
    </div>  
</div>

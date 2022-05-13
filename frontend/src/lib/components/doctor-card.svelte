<script>
    import doctor_img from '$lib/assets/book/doctor.png'
    import verified_img from '$lib/assets/book/correct.png'
</script>

<div class="flex flex-col lg:w-[30vw] w-full h-64 bg-white rounded-2xl drop-shadow-xl my-4">
    <div class="flex h-[75%] px-4">
        <div class="flex w-36 justify-center items-center">
            <img src={doctor_img} alt="doctor.png" class="w-24" />
            <img src={verified_img} alt="correct.png" class="relative right-5 top-5" />
        </div>
        <div class="pt-6">
            <h2 class="text-blue-600 font-bold">Dr. Moon Knight</h2>
            <p>Dentist</p>
            <p>12 years experience</p>
            <p>Dentist care,Rajendra nagar,Patna,Bihar</p>
            <p>₹400 consultation fee at clinic</p>
        </div>
    </div>
    <div class="flex justify-center items-center">
        <button class="bg-blue-600 text-white font-semibold rounded-full px-8 py-2"
            >Book now</button
        >
    </div>
</div>
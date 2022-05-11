<script>
    let menu = false
</script>

<div
class="navbar flex items-center flex-wrap lg:justify-between p-4 lg:px-24 lg:w-auto w-screen"
>
<div class="flex justify-between lg:w-auto w-full items-center">
    <div class="flex flex-row w-full lg:w-auto">
        <div>
            <i
                class="fa-solid {menu
                    ? 'fa-times'
                    : 'fa-bars'} text-primary p-2 mt-2 inline-flex rounded ml-auto lg:hidden md:hidden"
                id="menu"
                on:click|preventDefault={() => (menu = !menu)}
            />
        </div>
        <div class="p-2 mr-4 text-primary text-3xl font-bold tracking-wide font-poppins">
            <a href="/">Find<span class="text-[#fb3434]">Care</span></a>
        </div>
    </div>
    <div class="lg:hidden">
        <a href="/login"
            ><button
                class="bg-primary hover:bg-[#524af4] text-white rounded-full w-full px-5 py-1.5 font-light"
                >Login</button
            ></a
        >
    </div>
</div>
<div
    class="lg:w-auto {menu
        ? 'block'
        : 'hidden'} lg:flex md:flex lg:flex-row flex-col flex mb-5 lg:mb-0 font-semibold"
>
    <a href="/" class="px-3 mx-3 hover:text-[#fb3434]">Home</a>
    <a href="/about-us" class="px-3 mx-3 hover:text-[#fb3434]">About</a>
    <a href="/support" class="px-3 mx-3 hover:text-[#fb3434]">Support</a>
    <a href="/contact" class="px-3 mx-3 hover:text-[#fb3434]">Contact</a>
</div>
<div class="flex-col lg:flex hidden lg:flex-row mx-6 justify-center items-center">
    <a href="/login" class="font-semibold mr-7 hover:text-[#524af4]">Login</a>
    <a href="/signup"
        ><button
            class="bg-primary hover:bg-[#524af4] text-white rounded-full w-full px-7 py-1 font-medium"
            >Sign up</button
        ></a
    >
</div>
</div>
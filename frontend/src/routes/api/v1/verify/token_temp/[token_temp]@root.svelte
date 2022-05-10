<script>
	let show = false
    let password = ''
	let confirmPassword = ''

    const handleInput = (event) => {
		password = event.target.value
	}
</script>

<div class="h-screen w-screen flex items-center justify-center">
    <div class="font-maven">
        <h1 class="text-primary text-4xl font-bold font-poppins mb-2">FindCare</h1>
        <div class="border border-primary p-8 rounded">
            <h2 class="text-2xl font-bold mb-2">Change password</h2>
            <form class="">
                <div class="">
                    <label for="password">Password</label>
                    <input
                        type={show ? 'text' : 'password'}
                        name="password"
                        placeholder="***********"
                        title="Enter Your Password"
                        id="password"
                        class="block border rounded py-2 px-3 w-96 my-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
                        required
                        on:input={handleInput}
                        autocomplete="off"
                    />
                    <span>
                        <i
                            class="fa {show
                                ? 'fa-eye-slash'
                                : 'fa-eye'} hover:cursor-pointer text-slate-600 float-right relative bottom-11 right-3"
                            aria-hidden="true"
                            id="eye"
                            on:click|preventDefault={() => (show = !show)}
                        />
                    </span>
                </div>
                <div class="">
                    <label for="confirmPassword">Confirm Password</label>
                    <input
                        type="password"
                        name="confirmPassword"
                        placeholder="***********"
                        title="Enter Your Password Again"
                        id="confirmPassword"
                        class="block border rounded py-2 px-3 w-96 mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
                        required
                        autocomplete="off"
                        bind:value={confirmPassword}
                    />
                </div>
                <button
                    class="mt-4 bg-primary hover:bg-[#524af4] py-2 text-white rounded w-full font-medium"
                    >SUBMIT</button
                >
            </form>
        </div>
    </div>
</div>

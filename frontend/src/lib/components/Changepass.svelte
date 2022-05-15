<script>
    let show = false;
</script>

<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">
    Change Password
 </div>
 <div class="form w-full">
     <div class="relative w-full mb-4">
         <label for="changepass" class="">Change Passowrd</label>
         <div class="relative">
             <input
                 type={show ? 'text' : 'password'}
                 placeholder="********"
                 class="block border rounded py-2 pt-3 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
                 id="password"
                 autocomplete="off"
             />
             <span>
                 <i
                     class="fa {show ? 'fa-eye-slash' : 'fa-eye'} hover:cursor-pointer text-slate-600"
                     aria-hidden="true"
                     id="eye"
                     on:click|preventDefault={() => (show = !show)}
                 />
             </span>
         </div>
     </div>
     <div class="relative w-full mb-4">
         <label for="confirmpass" class="">Confirm Password</label>
         <input
             type="password"
             placeholder="********"
             class="block border rounded py-2 pt-3 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
             id="password"
             autocomplete="off"
         />
     </div>
     <button
         class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
         >Save Changes</button
     >
 </div>

 <style>
	#eye {
		position: absolute;
		right: 14px;
		transform: translate(0, -50%);
		top: 50%;
	}
</style>
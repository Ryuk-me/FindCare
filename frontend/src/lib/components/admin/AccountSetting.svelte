<div class="text-xl text-center w-full font-bold border-b p-3 mb-4">
    Edit Profile
  </div>
 <div class="form w-full">
     <div class="relative w-full mb-4">
         <div class="navigation px-6 mb-4 lg:mb-0 rounded-lg lg:mr-6">
             <div class="photo flex justify-center flex-col lg:flex-row items-center py-4">
                 <img
                     class="object-cover w-28 h-28 m-6 rounded-full"
                     src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
                     alt=""
                 />
                 <!-- <button
                         class="bg-primary hover:bg-[#524af4] text-white rounded-md w-full px-7 py-1 font-medium"
                         >Change Profile Photo</button
                     > -->
                 <input
                     type="file"
                     class="block w-full center text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-primary file:text-white hover:file:bg-[#524af4]"
                 />
             </div>
         </div>
     </div>
     <div class="relative w-full mb-4">
         <label for="name" class="">Name</label>
         <input
             type="text"
             class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
             placeholder="Neeraj Kumar"
             autocomplete="on"
         />
     </div>
     <div class="relative w-full mb-4">
         <label for="email" class="">Email</label>
         <input
             type="email"
             class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
             placeholder="your@domain.com"
             autocomplete="on"
         />
     </div>
     <div class="relative w-full mb-4">
         <label for="phone" class="">Phone Number</label>
         <input
             type="number"
             class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
             placeholder="9876xxxxxx"
             autocomplete="on"
         />
     </div>
     <div class="relative w-full mb-4">
         <label for="dob" class="">Date Of Birth</label>
         <input
             type="date"
             class="block border rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
             placeholder="your@domain.com"
             autocomplete="on"
         />
     </div>
     
     <div class="relative w-full mb-4">
         <label for="gender">Gender</label>
         <div class="flex items-center pt-2 lg:pt-5">
             <div class="flex items-center ">
                 <input
                     id="male"
                     type="radio"
                     name="gender"
                     class="mr-2"
                     value="male"
                     required
                     autocomplete="off"
                 />
                 <label class="form-check-label inline-block text-gray-800" for="male" value="male"
                     >Male</label
                 >
             </div>
             <div class="flex items-center mx-5">
                 <input
                     id="female"
                     type="radio"
                     name="gender"
                     class="mr-2"
                     value="female"
                     required
                     autocomplete="off"
                 />
                 <label class="form-check-label inline-block text-gray-800" for="female" value="female"
                     >Female</label
                 >
             </div>
             <div class="flex items-center">
                 <input
                     id="other"
                     type="radio"
                     name="gender"
                     class="mr-2"
                     value="other"
                     required
                     autocomplete="off"
                 />
                 <label class="form-check-label inline-block text-gray-800" for="other" value="other"
                     >Other</label
                 >
             </div>
         </div>
     </div>
     <div class="relative w-full mb-4">
         <label for="about">About</label>
         <textarea
             type="textarea"
             rows="3"
             name="about"
             placeholder="Tell us about yourself"
             title="Enter About Yourself"
             id="about"
             class="block border text rounded py-2 px-3 w-full mt-3 focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary"
             required
             autocomplete="off"
         />
     </div>
     <div class="relative w-full mb-4" />
     <button
         class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white mb-3 font-medium py-2 rounded focus:outline-none focus:shadow-outline"
         >Save Changes</button
     >
 </div>
 
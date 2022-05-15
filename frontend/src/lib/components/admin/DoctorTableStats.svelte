<script>
    import TableDropdown from "$lib/components/TableDropdown.svelte";
    export let doctorImg = 'https://cdn-icons-png.flaticon.com/512/387/387569.png'
    export let doctorName = 'Neeraj Kumar'
    export let numberOfAppointment = '453'
    export let numberOfPatients = '53'
    export let status = 'pending'
    export let color = "light";
</script>

<tr>
   <th
     class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center"
   >
     <img
       src="{doctorImg}"
       class="h-12 w-12 bg-white rounded-full border"
       alt="..."
     />
     <span
       class="ml-3 font-bold {color === 'light' ? 'btext-blueGray-600' : 'text-whit'}"
     >
       {doctorName}
     </span>
   </th>
   <td
     class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
   >
     {numberOfAppointment}
   </td>
   <td
     class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
   >
     {numberOfPatients}
   </td>
   <td
     class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
   >
   {#if status == 'verified' }
   <i class="fas fa-circle text-blue-500 mr-2"></i> {status}
   
   {/if}
   {#if status == 'pending' }
   <i class="fas fa-circle text-orange-500 mr-2"></i> {status}
   
   {/if}
   {#if status == 'removed' }
   <i class="fas fa-circle text-red-500 mr-2"></i> {status}
       
   {/if}
   </td>
   <td
      class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
    >
      <div class="flex">
        <button type="button" class="text-white bg-green-700 hover:bg-green-800 focus:ring-2 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">
           <i class="fas fa-check mr-2"></i> Verify
          </button>
      </div>
    </td>
   <td
     class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
   >
     <div class="flex items-center">
       <button type="button" class="text-white bg-red-700 hover:bg-red-800 focus:ring-2 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800">
           <i class="fas fa-xmark mr-2"></i> Remove
          </button>
     </div>
   </td>
 
 </tr>
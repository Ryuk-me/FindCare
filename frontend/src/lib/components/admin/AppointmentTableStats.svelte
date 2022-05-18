<script>
    import TableDropdown from "$lib/components/TableDropdown.svelte";
    export let doctorImg = 'https://cdn-icons-png.flaticon.com/512/4825/4825038.png'
    export let doctorName = 'Neeraj Kumar'
    export let clinicAddress = 'Punaichak, Patna'
    export let dateOfAppointment = '25-05-2022'
    export let status = 'upcoming'
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
     {dateOfAppointment}
   </td>
   <td
     class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
   >
   {#if status == 'completed' }
   <i class="fas fa-circle text-teal-500 mr-2"></i> {status}
   
   {/if}
   {#if status == 'cancelled' }
   <i class="fas fa-circle text-red-500 mr-2"></i> {status}
       
   {/if}
   {#if status == 'upcoming' }
   <i class="fas fa-circle text-orange-500 mr-2"></i> {status}
       
   {/if}
   </td>

   <td
     class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
   >
    {clinicAddress}
      
  
   </td>
 
 </tr>
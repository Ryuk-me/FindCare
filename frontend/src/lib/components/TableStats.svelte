<script>
     import TableDropdown from "$lib/components/TableDropdown.svelte";
     export let patientImg = 'https://cdn-icons-png.flaticon.com/512/4825/4825038.png'
     export let patientName = 'Neeraj Kumar'
     export let dateOfAppointment = '10-10-22'
     export let status = 'completed'
     export let color = "light";
</script>

<tr>
    <th
      class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center"
    >
      <img
        src="{patientImg}"
        class="h-12 w-12 bg-white rounded-full border"
        alt="..."
      />
      <span
        class="ml-3 font-bold {color === 'light' ? 'btext-blueGray-600' : 'text-whit'}"
      >
        {patientName}
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
    {#if status == 'pending' }
    <i class="fas fa-circle text-orange-500 mr-2"></i> {status}
    
    {/if}
    {#if status == 'completed' }
    <i class="fas fa-circle text-teal-500 mr-2"></i> {status}
    
    {/if}
    {#if status == 'canceled' }
    <i class="fas fa-circle text-red-500 mr-2"></i> {status}
        
    {/if}
    </td>
    <td
      class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
    >
      <div class="flex">
        <button type="button" class="text-white bg-green-700 hover:bg-green-800 focus:ring-2 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">
           <i class="fas fa-check mr-2"></i> Approve
          </button>
      </div>
    </td>
    <td
      class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
    >
      <div class="flex items-center">
        <button type="button" class="text-white bg-red-700 hover:bg-red-800 focus:ring-2 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800">
            <i class="fas fa-xmark mr-2"></i> Cancel
           </button>
      </div>
    </td>
  
  </tr>
<script>
    // core components
    export let statSubtitle = "Total Appointment";
    export let statTitle = "350";

    export let statIconName = "far fa-chart-bar";
    // can be any of the background color utilities
    // from tailwindcss
    export let statIconColor = "bg-red-500";
  </script>
  
  <div
    class="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
  >
    <div class="flex-auto p-4">
      <div class="flex flex-wrap">
        <div class="relative w-full pr-4 max-w-full flex-grow flex-1">
          <h5 class="text-blueGray-400 mb-3 uppercase font-bold text-xs">
            {statSubtitle}
          </h5>
          <span class="font-semibold text-xl text-blueGray-700">
            {statTitle}
          </span>
        </div>
        <div class="relative w-auto pl-4 flex-initial">
          <div
            class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full {statIconColor}"
          >
            <i class="{statIconName}"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
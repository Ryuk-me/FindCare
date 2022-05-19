<script>
	let sortBy = true
	export let placeholderdata = 'Search...'
	export let type
	import { adminQueryDoctorName, adminQueryUserEmail } from '../../stores'
</script>

<div
	class="flex md:flex-row flex-col justify-between lg:gap-24 relative my-4 pb-5 lg:w-[full] w-[90vww]"
>
	{#if type == 'user'}
		<input
			type="text"
			class="block border rounded-md py-2 pl-3 pr-10 w-full focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary  border-primary"
			placeholder={placeholderdata}
			bind:value={$adminQueryUserEmail}
			autocomplete="off"
			id="search"
		/>
	{:else}
		<input
			type="text"
			class="block border rounded-md py-2 pl-3 pr-10 w-full focus:outline-none focus:shadow-outline focus:ring-1 focus:ring-primary  border-primary"
			placeholder={placeholderdata}
			bind:value={$adminQueryDoctorName}
			autocomplete="off"
			id="search"
		/>
	{/if}
	<!-- <div class="search-button">
		<button
			class="bg-primary tracking-wider text-lg hover:bg-[#524af4] w-full text-white font-medium px-9 py-2 rounded focus:outline-none focus:shadow-outline"
			>Search</button
		>
	</div> -->
	<!-- <div class="flex justify-center">
		<div class="">
			<div class="dropdown relative">
				<button
					class="
                dropdown-toggle
                px-6
                py-2.5
                bg-blue-600
                text-white
                font-medium
                text-xs
                leading-tight
                uppercase
                rounded
                shadow-md
                hover:bg-blue-700 hover:shadow-lg
                focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0
                active:bg-blue-800 active:shadow-lg active:text-white
                transition
                duration-150
                ease-in-out
                flex
                items-center
                whitespace-nowrap
              "
					type="button"
					id="dropdownMenuButton1"
					data-bs-toggle="dropdown"
					aria-expanded="false"
					on:click|preventDefault={() => (sortBy = !sortBy)}
				>
					Sort By
					<svg
						aria-hidden="true"
						focusable="false"
						data-prefix="fas"
						data-icon="caret-down"
						class="w-2 ml-2"
						role="img"
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 320 512"
					>
						<path
							fill="currentColor"
							d="M31.3 192h257.3c17.8 0 26.7 21.5 14.1 34.1L174.1 354.8c-7.8 7.8-20.5 7.8-28.3 0L17.2 226.1C4.6 213.5 13.5 192 31.3 192z"
						/>
					</svg>
				</button>
				<ul
					class="
                dropdown-menu
                min-w-max
                absolute
                {sortBy ? 'hidden' : ''}
                bg-white
                text-base
                z-50
                float-left
                py-2
                list-none
                text-left
                rounded-lg
                shadow-lg
                mt-1
                m-0
                bg-clip-padding
                border-none
              "
					aria-labelledby="dropdownMenuButton1"
				>
					<li>
						<a
							class="
                    dropdown-item
                    text-sm
                    py-2
                    px-4
                    font-normal
                    block
                    w-full
                    whitespace-nowrap
                    bg-transparent
                    text-gray-700
                    hover:bg-gray-100
                  "
							href="#">New First</a
						>
					</li>
					<li>
						<a
							class="
                    dropdown-item
                    text-sm
                    py-2
                    px-4
                    font-normal
                    block
                    w-full
                    whitespace-nowrap
                    bg-transparent
                    text-gray-700
                    hover:bg-gray-100
                  "
							href="#">Upcoming First</a
						>
					</li>
				</ul>
			</div>
		</div>
	</div> -->
</div>

<script context="module">
	import { ENV, status_code } from '$lib/utils'
	export async function load({ params, fetch }) {
		const token = params.token
		const resp = await fetch(
			ENV.VITE_FINDCARE_API_BASE_URL + '/api/v1/email/verify-email?token=' + token
		)
		const data = await resp.json()
		return {
			props: {
				status: resp.status,
				msg: data.detail
			}
		}
	}
</script>

<script>
	export let msg
	export let status
</script>

<svelte:head>
	<title>Email Verification</title>
</svelte:head>
<div class="flex justify-center">
	{#if status === status_code.HTTP_202_ACCEPTED || status === status_code.HTTP_409_CONFLICT}
		<div class="animation-ctn grid place-items-center h-80 w-3/6">
			<div class="icon icon--order-success svg ">
				<svg xmlns="http://www.w3.org/2000/svg" width="154px" height="154px">
					<g fill="none" stroke="#22AE73" stroke-width="2">
						<circle
							cx="77"
							cy="77"
							r="72"
							style="stroke-dasharray:480px, 480px; stroke-dashoffset: 960px;"
						/>
						<circle
							id="colored"
							fill="#22AE73"
							cx="77"
							cy="77"
							r="72"
							style="stroke-dasharray:480px, 480px; stroke-dashoffset: 960px;"
						/>
						<polyline
							class="st0"
							stroke="#fff"
							stroke-width="10"
							points="43.5,77.8 63.7,97.9 112.2,49.4 "
							style="stroke-dasharray:100px, 100px; stroke-dashoffset: 200px;"
						/>
					</g>
				</svg>
			</div>
			<p class="text-2xl text-center first-letter:capitalize font-maven">{msg}</p>
			<a href="/login" class="text-primary font-maven text-xl font-bold hover:text-blue-800"
				>Click here to Login</a
			>
		</div>
	{:else}
		<div class="animation-ctn grid place-items-center h-80 w-3/6">
			<div class="icon icon--order-success svg">
				<svg xmlns="http://www.w3.org/2000/svg" width="154px" height="154px">
					<g fill="none" stroke="#F44812" stroke-width="2">
						<circle
							cx="77"
							cy="77"
							r="72"
							style="stroke-dasharray:480px, 480px; stroke-dashoffset: 960px;"
						/>
						<circle
							id="colored"
							fill="#F44812"
							cx="77"
							cy="77"
							r="72"
							style="stroke-dasharray:480px, 480px; stroke-dashoffset: 960px;"
						/>
						<polyline
							class="st0"
							stroke="#fff"
							stroke-width="10"
							points="43.5,77.8  112.2,77.8 "
							style="stroke-dasharray:100px, 100px; stroke-dashoffset: 200px;"
						/>
					</g>
				</svg>
			</div>
			<p class="text-2xl text-center first-letter:capitalize font-maven">{msg}</p>
			<a href="/login" class="text-primary font-maven text-xl font-bold hover:text-blue-800"
				>Click here to Login</a
			>
		</div>
	{/if}
</div>

<style>
	.animation-ctn {
		text-align: center;
		margin-top: 5em;
	}

	@-webkit-keyframes checkmark {
		0% {
			stroke-dashoffset: 100px;
		}

		100% {
			stroke-dashoffset: 200px;
		}
	}

	@-ms-keyframes checkmark {
		0% {
			stroke-dashoffset: 100px;
		}

		100% {
			stroke-dashoffset: 200px;
		}
	}

	@keyframes checkmark {
		0% {
			stroke-dashoffset: 100px;
		}

		100% {
			stroke-dashoffset: 0px;
		}
	}

	@-webkit-keyframes checkmark-circle {
		0% {
			stroke-dashoffset: 480px;
		}

		100% {
			stroke-dashoffset: 960px;
		}
	}

	@-ms-keyframes checkmark-circle {
		0% {
			stroke-dashoffset: 240px;
		}

		100% {
			stroke-dashoffset: 480px;
		}
	}

	@keyframes checkmark-circle {
		0% {
			stroke-dashoffset: 480px;
		}

		100% {
			stroke-dashoffset: 960px;
		}
	}

	@keyframes colored-circle {
		0% {
			opacity: 0;
		}

		100% {
			opacity: 100;
		}
	}

	/* other styles */
	/* .svg svg {
    display: none
}
 */
	.inlinesvg .svg svg {
		display: inline;
	}

	/* .svg img {
    display: none
} */

	.icon--order-success svg polyline {
		-webkit-animation: checkmark 0.25s ease-in-out 0.7s backwards;
		animation: checkmark 0.25s ease-in-out 0.7s backwards;
	}

	.icon--order-success svg circle {
		-webkit-animation: checkmark-circle 0.6s ease-in-out backwards;
		animation: checkmark-circle 0.6s ease-in-out backwards;
	}
	.icon--order-success svg circle#colored {
		-webkit-animation: colored-circle 0.6s ease-in-out 0.7s backwards;
		animation: colored-circle 0.6s ease-in-out 0.7s backwards;
	}
</style>

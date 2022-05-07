<script context="module">
	export async function load({ fetch }) {
		const res = await fetch('api/v1/auth/logout')
		return {
			status: 302,
			redirect: '/login'
		}
	}
</script>

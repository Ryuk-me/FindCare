<svelte:head>
	<title>Findcare</title>
</svelte:head>

<div class="container-home">
	<h1 class="text-2xl
	">Welcome to FindCare</h1>

	<button><a href="/login">login</a></button>
	<button><a href="/signup">signup</a></button>
	<button><a href="/reset">reset</a></button>
	<button><a href="/register-doctor">register-doctor</a></button>
	<button><a href="/profile">profile</a></button>
	<button><a href="/dashboard">dashboard</a></button>
</div>

<style>
	.container-home {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
</style>

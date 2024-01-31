<!-- ChatBubble.svelte -->
<script>
	export let text = '';
	export let sender = 'user';
	export let loading = false;
</script>

<div class="w-full block">
	<div
		class="flex items-start mb-4 max-w-3xl {sender == 'user' ? 'float-right' : 'float-left'} mx-10"
	>
		{#if sender === 'gpt'}
			<div class="mr-2">
				<svg viewBox="0 0 20 20" fill="currentColor" class="h-6 w-6 text-gray-400">
					<path
						fill-rule="evenodd"
						d="M10 0c-5.523 0-10 4.477-10 10s4.477 10 10 10 10-4.477 10-10-4.477-10-10-10zm2.5 14.5h-5v-1h5v1zm3-3h-8v-1h8v1zm0-3h-8v-1h8v1z"
						clip-rule="evenodd"
					/>
				</svg>
			</div>
		{/if}
		{#if loading}
			<div class="bg-white rounded-lg p-4 shadow-md animate-pulse">
				<div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
			</div>
		{:else}
			<div class="bg-white rounded-lg p-4 shadow-md">
				<p class="text-gray-800" bind:innerHTML={text} contenteditable="false" />
			</div>
		{/if}
		{#if sender === 'user'}
			<div class="ml-2">
				<svg viewBox="0 0 20 20" fill="currentColor" class="h-6 w-6 text-gray-400">
					<path
						fill-rule="evenodd"
						d="M10 0c-5.523 0-10 4.477-10 10s4.477 10 10 10 10-4.477 10-10-4.477-10-10-10zm2.5 14.5h-5v-1h5v1zm3-3h-8v-1h8v1zm0-3h-8v-1h8v1z"
						clip-rule="evenodd"
					/>
				</svg>
			</div>
		{/if}
	</div>
</div>

<style>
	.lds-ellipsis {
		display: inline-block;
		position: relative;
		width: 80px;
		height: 12px;
	}
	.lds-ellipsis div {
		position: absolute;
		top: 3px;
		width: 10px;
		height: 10px;
		border-radius: 50%;
		background: #444;
		animation-timing-function: cubic-bezier(0, 1, 1, 0);
	}
	.lds-ellipsis div:nth-child(1) {
		left: 8px;
		animation: lds-ellipsis1 0.6s infinite;
	}
	.lds-ellipsis div:nth-child(2) {
		left: 8px;
		animation: lds-ellipsis2 0.6s infinite;
	}
	.lds-ellipsis div:nth-child(3) {
		left: 32px;
		animation: lds-ellipsis2 0.6s infinite;
	}
	.lds-ellipsis div:nth-child(4) {
		left: 56px;
		animation: lds-ellipsis3 0.6s infinite;
	}
	@keyframes lds-ellipsis1 {
		0% {
			transform: scale(0);
		}
		100% {
			transform: scale(1);
		}
	}
	@keyframes lds-ellipsis3 {
		0% {
			transform: scale(1);
		}
		100% {
			transform: scale(0);
		}
	}
	@keyframes lds-ellipsis2 {
		0% {
			transform: translate(0, 0);
		}
		100% {
			transform: translate(24px, 0);
		}
	}
</style>
<script lang="ts">
	import { onMount } from 'svelte';
	import Message from '$lib/components/Message.svelte';

	let text = '';
	let result = '';
	let messagesDiv: HTMLDivElement;

	let messages = [
		{
			text: "Hi, ask me anything!",
			sender: 'gpt',
			loading: false
		}
	];

	const onSubmit = async () => {
		let userText = text;
		text = '';
		messages = [
			...messages,
			{
				text: userText,
				sender: 'user',
				loading: false
			}
		];
		messages = [
			...messages,
			{
				text: 'Thinking...',
				sender: 'gpt',
				loading: true
			}
		];
		setTimeout(() => {
			messagesDiv.scrollBy(0, messagesDiv.scrollHeight - messagesDiv.clientHeight + 100);
		}, 0);

		const response = await fetch('/api/chat', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				query: userText,
			})
		});

		let res = await response.json();
		result = res.result;
		messages = messages.slice(0, -1);
		messages = [
			...messages,
			{
				text: await result,
				sender: 'gpt',
				loading: false
			}
		];
		if (res) {
			setTimeout(() => {
				messagesDiv.scrollBy(0, messagesDiv.scrollHeight - messagesDiv.clientHeight + 100);
			}, 0);
		}

		console.log(result);
	};


	let imageUrl = '';
	let prediction: string = "";
	let error:string = "";

	const classifyImage = async () => {
		try {
			const response = await fetch('http://127.0.0.1:8000/predict', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ image: imageUrl })
			});

			const data = await response.json();
            console.log(data);
			prediction = data.prediction;
			error = "";
		} catch (err) {
			prediction = "";
			error = 'Error occurred while classifying the image.';
			console.error(err);
		}
	};

	
	onMount(() => {
		messagesDiv.scrollBy(0, messagesDiv.scrollHeight - messagesDiv.clientHeight);
	});
</script>

<main>
	<h1>Image Classifier</h1>

	<div>
		<label for="imageUrl">Image URL:</label>
		<input bind:value={imageUrl} type="text" id="imageUrl" />

		<button on:click={classifyImage}>Classify</button>
	</div>

	{#if prediction !== ""}
		<p>Prediction: {prediction}</p>
	{/if}

	{#if error !== ""}
		<p style="color: red;">Error: {error}</p>
	{/if}


	<h1>Chatbot</h1>
	<div class="min-h-screen text-primary-50">

		<div
		class="mx-auto flex w-[min(86rem,95%)] flex-col items-center justify-center h-screen max-h-screen bg-slate-100 relative"
	>
		<div class="w-full absolute inset-0 top-10 max-h-[85%] h-[85%]">
			<div bind:this={messagesDiv} class="flex-col flex overflow-auto overflow-x-hidden h-full">
				{#each messages as message}
					<Message text={message.text} sender={message.sender} loading={message.loading} />
				{/each}
			</div>
			
		</div>
		<div class="w-2/3 mx-auto flex absolute inset-x-0 bottom-10">
			<textarea
				name=""
				id=""
				cols="30"
				rows="10"
				bind:value={text}
				class="items-top h-14 w-full resize-none rounded-md border-2 p-3 pb-0 text-lg transition-all duration-300 ease-in-out placeholder:italic focus:outline-none"
				on:keydown={(e) => {
					if (e.key === 'Enter') {
						e.preventDefault();
						onSubmit();
						text = '';
					}
				}}
			/>
			<button
				on:click={onSubmit}
				class="mx-4 flex items-center justify-center rounded-md border-2 border-primary-900 px-4 text-lg transition-all duration-200 bg-white"
				>Submit</button
			>
		</div>
	</div>

	</div>
</main>

<style>
	main {
		text-align: center;
		margin-top: 50px;
	}

	input {
		margin-right: 10px;
	}
</style>

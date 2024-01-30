<script lang="ts">
	import { onMount } from 'svelte';

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
		imageUrl = 'https://example.com/your_image.jpg'; // Replace with your image URL
		classifyImage();
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

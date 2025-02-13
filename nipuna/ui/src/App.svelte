<script>
    import "./app.css"
    import { onMount } from "svelte";

    let textColor = "#ff0000"; // Initial color
    let colors = ["#ff0000", "#00ff00", "#0000ff", "#ff00ff"];
    let index = 0;

    onMount(() => {
        const interval = setInterval(() => {
        textColor = colors[index];
        index = (index + 1) % colors.length;
        }, 1000); // Change color every 1 second

        return () => clearInterval(interval); // Cleanup on destroy
    });
</script>

<div class="absolute left-1/2 top-1/2 translate-y-1/2 -translate-x-1/2 ">
    <p class="text-blue-600 text-6xl text-center color-text" style="color: {textColor};">Nipuna(Expert) Agents
    </p>
    <p class="text-2xl color-text" style="color: {textColor};">
        Declarative Framework on Steroids to Create, Run and Deploy AI Agents at Scale.
    </p>
    </div>
<div class="absolute left-1/2 top-3/4 -translate-x-1/2 text-2xl text-red-800 color-text" style="color: {textColor};">Coming Soon</div>
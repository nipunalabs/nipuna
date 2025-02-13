<!-- <script type="ts">
  import { writable } from 'svelte/store';
  
  // Define available components
  const components = [
      { type: 'text', name: 'Text', icon: 'T' },
      { type: 'button', name: 'Button', icon: 'ⓑ' },
      { type: 'input', name: 'Input', icon: 'ⓘ' },
      { type: 'container', name: 'Container', icon: '◫' }
  ];

  // Store for canvas elements
  const elements = writable([]);
  let selectedElement = writable(null);
  let draggedType = null;
  
  // Handle drag start
  function handleDragStart(event, type) {
      draggedType = type;
  }

  // Handle drop
  function handleDrop(event) {
      const rect = event.currentTarget.getBoundingClientRect();
      const newElement = {
          id: Date.now(),
          type: draggedType,
          x: event.clientX - rect.left - 50,
          y: event.clientY - rect.top - 25,
          properties: {
              text: 'New Element',
              color: '#000000',
              backgroundColor: '#ffffff',
              fontSize: 16,
              width: 100,
              height: 50
          }
      };
      elements.update(items => [...items, newElement]);
  }

  // Handle element click
  function selectElement(element) {
      selectedElement.set(element);
  }
</script>

<style>
  .builder {
      display: flex;
      height: 100vh;
      font-family: Arial, sans-serif;
  }

  .toolbar {
      width: 200px;
      background: #f0f0f0;
      padding: 20px;
      border-right: 1px solid #ccc;
  }

  .component-item {
      padding: 10px;
      margin: 5px;
      background: white;
      border: 1px solid #ccc;
      cursor: move;
      user-select: none;
  }

  .canvas {
      flex: 1;
      padding: 20px;
      background: #f8f8f8;
      position: relative;
  }

  .element {
      position: absolute;
      border: 1px solid transparent;
      transition: all 0.2s;
  }

  .element.selected {
      border: 2px solid #2196F3;
  }

  .properties-panel {
      width: 300px;
      background: #f0f0f0;
      padding: 20px;
      border-left: 1px solid #ccc;
  }

  .property-item {
      margin: 10px 0;
  }

  label {
      display: block;
      margin-bottom: 5px;
  }
</style>

<div class="builder">
  <!-- Left Toolbar -->
  <!-- <div class="toolbar">
      <h2>Components</h2>
      {#each components as component}
          <div class="component-item" 
               draggable="true"
               on:dragstart={() => handleDragStart(event, component.type)}>
              {component.icon} {component.name}
          </div>
      {/each}
  </div> -->

  <!-- Main Canvas -->
  <!-- <div class="canvas" 
       on:drop={handleDrop}
       on:dragover|preventDefault>
      {#each $elements as element (element.id)}
          <div class="element {element === $selectedElement ? 'selected' : ''}"
               style="left: {element.x}px; top: {element.y}px;
                      width: {element.properties.width}px;
                      height: {element.properties.height}px;
                      font-size: {element.properties.fontSize}px;
                      color: {element.properties.color};
                      background-color: {element.properties.backgroundColor}"
               on:click={() => selectElement(element)}>
              {#if element.type === 'text'}
                  {element.properties.text}
              {:else if element.type === 'button'}
                  <button>{element.properties.text}</button>
              {:else if element.type === 'input'}
                  <input type="text" placeholder={element.properties.text} />
              {:else if element.type === 'container'}
                  <div style="width: 100%; height: 100%; border: 1px dashed #666"></div>
              {/if}
          </div>
      {/each}
  </div> -->

  <!-- Right Properties Panel -->
  <!-- {#if $selectedElement}
      <div class="properties-panel">
          <h2>Properties</h2>
          <div class="property-item">
              <label>Text</label>
              <input type="text" bind:value={$selectedElement.properties.text}>
          </div>
          <div class="property-item">
              <label>Font Size</label>
              <input type="range" min="12" max="48" 
                     bind:value={$selectedElement.properties.fontSize}>
          </div>
          <div class="property-item">
              <label>Color</label>
              <input type="color" bind:value={$selectedElement.properties.color}>
          </div>
          <div class="property-item">
              <label>Background</label>
              <input type="color" bind:value={$selectedElement.properties.backgroundColor}>
          </div>
          <div class="property-item">
              <label>Width</label>
              <input type="number" bind:value={$selectedElement.properties.width}>
          </div>
          <div class="property-item">
              <label>Height</label>
              <input type="number" bind:value={$selectedElement.properties.height}>
          </div>
      </div>
  {/if}
</div> -->

<div>Welcome to Nipuna Labs</div>
# Custom Clip

Diffusion Studio functionality can be extended using custom `Clip` objects. In this guide, we will walk through the steps of creating a custom `Clip` object using and rendering it to the canvas. Before diving into the example, let's first discuss the lifecycle of a `Clip` object.

## Clip Lifecycle

When `Clip` objects are rendered to the canvas, they pass through several key phases:

### Constructor

The `constructor()` method is invoked first, during the initialization of the clip. This is where the initial state and values should be set up.

The method receives `props` as arguments, and you must always call `super(props)` to ensure the base class is properly initialized.

### Init

The `init()` method is called asynchronously before the `Clip` is added to a track/composition. This makes it the ideal place for I/O operations, such as fetching assets or loading buffers.

### Enter

This method is triggered right before the `Clip` is drawn to the canvas. Use `enter()` to perform any synchronous actions that need to be executed once, rather than on every render cycle.

### Update

The `update()` method is called on every redraw of the clip. It receives a `Timestamp` argument, which you can use to implement time-based state changes. The `update()` function may also return a promise—this is useful during video export to ensure frame accuracy. However, for playback, promises are not awaited to maintain smooth performance.

### Render

The `render()` method is called on every redraw of the clip. It receives a `Renderer` and `Timestamp` argument, which you can use to implement time-based state changes.

### Exit

This method is called after the `Clip` has been drawn to the canvas for the last time. It is commonly used to perform cleanup operations, such as removing filters or other resources to free memory.

## Example: Custom Alien Clip

This example is inspired by the [Pixi.js Texture Swap](https://pixijs.com/8.x/playground?exampleId=sprite.textureSwap) guide. You can refer to it for additional insights.

```typescript
import * as core from '@diffusionstudio/core';

// Define custom Clip properties extending `ClipProps`, such as start, stop, etc.
interface AlienClipProps extends core.ClipProps {
  speed?: number;  // Optional speed property
}

// Create a new class extending `Clip` and apply your custom properties
class AlienClip extends core.Clip {
  // Declare custom fields
  public speed = 0.2;
  public image = new Image();

  public constructor(props: AlienClipProps = {}) {
    // Ensure parent class `Clip` is properly initialized
    super(props);

    // Assign provided properties to the Clip instance
    Object.assign(this, props);
  }

  // Initialize the clip, typically used for loading assets asynchronously
  public override async init(): Promise<void> {
    this.image.crossOrigin = 'anonymous';
    this.image.src = 'https://pixijs.com/assets/flowerTop.png';
    await new Promise(resolve => this.image.onload = resolve);
  }

  // Enter phase: invoked when the clip is about to be drawn to the canvas
  public override enter(): void {
    // No specific actions in this example, but can be used for one-time setup
  }

  // Update the clip's state on each frame. Receives a `Timestamp` argument.
  public override update(renderer: core.Renderer, time: core.Timestamp): void | Promise<void> {
    // This can be useful for computationally expensive operations.
  }

  public override render(renderer: core.Renderer, time: core.Timestamp): void {
    const x = this.track!.composition!.width / 2;
    const y = this.track!.composition!.height / 2;

    // Adjust the sprite's angle based on elapsed time and configured speed
    const angle = time.frames * this.speed;

    renderer.ctx.save();
    renderer.ctx.translate(x, y);
    renderer.ctx.rotate(angle);
    renderer.ctx.drawImage(this.image, -this.image.width / 2, -this.image.height / 2);
    renderer.ctx.restore();
  }

  // Exit phase: invoked when the clip is no longer needed
  public override exit(): void {
    // Cleanup resources (e.g., removing filters)
  }
}
```

### Adding the Clip to a Composition

To include this `AlienClip` in a composition, you can do the following:

```typescript
const composition = new core.Composition();

// Add the custom AlienClip to the composition
await composition.add(new AlienClip({ speed: 0.4, duration: 150 }));
```

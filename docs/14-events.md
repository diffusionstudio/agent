# Events

Diffusion Studio is built around an event-driven architecture, making it essential to understand how events work within the library. Events play a significant role in how you interact with key components such as **Composition**, **Track**, and **Clip**. We've tailored our event system to be compatible with modern frontend frameworks like React, providing a seamless development experience.

### Composition Events

In Diffusion Studio, the **Composition** emits various events related to playback control, similar to those found in many editing applications:

```typescript
const composition = new core.Composition();

composition.on('currentframe', (event) => {
  // Logs the current frame of the playback
  console.log(event.detail);
});

// Logs a CustomEvent when playback starts
composition.on('play', console.log);

// Logs a CustomEvent when playback stops
composition.on('pause', console.log);
```

As with vanilla JavaScript's `CustomEvent`, you can access the object that triggered the event using `event.currentTarget`.

### Track Events

A **Track** automatically bubbles up events from its clips. Instead of subscribing to individual clip events, you can listen for the same events directly on the Track.

In addition to clip events, Tracks also emit `attach` and `detach` events when they are added to or removed from a **Composition**:

```typescript
track.on('attach', console.log);
track.on('detach', console.log);
```

### Clip Events

Clips represent individual media assets, and you can subscribe to various events that indicate changes or updates:

```typescript
clip.on('frame', console.log);
clip.on('update', console.log);
```

These events are triggered when the clip's position on the timeline changes or when a visual update occurs. 

<Callout>**Tip:** If you want to catch all events from a clip, you can subscribe to all events at once using the wildcard: `clip.on('*', console.log);`</Callout>

## Unsubscribing from Events

The `on` method returns an event ID, which you can use to unsubscribe from events when they are no longer needed:

```typescript
const attachEvt = clip.on('attach', console.log);
const detachEvt = clip.on('detach', console.log);

clip.off(attachEvt);
clip.off(detachEvt);
```

## Waiting for Events

Diffusion Studio provides a convenient way to wait for specific events to occur, which is particularly useful in asynchronous workflows:

```typescript
await new Promise(clip.resolve('load'));
```

This code will pause execution until the `load` event is triggered, ensuring that the clip has been fully loaded before proceeding.

# Composition

A `Composition` object manages the entire state of a video project and serves as the foundation for any video editing tasks in Diffusion Studio. This guide will walk you through setting up and manipulating a `Composition` object.

## Setting Up a Composition

To begin, import the `Composition` class from `@diffusionstudio/core` and create a new instance:

```typescript
import { Composition } from '@diffusionstudio/core';

const composition = new Composition();
```

When constructing a `Composition`, you can pass various options. Here are the default values:

```typescript
{
  height: 1080,
  width: 1920,
  background: '#000000'
}
```

The specified `height` and `width` define the canvas size, but these do not dictate the final video resolution, which can be configured with the Encoder. 

You can always change the `width` and `height` of the `Composition` after its creation using the `resize` method.

## Visualizing the Composition

To display the `Composition` within your application, you can attach it to a DOM element. The example below shows how to center the player inside a container and scale it according to the available space:

import { Tab, Tabs } from 'fumadocs-ui/components/tabs';

<Tabs items={["TypeScript", "HTML", "CSS"]}>
```typescript tab="TypeScript"
const container = document.getElementById('player-container') as HTMLDivElement;
const player = document.getElementById('player') as HTMLDivElement;

composition.mount(player);

const scale = Math.min(
  container.clientWidth / composition.width,
  container.clientHeight / composition.height,
);

player.style.width = `${composition.width}px`;
player.style.height = `${composition.height}px`;
player.style.transform = `scale(${scale})`;
player.style.transformOrigin = 'center';
```

```html tab="HTML"
<div id="player-container">
  <div id="player"></div>
</div>
```

```css tab="CSS"
#player-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```
</Tabs>

This setup ensures that the player is centered and scales to fit within the `player-container` while maintaining the aspect ratio of the `Composition`. For production environments, consider using a [ResizeObserver](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver) to handle dynamic resizing based on your specific needs.

> **Note:** Since the canvas cannot be added as a child of two different elements, you must remove it from the player before attaching it to another element:
```typescript
composition.unmount();
```

## Changing the Composition State

Here are some common state manipulations you might perform on a `Composition`:

### **Setting the Composition Duration**

By default, a `Composition`'s duration is determined by the last visible clip. However, you can assign a fixed duration using the duration setter:

```typescript
composition.duration = 300; // Sets the duration to 300 frames or 10 seconds
```

### **Adding Tracks**

For efficient usage, manually manipulate the `Tracks` in your `Composition`:

```typescript
const track = composition.createTrack('video');
// equivalent to
const track = composition.insertTrack(VideoTrack);
```

Alternatively, you can create a `Track` instance beforehand and then prepend it:

```typescript
const track = new VideoTrack();
// add clips beforehand
composition.insertTrack(track);
```

> You can remove the track again by calling `composition.removeTrack(track)`

### **Adding Clips**

The `Composition` offers a convenient method to create a `Track` and append a `Clip` to it:

```typescript
const clip = new VideoClip();
await composition.add(clip);
```

`add` is always an asynchronous action because it waits until the `Clip` can be visualized.

### **Finding Tracks and Clips**

If you need to search for specific tracks or clips and no direct reference is available, use the following methods:

```typescript
const tracks = composition.findTracks(track => track.id == 'some_uuid'); 
const clips = composition.findClips(clip => clip.name == 'some_name');
// Use .at(0) to get the first occurrence
```

There are also shorthand notations for finding specific types of tracks and clips:

```typescript
const tracks = composition.findTracks(TextTrack);
const clips = composition.findClips(TextClip);
```

### **Taking Screenshots**

To capture a screenshot of the current frame:

```typescript
composition.frame = 30;
const dataUrl = await composition.screenshot();
```

### **Playback Controls**

The most essential playback features are easily accessible through the `Composition`:

```typescript
await composition.play();
await composition.pause();
await composition.seek(30);
```

> **Hint:** Use the `composition.time()` function to conveniently display the current time of the `Composition`.

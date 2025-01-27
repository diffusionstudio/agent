# Rendering

Rendering videos on the client side is made highly efficient by utilizing WebCodecs, a modern browser API that supports hardware-accelerated encoding. This allows for fast and optimized video processing directly in the browser.

## Setup

To begin, you'll need a `Composition` to render. Below is an example of setting up an empty `Composition` for demonstration purposes:

```typescript
import * as core from '@diffusionstudio/core';

const composition = new core.Composition();
```

Next, create an encoder using the `Composition`:

```typescript
const encoder = new core.Encoder(composition);
```

## Configuring the Encoder

The encoder can be customized via its second argument, which allows you to configure various output settings. The default configuration is as follows:

```typescript
{
  resolution: 1,        // Scales the dimensions of the output.
  sampleRate: 48000,    // Defines the audio sample rate; higher values improve audio quality.
  numberOfChannels: 2,  // Specifies the number of audio channels.
  videoBitrate: 10e6,   // Sets the video bitrate; higher values yield better quality.
  gpuBatchSize: 5,      // Defines the workload for the GPU.
  fps: 30,              // Sets the output frame rate.
  debug: false,         // Enables logging of rendering performance.
  watermark: string,    // Adds a simple text watermark to the video.
}
```

For example, to produce a 4K video at 60 FPS from a default 1080p `Composition`, you can configure the encoder like this:

```typescript
const encoder = new core.Encoder(composition, {
  fps: 60,
  resolution: 2,
});
```

## Rendering the Video

To start exporting the video, use the `render` method, which accepts a render target as an argument. The recommended approach is to use the `showSaveFilePicker` API:

```typescript
const fileHandle = await window.showSaveFilePicker({
  suggestedName: 'untitled_video.mp4',
  types: [
    {
      description: 'Video File',
      accept: { 'video/mp4': ['.mp4'] },
    },
  ],
});

await encoder.render(fileHandle);
```

This approach writes the MP4 chunks directly to disk as they are generated, allowing you to render videos that exceed your available RAM. However, note that browser support for `showSaveFilePicker` is currently limited. In such cases, other export targets can be used:

```typescript
const blob = await encoder.render();            // Returns the video as a Blob.
await encoder.render('myVideo.mp4');            // Downloads the result with a specified name.
await encoder.render((data: Uint8Array, position: number) => {
  console.log(data, position)
});                                             // Streams the video to a callback.
```

To ensure compatibility across browsers, you can provide a fallback for `showSaveFilePicker`:

```typescript
if (!('showSaveFilePicker' in window)) {
  Object.assign(window, { showSaveFilePicker: async () => 'myVideo.mp4' });
}
```

This fallback ensures that the export process continues seamlessly even if `showSaveFilePicker` is not available.

## Aborting the export

This feature was implemented utilizing the `AbortController` Web API. You can simply pass in the abort signal as the second argument of the render method:

```typescript
const controller = new AbortController();

encoder.render(fileHandle, controller.signal);

controller.abort();
```

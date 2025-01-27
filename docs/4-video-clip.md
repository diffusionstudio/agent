# Video Clip

This guide provides a comprehensive overview of manipulating videos and exporting the final product.

## Adding and Manipulating Video

### Loading a Video Source

To add a video, you need a `VideoClip` and a `VideoSource`. You can create a `VideoSource` from a file or an external URL. Here, we will use a URL:

```typescript
import * as core from '@diffusionstudio/core';

const source = await core.VideoSource.from('https://diffusion-studio-public.s3.eu-central-1.amazonaws.com/videos/big_buck_bunny_1080p_30fps.mp4');
```

A `VideoSource` is a reusable reference that can be shared across multiple clips, optimizing memory usage.

### Creating a Video Clip

Now, create a `VideoClip` from the `VideoSource`:

```typescript
const video = new core.VideoClip(source, { // also accepts new File(...)
  position: 'center', // ensures the clip is centered
  height: '100%', // stretches the clip to the full height
}); 
```

> Note: By not setting width to 100%, the video will maintain its original aspect ratio.

### Performing Video Manipulations

You can perform various manipulations on the `VideoClip`:

```typescript
video
  .offset(-30) // time offset in frames (relative to current offset)
  .subclip(0, 180); // trims the clip from start to end frames
```

This sets the video's delay to `-30 frames` at `30 FPS`, resulting in a 5-second visible clip (`180 - 30 = 150 frames`). The video is centered and scaled to fill the entire composition. Specifying either height or width maintains the aspect ratio, while setting both does not.

### Adding the Clip to the Composition

Add the clip to the composition:

```typescript
await composition.add(video);
```

Alternatively, if adding multiple clips to the same track, use:

```typescript
const track = composition.createTrack('video');
await track.add(video);
```

The `add` method is asynchronous, ensuring the clip is fully loaded before proceeding.

## Using Realtime Playback

The composition provides various realtime playback options:

```typescript
composition.play(); // start playback
composition.pause(); // pause playback
composition.seek(120); // seek to a specific frame
composition.time(); // get human-readable time (e.g., 00:04 / 00:05)
composition.on('currentframe', console.log); // log frame events
```

## Exporting the Composition

To export the composition, use the `Encoder`:

```typescript
const encoder = new core.Encoder(composition);
```

You can customize the render settings with the second argument of the `Encoder` constructor. For example, to render at 4K resolution and 25 FPS:

```typescript
const encoder = new core.Encoder(composition, { resolution: 2, fps: 25 });
```

Export the video with the `render` method:

```typescript
await encoder.render('myVideo.mp4'); // specifies a filename
```

### Using the `showSaveFilePicker` API

The recommended method for client-side export is using `showSaveFilePicker`:

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

This writes the MP4 chunks directly to disk, allowing the export of large files while consuming minimal RAM.

### Full Example

Here is a complete example putting everything together:

```typescript
import * as core from '@diffusionstudio/core';

const composition = new core.Composition();

const player = document.getElementById('player') as HTMLDivElement;
composition.attachPlayer(player);

const source = await core.VideoSource.from('https://diffusion-studio-public.s3.eu-central-1.amazonaws.com/videos/big_buck_bunny_1080p_30fps.mp4');

const video = new VideoClip(source, {
    position: 'center',
    height: '100%',
    width: '100%',
})
  .offset(-30)
  .subclip(0, 180);

await composition.add(video);

const encoder = new core.Encoder(composition, { resolution: 2, fps: 25 });
await encoder.render('myVideo.mp4');
```

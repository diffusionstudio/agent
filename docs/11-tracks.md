# Tracks

Tracks serve as an abstraction layer in Diffusion Studio, providing three key functionalities:

1. **Efficient Clip Rendering:** Tracks determine which clips will be rendered, enabling the software to bypass unnecessary iterations over non-visible clips. Only visible clips within the track are processed.

2. **Layering Control:** Tracks define the layering order of visible elements. The `Track` at index 0 will be rendered last, meaning it appears on top of other tracks.

3. **Clip Management:** Tracks manage the clips' lifecycle, including initialization, adding, removing, and updating clips.

### Track Types and Creation

Similar to clips, tracks are typed. For instance, you can create a `TextTrack`, which is designed to hold only `TextClips` or classes derived from `TextClip` (e.g. `RichTextClip`):

```typescript
import { TextTrack } from '@diffusionstudio/core';

const track = new TextTrack();
```

You can now add clips to the track, but it's important to note that clips cannot overlap.

```typescript
await track.add(
  new TextClip({
    text: 'Hello',
    delay: 0, // Default delay
    duration: 30,
  })
);

await track.add(
  new TextClip({
    text: 'World',
    delay: 31,
    duration: 60,
  })
);
```

If clips overlap, Diffusion Studio will automatically adjust the start/stop times or move the clip to a different track. The `add` method is asynchronous because Diffusion Studio waits until the clip is fully initialized before adding it to the track.

You can render a track by adding it to a composition:

```typescript
import { Composition } from '@diffusionstudio/core';

const composition = new Composition();

composition.insertTrack(track);
```

> By calling `track.remove(clip)` you can remove a `Clip` from the `Track`

### Stack Mode

Tracks can also be configured to operate in *stack mode*, which ensures that each new clip added starts exactly where the previous clip ended (plus 1 millisecond). Stack mode can be enabled as follows:

```typescript
track.stacked(); // disable with track.stacked(false);
```

### Layering

Let's set up an example to illustrate how tracks are layered:

```typescript
// alterantive approach for creating tracks 
// and adding them to the composition
const video = composition.createTrack('video'); 
const image = composition.createTrack('image');
const text = composition.createTrack('text');
```

When a track is added to the composition it will be added to `position 0` and rendered last. Our `composition.tracks` array looks like this `[TextTrack, ImageTrack, VideoTrack]`. When visualized the text will be rendered on top of the images, which will be rendered on top of all `VideoClip`s inside the `VideoTrack`.

Each `Track` implements the `layer` method which can be used to change the order. It accepts an index or `top | bottom`:

```typescript
video.layer('top');
```

Now `VideoTrack` will be rendered on top of all other tracks.

### Caption Track

The `CaptionTrack` class provides specialized features for managing captions of audio or video clips. 

To begin, you need an `AudioClip` or `VideoClip` with an assigned transcript. For demonstration, we'll use a `MediaClip`, which is a base class for these types:

```typescript
import { Transcript, MediaClip } from '@diffusionstudio/core';

const transcript = new Transcript(); // Assume this is populated with data

const clip = new MediaClip({ transcript });
```

You can then create captions from the `MediaClip` using a `CaptionTrack`:

```typescript
await composition
  .createTrack('caption') // creates CaptionTrack
  .from(clip)             // sets the source
  .createCaptions();      // generates text clips from the source
```

The `createCaptions` method supports various caption presets.

One advantage of linking the `CaptionTrack` to a `MediaClip` is that captions will automatically adjust when you move the clip using `offset()`.

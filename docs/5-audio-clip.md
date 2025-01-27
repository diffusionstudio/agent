# Audio Clip

This guide will walk you through the steps of splitting an audio file into multiple clips, offsetting the start time of each clip, and trimming them.

## Manual Approach

### Setup

First, let's fetch an MP3 file of a piano recording and create an audio clip from it:

```typescript
import * as core from '@diffusionstudio/core';

const source = await core.AudioSource.from('https://diffusion-studio-public.s3.eu-central-1.amazonaws.com/audio/piano.mp3');

const clip0 = await composition.add(new core.AudioClip(source));
```

> **Hint:** The MP3 file contains 16 seconds of audio.

### Splitting the `AudioClip`

Splitting a clip creates a new copy of the clip that starts 1 millisecond after the specified split time (in frames). The original clip is shortened to end at the split time.

```typescript
const clip1 = await clip0.split(240);
```

In this example, `240` represents the midpoint of the audio clip.

### Manipulating the Clips

We can then manipulate each clip individually:

```typescript
clip0.subclip(15, 80).offset(-15);
```

This code trims the first clip from frame 15 to frame 80 and offsets it by -15 frames, moving it to the start of the composition.

```typescript
clip1
  .subclip(420)
  .offset(-420 + clip0.stop.frames);

clip1.volume = 0.5;
```

For the second clip:
- It is trimmed from frame 420 (14 seconds) to the end of the clip (16 seconds).
- It is offset by `-420` frames to align it with the start of the composition. Since the first clip (`clip0`) already occupies the start position, we adjust the offset by adding the stop frame of the first clip.
- The volume is reduced to 50% for demonstration purposes.

## Automated Approach

To achieve the same result more efficiently, we can use a stacked track:

```typescript
const track = composition.appendTrack(core.AudioTrack).stacked();
await track.add(
  new core.AudioClip(
    await core.AudioSource.from('https://diffusion-studio-public.s3.eu-central-1.amazonaws.com/audio/piano.mp3')
  )
);
```

In this approach:
1. A new track is created and converted to a stacked track using `.stacked()`.
2. An audio clip is appended to the track using the loaded audio source.

### Manipulating the Clips

Using the track reference, we can manipulate the clips without needing to manage individual clip references:

```typescript
await track.clips[0].split(240); // Split the first clip

track.clips[0].subclip(15, 80); // Trim the first clip
track.clips[1].subclip(420);    // Trim the second clip
```

With the stacked track approach, the offsets are automatically handled, making it easier to manage clip positions within the composition.

### Captions

The `AudioClip` (and `VideoClip`) also makes it easy to add captions to your composition. Let's see this in action:

```typescript
clip0.transcript = new core.Transcript(); // Assume this is populated with data

await clip0.createCaptions();
```

First we're adding a transcript to the `AudioClip` we created above. Then we're calling the asynchronous method `createCaptions` on the clip.

> This only works if your clip has been added to the composition ([example](https://github.com/diffusionstudio/examples/blob/f8bde98c53320b8bcd78a541244fc95ff2b40cbd/showcase/src/compositions/custom-captions.ts)).

# Image Clip

The `ImageClip` class, like all static clips (excluding Video & Audio), has a fixed start and stop time.

## Basic Usage

```typescript
import * as core from '@diffusionstudio/core';

const source = await core.ImageSource.from('https://diffusion-studio-public.s3.eu-central-1.amazonaws.com/images/lenna.png');

const image = new core.ImageClip(source, { delay: 20, duration: 100 });

await composition.add(image);
```

You can place an `ImageClip` on the timeline by setting its `delay` and `duration` properties.

## Moving the Clip along the Timeline

Using `offset`:

```typescript
image.offset(-20);
```

This adjustment will make the clip start at frame 0 and end at frame 100, equivalent to:

```typescript
image.delay = 0;
```

Alternatively, you can achieve the same result using the `trim` method:

```typescript
image.trim(0, 100);
```

Which sets the clip's delay to `0` and its duration to `100`.

## Splitting Clips

You can split an `ImageClip` into two clips at a specified frame:

```typescript
const imageNew = image.split(50);
```

This will split the clip at frame 50.

### Notes

1. **Internal Time Representation**: Internally, Diffusion Studio uses milliseconds for timing. Therefore, splitting the initial image clip at frame 50 (assuming 30 FPS) will set the stop time of the initial clip to `round(50/30*1000) = 1667ms` and the start time of the new clip to `1668ms`. This ensures high precision when rendering at different frame rates.

2. **Non-Overlapping Clips**: Since the new image clip (`imageNew`) is part of the same track as the initial clip, you cannot use `imageNew.offset(-50)` to place them visually next to each other. This would violate the rule that clips within the same track cannot overlap. To achieve this, you must first remove the new clip from the track:

```typescript
imageNew.detach();
```

Then add it to a new track:

```typescript
composition.add(imageNew.offset(-50));
```

By following these steps, you can manage and manipulate image clips effectively within your composition.

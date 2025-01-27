# Migration Guide: V1 to V2

This guide outlines the changes and steps required to migrate from Diffusion Studio Core V1 to V2.

## Major Changes Overview

### Removal of Pixi.js
- Pixi.js and Pixi Filters have been removed to optimize performance for automation workloads
- The library now uses a custom rendering implementation inspired by Pixi.js
- This change significantly reduces the library size and improves performance for large-scale operations

### New Core Components

#### Renderer
- New abstraction layer for the 2D Canvas Context API
- Replaces Pixi.js rendering system

#### Ticker
- Updates composition every 200ms
- Runs at desired framerate during playback
- Automatically inactive in headless environments

### New Components
- **New Clips**: 
  - `WaveformClip`
  - `RectangleClip`
  - `CircleClip`
- **New Tracks**: 
  - `ShapeTrack`

Example of using new shape components:
```typescript
import { RectangleClip, ShapeTrack } from '@diffusionstudio/core'

const shapeTrack = new ShapeTrack()
const rectangle = new RectangleClip({
  width: 100,
  height: 100,
  fill: '#ff0000',
  radius: 10,
  duration: 5
})

await shapeTrack.add(rectangle)
```

## Breaking Changes

### Composition Changes
```diff
- Composition.settings.backend
# This property has been removed

- Composition.attachPlayer(div)
+ Composition.mount(div)

- Composition.detachPlayer(div)
+ Composition.unmount()

- Composition.shiftTrack()
+ Composition.insertTrack()
```

Example of updated composition usage:
```typescript
// V1
const composition = new Composition()
composition.attachPlayer(element)
composition.shiftTrack(track)

// V2
const composition = new Composition()
composition.mount(element)
composition.insertTrack(track) // Accepts position as second argument
```

### Track Changes
```diff
- CaptionTrack.generate()
+ CaptionTrack.createCaptions()
```

Example of caption track changes:
```typescript
// V1
const captions = await captionTrack.from(audioClip).generate()

// V2
const captions = await captionTrack.from(audioClip).createCaptions()
```

### Clip Changes
```diff
# Timing Properties
- clip.start
+ clip.delay

- clip.stop
+ clip.duration

- clip.set()
# This method has been removed

# New Property
+ clip.trim()
# Equivalent to setting start and stop in V1

# Filter Changes
- clip.filters // Previously Pixi filters
+ clip.filter // Now accepts 2D Canvas Context API filters as string

# Mask Changes
- clip.mask // Previous implementation
+ clip.mask // New mask objects

# Animation Changes
- Individual property Keyframes
+ clip.animations // New animations array
```

Example of animation changes:
```typescript
// V1 - Individual keyframes per property
clip.x = new Keyframe([80], [960])
clip.width = new Keyframe([60], [1000])

// V2 - Centralized animations array
clip.animations = [
  {
    key: 'x',
    frames: [{ frame: 80, value: 960 }]
  },
  {
    key: 'width',
    frames: [{ frame: 60, value: 1000 }]
  }
]
```

Example of updated clip timing:
```typescript
// V1
clip.start = 2
clip.stop = 7

// V2
clip.delay = 2
clip.duration = 5 // Note: Now using duration instead of end time

// New trim functionality
clip.trim(2, 7) // Equivalent to V1's start/stop
```

Example of new filter syntax:
```typescript
// V1
clip.filters = new BlurFilter(5)

// V2
clip.filter = 'blur(5px)'

// Multiple filters
clip.filter = 'blur(5px) brightness(150%)'
```

### Media Clip Changes
```diff
- MediaClip.offset
# This property has been removed

- MediaClip.offsetBy()
+ MediaClip.offset()

- MediaClip.addCaptions()
+ MediaClip.createCaptions()
```

Example of media clip changes:
```typescript
// V1
mediaClip.offsetBy(2)
await mediaClip.addCaptions()

// V2
mediaClip.offset(2)
await mediaClip.createCaptions()
```

### Audio Clip Changes
```diff
- AudioClip.sample()
# has been removed

- AudioClip.fastsampler()
+ AudioClip.sample()
```

### Text Changes
```diff
- ComplexTextClip
+ RichTextClip
```

### Other Changes
```diff
- CanvasEncoder
# This component has been removed

- Font
+ FontManager
# Now supports loading and managing multiple fonts
```

Example of font management:
```typescript
// V1
const font = await Font.load({
  family: 'Arial',
  weight: 400,
  source: 'arial.ttf'
})

// V2
const fontManager = new FontManager()
const font = await fontManager.load({
  family: 'Arial',
  weight: 400,
  source: 'arial.ttf'
})

// or

const font = FontManager.load({
  family: 'Arial',
  weight: 400,
  source: 'arial.ttf'
})
```

### Encoder Changes
When no target is provided, the render method returns a Blob. It's no longer possible to upload
the array buffer to a remote server. Additionally, a Stream callback can now be provided.

```diff
# V1
- await new Encoder(...).render()

# V2
- await new Encoder(...).render()
+ const blob = await new Encoder(...).render()

# V1
- await new Encoder(...).render('https://example.com/location/file.mp4')

# V2
+ const blob = await new Encoder(...).render()
+ await fetch(url, {
+    method: 'PUT',
+    headers: {
+      'Content-Type': 'video/mp4',
+    },
+    body: blob
+ });

# V2
+ await new Encoder(...).render((data: Uint8Array, position: number) => {
+   console.log(data, position)
+ })
```

## Duration Behavior Changes

- `MediaClip.duration` now returns the clipped duration
- Use `AudioSource.duration` to get the original duration

Example of duration handling:
```typescript
// V1
mediaClip.start = 2
mediaClip.stop = 62
const duration = mediaClip.duration // Sets full duration

// V2
const fullDuration = mediaClip.source.duration // Original duration
mediaClip.duration = 60 // Set clip duration directly, will trim to 60 frames
```

## Getting Help

If you need assistance with the migration or have questions about specific changes:
- Join our Discord community for support
- Refer to the TypeScript types for detailed property information
- Check the updated documentation for new features and APIs 

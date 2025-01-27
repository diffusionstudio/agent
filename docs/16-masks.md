# Masks

Masks are essential tools to crop, hide, or emphasize specific parts of your video. Here, we will demonstrate how to use the `RectangleMask` and how to apply it to a video clip.

## What is a Mask?

A mask defines a specific region within a composition where content can be displayed. It is a powerful feature to control visibility and apply creative effects. This guide will focus on the `RectangleMask`, but similar principles apply to other masks like `CircleMask`.

---

## Example: Using `RectangleMask`

To get started, we will create a composition, define a `RectangleMask`, and apply it to a video clip.

### Code Example

```typescript
import * as core from '@diffusionstudio/core';
// Step 1: Create a composition
const composition = new core.Composition();

// Step 2: Define a RectangleMask
const mask = new core.RectangleMask({
  x: 480, // Horizontal offset
  y: 0,   // Vertical offset
  width: composition.width - 960, // Mask width
  height: composition.height,     // Mask height
  radius: 100,                    // Corner radius for rounded edges
});

// Step 3: Add a video clip with the mask applied
await composition.add(
  new core.VideoClip(new File([], 'sample.mp4'), {
    position: 'center', // Center the video in the composition
    muted: true,        // Mute the video
    mask,               // Apply the mask
    height: '100%',     // Set the height of the video
  })
);
```

### Key Parameters

- **`x` and `y`**: Define the top-left corner of the mask.
- **`width` and `height`**: Set the size of the mask relative to the composition.
- **`radius`**: Adds rounded corners to the mask.

---

## Next Steps

- Explore other mask types, like `CircleMask`, for additional creative possibilities.
- Combine masks with animation properties to create dynamic transitions and effects.
- Review the full API documentation for advanced customization options.

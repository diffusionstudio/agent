# Keyframe Animations

With Diffusion Studio, you can easily create complex animations by defining how properties of an object change over time using **keyframes**.

This guide will show you how to create and apply keyframe animations to a rectangle using the `core.RectangleClip` class.

## Keyframe Animation Basics

In the animation system, you define animations by specifying:
- **Key**: The property of the object to animate (e.g., `x`, `width`, `height`, `fill`).
- **Easing**: The interpolation method between frames (e.g., `ease-in-out`).
- **Frames**: The sequence of frames where the property changes. Each frame is defined with a `frame` number and a `value`.
- **Extrapolate** *(Optional)*: Defines how the property behaves outside the defined keyframes (e.g., `clamp` or `extend`).

### Example: Animating a Rectangle

Here’s an example of animating a rectangle’s position, size, and color:

```typescript
new core.RectangleClip({
  animations: [
    {
      key: 'x', // Animates the x-position
      easing: 'ease-in-out', // Smooth transition
      extrapolate: 'clamp', // Values outside keyframes are clamped
      frames: [
        { frame: 80, value: 960 }, // At frame 80, x = 960
        { frame: 120, value: 50 }, // At frame 120, x = 50
      ],
    },
    {
      key: 'width', // Animates the width
      easing: 'ease-out',
      frames: [
        { frame: 0, value: 0 }, // At frame 0, width = 0
        { frame: 60, value: 1000 }, // At frame 60, width = 1000
        { frame: 120, value: 60 }, // At frame 120, width = 60
      ],
    },
    {
      key: 'height', // Animates the height
      easing: 'ease-in',
      frames: [
        { frame: 0, value: 0 }, // At frame 0, height = 0
        { frame: 60, value: 700 }, // At frame 60, height = 700
        { frame: 120, value: 40 }, // At frame 120, height = 40
      ],
    },
    {
      key: 'fill', // Animates the fill color
      frames: [
        { frame: 0, value: '#FF0000' }, // At frame 0, fill = red
        { frame: 120, value: '#00FF00' }, // At frame 120, fill = green
      ], // will use linear interpolation by default
    }
  ]
});
```

### Key Concepts in the Example

1. **`x` Position Animation**: The rectangle starts at `x = 960` and transitions to `x = 50` between frames 80 and 120.
2. **Width and Height Animations**: These define how the size of the rectangle changes over time:
   - The width starts at 0, peaks at 1000, and then shrinks to 60.
   - The height follows a similar pattern, starting at 0, peaking at 700, and ending at 40.
3. **Color Animation (`fill`)**: The rectangle changes its fill color from red to green over the animation duration.

---

With just a few lines of code, you can bring static graphics to life with rich, keyframe-based animations. Experiment with different properties and easing functions to create stunning effects!

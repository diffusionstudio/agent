# Waveform Clip

The `WaveformClip` in Diffusion Studio allows you to generate visually appealing and customizable waveform visualizations for audio files. This guide will walk you through the usage and configuration of the `WaveformClip` class.

## Creating a Waveform Clip

Below is an example of how to create a `WaveformClip`:

```typescript
new core.WaveformClip(new File([], 'audio.mp3'), {
  width: '90%',          // Width of the waveform clip as a percentage of the canvas or in pixels
  height: 700,           // Height of the waveform clip in pixels
  duration: 600,         // Duration of the waveform animation in seconds
  x: '50%',              // X-axis position of the clip, can be a percentage or pixel value
  y: '100%',             // Y-axis position of the clip, can be a percentage or pixel value
  bar: {
    width: 18,           // Width of each bar in the waveform
    gap: 14,             // Gap between each bar
    radius: 5,           // Border radius for rounded bars
  },
  anchor: {
    x: 0.5,              // X-axis anchor point (0 is left, 1 is right, 0.5 is center)
    y: 1,                // Y-axis anchor point (0 is top, 1 is bottom, 0.5 is center)
  },
})
```

### Parameters Explained

- **`new File([], 'audio.mp3')`**: Specifies the audio file to be used for the waveform visualization. Replace with your audio file.

- **`width`**: Determines the width of the waveform clip. Accepts percentages (e.g., `'90%'`) or pixel values (e.g., `700`).

- **`height`**: Specifies the height of the waveform clip in pixels.

- **`duration`**: Defines the length of the animation in seconds. This controls how the waveform progresses.

- **`x` & `y`**: Set the position of the waveform clip on the canvas. Accepts percentages (e.g., `'50%'`) or pixel values.

- **`bar`**: Customize the appearance of the waveform's bars:
  - `width`: The width of each individual bar in pixels.
  - `gap`: The gap between each bar in pixels.
  - `radius`: The border radius of each bar for rounded edges.

- **`anchor`**: Controls the anchor point of the clip. This determines how the clip is positioned relative to its `x` and `y` coordinates.
  - `x`: Horizontal anchor point (e.g., `0` for left, `0.5` for center, `1` for right).
  - `y`: Vertical anchor point (e.g., `0` for top, `0.5` for center, `1` for bottom).

## Example Use Case

The `WaveformClip` is ideal for creating audio visualizations in video projects or for enhancing multimedia content. Customize the dimensions, position, and style to match your design needs.

Getting started with the core library

## Welcome

`@diffusionstudio/core` is a 2D motion graphics and video rendering engine powered by WebCodecs. Developers commonly use it to implement automation pipelines and build browser-based video editing applications.

## Terminology

To better understand the documentation, here are some key terms you should know:

- **Composition:** The root object that contains all assets to be rendered in a single video.
- **Track:** A chronological sequence of clips of the same type (e.g., video clips).
- **Clip:** An object that contains specific rendering information, such as position and duration of visibility within the video.
- **Framerate:** The rate at which frames are displayed, measured in frames per second (FPS). If not specified otherwise, Diffusion Studio uses a default frame rate of 30 FPS.
- **Encoder:** A tool that compresses the size of each frame within the sequence, using common codecs such as H.264/AVC1 or H.265/HEVC.
- **Renderer:** An abstraction responsible for creating and managing the rendering context (WebGL or Canvas), drawing the composition state to the screen.
- **Ticker:** A tool that ensures the composition state is updated at the correct frame rate and rendered to the screen.

## Installation

```sh
npm i @diffusionstudio/core
```

Now you can start hacking!

## Enjoy!

```typescript
import * as core from '@diffusionstudio/core';

const text = new core.TextClip({
  text: 'Hello World', 
  position: 'center' 
}); 

const composition = new core.Composition();            // create root object
await composition.add(text);                      // render text

const blob = await new core.Encoder(composition).render();
```

# Operator UI

The [Operator UI](https://operator-ui.vercel.app) provides a set of convenience functions and object references for interacting with the video editor programmatically.

## Functions

### `window.render(): Promise<void>`

Initiates the rendering process using the current composition (`window.composition`).

### `window.files(): Promise<File[]>`

Retrieves a list of files uploaded to the editor.

## Objects

### `window.composition: Composition`

Represents the current composition being edited.

### `window.core: typeof core from '@diffusionstudio/core'`

Provides access to the core library for handling video editing operations.

## Example Usage

The following example demonstrates how to:
1. Retrieve the first uploaded video file.
2. Create a subclip of the first 150 seconds.
3. Add the subclip to the composition.
4. Render the final composition.

```javascript
const [videoFile] = await files();
const video = new core.VideoClip(videoFile).subclip(0, 150);
await composition.add(video);
await render();
```

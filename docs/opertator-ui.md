# Operator UI

The operator UI provides a set of convenience functions and attributes for interacting with the video editor.

## Functions

### `window.render(): Promise<void>`

Starts the rendering process using the current composition (`window.composition`).

### `window.files(): Promise<File[]>`

This function returns a list of files uploaded to the editor.

### `window.composition: Composition`

This is the current composition.

### `window.core: * as core from '@diffusionstudio/core'`

This is the core object provides access to the core library.

## Example

Get the first video file, create a subclip of 150 seconds, add it to the composition, and render the composition.

```javascript
const [videoFile] = files();
const video = new core.VideoClip(videoFile).subclip(0, 150);
await composition.add(video);
await render();
```

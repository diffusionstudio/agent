# Text Clips

Here is a basic example of how to style text clips:

```typescript
import * as core from '@diffusionstudio/core';

const font = await core.FontManager.load({ 
  family: 'Geologica', 
  weight: '400',
});

const text = new core.TextClip({
  text: 'Hello World',
  align: 'center',
  baseline: 'middle',
  color: '#FFFFFF',
  font,
  fontSize: 16, // make sure to place after font
  leading: 1.1,
  stroke: {
    color: '#000000',
    width: 4,
    lineJoin: 'round',
  },
  shadow: {
    opacity: 70,
    blur: 6,
    offsetX: 2,
    offsetY: 4,
  },
  x: '12%',
  y: '50%',
});
```

We have loaded the web font from a predefined set of popular web fonts. You can also use custom web fonts like this:

```typescript
const manager = new core.FontManager();

const roboto = await manager.load({
  source: "https://fonts.gstatic.com/s/roboto/v32/KFOlCnqEu92Fr1MmSU5fBBc4AMP6lQ.woff2",
  weight: '400',
  family: 'Roboto'
});
```

For more examples, see [examples](https://github.com/diffusionstudio/examples/blob/f8bde98c53320b8bcd78a541244fc95ff2b40cbd/showcase/src/compositions/font.ts).

Setting the `align` and `baseline` properties will adjust the anchor point, comparable to the [transform-origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin) in CSS.

## Rich Text

We have tested various methods to render text with differently styled subsections, such as changing the color of a particular word. While Pixi.js `HTMLText` was a promising solution, the quality of the text did not meet our standards. We ultimately implemented our own solution using foreignObjects. Although visually satisfying, the performance was inadequate for production use. We reverted to a 2D context implementation, resulting in the current state.

```typescript
const font = await core.FontManager.load({ 
  family: 'Geologica', 
  weight: '800',
});

const text = new RichTextClip({
  text: 'Complex Text',
  duration: composition.duration,
  align: 'center',
  baseline: 'middle',
  font,
  casing: 'upper',
  fontSize: 18,
  stroke: {
    width: 3,
    color: '#000000',
  },
  y: '85%',
  x: '50%',
  styles: [{
    start: 8,
    style: {
      color: '#19fa2c'
    }
  }],
});
```

The `RichTextClip` is derived from the `TextClip`, with the notable addition of`styles` and `maxWidth` properties. The `styles` array allows you to define the styles you want to override for specific sections of the `RichTextClip`. Currently available styles include:
* `color?: string;`
* `fontSize?: number;`
* `stroke?: Stroke;`
* `font?: Font;`

Each style object requires a `start` index indicating where the section should begin. Optionally, you can specify a `stop` index, with the default being the end of the text.

See it in action [here](https://github.com/diffusionstudio/examples/blob/f8bde98c53320b8bcd78a541244fc95ff2b40cbd/showcase/src/compositions/custom-captions.ts).

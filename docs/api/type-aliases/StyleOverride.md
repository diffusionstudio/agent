[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / StyleOverride

# Type Alias: StyleOverride

> **StyleOverride**: `object`

## Type declaration

### start

> **start**: `number`

Defines the start of the style segment

### stop?

> `optional` **stop**: `number`

Defines the stop of the style segment, leave
undefined when it's the end of the text

### style

> **style**: `object`

Defines the style of the text

### style.color?

> `optional` **color**: [`hex`](hex.md)

Defines the fill style of the text

### style.font?

> `optional` **font**: [`Font`](../interfaces/Font.md)

Defines the font of the text

### style.fontSize?

> `optional` **fontSize**: `number`

Defines the font size of the text

### style.stroke?

> `optional` **stroke**: `Partial`\<[`Stroke`](../interfaces/Stroke.md)\>

Defines the stroke of the text

## Defined in

[src/clips/text/text.types.ts:5](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.types.ts#L5)

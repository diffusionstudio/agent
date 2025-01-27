[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / TextClipProps

# Interface: TextClipProps

## Extends

- [`ClipProps`](ClipProps.md).`Omit`\<[`VisualMixinProps`](VisualMixinProps.md), `"anchor"` \| `"width"` \| `"height"`\>

## Properties

### align?

> `optional` **align**: [`TextAlign`](../type-aliases/TextAlign.md)

#### Defined in

[src/clips/text/text.interfaces.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L18)

***

### anchorX?

> `optional` **anchorX**: `number`

#### Inherited from

`Omit.anchorX`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L26)

***

### anchorY?

> `optional` **anchorY**: `number`

#### Inherited from

`Omit.anchorY`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:27](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L27)

***

### animations?

> `optional` **animations**: [`TextClipAnimationOptions`](../type-aliases/TextClipAnimationOptions.md)

#### Overrides

[`ClipProps`](ClipProps.md).[`animations`](ClipProps.md#animations)

#### Defined in

[src/clips/text/text.interfaces.ts:27](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L27)

***

### baseline?

> `optional` **baseline**: [`TextBaseline`](../type-aliases/TextBaseline.md)

#### Defined in

[src/clips/text/text.interfaces.ts:19](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L19)

***

### blendMode?

> `optional` **blendMode**: [`BlendMode`](../type-aliases/BlendMode.md)

#### Inherited from

`Omit.blendMode`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L30)

***

### casing?

> `optional` **casing**: [`TextCase`](../type-aliases/TextCase.md)

#### Defined in

[src/clips/text/text.interfaces.ts:22](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L22)

***

### color?

> `optional` **color**: \`#$\{string\}\`

#### Defined in

[src/clips/text/text.interfaces.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L20)

***

### delay?

> `optional` **delay**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](../classes/Timestamp.md)

#### Inherited from

[`ClipProps`](ClipProps.md).[`delay`](ClipProps.md#delay)

#### Defined in

[src/clips/clip/clip.interfaces.ts:10](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.interfaces.ts#L10)

***

### disabled?

> `optional` **disabled**: `boolean`

#### Inherited from

[`ClipProps`](ClipProps.md).[`disabled`](ClipProps.md#disabled)

#### Defined in

[src/clips/clip/clip.interfaces.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.interfaces.ts#L7)

***

### duration?

> `optional` **duration**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](../classes/Timestamp.md)

#### Inherited from

[`ClipProps`](ClipProps.md).[`duration`](ClipProps.md#duration)

#### Defined in

[src/clips/clip/clip.interfaces.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.interfaces.ts#L9)

***

### filter?

> `optional` **filter**: `string`

#### Inherited from

`Omit.filter`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:29](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L29)

***

### font?

> `optional` **font**: [`Font`](Font.md)

#### Defined in

[src/clips/text/text.interfaces.ts:17](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L17)

***

### fontSize?

> `optional` **fontSize**: `number`

#### Defined in

[src/clips/text/text.interfaces.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L24)

***

### freeTransform?

> `optional` **freeTransform**: `boolean`

#### Inherited from

`Omit.freeTransform`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:28](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L28)

***

### glow?

> `optional` **glow**: [`Glow`](Glow.md)

#### Defined in

[src/clips/text/text.interfaces.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L26)

***

### leading?

> `optional` **leading**: `number`

#### Defined in

[src/clips/text/text.interfaces.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L25)

***

### mask?

> `optional` **mask**: [`Mask`](../classes/Mask.md)

#### Inherited from

`Omit.mask`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:31](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L31)

***

### name?

> `optional` **name**: `string`

#### Inherited from

[`ClipProps`](ClipProps.md).[`name`](ClipProps.md#name)

#### Defined in

[src/clips/clip/clip.interfaces.ts:8](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.interfaces.ts#L8)

***

### opacity?

> `optional` **opacity**: `number`

#### Inherited from

`Omit.opacity`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L13)

***

### position?

> `optional` **position**: `"center"` \| [`RelativePoint`](RelativePoint.md)

#### Inherited from

`Omit.position`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:17](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L17)

***

### rotation?

> `optional` **rotation**: `number`

#### Inherited from

`Omit.rotation`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:12](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L12)

***

### scale?

> `optional` **scale**: `number` \| [`Point`](Point.md)

#### Inherited from

`Omit.scale`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L20)

***

### scaleX?

> `optional` **scaleX**: `number`

#### Inherited from

`Omit.scaleX`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L21)

***

### scaleY?

> `optional` **scaleY**: `number`

#### Inherited from

`Omit.scaleY`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:22](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L22)

***

### shadow?

> `optional` **shadow**: [`Shadow`](Shadow.md) \| [`Shadow`](Shadow.md)[]

#### Defined in

[src/clips/text/text.interfaces.ts:23](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L23)

***

### stroke?

> `optional` **stroke**: [`Stroke`](Stroke.md)

#### Defined in

[src/clips/text/text.interfaces.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L21)

***

### text?

> `optional` **text**: `string`

#### Defined in

[src/clips/text/text.interfaces.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.interfaces.ts#L16)

***

### translate?

> `optional` **translate**: `number` \| [`Point`](Point.md)

#### Inherited from

`Omit.translate`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:14](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L14)

***

### translateX?

> `optional` **translateX**: `number` \| \`$\{number\}%\`

#### Inherited from

`Omit.translateX`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L15)

***

### translateY?

> `optional` **translateY**: `number` \| \`$\{number\}%\`

#### Inherited from

`Omit.translateY`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L16)

***

### x?

> `optional` **x**: `number` \| \`$\{number\}%\`

#### Inherited from

`Omit.x`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L18)

***

### y?

> `optional` **y**: `number` \| \`$\{number\}%\`

#### Inherited from

`Omit.y`

#### Defined in

[src/clips/mixins/visual.interfaces.ts:19](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L19)

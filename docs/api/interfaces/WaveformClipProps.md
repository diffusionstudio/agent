[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / WaveformClipProps

# Interface: WaveformClipProps

## Extends

- `Omit`\<[`MediaClipProps`](MediaClipProps.md), `"volume"`\>.[`VisualMixinProps`](VisualMixinProps.md)

## Properties

### anchor?

> `optional` **anchor**: `number` \| [`Point`](Point.md)

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`anchor`](VisualMixinProps.md#anchor)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L25)

***

### anchorX?

> `optional` **anchorX**: `number`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`anchorX`](VisualMixinProps.md#anchorx)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L26)

***

### anchorY?

> `optional` **anchorY**: `number`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`anchorY`](VisualMixinProps.md#anchory)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:27](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L27)

***

### animations?

> `optional` **animations**: [`VisualMixinAnimationOptions`](../type-aliases/VisualMixinAnimationOptions.md)

#### Overrides

`Omit.animations`

#### Defined in

[src/clips/shape/waveform.interfaces.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/shape/waveform.interfaces.ts#L15)

***

### bar?

> `optional` **bar**: [`WaveformBar`](WaveformBar.md)

#### Defined in

[src/clips/shape/waveform.interfaces.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/shape/waveform.interfaces.ts#L16)

***

### blendMode?

> `optional` **blendMode**: [`BlendMode`](../type-aliases/BlendMode.md)

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`blendMode`](VisualMixinProps.md#blendmode)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L30)

***

### delay?

> `optional` **delay**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](../classes/Timestamp.md)

#### Inherited from

`Omit.delay`

#### Defined in

[src/clips/clip/clip.interfaces.ts:10](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.interfaces.ts#L10)

***

### disabled?

> `optional` **disabled**: `boolean`

#### Inherited from

`Omit.disabled`

#### Defined in

[src/clips/clip/clip.interfaces.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.interfaces.ts#L7)

***

### duration?

> `optional` **duration**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](../classes/Timestamp.md)

#### Inherited from

`Omit.duration`

#### Defined in

[src/clips/clip/clip.interfaces.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.interfaces.ts#L9)

***

### fill?

> `optional` **fill**: [`FillOptions`](FillOptions.md)

#### Defined in

[src/clips/shape/waveform.interfaces.ts:17](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/shape/waveform.interfaces.ts#L17)

***

### filter?

> `optional` **filter**: `string`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`filter`](VisualMixinProps.md#filter)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:29](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L29)

***

### freeTransform?

> `optional` **freeTransform**: `boolean`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`freeTransform`](VisualMixinProps.md#freetransform)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:28](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L28)

***

### height?

> `optional` **height**: `number` \| \`$\{number\}%\`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`height`](VisualMixinProps.md#height)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:23](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L23)

***

### magnitude?

> `optional` **magnitude**: `number`

#### Defined in

[src/clips/shape/waveform.interfaces.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/shape/waveform.interfaces.ts#L20)

***

### mask?

> `optional` **mask**: [`Mask`](../classes/Mask.md)

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`mask`](VisualMixinProps.md#mask)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:31](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L31)

***

### muted?

> `optional` **muted**: `boolean`

#### Inherited from

`Omit.muted`

#### Defined in

[src/clips/media/media.interfaces.ts:8](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.interfaces.ts#L8)

***

### name?

> `optional` **name**: `string`

#### Inherited from

`Omit.name`

#### Defined in

[src/clips/clip/clip.interfaces.ts:8](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.interfaces.ts#L8)

***

### opacity?

> `optional` **opacity**: `number`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`opacity`](VisualMixinProps.md#opacity)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L13)

***

### playing?

> `optional` **playing**: `boolean`

#### Inherited from

`Omit.playing`

#### Defined in

[src/clips/media/media.interfaces.ts:5](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.interfaces.ts#L5)

***

### position?

> `optional` **position**: `"center"` \| [`RelativePoint`](RelativePoint.md)

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`position`](VisualMixinProps.md#position)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:17](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L17)

***

### rotation?

> `optional` **rotation**: `number`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`rotation`](VisualMixinProps.md#rotation)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:12](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L12)

***

### sampleRate?

> `optional` **sampleRate**: `number`

#### Defined in

[src/clips/shape/waveform.interfaces.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/shape/waveform.interfaces.ts#L18)

***

### scale?

> `optional` **scale**: `number` \| [`Point`](Point.md)

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`scale`](VisualMixinProps.md#scale)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L20)

***

### scaleX?

> `optional` **scaleX**: `number`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`scaleX`](VisualMixinProps.md#scalex)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L21)

***

### scaleY?

> `optional` **scaleY**: `number`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`scaleY`](VisualMixinProps.md#scaley)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:22](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L22)

***

### smoothing?

> `optional` **smoothing**: `number`

#### Defined in

[src/clips/shape/waveform.interfaces.ts:19](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/shape/waveform.interfaces.ts#L19)

***

### transcript?

> `optional` **transcript**: [`Transcript`](../classes/Transcript.md)

#### Inherited from

`Omit.transcript`

#### Defined in

[src/clips/media/media.interfaces.ts:6](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.interfaces.ts#L6)

***

### translate?

> `optional` **translate**: `number` \| [`Point`](Point.md)

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`translate`](VisualMixinProps.md#translate)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:14](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L14)

***

### translateX?

> `optional` **translateX**: `number` \| \`$\{number\}%\`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`translateX`](VisualMixinProps.md#translatex)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L15)

***

### translateY?

> `optional` **translateY**: `number` \| \`$\{number\}%\`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`translateY`](VisualMixinProps.md#translatey)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L16)

***

### width?

> `optional` **width**: `number` \| \`$\{number\}%\`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`width`](VisualMixinProps.md#width)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L24)

***

### x?

> `optional` **x**: `number` \| \`$\{number\}%\`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`x`](VisualMixinProps.md#x)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L18)

***

### y?

> `optional` **y**: `number` \| \`$\{number\}%\`

#### Inherited from

[`VisualMixinProps`](VisualMixinProps.md).[`y`](VisualMixinProps.md#y)

#### Defined in

[src/clips/mixins/visual.interfaces.ts:19](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.interfaces.ts#L19)

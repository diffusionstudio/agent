[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Encoder

# Class: Encoder

## Extends

- `WebcodecsVideoEncoder`

## Constructors

### new Encoder()

> **new Encoder**(`composition`, `init`?): [`Encoder`](Encoder.md)

Create a new audio and video encoder and multiplex the result 
using a mp4 container

#### Parameters

• **composition**: [`Composition`](Composition.md)

The composition to render

• **init?**: `VideoEncoderInit`

#### Returns

[`Encoder`](Encoder.md)

#### Example

```
new Encoder(composition, { resolution: 2 }).render() // will render at 4K
```

#### Overrides

`WebcodecsVideoEncoder.constructor`

#### Defined in

[src/encoders/encoder.ts:27](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/encoder.ts#L27)

## Properties

### \_handlers

> **\_handlers**: `object` = `{}`

#### \*?

> `optional` **\***: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### error?

> `optional` **error**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### render?

> `optional` **render**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### Inherited from

`WebcodecsVideoEncoder._handlers`

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### audio

> **audio**: `boolean`

Defines if the audio should be encoded

#### Inherited from

`WebcodecsVideoEncoder.audio`

#### Defined in

[src/encoders/webcodecs.video.ts:23](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L23)

***

### composition

> **composition**: [`Composition`](Composition.md)

#### Inherited from

`WebcodecsVideoEncoder.composition`

#### Defined in

[src/encoders/webcodecs.video.ts:14](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L14)

***

### debug

> **debug**: `boolean`

Defines if the performance should be logged

#### Default

```ts
false;
```

#### Inherited from

`WebcodecsVideoEncoder.debug`

#### Defined in

[src/encoders/webcodecs.video.ts:22](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L22)

***

### fps

> **fps**: `number`

Defines the fps at which the composition
will be rendered

#### Default

```ts
30
```

#### Inherited from

`WebcodecsVideoEncoder.fps`

#### Defined in

[src/encoders/webcodecs.video.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L21)

***

### gpuBatchSize

> **gpuBatchSize**: `number`

Defines the maximum size of the video
encoding queue, increasing this number
will put a higher pressure on the gpu.
It's restricted to a value between 1 and 100

#### Default

```ts
5
```

#### Inherited from

`WebcodecsVideoEncoder.gpuBatchSize`

#### Defined in

[src/encoders/webcodecs.video.ts:19](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L19)

***

### numberOfChannels

> **numberOfChannels**: `number`

Defines the number of channels
of the composed audio

#### Default

```ts
2
```

#### Inherited from

`WebcodecsVideoEncoder.numberOfChannels`

#### Defined in

[src/encoders/webcodecs.video.ts:17](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L17)

***

### resolution

> **resolution**: `number`

Multiplier of the composition size

#### Example

```ts
2 // 1080p -> 4K
```

#### Default

```ts
1 // 1080p -> 1080p
```

#### Inherited from

`WebcodecsVideoEncoder.resolution`

#### Defined in

[src/encoders/webcodecs.video.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L15)

***

### sampleRate

> **sampleRate**: `number`

A floating point number indicating the audio context's sample rate, in samples per second.

#### Default

```ts
48000
```

#### Inherited from

`WebcodecsVideoEncoder.sampleRate`

#### Defined in

[src/encoders/webcodecs.video.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L16)

***

### videoBitrate

> **videoBitrate**: `number`

Defines the bitrate at which the video
should be rendered at

#### Default

```ts
10e6
```

#### Inherited from

`WebcodecsVideoEncoder.videoBitrate`

#### Defined in

[src/encoders/webcodecs.video.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L18)

***

### watermark

> **watermark**: `boolean`

Defines if the watermark should be added

#### Default

```ts
false;
```

#### Inherited from

`WebcodecsVideoEncoder.watermark`

#### Defined in

[src/encoders/webcodecs.video.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L20)

## Methods

### bubble()

> **bubble**(`target`): `string`

#### Parameters

• **target**: `EventEmitter`\<`EncoderEvents`, [`Constructor`](../type-aliases/Constructor.md)\>

#### Returns

`string`

#### Inherited from

`WebcodecsVideoEncoder.bubble`

#### Defined in

[src/mixins/event.ts:66](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L66)

***

### emit()

> **emit**\<`T`\>(`eventType`, `detail`): `void`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| `"render"`

#### Parameters

• **eventType**: `T`

• **detail**: `BaseEvents`\<`EncoderEvents`\>\[`T`\]

#### Returns

`void`

#### Inherited from

`WebcodecsVideoEncoder.emit`

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### encodeVideo()

> **encodeVideo**(`muxer`, `config`, `signal`?): `Promise`\<`void`\>

render and encode visual frames

#### Parameters

• **muxer**: `Muxer`\<`StreamTarget`\>

• **config**: `VideoEncoderConfig`

• **signal?**: `AbortSignal`

#### Returns

`Promise`\<`void`\>

#### Inherited from

`WebcodecsVideoEncoder.encodeVideo`

#### Defined in

[src/encoders/webcodecs.video.ts:43](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/webcodecs.video.ts#L43)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

`WebcodecsVideoEncoder.off`

#### Defined in

[src/mixins/event.ts:33](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L33)

***

### on()

> **on**\<`T`\>(`eventType`, `callback`): `string`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| `"render"`

#### Parameters

• **eventType**: `T`

• **callback**

#### Returns

`string`

#### Inherited from

`WebcodecsVideoEncoder.on`

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### render()

> **render**(`target`?, `signal`?): `Promise`\<`undefined` \| `Blob`\>

Export the specified composition

#### Parameters

• **target?**: `string` \| `StreamCallback` \| `FileSystemFileHandle`

• **signal?**: `AbortSignal`

#### Returns

`Promise`\<`undefined` \| `Blob`\>

#### Throws

DOMException if the export has been aborted

#### Defined in

[src/encoders/encoder.ts:35](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/encoder.ts#L35)

***

### resolve()

> **resolve**(`eventType`): (`resolve`, `reject`) => `void`

#### Parameters

• **eventType**: `"*"` \| `"error"` \| `"render"`

#### Returns

`Function`

##### Parameters

• **resolve**

• **reject**

##### Returns

`void`

#### Inherited from

`WebcodecsVideoEncoder.resolve`

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

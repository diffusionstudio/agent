[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / OpusEncoder

# Class: OpusEncoder

## Constructors

### new OpusEncoder()

> **new OpusEncoder**(`init`): [`OpusEncoder`](OpusEncoder.md)

Create a new OpusEncoder for encoding pcm to opus

#### Parameters

• **init**: [`OpusEncoderInit`](../type-aliases/OpusEncoderInit.md)

encoder callbacks

#### Returns

[`OpusEncoder`](OpusEncoder.md)

#### Defined in

[src/encoders/opus/opus.encoder.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/opus/opus.encoder.ts#L26)

## Properties

### config?

> `optional` **config**: [`OpusEncoderConfig`](../type-aliases/OpusEncoderConfig.md)

#### Defined in

[src/encoders/opus/opus.encoder.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/opus/opus.encoder.ts#L16)

***

### error

> **error**: `WebCodecsErrorCallback`

#### Defined in

[src/encoders/opus/opus.encoder.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/opus/opus.encoder.ts#L15)

***

### output

> **output**: [`EncodedOpusChunkOutputCallback`](../type-aliases/EncodedOpusChunkOutputCallback.md)

#### Defined in

[src/encoders/opus/opus.encoder.ts:14](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/opus/opus.encoder.ts#L14)

## Methods

### configure()

> **configure**(`config`): `Promise`\<`void`\>

Configure the encoder. **Note** these values must match the samples to encode

#### Parameters

• **config**: [`OpusEncoderConfig`](../type-aliases/OpusEncoderConfig.md)

The sample rate and channel count to use

#### Returns

`Promise`\<`void`\>

#### Defined in

[src/encoders/opus/opus.encoder.ts:35](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/opus/opus.encoder.ts#L35)

***

### encode()

> **encode**(`samples`): `void`

Encode the samples synchronously (this is a blocking event)

#### Parameters

• **samples**: [`OpusEncoderSamples`](../type-aliases/OpusEncoderSamples.md)

The data to encode

#### Returns

`void`

#### Defined in

[src/encoders/opus/opus.encoder.ts:74](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/encoders/opus/opus.encoder.ts#L74)

[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Serializer

# Class: Serializer

## Extended by

- [`ClassicCaptionPreset`](ClassicCaptionPreset.md)
- [`SpotlightCaptionPreset`](SpotlightCaptionPreset.md)
- [`GuineaCaptionPreset`](GuineaCaptionPreset.md)
- [`CascadeCaptionPreset`](CascadeCaptionPreset.md)
- [`SolarCaptionPreset`](SolarCaptionPreset.md)
- [`WhisperCaptionPreset`](WhisperCaptionPreset.md)
- [`VerdantCaptionPreset`](VerdantCaptionPreset.md)
- [`FontManager`](FontManager.md)

## Constructors

### new Serializer()

> **new Serializer**(): [`Serializer`](Serializer.md)

#### Returns

[`Serializer`](Serializer.md)

## Properties

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

## Methods

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Defined in

[src/services/serializer.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L9)

***

### fromJSON()

> `static` **fromJSON**\<`T`, `K`\>(`this`, `obj`): `T`

#### Type Parameters

• **T** *extends* [`Serializer`](Serializer.md)

• **K** = `object`

#### Parameters

• **this**

• **obj**: `K` *extends* `string` ? `never` : `K`

#### Returns

`T`

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

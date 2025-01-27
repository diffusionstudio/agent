[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / ClassicCaptionPreset

# Class: ClassicCaptionPreset

## Extends

- [`Serializer`](Serializer.md)

## Implements

- [`CaptionPresetStrategy`](../interfaces/CaptionPresetStrategy.md)

## Constructors

### new ClassicCaptionPreset()

> **new ClassicCaptionPreset**(`config`): [`ClassicCaptionPreset`](ClassicCaptionPreset.md)

#### Parameters

• **config**: `Partial`\<[`DefaultCaptionPresetConfig`](../type-aliases/DefaultCaptionPresetConfig.md)\> = `{}`

#### Returns

[`ClassicCaptionPreset`](ClassicCaptionPreset.md)

#### Overrides

[`Serializer`](Serializer.md).[`constructor`](Serializer.md#constructors)

#### Defined in

[src/tracks/caption/preset.classic.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.classic.ts#L24)

## Properties

### generatorOptions

> **generatorOptions**: [`GeneratorOptions`](../type-aliases/GeneratorOptions.md)

#### Defined in

[src/tracks/caption/preset.classic.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.classic.ts#L16)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

[`Serializer`](Serializer.md).[`id`](Serializer.md#id)

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### position

> **position**: [`RelativePoint`](../interfaces/RelativePoint.md)

This function returns the position of the captions

#### Implementation of

[`CaptionPresetStrategy`](../interfaces/CaptionPresetStrategy.md).[`position`](../interfaces/CaptionPresetStrategy.md#position)

#### Defined in

[src/tracks/caption/preset.classic.ts:22](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.classic.ts#L22)

***

### type

> `readonly` **type**: `string` = `'CLASSIC'`

Defines the type of strategy

#### Implementation of

[`CaptionPresetStrategy`](../interfaces/CaptionPresetStrategy.md).[`type`](../interfaces/CaptionPresetStrategy.md#type)

#### Defined in

[src/tracks/caption/preset.classic.ts:19](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.classic.ts#L19)

## Methods

### applyTo()

> **applyTo**(`track`): `Promise`\<`void`\>

This function applies the settings to the track

#### Parameters

• **track**: [`CaptionTrack`](CaptionTrack.md)

#### Returns

`Promise`\<`void`\>

#### Implementation of

[`CaptionPresetStrategy`](../interfaces/CaptionPresetStrategy.md).[`applyTo`](../interfaces/CaptionPresetStrategy.md#applyto)

#### Defined in

[src/tracks/caption/preset.classic.ts:31](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.classic.ts#L31)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

[`Serializer`](Serializer.md).[`toJSON`](Serializer.md#tojson)

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

#### Inherited from

[`Serializer`](Serializer.md).[`fromJSON`](Serializer.md#fromjson)

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

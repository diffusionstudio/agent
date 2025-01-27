[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / SpotlightCaptionPreset

# Class: SpotlightCaptionPreset

## Extends

- [`Serializer`](Serializer.md)

## Implements

- [`CaptionPresetStrategy`](../interfaces/CaptionPresetStrategy.md)

## Constructors

### new SpotlightCaptionPreset()

> **new SpotlightCaptionPreset**(`config`): [`SpotlightCaptionPreset`](SpotlightCaptionPreset.md)

#### Parameters

• **config**: `Partial`\<[`SingleColorCaptionPresetConfig`](../type-aliases/SingleColorCaptionPresetConfig.md)\> = `{}`

#### Returns

[`SpotlightCaptionPreset`](SpotlightCaptionPreset.md)

#### Overrides

[`Serializer`](Serializer.md).[`constructor`](Serializer.md#constructors)

#### Defined in

[src/tracks/caption/preset.spotlight.ts:28](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.spotlight.ts#L28)

## Properties

### color

> **color**: \`#$\{string\}\`

#### Defined in

[src/tracks/caption/preset.spotlight.ts:23](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.spotlight.ts#L23)

***

### generatorOptions

> **generatorOptions**: [`GeneratorOptions`](../type-aliases/GeneratorOptions.md)

#### Defined in

[src/tracks/caption/preset.spotlight.ts:17](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.spotlight.ts#L17)

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

[src/tracks/caption/preset.spotlight.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.spotlight.ts#L26)

***

### type

> `readonly` **type**: `"SPOTLIGHT"` = `'SPOTLIGHT'`

Defines the type of strategy

#### Implementation of

[`CaptionPresetStrategy`](../interfaces/CaptionPresetStrategy.md).[`type`](../interfaces/CaptionPresetStrategy.md#type)

#### Defined in

[src/tracks/caption/preset.spotlight.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.spotlight.ts#L20)

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

[src/tracks/caption/preset.spotlight.ts:36](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.spotlight.ts#L36)

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

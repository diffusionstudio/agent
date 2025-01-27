[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / CaptionPresetStrategy

# Interface: CaptionPresetStrategy

## Properties

### position

> **position**: [`RelativePoint`](RelativePoint.md)

This function returns the position of the captions

#### Defined in

[src/tracks/caption/preset.interface.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.interface.ts#L13)

***

### type

> **type**: `string`

Defines the type of strategy

#### Defined in

[src/tracks/caption/preset.interface.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.interface.ts#L9)

## Methods

### applyTo()

> **applyTo**(`track`): `Promise`\<`void`\>

This function applies the settings to the track

#### Parameters

• **track**: [`CaptionTrack`](../classes/CaptionTrack.md)

#### Returns

`Promise`\<`void`\>

#### Defined in

[src/tracks/caption/preset.interface.ts:17](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/caption/preset.interface.ts#L17)

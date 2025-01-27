[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / ClipDeserializer

# Class: ClipDeserializer

## Constructors

### new ClipDeserializer()

> **new ClipDeserializer**(): [`ClipDeserializer`](ClipDeserializer.md)

#### Returns

[`ClipDeserializer`](ClipDeserializer.md)

## Methods

### fromSource()

> `static` **fromSource**(`data`): `undefined` \| [`VideoClip`](VideoClip.md) \| [`AudioClip`](AudioClip.md) \| [`HtmlClip`](HtmlClip.md) \| [`ImageClip`](ImageClip.md)

#### Parameters

• **data**: [`Source`](Source.md)

#### Returns

`undefined` \| [`VideoClip`](VideoClip.md) \| [`AudioClip`](AudioClip.md) \| [`HtmlClip`](HtmlClip.md) \| [`ImageClip`](ImageClip.md)

#### Defined in

[src/clips/clip/clip.desierializer.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.desierializer.ts#L26)

***

### fromType()

> `static` **fromType**(`data`): [`Clip`](Clip.md)

#### Parameters

• **data**

• **data.type**: [`ClipType`](../type-aliases/ClipType.md)

#### Returns

[`Clip`](Clip.md)

#### Defined in

[src/clips/clip/clip.desierializer.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.desierializer.ts#L9)

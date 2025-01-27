[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / FontManager

# Class: FontManager

## Extends

- [`Serializer`](Serializer.md)

## Constructors

### new FontManager()

> **new FontManager**(): [`FontManager`](FontManager.md)

#### Returns

[`FontManager`](FontManager.md)

#### Inherited from

[`Serializer`](Serializer.md).[`constructor`](Serializer.md#constructors)

## Properties

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

[`Serializer`](Serializer.md).[`id`](Serializer.md#id)

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### loadedFonts

> **loadedFonts**: [`FontSource`](../type-aliases/FontSource.md)[] = `[]`

The fonts that have been loaded

#### Defined in

[src/font/manager.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/font/manager.ts#L13)

## Methods

### copy()

> **copy**(): [`FontManager`](FontManager.md)

#### Returns

[`FontManager`](FontManager.md)

#### Defined in

[src/font/manager.ts:139](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/font/manager.ts#L139)

***

### load()

> **load**\<`T`\>(`options`): `Promise`\<[`Font`](../interfaces/Font.md)\>

Load the font that has been initiated via the constructor

#### Type Parameters

• **T** *extends* `"The Bold Font"` \| `"Komika Axis"` \| `"Geologica"` \| `"Nunito"` \| `"Figtree"` \| `"Urbanist"` \| `"Montserrat"` \| `"Bangers"` \| `"Chewy"` \| `"Source Code Pro"`

#### Parameters

• **options**: [`FontSource`](../type-aliases/FontSource.md) \| [`WebfontProperties`](../type-aliases/WebfontProperties.md)\<`T`\>

#### Returns

`Promise`\<[`Font`](../interfaces/Font.md)\>

#### Defined in

[src/font/manager.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/font/manager.ts#L18)

***

### reload()

> **reload**(): `Promise`\<`void`\>

Reload all fonts

#### Returns

`Promise`\<`void`\>

#### Defined in

[src/font/manager.ts:74](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/font/manager.ts#L74)

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

***

### load()

> `static` **load**\<`T`\>(`options`): `Promise`\<[`Font`](../interfaces/Font.md)\>

#### Type Parameters

• **T** *extends* `"The Bold Font"` \| `"Komika Axis"` \| `"Geologica"` \| `"Nunito"` \| `"Figtree"` \| `"Urbanist"` \| `"Montserrat"` \| `"Bangers"` \| `"Chewy"` \| `"Source Code Pro"`

#### Parameters

• **options**: [`FontSource`](../type-aliases/FontSource.md) \| [`WebfontProperties`](../type-aliases/WebfontProperties.md)\<`T`\>

#### Returns

`Promise`\<[`Font`](../interfaces/Font.md)\>

#### Defined in

[src/font/manager.ts:132](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/font/manager.ts#L132)

***

### localFonts()

> `static` **localFonts**(): `Promise`\<[`FontSources`](../type-aliases/FontSources.md)[]\>

Get all available local fonts, requires the
**Local Font Access API**

#### Returns

`Promise`\<[`FontSources`](../type-aliases/FontSources.md)[]\>

#### Defined in

[src/font/manager.ts:84](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/font/manager.ts#L84)

***

### webFonts()

> `static` **webFonts**(): [`FontSources`](../type-aliases/FontSources.md)[]

Get common web fonts

#### Returns

[`FontSources`](../type-aliases/FontSources.md)[]

#### Defined in

[src/font/manager.ts:117](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/font/manager.ts#L117)

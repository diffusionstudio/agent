[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Library

# Class: Library

## Extends

- `EventEmitter`\<`LibraryEvents`, [`Constructor`](../type-aliases/Constructor.md), `this`\>

## Constructors

### new Library()

> **new Library**(...`args`): [`Library`](Library.md)

#### Parameters

• ...**args**: `any`[]

#### Returns

[`Library`](Library.md)

#### Inherited from

`EventEmitterMixin<LibraryEvents>(Serializer).constructor`

#### Defined in

[src/types/index.ts:40](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/types/index.ts#L40)

## Properties

### \_handlers

> **\_handlers**: `object` = `{}`

#### \*?

> `optional` **\***: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### add?

> `optional` **add**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### error?

> `optional` **error**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### remove?

> `optional` **remove**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### Inherited from

`EventEmitterMixin<LibraryEvents>(Serializer)._handlers`

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### sources

> **sources**: [`Source`](Source.md)[] = `[]`

#### Defined in

[src/library/index.ts:12](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/library/index.ts#L12)

## Methods

### add()

> **add**(...`sources`): `Promise`\<[`Library`](Library.md)\>

#### Parameters

• ...**sources**: ([`Source`](Source.md) \| `Promise`\<[`Source`](Source.md)\>)[]

#### Returns

`Promise`\<[`Library`](Library.md)\>

#### Defined in

[src/library/index.ts:14](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/library/index.ts#L14)

***

### at()

> **at**\<`T`\>(`index`): `T`

#### Type Parameters

• **T** *extends* [`Source`](Source.md)

#### Parameters

• **index**: `number`

#### Returns

`T`

#### Defined in

[src/library/index.ts:51](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/library/index.ts#L51)

***

### bubble()

> **bubble**(`target`): `string`

#### Parameters

• **target**: `EventEmitter`\<`LibraryEvents`, [`Constructor`](../type-aliases/Constructor.md)\>

#### Returns

`string`

#### Inherited from

`EventEmitterMixin<LibraryEvents>(Serializer).bubble`

#### Defined in

[src/mixins/event.ts:66](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L66)

***

### emit()

> **emit**\<`T`\>(`eventType`, `detail`): `void`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| keyof LibraryEvents

#### Parameters

• **eventType**: `T`

• **detail**: `BaseEvents`\<`LibraryEvents`\>\[`T`\]

#### Returns

`void`

#### Inherited from

`EventEmitterMixin<LibraryEvents>(Serializer).emit`

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### get()

> **get**\<`T`\>(`key`): `T`

#### Type Parameters

• **T** *extends* [`Source`](Source.md)

#### Parameters

• **key**: `string`

#### Returns

`T`

#### Defined in

[src/library/index.ts:43](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/library/index.ts#L43)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

`EventEmitterMixin<LibraryEvents>(Serializer).off`

#### Defined in

[src/mixins/event.ts:33](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L33)

***

### on()

> **on**\<`T`\>(`eventType`, `callback`): `string`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| keyof LibraryEvents

#### Parameters

• **eventType**: `T`

• **callback**

#### Returns

`string`

#### Inherited from

`EventEmitterMixin<LibraryEvents>(Serializer).on`

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### remove()

> **remove**(`source`): `this`

#### Parameters

• **source**: `string` \| [`Source`](Source.md)

#### Returns

`this`

#### Defined in

[src/library/index.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/library/index.ts#L25)

***

### resolve()

> **resolve**(`eventType`): (`resolve`, `reject`) => `void`

#### Parameters

• **eventType**: `"*"` \| `"error"` \| keyof LibraryEvents

#### Returns

`Function`

##### Parameters

• **resolve**

• **reject**

##### Returns

`void`

#### Inherited from

`EventEmitterMixin<LibraryEvents>(Serializer).resolve`

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

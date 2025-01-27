[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / StorageItem

# Class: StorageItem\<T\>

## Extends

- `EventEmitter`\<`Events`, *typeof* [`Serializer`](Serializer.md), `this`\> & [`Serializer`](Serializer.md)\<`this`\>

## Type Parameters

• **T**

## Constructors

### new StorageItem()

> **new StorageItem**\<`T`\>(`store`, `key`, `value`): [`StorageItem`](StorageItem.md)\<`T`\>

#### Parameters

• **store**: [`Store`](Store.md)

• **key**: `string`

• **value**: `T` \| `Promise`\<`T`\>

#### Returns

[`StorageItem`](StorageItem.md)\<`T`\>

#### Overrides

`EventEmitterMixin<Events, typeof Serializer>(Serializer).constructor`

#### Defined in

[src/services/storage-item.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/storage-item.ts#L18)

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

#### update?

> `optional` **update**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### Inherited from

`EventEmitterMixin<Events, typeof Serializer>(Serializer)._handlers`

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

`EventEmitterMixin<Events, typeof Serializer>(Serializer).id`

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### loaded

> **loaded**: `boolean` = `false`

#### Defined in

[src/services/storage-item.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/storage-item.ts#L16)

## Accessors

### key

> `get` **key**(): `string`

#### Returns

`string`

#### Defined in

[src/services/storage-item.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/storage-item.ts#L26)

***

### value

> `get` **value**(): `T`

> `set` **value**(`newValue`): `void`

#### Parameters

• **newValue**: `T`

#### Returns

`T`

#### Defined in

[src/services/storage-item.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/storage-item.ts#L30)

## Methods

### bubble()

> **bubble**(`target`): `string`

#### Parameters

• **target**: `EventEmitter`\<`Events`, *typeof* [`Serializer`](Serializer.md)\>

#### Returns

`string`

#### Inherited from

`EventEmitterMixin<Events, typeof Serializer>(Serializer).bubble`

#### Defined in

[src/mixins/event.ts:66](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L66)

***

### emit()

> **emit**\<`T`\>(`eventType`, `detail`): `void`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| `"update"`

#### Parameters

• **eventType**: `T`

• **detail**: `BaseEvents`\<`Events`\>\[`T`\]

#### Returns

`void`

#### Inherited from

`EventEmitterMixin<Events, typeof Serializer>(Serializer).emit`

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

`EventEmitterMixin<Events, typeof Serializer>(Serializer).off`

#### Defined in

[src/mixins/event.ts:33](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L33)

***

### on()

> **on**\<`T`\>(`eventType`, `callback`): `string`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| `"update"`

#### Parameters

• **eventType**: `T`

• **callback**

#### Returns

`string`

#### Inherited from

`EventEmitterMixin<Events, typeof Serializer>(Serializer).on`

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### resolve()

> **resolve**(`eventType`): (`resolve`, `reject`) => `void`

#### Parameters

• **eventType**: `"*"` \| `"error"` \| `"update"`

#### Returns

`Function`

##### Parameters

• **resolve**

• **reject**

##### Returns

`void`

#### Inherited from

`EventEmitterMixin<Events, typeof Serializer>(Serializer).resolve`

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

`EventEmitterMixin<Events, typeof Serializer>(Serializer).toJSON`

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

`EventEmitterMixin<Events, typeof Serializer>(Serializer).fromJSON`

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Store

# Class: Store

## Constructors

### new Store()

> **new Store**(`namespace`?, `storageEngine`?): [`Store`](Store.md)

#### Parameters

• **namespace?**: `string`

• **storageEngine?**: `Storage` = `localStorage`

#### Returns

[`Store`](Store.md)

#### Defined in

[src/services/store.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/store.ts#L9)

## Properties

### namespace?

> `readonly` `optional` **namespace**: `string`

#### Defined in

[src/services/store.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/store.ts#L7)

***

### storageEngine

> `readonly` **storageEngine**: `Storage`

#### Defined in

[src/services/store.ts:6](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/store.ts#L6)

## Methods

### define()

> **define**\<`T`\>(`key`, `defaultValue`, `deserializer`?): [`StorageItem`](StorageItem.md)\<`T`\>

#### Type Parameters

• **T**

#### Parameters

• **key**: `string`

• **defaultValue**: `T`

• **deserializer?**: [`Deserializer`](../type-aliases/Deserializer.md)\<`T`\>

#### Returns

[`StorageItem`](StorageItem.md)\<`T`\>

#### Defined in

[src/services/store.ts:14](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/store.ts#L14)

***

### get()

> **get**\<`T`\>(`key`): `null` \| `T`

#### Type Parameters

• **T**

#### Parameters

• **key**: `string`

#### Returns

`null` \| `T`

#### Defined in

[src/services/store.ts:37](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/store.ts#L37)

***

### remove()

> **remove**(`key`): `void`

#### Parameters

• **key**: `string`

#### Returns

`void`

#### Defined in

[src/services/store.ts:47](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/store.ts#L47)

***

### set()

> **set**\<`T`\>(`key`, `value`): `void`

#### Type Parameters

• **T**

#### Parameters

• **key**: `string`

• **value**: `T`

#### Returns

`void`

#### Defined in

[src/services/store.ts:28](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/store.ts#L28)

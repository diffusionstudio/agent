[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Timestamp

# Class: Timestamp

Defines a time indication object that uses
milliseconds rounded to the nearest integer
and 30fps internally. By default the time is 0

## Implements

- `Omit`\<[`Serializer`](Serializer.md), `"id"`\>

## Constructors

### new Timestamp()

> **new Timestamp**(`milliseconds`): [`Timestamp`](Timestamp.md)

Create a new timestamp from **milliseconds**

#### Parameters

• **milliseconds**: `number` = `0`

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/models/timestamp.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L21)

## Accessors

### frames

> `get` **frames**(): [`frame`](../type-aliases/frame.md)

Defines the time in frames at the
current frame rate

> `set` **frames**(`value`): `void`

#### Parameters

• **value**: [`frame`](../type-aliases/frame.md)

#### Returns

[`frame`](../type-aliases/frame.md)

#### Defined in

[src/models/timestamp.ts:40](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L40)

***

### millis

> `get` **millis**(): `number`

Base unit of the timestamp

> `set` **millis**(`value`): `void`

#### Parameters

• **value**: `number`

#### Returns

`number`

#### Defined in

[src/models/timestamp.ts:28](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L28)

***

### seconds

> `get` **seconds**(): `number`

Convert the timestamp to seconds

> `set` **seconds**(`value`): `void`

#### Parameters

• **value**: `number`

#### Returns

`number`

#### Defined in

[src/models/timestamp.ts:51](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L51)

## Methods

### add()

> **add**(`time`): [`Timestamp`](Timestamp.md)

add two timestamps the timestamp being added will adapt
its fps to the current fps

#### Parameters

• **time**: [`Timestamp`](Timestamp.md)

#### Returns

[`Timestamp`](Timestamp.md)

A new Timestamp instance with the added frames

#### Defined in

[src/models/timestamp.ts:84](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L84)

***

### addFrames()

> **addFrames**(`value`): `this`

Equivalent to frames += x

#### Parameters

• **value**: [`frame`](../type-aliases/frame.md)

#### Returns

`this`

#### Defined in

[src/models/timestamp.ts:71](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L71)

***

### addMillis()

> **addMillis**(`value`): `this`

Equivalent to millis += x

#### Parameters

• **value**: `number`

#### Returns

`this`

#### Defined in

[src/models/timestamp.ts:62](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L62)

***

### copy()

> **copy**(): [`Timestamp`](Timestamp.md)

get a copy of the object

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/models/timestamp.ts:121](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L121)

***

### subtract()

> **subtract**(`time`): [`Timestamp`](Timestamp.md)

subtract two timestamps timestamp being subtracted
will adapt its fps to the current fps

#### Parameters

• **time**: [`Timestamp`](Timestamp.md)

#### Returns

[`Timestamp`](Timestamp.md)

A new Timestamp instance with the added frames

#### Defined in

[src/models/timestamp.ts:93](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L93)

***

### toJSON()

> **toJSON**(): `number`

#### Returns

`number`

#### Implementation of

`Omit.toJSON`

#### Defined in

[src/models/timestamp.ts:125](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L125)

***

### fromFrames()

> `static` **fromFrames**(`value`, `fps`?): [`Timestamp`](Timestamp.md)

Create a new timestamp from frames

#### Parameters

• **value**: [`frame`](../type-aliases/frame.md)

• **fps?**: `number`

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/models/timestamp.ts:111](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L111)

***

### fromJSON()

> `static` **fromJSON**(`value`): [`Timestamp`](Timestamp.md)

#### Parameters

• **value**: `number`

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/models/timestamp.ts:129](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L129)

***

### fromSeconds()

> `static` **fromSeconds**(`value`): [`Timestamp`](Timestamp.md)

Create a new timestamp from seconds

#### Parameters

• **value**: `number`

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/models/timestamp.ts:101](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/timestamp.ts#L101)

[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / BaseError

# Class: BaseError

## Extends

- `Error`

## Extended by

- [`IOError`](IOError.md)
- [`ValidationError`](ValidationError.md)
- [`EncoderError`](EncoderError.md)
- [`ReferenceError`](ReferenceError.md)

## Constructors

### new BaseError()

> **new BaseError**(`__namedParameters`, ...`args`): [`BaseError`](BaseError.md)

#### Parameters

• **\_\_namedParameters**

• **\_\_namedParameters.code**: `undefined` \| `string` = `''`

• **\_\_namedParameters.message**: `undefined` \| `string` = `''`

• ...**args**: `any`[]

#### Returns

[`BaseError`](BaseError.md)

#### Overrides

`Error.constructor`

#### Defined in

[src/errors/base-error.ts:5](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/errors/base-error.ts#L5)

## Properties

### cause?

> `optional` **cause**: `unknown`

#### Inherited from

`Error.cause`

#### Defined in

node\_modules/typescript/lib/lib.es2022.error.d.ts:24

***

### code

> `readonly` **code**: `string`

#### Defined in

[src/errors/base-error.ts:4](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/errors/base-error.ts#L4)

***

### message

> `readonly` **message**: `string`

#### Overrides

`Error.message`

#### Defined in

[src/errors/base-error.ts:3](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/errors/base-error.ts#L3)

***

### name

> **name**: `string`

#### Inherited from

`Error.name`

#### Defined in

node\_modules/typescript/lib/lib.es5.d.ts:1076

***

### stack?

> `optional` **stack**: `string`

#### Inherited from

`Error.stack`

#### Defined in

node\_modules/typescript/lib/lib.es5.d.ts:1078

***

### prepareStackTrace()?

> `static` `optional` **prepareStackTrace**: (`err`, `stackTraces`) => `any`

Optional override for formatting stack traces

#### Parameters

• **err**: `Error`

• **stackTraces**: `CallSite`[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

`Error.prepareStackTrace`

#### Defined in

node\_modules/@types/node/globals.d.ts:143

***

### stackTraceLimit

> `static` **stackTraceLimit**: `number`

#### Inherited from

`Error.stackTraceLimit`

#### Defined in

node\_modules/@types/node/globals.d.ts:145

## Methods

### captureStackTrace()

> `static` **captureStackTrace**(`targetObject`, `constructorOpt`?): `void`

Create .stack property on a target object

#### Parameters

• **targetObject**: `object`

• **constructorOpt?**: `Function`

#### Returns

`void`

#### Inherited from

`Error.captureStackTrace`

#### Defined in

node\_modules/@types/node/globals.d.ts:136

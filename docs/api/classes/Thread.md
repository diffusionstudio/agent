[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Thread

# Class: Thread\<Result\>

## Type Parameters

• **Result**

## Constructors

### new Thread()

> **new Thread**\<`Result`\>(`Worker`): [`Thread`](Thread.md)\<`Result`\>

#### Parameters

• **Worker**: [`Constructor`](../type-aliases/Constructor.md)\<`Worker`\>

#### Returns

[`Thread`](Thread.md)\<`Result`\>

#### Defined in

[src/services/thread.ts:19](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/thread.ts#L19)

## Properties

### worker

> **worker**: `Worker`

#### Defined in

[src/services/thread.ts:17](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/thread.ts#L17)

## Methods

### run()

> **run**\<`Arg`\>(`payload`?, `listner`?): `Promise`\<`TreadResponse`\<`Result`\>\>

#### Type Parameters

• **Arg**

#### Parameters

• **payload?**: `Arg`

• **listner?**: `EventListener`

#### Returns

`Promise`\<`TreadResponse`\<`Result`\>\>

#### Defined in

[src/services/thread.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/thread.ts#L24)

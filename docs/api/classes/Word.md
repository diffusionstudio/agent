[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Word

# Class: Word

## Constructors

### new Word()

> **new Word**(`text`, `start`, `stop`, `confidence`?): [`Word`](Word.md)

Create a new Word object

#### Parameters

• **text**: `string`

The string contents of the word

• **start**: `number`

Start in **milliseconds**

• **stop**: `number`

Stop in **milliseconds**

• **confidence?**: `number`

Predicition confidence

#### Returns

[`Word`](Word.md)

#### Defined in

[src/models/transcript.word.ts:36](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.word.ts#L36)

## Properties

### confidence?

> `optional` **confidence**: `number`

Defines the confidence of
the predicition

#### Defined in

[src/models/transcript.word.ts:27](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.word.ts#L27)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

A unique identifier for the word

#### Defined in

[src/models/transcript.word.ts:8](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.word.ts#L8)

***

### start

> **start**: [`Timestamp`](Timestamp.md)

Defines the time stamp at
which the text is spoken

#### Defined in

[src/models/transcript.word.ts:17](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.word.ts#L17)

***

### stop

> **stop**: [`Timestamp`](Timestamp.md)

Defines the time stamp at
which the text was spoken

#### Defined in

[src/models/transcript.word.ts:22](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.word.ts#L22)

***

### text

> **text**: `string`

Defines the text to be displayed

#### Defined in

[src/models/transcript.word.ts:12](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.word.ts#L12)

## Accessors

### duration

> `get` **duration**(): [`Timestamp`](Timestamp.md)

Defines the time between start
and stop returned as a timestamp

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/models/transcript.word.ts:47](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.word.ts#L47)

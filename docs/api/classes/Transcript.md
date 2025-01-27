[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Transcript

# Class: Transcript

## Implements

- [`Serializer`](Serializer.md)

## Constructors

### new Transcript()

> **new Transcript**(`groups`, `language`): [`Transcript`](Transcript.md)

#### Parameters

• **groups**: [`WordGroup`](WordGroup.md)[] = `[]`

• **language**: [`Language`](../enumerations/Language.md) = `Language.en`

#### Returns

[`Transcript`](Transcript.md)

#### Defined in

[src/models/transcript.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L26)

## Properties

### groups

> **groups**: [`WordGroup`](WordGroup.md)[] = `[]`

#### Defined in

[src/models/transcript.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L16)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Implementation of

[`Serializer`](Serializer.md).[`id`](Serializer.md#id)

#### Defined in

[src/models/transcript.ts:14](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L14)

***

### language

> **language**: [`Language`](../enumerations/Language.md) = `Language.en`

#### Defined in

[src/models/transcript.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L15)

## Accessors

### text

> `get` **text**(): `string`

#### Returns

`string`

#### Defined in

[src/models/transcript.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L18)

***

### words

> `get` **words**(): [`Word`](Word.md)[]

#### Returns

[`Word`](Word.md)[]

#### Defined in

[src/models/transcript.ts:22](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L22)

## Methods

### copy()

> **copy**(): [`Transcript`](Transcript.md)

Create a deep copy of the transcript

#### Returns

[`Transcript`](Transcript.md)

A new Transcript instance

#### Defined in

[src/models/transcript.ts:150](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L150)

***

### iter()

> **iter**(`__namedParameters`): `Generator`\<[`WordGroup`](WordGroup.md), `void`, `unknown`\>

Iterate over all words in groups

#### Parameters

• **\_\_namedParameters**: [`GeneratorOptions`](../type-aliases/GeneratorOptions.md)

#### Returns

`Generator`\<[`WordGroup`](WordGroup.md), `void`, `unknown`\>

#### Defined in

[src/models/transcript.ts:34](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L34)

***

### optimize()

> **optimize**(): `this`

This method will optimize the transcipt for display

#### Returns

`this`

#### Defined in

[src/models/transcript.ts:67](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L67)

***

### slice()

> **slice**(`count`, `startAtZero`): [`Transcript`](Transcript.md)

Create a new Transcript containing the
first `{count}` words

#### Parameters

• **count**: `number`

Defines the number of words required

• **startAtZero**: `boolean` = `true`

Defines if the first word should start at 0 milliseconds

#### Returns

[`Transcript`](Transcript.md)

A new Transcript instance

#### Defined in

[src/models/transcript.ts:126](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L126)

***

### toJSON()

> **toJSON**(): [`Captions`](../type-aliases/Captions.md)

#### Returns

[`Captions`](../type-aliases/Captions.md)

#### Implementation of

[`Serializer`](Serializer.md).[`toJSON`](Serializer.md#tojson)

#### Defined in

[src/models/transcript.ts:109](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L109)

***

### toSRT()

> **toSRT**(`options`): `object`

Convert the transcript into a SRT compatible
string and downloadable blob

#### Parameters

• **options**: [`GeneratorOptions`](../type-aliases/GeneratorOptions.md) = `{}`

#### Returns

`object`

##### blob

> **blob**: `Blob`

##### text

> **text**: `string`

#### Defined in

[src/models/transcript.ts:89](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L89)

***

### from()

> `static` **from**(`url`, `init`?): `Promise`\<[`Transcript`](Transcript.md)\>

Fetch captions from an external resource and parse them. JSON needs
to be of the form `{ token: string; start: number; stop: number; }[][]`

#### Parameters

• **url**: `string` \| `URL` \| `Request`

Location of the captions

• **init?**: `RequestInit`

Additional fetch parameters such as method or headers

#### Returns

`Promise`\<[`Transcript`](Transcript.md)\>

A Transcript with processed captions

#### Defined in

[src/models/transcript.ts:176](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L176)

***

### fromJSON()

> `static` **fromJSON**(`data`): [`Transcript`](Transcript.md)

#### Parameters

• **data**: [`Captions`](../type-aliases/Captions.md)

#### Returns

[`Transcript`](Transcript.md)

#### Defined in

[src/models/transcript.ts:154](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/models/transcript.ts#L154)

[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / VideoSource

# Class: VideoSource

## Extends

- `Mixin`\<*typeof* [`AudioSource`](AudioSource.md), `this`\> & [`AudioSource`](AudioSource.md)\<`this`\>

## Constructors

### new VideoSource()

> **new VideoSource**(): [`VideoSource`](VideoSource.md)

#### Returns

[`VideoSource`](VideoSource.md)

#### Inherited from

`VisualSourceMixin(AudioSource).constructor`

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

#### load?

> `optional` **load**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### update?

> `optional` **update**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### Inherited from

`VisualSourceMixin(AudioSource)._handlers`

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### added

> **added**: `boolean` = `false`

Indicates whether the source is used inside the composition

#### Inherited from

`VisualSourceMixin(AudioSource).added`

#### Defined in

[src/sources/source.ts:39](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L39)

***

### audioBuffer?

> `optional` **audioBuffer**: `AudioBuffer`

#### Inherited from

`VisualSourceMixin(AudioSource).audioBuffer`

#### Defined in

[src/sources/audio.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/audio.ts#L30)

***

### data

> **data**: `Record`\<`string`, `unknown`\> = `{}`

Data associated with the source

#### Inherited from

`VisualSourceMixin(AudioSource).data`

#### Defined in

[src/sources/source.ts:34](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L34)

***

### duration

> `readonly` **duration**: [`Timestamp`](Timestamp.md)

Duration of the source

#### Inherited from

`VisualSourceMixin(AudioSource).duration`

#### Defined in

[src/sources/audio.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/audio.ts#L24)

***

### element

> `readonly` **element**: `HTMLVideoElement`

#### Overrides

`VisualSourceMixin(AudioSource).element`

#### Defined in

[src/sources/video.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/video.ts#L13)

***

### external

> **external**: `boolean` = `false`

True if the file has been retrieved from an
external source

#### Inherited from

`VisualSourceMixin(AudioSource).external`

#### Defined in

[src/sources/source.ts:70](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L70)

***

### externalURL

> **externalURL**: `undefined` \| `string` \| `URL` \| `Request`

External url if the file has been fetched remotely

#### Inherited from

`VisualSourceMixin(AudioSource).externalURL`

#### Defined in

[src/sources/source.ts:63](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L63)

***

### file?

> `optional` **file**: `File`

Access to the data of the source

#### Inherited from

`VisualSourceMixin(AudioSource).file`

#### Defined in

[src/sources/source.ts:75](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L75)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

`VisualSourceMixin(AudioSource).id`

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### mimeType

> **mimeType**: `undefined` \| [`MimeType`](../type-aliases/MimeType.md)

Type of the file that has been loaded

#### Inherited from

`VisualSourceMixin(AudioSource).mimeType`

#### Defined in

[src/sources/source.ts:57](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L57)

***

### name

> **name**: `string` = `''`

Original name of the file e.g. clip.mp4

#### Inherited from

`VisualSourceMixin(AudioSource).name`

#### Defined in

[src/sources/source.ts:51](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L51)

***

### state

> **state**: `"READY"` \| `"LOADING"` \| `"ERROR"` \| `"IDLE"` = `'IDLE'`

Indicates if the track is loading

#### Inherited from

`VisualSourceMixin(AudioSource).state`

#### Defined in

[src/sources/source.ts:28](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L28)

***

### transcript?

> `optional` **transcript**: [`Transcript`](Transcript.md)

#### Inherited from

`VisualSourceMixin(AudioSource).transcript`

#### Defined in

[src/sources/audio.ts:29](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/audio.ts#L29)

***

### type

> `readonly` **type**: [`ClipType`](../type-aliases/ClipType.md) = `'video'`

#### Overrides

`VisualSourceMixin(AudioSource).type`

#### Defined in

[src/sources/video.ts:12](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/video.ts#L12)

## Accessors

### aspectRatio

> `get` **aspectRatio**(): `number`

The aspect ratio of the source

#### Returns

`number`

#### Inherited from

`VisualSourceMixin(AudioSource).aspectRatio`

#### Defined in

[src/sources/visual.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/visual.ts#L26)

***

### height

> `get` **height**(): `number`

The height of the source

#### Returns

`number`

#### Overrides

`VisualSourceMixin(AudioSource).height`

#### Defined in

[src/sources/video.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/video.ts#L15)

***

### objectURL

> `get` **objectURL**(): `undefined` \| `string`

The object url of the source

#### Returns

`undefined` \| `string`

#### Inherited from

`VisualSourceMixin(AudioSource).objectURL`

#### Defined in

[src/sources/source.ts:86](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L86)

***

### width

> `get` **width**(): `number`

The width of the source

#### Returns

`number`

#### Overrides

`VisualSourceMixin(AudioSource).width`

#### Defined in

[src/sources/video.ts:19](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/video.ts#L19)

## Methods

### arrayBuffer()

> **arrayBuffer**(): `Promise`\<`ArrayBuffer`\>

Get the source as an array buffer

#### Returns

`Promise`\<`ArrayBuffer`\>

#### Inherited from

`VisualSourceMixin(AudioSource).arrayBuffer`

#### Defined in

[src/sources/source.ts:189](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L189)

***

### bubble()

> **bubble**(`target`): `string`

#### Parameters

• **target**: `EventEmitter`\<`Events`, *typeof* [`Serializer`](Serializer.md)\>

#### Returns

`string`

#### Inherited from

`VisualSourceMixin(AudioSource).bubble`

#### Defined in

[src/mixins/event.ts:66](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L66)

***

### decode()

> **decode**(`numberOfChannels`, `sampleRate`, `cache`): `Promise`\<`AudioBuffer`\>

#### Parameters

• **numberOfChannels**: `number` = `2`

• **sampleRate**: `number` = `48000`

• **cache**: `boolean` = `false`

#### Returns

`Promise`\<`AudioBuffer`\>

#### Inherited from

`VisualSourceMixin(AudioSource).decode`

#### Defined in

[src/sources/audio.ts:51](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/audio.ts#L51)

***

### download()

> **download**(): `Promise`\<`void`\>

Downloads the file

#### Returns

`Promise`\<`void`\>

#### Inherited from

`VisualSourceMixin(AudioSource).download`

#### Defined in

[src/sources/source.ts:209](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L209)

***

### emit()

> **emit**\<`T`\>(`eventType`, `detail`): `void`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| keyof Events

#### Parameters

• **eventType**: `T`

• **detail**: `BaseEvents`\<`Events`\>\[`T`\]

#### Returns

`void`

#### Inherited from

`VisualSourceMixin(AudioSource).emit`

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### from()

> **from**(`input`, `init`?): `Promise`\<[`VideoSource`](VideoSource.md)\>

#### Parameters

• **input**: `string` \| `File` \| `URL` \| `Request`

• **init?**: `RequestInit`

#### Returns

`Promise`\<[`VideoSource`](VideoSource.md)\>

#### Inherited from

`VisualSourceMixin(AudioSource).from`

#### Defined in

[src/sources/source.ts:149](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L149)

***

### getFile()

> **getFile**(): `Promise`\<`File`\>

Method for retrieving the file when 
it has been loaded

#### Returns

`Promise`\<`File`\>

Loaded File

#### Overrides

`VisualSourceMixin(AudioSource).getFile`

#### Defined in

[src/sources/video.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/video.ts#L72)

***

### loaded()

> **loaded**(): `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

#### Inherited from

`VisualSourceMixin(AudioSource).loaded`

#### Defined in

[src/sources/source.ts:172](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L172)

***

### loadElement()

> `protected` **loadElement**(): `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

#### Overrides

`VisualSourceMixin(AudioSource).loadElement`

#### Defined in

[src/sources/video.ts:23](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/video.ts#L23)

***

### loadFile()

> `protected` **loadFile**(`file`): `Promise`\<`void`\>

#### Parameters

• **file**: `File`

#### Returns

`Promise`\<`void`\>

#### Inherited from

`VisualSourceMixin(AudioSource).loadFile`

#### Defined in

[src/sources/source.ts:126](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L126)

***

### loadUrl()

> `protected` **loadUrl**(`url`, `init`?): `Promise`\<`void`\>

#### Parameters

• **url**: `string` \| `URL` \| `Request`

• **init?**: `RequestInit`

#### Returns

`Promise`\<`void`\>

#### Overrides

`VisualSourceMixin(AudioSource).loadUrl`

#### Defined in

[src/sources/video.ts:48](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/video.ts#L48)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

`VisualSourceMixin(AudioSource).off`

#### Defined in

[src/mixins/event.ts:33](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L33)

***

### on()

> **on**\<`T`\>(`eventType`, `callback`): `string`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| keyof Events

#### Parameters

• **eventType**: `T`

• **callback**

#### Returns

`string`

#### Inherited from

`VisualSourceMixin(AudioSource).on`

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### remove()

> **remove**(): `Promise`\<`void`\>

Clean up the data associated with this object

#### Returns

`Promise`\<`void`\>

#### Inherited from

`VisualSourceMixin(AudioSource).remove`

#### Defined in

[src/sources/source.ts:198](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L198)

***

### resolve()

> **resolve**(`eventType`): (`resolve`, `reject`) => `void`

#### Parameters

• **eventType**: `"*"` \| `"error"` \| keyof Events

#### Returns

`Function`

##### Parameters

• **resolve**

• **reject**

##### Returns

`void`

#### Inherited from

`VisualSourceMixin(AudioSource).resolve`

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

***

### sample()

> **sample**(`options`): `Promise`\<`Float32Array`\>

Sampler that uses a window size to calculate the max value of the samples in the window.

#### Parameters

• **options**: [`SamplerOptions`](../type-aliases/SamplerOptions.md) = `{}`

Sampling options.

#### Returns

`Promise`\<`Float32Array`\>

An array of the max values of the samples in the window.

#### Inherited from

`VisualSourceMixin(AudioSource).sample`

#### Defined in

[src/sources/audio.ts:85](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/audio.ts#L85)

***

### silences()

> **silences**(`options`): `Promise`\<[`AudioSlice`](../type-aliases/AudioSlice.md)[]\>

Find silences in the audio clip. Results are cached.

uses default sample rate of 3000

#### Parameters

• **options**: [`SilenceDetectionOptions`](../type-aliases/SilenceDetectionOptions.md) = `{}`

Silences options.

#### Returns

`Promise`\<[`AudioSlice`](../type-aliases/AudioSlice.md)[]\>

An array of the silences (in ms) in the clip.

#### Inherited from

`VisualSourceMixin(AudioSource).silences`

#### Defined in

[src/sources/audio.ts:142](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/audio.ts#L142)

***

### thumbnail()

> **thumbnail**(): `Promise`\<`HTMLVideoElement`\>

#### Returns

`Promise`\<`HTMLVideoElement`\>

#### Overrides

`VisualSourceMixin(AudioSource).thumbnail`

#### Defined in

[src/sources/video.ts:87](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/video.ts#L87)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

`VisualSourceMixin(AudioSource).toJSON`

#### Defined in

[src/services/serializer.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L9)

***

### from()

> `static` **from**\<`T`\>(`this`, `input`, `init`?, `source`?): `Promise`\<`T`\>

Create a new source for the specified input

#### Type Parameters

• **T** *extends* [`Source`](Source.md)

#### Parameters

• **this**

• **input**: `string` \| `File` \| `URL` \| `Request`

• **init?**: `RequestInit`

• **source?**: `T` = `...`

#### Returns

`Promise`\<`T`\>

#### Inherited from

`VisualSourceMixin(AudioSource).from`

#### Defined in

[src/sources/source.ts:226](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L226)

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

`VisualSourceMixin(AudioSource).fromJSON`

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

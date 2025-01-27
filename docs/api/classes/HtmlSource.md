[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / HtmlSource

# Class: HtmlSource

## Extends

- `Mixin`\<*typeof* [`Source`](Source.md), `this`\> & [`Source`](Source.md)\<`this`\>

## Constructors

### new HtmlSource()

> **new HtmlSource**(): [`HtmlSource`](HtmlSource.md)

#### Returns

[`HtmlSource`](HtmlSource.md)

#### Overrides

`VisualSourceMixin(Source).constructor`

#### Defined in

[src/sources/html.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/html.ts#L18)

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

`VisualSourceMixin(Source)._handlers`

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### added

> **added**: `boolean` = `false`

Indicates whether the source is used inside the composition

#### Inherited from

`VisualSourceMixin(Source).added`

#### Defined in

[src/sources/source.ts:39](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L39)

***

### data

> **data**: `Record`\<`string`, `unknown`\> = `{}`

Data associated with the source

#### Inherited from

`VisualSourceMixin(Source).data`

#### Defined in

[src/sources/source.ts:34](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L34)

***

### duration

> `readonly` **duration**: [`Timestamp`](Timestamp.md)

Duration of the source

#### Inherited from

`VisualSourceMixin(Source).duration`

#### Defined in

[src/sources/source.ts:23](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L23)

***

### element

> **element**: `HTMLIFrameElement`

Access to the iframe that is required
for extracting the html's dimensions

#### Overrides

`VisualSourceMixin(Source).element`

#### Defined in

[src/sources/html.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/html.ts#L15)

***

### external

> **external**: `boolean` = `false`

True if the file has been retrieved from an
external source

#### Inherited from

`VisualSourceMixin(Source).external`

#### Defined in

[src/sources/source.ts:70](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L70)

***

### externalURL

> **externalURL**: `undefined` \| `string` \| `URL` \| `Request`

External url if the file has been fetched remotely

#### Inherited from

`VisualSourceMixin(Source).externalURL`

#### Defined in

[src/sources/source.ts:63](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L63)

***

### file?

> `optional` **file**: `File`

Access to the data of the source

#### Inherited from

`VisualSourceMixin(Source).file`

#### Defined in

[src/sources/source.ts:75](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L75)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

`VisualSourceMixin(Source).id`

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### mimeType

> **mimeType**: `undefined` \| [`MimeType`](../type-aliases/MimeType.md)

Type of the file that has been loaded

#### Inherited from

`VisualSourceMixin(Source).mimeType`

#### Defined in

[src/sources/source.ts:57](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L57)

***

### name

> **name**: `string` = `''`

Original name of the file e.g. clip.mp4

#### Inherited from

`VisualSourceMixin(Source).name`

#### Defined in

[src/sources/source.ts:51](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L51)

***

### state

> **state**: `"READY"` \| `"LOADING"` \| `"ERROR"` \| `"IDLE"` = `'IDLE'`

Indicates if the track is loading

#### Inherited from

`VisualSourceMixin(Source).state`

#### Defined in

[src/sources/source.ts:28](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L28)

***

### type

> `readonly` **type**: [`ClipType`](../type-aliases/ClipType.md) = `'html'`

Type of the source which is compatible
with clips and tracks

#### Overrides

`VisualSourceMixin(Source).type`

#### Defined in

[src/sources/html.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/html.ts#L9)

## Accessors

### aspectRatio

> `get` **aspectRatio**(): `number`

The aspect ratio of the source

#### Returns

`number`

#### Inherited from

`VisualSourceMixin(Source).aspectRatio`

#### Defined in

[src/sources/visual.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/visual.ts#L26)

***

### document

> `get` **document**(): `undefined` \| `Document`

Access to the html document as loaded
within the iframe. Can be manipulated with
javascript

#### Returns

`undefined` \| `Document`

#### Defined in

[src/sources/html.ts:43](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/html.ts#L43)

***

### height

> `get` **height**(): `number`

The height of the source

#### Returns

`number`

#### Overrides

`VisualSourceMixin(Source).height`

#### Defined in

[src/sources/html.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/html.ts#L30)

***

### imageUrl

> `get` **imageUrl**(): `string`

#### Returns

`string`

#### Defined in

[src/sources/html.ts:47](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/html.ts#L47)

***

### objectURL

> `get` **objectURL**(): `undefined` \| `string`

The object url of the source

#### Returns

`undefined` \| `string`

#### Inherited from

`VisualSourceMixin(Source).objectURL`

#### Defined in

[src/sources/source.ts:86](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L86)

***

### width

> `get` **width**(): `number`

The width of the source

#### Returns

`number`

#### Overrides

`VisualSourceMixin(Source).width`

#### Defined in

[src/sources/html.ts:34](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/html.ts#L34)

## Methods

### arrayBuffer()

> **arrayBuffer**(): `Promise`\<`ArrayBuffer`\>

Get the source as an array buffer

#### Returns

`Promise`\<`ArrayBuffer`\>

#### Inherited from

`VisualSourceMixin(Source).arrayBuffer`

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

`VisualSourceMixin(Source).bubble`

#### Defined in

[src/mixins/event.ts:66](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L66)

***

### download()

> **download**(): `Promise`\<`void`\>

Downloads the file

#### Returns

`Promise`\<`void`\>

#### Inherited from

`VisualSourceMixin(Source).download`

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

`VisualSourceMixin(Source).emit`

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### from()

> **from**(`input`, `init`?): `Promise`\<[`HtmlSource`](HtmlSource.md)\>

#### Parameters

• **input**: `string` \| `File` \| `URL` \| `Request`

• **init?**: `RequestInit`

#### Returns

`Promise`\<[`HtmlSource`](HtmlSource.md)\>

#### Inherited from

`VisualSourceMixin(Source).from`

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

#### Inherited from

`VisualSourceMixin(Source).getFile`

#### Defined in

[src/sources/source.ts:95](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L95)

***

### loaded()

> **loaded**(): `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

#### Inherited from

`VisualSourceMixin(Source).loaded`

#### Defined in

[src/sources/source.ts:172](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L172)

***

### loadElement()

> `protected` **loadElement**(): `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

#### Inherited from

`VisualSourceMixin(Source).loadElement`

#### Defined in

[src/sources/source.ts:110](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L110)

***

### loadFile()

> `protected` **loadFile**(`file`): `Promise`\<`void`\>

#### Parameters

• **file**: `File`

#### Returns

`Promise`\<`void`\>

#### Inherited from

`VisualSourceMixin(Source).loadFile`

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

#### Inherited from

`VisualSourceMixin(Source).loadUrl`

#### Defined in

[src/sources/source.ts:133](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/source.ts#L133)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

`VisualSourceMixin(Source).off`

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

`VisualSourceMixin(Source).on`

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### remove()

> **remove**(): `Promise`\<`void`\>

Clean up the data associated with this object

#### Returns

`Promise`\<`void`\>

#### Inherited from

`VisualSourceMixin(Source).remove`

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

`VisualSourceMixin(Source).resolve`

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

***

### thumbnail()

> **thumbnail**(): `Promise`\<`HTMLImageElement`\>

Get a visulization of the source
as an html element

#### Returns

`Promise`\<`HTMLImageElement`\>

#### Overrides

`VisualSourceMixin(Source).thumbnail`

#### Defined in

[src/sources/html.ts:51](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/html.ts#L51)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

`VisualSourceMixin(Source).toJSON`

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

`VisualSourceMixin(Source).from`

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

`VisualSourceMixin(Source).fromJSON`

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

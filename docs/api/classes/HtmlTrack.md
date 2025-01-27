[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / HtmlTrack

# Class: HtmlTrack

## Extends

- [`Track`](Track.md)\<[`HtmlClip`](HtmlClip.md)\>

## Constructors

### new HtmlTrack()

> **new HtmlTrack**(): [`HtmlTrack`](HtmlTrack.md)

#### Returns

[`HtmlTrack`](HtmlTrack.md)

#### Inherited from

[`Track`](Track.md).[`constructor`](Track.md#constructors)

## Properties

### \_handlers

> **\_handlers**: `object` = `{}`

#### \*?

> `optional` **\***: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### attach?

> `optional` **attach**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### detach?

> `optional` **detach**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### error?

> `optional` **error**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### frame?

> `optional` **frame**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### update?

> `optional` **update**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### Inherited from

[`Track`](Track.md).[`_handlers`](Track.md#_handlers)

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### clips

> **clips**: [`HtmlClip`](HtmlClip.md)[] = `[]`

The clips to be displayed

#### Inherited from

[`Track`](Track.md).[`clips`](Track.md#clips)

#### Defined in

[src/tracks/track/track.ts:49](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L49)

***

### composition?

> `optional` **composition**: [`Composition`](Composition.md)

Reference to the composition

#### Inherited from

[`Track`](Track.md).[`composition`](Track.md#composition)

#### Defined in

[src/tracks/track/track.ts:59](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L59)

***

### data

> **data**: `Record`\<`string`, `unknown`\> = `{}`

Data associated with the track

#### Inherited from

[`Track`](Track.md).[`data`](Track.md#data)

#### Defined in

[src/tracks/track/track.ts:27](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L27)

***

### disabled

> **disabled**: `boolean` = `false`

Controls the visability of the track

#### Inherited from

[`Track`](Track.md).[`disabled`](Track.md#disabled)

#### Defined in

[src/tracks/track/track.ts:44](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L44)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

[`Track`](Track.md).[`id`](Track.md#id)

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### pointer

> **pointer**: `number` = `0`

Pointer to the expected track

#### Inherited from

[`Track`](Track.md).[`pointer`](Track.md#pointer)

#### Defined in

[src/tracks/track/track.ts:54](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L54)

***

### primary

> **primary**: `boolean` = `false`

Flag to check if the track is the primary track

#### Inherited from

[`Track`](Track.md).[`primary`](Track.md#primary)

#### Defined in

[src/tracks/track/track.ts:33](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L33)

***

### strategy

> **strategy**: `InsertStrategy`\<`"DEFAULT"` \| `"STACK"`\>

Controls how the clips should be inserted and updated

#### Inherited from

[`Track`](Track.md).[`strategy`](Track.md#strategy)

#### Defined in

[src/tracks/track/track.ts:69](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L69)

***

### type

> `readonly` **type**: `"html"` = `'html'`

Id that can be used to search by kind

#### Overrides

[`Track`](Track.md).[`type`](Track.md#type)

#### Defined in

[src/tracks/html/html.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/html/html.ts#L7)

## Accessors

### start

> `get` **start**(): [`Timestamp`](Timestamp.md)

Get the last visible frame of the clip

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

[`Track`](Track.md).[`start`](Track.md#start)

#### Defined in

[src/tracks/track/track.ts:249](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L249)

***

### stop

> `get` **stop**(): [`Timestamp`](Timestamp.md)

Get the first visible frame of the clip

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

[`Track`](Track.md).[`stop`](Track.md#stop)

#### Defined in

[src/tracks/track/track.ts:242](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L242)

## Methods

### add()

> **add**(`clip`, `index`?): `Promise`\<[`HtmlClip`](HtmlClip.md)\>

Adds a new clip to the track

#### Parameters

• **clip**: [`HtmlClip`](HtmlClip.md)

The clip to add

• **index?**: `number`

The index to insert the clip at, will be ignored if track is not stacked

#### Returns

`Promise`\<[`HtmlClip`](HtmlClip.md)\>

#### Throws

Error if the clip can't be added

#### Inherited from

[`Track`](Track.md).[`add`](Track.md#add)

#### Defined in

[src/tracks/track/track.ts:201](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L201)

***

### bubble()

> **bubble**(`target`): `string`

#### Parameters

• **target**: `EventEmitter`\<`Events`, *typeof* [`Serializer`](Serializer.md)\>

#### Returns

`string`

#### Inherited from

[`Track`](Track.md).[`bubble`](Track.md#bubble)

#### Defined in

[src/mixins/event.ts:66](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L66)

***

### clear()

> **clear**(): `void`

Remove all clips from the track

#### Returns

`void`

#### Inherited from

[`Track`](Track.md).[`clear`](Track.md#clear)

#### Defined in

[src/tracks/track/track.ts:265](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L265)

***

### connect()

> **connect**(`composition`): `this`

Connect the track with the composition

#### Parameters

• **composition**: [`Composition`](Composition.md)

#### Returns

`this`

#### Inherited from

[`Track`](Track.md).[`connect`](Track.md#connect)

#### Defined in

[src/tracks/track/track.ts:74](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L74)

***

### detach()

> **detach**(): `this`

Remove the track from the composition

#### Returns

`this`

#### Inherited from

[`Track`](Track.md).[`detach`](Track.md#detach-1)

#### Defined in

[src/tracks/track/track.ts:256](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L256)

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

[`Track`](Track.md).[`emit`](Track.md#emit)

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### layer()

> **layer**(`layer`): `this`

Change the layer of the track

#### Parameters

• **layer**: [`TrackLayer`](../type-aliases/TrackLayer.md)

#### Returns

`this`

#### Inherited from

[`Track`](Track.md).[`layer`](Track.md#layer)

#### Defined in

[src/tracks/track/track.ts:102](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L102)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

[`Track`](Track.md).[`off`](Track.md#off)

#### Defined in

[src/mixins/event.ts:33](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L33)

***

### offset()

> **offset**(`time`): `this`

Move all clips of the track at once along the timeline

#### Parameters

• **time**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

#### Returns

`this`

#### Inherited from

[`Track`](Track.md).[`offset`](Track.md#offset)

#### Defined in

[src/tracks/track/track.ts:130](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L130)

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

[`Track`](Track.md).[`on`](Track.md#on)

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### remove()

> **remove**\<`L`\>(`clip`): `undefined` \| `L`

Remove a given clip from the track

#### Type Parameters

• **L** *extends* [`HtmlClip`](HtmlClip.md)

#### Parameters

• **clip**: `L`

#### Returns

`undefined` \| `L`

`Track` when it has been successfully removed `undefined` otherwise

#### Inherited from

[`Track`](Track.md).[`remove`](Track.md#remove)

#### Defined in

[src/tracks/track/track.ts:224](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L224)

***

### render()

> **render**(`renderer`, `time`): `void`

#### Parameters

• **renderer**: [`Renderer`](Renderer.md)

• **time**: [`Timestamp`](Timestamp.md)

#### Returns

`void`

#### Inherited from

[`Track`](Track.md).[`render`](Track.md#render)

#### Defined in

[src/tracks/track/track.ts:189](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L189)

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

[`Track`](Track.md).[`resolve`](Track.md#resolve)

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

***

### seek()

> **seek**(`time`): `void`

Seek the provided time if the track contains
audio or video clips

#### Parameters

• **time**: [`Timestamp`](Timestamp.md)

#### Returns

`void`

#### Inherited from

[`Track`](Track.md).[`seek`](Track.md#seek)

#### Defined in

[src/tracks/track/track.ts:125](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L125)

***

### stacked()

> **stacked**(`value`): `this`

Applies the stack property

#### Parameters

• **value**: `boolean` = `true`

#### Returns

`this`

#### Inherited from

[`Track`](Track.md).[`stacked`](Track.md#stacked)

#### Defined in

[src/tracks/track/track.ts:85](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L85)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

[`Track`](Track.md).[`toJSON`](Track.md#tojson)

#### Defined in

[src/services/serializer.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L9)

***

### update()

> **update**(`renderer`, `time`, `mode`, `fps`): `void` \| `Promise`\<`void`\>

Triggered when the track is redrawn

#### Parameters

• **renderer**: [`Renderer`](Renderer.md)

• **time**: [`Timestamp`](Timestamp.md)

• **mode**: [`RenderMode`](../type-aliases/RenderMode.md) = `'pause'`

• **fps**: `number` = `FPS_DEFAULT`

#### Returns

`void` \| `Promise`\<`void`\>

#### Inherited from

[`Track`](Track.md).[`update`](Track.md#update-1)

#### Defined in

[src/tracks/track/track.ts:143](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L143)

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

[`Track`](Track.md).[`fromJSON`](Track.md#fromjson)

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

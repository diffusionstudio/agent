[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / VideoTrack

# Class: VideoTrack

## Extends

- [`MediaTrack`](MediaTrack.md)\<[`VideoClip`](VideoClip.md)\>

## Constructors

### new VideoTrack()

> **new VideoTrack**(): [`VideoTrack`](VideoTrack.md)

#### Returns

[`VideoTrack`](VideoTrack.md)

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`constructor`](MediaTrack.md#constructors)

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

[`MediaTrack`](MediaTrack.md).[`_handlers`](MediaTrack.md#_handlers)

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### clips

> **clips**: [`VideoClip`](VideoClip.md)[] = `[]`

The clips to be displayed

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`clips`](MediaTrack.md#clips)

#### Defined in

[src/tracks/media/media.ts:8](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/media/media.ts#L8)

***

### composition?

> `optional` **composition**: [`Composition`](Composition.md)

Reference to the composition

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`composition`](MediaTrack.md#composition)

#### Defined in

[src/tracks/track/track.ts:59](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L59)

***

### data

> **data**: `Record`\<`string`, `unknown`\> = `{}`

Data associated with the track

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`data`](MediaTrack.md#data)

#### Defined in

[src/tracks/track/track.ts:27](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L27)

***

### disabled

> **disabled**: `boolean` = `false`

Controls the visability of the track

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`disabled`](MediaTrack.md#disabled)

#### Defined in

[src/tracks/track/track.ts:44](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L44)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`id`](MediaTrack.md#id)

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### pointer

> **pointer**: `number` = `0`

Pointer to the expected track

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`pointer`](MediaTrack.md#pointer)

#### Defined in

[src/tracks/track/track.ts:54](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L54)

***

### primary

> **primary**: `boolean` = `false`

Flag to check if the track is the primary track

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`primary`](MediaTrack.md#primary)

#### Defined in

[src/tracks/track/track.ts:33](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L33)

***

### strategy

> **strategy**: `InsertStrategy`\<`"DEFAULT"` \| `"STACK"`\>

Controls how the clips should be inserted and updated

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`strategy`](MediaTrack.md#strategy)

#### Defined in

[src/tracks/track/track.ts:69](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L69)

***

### type

> `readonly` **type**: `"video"` = `'video'`

Id that can be used to search by kind

#### Overrides

[`MediaTrack`](MediaTrack.md).[`type`](MediaTrack.md#type)

#### Defined in

[src/tracks/video/video.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/video/video.ts#L7)

## Accessors

### start

> `get` **start**(): [`Timestamp`](Timestamp.md)

Get the last visible frame of the clip

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`start`](MediaTrack.md#start)

#### Defined in

[src/tracks/track/track.ts:249](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L249)

***

### stop

> `get` **stop**(): [`Timestamp`](Timestamp.md)

Get the first visible frame of the clip

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`stop`](MediaTrack.md#stop)

#### Defined in

[src/tracks/track/track.ts:242](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L242)

## Methods

### add()

> **add**(`clip`, `index`?): `Promise`\<[`MediaClip`](MediaClip.md)\>

Adds a new clip to the track

#### Parameters

• **clip**: [`MediaClip`](MediaClip.md)

The clip to add

• **index?**: `number`

The index to insert the clip at, will be ignored if track is not stacked

#### Returns

`Promise`\<[`MediaClip`](MediaClip.md)\>

#### Throws

Error if the clip can't be added

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`add`](MediaTrack.md#add)

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

[`MediaTrack`](MediaTrack.md).[`bubble`](MediaTrack.md#bubble)

#### Defined in

[src/mixins/event.ts:66](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L66)

***

### clear()

> **clear**(): `void`

Remove all clips from the track

#### Returns

`void`

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`clear`](MediaTrack.md#clear)

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

[`MediaTrack`](MediaTrack.md).[`connect`](MediaTrack.md#connect)

#### Defined in

[src/tracks/track/track.ts:74](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L74)

***

### detach()

> **detach**(): `this`

Remove the track from the composition

#### Returns

`this`

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`detach`](MediaTrack.md#detach-1)

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

[`MediaTrack`](MediaTrack.md).[`emit`](MediaTrack.md#emit)

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

[`MediaTrack`](MediaTrack.md).[`layer`](MediaTrack.md#layer)

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

[`MediaTrack`](MediaTrack.md).[`off`](MediaTrack.md#off)

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

[`MediaTrack`](MediaTrack.md).[`offset`](MediaTrack.md#offset)

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

[`MediaTrack`](MediaTrack.md).[`on`](MediaTrack.md#on)

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### remove()

> **remove**\<`L`\>(`clip`): `undefined` \| `L`

Remove a given clip from the track

#### Type Parameters

• **L** *extends* [`MediaClip`](MediaClip.md)

#### Parameters

• **clip**: `L`

#### Returns

`undefined` \| `L`

`Track` when it has been successfully removed `undefined` otherwise

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`remove`](MediaTrack.md#remove)

#### Defined in

[src/tracks/track/track.ts:224](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L224)

***

### removeSilences()

> **removeSilences**(`options`): `Promise`\<`void`\>

Remove silences from all clips in the track

#### Parameters

• **options**: [`SilenceRemoveOptions`](../type-aliases/SilenceRemoveOptions.md) = `{}`

Options for silence detection

#### Returns

`Promise`\<`void`\>

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`removeSilences`](MediaTrack.md#removesilences)

#### Defined in

[src/tracks/media/media.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/media/media.ts#L20)

***

### render()

> **render**(`renderer`, `time`): `void`

#### Parameters

• **renderer**: [`Renderer`](Renderer.md)

• **time**: [`Timestamp`](Timestamp.md)

#### Returns

`void`

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`render`](MediaTrack.md#render)

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

[`MediaTrack`](MediaTrack.md).[`resolve`](MediaTrack.md#resolve)

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

***

### seek()

> **seek**(`time`): `Promise`\<`void`\>

Seek the provided time if the track contains
audio or video clips

#### Parameters

• **time**: [`Timestamp`](Timestamp.md)

#### Returns

`Promise`\<`void`\>

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`seek`](MediaTrack.md#seek)

#### Defined in

[src/tracks/media/media.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/media/media.ts#L9)

***

### stacked()

> **stacked**(`value`): `this`

Applies the stack property

#### Parameters

• **value**: `boolean` = `true`

#### Returns

`this`

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`stacked`](MediaTrack.md#stacked)

#### Defined in

[src/tracks/track/track.ts:85](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/tracks/track/track.ts#L85)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

[`MediaTrack`](MediaTrack.md).[`toJSON`](MediaTrack.md#tojson)

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

[`MediaTrack`](MediaTrack.md).[`update`](MediaTrack.md#update-1)

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

[`MediaTrack`](MediaTrack.md).[`fromJSON`](MediaTrack.md#fromjson)

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

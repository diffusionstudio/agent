[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Composition

# Class: Composition

## Extends

- `EventEmitter`\<[`CompositionEvents`](../type-aliases/CompositionEvents.md), *typeof* [`Serializer`](Serializer.md), `this`\> & [`Serializer`](Serializer.md)\<`this`\>

## Constructors

### new Composition()

> **new Composition**(`__namedParameters`): [`Composition`](Composition.md)

#### Parameters

• **\_\_namedParameters**: `Partial`\<[`CompositionSettings`](../type-aliases/CompositionSettings.md)\> = `{}`

#### Returns

[`Composition`](Composition.md)

#### Overrides

`EventEmitterMixin<CompositionEvents, typeof Serializer>(Serializer).constructor`

#### Defined in

[src/composition/composition.ts:39](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L39)

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

#### currentframe?

> `optional` **currentframe**: `object`

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

#### init?

> `optional` **init**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### load?

> `optional` **load**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### pause?

> `optional` **pause**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### play?

> `optional` **play**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### resize?

> `optional` **resize**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### update?

> `optional` **update**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### Inherited from

`EventEmitterMixin<CompositionEvents, typeof Serializer>(Serializer)._handlers`

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

`EventEmitterMixin<CompositionEvents, typeof Serializer>(Serializer).id`

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### renderer

> **renderer**: [`Renderer`](Renderer.md)

Access to the gpu renderer

#### Defined in

[src/composition/composition.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L24)

***

### ticker

> **ticker**: `Ticker`

The ticker used for rendering the composition

#### Defined in

[src/composition/composition.ts:34](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L34)

***

### tracks

> **tracks**: [`Track`](Track.md)\<[`Clip`](Clip.md)\>[] = `[]`

Tracks attached to the composition

#### Defined in

[src/composition/composition.ts:29](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L29)

## Accessors

### duration

> `get` **duration**(): [`Timestamp`](Timestamp.md)

This is where the playback stops playing

> `set` **duration**(`time`): `void`

Limit the total duration of the composition

#### Parameters

• **time**: `undefined` \| [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/composition/composition.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L78)

***

### height

> `get` **height**(): `number`

Get the current height of the canvas

#### Returns

`number`

#### Defined in

[src/composition/composition.ts:71](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L71)

***

### settings

> `get` **settings**(): [`CompositionSettings`](../type-aliases/CompositionSettings.md)

Settings of the composition

#### Returns

[`CompositionSettings`](../type-aliases/CompositionSettings.md)

#### Defined in

[src/composition/composition.ts:53](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L53)

***

### width

> `get` **width**(): `number`

Get the current width of the canvas

#### Returns

`number`

#### Defined in

[src/composition/composition.ts:64](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L64)

## Methods

### add()

> **add**\<`L`\>(`clip`): `Promise`\<`L`\>

Convenience function for appending a track
aswell as the clip to the composition

#### Type Parameters

• **L** *extends* [`Clip`](Clip.md)

#### Parameters

• **clip**: `L`

#### Returns

`Promise`\<`L`\>

#### Defined in

[src/composition/composition.ts:161](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L161)

***

### audio()

> **audio**(`numberOfChannels`, `sampleRate`): `Promise`\<`AudioBuffer`\>

#### Parameters

• **numberOfChannels**: `number` = `2`

• **sampleRate**: `number` = `48000`

#### Returns

`Promise`\<`AudioBuffer`\>

#### Defined in

[src/composition/composition.ts:327](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L327)

***

### bubble()

> **bubble**(`target`): `string`

#### Parameters

• **target**: `EventEmitter`\<[`CompositionEvents`](../type-aliases/CompositionEvents.md), *typeof* [`Serializer`](Serializer.md)\>

#### Returns

`string`

#### Inherited from

`EventEmitterMixin<CompositionEvents, typeof Serializer>(Serializer).bubble`

#### Defined in

[src/mixins/event.ts:66](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L66)

***

### clear()

> **clear**(): `void`

Remove all tracks and clips from the composition

#### Returns

`void`

#### Defined in

[src/composition/composition.ts:378](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L378)

***

### createTrack()

> **createTrack**\<`T`\>(`type`): [`TrackMap`](../type-aliases/TrackMap.md)\[`T`\]

Create a track with the given type

#### Type Parameters

• **T** *extends* keyof [`TrackMap`](../type-aliases/TrackMap.md)

#### Parameters

• **type**: `T`

the desired type of the track

#### Returns

[`TrackMap`](../type-aliases/TrackMap.md)\[`T`\]

A new track

#### Defined in

[src/composition/composition.ts:150](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L150)

***

### emit()

> **emit**\<`T`\>(`eventType`, `detail`): `void`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| keyof CompositionEvents

#### Parameters

• **eventType**: `T`

• **detail**: `BaseEvents`\<[`CompositionEvents`](../type-aliases/CompositionEvents.md)\>\[`T`\]

#### Returns

`void`

#### Inherited from

`EventEmitterMixin<CompositionEvents, typeof Serializer>(Serializer).emit`

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### findClips()

> **findClips**\<`T`\>(`predicate`): `T`[]

Find clips that match the profided parameters

#### Type Parameters

• **T** *extends* [`Clip`](Clip.md)

#### Parameters

• **predicate**: (`value`) => `boolean` \| () => `T`

#### Returns

`T`[]

#### Defined in

[src/composition/composition.ts:214](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L214)

***

### findTracks()

> **findTracks**\<`T`\>(`predicate`): `T`[]

Find tracks that match the profided parameters

#### Type Parameters

• **T** *extends* [`Track`](Track.md)\<[`Clip`](Clip.md)\>

#### Parameters

• **predicate**: (`value`) => `boolean` \| () => `T`

#### Returns

`T`[]

#### Defined in

[src/composition/composition.ts:195](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L195)

***

### insertTrack()

> **insertTrack**\<`L`\>(`Track`, `index`): `L`

Insert a new track at the specified index (defaults to 0)

#### Type Parameters

• **L** *extends* [`Track`](Track.md)\<[`Clip`](Clip.md)\>

#### Parameters

• **Track**: `L` \| () => `L`

The track to insert

• **index**: `number` = `0`

The index to insert at (0 = top layer, default: 0)

#### Returns

`L`

#### Defined in

[src/composition/composition.ts:134](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L134)

***

### mount()

> **mount**(`element`): `void`

Add the renderer to the dom.
This will start the ticker

#### Parameters

• **element**: `HTMLElement`

#### Returns

`void`

#### Defined in

[src/composition/composition.ts:113](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L113)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

`EventEmitterMixin<CompositionEvents, typeof Serializer>(Serializer).off`

#### Defined in

[src/mixins/event.ts:33](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L33)

***

### on()

> **on**\<`T`\>(`eventType`, `callback`): `string`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| keyof CompositionEvents

#### Parameters

• **eventType**: `T`

• **callback**

#### Returns

`string`

#### Inherited from

`EventEmitterMixin<CompositionEvents, typeof Serializer>(Serializer).on`

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### pause()

> **pause**(): `Promise`\<`void`\>

Pause the composition

#### Returns

`Promise`\<`void`\>

#### Defined in

[src/composition/composition.ts:322](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L322)

***

### play()

> **play**(): `Promise`\<`void`\>

Play the composition

#### Returns

`Promise`\<`void`\>

#### Defined in

[src/composition/composition.ts:304](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L304)

***

### remove()

> **remove**\<`L`\>(`clip`): `undefined` \| `L`

Remove a given clip from the composition

#### Type Parameters

• **L** *extends* [`Clip`](Clip.md)

#### Parameters

• **clip**: `L`

#### Returns

`undefined` \| `L`

`Clip` when it has been successfully removed `undefined` otherwise

#### Defined in

[src/composition/composition.ts:172](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L172)

***

### removeTrack()

> **removeTrack**\<`T`\>(`track`): `undefined` \| `T`

Remove a given track from the composition

#### Type Parameters

• **T** *extends* [`Track`](Track.md)\<[`Clip`](Clip.md)\>

#### Parameters

• **track**: `T`

#### Returns

`undefined` \| `T`

`Track` when it has been successfully removed `undefined` otherwise

#### Defined in

[src/composition/composition.ts:409](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L409)

***

### removeTracks()

> **removeTracks**(`Track`): [`Track`](Track.md)\<[`Clip`](Clip.md)\>[]

Remove all tracks that are of the specified type

#### Parameters

• **Track**

#### Returns

[`Track`](Track.md)\<[`Clip`](Clip.md)\>[]

#### Defined in

[src/composition/composition.ts:184](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L184)

***

### render()

> **render**(`frame`): `void`

Compute the currently active frame

#### Parameters

• **frame**: [`frame`](../type-aliases/frame.md)

#### Returns

`void`

#### Defined in

[src/composition/composition.ts:241](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L241)

***

### resize()

> **resize**(`width`, `height`): `void`

Resize the renderer

#### Parameters

• **width**: `number`

• **height**: `number`

#### Returns

`void`

#### Defined in

[src/composition/composition.ts:103](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L103)

***

### resolve()

> **resolve**(`eventType`): (`resolve`, `reject`) => `void`

#### Parameters

• **eventType**: `"*"` \| `"error"` \| keyof CompositionEvents

#### Returns

`Function`

##### Parameters

• **resolve**

• **reject**

##### Returns

`void`

#### Inherited from

`EventEmitterMixin<CompositionEvents, typeof Serializer>(Serializer).resolve`

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

***

### screenshot()

> **screenshot**(`format`, `quality`): `string`

Take a screenshot of the still frame

#### Parameters

• **format**: [`ScreenshotImageFormat`](../type-aliases/ScreenshotImageFormat.md) = `'png'`

• **quality**: `number` = `1`

#### Returns

`string`

#### Defined in

[src/composition/composition.ts:275](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L275)

***

### seek()

> **seek**(`value`): `Promise`\<`void`\>

Set the playback position to a specific time

#### Parameters

• **value**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

new playback time

#### Returns

`Promise`\<`void`\>

#### Defined in

[src/composition/composition.ts:283](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L283)

***

### time()

> **time**(`precision`?): `string`

Get the current playback time and composition
duration formatted as `00:00 / 00:00` by default.
if **hours** is set the format is `HH:mm:ss` whereas
**milliseconds** will return `mm:ss.SSS`

#### Parameters

• **precision?**

• **precision.hours?**: `boolean`

• **precision.milliseconds?**: `boolean`

#### Returns

`string`

#### Defined in

[src/composition/composition.ts:392](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L392)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

`EventEmitterMixin<CompositionEvents, typeof Serializer>(Serializer).toJSON`

#### Defined in

[src/services/serializer.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L9)

***

### unmount()

> **unmount**(): `void`

Remove the renderer from the dom.
This will stop the ticker

#### Returns

`void`

#### Defined in

[src/composition/composition.ts:123](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L123)

***

### update()

> **update**(`frame`): `void`

Update the composition at a specific frame

#### Parameters

• **frame**: [`frame`](../type-aliases/frame.md)

#### Returns

`void`

#### Defined in

[src/composition/composition.ts:254](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/composition/composition.ts#L254)

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

`EventEmitterMixin<CompositionEvents, typeof Serializer>(Serializer).fromJSON`

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

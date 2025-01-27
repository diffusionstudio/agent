[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Clip

# Class: Clip

## Extends

- `EventEmitter`\<[`ClipEvents`](../type-aliases/ClipEvents.md), *typeof* [`Serializer`](Serializer.md), `this`\> & [`Serializer`](Serializer.md)\<`this`\>

## Extended by

- [`MediaClip`](MediaClip.md)

## Constructors

### new Clip()

> **new Clip**(`props`): [`Clip`](Clip.md)

#### Parameters

• **props**: [`ClipProps`](../interfaces/ClipProps.md) = `{}`

#### Returns

[`Clip`](Clip.md)

#### Overrides

`EventEmitterMixin<ClipEvents, typeof Serializer>(Serializer).constructor`

#### Defined in

[src/clips/clip/clip.ts:114](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L114)

## Properties

### \_delay

> **\_delay**: [`Timestamp`](Timestamp.md)

#### Defined in

[src/clips/clip/clip.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L21)

***

### \_duration

> **\_duration**: [`Timestamp`](Timestamp.md)

#### Defined in

[src/clips/clip/clip.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L24)

***

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

#### offset?

> `optional` **offset**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### update?

> `optional` **update**: `object`

##### Index Signature

 \[`x`: `string`\]: (`event`) => `void`

#### Inherited from

`EventEmitterMixin<ClipEvents, typeof Serializer>(Serializer)._handlers`

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### \_name

> **\_name**: `undefined` \| `string`

#### Defined in

[src/clips/clip/clip.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L18)

***

### animations

> **animations**: [`ClipAnimationOptions`](../type-aliases/ClipAnimationOptions.md) = `[]`

Animation properties for the clip

#### Defined in

[src/clips/clip/clip.ts:68](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L68)

***

### createdAt

> `readonly` **createdAt**: `Date`

Timestamp when the clip has been created

#### Defined in

[src/clips/clip/clip.ts:56](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L56)

***

### data

> **data**: `Record`\<`string`, `unknown`\> = `{}`

Data associated with the clip

#### Defined in

[src/clips/clip/clip.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L30)

***

### disabled

> **disabled**: `boolean` = `false`

Controls the visability of the clip

#### Defined in

[src/clips/clip/clip.ts:62](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L62)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

`EventEmitterMixin<ClipEvents, typeof Serializer>(Serializer).id`

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### initialized

> **initialized**: `boolean` = `false`

Flag to check if the clip has been initialized

#### Defined in

[src/clips/clip/clip.ts:35](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L35)

***

### rendered?

> `optional` **rendered**: `boolean` = `false`

Flag to check if the clip has been rendered

#### Defined in

[src/clips/clip/clip.ts:51](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L51)

***

### source?

> `optional` **source**: [`Source`](Source.md)

Defines the source of the clip with a
one-to-many (1:n) relationship

#### Defined in

[src/clips/clip/clip.ts:46](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L46)

***

### track?

> `optional` **track**: [`Track`](Track.md)\<[`Clip`](Clip.md)\>

Access the parent track

#### Defined in

[src/clips/clip/clip.ts:73](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L73)

***

### type

> `readonly` **type**: [`ClipType`](../type-aliases/ClipType.md) = `'base'`

Defines the type of the clip

#### Defined in

[src/clips/clip/clip.ts:40](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L40)

## Accessors

### delay

> `get` **delay**(): [`Timestamp`](Timestamp.md)

Get the delay of the clip

> `set` **delay**(`time`): `void`

Change clip's offset to zero in seconds. Can be negative

#### Parameters

• **time**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/clips/clip/clip.ts:103](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L103)

***

### duration

> `get` **duration**(): [`Timestamp`](Timestamp.md)

Get the duration of the clip

> `set` **duration**(`time`): `void`

Set the duration of the clip, needs to be positive

#### Parameters

• **time**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/clips/clip/clip.ts:110](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L110)

***

### name

> `get` **name**(): `undefined` \| `string`

Human readable identifier ot the clip

> `set` **name**(`name`): `void`

#### Parameters

• **name**: `string`

#### Returns

`undefined` \| `string`

#### Defined in

[src/clips/clip/clip.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L78)

***

### start

> `get` **start**(): [`Timestamp`](Timestamp.md)

Get the first visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/clips/clip/clip.ts:89](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L89)

***

### stop

> `get` **stop**(): [`Timestamp`](Timestamp.md)

Get the last visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Defined in

[src/clips/clip/clip.ts:96](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L96)

## Methods

### animate()

> **animate**(`time`): `this`

Set the animation time of the clip
and interpolate the values

#### Parameters

• **time**: [`Timestamp`](Timestamp.md)

the current absolute time to render

#### Returns

`this`

#### Defined in

[src/clips/clip/clip.ts:125](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L125)

***

### bubble()

> **bubble**(`target`): `string`

#### Parameters

• **target**: `EventEmitter`\<[`ClipEvents`](../type-aliases/ClipEvents.md), *typeof* [`Serializer`](Serializer.md)\>

#### Returns

`string`

#### Inherited from

`EventEmitterMixin<ClipEvents, typeof Serializer>(Serializer).bubble`

#### Defined in

[src/mixins/event.ts:66](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L66)

***

### connect()

> **connect**(`track`): `Promise`\<`void`\>

Method for connecting the track with the clip

#### Parameters

• **track**: [`Track`](Track.md)\<[`Clip`](Clip.md)\>

#### Returns

`Promise`\<`void`\>

#### Defined in

[src/clips/clip/clip.ts:148](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L148)

***

### copy()

> **copy**(): [`Clip`](Clip.md)

Create a copy of the clip

#### Returns

[`Clip`](Clip.md)

#### Defined in

[src/clips/clip/clip.ts:296](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L296)

***

### detach()

> **detach**(): `this`

Remove the clip from the track

#### Returns

`this`

#### Defined in

[src/clips/clip/clip.ts:230](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L230)

***

### emit()

> **emit**\<`T`\>(`eventType`, `detail`): `void`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| keyof ClipEvents

#### Parameters

• **eventType**: `T`

• **detail**: `BaseEvents`\<[`ClipEvents`](../type-aliases/ClipEvents.md)\>\[`T`\]

#### Returns

`void`

#### Inherited from

`EventEmitterMixin<ClipEvents, typeof Serializer>(Serializer).emit`

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### enter()

> **enter**(): `void`

Triggered when the clip enters the scene

#### Returns

`void`

#### Defined in

[src/clips/clip/clip.ts:210](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L210)

***

### exit()

> **exit**(): `void`

Triggered when the clip exits the scene

#### Returns

`void`

#### Defined in

[src/clips/clip/clip.ts:225](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L225)

***

### init()

> **init**(): `Promise`\<`void`\>

Triggered when the clip is
added to the composition

#### Returns

`Promise`\<`void`\>

#### Defined in

[src/clips/clip/clip.ts:205](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L205)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

`EventEmitterMixin<ClipEvents, typeof Serializer>(Serializer).off`

#### Defined in

[src/mixins/event.ts:33](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L33)

***

### offset()

> **offset**(`time`): `this`

Offsets the clip by a given frame number

#### Parameters

• **time**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

#### Returns

`this`

#### Defined in

[src/clips/clip/clip.ts:187](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L187)

***

### on()

> **on**\<`T`\>(`eventType`, `callback`): `string`

#### Type Parameters

• **T** *extends* `"*"` \| `"error"` \| keyof ClipEvents

#### Parameters

• **eventType**: `T`

• **callback**

#### Returns

`string`

#### Inherited from

`EventEmitterMixin<ClipEvents, typeof Serializer>(Serializer).on`

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### render()

> **render**(`renderer`, `time`): `void`

#### Parameters

• **renderer**: [`Renderer`](Renderer.md)

• **time**: [`Timestamp`](Timestamp.md)

#### Returns

`void`

#### Defined in

[src/clips/clip/clip.ts:220](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L220)

***

### resolve()

> **resolve**(`eventType`): (`resolve`, `reject`) => `void`

#### Parameters

• **eventType**: `"*"` \| `"error"` \| keyof ClipEvents

#### Returns

`Function`

##### Parameters

• **resolve**

• **reject**

##### Returns

`void`

#### Inherited from

`EventEmitterMixin<ClipEvents, typeof Serializer>(Serializer).resolve`

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

***

### split()

> **split**(`time`?): `Promise`\<[`Clip`](Clip.md)\>

Split the clip into two clips at the specified time

#### Parameters

• **time?**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

split, will use the current frame of the composition 
a fallback

#### Returns

`Promise`\<[`Clip`](Clip.md)\>

The clip that was created by performing this action

#### Defined in

[src/clips/clip/clip.ts:260](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L260)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

`EventEmitterMixin<ClipEvents, typeof Serializer>(Serializer).toJSON`

#### Defined in

[src/services/serializer.ts:9](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L9)

***

### trim()

> **trim**(`start`, `stop`): `this`

Trim the clip to the specified start and stop

#### Parameters

• **start**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md) = `...`

• **stop**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md) = `...`

#### Returns

`this`

#### Defined in

[src/clips/clip/clip.ts:239](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L239)

***

### update()

> **update**(`renderer`, `time`, `mode`, `fps`): `void` \| `Promise`\<`void`\>

Triggered for each redraw of the scene.
Can return a promise which will be awaited 
during export.

#### Parameters

• **renderer**: [`Renderer`](Renderer.md)

• **time**: [`Timestamp`](Timestamp.md)

the current time to render

• **mode**: [`RenderMode`](../type-aliases/RenderMode.md) = `'pause'`

• **fps**: `number` = `FPS_DEFAULT`

#### Returns

`void` \| `Promise`\<`void`\>

#### Defined in

[src/clips/clip/clip.ts:218](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L218)

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

`EventEmitterMixin<ClipEvents, typeof Serializer>(Serializer).fromJSON`

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

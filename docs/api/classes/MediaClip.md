[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / MediaClip

# Class: MediaClip

## Extends

- [`Clip`](Clip.md)

## Extended by

- [`AudioClip`](AudioClip.md)

## Constructors

### new MediaClip()

> **new MediaClip**(`props`): [`MediaClip`](MediaClip.md)

#### Parameters

• **props**: [`MediaClipProps`](../interfaces/MediaClipProps.md) = `{}`

#### Returns

[`MediaClip`](MediaClip.md)

#### Overrides

[`Clip`](Clip.md).[`constructor`](Clip.md#constructors)

#### Defined in

[src/clips/media/media.ts:28](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L28)

## Properties

### \_delay

> **\_delay**: [`Timestamp`](Timestamp.md)

#### Inherited from

[`Clip`](Clip.md).[`_delay`](Clip.md#_delay)

#### Defined in

[src/clips/clip/clip.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L21)

***

### \_duration

> **\_duration**: [`Timestamp`](Timestamp.md)

#### Inherited from

[`Clip`](Clip.md).[`_duration`](Clip.md#_duration)

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

[`Clip`](Clip.md).[`_handlers`](Clip.md#_handlers)

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### \_name

> **\_name**: `undefined` \| `string`

#### Inherited from

[`Clip`](Clip.md).[`_name`](Clip.md#_name)

#### Defined in

[src/clips/clip/clip.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L18)

***

### animations

> **animations**: [`ClipAnimationOptions`](../type-aliases/ClipAnimationOptions.md) = `[]`

Animation properties for the clip

#### Inherited from

[`Clip`](Clip.md).[`animations`](Clip.md#animations)

#### Defined in

[src/clips/clip/clip.ts:68](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L68)

***

### createdAt

> `readonly` **createdAt**: `Date`

Timestamp when the clip has been created

#### Inherited from

[`Clip`](Clip.md).[`createdAt`](Clip.md#createdat)

#### Defined in

[src/clips/clip/clip.ts:56](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L56)

***

### data

> **data**: `Record`\<`string`, `unknown`\> = `{}`

Data associated with the clip

#### Inherited from

[`Clip`](Clip.md).[`data`](Clip.md#data)

#### Defined in

[src/clips/clip/clip.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L30)

***

### disabled

> **disabled**: `boolean` = `false`

Controls the visability of the clip

#### Inherited from

[`Clip`](Clip.md).[`disabled`](Clip.md#disabled)

#### Defined in

[src/clips/clip/clip.ts:62](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L62)

***

### element?

> `optional` **element**: `HTMLVideoElement` \| `HTMLAudioElement`

#### Defined in

[src/clips/media/media.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L15)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

[`Clip`](Clip.md).[`id`](Clip.md#id)

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### initialized

> **initialized**: `boolean` = `false`

Flag to check if the clip has been initialized

#### Inherited from

[`Clip`](Clip.md).[`initialized`](Clip.md#initialized)

#### Defined in

[src/clips/clip/clip.ts:35](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L35)

***

### playing

> **playing**: `boolean` = `false`

Is the media currently playing

#### Defined in

[src/clips/media/media.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L20)

***

### range

> **range**: [[`Timestamp`](Timestamp.md), [`Timestamp`](Timestamp.md)]

Trimmed start and stop values

#### Defined in

[src/clips/media/media.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L26)

***

### rendered?

> `optional` **rendered**: `boolean` = `false`

Flag to check if the clip has been rendered

#### Inherited from

[`Clip`](Clip.md).[`rendered`](Clip.md#rendered)

#### Defined in

[src/clips/clip/clip.ts:51](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L51)

***

### source

> **source**: [`AudioSource`](AudioSource.md)

Defines the source of the clip with a
one-to-many (1:n) relationship

#### Overrides

[`Clip`](Clip.md).[`source`](Clip.md#source)

#### Defined in

[src/clips/media/media.ts:14](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L14)

***

### track?

> `optional` **track**: [`Track`](Track.md)\<[`Clip`](Clip.md)\>

Access the parent track

#### Inherited from

[`Clip`](Clip.md).[`track`](Clip.md#track)

#### Defined in

[src/clips/clip/clip.ts:73](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L73)

***

### type

> `readonly` **type**: [`ClipType`](../type-aliases/ClipType.md) = `'base'`

Defines the type of the clip

#### Inherited from

[`Clip`](Clip.md).[`type`](Clip.md#type)

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

#### Inherited from

[`Clip`](Clip.md).[`delay`](Clip.md#delay)

#### Defined in

[src/clips/clip/clip.ts:103](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L103)

***

### duration

> `get` **duration**(): [`Timestamp`](Timestamp.md)

Get the duration of the clip

> `set` **duration**(`time`): `void`

Get the duration of the clip

#### Parameters

• **time**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

#### Returns

[`Timestamp`](Timestamp.md)

#### Overrides

[`Clip`](Clip.md).[`duration`](Clip.md#duration)

#### Defined in

[src/clips/media/media.ts:86](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L86)

***

### muted

> `get` **muted**(): `boolean`

Defines if the clip is currently muted

#### Default

```ts
false
```

> `set` **muted**(`state`): `void`

#### Parameters

• **state**: `boolean`

#### Returns

`boolean`

#### Defined in

[src/clips/media/media.ts:113](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L113)

***

### name

> `get` **name**(): `undefined` \| `string`

Human readable identifier ot the clip

> `set` **name**(`name`): `void`

#### Parameters

• **name**: `string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`Clip`](Clip.md).[`name`](Clip.md#name)

#### Defined in

[src/clips/clip/clip.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L78)

***

### start

> `get` **start**(): [`Timestamp`](Timestamp.md)

Get the first visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Overrides

[`Clip`](Clip.md).[`start`](Clip.md#start)

#### Defined in

[src/clips/media/media.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L78)

***

### stop

> `get` **stop**(): [`Timestamp`](Timestamp.md)

Get the last visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Overrides

[`Clip`](Clip.md).[`stop`](Clip.md#stop)

#### Defined in

[src/clips/media/media.ts:82](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L82)

***

### transcript

> `get` **transcript**(): `undefined` \| [`Transcript`](Transcript.md)

Defines the transcript of the video/audio. 
Will be trimmed to the clip range.
If the duration is not set, the transcript will be returned.

> `set` **transcript**(`transcript`): `void`

#### Parameters

• **transcript**: `undefined` \| [`Transcript`](Transcript.md)

#### Returns

`undefined` \| [`Transcript`](Transcript.md)

#### Defined in

[src/clips/media/media.ts:40](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L40)

***

### volume

> `get` **volume**(): [`float`](../type-aliases/float.md)

Number between 0 and 1 defining the volume of the media

#### Default

```ts
1;
```

> `set` **volume**(`volume`): `void`

#### Parameters

• **volume**: [`float`](../type-aliases/float.md)

#### Returns

[`float`](../type-aliases/float.md)

#### Defined in

[src/clips/media/media.ts:207](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L207)

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

#### Inherited from

[`Clip`](Clip.md).[`animate`](Clip.md#animate)

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

[`Clip`](Clip.md).[`bubble`](Clip.md#bubble)

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

#### Inherited from

[`Clip`](Clip.md).[`connect`](Clip.md#connect)

#### Defined in

[src/clips/clip/clip.ts:148](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L148)

***

### copy()

> **copy**(): [`MediaClip`](MediaClip.md)

Create a copy of the clip

#### Returns

[`MediaClip`](MediaClip.md)

#### Overrides

[`Clip`](Clip.md).[`copy`](Clip.md#copy)

#### Defined in

[src/clips/media/media.ts:217](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L217)

***

### createCaptions()

> **createCaptions**(`strategy`?): `Promise`\<[`CaptionTrack`](CaptionTrack.md)\>

Generates a new caption track for the current clip using the specified captioning strategy.

#### Parameters

• **strategy?**: [`CaptionPresetStrategy`](../interfaces/CaptionPresetStrategy.md) \| () => [`CaptionPresetStrategy`](../interfaces/CaptionPresetStrategy.md)

An optional CaptionPresetStrategy to define how captions should be generated.

#### Returns

`Promise`\<[`CaptionTrack`](CaptionTrack.md)\>

#### Defined in

[src/clips/media/media.ts:263](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L263)

***

### detach()

> **detach**(): `this`

Remove the clip from the track

#### Returns

`this`

#### Inherited from

[`Clip`](Clip.md).[`detach`](Clip.md#detach-1)

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

[`Clip`](Clip.md).[`emit`](Clip.md#emit)

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### enter()

> **enter**(): `void`

Triggered when the clip enters the scene

#### Returns

`void`

#### Inherited from

[`Clip`](Clip.md).[`enter`](Clip.md#enter)

#### Defined in

[src/clips/clip/clip.ts:210](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L210)

***

### exit()

> **exit**(): `void`

Triggered when the clip exits the scene

#### Returns

`void`

#### Overrides

[`Clip`](Clip.md).[`exit`](Clip.md#exit)

#### Defined in

[src/clips/media/media.ts:158](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L158)

***

### init()

> **init**(): `Promise`\<`void`\>

Triggered when the clip is
added to the composition

#### Returns

`Promise`\<`void`\>

#### Inherited from

[`Clip`](Clip.md).[`init`](Clip.md#init)

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

[`Clip`](Clip.md).[`off`](Clip.md#off)

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

#### Inherited from

[`Clip`](Clip.md).[`offset`](Clip.md#offset-1)

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

[`Clip`](Clip.md).[`on`](Clip.md#on)

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### removeSilences()

> **removeSilences**(`options`): `Promise`\<[`MediaClip`](MediaClip.md)[]\>

Remove silences from the clip

#### Parameters

• **options**: [`SilenceRemoveOptions`](../type-aliases/SilenceRemoveOptions.md) = `{}`

Options for silence detection

#### Returns

`Promise`\<[`MediaClip`](MediaClip.md)[]\>

#### Defined in

[src/clips/media/media.ts:283](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L283)

***

### render()

> **render**(`renderer`, `time`): `void`

#### Parameters

• **renderer**: [`Renderer`](Renderer.md)

• **time**: [`Timestamp`](Timestamp.md)

#### Returns

`void`

#### Inherited from

[`Clip`](Clip.md).[`render`](Clip.md#render)

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

[`Clip`](Clip.md).[`resolve`](Clip.md#resolve)

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

***

### seek()

> **seek**(`time`): `Promise`\<`void`\>

Set the media playback to a given time

#### Parameters

• **time**: [`Timestamp`](Timestamp.md)

#### Returns

`Promise`\<`void`\>

#### Defined in

[src/clips/media/media.ts:138](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L138)

***

### split()

> **split**(`time`?): `Promise`\<[`MediaClip`](MediaClip.md)\>

Split the clip into two clips at the specified time

#### Parameters

• **time?**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

split, will use the current frame of the composition 
a fallback

#### Returns

`Promise`\<[`MediaClip`](MediaClip.md)\>

The clip that was created by performing this action

#### Overrides

[`Clip`](Clip.md).[`split`](Clip.md#split)

#### Defined in

[src/clips/media/media.ts:223](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L223)

***

### subclip()

> **subclip**(`start`?, `stop`?): `this`

Returns a slice of a media clip with trimmed start and stop

#### Parameters

• **start?**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

• **stop?**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

#### Returns

`this`

#### Defined in

[src/clips/media/media.ts:167](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L167)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

[`Clip`](Clip.md).[`toJSON`](Clip.md#tojson)

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

#### Overrides

[`Clip`](Clip.md).[`trim`](Clip.md#trim)

#### Defined in

[src/clips/media/media.ts:123](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L123)

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

#### Inherited from

[`Clip`](Clip.md).[`update`](Clip.md#update-1)

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

[`Clip`](Clip.md).[`fromJSON`](Clip.md#fromjson)

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

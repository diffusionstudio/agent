[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / AudioClip

# Class: AudioClip

## Extends

- [`MediaClip`](MediaClip.md)

## Constructors

### new AudioClip()

> **new AudioClip**(`source`?, `props`?): [`AudioClip`](AudioClip.md)

#### Parameters

• **source?**: `File` \| [`AudioSource`](AudioSource.md)

• **props?**: [`AudioClipProps`](../interfaces/AudioClipProps.md) = `{}`

#### Returns

[`AudioClip`](AudioClip.md)

#### Overrides

[`MediaClip`](MediaClip.md).[`constructor`](MediaClip.md#constructors)

#### Defined in

[src/clips/audio/audio.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/audio/audio.ts#L20)

## Properties

### \_delay

> **\_delay**: [`Timestamp`](Timestamp.md)

#### Inherited from

[`MediaClip`](MediaClip.md).[`_delay`](MediaClip.md#_delay)

#### Defined in

[src/clips/clip/clip.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L21)

***

### \_duration

> **\_duration**: [`Timestamp`](Timestamp.md)

#### Inherited from

[`MediaClip`](MediaClip.md).[`_duration`](MediaClip.md#_duration)

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

[`MediaClip`](MediaClip.md).[`_handlers`](MediaClip.md#_handlers)

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### \_name

> **\_name**: `undefined` \| `string`

#### Inherited from

[`MediaClip`](MediaClip.md).[`_name`](MediaClip.md#_name)

#### Defined in

[src/clips/clip/clip.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L18)

***

### animations

> **animations**: [`ClipAnimationOptions`](../type-aliases/ClipAnimationOptions.md) = `[]`

Animation properties for the clip

#### Inherited from

[`MediaClip`](MediaClip.md).[`animations`](MediaClip.md#animations)

#### Defined in

[src/clips/clip/clip.ts:68](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L68)

***

### createdAt

> `readonly` **createdAt**: `Date`

Timestamp when the clip has been created

#### Inherited from

[`MediaClip`](MediaClip.md).[`createdAt`](MediaClip.md#createdat)

#### Defined in

[src/clips/clip/clip.ts:56](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L56)

***

### data

> **data**: `Record`\<`string`, `unknown`\> = `{}`

Data associated with the clip

#### Inherited from

[`MediaClip`](MediaClip.md).[`data`](MediaClip.md#data)

#### Defined in

[src/clips/clip/clip.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L30)

***

### disabled

> **disabled**: `boolean` = `false`

Controls the visability of the clip

#### Inherited from

[`MediaClip`](MediaClip.md).[`disabled`](MediaClip.md#disabled)

#### Defined in

[src/clips/clip/clip.ts:62](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L62)

***

### element

> **element**: `HTMLAudioElement`

Access to the HTML5 audio element

#### Overrides

[`MediaClip`](MediaClip.md).[`element`](MediaClip.md#element)

#### Defined in

[src/clips/audio/audio.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/audio/audio.ts#L18)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

[`MediaClip`](MediaClip.md).[`id`](MediaClip.md#id)

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### initialized

> **initialized**: `boolean` = `false`

Flag to check if the clip has been initialized

#### Inherited from

[`MediaClip`](MediaClip.md).[`initialized`](MediaClip.md#initialized)

#### Defined in

[src/clips/clip/clip.ts:35](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L35)

***

### playing

> **playing**: `boolean` = `false`

Is the media currently playing

#### Inherited from

[`MediaClip`](MediaClip.md).[`playing`](MediaClip.md#playing)

#### Defined in

[src/clips/media/media.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L20)

***

### range

> **range**: [[`Timestamp`](Timestamp.md), [`Timestamp`](Timestamp.md)]

Trimmed start and stop values

#### Inherited from

[`MediaClip`](MediaClip.md).[`range`](MediaClip.md#range)

#### Defined in

[src/clips/media/media.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L26)

***

### rendered?

> `optional` **rendered**: `boolean` = `false`

Flag to check if the clip has been rendered

#### Inherited from

[`MediaClip`](MediaClip.md).[`rendered`](MediaClip.md#rendered)

#### Defined in

[src/clips/clip/clip.ts:51](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L51)

***

### source

> **source**: [`AudioSource`](AudioSource.md)

Defines the source of the clip with a
one-to-many (1:n) relationship

#### Overrides

[`MediaClip`](MediaClip.md).[`source`](MediaClip.md#source)

#### Defined in

[src/clips/audio/audio.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/audio/audio.ts#L13)

***

### track?

> `optional` **track**: [`Track`](Track.md)\<[`AudioClip`](AudioClip.md)\>

Access the parent track

#### Overrides

[`MediaClip`](MediaClip.md).[`track`](MediaClip.md#track)

#### Defined in

[src/clips/audio/audio.ts:12](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/audio/audio.ts#L12)

***

### type

> `readonly` **type**: `"audio"` = `'audio'`

Defines the type of the clip

#### Overrides

[`MediaClip`](MediaClip.md).[`type`](MediaClip.md#type)

#### Defined in

[src/clips/audio/audio.ts:11](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/audio/audio.ts#L11)

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

[`MediaClip`](MediaClip.md).[`delay`](MediaClip.md#delay)

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

#### Inherited from

[`MediaClip`](MediaClip.md).[`duration`](MediaClip.md#duration)

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

#### Inherited from

[`MediaClip`](MediaClip.md).[`muted`](MediaClip.md#muted)

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

[`MediaClip`](MediaClip.md).[`name`](MediaClip.md#name)

#### Defined in

[src/clips/clip/clip.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L78)

***

### start

> `get` **start**(): [`Timestamp`](Timestamp.md)

Get the first visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

[`MediaClip`](MediaClip.md).[`start`](MediaClip.md#start)

#### Defined in

[src/clips/media/media.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L78)

***

### stop

> `get` **stop**(): [`Timestamp`](Timestamp.md)

Get the last visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

[`MediaClip`](MediaClip.md).[`stop`](MediaClip.md#stop)

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

#### Inherited from

[`MediaClip`](MediaClip.md).[`transcript`](MediaClip.md#transcript)

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

#### Inherited from

[`MediaClip`](MediaClip.md).[`volume`](MediaClip.md#volume)

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

[`MediaClip`](MediaClip.md).[`animate`](MediaClip.md#animate)

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

[`MediaClip`](MediaClip.md).[`bubble`](MediaClip.md#bubble)

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

[`MediaClip`](MediaClip.md).[`connect`](MediaClip.md#connect)

#### Defined in

[src/clips/clip/clip.ts:148](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L148)

***

### copy()

> **copy**(): [`AudioClip`](AudioClip.md)

Create a copy of the clip

#### Returns

[`AudioClip`](AudioClip.md)

#### Overrides

[`MediaClip`](MediaClip.md).[`copy`](MediaClip.md#copy)

#### Defined in

[src/clips/audio/audio.ts:63](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/audio/audio.ts#L63)

***

### createCaptions()

> **createCaptions**(`strategy`?): `Promise`\<[`CaptionTrack`](CaptionTrack.md)\>

Generates a new caption track for the current clip using the specified captioning strategy.

#### Parameters

• **strategy?**: [`CaptionPresetStrategy`](../interfaces/CaptionPresetStrategy.md) \| () => [`CaptionPresetStrategy`](../interfaces/CaptionPresetStrategy.md)

An optional CaptionPresetStrategy to define how captions should be generated.

#### Returns

`Promise`\<[`CaptionTrack`](CaptionTrack.md)\>

#### Inherited from

[`MediaClip`](MediaClip.md).[`createCaptions`](MediaClip.md#createcaptions)

#### Defined in

[src/clips/media/media.ts:263](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L263)

***

### detach()

> **detach**(): `this`

Remove the clip from the track

#### Returns

`this`

#### Inherited from

[`MediaClip`](MediaClip.md).[`detach`](MediaClip.md#detach-1)

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

[`MediaClip`](MediaClip.md).[`emit`](MediaClip.md#emit)

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### enter()

> **enter**(): `void`

Triggered when the clip enters the scene

#### Returns

`void`

#### Inherited from

[`MediaClip`](MediaClip.md).[`enter`](MediaClip.md#enter)

#### Defined in

[src/clips/clip/clip.ts:210](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L210)

***

### exit()

> **exit**(): `void`

Triggered when the clip exits the scene

#### Returns

`void`

#### Inherited from

[`MediaClip`](MediaClip.md).[`exit`](MediaClip.md#exit)

#### Defined in

[src/clips/media/media.ts:158](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L158)

***

### init()

> **init**(): `Promise`\<`void`\>

Triggered when the clip is
added to the composition

#### Returns

`Promise`\<`void`\>

#### Overrides

[`MediaClip`](MediaClip.md).[`init`](MediaClip.md#init)

#### Defined in

[src/clips/audio/audio.ts:34](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/audio/audio.ts#L34)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

[`MediaClip`](MediaClip.md).[`off`](MediaClip.md#off)

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

[`MediaClip`](MediaClip.md).[`offset`](MediaClip.md#offset-1)

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

[`MediaClip`](MediaClip.md).[`on`](MediaClip.md#on)

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

#### Inherited from

[`MediaClip`](MediaClip.md).[`removeSilences`](MediaClip.md#removesilences)

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

[`MediaClip`](MediaClip.md).[`render`](MediaClip.md#render)

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

[`MediaClip`](MediaClip.md).[`resolve`](MediaClip.md#resolve)

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

#### Inherited from

[`MediaClip`](MediaClip.md).[`seek`](MediaClip.md#seek)

#### Defined in

[src/clips/media/media.ts:138](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L138)

***

### split()

> **split**(`time`?): `Promise`\<[`AudioClip`](AudioClip.md)\>

Split the clip into two clips at the specified time

#### Parameters

• **time?**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

split, will use the current frame of the composition 
a fallback

#### Returns

`Promise`\<[`AudioClip`](AudioClip.md)\>

The clip that was created by performing this action

#### Inherited from

[`MediaClip`](MediaClip.md).[`split`](MediaClip.md#split)

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

#### Inherited from

[`MediaClip`](MediaClip.md).[`subclip`](MediaClip.md#subclip)

#### Defined in

[src/clips/media/media.ts:167](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L167)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

[`MediaClip`](MediaClip.md).[`toJSON`](MediaClip.md#tojson)

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

#### Inherited from

[`MediaClip`](MediaClip.md).[`trim`](MediaClip.md#trim)

#### Defined in

[src/clips/media/media.ts:123](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L123)

***

### update()

> **update**(`_renderer`, `_time`, `mode`): `void` \| `Promise`\<`void`\>

Triggered for each redraw of the scene.
Can return a promise which will be awaited 
during export.

#### Parameters

• **\_renderer**: [`Renderer`](Renderer.md)

• **\_time**: [`Timestamp`](Timestamp.md)

• **mode**: [`RenderMode`](../type-aliases/RenderMode.md) = `'pause'`

#### Returns

`void` \| `Promise`\<`void`\>

#### Overrides

[`MediaClip`](MediaClip.md).[`update`](MediaClip.md#update-1)

#### Defined in

[src/clips/audio/audio.ts:55](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/audio/audio.ts#L55)

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

[`MediaClip`](MediaClip.md).[`fromJSON`](MediaClip.md#fromjson)

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

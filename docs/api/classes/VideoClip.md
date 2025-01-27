[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / VideoClip

# Class: VideoClip

## Extends

- `Mixin`\<*typeof* [`MediaClip`](MediaClip.md), `this`\> & [`MediaClip`](MediaClip.md)\<`this`\>

## Constructors

### new VideoClip()

> **new VideoClip**(`source`?, `props`?): [`VideoClip`](VideoClip.md)

#### Parameters

• **source?**: `File` \| [`VideoSource`](VideoSource.md)

• **props?**: [`VideoClipProps`](../interfaces/VideoClipProps.md) = `{}`

#### Returns

[`VideoClip`](VideoClip.md)

#### Overrides

`VisualMixin(MediaClip).constructor`

#### Defined in

[src/clips/video/video.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L30)

## Properties

### \_delay

> **\_delay**: [`Timestamp`](Timestamp.md)

#### Inherited from

`VisualMixin(MediaClip)._delay`

#### Defined in

[src/clips/clip/clip.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L21)

***

### \_duration

> **\_duration**: [`Timestamp`](Timestamp.md)

#### Inherited from

`VisualMixin(MediaClip)._duration`

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

`VisualMixin(MediaClip)._handlers`

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### \_height?

> `optional` **\_height**: `number` \| \`$\{number\}%\`

#### Inherited from

`VisualMixin(MediaClip)._height`

#### Defined in

[src/clips/mixins/visual.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L24)

***

### \_name

> **\_name**: `undefined` \| `string`

#### Inherited from

`VisualMixin(MediaClip)._name`

#### Defined in

[src/clips/clip/clip.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L18)

***

### \_width?

> `optional` **\_width**: `number` \| \`$\{number\}%\`

#### Inherited from

`VisualMixin(MediaClip)._width`

#### Defined in

[src/clips/mixins/visual.ts:27](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L27)

***

### anchorX

> **anchorX**: `number` = `0`

The anchor x position, proxy for the anchor.x property

#### Default

```ts
0
```

#### Inherited from

`VisualMixin(MediaClip).anchorX`

#### Defined in

[src/clips/mixins/visual.ts:36](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L36)

***

### anchorY

> **anchorY**: `number` = `0`

The anchor y position, proxy for the anchor.y property

#### Default

```ts
0
```

#### Inherited from

`VisualMixin(MediaClip).anchorY`

#### Defined in

[src/clips/mixins/visual.ts:43](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L43)

***

### animations

> **animations**: [`VisualMixinAnimationOptions`](../type-aliases/VisualMixinAnimationOptions.md) = `[]`

Animation properties for the clip

#### Overrides

`VisualMixin(MediaClip).animations`

#### Defined in

[src/clips/video/video.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L18)

***

### blendMode?

> `optional` **blendMode**: [`BlendMode`](../type-aliases/BlendMode.md)

Sets the type of compositing operation to apply when drawing new shapes.
https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/globalCompositeOperation

#### Default

```ts
'source-over'
```

#### Inherited from

`VisualMixin(MediaClip).blendMode`

#### Defined in

[src/clips/mixins/visual.ts:125](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L125)

***

### createdAt

> `readonly` **createdAt**: `Date`

Timestamp when the clip has been created

#### Inherited from

`VisualMixin(MediaClip).createdAt`

#### Defined in

[src/clips/clip/clip.ts:56](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L56)

***

### data

> **data**: `Record`\<`string`, `unknown`\> = `{}`

Data associated with the clip

#### Inherited from

`VisualMixin(MediaClip).data`

#### Defined in

[src/clips/clip/clip.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L30)

***

### disabled

> **disabled**: `boolean` = `false`

Controls the visability of the clip

#### Inherited from

`VisualMixin(MediaClip).disabled`

#### Defined in

[src/clips/clip/clip.ts:62](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L62)

***

### element

> **element**: `HTMLVideoElement`

Html5 video element access

#### Overrides

`VisualMixin(MediaClip).element`

#### Defined in

[src/clips/video/video.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L26)

***

### filter?

> `optional` **filter**: `string`

Defines the filter property of the Canvas 2D API. It provides 
filter effects such as blurring and grayscaling. 
It is similar to the CSS filter property and accepts the same values.
https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/filter

#### Inherited from

`VisualMixin(MediaClip).filter`

#### Defined in

[src/clips/mixins/visual.ts:117](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L117)

***

### frame?

> `optional` **frame**: `VideoFrame`

#### Defined in

[src/clips/video/video.ts:27](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L27)

***

### freeTransform

> **freeTransform**: `boolean` = `true`

If true, the clip will be free transformed

#### Default

```ts
true
```

#### Inherited from

`VisualMixin(MediaClip).freeTransform`

#### Defined in

[src/clips/mixins/visual.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L78)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

`VisualMixin(MediaClip).id`

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### initialized

> **initialized**: `boolean` = `false`

Flag to check if the clip has been initialized

#### Inherited from

`VisualMixin(MediaClip).initialized`

#### Defined in

[src/clips/clip/clip.ts:35](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L35)

***

### mask?

> `optional` **mask**: [`Mask`](Mask.md)

#### Inherited from

`VisualMixin(MediaClip).mask`

#### Defined in

[src/clips/mixins/visual.ts:29](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L29)

***

### opacity

> **opacity**: `number` = `100`

Defines the opacity of the clip as a number
between 0 and 1

#### Default

```ts
100
```

#### Inherited from

`VisualMixin(MediaClip).opacity`

#### Defined in

[src/clips/mixins/visual.ts:108](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L108)

***

### playing

> **playing**: `boolean` = `false`

Is the media currently playing

#### Inherited from

`VisualMixin(MediaClip).playing`

#### Defined in

[src/clips/media/media.ts:20](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L20)

***

### range

> **range**: [[`Timestamp`](Timestamp.md), [`Timestamp`](Timestamp.md)]

Trimmed start and stop values

#### Inherited from

`VisualMixin(MediaClip).range`

#### Defined in

[src/clips/media/media.ts:26](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L26)

***

### rendered?

> `optional` **rendered**: `boolean` = `false`

Flag to check if the clip has been rendered

#### Inherited from

`VisualMixin(MediaClip).rendered`

#### Defined in

[src/clips/clip/clip.ts:51](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L51)

***

### rotation

> **rotation**: `number` = `0`

Defines the rotation of the clip in degrees

#### Default

```ts
0
```

#### Example

```ts
90
```

#### Inherited from

`VisualMixin(MediaClip).rotation`

#### Defined in

[src/clips/mixins/visual.ts:100](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L100)

***

### scaleX

> **scaleX**: `number` = `1`

The scale x factor

#### Default

```ts
1
```

#### Inherited from

`VisualMixin(MediaClip).scaleX`

#### Defined in

[src/clips/mixins/visual.ts:50](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L50)

***

### scaleY

> **scaleY**: `number` = `1`

The scale y factor

#### Default

```ts
1
```

#### Inherited from

`VisualMixin(MediaClip).scaleY`

#### Defined in

[src/clips/mixins/visual.ts:57](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L57)

***

### source

> **source**: [`VideoSource`](VideoSource.md)

#### Overrides

`VisualMixin(MediaClip).source`

#### Defined in

[src/clips/video/video.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L15)

***

### track?

> `optional` **track**: [`Track`](Track.md)\<[`VideoClip`](VideoClip.md)\>

Access the parent track

#### Overrides

`VisualMixin(MediaClip).track`

#### Defined in

[src/clips/video/video.ts:17](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L17)

***

### translateX

> **translateX**: `number` = `0`

The translate x factor

#### Default

```ts
0
```

#### Inherited from

`VisualMixin(MediaClip).translateX`

#### Defined in

[src/clips/mixins/visual.ts:64](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L64)

***

### translateY

> **translateY**: `number` = `0`

The translate y factor

#### Default

```ts
0
```

#### Inherited from

`VisualMixin(MediaClip).translateY`

#### Defined in

[src/clips/mixins/visual.ts:71](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L71)

***

### type

> `readonly` **type**: `"video"` = `'video'`

Defines the type of the clip

#### Overrides

`VisualMixin(MediaClip).type`

#### Defined in

[src/clips/video/video.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L16)

***

### x

> **x**: `number` \| \`$\{number\}%\` = `0`

The position of the clip on the x axis.

#### Default

```ts
0
```

#### Inherited from

`VisualMixin(MediaClip).x`

#### Defined in

[src/clips/mixins/visual.ts:85](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L85)

***

### y

> **y**: `number` \| \`$\{number\}%\` = `0`

The position of the clip on the y axis.

#### Default

```ts
0
```

#### Inherited from

`VisualMixin(MediaClip).y`

#### Defined in

[src/clips/mixins/visual.ts:92](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L92)

## Accessors

### anchor

> `get` **anchor**(): [`Point`](../interfaces/Point.md)

The anchor sets the origin point of the clip. Setting the anchor to (0.5,0.5) 
means the clips' origin is centered. Setting the anchor to (1,1) would mean 
the clips' origin point will be the bottom right corner. If you pass only 
single parameter, it will set both x and y to the same value.

> `set` **anchor**(`value`): `void`

#### Parameters

• **value**: `number` \| [`Point`](../interfaces/Point.md)

#### Returns

[`Point`](../interfaces/Point.md)

#### Inherited from

`VisualMixin(MediaClip).anchor`

#### Defined in

[src/clips/mixins/visual.ts:151](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L151)

***

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

`VisualMixin(MediaClip).delay`

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

`VisualMixin(MediaClip).duration`

#### Defined in

[src/clips/media/media.ts:86](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L86)

***

### height

> `get` **height**(): `number` \| \`$\{number\}%\`

Gets the current height of the clip

> `set` **height**(`value`): `void`

#### Parameters

• **value**: `undefined` \| `number` \| \`$\{number\}%\`

#### Returns

`number` \| \`$\{number\}%\`

#### Inherited from

`VisualMixin(MediaClip).height`

#### Defined in

[src/clips/mixins/visual.ts:187](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L187)

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

`VisualMixin(MediaClip).muted`

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

`VisualMixin(MediaClip).name`

#### Defined in

[src/clips/clip/clip.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L78)

***

### position

> `get` **position**(): [`RelativePoint`](../interfaces/RelativePoint.md)

The coordinate of the object relative to the local coordinates of the parent.

#### Default

```ts
{ x: 0, y: 0 }
```

> `set` **position**(`value`): `void`

#### Parameters

• **value**: `"center"` \| [`RelativePoint`](../interfaces/RelativePoint.md)

#### Returns

[`RelativePoint`](../interfaces/RelativePoint.md)

#### Inherited from

`VisualMixin(MediaClip).position`

#### Defined in

[src/clips/mixins/visual.ts:210](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L210)

***

### scale

> `get` **scale**(): [`Point`](../interfaces/Point.md)

The scale factors of this object along the local coordinate axes.
Will be added to the scale applied by setting height and/or width

#### Default

```ts
{ x: 1, y: 1 }
```

> `set` **scale**(`value`): `void`

#### Parameters

• **value**: `number` \| [`Point`](../interfaces/Point.md)

#### Returns

[`Point`](../interfaces/Point.md)

#### Inherited from

`VisualMixin(MediaClip).scale`

#### Defined in

[src/clips/mixins/visual.ts:170](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L170)

***

### size

> `get` **size**(): [`Size`](../type-aliases/Size.md)

#### Returns

[`Size`](../type-aliases/Size.md)

#### Inherited from

`VisualMixin(MediaClip).size`

#### Defined in

[src/clips/mixins/visual.ts:225](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L225)

***

### start

> `get` **start**(): [`Timestamp`](Timestamp.md)

Get the first visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

`VisualMixin(MediaClip).start`

#### Defined in

[src/clips/media/media.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L78)

***

### stop

> `get` **stop**(): [`Timestamp`](Timestamp.md)

Get the last visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

`VisualMixin(MediaClip).stop`

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

`VisualMixin(MediaClip).transcript`

#### Defined in

[src/clips/media/media.ts:40](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L40)

***

### translate

> `get` **translate**(): [`Point`](../interfaces/Point.md)

2D position offset of the clip.

#### Default

```ts
{ x: 0, y: 0 }
```

> `set` **translate**(`value`): `void`

#### Parameters

• **value**: `number` \| [`Point`](../interfaces/Point.md)

#### Returns

[`Point`](../interfaces/Point.md)

#### Inherited from

`VisualMixin(MediaClip).translate`

#### Defined in

[src/clips/mixins/visual.ts:131](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L131)

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

`VisualMixin(MediaClip).volume`

#### Defined in

[src/clips/media/media.ts:207](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L207)

***

### width

> `get` **width**(): `number` \| \`$\{number\}%\`

Gets the current width of the clip

> `set` **width**(`value`): `void`

#### Parameters

• **value**: `undefined` \| `number` \| \`$\{number\}%\`

#### Returns

`number` \| \`$\{number\}%\`

#### Inherited from

`VisualMixin(MediaClip).width`

#### Defined in

[src/clips/mixins/visual.ts:198](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L198)

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

`VisualMixin(MediaClip).animate`

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

`VisualMixin(MediaClip).bubble`

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

`VisualMixin(MediaClip).connect`

#### Defined in

[src/clips/clip/clip.ts:148](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L148)

***

### copy()

> **copy**(): [`VideoClip`](VideoClip.md)

#### Returns

[`VideoClip`](VideoClip.md)

#### Overrides

`VisualMixin(MediaClip).copy`

#### Defined in

[src/clips/video/video.ts:119](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L119)

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

`VisualMixin(MediaClip).createCaptions`

#### Defined in

[src/clips/media/media.ts:263](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L263)

***

### detach()

> **detach**(): `this`

Remove the clip from the track

#### Returns

`this`

#### Inherited from

`VisualMixin(MediaClip).detach`

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

`VisualMixin(MediaClip).emit`

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### enter()

> **enter**(): `void`

Triggered when the clip enters the scene

#### Returns

`void`

#### Inherited from

`VisualMixin(MediaClip).enter`

#### Defined in

[src/clips/clip/clip.ts:210](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L210)

***

### exit()

> **exit**(): `void`

#### Returns

`void`

#### Overrides

`VisualMixin(MediaClip).exit`

#### Defined in

[src/clips/video/video.ts:108](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L108)

***

### init()

> **init**(): `Promise`\<`void`\>

Triggered when the clip is
added to the composition

#### Returns

`Promise`\<`void`\>

#### Overrides

`VisualMixin(MediaClip).init`

#### Defined in

[src/clips/video/video.ts:44](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L44)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

`VisualMixin(MediaClip).off`

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

`VisualMixin(MediaClip).offset`

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

`VisualMixin(MediaClip).on`

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

`VisualMixin(MediaClip).removeSilences`

#### Defined in

[src/clips/media/media.ts:283](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L283)

***

### render()

> **render**(`renderer`): `void`

#### Parameters

• **renderer**: [`Renderer`](Renderer.md)

#### Returns

`void`

#### Overrides

`VisualMixin(MediaClip).render`

#### Defined in

[src/clips/video/video.ts:83](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L83)

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

`VisualMixin(MediaClip).resolve`

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

`VisualMixin(MediaClip).seek`

#### Defined in

[src/clips/media/media.ts:138](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L138)

***

### split()

> **split**(`time`?): `Promise`\<[`VideoClip`](VideoClip.md)\>

Split the clip into two clips at the specified time

#### Parameters

• **time?**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

split, will use the current frame of the composition 
a fallback

#### Returns

`Promise`\<[`VideoClip`](VideoClip.md)\>

The clip that was created by performing this action

#### Inherited from

`VisualMixin(MediaClip).split`

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

`VisualMixin(MediaClip).subclip`

#### Defined in

[src/clips/media/media.ts:167](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L167)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

`VisualMixin(MediaClip).toJSON`

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

`VisualMixin(MediaClip).trim`

#### Defined in

[src/clips/media/media.ts:123](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/media/media.ts#L123)

***

### update()

> **update**(`_renderer`, `_time`, `mode`, `fps`): `void` \| `Promise`\<`void`\>

Triggered for each redraw of the scene.
Can return a promise which will be awaited 
during export.

#### Parameters

• **\_renderer**: [`Renderer`](Renderer.md)

• **\_time**: [`Timestamp`](Timestamp.md)

• **mode**: [`RenderMode`](../type-aliases/RenderMode.md) = `'pause'`

• **fps**: `number` = `FPS_DEFAULT`

#### Returns

`void` \| `Promise`\<`void`\>

#### Overrides

`VisualMixin(MediaClip).update`

#### Defined in

[src/clips/video/video.ts:69](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/video/video.ts#L69)

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

`VisualMixin(MediaClip).fromJSON`

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

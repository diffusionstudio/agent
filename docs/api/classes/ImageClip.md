[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / ImageClip

# Class: ImageClip

## Extends

- `Mixin`\<*typeof* [`Clip`](Clip.md), `this`\> & [`Clip`](Clip.md)\<`this`\>

## Constructors

### new ImageClip()

> **new ImageClip**(`source`?, `props`?): [`ImageClip`](ImageClip.md)

#### Parameters

• **source?**: `File` \| [`ImageSource`](ImageSource.md)

• **props?**: [`ImageClipProps`](../interfaces/ImageClipProps.md) = `{}`

#### Returns

[`ImageClip`](ImageClip.md)

#### Overrides

`VisualMixin(Clip).constructor`

#### Defined in

[src/clips/image/image.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/image/image.ts#L15)

## Properties

### \_delay

> **\_delay**: [`Timestamp`](Timestamp.md)

#### Inherited from

`VisualMixin(Clip)._delay`

#### Defined in

[src/clips/clip/clip.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L21)

***

### \_duration

> **\_duration**: [`Timestamp`](Timestamp.md)

#### Inherited from

`VisualMixin(Clip)._duration`

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

`VisualMixin(Clip)._handlers`

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### \_height?

> `optional` **\_height**: `number` \| \`$\{number\}%\`

#### Inherited from

`VisualMixin(Clip)._height`

#### Defined in

[src/clips/mixins/visual.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L24)

***

### \_name

> **\_name**: `undefined` \| `string`

#### Inherited from

`VisualMixin(Clip)._name`

#### Defined in

[src/clips/clip/clip.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L18)

***

### \_width?

> `optional` **\_width**: `number` \| \`$\{number\}%\`

#### Inherited from

`VisualMixin(Clip)._width`

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

`VisualMixin(Clip).anchorX`

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

`VisualMixin(Clip).anchorY`

#### Defined in

[src/clips/mixins/visual.ts:43](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L43)

***

### animations

> **animations**: [`VisualMixinAnimationOptions`](../type-aliases/VisualMixinAnimationOptions.md) = `[]`

Animation properties for the clip

#### Overrides

`VisualMixin(Clip).animations`

#### Defined in

[src/clips/image/image.ts:14](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/image/image.ts#L14)

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

`VisualMixin(Clip).blendMode`

#### Defined in

[src/clips/mixins/visual.ts:125](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L125)

***

### createdAt

> `readonly` **createdAt**: `Date`

Timestamp when the clip has been created

#### Inherited from

`VisualMixin(Clip).createdAt`

#### Defined in

[src/clips/clip/clip.ts:56](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L56)

***

### data

> **data**: `Record`\<`string`, `unknown`\> = `{}`

Data associated with the clip

#### Inherited from

`VisualMixin(Clip).data`

#### Defined in

[src/clips/clip/clip.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L30)

***

### disabled

> **disabled**: `boolean` = `false`

Controls the visability of the clip

#### Inherited from

`VisualMixin(Clip).disabled`

#### Defined in

[src/clips/clip/clip.ts:62](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L62)

***

### element

> **element**: `HTMLImageElement`

#### Defined in

[src/clips/image/image.ts:12](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/image/image.ts#L12)

***

### filter?

> `optional` **filter**: `string`

Defines the filter property of the Canvas 2D API. It provides 
filter effects such as blurring and grayscaling. 
It is similar to the CSS filter property and accepts the same values.
https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/filter

#### Inherited from

`VisualMixin(Clip).filter`

#### Defined in

[src/clips/mixins/visual.ts:117](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L117)

***

### freeTransform

> **freeTransform**: `boolean` = `true`

If true, the clip will be free transformed

#### Default

```ts
true
```

#### Inherited from

`VisualMixin(Clip).freeTransform`

#### Defined in

[src/clips/mixins/visual.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L78)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

`VisualMixin(Clip).id`

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### initialized

> **initialized**: `boolean` = `false`

Flag to check if the clip has been initialized

#### Inherited from

`VisualMixin(Clip).initialized`

#### Defined in

[src/clips/clip/clip.ts:35](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L35)

***

### mask?

> `optional` **mask**: [`Mask`](Mask.md)

#### Inherited from

`VisualMixin(Clip).mask`

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

`VisualMixin(Clip).opacity`

#### Defined in

[src/clips/mixins/visual.ts:108](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L108)

***

### rendered?

> `optional` **rendered**: `boolean` = `false`

Flag to check if the clip has been rendered

#### Inherited from

`VisualMixin(Clip).rendered`

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

`VisualMixin(Clip).rotation`

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

`VisualMixin(Clip).scaleX`

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

`VisualMixin(Clip).scaleY`

#### Defined in

[src/clips/mixins/visual.ts:57](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L57)

***

### source

> **source**: [`ImageSource`](ImageSource.md)

Defines the source of the clip with a
one-to-many (1:n) relationship

#### Overrides

`VisualMixin(Clip).source`

#### Defined in

[src/clips/image/image.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/image/image.ts#L13)

***

### track?

> `optional` **track**: [`Track`](Track.md)\<[`ImageClip`](ImageClip.md)\>

Access the parent track

#### Overrides

`VisualMixin(Clip).track`

#### Defined in

[src/clips/image/image.ts:11](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/image/image.ts#L11)

***

### translateX

> **translateX**: `number` = `0`

The translate x factor

#### Default

```ts
0
```

#### Inherited from

`VisualMixin(Clip).translateX`

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

`VisualMixin(Clip).translateY`

#### Defined in

[src/clips/mixins/visual.ts:71](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L71)

***

### type

> `readonly` **type**: `"image"` = `'image'`

Defines the type of the clip

#### Overrides

`VisualMixin(Clip).type`

#### Defined in

[src/clips/image/image.ts:10](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/image/image.ts#L10)

***

### x

> **x**: `number` \| \`$\{number\}%\` = `0`

The position of the clip on the x axis.

#### Default

```ts
0
```

#### Inherited from

`VisualMixin(Clip).x`

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

`VisualMixin(Clip).y`

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

`VisualMixin(Clip).anchor`

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

`VisualMixin(Clip).delay`

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

#### Inherited from

`VisualMixin(Clip).duration`

#### Defined in

[src/clips/clip/clip.ts:110](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L110)

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

`VisualMixin(Clip).height`

#### Defined in

[src/clips/mixins/visual.ts:187](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L187)

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

`VisualMixin(Clip).name`

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

`VisualMixin(Clip).position`

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

`VisualMixin(Clip).scale`

#### Defined in

[src/clips/mixins/visual.ts:170](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L170)

***

### size

> `get` **size**(): [`Size`](../type-aliases/Size.md)

#### Returns

[`Size`](../type-aliases/Size.md)

#### Inherited from

`VisualMixin(Clip).size`

#### Defined in

[src/clips/mixins/visual.ts:225](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L225)

***

### start

> `get` **start**(): [`Timestamp`](Timestamp.md)

Get the first visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

`VisualMixin(Clip).start`

#### Defined in

[src/clips/clip/clip.ts:89](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L89)

***

### stop

> `get` **stop**(): [`Timestamp`](Timestamp.md)

Get the last visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

`VisualMixin(Clip).stop`

#### Defined in

[src/clips/clip/clip.ts:96](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L96)

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

`VisualMixin(Clip).translate`

#### Defined in

[src/clips/mixins/visual.ts:131](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L131)

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

`VisualMixin(Clip).width`

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

`VisualMixin(Clip).animate`

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

`VisualMixin(Clip).bubble`

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

`VisualMixin(Clip).connect`

#### Defined in

[src/clips/clip/clip.ts:148](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L148)

***

### copy()

> **copy**(): [`ImageClip`](ImageClip.md)

Create a copy of the clip

#### Returns

[`ImageClip`](ImageClip.md)

#### Overrides

`VisualMixin(Clip).copy`

#### Defined in

[src/clips/image/image.ts:59](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/image/image.ts#L59)

***

### detach()

> **detach**(): `this`

Remove the clip from the track

#### Returns

`this`

#### Inherited from

`VisualMixin(Clip).detach`

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

`VisualMixin(Clip).emit`

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### enter()

> **enter**(): `void`

Triggered when the clip enters the scene

#### Returns

`void`

#### Inherited from

`VisualMixin(Clip).enter`

#### Defined in

[src/clips/clip/clip.ts:210](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L210)

***

### exit()

> **exit**(): `void`

Triggered when the clip exits the scene

#### Returns

`void`

#### Inherited from

`VisualMixin(Clip).exit`

#### Defined in

[src/clips/clip/clip.ts:225](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L225)

***

### init()

> **init**(): `Promise`\<`void`\>

Triggered when the clip is
added to the composition

#### Returns

`Promise`\<`void`\>

#### Overrides

`VisualMixin(Clip).init`

#### Defined in

[src/clips/image/image.ts:29](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/image/image.ts#L29)

***

### off()

> **off**(`id`?, ...`ids`?): `void`

#### Parameters

• **id?**: `string`

• ...**ids?**: `string`[]

#### Returns

`void`

#### Inherited from

`VisualMixin(Clip).off`

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

`VisualMixin(Clip).offset`

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

`VisualMixin(Clip).on`

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### render()

> **render**(`renderer`): `void`

#### Parameters

• **renderer**: [`Renderer`](Renderer.md)

#### Returns

`void`

#### Overrides

`VisualMixin(Clip).render`

#### Defined in

[src/clips/image/image.ts:34](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/image/image.ts#L34)

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

`VisualMixin(Clip).resolve`

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

***

### split()

> **split**(`time`?): `Promise`\<[`ImageClip`](ImageClip.md)\>

Split the clip into two clips at the specified time

#### Parameters

• **time?**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

split, will use the current frame of the composition 
a fallback

#### Returns

`Promise`\<[`ImageClip`](ImageClip.md)\>

The clip that was created by performing this action

#### Inherited from

`VisualMixin(Clip).split`

#### Defined in

[src/clips/clip/clip.ts:260](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L260)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

`VisualMixin(Clip).toJSON`

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

`VisualMixin(Clip).trim`

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

#### Inherited from

`VisualMixin(Clip).update`

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

`VisualMixin(Clip).fromJSON`

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

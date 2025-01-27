[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / RichTextClip

# Class: RichTextClip

## Extends

- [`TextClip`](TextClip.md)

## Constructors

### new RichTextClip()

> **new RichTextClip**(`props`): [`RichTextClip`](RichTextClip.md)

#### Parameters

• **props**: [`RichTextClipProps`](../interfaces/RichTextClipProps.md) = `{}`

#### Returns

[`RichTextClip`](RichTextClip.md)

#### Overrides

[`TextClip`](TextClip.md).[`constructor`](TextClip.md#constructors)

#### Defined in

[src/clips/text/text.rich.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.rich.ts#L30)

## Properties

### \_delay

> **\_delay**: [`Timestamp`](Timestamp.md)

#### Inherited from

[`TextClip`](TextClip.md).[`_delay`](TextClip.md#_delay)

#### Defined in

[src/clips/clip/clip.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L21)

***

### \_duration

> **\_duration**: [`Timestamp`](Timestamp.md)

#### Inherited from

[`TextClip`](TextClip.md).[`_duration`](TextClip.md#_duration)

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

[`TextClip`](TextClip.md).[`_handlers`](TextClip.md#_handlers)

#### Defined in

[src/mixins/event.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L7)

***

### \_height?

> `optional` **\_height**: `number` \| \`$\{number\}%\`

#### Inherited from

[`TextClip`](TextClip.md).[`_height`](TextClip.md#_height)

#### Defined in

[src/clips/mixins/visual.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L24)

***

### \_name

> **\_name**: `undefined` \| `string`

#### Inherited from

[`TextClip`](TextClip.md).[`_name`](TextClip.md#_name)

#### Defined in

[src/clips/clip/clip.ts:18](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L18)

***

### \_width?

> `optional` **\_width**: `number` \| \`$\{number\}%\`

#### Inherited from

[`TextClip`](TextClip.md).[`_width`](TextClip.md#_width)

#### Defined in

[src/clips/mixins/visual.ts:27](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L27)

***

### align

> **align**: [`TextAlign`](../type-aliases/TextAlign.md) = `'left'`

Alignment for multiline text, does not affect single line text.

#### Inherited from

[`TextClip`](TextClip.md).[`align`](TextClip.md#align)

#### Defined in

[src/clips/text/text.ts:49](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L49)

***

### anchorX

> **anchorX**: `number` = `0`

The anchor x position, proxy for the anchor.x property

#### Default

```ts
0
```

#### Inherited from

[`TextClip`](TextClip.md).[`anchorX`](TextClip.md#anchorx)

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

[`TextClip`](TextClip.md).[`anchorY`](TextClip.md#anchory)

#### Defined in

[src/clips/mixins/visual.ts:43](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L43)

***

### animations

> **animations**: [`TextClipAnimationOptions`](../type-aliases/TextClipAnimationOptions.md) = `[]`

Animation properties for the clip

#### Inherited from

[`TextClip`](TextClip.md).[`animations`](TextClip.md#animations)

#### Defined in

[src/clips/text/text.ts:16](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L16)

***

### background?

> `optional` **background**: [`Background`](../type-aliases/Background.md)

#### Defined in

[src/clips/text/text.rich.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.rich.ts#L25)

***

### baseline

> **baseline**: [`TextBaseline`](../type-aliases/TextBaseline.md) = `'top'`

The baseline of the text that is rendered.

#### Inherited from

[`TextClip`](TextClip.md).[`baseline`](TextClip.md#baseline)

#### Defined in

[src/clips/text/text.ts:55](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L55)

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

[`TextClip`](TextClip.md).[`blendMode`](TextClip.md#blendmode)

#### Defined in

[src/clips/mixins/visual.ts:125](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L125)

***

### casing

> **casing**: `undefined` \| [`TextCase`](../type-aliases/TextCase.md)

The casing of the text, e.g. uppercase

#### Inherited from

[`TextClip`](TextClip.md).[`casing`](TextClip.md#casing)

#### Defined in

[src/clips/text/text.ts:43](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L43)

***

### color

> **color**: \`#$\{string\}\` = `'#FFFFFF'`

A fillstyle that will be used on the text '#00FF00'.

#### Inherited from

[`TextClip`](TextClip.md).[`color`](TextClip.md#color)

#### Defined in

[src/clips/text/text.ts:28](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L28)

***

### createdAt

> `readonly` **createdAt**: `Date`

Timestamp when the clip has been created

#### Inherited from

[`TextClip`](TextClip.md).[`createdAt`](TextClip.md#createdat)

#### Defined in

[src/clips/clip/clip.ts:56](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L56)

***

### data

> **data**: `Record`\<`string`, `unknown`\> = `{}`

Data associated with the clip

#### Inherited from

[`TextClip`](TextClip.md).[`data`](TextClip.md#data)

#### Defined in

[src/clips/clip/clip.ts:30](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L30)

***

### disabled

> **disabled**: `boolean` = `false`

Controls the visability of the clip

#### Inherited from

[`TextClip`](TextClip.md).[`disabled`](TextClip.md#disabled)

#### Defined in

[src/clips/clip/clip.ts:62](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L62)

***

### filter?

> `optional` **filter**: `string`

Defines the filter property of the Canvas 2D API. It provides 
filter effects such as blurring and grayscaling. 
It is similar to the CSS filter property and accepts the same values.
https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/filter

#### Inherited from

[`TextClip`](TextClip.md).[`filter`](TextClip.md#filter)

#### Defined in

[src/clips/mixins/visual.ts:117](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L117)

***

### font

> **font**: [`Font`](../interfaces/Font.md)

The font to use for the text.

#### Inherited from

[`TextClip`](TextClip.md).[`font`](TextClip.md#font)

#### Defined in

[src/clips/text/text.ts:34](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L34)

***

### freeTransform

> **freeTransform**: `boolean` = `true`

If true, the clip will be free transformed

#### Default

```ts
true
```

#### Inherited from

[`TextClip`](TextClip.md).[`freeTransform`](TextClip.md#freetransform)

#### Defined in

[src/clips/mixins/visual.ts:78](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L78)

***

### glow

> **glow**: `undefined` \| [`Glow`](../interfaces/Glow.md)

An object describing the glow to apply

#### Inherited from

[`TextClip`](TextClip.md).[`glow`](TextClip.md#glow)

#### Defined in

[src/clips/text/text.ts:79](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L79)

***

### id

> **id**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

Unique identifier of the object

#### Inherited from

[`TextClip`](TextClip.md).[`id`](TextClip.md#id)

#### Defined in

[src/services/serializer.ts:7](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L7)

***

### initialized

> **initialized**: `boolean` = `false`

Flag to check if the clip has been initialized

#### Inherited from

[`TextClip`](TextClip.md).[`initialized`](TextClip.md#initialized)

#### Defined in

[src/clips/clip/clip.ts:35](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L35)

***

### leading

> **leading**: `number` = `1.3`

The space between lines

#### Inherited from

[`TextClip`](TextClip.md).[`leading`](TextClip.md#leading)

#### Defined in

[src/clips/text/text.ts:73](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L73)

***

### mask?

> `optional` **mask**: [`Mask`](Mask.md)

#### Inherited from

[`TextClip`](TextClip.md).[`mask`](TextClip.md#mask)

#### Defined in

[src/clips/mixins/visual.ts:29](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L29)

***

### maxWidth

> **maxWidth**: `undefined` \| `number` \| \`$\{number\}%\`

The width at which text will wrap

#### Defined in

[src/clips/text/text.rich.ts:22](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.rich.ts#L22)

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

[`TextClip`](TextClip.md).[`opacity`](TextClip.md#opacity)

#### Defined in

[src/clips/mixins/visual.ts:108](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L108)

***

### rendered?

> `optional` **rendered**: `boolean` = `false`

Flag to check if the clip has been rendered

#### Inherited from

[`TextClip`](TextClip.md).[`rendered`](TextClip.md#rendered)

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

[`TextClip`](TextClip.md).[`rotation`](TextClip.md#rotation)

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

[`TextClip`](TextClip.md).[`scaleX`](TextClip.md#scalex)

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

[`TextClip`](TextClip.md).[`scaleY`](TextClip.md#scaley)

#### Defined in

[src/clips/mixins/visual.ts:57](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L57)

***

### shadow

> **shadow**: `undefined` \| [`Shadow`](../interfaces/Shadow.md) \| [`Shadow`](../interfaces/Shadow.md)[]

Set a drop shadow for the text.

#### Inherited from

[`TextClip`](TextClip.md).[`shadow`](TextClip.md#shadow)

#### Defined in

[src/clips/text/text.ts:67](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L67)

***

### source

> **source**: [`VisualSource`](VisualSource.md) & [`Source`](Source.md)

Defines the source of the clip with a
one-to-many (1:n) relationship

#### Inherited from

[`TextClip`](TextClip.md).[`source`](TextClip.md#source)

#### Defined in

[src/clips/mixins/visual.ts:21](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L21)

***

### stroke

> **stroke**: `undefined` \| [`Stroke`](../interfaces/Stroke.md)

An object describing the stroke to apply

#### Inherited from

[`TextClip`](TextClip.md).[`stroke`](TextClip.md#stroke)

#### Defined in

[src/clips/text/text.ts:61](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L61)

***

### styles?

> `optional` **styles**: [`StyleOverride`](../type-aliases/StyleOverride.md)[]

#### Defined in

[src/clips/text/text.rich.ts:28](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.rich.ts#L28)

***

### text

> **text**: `string` = `''`

Set the copy for the text object. To split a line you can use '\n'.

#### Inherited from

[`TextClip`](TextClip.md).[`text`](TextClip.md#text)

#### Defined in

[src/clips/text/text.ts:22](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L22)

***

### track?

> `optional` **track**: [`Track`](Track.md)\<[`RichTextClip`](RichTextClip.md)\>

Access the parent track

#### Overrides

[`TextClip`](TextClip.md).[`track`](TextClip.md#track)

#### Defined in

[src/clips/text/text.rich.ts:15](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.rich.ts#L15)

***

### translateX

> **translateX**: `number` = `0`

The translate x factor

#### Default

```ts
0
```

#### Inherited from

[`TextClip`](TextClip.md).[`translateX`](TextClip.md#translatex)

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

[`TextClip`](TextClip.md).[`translateY`](TextClip.md#translatey)

#### Defined in

[src/clips/mixins/visual.ts:71](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L71)

***

### type

> `readonly` **type**: `"text"` = `'text'`

Defines the type of the clip

#### Inherited from

[`TextClip`](TextClip.md).[`type`](TextClip.md#type)

#### Defined in

[src/clips/text/text.ts:14](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L14)

***

### x

> **x**: `number` \| \`$\{number\}%\` = `0`

The position of the clip on the x axis.

#### Default

```ts
0
```

#### Inherited from

[`TextClip`](TextClip.md).[`x`](TextClip.md#x)

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

[`TextClip`](TextClip.md).[`y`](TextClip.md#y)

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

[`TextClip`](TextClip.md).[`anchor`](TextClip.md#anchor)

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

[`TextClip`](TextClip.md).[`delay`](TextClip.md#delay)

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

[`TextClip`](TextClip.md).[`duration`](TextClip.md#duration)

#### Defined in

[src/clips/clip/clip.ts:110](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L110)

***

### fontSize

> `get` **fontSize**(): `number`

Proxy for font.size

> `set` **fontSize**(`value`): `void`

#### Parameters

• **value**: `number`

#### Returns

`number`

#### Inherited from

[`TextClip`](TextClip.md).[`fontSize`](TextClip.md#fontsize)

#### Defined in

[src/clips/text/text.ts:163](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L163)

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

[`TextClip`](TextClip.md).[`height`](TextClip.md#height)

#### Defined in

[src/clips/mixins/visual.ts:187](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L187)

***

### name

> `get` **name**(): `string`

Human readable identifier ot the clip

#### Returns

`string`

#### Inherited from

[`TextClip`](TextClip.md).[`name`](TextClip.md#name)

#### Defined in

[src/clips/text/text.ts:171](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L171)

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

[`TextClip`](TextClip.md).[`position`](TextClip.md#position)

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

[`TextClip`](TextClip.md).[`scale`](TextClip.md#scale)

#### Defined in

[src/clips/mixins/visual.ts:170](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L170)

***

### shadows

> `get` **shadows**(): [`Shadow`](../interfaces/Shadow.md)[]

#### Returns

[`Shadow`](../interfaces/Shadow.md)[]

#### Inherited from

[`TextClip`](TextClip.md).[`shadows`](TextClip.md#shadows)

#### Defined in

[src/clips/text/text.ts:182](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.ts#L182)

***

### size

> `get` **size**(): [`Size`](../type-aliases/Size.md)

#### Returns

[`Size`](../type-aliases/Size.md)

#### Inherited from

[`TextClip`](TextClip.md).[`size`](TextClip.md#size)

#### Defined in

[src/clips/mixins/visual.ts:225](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/mixins/visual.ts#L225)

***

### start

> `get` **start**(): [`Timestamp`](Timestamp.md)

Get the first visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

[`TextClip`](TextClip.md).[`start`](TextClip.md#start)

#### Defined in

[src/clips/clip/clip.ts:89](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L89)

***

### stop

> `get` **stop**(): [`Timestamp`](Timestamp.md)

Get the last visible frame

#### Returns

[`Timestamp`](Timestamp.md)

#### Inherited from

[`TextClip`](TextClip.md).[`stop`](TextClip.md#stop)

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

[`TextClip`](TextClip.md).[`translate`](TextClip.md#translate)

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

[`TextClip`](TextClip.md).[`width`](TextClip.md#width)

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

[`TextClip`](TextClip.md).[`animate`](TextClip.md#animate)

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

[`TextClip`](TextClip.md).[`bubble`](TextClip.md#bubble)

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

[`TextClip`](TextClip.md).[`connect`](TextClip.md#connect)

#### Defined in

[src/clips/clip/clip.ts:148](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L148)

***

### copy()

> **copy**(): [`RichTextClip`](RichTextClip.md)

Create a copy of the clip

#### Returns

[`RichTextClip`](RichTextClip.md)

#### Overrides

[`TextClip`](TextClip.md).[`copy`](TextClip.md#copy)

#### Defined in

[src/clips/text/text.rich.ts:197](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.rich.ts#L197)

***

### detach()

> **detach**(): `this`

Remove the clip from the track

#### Returns

`this`

#### Inherited from

[`TextClip`](TextClip.md).[`detach`](TextClip.md#detach-1)

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

[`TextClip`](TextClip.md).[`emit`](TextClip.md#emit)

#### Defined in

[src/mixins/event.ts:52](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L52)

***

### enter()

> **enter**(): `void`

Triggered when the clip enters the scene

#### Returns

`void`

#### Inherited from

[`TextClip`](TextClip.md).[`enter`](TextClip.md#enter)

#### Defined in

[src/clips/clip/clip.ts:210](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L210)

***

### exit()

> **exit**(): `void`

Triggered when the clip exits the scene

#### Returns

`void`

#### Inherited from

[`TextClip`](TextClip.md).[`exit`](TextClip.md#exit)

#### Defined in

[src/clips/clip/clip.ts:225](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L225)

***

### init()

> **init**(): `Promise`\<`void`\>

Triggered when the clip is
added to the composition

#### Returns

`Promise`\<`void`\>

#### Inherited from

[`TextClip`](TextClip.md).[`init`](TextClip.md#init)

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

[`TextClip`](TextClip.md).[`off`](TextClip.md#off)

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

[`TextClip`](TextClip.md).[`offset`](TextClip.md#offset-1)

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

[`TextClip`](TextClip.md).[`on`](TextClip.md#on)

#### Defined in

[src/mixins/event.ts:13](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L13)

***

### render()

> **render**(`renderer`): `Promise`\<`void`\>

#### Parameters

• **renderer**: [`Renderer`](Renderer.md)

#### Returns

`Promise`\<`void`\>

#### Overrides

[`TextClip`](TextClip.md).[`render`](TextClip.md#render)

#### Defined in

[src/clips/text/text.rich.ts:81](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.rich.ts#L81)

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

[`TextClip`](TextClip.md).[`resolve`](TextClip.md#resolve)

#### Defined in

[src/mixins/event.ts:72](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/mixins/event.ts#L72)

***

### split()

> **split**(`time`?): `Promise`\<[`RichTextClip`](RichTextClip.md)\>

Split the clip into two clips at the specified time

#### Parameters

• **time?**: [`frame`](../type-aliases/frame.md) \| [`Timestamp`](Timestamp.md)

split, will use the current frame of the composition 
a fallback

#### Returns

`Promise`\<[`RichTextClip`](RichTextClip.md)\>

The clip that was created by performing this action

#### Inherited from

[`TextClip`](TextClip.md).[`split`](TextClip.md#split)

#### Defined in

[src/clips/clip/clip.ts:260](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L260)

***

### toJSON()

> **toJSON**(): `any`

#### Returns

`any`

#### Inherited from

[`TextClip`](TextClip.md).[`toJSON`](TextClip.md#tojson)

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

[`TextClip`](TextClip.md).[`trim`](TextClip.md#trim)

#### Defined in

[src/clips/clip/clip.ts:239](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/clip/clip.ts#L239)

***

### update()

> **update**(`renderer`): `void`

Triggered for each redraw of the scene.
Can return a promise which will be awaited 
during export.

#### Parameters

• **renderer**: [`Renderer`](Renderer.md)

#### Returns

`void`

#### Overrides

[`TextClip`](TextClip.md).[`update`](TextClip.md#update-1)

#### Defined in

[src/clips/text/text.rich.ts:36](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/clips/text/text.rich.ts#L36)

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

[`TextClip`](TextClip.md).[`fromJSON`](TextClip.md#fromjson)

#### Defined in

[src/services/serializer.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/services/serializer.ts#L25)

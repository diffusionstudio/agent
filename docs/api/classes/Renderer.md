[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / Renderer

# Class: Renderer

## Constructors

### new Renderer()

> **new Renderer**(`width`, `height`, `background`, `resolution`): [`Renderer`](Renderer.md)

#### Parameters

• **width**: `number` = `1920`

• **height**: `number` = `1080`

• **background**: \`#$\{string\}\` \| `"transparent"` = `'#000000'`

• **resolution**: `number` = `1`

#### Returns

[`Renderer`](Renderer.md)

#### Defined in

[src/renderer/renderer.ts:56](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L56)

## Properties

### background

> **background**: \`#$\{string\}\` \| `"transparent"` = `'#000000'`

The background color of the canvas

#### Defined in

[src/renderer/renderer.ts:49](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L49)

***

### canvas

> `readonly` **canvas**: `HTMLCanvasElement`

The canvas element

#### Defined in

[src/renderer/renderer.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L24)

***

### ctx

> `readonly` **ctx**: `CanvasRenderingContext2D`

The context of the canvas

#### Defined in

[src/renderer/renderer.ts:29](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L29)

***

### height

> **height**: `number` = `1080`

The height of the canvas

#### Defined in

[src/renderer/renderer.ts:44](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L44)

***

### resolution

> **resolution**: `number` = `1`

The resolution of the canvas

#### Defined in

[src/renderer/renderer.ts:34](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L34)

***

### textScale

> **textScale**: `number` = `4`

The scale of the text

#### Defined in

[src/renderer/renderer.ts:54](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L54)

***

### width

> **width**: `number` = `1920`

The width of the canvas

#### Defined in

[src/renderer/renderer.ts:39](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L39)

## Methods

### blendMode()

> **blendMode**(`mode`?): `this`

#### Parameters

• **mode?**: [`BlendMode`](../type-aliases/BlendMode.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:256](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L256)

***

### circle()

> **circle**(`circle`): `this`

#### Parameters

• **circle**: [`Circle`](../interfaces/Circle.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:136](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L136)

***

### clear()

> **clear**(`region`?): `this`

#### Parameters

• **region?**: [`Rect`](../interfaces/Rect.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:91](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L91)

***

### clip()

> **clip**(`path`?, `fillRule`?): `this`

#### Parameters

• **path?**: `Path2D`

• **fillRule?**: [`FillRule`](../type-aliases/FillRule.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:172](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L172)

***

### copy()

> **copy**(`resolution`): [`Renderer`](Renderer.md)

Copy the renderer

#### Parameters

• **resolution**: `number` = `...`

#### Returns

[`Renderer`](Renderer.md)

#### Defined in

[src/renderer/renderer.ts:87](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L87)

***

### fill()

> **fill**(`options`?, `draw`?): `this`

#### Parameters

• **options?**: [`FillOptions`](../interfaces/FillOptions.md)

• **draw?**: `boolean` = `false`

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:284](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L284)

***

### fillText()

> **fillText**(`text`, `options`): `this`

#### Parameters

• **text**: `string`

• **options**: [`RelativePoint`](../interfaces/RelativePoint.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:210](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L210)

***

### filter()

> **filter**(`filter`?): `this`

#### Parameters

• **filter?**: `string`

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:276](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L276)

***

### image()

> **image**(`image`, `options`): `this`

#### Parameters

• **image**: `CanvasImageSourceWebCodecs`

• **options**: [`ImageOptions`](../interfaces/ImageOptions.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:152](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L152)

***

### measureText()

> **measureText**(`text`, `options`): `TextMetrics`

#### Parameters

• **text**: `string`

• **options**: [`Font`](../interfaces/Font.md)

#### Returns

`TextMetrics`

#### Defined in

[src/renderer/renderer.ts:220](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L220)

***

### mount()

> **mount**(`element`): `void`

Add the renderer to the dom

#### Parameters

• **element**: `HTMLElement`

#### Returns

`void`

#### Defined in

[src/renderer/renderer.ts:346](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L346)

***

### opacity()

> **opacity**(`opacity`): `this`

#### Parameters

• **opacity**: `number`

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:178](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L178)

***

### rect()

> **rect**(`rect`): `this`

#### Parameters

• **rect**: [`RoundRect`](../interfaces/RoundRect.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:112](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L112)

***

### resize()

> **resize**(`width`, `height`): `this`

Resize the canvas

#### Parameters

• **width**: `number`

• **height**: `number`

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:74](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L74)

***

### restore()

> **restore**(): `this`

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:270](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L270)

***

### save()

> **save**(): `this`

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:264](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L264)

***

### shadow()

> **shadow**(`options`?): `this`

#### Parameters

• **options?**: [`Shadow`](../interfaces/Shadow.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:305](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L305)

***

### stroke()

> **stroke**(`options`?, `draw`?): `this`

#### Parameters

• **options?**: [`Stroke`](../interfaces/Stroke.md)

• **draw?**: `boolean` = `false`

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:322](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L322)

***

### strokeText()

> **strokeText**(`text`, `options`): `this`

#### Parameters

• **text**: `string`

• **options**: [`RelativePoint`](../interfaces/RelativePoint.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:200](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L200)

***

### text()

> **text**(`options`): `this`

#### Parameters

• **options**: [`TextOptions`](../interfaces/TextOptions.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:184](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L184)

***

### transform()

> **transform**(`transform`?): `this`

#### Parameters

• **transform?**: [`Transform`](../interfaces/Transform.md)

#### Returns

`this`

#### Defined in

[src/renderer/renderer.ts:231](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L231)

***

### unmount()

> **unmount**(): `void`

Remove the renderer from the dom

#### Returns

`void`

#### Defined in

[src/renderer/renderer.ts:353](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L353)

***

### watermark()

> **watermark**(`render`): `void`

Draw a watermark on the canvas

#### Parameters

• **render**: `boolean` = `false`

#### Returns

`void`

#### Defined in

[src/renderer/renderer.ts:383](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/renderer/renderer.ts#L383)

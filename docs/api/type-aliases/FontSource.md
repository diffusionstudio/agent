[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / FontSource

# Type Alias: FontSource

> **FontSource**: `object`

Defines the properties that are required
to load a new font

## Type declaration

### family

> **family**: `string`

Name of the Family

#### Example

```ts
'Arial'
```

### size?

> `optional` **size**: `number`

The size of the font

#### Example

```ts
16
```

### source

> **source**: `string`

Source of the Variant

#### Example

```ts
url(arial.ttf)
```

### style?

> `optional` **style**: [`FontStyle`](FontStyle.md)

Defines the font style

#### Example

```ts
'italic'
```

### weight?

> `optional` **weight**: [`FontWeight`](FontWeight.md)

The weight of the font

#### Example

```ts
'400'
```

## Defined in

[src/font/types.ts:24](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/font/types.ts#L24)

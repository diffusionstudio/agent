[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / WebfontProperties

# Type Alias: WebfontProperties\<T\>

> **WebfontProperties**\<`T`\>: `object`

Defines the arguments to identify
a default webfont

## Type Parameters

• **T** *extends* keyof *typeof* [`WebFonts`](../variables/WebFonts.md)

## Type declaration

### family

> **family**: `T`

### size?

> `optional` **size**: `number`

### weight

> **weight**: *typeof* [`WebFonts`](../variables/WebFonts.md)\[`T`\]\[`"weights"`\]\[`number`\]

## Defined in

[src/font/types.ts:65](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/font/types.ts#L65)

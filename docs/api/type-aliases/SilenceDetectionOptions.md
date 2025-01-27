[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / SilenceDetectionOptions

# Type Alias: SilenceDetectionOptions

> **SilenceDetectionOptions**: `object`

## Type declaration

### hopSize?

> `optional` **hopSize**: `number`

This parameter affects how accurately the algorithm captures short silences.

#### Default

```ts
1024
```

### minDuration?

> `optional` **minDuration**: `number`

Setting a minimum duration in **milliseconds** for a silence period helps avoid detecting brief gaps between sounds as silences.

#### Default

```ts
500
```

### threshold?

> `optional` **threshold**: `number`

If the RMS is below the threshold, the frame is considered silent.

#### Default

```ts
0.02
```

## Defined in

[src/sources/audio.types.ts:25](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/sources/audio.types.ts#L25)

[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / audioBufferToWav

# Function: audioBufferToWav()

> **audioBufferToWav**(`buffer`, `type`): `Blob`

Converts the specified AudioBuffer to a Blob.

Note that changing the MIME type does not change the actual file format.
The output is a WAVE in any case

## Parameters

• **buffer**: `AudioBuffer`

• **type**: `string` = `'audio/wav'`

## Returns

`Blob`

## Defined in

[src/utils/audio.ts:103](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/utils/audio.ts#L103)

[**@diffusionstudio/core-v2**](../README.md) • **Docs**

***

[@diffusionstudio/core-v2](../globals.md) / showFileDialog

# Function: showFileDialog()

> **showFileDialog**(`accept`, `multiple`): `Promise`\<`File`[]\>

This utility creates a file input element and clicks on it

## Parameters

• **accept**: `string`

comma separated mime types

• **multiple**: `boolean` = `true`

enable multiselection

## Returns

`Promise`\<`File`[]\>

## Example

```ts
audio/mp3, video/mp4
```

## Default

```ts
true
```

## Defined in

[src/utils/browser.ts:48](https://github.com/diffusionstudio/core-v2/blob/ce69ef92917fd6c7f2f6e872cf6c87954dee9b56/src/utils/browser.ts#L48)

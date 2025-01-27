# Opus Encoder

Since the `AudioEncoder` API is currently only supported on Chromium-based browsers, we have implemented a replacement using an Emscripten-compiled version of [libopus](https://github.com/xiph/opus). In this guide, we will use an audio buffer generated with the Web Audio API and multiplex it into an MP4 container using [mp4-muxer](https://github.com/Vanilagy/mp4-muxer).

## Basic Setup

Start by creating a new `Muxer` instance unsing Vanilagy's implementation:

```typescript
import { Muxer, ArrayBufferTarget } from 'mp4-muxer';

const muxer = new Muxer({
  target: new ArrayBufferTarget(),
  audio: {
    codec: 'opus',
    numberOfChannels: 2,
    sampleRate: 48000,
  },
  fastStart: 'in-memory',
});
```

Next, create an Opus encoder instance and use the encoder callback to pass audio chunks directly into the muxer:

```typescript
import { OpusEncoder } from '@diffusionstudio/core';

const encoder = new OpusEncoder({
  output: (chunk, meta) => {
    muxer.addAudioChunkRaw(
      chunk.data,
      chunk.type,
      chunk.timestamp,
      chunk.duration,
      meta,
    );
  },
  error: console.error,
});
```

## Configuring the Encoder

The encoder configuration is asynchronous, as the WASM file is fetched if it isn't cached. Configure the encoder as shown below:

```typescript
await encoder.configure({
  numberOfChannels: 2,
  sampleRate: 48000,
});
```

## Preparing Audio Samples for Encoding

To create an audio buffer, we’ll use the Fetch API and the Web Audio API. Here's an example that fetches and decodes an MP3 file:

```typescript
const response = await fetch('https://diffusion-studio-public.s3.eu-central-1.amazonaws.com/audio/sfx/tada.mp3');
const arrayBuffer = await response.arrayBuffer();
const context = new OfflineAudioContext(2, 1, 48000);

// Decode the audio data into an AudioBuffer
const audioBuffer = await context.decodeAudioData(arrayBuffer);
```

Since the encoder works with interleaved `Int16` samples, we need to convert the `AudioBuffer`. Diffusion Studio provides a utility for this:

```typescript
import { bufferToI16Interleaved } from '@diffusionstudio/core';

const samples = bufferToI16Interleaved(audioBuffer);
```

## Encoding Audio Samples

Now, pass the prepared samples to the encoder for processing:

```typescript
encoder.encode({
  data: samples,
  numberOfFrames: audioBuffer.length,
});
```

The `numberOfFrames` parameter refers to the number of audio samples per channel.

## Finalizing the Muxer and Exporting the MP4

Once encoding is complete, finalize the muxer and extract the MP4 file:

```typescript
muxer.finalize();

// The final MP4 data is available in the muxer’s target buffer
const mp4Blob = new Blob([muxer.target.buffer], { type: 'video/mp4' });
```

You now have an MP4 file that contains your encoded Opus audio.

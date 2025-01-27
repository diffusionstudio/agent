The `Timestamp` object is used to manage the connection between frames and milliseconds internally. You will usually receive a timestamp when calling getters on time-related properties, such as the `delay` and `duration` of a clip.

You can also use the `Timestamp` externally for higher precision if your application requires it, like this:

```typescript
import { Timestamp, ImageClip } from '@diffusionstudio/core';

const timestamp = new Timestamp(1000); // in milliseconds

new ImageClip({ stop: timestamp });

timestamp.frames;  // 30
timestamp.millis;  // 1000
timestamp.seconds; // 1
```

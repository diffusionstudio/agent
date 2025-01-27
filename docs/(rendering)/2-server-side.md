This guide will walk you through setting up an AWS S3 bucket and executing a Node.js script using Puppeteer to interact with Diffusion Studio. Follow the steps below to get your environment up and running.

## Prerequisites

Before proceeding, ensure you have the following:

- **Node.js** installed on your machine.
- An **AWS Account** with permissions to create and configure S3 buckets.

## AWS S3 Bucket Setup

### Create an S3 Bucket

1. Log in to the AWS Management Console.
2. Navigate to the S3 service and create a new bucket.
3. Note down the **bucket name** and **region** for later use.

### Create an IAM User

1. In the AWS Management Console, go to the IAM service.
2. Create a new IAM user with **programmatic access**.
3. Attach the `AmazonS3FullAccess` policy to this user to grant full access to S3.
4. Save the **Access Key ID** and **Secret Access Key** securely.

### Configure CORS for the S3 Bucket

1. Go to the S3 bucket you created.
2. Navigate to the **Permissions** tab.
3. Under the **CORS configuration** section, add the following rules:

    ```json
    [
      {
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["GET", "PUT", "HEAD"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
      }
    ]
    ```

    This configuration enables your application to interact with the S3 bucket without being blocked by CORS.

## Project Setup

### Client-Side Configuration

Create a website that assigns the core Diffusion Studio library to the global context. Below is an example of how to do this:

```typescript title="browser"
import * as core from '@diffusionstudio/core';

Object.assign(window, { core });
```

Ensure this website is accessible via HTTP from the server or machine where the Node.js script will run. You can achieve this by serving it with a tool like Vite.

### Server-Side Configuration

The following instructions cover the Node.js setup, particularly configuring the S3 client.

#### Configure the S3 Client

```typescript
import { S3Client } from '@aws-sdk/client-s3';

const s3 = new S3Client({
  credentials: {
    accessKeyId: '<S3_ACCESS_KEY>',
    secretAccessKey: '<S3_SECRET_KEY>',
  },
  region: '<S3_REGION>',
});
```

Replace `<S3_ACCESS_KEY>`, `<S3_SECRET_KEY>`, and `<S3_REGION>` with your actual AWS credentials and region.

#### Create a Function to Generate Presigned URLs

Presigned URLs allow temporary access to S3 objects. Here’s how to create one:

```typescript
import { PutObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

async function generatePresignedUrl() {
  const id = new Date().toISOString().split('.')[0];
  const bucketName = '<S3_BUCKET>';
  const objectKey = `output/video-${id}.mp4`;
  const expiresIn = 3600; // URL expiration time in seconds (1 hour)

  const command = new PutObjectCommand({
    Bucket: bucketName,
    Key: objectKey,
    ContentType: 'video/mp4',
  });

  return await getSignedUrl(s3, command, { expiresIn });
};
```

Replace `<S3_BUCKET>` with the name of your S3 bucket.

#### Define the Video Processing Pipeline

This function will be executed using Puppeteer and will leverage Diffusion Studio to render a video and upload it to S3.

```typescript
async function main(presignedUrl: string) {
  try {
    const composition = new core.Composition();

    const source = await core.VideoSource.from('https://diffusion-studio-public.s3.eu-central-1.amazonaws.com/videos/big_buck_bunny_1080p_30fps.mp4');

    const video = new core.VideoClip(source).subclip(0, 150);

    const text = new core.TextClip({
      text: 'Bunny - Our Brave Hero',
      position: 'center',
      duration: 90,
      stroke: { color: '#000000' }
    });

    await composition.appendClip(video);
    await composition.appendClip(text);

    await new core.Encoder(composition).render(presignedUrl);

    return 'SUCCESS';
  } catch (e) {
    return String(e);
  }
}
```

#### Execute the Script with Puppeteer

Finally, use Puppeteer to load your website, generate the presigned URL, and run the video processing function:

```typescript
import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Replace with the URL of your website that loads the core library
  await page.goto('http://localhost:5173');

  const presignedUrl = await generatePresignedUrl();

  const res = await page.evaluate(main, presignedUrl);

  console.log(res);

  await browser.close();
})();
```

This script launches a headless browser, navigates to your website, and runs the video processing pipeline, uploading the output to the S3 bucket.

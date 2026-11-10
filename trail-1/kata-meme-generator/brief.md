# DankDeploy — Meme Generator Service

## Project Brief

**From:** Product Owner, DankDeploy
**To:** Engineering
**Priority:** High

---

## Overview

DankDeploy is building a web application that allows users to upload an image and receive it back as a properly formatted meme — with caption text rendered in the right style and position.

We need you to develop the **Meme Generator Service** — a service exposing a single HTTP endpoint that accepts an image and caption text, and returns a finished meme.

## Requirements

### Core Functionality

1. The service must accept an uploaded image and one or two lines of caption text, and return the image with the caption rendered onto it in classic meme style.
2. Text should be **automatically positioned** — top text and bottom text should be placed appropriately regardless of the image dimensions.
3. The text must be **readable** against any background — it should work on light images, dark images, and busy images alike.
4. The service should handle common image formats.

### Privacy

DankDeploy takes user privacy seriously — yes, even for memes.

- Uploaded photos **must never be stored** beyond what is necessary to process the request.
- No uploaded image data should be written to disk, logged, or retained after the response is sent.

### Performance

- The service should respond **quickly** — meme inspiration is fleeting.
- The service should be capable of handling **multiple concurrent requests** without degrading.

### Quality

- The output should look like a **proper meme** — the kind you'd actually send to a group chat, not something that looks auto-generated.
- Text rendering should handle **long captions** gracefully — wrapping, sizing down, or truncating as appropriate.
- The service should handle edge cases **gracefully** (e.g., extremely long text, image too large, unsupported format).

## Evaluation Criteria

Your submission will be evaluated on:

- **Robustness** — Does it handle edge cases and unexpected input well?
- **Latency** — How fast does it respond?
- **Performance under load** — How does it behave with concurrent users?
- **Resource consumption** — Is it efficient with memory and CPU?
- **Code quality** — Documentation, readability, maintainability, and near-production readiness.

## Deliverables

- A working service with a single endpoint for meme generation.
- A README documenting how to build, run, and test the service.
- Any configuration or setup scripts necessary.

## Extra Credit

If time permits: extend the service to accept a **GIF** and return it with caption text applied to every frame, preserving the animation.

---

*If the memes aren't dank, the deploy doesn't ship.*

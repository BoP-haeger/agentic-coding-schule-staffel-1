# CleanCut Studios — Background Remover Service

## Project Brief

**From:** Product Owner, CleanCut Studios
**To:** Engineering
**Priority:** High

---

## Overview

CleanCut Studios is building a web application that allows users to upload a photo and receive the same photo back with the background removed — or replaced with a background of their choosing.

We need you to develop the **Background Remover Service** — a service exposing HTTP endpoints that accept a photo upload and return the modified image.

## Requirements

### Core Functionality

1. The service must accept an uploaded image and return the same image with the background removed, leaving only the foreground subject(s) on a transparent background.
2. The service should also support **background replacement** — the user may optionally provide a replacement background image or a solid colour.
3. The edges around the subject should look **clean and natural** — no harsh outlines or obvious artefacts.
4. The service should handle common image formats.

### Privacy

CleanCut Studios takes user privacy seriously.

- Uploaded photos **must never be stored** beyond what is necessary to process the request.
- No uploaded image data should be written to disk, logged, or retained after the response is sent.

### Performance

- The service should respond **quickly** — users expect a snappy experience.
- The service should be capable of handling **multiple concurrent requests** without degrading.

### Quality

- The output should be **production quality** — suitable for use in professional contexts like LinkedIn headshots or product listings.
- The service should handle edge cases **gracefully** (e.g., no clear foreground subject, image too large, unsupported format).

## Evaluation Criteria

Your submission will be evaluated on:

- **Robustness** — Does it handle edge cases and unexpected input well?
- **Latency** — How fast does it respond?
- **Performance under load** — How does it behave with concurrent users?
- **Resource consumption** — Is it efficient with memory and CPU?
- **Code quality** — Documentation, readability, maintainability, and near-production readiness.

## Deliverables

- A working service with endpoints for background removal and replacement.
- A README documenting how to build, run, and test the service.
- Any configuration or setup scripts necessary.

## Extra Credit

If time permits: extend the service to accept a **live webcam feed** and perform background removal in real time.

---

*Your work will be front and centre — literally. Make it pixel-perfect.*

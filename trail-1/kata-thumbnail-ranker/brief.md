# ClickBait Labs — Thumbnail Ranker Service

## Project Brief

**From:** Product Owner, ClickBait Labs
**To:** Engineering
**Priority:** High

---

## Overview

ClickBait Labs is building a web application that allows content creators to upload a set of candidate thumbnail images and receive them back ranked by predicted click-through appeal — helping creators choose the best thumbnail for their content.

We need you to develop the **Thumbnail Ranker Service** — a service exposing HTTP endpoints that accept a batch of images and return them ranked with scores and reasoning.

## Requirements

### Core Functionality

1. The service must accept a batch of uploaded images (2–10) and return them ranked by predicted visual appeal and click-through potential.
2. Each image should receive a **score** and a brief **explanation** of what makes it strong or weak as a thumbnail.
3. The ranking should consider factors that matter for thumbnails — things like **visual clarity, contrast, composition, text readability** (if text is present), and **emotional impact**.
4. The service should handle common image formats.

### Privacy

ClickBait Labs takes user privacy seriously.

- Uploaded images **must never be stored** beyond what is necessary to process the request.
- No uploaded image data should be written to disk, logged, or retained after the response is sent.

### Performance

- The service should respond **quickly enough to be useful** in a creator's workflow — they shouldn't have to wait around.
- The service should be capable of handling **multiple concurrent requests** without degrading.

### Quality

- The rankings should be **defensible** — a creator should look at the results and broadly agree with the ordering, even if they might quibble with individual placements.
- The explanations should be **specific and actionable**, not generic ("this image is good").
- The service should handle edge cases **gracefully** (e.g., only one image uploaded, images too large, unsupported format, images that are clearly not thumbnails).

## Evaluation Criteria

Your submission will be evaluated on:

- **Robustness** — Does it handle edge cases and unexpected input well?
- **Latency** — How fast does it respond?
- **Performance under load** — How does it behave with concurrent users?
- **Resource consumption** — Is it efficient with memory and CPU?
- **Code quality** — Documentation, readability, maintainability, and near-production readiness.

## Deliverables

- A working service with endpoints for thumbnail ranking.
- A README documenting how to build, run, and test the service.
- Any configuration or setup scripts necessary.

## Extra Credit

If time permits: extend the service to **suggest improvements** — crop recommendations, colour adjustments, or overlay suggestions that would improve a thumbnail's appeal.

---

*First impressions are everything. Help creators make theirs count.*

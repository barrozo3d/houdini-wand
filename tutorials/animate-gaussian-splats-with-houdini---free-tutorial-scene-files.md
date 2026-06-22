---
title: Animate Gaussian Splats with Houdini - Free Tutorial + Scene Files
source: YouTube
url: https://www.youtube.com/watch?v=MqtMQl8DtjQ
author: SOP Cemetery
ingested: 2026-06-22
houdini_version: "unspecified"
tags: [vex, attributes, procedural, rendering, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/animate-gaussian-splats-with-houdini---free-tutorial-scene-files/
frame_count: 0
---

# Animate Gaussian Splats with Houdini - Free Tutorial + Scene Files

**Source:** [YouTube](https://www.youtube.com/watch?v=MqtMQl8DtjQ)
**Author:** SOP Cemetery
**Duration:** 81m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Kind: captions Language: en [music] &gt;&gt; Hi guys. I'm Bogdan. And due to the popular demands, I finally managed to put myself together and recorded a tutorial for you on how to animate a Gaussian splats using Houdini. Because this is a fairly large scene, instead of rebuilding every single node from scratch, I think it makes more sense to walk you through the final setup node by node and explain the reason behind each important choice. I will also give you the project file so you can explore the scene by yourself, modify it, break it, improve it, and hopefully use it to start as a starting point for your own ocean splat animations. But before jumping in, I want to give you a bit of a context about Gaussian splatting. I'm sure that you already know what Gaussian splattings are, but I think it's worth taking a few minutes to give me a chance to have my take to explain the basic idea, especially because understanding what a splat actually is makes the Houdini setup much easier to follow. So let's let's see. Gaussian splatting appeared in 2023 at SIGGRAPH with a paper from five six guys. I don't remember the names and they proposed a new way to represent 3D objects and environments...



---

## Structured Notes

### Core Technique
A node-by-node walkthrough of a complete, pre-built Houdini scene for animating Gaussian splats (the point-cloud-with-ellipsoid-covariance representation introduced at SIGGRAPH 2023), explaining the reasoning behind each major node choice rather than building the setup from scratch.

### Summary
Bogdan (SOP Cemetery) presents a long-form (81-minute) tutorial walking through an existing, fairly large Houdini scene that animates Gaussian splats, rather than rebuilding every node live — the project file is provided so viewers can explore, modify, and use it as a starting point for their own splat animations. He opens with context on what Gaussian splatting actually is (a 3D scene representation introduced in a 2023 SIGGRAPH paper, using oriented ellipsoid "splats" instead of meshes or traditional point clouds), explaining that understanding the splat data representation is key to following the Houdini setup. The video has 9 chapters/sections covering the build, but only the introductory framing was captured in this ingestion pass. (Transcript truncated by ingestion at ~1200 characters — captions fallback was used since Whisper transcription failed on this run, and the per-chapter segmentation that Whisper normally provides was unavailable. The actual node setup, splat attribute handling, and animation technique shown across the remaining ~80 minutes were not captured here. A follow-up pass — fixing the cookies/yt-dlp audio download issue so Whisper can run, or re-ingesting with a working audio path — is needed to capture the full chaptered transcript and extract real node-level detail.)

### Key Steps
1. [Context] Understand Gaussian splatting as a 3D representation: oriented ellipsoid "splats" with position, scale/covariance, color and opacity, introduced at SIGGRAPH 2023
2. [Scene exploration] Open the provided project file rather than building from scratch; walk through the existing node network
3. [Remaining steps] Node-by-node breakdown of splat import, attribute setup, and animation technique — not captured in this ingestion pass; requires re-ingestion with working audio transcription for full detail

### Houdini Nodes / VEX / Settings
- Gaussian splat data representation — points carrying position, scale/orientation (covariance), color and opacity attributes, used in place of traditional mesh or point-cloud rendering
- [Remaining node-level detail not captured — see Summary note on transcript truncation]

### Difficulty
Advanced

### Houdini Version
Unspecified

### Tags
vex, attributes, procedural, rendering, intermediate, advanced

---

## Related Tutorials
[None yet — first Gaussian-splatting-focused entry in this skill's library]

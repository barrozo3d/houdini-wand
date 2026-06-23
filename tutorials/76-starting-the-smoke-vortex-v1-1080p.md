---
title: 76 starting the smoke vortex v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=BFZ3tItjKn8
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/76-starting-the-smoke-vortex-v1-1080p/
frame_count: 4
---

# 76 starting the smoke vortex v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=BFZ3tItjKn8)
**Author:** The VFX School Archive
**Duration:** 7m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, let's test what we just learned on a new setup. I'm going to delete this sphere, which was just for demonstration purposes of the sign function. And I'm going to create a Taurus. And I'm going to dive inside. And I'm going to align it with the Z axis. Okay, let me adjust the size of this to be too big 0.6. And let's reduce this to 0.05. Probably even more 0.025. Yep. Next, I'm going to transform. I'm going to increase the rows here to 16 and give it a bit more resolution here, maybe twice as much. Because we're going to want to let me press Shift W. So you can see the subdivisions. I'm going to apply a transform, which I'm going to be using for scaling this on this direction. Yep. And then I'll subdivide. So we have more geometry and get smudger. Okay, this is going to be the main object that we're going to be used for sourcing. I'm also going to pull it up. One. So it doesn't really touch the ground. And let's animate it to rotate. Okay, we'll go here to the rotation on the Z axis and say time times 90. So now it rotates. Probably go faster. Let's say 120. Okay, similar like that. This is going to be the object that we'll use for sourcing. So we'll first go into another geometry and I'll call this torus source. We'll live inside. We'll get our object merge. Let's grab the torus. Remember you need to bring the transform into this object so that it actually rotates. Next what we're going to do is we're going to add a bit of a mountain to this. Then we can distort. Let's not center the noise. Let's just make it pull out. Just these dimensions 0.2. This is 0.4. And let's make sure that this is also animated. So here I'm going to use time. Okay, so it's rotating and it's changing shape constantly. Maybe increase the reference here 0.6. Now let's calculate the velocity. Let's have some velocity on this. So we'll use a trail swap. Then we'll just say compute velocity and now we should have velocity trails. That take into account the rotation and also the movement from that's coming from the mountain animation. Next, we're going to transform this into a pyro source. And here we want, we don't want to keep the input. We want volume scatter so that we can actually scatter points inside. We will adjust the particle separation the same way as before. So we don't need to worry with this for now, but let's bring it lower so we can actually see what's happening. And here on the pyro source we want to source smoke. So it's going to be creating density and temperature. We also want to have a volume that includes holds the velocity information that's on these points. So for that we will need to create an attribute transfer and we'll transfer to these points we'll transfer the velocity. So now if you look at these points we should have trails on these points as well. So this will be the our velocity section. Everything else is going to come from around here. So back to this pyro source. Let's go create some variation on the density with that attribute noise. We'll affect both the same way. So the attribute noise will be one dimension and we'll affect both the temperature and the density. But for now let's just keep it on the color so that we can have a better look at what's happening. So I'll keep it animated. I'll say we'll center the noise as well. We'll reduce the saturation to 0.5. The element size is 0.25. And let's increase the roughness a bit as well. 0.8. And we'll establish the minimum to be 0. You can also remap it to 1 so that we have 1 and we should have something like this. Okay, some interesting variation there. Now this seems to be working well so we'll just assign this to density and temperature. Now we'll restrise this volume restrise attributes. And we want to restrise density and temperature. We'll use the voxel size here to determine the particle separation here based relative reference. Let me bring this down as well 0.05. This is what we have. So here we have two volumes. Temperature. So here we have two volumes density and temperature.

**Frame:** tutorials\frames\76-starting-the-smoke-vortex-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Houdini Nodes / VEX / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Houdini Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]

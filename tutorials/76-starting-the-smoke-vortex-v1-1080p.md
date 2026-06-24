---
title: 76 starting the smoke vortex v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=BFZ3tItjKn8
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "Not specified"
tags: ["dop", "sop", "pyro", "smoke", "simulation", "intermediate"]
extraction_status: complete
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
Building a rotating, shape-distorted Torus as the emitter geometry for a Pyro smoke vortex — scattering source points across the torus surface and computing per-point velocity from its rotation + animated noise distortion so the resulting smoke inherits realistic swirling motion from the source geometry itself.

### Summary
Continuation lesson (follows a prior sine-function/sphere demo) applying the same animation principles to a new emitter shape. Builds a Torus (aligned to Z, tuned radius/thickness ~0.6/0.025), increases its row/column resolution, applies a Transform (kept separate, for non-uniform scaling) and a Subdivide for smoother geometry, lifts it off the ground, and animates rotation around Z via `time * 120` (or similar) — referencing the original Torus into a "torus source" network via Object Merge (importantly bringing the Transform along so the merged copy still inherits the rotation animation). Adds a Mountain SOP (noise displacement, not centered, asymmetric dimensions like 0.2/0.4) driven by `time` so the shape continuously warps as it spins. Computes per-point **velocity from the geometry's actual motion** using a Trail SOP set to "Compute Velocity" — this captures both the rotation and the mountain-noise shape change as a true velocity field (visible as velocity trails on the points). Converts the result into a **Pyro Source** node (set to NOT keep the input, but instead do Volume Scatter to generate points inside the volume, with tuned Particle Separation) configured to source both density and temperature. Since the Pyro Source's own scattered points don't carry the Trail SOP's velocity, an **Attribute Transfer** node pulls the velocity attribute from the torus-source points onto the newly scattered pyro-source points, restoring the rotational/shape-change motion on the actual smoke-driving points. Adds an **Attribute Noise** node (animated, centered, reduced saturation ~0.5, element size ~0.25, increased roughness ~0.8, remapped to a 0–1 range) to add density/temperature variation, applied identically to both fields (previewed on a Color attribute first for visual feedback before assigning to Density/Temperature). Finishes by converting these point attributes into actual sim volumes with **Volume Rasterize Attributes**, rasterizing both Density and Temperature using a Voxel Size tied to the same particle-separation-style reference value (~0.05) — producing the two source volumes (density + temperature) that will drive the Pyro simulation in a later lesson.

### Key Steps
1. Torus: align to Z axis, tune Radius (~0.6) and minor radius (~0.025), increase Rows (e.g. 16) and Columns resolution; Shift+W to preview subdivisions.
2. Transform SOP (kept separate, for axis-specific scaling) → Subdivide for smoother geometry.
3. Lift the torus off the ground (translate Z ~1) and animate Rotation Z with an expression like `time * 120` for continuous spin.
4. New geometry network "torus source": Object Merge the torus — critically, merge it in a way that includes its Transform node so the rotation animation is preserved in the new context.
5. Mountain SOP: enable noise displacement, uncheck Center, set asymmetric dimensions (e.g. 0.2 / 0.4), animate via `time` in the noise offset so the shape warps continuously; tune Element Size/Frequency (~0.6).
6. Trail SOP → Compute Velocity, to derive a true per-point velocity attribute from the combined rotation + shape-change motion (verify via visible velocity trails).
7. Pyro Source node: disable "Keep Input," enable Volume Scatter (points generated inside the volume, tune Particle Separation lower to preview density), set to source Smoke (Density + Temperature).
8. Attribute Transfer: pull the `v` (velocity) attribute from the torus-source points onto the Pyro Source's newly scattered points, since Volume Scatter's own points start without velocity.
9. Attribute Noise: animated, Center on, Saturation ~0.5, Element Size ~0.25, Roughness ~0.8, Minimum 0 remapped toward 1 — preview on Color first, then apply identically to Density and Temperature for organic variation.
10. Volume Rasterize Attributes: rasterize Density and Temperature point attributes into actual volume grids, Voxel Size tied to the same reference scale (~0.05) used for Particle Separation — produces the final density + temperature source volumes.

### Houdini Nodes / VEX / Settings
Torus, Transform, Subdivide, Object Merge (bringing in upstream Transform for animation), Mountain (noise displacement, animated via `time`), Trail (Compute Velocity), Pyro Source (Volume Scatter, Particle Separation, Source Smoke: Density + Temperature), Attribute Transfer (velocity), Attribute Noise (animated, Saturation, Element Size, Roughness, remap range), Volume Rasterize Attributes (Voxel Size). Expression: `time * <speed>` for rotation/noise animation.

### Difficulty
Intermediate to Advanced — assumes familiarity with basic Pyro source-building concepts; this lesson specifically focuses on deriving believable emitter velocity from animated source geometry rather than faking it.

### Houdini Version
Not specified.

### Tags
"dop", "sop", "pyro", "smoke", "simulation", "intermediate"

---

## Related Tutorials
- `78-building-the-vortex-dop-network-v1-1080p.md` — direct continuation, takes these source volumes into the actual Pyro DOP simulation

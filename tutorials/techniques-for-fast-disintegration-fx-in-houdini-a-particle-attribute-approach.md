---
title: Techniques for Fast Disintegration FX in Houdini – A Particle & Attribute Approach
source: YouTube
url: https://www.youtube.com/watch?v=Syn7XjeCH_8
author: the point and prim
ingested: 2026-07-16
houdini_version: "Not specified"
tags: [disintegration, particle-simulation, distance-along-geometry, smooth-function, materialx, karma-xpu, quaternion-blend, the-point-and-prim]
extraction_status: complete
frames_dir: tutorials/frames/techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Techniques for Fast Disintegration FX in Houdini – A Particle & Attribute Approach

**Source:** [YouTube](https://www.youtube.com/watch?v=Syn7XjeCH_8)
**Author:** the point and prim
**Duration:** 5m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome. In this breakdown video I'll be walking you through the workflow
[0:08] I used to create this disintegration effect in Houdini. We'll be covering attribute manipulation
[0:13] and particle simulation techniques and how pairing these together can produce an interesting
[0:17] result without long simulation times. I'll also briefly be covering the shading and rendering
[0:23] setup in material X and Karma XPU. This is a breakdown video and not really tutorial,
[0:29] but if you're curious to learn more I'm giving the hip file away for free on my Gum
[0:33] Road. You'll find the link in the description below.
[0:36] Starting with the mask we can use the distance along geometry node and manually select a few
[0:41] points to art direct where the effect spreads from. This node creates a dist attribute
[0:45] which we will then remap to drive the animation. Utilizing the smooth function and animator
[0:50] parameter and the classic rest noise rest technique. We can maintain full control over the
[0:56] timing with simple keyframes. For fracturing we only need one side of polygons. I use a
[1:03] scatter and the near point function to create a class attribute which can then be used
[1:07] for a cheap fracture using the split points node. Next I pack the geometry based off a unique
[1:13] per piece attribute. I convert the class to name but this works with any attribute as
[1:18] long as it's unique per piece. We need to simulate points so let's extract the piece
[1:22] centroids with an ad node. When packing I transfer the dist attribute from earlier. This
[1:26] means the mask point fault can be reused to retrieve the spreading animation. Lastly I'll
[1:32] set the stop attribute. We will want to gradually animate it from 1 to 0 inside the popnet
[1:37] using the mask. This will activate the points over the course of the sim. Inside dops I use
[1:46] a pop wrangle with a simple if statement. This simply reads the mask and the animator position
[1:52] of the source points pre simulation. If the mask has values of anything but 0 the stop
[1:58] attribute is switched from 1 to 0 meaning it becomes active in the simulation. If this
[2:04] condition is not met the points will simply update the positions to match the incoming
[2:07] animation. This is the other important line here. It creates an attribute that will increment
[2:13] on each frame a particle has become and remained active which is useful for manipulation
[2:18] per sim. The rest of this is standard particle simulation nodes. Pop drag pop wind and a pop
[2:24] advec by volumes. I'll come back to this later after we cover the smokes him. Once the
[2:32] particles are cached I copy the packed prims back on the points using the attribute created
[2:37] before. For particle rotations I use the active time attribute from the pop sim to blend
[2:43] from a rest paternion with the spinning one. Without going into a lot of detail this is
[2:49] the rest orient. All of this is the spinning orient and this blends between the two of them
[2:54] using active time as a bias. Moving onto the second layer of the sim, the inner core.
[3:04] I created the points using a simple points from volume, point to form it and applied the
[3:09] same mask. I split the points into two streams using the mask attribute. One will be for
[3:16] sourcing, the other for collision data. I want a source just the leading edge of the
[3:24] mask instead of everything at once. To do this I compare the points on the previous frame
[3:28] and the current one and then extract the difference. These points are then russerized for the
[3:37] smoke sim. The sim itself is very basic. Using only the soft level pirus solver with some
[3:43] wind and turbulence. I keep it very low res as we only need its valve field for evaction
[3:48] and never to render it. The smoke sim is then piped into both pop nets where we utilize
[3:53] the pop evac by volumes node to transfer the movement of our smoke sim onto the particles.
[4:01] A neat trick is to blend off the particle evaction by age. Serve the valve field from the smoke
[4:05] simulation dissipates, the pop wind will take over and you won't have unwanted particles
[4:09] left floating around with no movement. Finally I create some flake geometry with variations
[4:14] and instance one of the points to finish up this layer. I use simple sop imports to bring
[4:24] my geo into Solaris and rebuild the instances for the ash using an internal point cloud
[4:28] from Solaris. You can of course also just import the pack primitives directly if you want
[4:33] to. Moving onto shaders, the hand shader is just a bunch of noises layered together which
[4:38] are also piped into displacement. The only key thing here is that I'm using the rest
[4:42] attribute so the noises don't swim through world space. The inner particle shader is what
[4:48] is doing most of the heavy lifting for this effect. By remapping the age attribute we
[4:52] can drive the strength of a mission as well as blend between colors as the particles age.
[4:56] On here I've just got a simple key and fill light setup. I'm using an LP E-Tag node
[5:01] and enabling this checkbox so that I can split my beauty pass by its light groups and comp
[5:05] which provides a bit more control over the final look. My camera has almost no movement
[5:09] in the shot so I did use some dirty tricks like making some additional atmosparsers by
[5:13] animating and motion blurring some noise in 2D.
[5:16] And that's it for this video, thank you so much for watching. If you'd like to explore
[5:20] the techniques further and encourage you to check out the free hit file available on Gumroad.
[5:25] Bye for now and see you in the next one.



---

## Captured Frames

- [0:36] tutorials/frames/techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach/frame_000.jpg
- [1:07] tutorials/frames/techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach/frame_001.jpg
- [1:46] tutorials/frames/techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach/frame_002.jpg
- [2:43] tutorials/frames/techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach/frame_003.jpg
- [3:16] tutorials/frames/techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach/frame_004.jpg
- [3:53] tutorials/frames/techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach/frame_005.jpg
- [4:34] tutorials/frames/techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach/frame_006.jpg

---

## Structured Notes

### Core Technique
A fast disintegration effect built entirely from **attribute manipulation driving particle activation** (rather than long-running full simulations): a Distance-Along-Geometry-driven smooth-function mask controls a per-point "stop" attribute inside the POP solver to stagger when packed fracture pieces go active, combined with a leading-edge-only smoke advection field and a quaternion blend for particle spin-up.

### Summary
Framed as a breakdown rather than a formal tutorial, this video shows how combining simple attribute tricks with particle simulation avoids the long sim times of more literal destruction approaches. The mask driving the whole effect reuses the channel's own toolkit: **Distance Along Geometry** from a handful of manually-selected art-directed points produces a `dist` attribute, which is remapped through the **smooth function** with an animated parameter and the classic **rest-noise-rest** technique for edge breakup — giving full keyframe-level timing control over where and when the effect spreads. For fracturing, only one side of the surface is needed, so a cheap approach suffices: **Scatter** points, use **Near Point** to build a per-point `class` attribute (nearest-neighbor grouping), then feed that into **Split Points** for an inexpensive fracture. Pieces are packed using a per-piece-unique attribute (author converts `class` to `name`, though any unique-per-piece attribute works), and piece centroids are extracted with an **Add** SOP to serve as the actual simulated points — critically, the earlier `dist` mask attribute is transferred onto these centroid points during packing so the same spreading-mask data can be reused inside the POP sim without recomputing it. A `stop` attribute is initialized to 1 (inactive) and driven from 1→0 progressively via the mask inside the **POP Network**, using a **POP Wrangle** with a simple conditional: it reads the mask and the point's pre-sim animated position; if the mask is anything other than 0, `stop` flips to 0 (the point becomes an active/live particle); otherwise the point just continues to track its incoming pre-sim animated position untouched. The same wrangle also increments an `active_time`-style attribute every frame a particle has been active, which is later reused for per-particle spin-up. From there it's largely standard particle nodes — **POP Drag**, **POP Wind**, and **POP Advect by Volumes** (revisited after the smoke sim is built). Once particles are cached, the packed fracture pieces are copied back onto the points using the piece-unique attribute created earlier. Piece rotation reuses the channel's **quaternion** approach from its dedicated rotation video: the `active_time` attribute is used as a blend bias between a static "rest" orient quaternion and a continuously-spinning orient quaternion, so pieces smoothly ramp from stationary to spinning as they've been active longer, rather than snapping instantly to full rotation speed. A second, inner-core layer adds volumetric detail: points are generated from a volume (Points from Volume), Point-formed, and masked with the same `dist` mask, then split into two streams — one for smoke sourcing, one for collision — where the sourcing stream isolates only the **leading edge** of the mask by diffing the mask's value between the previous frame and current frame (rather than sourcing the whole masked region every frame), and those edge points are rasterized to drive a deliberately low-resolution, unrendered **Pyro solver** (wind + turbulence only) used purely to supply a velocity field. That smoke sim feeds **POP Advect by Volumes** in both POP networks so the particles' motion is pulled from the smoke's velocity field, with a neat blend-by-age trick: as the smoke's advection influence dissipates with age, POP Wind gradually takes over so particles don't end up motionless once the volume field fades. A final flake-geometry layer (with per-instance variation) is instanced onto some of the points to add fine debris detail. The scene is brought into Solaris via simple SOP Imports, with the ash instances rebuilt using an internal Solaris point cloud (packed primitives could also be imported directly). Shading uses **MaterialX** on **Karma XPU**: the main hero-object shader layers several noises (also piped into displacement) using the `rest` attribute so the noise doesn't swim through world space as the object deforms/breaks; the inner-particle shader does most of the visual heavy lifting by remapping the particle `age` attribute to drive emission strength and color blending as particles age. Lighting is a simple key+fill setup using an **LPE Tag** node with light-group splitting enabled for compositing control, plus some 2D atmosphere/dirt tricks (animated, motion-blurred noise layers) added in comp to compensate for the shot's near-static camera.

### Key Steps
1. Build the spreading mask: **Distance Along Geometry** from manually-selected art-direction points → `dist` attribute → remap through the **smooth function** (animated parameter) with **rest-noise-rest** edge breakup for organic timing control.
2. Cheap one-sided fracture: **Scatter** points, use **Near Point** to build a nearest-neighbor `class` attribute, feed into **Split Points**.
3. Pack pieces using a unique-per-piece attribute (`class` → `name` or equivalent); extract piece centroids with an **Add** SOP as the actual simulated points, transferring the `dist` mask attribute onto them during packing.
4. Initialize a `stop` attribute at 1 (inactive); inside the **POP Network**, use a **POP Wrangle** to read the mask + pre-sim animated position each frame — flip `stop` to 0 (go active) if the mask is nonzero, otherwise keep tracking the incoming animated position; also increment an `active_time` attribute every active frame.
5. Run standard particle motion: **POP Drag**, **POP Wind**, **POP Advect by Volumes** (revisited once the smoke sim exists).
6. Copy the packed fracture pieces back onto the cached particle points using the piece-unique attribute; drive piece rotation with a **quaternion blend** between a static "rest" orient and a continuously-spinning orient, biased by the `active_time` attribute for a gradual spin-up.
7. Build the inner-core smoke layer: **Points from Volume** → Point-form → mask with `dist` → split into sourcing vs. collision streams; isolate the mask's **leading edge only** by diffing mask values between the previous and current frame for the sourcing stream.
8. Rasterize the leading-edge points and run a low-res, unrendered **Pyro solver** (wind + turbulence) purely to generate a velocity field for advection.
9. Feed the smoke sim into **POP Advect by Volumes** in both particle networks; blend advection influence off by particle age so **POP Wind** takes over as the volume field dissipates, avoiding motionless leftover particles.
10. Add a flake-geometry instancing layer (per-instance variation) on a subset of points for fine debris; bring everything into Solaris via **SOP Import**, rebuilding ash instances from an internal Solaris point cloud.
11. Shade in **MaterialX**/**Karma XPU**: layer noises (also driving displacement) using the `rest` attribute on the hero shader to avoid world-space noise swimming; drive the particle shader's emission strength/color blend by remapping the `age` attribute.
12. Light with a simple key+fill setup, using **LPE Tag** with light-group splitting for comp control; add 2D atmosphere/dirt via animated, motion-blurred noise layers in comp to compensate for a near-static camera.

### Houdini Nodes / VEX / Settings
Distance Along Geometry, smooth function (rest-noise-rest mask), Scatter, Near Point (`class` attribute), Split Points (cheap fracture), Pack (unique-per-piece `name` attribute), Add SOP (centroid extraction), `stop` attribute + POP Wrangle (conditional mask-driven activation), `active_time` attribute (per-frame increment while active), POP Drag, POP Wind, POP Advect by Volumes, quaternion blend (rest-orient vs. spinning-orient biased by `active_time`), Points from Volume, Point (point-forming), Pyro Solver (low-res, wind + turbulence, unrendered, advection-only), leading-edge mask diff (previous-frame vs. current-frame comparison), instancing (flake geometry with variation), SOP Import (Solaris), MaterialX shading (Karma XPU), `rest` attribute (shader noise stabilization), `age` attribute remap (particle shader emission/color), LPE Tag (light-group splitting).

### Difficulty
Advanced (chains multiple attribute-driven masking and particle-activation tricks from earlier videos in the series into a single multi-layer effect, plus a full MaterialX/Karma XPU shading and lighting pipeline).

### Houdini Version
Not specified.

### Tags
#disintegration #particle-simulation #distance-along-geometry #smooth-function #materialx #karma-xpu #quaternion-blend #pop-network #the-point-and-prim

---

## Related Tutorials
- [Houdini: How to mask with the smooth function](houdini-how-to-mask-with-the-smooth-function.md) — same channel/author; this disintegration effect is built directly on the smooth-function + rest-noise-rest masking technique introduced there.
- [Procedurally mask deforming / animated geometry - Houdini](procedurally-mask-deforming-animated-geometry---houdini.md) — same channel/author; shares the Distance Along Geometry mask-generation approach used here for the disintegration spread.
- [Particle rotations in Houdini (how to rotate orient)](particle-rotations-in-houdini-how-to-rotate-orient.md) — same channel/author; this video's rest-to-spinning quaternion blend for piece rotation directly reuses the angle/axis quaternion technique taught there.

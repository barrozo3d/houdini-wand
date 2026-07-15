---
title: Procedural Tips: Flow Maps, RBD Emit and more
source: YouTube
url: https://www.youtube.com/watch?v=XFOiCiljWh8
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.550"
tags: [flow-maps, cops, rbd, materialx, karma, vex, solaris, product-viz, liquid, umbrella]
extraction_status: complete
frames_dir: tutorials/frames/procedural-tips-flow-maps-rbd-emit-and-more/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Tips: Flow Maps, RBD Emit and more

**Source:** [YouTube](https://www.youtube.com/watch?v=XFOiCiljWh8)
**Author:** cgside
**Duration:** 4m12s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, in this video I'll share 5 different tips that might help you in your future projects.
[0:06] This full scene is available on Patreon by the way.


### Flow Maps [0:10]
**Transcript (timestamped):**
[0:10] So I have this glass profile that I will revolve, and in order to have an inside selection
[0:16] to create the liquids, I can at least point save that range of points, making sure I resemble
[0:22] to get the points properly sorted, and with a range save out an inside group.
[0:27] And after having the glass geometry, I can still access that group and promote it to primitives,
[0:33] so I'm able to extract the liquid geometry.
[0:38] Now let's have a look at FlowMaps to create the liquid effects.
[0:42] You should be aware that this FlowMap visualized node as a bug if you try to use the viewport shader,
[0:49] but in our case we will use the vertex color.
[0:52] Also setting the FlowMap mode from color, previously created, and for the diffuse texture,
[0:59] I'm loading custom generator from cops. It's a VOP cop generator that uses a noise with another
[1:06] one distorting the position, which comes from the x and y position of the generator.
[1:13] Feeding the noise to a ramp and from the outside adding some blue colors.
[1:19] Then we can copy the nodepad with control C and paste it in the diffuse texture,
[1:24] along with the OP syntax, to import from cops.
[1:29] And as we are using the FlowMap mode as color, there's this point of option
[1:34] rating a noise to control the pattern.
[1:38] Finally, we can keep it animated, or just place a time shift with the desired frame to render.
[1:44] Okay, let's see how to easily create the umbrella effect.


### Umbrella Effect [1:45]
**Transcript (timestamped):**
[1:49] I am starting with the UVs, in this case we want them in a circular pattern to place the stripes.
[1:56] So for that we can use the polar projection,
[1:59] promoting the UVs to point the treewood since we want to use them in a pointvop.
[2:06] And in there it's really simple, just using a Stripes node, and again a turbulent noise to
[2:13] distort the UVs. You can play with the amount of stripes and widths.
[2:19] And in another pointvop I'm just displacing the points with the color from the previous one.
[2:26] Continuing on the umbrella, I'm saving out a position attribute to use in salaries,
[2:31] so I can orient the textures properly. As you can see I'm rotating and transforming the umbrella,
[2:37] and that way I can't have precise control over the rotation of the texture.
[2:42] As you can see I'm using the Carmetrip Lanner to texture the toothpick.
[2:46] And if I remove these nodes I get the wrong orientation.
[2:50] That's why I'm using the previously saved position, plus I rotate 3D, set to rotate 90 degrees
[2:57] along the Z axis. In this case since we are doing a transformation inside salaries,
[3:03] you might already assume it's rotated. And you can replace the custom position attribute just by
[3:11] the material exposition node. Okay, as the final tip let me show you how I created the ice cubes.


### Ice Cubes [3:13]
**Transcript (timestamped):**
[3:17] I extracted the top patch from the liquid and extruded it to create the collision geometry.
[3:24] Created a simple distorted cube and I will emit them using the RBD solver.
[3:30] I am also using the RBD configure to create packed frames and set the collision geometry to a box.
[3:38] Set some initial random rule and in this wrangle for every fifth frame and before frame 72 emit geometry.
[3:50] And finally you can cache out a resting frame. So that's basically the bunch of random tips
[3:57] but that I thought might be useful and worth sharing. The file will be available on Patreon if you
[4:03] want to have a look too. Thank you and see you soon.



---

## Captured Frames

- [0:15] tutorials/frames/procedural-tips-flow-maps-rbd-emit-and-more/frame_000.jpg
- [0:55] tutorials/frames/procedural-tips-flow-maps-rbd-emit-and-more/frame_001.jpg
- [1:30] tutorials/frames/procedural-tips-flow-maps-rbd-emit-and-more/frame_002.jpg
- [2:10] tutorials/frames/procedural-tips-flow-maps-rbd-emit-and-more/frame_003.jpg
- [2:50] tutorials/frames/procedural-tips-flow-maps-rbd-emit-and-more/frame_004.jpg
- [3:30] tutorials/frames/procedural-tips-flow-maps-rbd-emit-and-more/frame_005.jpg
- [4:05] tutorials/frames/procedural-tips-flow-maps-rbd-emit-and-more/frame_006.jpg

---

## Structured Notes

### Core Technique
Five product-viz tips for a cocktail-glass shot: extracting an "inside" liquid selection from a revolved profile, driving MaterialX Flow Map with a COPs-generated vertex-color noise pattern for swirling liquid, using polar-projected UVs + a Point VOP Stripes node for a circular umbrella pattern, saving a pre-transform position attribute to fix Triplanar orientation after Solaris transforms, and using RBD as a simple staggered ice-cube emitter.

### Summary
A glass profile is revolved, with an inside-liquid point range saved and promoted to primitives so the liquid geometry can be extracted from the same revolved mesh. MaterialX's Flow Map (set to vertex-color mode, since the viewport-shader FlowMap-visualize node has a known bug) drives liquid swirl using a custom VOP COPs generator: two noises, one distorting the position of the other using the generator's own x/y position inputs, fed through a Ramp with blue-tinted output at the edges — imported into the diffuse texture via `op:` syntax. FlowMap's "point" option adds a controllable pattern noise; a Time Shift can freeze the animated flow at a chosen render frame. For the umbrella, polar-projected UVs (promoted to point since a Point VOP is used) feed a Stripes node distorted by turbulence noise (width/count adjustable), then displace points along color from a second Point VOP. A saved pre-Solaris-transform position attribute plus a 90°-Z Rotate3D fixes Triplanar texture orientation that would otherwise break once the umbrella is rotated/transformed inside Solaris (replaceable by the Material's exposition node for the position input). Ice cubes: extract the liquid's top patch, extrude for collision geometry, distort a simple cube, and emit via RBD Solver with RBD Configure (packed frames, box collision), random initial rotation, and a wrangle that emits geometry every 5th frame before frame 72 — then cache a resting frame for a static hero shot.

### Key Steps
1. **Liquid selection**: on a revolved glass profile, save a resampled/sorted point range as an "inside" group, then promote it to primitives after generating the glass geometry so the liquid mesh can be extracted from that same group.
2. **Flow Map liquid swirl**: note the FlowMap-visualize node's viewport-shader bug — use **vertex color** mode instead; set FlowMap mode to color; build a custom **VOP COPs generator** with a noise distorted by a second noise fed from the generator's own x/y position inputs, output through a Ramp with blue accents at the edges.
3. Import the COPs generator into the diffuse texture slot via **copy/paste + `op:` syntax** referencing the COPs network path.
4. Use FlowMap's **point** option to add a secondary pattern noise on top of the flow; use a **Time Shift** to freeze the animation at the desired render frame instead of leaving it animated.
5. **Umbrella pattern**: polar-project UVs onto the umbrella, promote to point (needed for the following Point VOP), then use a **Stripes** node distorted by a turbulence noise (adjustable stripe count/width) inside the VOP.
6. In a second Point VOP, **displace points** using the color output from the first Stripes VOP for physical ribbing detail.
7. **Fixing Triplanar orientation after Solaris transforms**: save out a pre-transform position attribute in SOPs before the umbrella is rotated/transformed in Solaris; feed that saved position, offset by a **Rotate3D set to 90° on Z**, into the Triplanar node so texture orientation stays correct regardless of the object's in-context transform — can alternatively be replaced by wiring the Material's `exposition` node directly into the position input.
8. **Ice cubes**: extract the top patch from the liquid geometry, extrude it to create simple collision geometry; build a slightly distorted cube as the ice-cube source shape.
9. Emit the cubes via **RBD Solver**, using **RBD Configure** to enable packed frames and set the collision geometry to a box; set an initial random rotation.
10. In a wrangle, emit new geometry **every 5th frame, and only before frame 72**, creating a naturally staggered ice fill rather than dumping all cubes at once.
11. Cache out a single resting frame once the simulation settles, for use as the final static hero-shot render.

### Houdini Nodes / VEX / Settings
Revolve, Resample, Sort, Group Range (inside-liquid group), Attribute Promote, MaterialX Flow Map (vertex-color mode, point noise option), custom VOP COPs generator (noise distorting noise via x/y position inputs, Ramp with edge color), `op:` texture-path syntax, Time Shift, Polar Project (UVs), Point VOP (Stripes node, Turbulent Noise distortion, color-driven point displacement), saved pre-transform position attribute + Rotate3D (90° Z) for Triplanar orientation fix, Material `exposition` node (alternative position source), RBD Solver, RBD Configure (packed frames, box collision), Attribute Wrangle (frame-modulo emission logic, `frame % 5` before frame 72), cache/resting-frame export.

### Difficulty
Advanced (combines MaterialX Flow Map internals, custom COPs VOP generators, Solaris-transform-aware Triplanar fixes, and RBD emission scripting).

### Houdini Version
20.5.550 (visible in viewport title bar).

### Tags
flow-maps, cops, rbd, materialx, karma, vex, solaris, product-viz, liquid, umbrella

---

## Related Tutorials
- [Procedural Fries with MtlX and Karma XPU](procedural-fries-with-mtlx-and-karma-xpu.md) — related MaterialX/Karma product-viz shading techniques from the same channel.
- [Procedural Pizza in COPs](procedural-pizza-in-cops.md) — shares the COPs-generator-for-texturing approach used here for the liquid diffuse map.

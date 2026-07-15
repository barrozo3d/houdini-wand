---
title: Vellum Balloon Text in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=T-_L6BeLSkg
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.331"
tags: [vellum, vdb, typography, karma, materialx, simulation, balloon, text-effects]
extraction_status: complete
frames_dir: tutorials/frames/vellum-balloon-text-in-houdini/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Vellum Balloon Text in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=T-_L6BeLSkg)
**Author:** cgside
**Duration:** 9m43s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm going to show you step by step how you can create this
[0:07] balloon text effect using Odini and Valon. So let's get into it. So with a fresh Odini scene let's start by dropping the geometry container and


### Tutorial [0:14]
**Transcript (timestamped):**
[0:21] font
[0:24] and
[0:26] I'm gonna write cgs for cg sites
[0:30] and
[0:31] I'm gonna pick a different font
[0:35] that has some rounded corners. So let me pick the font.
[0:43] So this is the font I'm going to use. It is a bit more rounded and it will work better for the effect.
[0:53] So let's extrude it.
[1:00] And we will extrude about 0.2
[1:06] and I'll put the back.
[1:09] Then I'm gonna create a VDB from polygons so we can round it
[1:16] because right now it's just too sharp. We can bevel it but
[1:22] it will work better with a VDB conversion. VDB from polygons.
[1:30] And let's say 0.01
[1:36] and now we will smooth it out.
[1:41] So let's first convert VDB to polygons so we can check the final result.
[1:50] So as you can see it's not looking great.
[1:54] Let's
[1:56] smooth as the F.
[2:01] And now it's looking better. Let's say we want 10
[2:07] and after the smooth I also want to erode it. So let's put on a Rishabes.
[2:18] And let's erode it by
[2:25] something like this should be fine. So we're going from this to this.
[2:34] And now this geometry is not the best for simulation. Let me just save this quickly.
[2:43] So as I was saying this geometry is not ideal.
[2:46] So we will remesh
[2:53] and let me check the amount of remesh I used. So 0.0075
[3:06] this should give us enough resolution.
[3:11] And now we can start our valum simulation.
[3:16] So let's just organize this and put down a valum configuration balloon.
[3:24] This will create the valum plot and the pressure constraint.
[3:31] And let's create a valum solver.
[3:39] And if you hold down j you can drag and connect everything.
[3:47] Now just wait a bit.
[3:52] And let's check the result.
[3:57] And this will fall down. We will need to remove the gravity.
[4:04] So let's remove the gravity.
[4:07] And we will need to set up some things in here.
[4:17] So to start with let's go to our valum plot.
[4:22] And
[4:27] what we need to do
[4:29] is to play with the wrestling scale of the stretch.
[4:38] So in this case I use 0.1.
[4:42] 1.18
[4:46] and let's see what that gives us.
[4:51] Nothing too much.
[4:53] And we will also increase the stretch to 10,000.
[5:08] And while we're here let's decrease the band stiffness to 0.01.
[5:18] Let's see what that gives us.
[5:23] That is giving us these results which is a bit too much.
[5:30] And not very controlled.
[5:32] So what we can do is to play with the valum pressure.
[5:38] So let's go to the valum pressure.
[5:40] And we can say the wrestling scale let's try 50.
[5:49] And we will just use one frame.
[5:52] So we could actually use just this frame, the previous one.
[5:59] So as you can see we already have the effect.
[6:03] This one is a bit too much in my opinion so we can use this one.
[6:10] So you can see it's creating some nice wrinkles in here and here.
[6:16] So I think I'm gonna use this one.
[6:22] Now let's create a valumio.
[6:25] So just to bake the result and we will remove time dependent cats,
[6:33] cache and just save to this.
[6:37] Now we can just have it the frame freeze.
[6:44] So let's create a no just for demonstration purpose.
[6:50] I'm gonna render this out.
[6:55] So we can go to some areas.


### Render [6:58]
**Transcript (timestamped):**
[7:00] And it's top import.
[7:04] And let's import geometry.
[7:08] Let's set it like this.
[7:15] And let's create a material library.
[7:23] And inside let's do a calendar material builder.
[7:29] Let's sort of view and assign to everything.
[7:33] Now we can create a dome light.
[7:35] And let's say it's a let alone.
[7:37] I'm gonna use Christmas photo studio from HDI Heaven or Polyaven.
[7:43] I mean, and let's create the camera settings.
[7:49] Let's change it to exp you.
[7:51] Give it some quality.
[7:53] And let's create a camera settings.
[7:55] Let's change it to exp you.
[7:57] Give it some quality.
[7:59] Let's change it to exp you.
[8:01] Let's create some quality.
[8:08] And the camera freeze the diffuse limits.
[8:12] Reflections and refractions is fine.
[8:18] Let's test these out.
[8:20] Camera exp you.
[8:25] And let's get rid of the background.
[8:28] So display environment lights as backgrounds turned off.
[8:34] Let's change it to dark.
[8:37] Let's go to render and save viewport size.
[8:44] That way if we have a camera we won't render the full resolution,
[8:48] but just the portion of the viewport.
[8:52] So but in this case I'm not even going to bother creating a camera.
[8:58] I'm just gonna do a simple material.
[9:02] So let's change this to some RNG.
[9:10] And increase the metowness.
[9:15] And increase the bit the roughness.
[9:19] So yeah guys it's basically it's nothing to complex.
[9:24] As you can see it's just really easy to set up.
[9:29] And I hope you have learned something new.
[9:32] Let me know in the comments.
[9:35] And I'll see you soon.
[9:37] Thank you.



---

## Captured Frames

- [0:30] tutorials/frames/vellum-balloon-text-in-houdini/frame_000.jpg
- [1:30] tutorials/frames/vellum-balloon-text-in-houdini/frame_001.jpg
- [2:50] tutorials/frames/vellum-balloon-text-in-houdini/frame_002.jpg
- [5:00] tutorials/frames/vellum-balloon-text-in-houdini/frame_003.jpg
- [5:50] tutorials/frames/vellum-balloon-text-in-houdini/frame_004.jpg
- [6:20] tutorials/frames/vellum-balloon-text-in-houdini/frame_005.jpg
- [9:10] tutorials/frames/vellum-balloon-text-in-houdini/frame_006.jpg

---

## Structured Notes

### Core Technique
Create an inflated "balloon text" effect by VDB-rounding a font's extruded letters (since Bevel alone looks too sharp), remeshing for simulation-friendly topology, then running a **Vellum Configure Balloon** setup and deliberately dialing in unstable/high parameters (very high stretch stiffness, very low bend stiffness, cranked pressure rest scale) to produce the characteristic wrinkled-fabric look, freezing on whichever single frame looks best rather than letting the sim settle.

### Summary
Text is created via a Font node, extruded (~0.2, with back cap), then converted to VDB and rounded out via **VDB Smooth**, since a straight Bevel wasn't smooth enough. After converting back to polygons to check the result, the smooth amount and an added **Erode** pass refine the rounded shape further. Since this VDB-remeshed geometry isn't well-suited for simulation directly, a separate **Remesh** pass (small remesh size, e.g. 0.0075) gives clean, simulation-appropriate topology. The core Vellum setup uses **Vellum Configure Balloon** (auto-creating the Vellum Cloth and Pressure constraints) feeding a **Vellum Solver**, with gravity removed so the letters don't fall. To get the wrinkled balloon-fabric look, the Vellum Cloth constraint's rest-scale/stiffness values are pushed to unusual extremes: stretch stiffness cranked to ~10,000, bend stiffness dropped to ~0.01 — producing an uncontrolled, overly wrinkled result — then the **Vellum Pressure** constraint's rest-scale is set high (~50) and only a single simulated frame is used (not letting it fully settle), since one particular early frame produced the best-looking wrinkle pattern. The chosen frame is baked to a **Vellum I/O cache** (with "remove time dependent" caching) so it can be frozen and used as static geometry for rendering. Rendering brings the geometry into Solaris, assigns a Karma Material Builder material, uses a Dome Light with an HDRI (from Poly Haven), sets Karma to XPU, tweaks camera/quality/reflection-refraction limits, disables the environment-light background for a clean black backdrop, and finishes with a simple gold/metallic MaterialX shader (increased metalness and roughness) rather than building a full custom material.

### Key Steps
1. Create text via **Font** node, **Extrude** (~0.2, with back cap enabled), choosing a rounded-corner font style that suits the inflated look.
2. Convert to **VDB from Polygons** and use **VDB Smooth** to round out the sharp extruded edges (a plain Bevel wasn't smooth enough for this effect).
3. Convert back to polygons to check the result; if it still looks rough, increase the smooth amount (~10) and add a **VDB Reshape/Erode** pass to further refine the rounded shape.
4. Since this VDB-derived geometry isn't ideal for simulation, **Remesh** it with a small remesh size (~0.0075) for clean, simulation-friendly topology.
5. Set up **Vellum Configure Balloon** (auto-creates the Vellum Cloth constraint and Vellum Pressure constraint) and connect it to a **Vellum Solver** (hold J to drag-connect nodes quickly).
6. Remove gravity from the solver so the balloon letters don't fall.
7. In the **Vellum Cloth** constraint, push the **stretch stiffness** rest-scale/value up dramatically (author uses ~10,000) and drop the **bend stiffness** down to ~0.01 — producing an initial, overly-wrinkled/uncontrolled result.
8. In the **Vellum Pressure** constraint, set the rest-scale to a high value (~50) to control the amount of inflation/wrinkle detail.
9. Rather than simulating to convergence, **scrub through individual frames** and pick whichever single frame gives the best wrinkle look (an earlier, less-settled frame was chosen over a later one that looked "too much").
10. Bake the chosen frame to a **Vellum I/O** cache node with time-dependent caching disabled, freezing it as static geometry.
11. **Render setup**: import the geometry into Solaris, create a Material Library with a Karma Material Builder, assign it to everything; add a Dome Light using an HDRI (Poly Haven, "Christmas photo studio"); set the render engine to **Karma XPU**, tune quality/diffuse/reflection/refraction limits, disable the dome light as a visible background for a clean black backdrop, and enable "save viewport size" for camera-less quick renders.
12. Finish with a simple gold-look MaterialX shader: increase metalness and bump up roughness slightly, without building a fully custom shading network.

### Houdini Nodes / VEX / Settings
Font, Extrude, VDB from Polygons, VDB Smooth, Convert VDB, VDB Reshape/Erode, Remesh, Vellum Configure Balloon (Vellum Cloth + Vellum Pressure constraints), Vellum Solver (gravity disabled), stiffness/rest-scale tuning (stretch ~10,000, bend ~0.01, pressure rest-scale ~50), frame-by-frame visual selection (no full settle), Vellum I/O (time-dependent caching disabled), Material Library, Karma Material Builder, Dome Light (Poly Haven HDRI), Karma XPU render settings, MaterialX Standard Surface (metalness/roughness gold look).

### Difficulty
Intermediate (the technique is approachable — mostly extreme parameter tuning and frame-picking rather than complex node networks).

### Houdini Version
20.5.331 (visible in viewport title bar).

### Tags
vellum, vdb, typography, karma, materialx, simulation, balloon, text-effects

---

## Related Tutorials
- [Vellum Typography in Houdini](vellum-typography-in-houdini.md) — likely companion/alternate typography-effect video using Vellum from the same channel.
- [Modeling Assets with Vellum](modeling-assets-with-vellum.md) — shares the studio's broader pattern of using Vellum for stylized deformation rather than realistic simulation.

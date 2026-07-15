---
title: Vellum Typography in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=Sr7iwTjwo2E
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.701"
tags: [vellum, curvature, remesh, materialx, karma, typography, wrinkles, animated-mask, metal]
extraction_status: complete
frames_dir: tutorials/frames/vellum-typography-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Vellum Typography in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=Sr7iwTjwo2E)
**Author:** cgside
**Duration:** 6m36s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I'm gonna be showing you how you can
[0:06] build this typography effect using Valum. Along the way we will learn how to use
[0:11] some custom masks to feed our Valum simulation. So let's get started! So here's the
[0:20] final result of my setup. Let's start from the beginning. I used first a font to
[0:27] create the text using a custom font but you can find it for free online. Then I
[0:34] use an edit to place the letters to arrange them then creating a match size to
[0:41] place them in the center and adding some thickness. From here I can create a
[0:47] VDB from polygons, smooth it and convert it to polygons as you can see. And now
[0:57] after the thicken I can split the primitives along the Z axis and group the
[1:07] unshared edges, convert to curves, re-sample them and re-project them into the
[1:17] converted VDB, the geometry. Then I create a curvature attribute on the curves and
[1:26] with a value of 1 then one on the geometry with a value of 0 and the one
[1:35] attribute transfer as you can see. So I have these results so I can have those
[1:42] wrinkles around the curvature I guess. And I'm playing with the blend width so I
[1:52] can get this nice transition. Then in here I'm remashing by attributes so
[2:00] using the target mesh size attribute and I'm remashing between those values
[2:06] using the curvature so I get more polygons around the parts that will
[2:17] have those details. As you can see I have more polygons in here, probably can
[2:24] see it from the distance better. And then I'm animating the curvature
[2:31] attributes as you can see from 0 to 1 and I'm animating between frame 12 and 14.
[2:40] So I just want them at the ends. From here I'm creating my bounds or my
[2:51] collision geometry which is just a box from a bound and creating the valum plot.
[3:00] Pretty much default settings and I saved this output group the stretch because
[3:08] I'm going to use it in the valum solver and the valum pressure. This is just a
[3:13] valum configurable one. Then on the valum pressure I am also saving the pressure
[3:19] group and then I have the valum solver. So in the valum solver I am creating a
[3:28] valum constraint property on the pressure group and animating between frame
[3:34] 1 and 15. The rest length scale from a value of 1 to 5.5. So just expanding the
[3:42] letters. Then I have another one on the stretch group where I'm loading in the
[3:50] mask and blending the rest scale with that specific mask. Between the original
[3:57] rest scale or wrestling scale and a multiplied one in this case by 1.8.
[4:05] And if we have a look at the simulation as you can see from frame 13 at frame 12
[4:19] we don't have those details but from frame 13 to 15 we start to get them.
[4:28] And that was the desired look I was after. And I'm just time shifting on frame 15
[4:38] doing a valum post process to smooth out the geometry and give it one level of
[4:47] subdivision. Deleting the attributes and creating a connectivity and just
[4:55] softened the normals. Then in Solaris I'm importing the geometry and creating
[5:04] a material based on the class attribute we created with the connectivity nodes
[5:09] and from that I use a random material X random color and played with the U
[5:19] range and saturation and brightness and also the seeds and created that specific
[5:27] yellowish color or gold color. And I'm also adding the
[5:35] setting the metalness to one and playing with the roughness and the coat
[5:42] attributes or parameters. I have also a dome lights in the scene and the lights on
[5:53] the left side as you can see which is creating some nice reflections and if we
[6:02] render these as you can see we have that metallic look and those wrinkles are
[6:13] quite visible. So yeah this was a quick one just to show you how simple it is to
[6:21] build this typography effect. You can as always grab the file on my
[6:28] Patreon and yeah I hope to see you next time. Thank you.



---

## Captured Frames

- [0:25] tutorials/frames/vellum-typography-in-houdini/frame_000.jpg
- [0:50] tutorials/frames/vellum-typography-in-houdini/frame_001.jpg
- [1:30] tutorials/frames/vellum-typography-in-houdini/frame_002.jpg
- [2:10] tutorials/frames/vellum-typography-in-houdini/frame_003.jpg
- [3:20] tutorials/frames/vellum-typography-in-houdini/frame_004.jpg
- [4:20] tutorials/frames/vellum-typography-in-houdini/frame_005.jpg
- [5:20] tutorials/frames/vellum-typography-in-houdini/frame_006.jpg
- [6:20] tutorials/frames/vellum-typography-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
Drive a Vellum balloon-typography simulation with a **curvature-derived, animated custom mask** — computed from the letters' inner-edge curves, remeshed by attribute for extra detail there, and animated from 0 to 1 only near the end of the sim — so the pressure/stretch constraints locally amplify only around tight curves, producing realistic wrinkles concentrated exactly where real inflated letters would wrinkle.

### Summary
Text is created via Font, arranged with an Edit node, centered/thickened via Match Size, then rounded with a VDB from Polygons → Smooth → Convert back to polygons pass. After splitting primitives along Z and grouping unshared edges, those edges are converted to curves, resampled, and re-projected onto the VDB-smoothed geometry. A curvature attribute is set to 1 on the curves and 0 on the base geometry, then blended via Attribute Transfer with a tunable blend width for a smooth falloff — concentrating detail near the letters' inner curves. **Remesh by Attribute** uses this curvature value to drive a target-mesh-size range, adding more polygons specifically where wrinkle detail will appear. The curvature attribute is then **animated from 0 to 1 between frames 12 and 14** — deliberately localized to the sim's tail end. Collision geometry is a simple Bound-derived box; **Vellum Configure Balloon** creates the cloth/pressure setup, with the stretch group and pressure group both saved for solver-level targeting. Inside the **Vellum Solver**, a Vellum Constraint Property on the **pressure group** animates rest-length-scale from 1 to 5.5 between frames 1 and 15 (inflating the letters), while a second constraint on the **stretch group** loads the curvature mask and blends between the original rest scale and a **1.8×-multiplied** rest scale using that mask — so only the curvature-flagged regions stretch more, creating wrinkles that only appear from frame 13 onward once the animated curvature mask kicks in. After Time Shifting to frame 15, a Vellum Post Process smooths the geometry with one level of subdivision, unneeded attributes are deleted, Connectivity creates a per-letter class attribute, and normals are softened. In Solaris, a MaterialX Random Color node keyed to the connectivity class attribute (with tuned hue range/saturation/brightness/seed) produces a gold/yellow color variation per letter, with metalness set to 1 and roughness/coat tuned for a glossy balloon-metal look; a Dome Light plus a side light complete the setup for the final metallic, visibly-wrinkled render.

### Key Steps
1. Create text via **Font**, arrange letters with an **Edit** node, center and add thickness via **Match Size**.
2. Round the extruded shape with **VDB from Polygons** → **VDB Smooth** → **Convert VDB** back to polygons.
3. **Split** primitives along Z, group unshared edges, **Convert Line**, **Resample**, and re-project the curves onto the VDB-smoothed geometry via Ray Project.
4. Set a **curvature** attribute to 1 on the curves and 0 on the base geometry, then blend with **Attribute Transfer** using a tunable blend width for a smooth falloff around the letters' inner edges.
5. **Remesh by Attribute**: use the curvature value to drive a target-mesh-size range, so more polygons are added specifically in the curvature/wrinkle-prone regions.
6. **Animate the curvature attribute from 0 to 1 between frames 12 and 14** — deliberately timed to only affect the tail end of the simulation, so wrinkles appear late rather than throughout.
7. Build collision geometry from a **Bound**-derived box; set up **Vellum Configure Balloon** (near-default settings), saving both the **stretch** output group and the **pressure** output group for solver targeting.
8. In the **Vellum Solver**, add a Vellum Constraint Property targeting the **pressure group**, animating rest-length-scale from **1 to 5.5** between frames 1 and 15 to inflate the letters.
9. Add a second Vellum Constraint Property targeting the **stretch group**, loading the curvature mask and **blending between the original rest scale and a 1.8×-multiplied rest scale** using that mask — so wrinkle-prone (high-curvature) regions stretch more once the mask activates.
10. Observe the result: no wrinkle detail visible up to frame 12, wrinkles begin appearing from frame 13 through 15 as the animated curvature mask ramps up — matching the desired look.
11. **Time Shift** to frame 15, run a **Vellum Post Process** to smooth the geometry with one level of subdivision, delete unneeded attributes, run **Connectivity** for a per-letter class attribute, and soften normals.
12. **Shading in Solaris**: import the geometry, build a material keyed by the Connectivity class attribute feeding a **MaterialX Random Color** node — tune hue range, saturation, brightness, and seed to land on a gold/yellow color variation per letter; set metalness to 1 and adjust roughness/coat for a glossy balloon look.
13. Light with a Dome Light plus a side light for reflections; render to show the metallic look with visible wrinkles concentrated exactly where the animated curvature mask drove extra stretch.

### Houdini Nodes / VEX / Settings
Font, Edit, Match Size, VDB from Polygons, VDB Smooth, Convert VDB, Split, Group (unshared edges), Convert Line, Resample, Ray Project, Attribute Create (curvature = 0/1), Attribute Transfer (blend width), Remesh by Attribute (curvature-driven target mesh size), animated curvature attribute (frame 12→14), Bound (collision box), Vellum Configure Balloon (stretch/pressure output groups), Vellum Solver, Vellum Constraint Property (pressure-group rest-length-scale animation 1→5.5 over frames 1–15; stretch-group mask-blended rest scale ×1.8), Time Shift, Vellum Post Process (smooth + subdivision), Attribute Delete, Connectivity (per-letter class), soft normals, MaterialX Random Color (hue/saturation/brightness/seed keyed by class attribute), Standard Surface (metalness 1, roughness/coat tuning), Dome Light + side light, Karma render.

### Difficulty
Advanced (the curvature-derived animated mask driving two separate Vellum constraint properties is a sophisticated, non-obvious simulation-shaping technique).

### Houdini Version
20.5.701 (visible in viewport title bar).

### Tags
vellum, curvature, remesh, materialx, karma, typography, wrinkles, animated-mask, metal

---

## Related Tutorials
- [Vellum Balloon Text in Houdini](vellum-balloon-text-in-houdini.md) — earlier, simpler balloon-typography video from the same channel using extreme stiffness values instead of a curvature-driven animated mask for wrinkle control.
- [Modeling Assets with Vellum](modeling-assets-with-vellum.md) — shares the broader pattern of using Vellum constraints/masks for stylized deformation rather than realistic simulation.

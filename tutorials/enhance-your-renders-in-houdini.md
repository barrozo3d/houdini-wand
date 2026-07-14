---
title: Enhance your renders in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=c193tsyLH-0
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, vdb, cops, texturing, procedural, shaders, karma, noise, food, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/enhance-your-renders-in-houdini/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Enhance your renders in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=c193tsyLH-0)
**Author:** cgside
**Duration:** 10m21s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this video I wanted to show you a few techniques in Odini
[0:07] when I was working in this project. Basically I want to show you how to add more life to it
[0:15] by using let's say cops for texturing, doing some water drops and also add more life to these
[0:25] otherwise boring letters. So yeah let's get into it. So the first thing I wanted to show you is


### Deformation [0:30]
**Transcript (timestamped):**
[0:34] on how to deform a bit these letters to add a bit more detail. So I'm starting by isolating
[0:45] the letters and I imported this as an FBX from ZBrush and it comes with a name attribute from
[0:55] the subtitles. So here I have the letters and my final goal is to deform the ends or the edges
[1:05] to have these only lighting effect as you can see. It's just a lazy way of doing it. I could have
[1:14] sculpted a bit more and added more detail but I felt like I felt like using Odini to do some operations
[1:23] some final touches. So I'm first isolating the letters then running a loop because I have to
[1:32] but the principle is really easy. We isolate these corner edges, these are angles.
[1:40] So by using the mini edge angle in a group note then I'm converting those edges to lines
[1:50] and blasting everything but primitive zero in this case I'm isolating just one.
[1:59] Doing a basic resample and fusing to unites the curve. Then from here we can deform it.
[2:09] Using the scene function as you can see it's really simple just scene of the curve view.
[2:19] It's not really curve view but it's using the same principle and I'm just displacing it as you can see.
[2:27] Now the idea is to apply this to the geometry and you can do that by saving a rest state which in the
[2:36] East cases before we apply the deforming geometry. And then with the letters set to points and you can play
[2:46] with the radius and with the normalized threshold. You can input the rest geometry in the second input and on the
[2:53] third you input the deform geometry and you go from this to this more life like geometry at least that was my idea.
[3:05] And then you can I can also compile this I believe. Yes I didn't do that it's just two pieces.
[3:14] So yeah that was the first tip. So now I wanted to show you how you can create some water drops in a really
[3:24] simple way and cheap way at least I believe. And the way you do that in this case way I'm doing it is
[3:34] by isolating the parts that will receive those water drops. And then I'm remaching and the reason I'm
[3:42] remaching is because before we didn't have a consistent amount of geometry or distribution of geometry
[3:51] and that will not work for this approach. So I'm remaching and then subdividing in this case open sub-div loop
[4:01] because we are working with triangles. And then I'm creating an attribute noise as you can see by
[4:10] branching the values I can get these isolated spots, these islands doing a second one to add smaller ones as you can see.
[4:22] Then in this wrangle I'm displacing that geometry along the normal those areas along the normal.
[4:30] Blasting away anything that is not part of those areas.
[4:40] Creating an add to delete any unused points but this is really a mess and can't be used.
[4:48] So I'm also deleting the interior parts as you can see by working out the distance between the
[4:58] bounding box center and then just removing by threshold. Then I'm doing a remached grid and this looks like
[5:08] is going to work a bit better and I'm using tin plates so we can work with single-sided geometry.
[5:16] Assembling and grouping randomly some parts that I want to delete because I felt that was just too much.
[5:26] I'm packing and doing a basic PDB operation to reshape the bubbles or the water drops basically by doing a VDB from polygons,
[5:40] reshape a bit and converting to polygons.
[5:44] And that's how the water drops were done. That's all.
[5:50] Now let's have a look on how to do the shading or the texturing for this paddy that you see in the final render.


### Shading [5:52]
**Transcript (timestamped):**
[6:00] Let's dive into that network and I will get some space in here.
[6:10] So the idea is simple is to layer a bunch of different noises and I'm doing a fractural 3D noises and for that you need to
[6:24] restore the original position so you can fit that into the position of the fractal noise.
[6:32] So this is my first noise that will act as an overall displacement and it will also affect the
[6:42] the Albedo or the SSS. Then I have a second one and a finer detailed one and finally this one.
[6:52] And this will make more sense if I start to look at the first colors.
[6:56] So with the first noise that we have in here I am blending two colors and using that noise as a mask.
[7:06] So this is our first noise. Then this Chevy Chef is being used yet with another color.
[7:16] As you can see blending, starting to shame those noises.
[7:22] And this one is the finer detail. So a darker color to have those fine details.
[7:30] And finally the gray part which is that last noise will look that as you can see in here.
[7:42] And for the displacement let's see if this doesn't break.
[7:48] I'm gonna start to disable them.
[7:54] And so the first noise that we looked in a minute is just an overall displacement that I'm using.
[8:06] And as you can see I have these multiply constants and remaps. It's just a way to control the noise.
[8:12] So when it goes to render I don't have to play with a remap and reduce or reduce the displacement amount.
[8:20] So yeah, usually you want this pretty low.
[8:26] So this is the first noise. Then I'm layering the second one which is adding quite a bit of detail as you can see.
[8:36] That Chevy Chef, I just found that worked really well.
[8:40] And then for the third one is adding that finer detail.
[8:44] If you remember from here, so this finer detail.
[8:50] And finally displacing the gray part.
[8:54] As you can see this part in here which you can see also in here.
[9:02] So those yellow spots.
[9:04] So yeah, that's basically the texturing of the paddy.
[9:12] And I'm doing that for all the other geometries that you see in here.
[9:18] And let me just do a final render.


### Final render [9:23]
**Transcript (timestamped):**
[9:24] So yeah, that was my attempt on creating a CGI burger.
[9:28] If you want you can grab the full scene on my Patreon.
[9:32] And I hope you have learned something new from this video. Let me know in the comments.
[9:38] And also if you want to create a more realistic burger, I couldn't recommend enough this channel called the Anan.
[9:47] And he also gave me some feedback on my burger.
[9:51] Because I was inspired by this amazingly detailed burger that he created.
[9:57] And he does for his channel.
[10:00] It's a long series of videos.
[10:04] So if you are really interested in creating something similar, you can check out his channel.
[10:12] Other than that, thank you for watching.
[10:15] And I'll see you next time. Thank you.



---

## Captured Frames

- [0:10] tutorials/frames/enhance-your-renders-in-houdini/frame_000.jpg
- [1:50] tutorials/frames/enhance-your-renders-in-houdini/frame_001.jpg
- [3:30] tutorials/frames/enhance-your-renders-in-houdini/frame_002.jpg
- [5:00] tutorials/frames/enhance-your-renders-in-houdini/frame_003.jpg
- [6:10] tutorials/frames/enhance-your-renders-in-houdini/frame_004.jpg
- [8:20] tutorials/frames/enhance-your-renders-in-houdini/frame_005.jpg

---

## Structured Notes

### Core Technique
Three finishing tricks used on a CGI burger render: adding sine-wave edge deformation + Lattice-based rest/deform capture to fake extra sculpted detail on ZBrush-imported letter geometry, generating cheap procedural water-drop/bubble clusters via noise-masked normal displacement + VDB reshaping, and layering multiple fractal noises in COPs to drive both the color/albedo and the displacement of a food (patty) shader.

### Summary
For the lettering (imported as FBX from ZBrush with a `name` attribute from the original subtitles), the goal was to add a subtle wavy/lit edge highlight cheaply instead of hand-sculpting more detail. Corner/angle edges are isolated via **Group** (min edge angle), converted to a line, isolated to a single primitive, resampled and fused into one continuous curve, then displaced using `sin()` of the curve's parametric value (curve-U, referred to loosely as "curve view") for a simple wave. That deformed curve becomes a **Lattice** deformer's target: the original geometry (converted to points) is captured with tunable radius/normalize-threshold, with the rest-state geometry on the second input and the deformed curve on the third, giving a "more lifelike" edge without manual sculpting; the whole two-node setup can optionally be compiled into a single Compile Block for performance. For water drops on the bun, geometry destined to receive drops is Remeshed to get uniform point distribution (needed for the following noise step to work reliably), Subdivided (Open Subdiv, Loop scheme since working with triangles), and passed through a branched **Attribute Noise** pass (two noise layers, a coarser one for larger islands and a finer one for smaller ones) that isolates "islands"; a wrangle displaces those island points along their normal, then everything not part of an island is blasted away, unused points are cleaned with **Add** (delete unused points), and interior "mess" geometry is removed by thresholding the distance from each point to its piece's bounding-box center. The surviving points are remeshed into a grid, converted to Tin/thin-plate single-sided shells, packed, randomly grouped/deleted to thin out overly dense clusters, then reshaped into rounder droplet forms via a **VDB From Polygons → VDB Reshape → convert back to polygons** pass. For shading the patty (and, by extension, all the other food geometries in the scene), a layered **COPs fractal-noise stack** does double duty: three chained 3D fractal noises (using **Restore Position** to feed real-world `P` into the noise so it stays consistent regardless of UV layout) each drive both a color-blend layer (masking between different browns/darker tones per noise) and a displacement contribution — a first coarse noise for overall shape displacement (kept subtle, with Remap/Multiply-constant controls used purely so displacement strength can be tuned without re-touching the Remap at render time), a second finer noise adding significant surface detail (a specific noise type the author found worked especially well), and a third even-finer noise for fine surface grain, plus a final flat gray "burnt spot" pass layered on top for yellowish char detail.

### Key Steps
1. **Isolate corner/wave curve:** Group SOP (edges by min edge angle) on the imported letter geometry → Convert Line → Blast down to a single primitive (index 0) → Resample → Fuse to unify into one continuous curve.
2. **Wave deform:** displace the isolated curve using `sin()` of its parametric/curve-U value (a simplified "curve view"-style displacement) to create a gentle undulating wave along the curve.
3. **Lattice capture for "more lifelike" edges:** save a rest-state copy of the original geometry before deforming; feed a **Lattice** SOP set to Points, with tunable Radius and Normalize Threshold — original geometry on input 1 (as points), rest geometry on input 2, and the sine-deformed curve on input 3 — to transfer the curve's displacement onto the letter's edge geometry; optionally wrap the setup in a Compile Block for performance (author left it as two separate nodes here).
4. **Prep for water drops:** Remesh the target surface region to guarantee even point density, then Subdivide (Open Subdiv, Loop — required since the mesh is triangulated) so the following per-point noise step behaves predictably.
5. **Island generation:** run **Attribute Noise** twice (branched) — a coarser pass for bigger drop islands, a finer pass layered in for smaller ones — to identify which points belong to a "drop"; in an Attribute Wrangle, displace those island points along their normal, then Blast away everything not part of an island.
6. **Cleanup:** use **Add** (delete unused points) to remove now-orphaned points; remove leftover interior "mess" geometry per-piece by measuring distance from each point to its piece's bounding-box center and thresholding it away.
7. **Droplet reconstruction:** Remesh to a Grid, convert to **Tin (thin-plate)** single-sided shells for lightweight geometry, Assemble + randomly group/delete some pieces to thin out an overly dense result, Pack, then run **VDB From Polygons → VDB Reshape → convert to Polygons** to round the shells into believable rounded water-drop/bubble forms.
8. **Shading network (COPs):** for each food surface (patty shown as the example), use **Restore Position** to recover true 3D `P` for 3D **Fractal Noise** sampling (keeps noise consistent regardless of UV layout); layer 3 fractal noises of increasing fineness plus a final flat "burnt spot" gray layer — each noise both blends a color pair (as a mask between two browns/tones, darker for finer details) and drives a portion of the final displacement.
9. **Displacement control:** for the coarse overall-displacement noise, add Multiply-constant and Remap nodes purely so the displacement strength can be dialed in at render time without needing to re-adjust the Remap directly; keep the overall displacement amount low relative to the color-driving noise contributions.
10. **Repeat per asset:** apply the same layered-noise shading network to all other food geometries in the scene for visual consistency.

### Houdini Nodes / VEX / Settings
SOPs: Group (min/max edge angle), Convert Line, Blast, Resample, Fuse, Attribute Wrangle (VEX `sin()` on curve-U for wave displacement; normal-based island displacement; bbox-center distance threshold cleanup), Lattice (Points mode, Radius, Normalize Threshold, 3-input rest/deform capture), Compile Block (optional), Remesh, Subdivide (Open Subdiv, Loop), Attribute Noise (branched, coarse + fine passes), Add (delete unused points), Assemble, Pack, Tin (thin-plate single-sided conversion), VDB From Polygons, VDB Reshape. COPs: Restore Position, Fractal Noise (3D, layered x3 at increasing fineness + a flat gray "burnt spot" layer), Blend/mask-based color mixing, Multiply (constant), Remap (render-time displacement control).

### Difficulty
Intermediate — no especially advanced VEX, but requires understanding of Lattice-based rest/deform capture and layered noise-driven COPs shading; the water-drop pipeline has several non-obvious cleanup steps.

### Houdini Version
20.5 (UI matches Houdini 20.5-era Copernicus/Karma workflow).

### Tags
#vex #vdb #cops #texturing #procedural #shaders #karma #noise #food #intermediate

---

## Related Tutorials
Cross-link with any other cgside COPs-materials or VDB-reshaping tutorials once extracted from this batch — shares the layered-fractal-noise-for-color-and-displacement pattern with the mattress/leather materials tutorials.

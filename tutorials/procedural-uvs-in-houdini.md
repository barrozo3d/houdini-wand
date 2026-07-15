---
title: Procedural UV's In Houdini
source: YouTube
url: https://www.youtube.com/watch?v=7ZJeWIFYSxg
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.302"
tags: [uvs, find-shortest-path, vdb, vex, hda, gradient, cake, procedural-uvs]
extraction_status: complete
frames_dir: tutorials/frames/procedural-uvs-in-houdini/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural UV's In Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=7ZJeWIFYSxg)
**Author:** cgside
**Duration:** 4m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'll be showing you how you can do some procedural
[0:05] UVs in Odinni.
[0:06] Basically I add this geometry which is a bit iPolly from a VDB operation and I couldn't
[0:14] select any seams or do the UVs in a more traditional way so I have a technique to show you
[0:21] now you can UV a mesh like this.
[0:24] So yeah let's get into it.
[0:27] Okay starting with this initial geometry which is a bit iPolly and a weird
[0:33] uh, tessellation as you can see.
[0:36] So let's look at this what I called sheep UVs.
[0:39] So first I'm remashing it to reduce the polycount and re-projecting it to the original
[0:45] geometry so we keep the silhouette.
[0:48] Then poly reducing because I'm going to select only those art angles, those edges
[0:56] by using the mean edge length and as you can see it's doing a good job.
[1:02] This will end up being our seams.
[1:05] Then converting to a line, re-sampling it quite a bit and re-projecting it to the original
[1:11] cake geometry.
[1:13] Smoothed bit lines, creating a group called seams and now I'm going to add a color in
[1:20] this case red and a black color to the cake then transferring that and since we're going
[1:25] to use the fine shortest pet node we'll use this as a cost attribute.
[1:31] But in this case we need it inverted, that's why I am using this.
[1:37] I am inverting the red color and coming to this part of the network we have to the curves.
[1:46] Now we need to re-sample it quite a bit otherwise we would iterate too many times in the loop.
[1:52] So re-sampling it and converting to line so each segment becomes a single primitive as
[1:57] you can see.
[1:58] I can show you the points.
[2:00] And we will iterate over each line which just have two points.
[2:06] And in the fine shortest pet we can introduce that pet cost that we created and start an
[2:11] end points to 0 and 1.
[2:13] And if we iterate we get the shortest pet of those lines.
[2:21] And then we can group it and group transfer it to the original geometry as you can see.
[2:27] Then it's a matter of UV flatten and passing the seams and we end up with some almost perfect
[2:37] UVs for this kind of geometry.
[2:41] So as you can see some of the UV shells are slightly rotated and of course you can
[2:46] use a UV transfer.
[2:48] But let's level up the procedural approach using this HDEI created.
[2:54] And I will make sure to include these on the patron files.
[2:58] But basically I am creating a connectivity on the UVs.
[3:02] Then adding a mask along the Y using the relative bounding box.
[3:08] Swapping these two UV space and now we can measure the gradients of that mask as you can
[3:14] see we will have the direction.
[3:16] And finally we can calculate the angle by using some bags.
[3:22] And swapping it again to 3D space let's say and UV layouts to have them because in this
[3:32] part they can be overlapping each other.
[3:39] Some UVs to vertices I believe yes and then fusing the points.
[3:46] And that's basically how I've done the UVs for this cake and I've done the same for
[3:50] the slice as you can see.
[3:52] And of course this is basic geometry but I hope this is coming in handy in some of your
[3:59] future projects.
[4:01] So yeah that's basically it.
[4:02] If you want you can grab this part of the scene on Patreon and I hope to see you next
[4:07] time.



---

## Captured Frames

- [0:20] tutorials/frames/procedural-uvs-in-houdini/frame_000.jpg
- [1:00] tutorials/frames/procedural-uvs-in-houdini/frame_001.jpg
- [1:40] tutorials/frames/procedural-uvs-in-houdini/frame_002.jpg
- [2:30] tutorials/frames/procedural-uvs-in-houdini/frame_003.jpg
- [3:10] tutorials/frames/procedural-uvs-in-houdini/frame_004.jpg
- [3:50] tutorials/frames/procedural-uvs-in-houdini/frame_005.jpg

---

## Structured Notes

### Core Technique
UV a messy, high-poly VDB-derived mesh (a cut cake slice) with no clean manual seam options by procedurally deriving seam curves from a simplified/edge-angle-detected proxy, using **Find Shortest Path** (fed a color-derived cost attribute) to snap those rough seam curves onto exact edge paths on the real geometry, then fixing island rotation with a custom **Orient UVs Up** HDA that measures a UV-space gradient to auto-align each shell.

### Summary
The source geometry (from a VDB Boolean cut) is too irregular/tessellated for traditional manual seam picking. The fix: build a simplified proxy by Remeshing (reducing polycount) and Ray-projecting it back onto the original silhouette, then **Poly Reduce** it further so only the sharpest edges remain — these are selected via a **mean-edge-length/edge-angle** Group, which reliably marks the natural break lines (the future seams). That edge selection is converted to a Line, heavily Resampled, and Ray-projected back onto the original cake geometry, then smoothed slightly and grouped as "seams." A red/black color is assigned and transferred onto the original mesh to serve as a **cost attribute for Find Shortest Path** — inverted since the red channel needs flipping for the cost to behave correctly. The seam-guide curve is Resampled heavily and Converted to Line so each segment is a single 2-point primitive; a for-each loop over these segments runs **Find Shortest Path** using the assigned cost attribute (with start/end points set to 0/1) to snap each rough segment onto the exact shortest edge-path on the real mesh — the result is grouped and Group-Transferred back onto the original geometry as the true seam group, which finally feeds **UV Flatten** to produce almost-perfect UVs for this otherwise-impossible-to-hand-UV geometry. Since some resulting UV shells end up randomly rotated relative to each other, a custom **HDA** ("Cheap UVs" / orient-UVs-up style) fixes this: it runs Connectivity on the UV shells, builds a Y-axis mask from the relative bounding box, swaps that mask into UV space, **measures the gradient of the mask** to get a "which way is up" direction per shell, computes the rotation angle via VEX, swaps back to 3D space, and finally runs **UV Layout** to resolve any resulting overlaps — producing correctly-oriented, non-overlapping UV islands. The same pipeline was applied to both the main cake body and the cut slice piece.

### Key Steps
1. Build a simplified seam-detection proxy: **Remesh** the messy source geometry to reduce polycount, then **Ray**-project it back onto the original silhouette to preserve the overall shape.
2. **Poly Reduce** further and select the resulting sharp edges via a **mean edge length / edge angle** Group — these naturally mark the seam locations.
3. Convert that edge group to a **Line**, Resample heavily, and **Ray**-project the curve back onto the original high-poly cake geometry to get seam curves that actually sit on the real surface.
4. Smooth the projected lines slightly, group as "seams," assign a red/black color, and **transfer that color onto the original mesh** to act as a **Find Shortest Path cost attribute** — inverting the red channel so the cost behaves correctly (low-cost paths follow the intended seam).
5. **Resample** the seam-guide curve heavily and **Convert Line** so each 2-point segment becomes an individual primitive (needed for per-segment iteration).
6. Run a **for-each loop** over each 2-point segment, using **Find Shortest Path** with the assigned cost attribute and start/end points set to 0/1 — this snaps each rough guide segment onto the exact shortest edge-path on the real mesh.
7. **Group** the resulting shortest-path edges and **Group Transfer** them back onto the original geometry as the definitive seam group.
8. Feed that seam group into **UV Flatten** — produces near-perfect UVs for otherwise un-UV-able geometry, though some resulting shells end up randomly rotated relative to each other.
9. **Custom "Orient UVs Up" HDA fix**: run **Connectivity** on the UV shells; build a Y-axis mask using the relative bounding box; **swap the mask into UV space**.
10. **Measure the gradient** of that mask (per island) to determine each shell's "which way is up" direction; compute the required rotation angle via a VEX wrangle.
11. Swap back to 3D space, apply the computed rotation per shell, then run **UV Layout** to resolve any overlaps introduced by the rotation — final result: correctly-oriented, non-overlapping UV islands, applied to both the cake body and the cut slice piece.

### Houdini Nodes / VEX / Settings
Remesh, Ray (silhouette-preserving re-projection, ×2 uses), Poly Reduce, Group (mean edge length / edge angle seam detection), Convert Line, Resample, Smooth, color assignment (red/black) + Attribute Transfer (cost attribute), Find Shortest Path (cost-driven, per-segment for-each loop), Group + Group Transfer, UV Flatten, custom HDA ("Orient UVs Up" / "Cheap UVs"): Connectivity, relative-bounding-box Y mask, UV-space swap, Measure (gradient), VEX angle-computation wrangle, UV Layout (overlap resolution).

### Difficulty
Advanced (the Find-Shortest-Path-based seam-snapping and gradient-based UV-orientation HDA are both sophisticated, non-obvious solutions to a real production UV problem).

### Houdini Version
20.5.302 (visible in viewport title bar).

### Tags
uvs, find-shortest-path, vdb, vex, hda, gradient, cake, procedural-uvs

---

## Related Tutorials
- [Vex Problem Solving in Houdini](vex-problem-solving-in-houdini.md) — revisits this same UV-ing problem with a Cluster-node (normal-based) seam-detection alternative to the Find-Shortest-Path approach used here.
- [Orient UVS like a PRO in Houdini 21](orient-uvs-like-a-pro-in-houdini-21.md) — deeper, more robust follow-up version of the same gradient/oriented-bounding-box UV-auto-orientation HDA referenced here.
- [Procedural tips and tricks in Houdini 20.5](procedural-tips-and-tricks-in-houdini-205.md) — shares the Find Shortest Path technique used here, applied there to jewelry stone-holder wire meshes.
- [Vex quick tips #2 | Iterating over numbers](vex-quick-tips-2-iterating-over-numbers.md) — shares the Find Shortest Path technique used here, applied there to a randomized grid-cutting problem.

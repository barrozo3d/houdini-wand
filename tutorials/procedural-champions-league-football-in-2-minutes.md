---
title: Procedural Champions League football in 2 minutes
source: YouTube
url: https://www.youtube.com/watch?v=kpWtT6tPvP0
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.593"
tags: [platonic-solids, for-each, vex, uvs, sweep, procedural-modeling, ray-project, sports]
extraction_status: complete
frames_dir: tutorials/frames/procedural-champions-league-football-in-2-minutes/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Champions League football in 2 minutes

**Source:** [YouTube](https://www.youtube.com/watch?v=kpWtT6tPvP0)
**Author:** cgside
**Duration:** 2m16s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there, let's see how we can recreate the new champions league ball.
[0:04] We start with one of the Platonic solid presets, create the naturoput for each prem, then
[0:09] subdividing and rate projecting it to a perfect sphere.
[0:14] Now we need to create an orient the stars, so for that I am running a loop for each named
[0:20] primitive.
[0:21] Inside we add normals pointing in, subdivided and select the target point so we can recreate
[0:28] a star.
[0:29] Now we pick along the existing normals, subdivided and scale it down a bit to better represent
[0:35] the original design.
[0:38] Then we just need to invert the normals and rate projected along the main shape.
[0:44] Now in order to recreate that Jason stars look, we need to rotate them around the normal,
[0:50] using these wax snippets.
[0:54] Using the shape and re-projecting it.
[1:00] And then we can select the border edges and polyfill it with what's splitting the star
[1:06] springs by the initial ID we add and creating a connectivity attribute so we can use it
[1:13] for texturing and geo operations.
[1:17] And now just project everything again.
[1:20] So we get a spherical shape along the patches too.
[1:24] Now in this loop I am just emphasizing the patches, extruding in and out and then beveling
[1:30] the outer edge.
[1:32] Creating the UVs, using a near-adjusted some colors to use as a guide in Photoshop.
[1:40] And finally adding some subdivisions.
[1:44] For the stitches I just extracted the outer edges and converted it to a curve.
[1:51] Clean the shape with polypads and then we can cut at each point.
[1:57] Selecting every other cream and blasting those.
[2:00] And finally we can sweep the curves.
[2:04] So that's it, feel free to ask any questions and download the project files on my Patreon.
[2:11] See you next time.



---

## Captured Frames

- [0:10] tutorials/frames/procedural-champions-league-football-in-2-minutes/frame_000.jpg
- [0:30] tutorials/frames/procedural-champions-league-football-in-2-minutes/frame_001.jpg
- [0:55] tutorials/frames/procedural-champions-league-football-in-2-minutes/frame_002.jpg
- [1:20] tutorials/frames/procedural-champions-league-football-in-2-minutes/frame_003.jpg
- [1:50] tutorials/frames/procedural-champions-league-football-in-2-minutes/frame_004.jpg
- [2:10] tutorials/frames/procedural-champions-league-football-in-2-minutes/frame_005.jpg

---

## Structured Notes

### Core Technique
Recreate the Champions League football's distinctive star-panel pattern procedurally, starting from a Platonic solid base and using a for-each loop per named primitive to build each 5-pointed star patch, then Ray-projecting everything back onto a perfect sphere to keep the panels curved correctly.

### Summary
A Platonic solid preset provides the base panel layout; each primitive is named, subdivided, and Ray-projected onto a sphere for a spherical starting form. Inside a for-each loop over each named primitive, normals point inward, the shape is subdivided, and a target point is picked to recreate a 5-pointed star by picking along existing normals, subdividing, and scaling down. Normals are inverted and everything is Ray-projected onto the main shape again. A VEX-driven rotation (rotating each star patch around its own normal by an angle derived from a snippet) recreates the specific "jagged star" look seen on the real ball. Border edges are selected and Polyfilled, star springs are split by their initial ID with a Connectivity attribute for texturing/geo targeting, and the whole thing is Ray-projected again for a fully spherical result across all patches. A separate loop extrudes and bevels the patches for relief, generates UVs, and adds guide colors for Photoshop texturing. Stitches are created by extracting outer edges, converting to a curve, cleaning with Polypatch, cutting at each point, selecting every other segment, blasting, and Sweeping the remaining curves into stitch geometry.

### Key Steps
1. Start from one of Houdini's **Platonic solid** presets; create a name attribute per primitive, subdivide, and Ray-project the whole shape onto a perfect sphere.
2. Run a **for-each loop over each named primitive**: inside, add normals pointing inward, subdivide, and select a target point to begin recreating a star shape.
3. Build the star: pick geometry along the existing normals, subdivide, and scale down slightly to better match the reference design's proportions.
4. Invert the normals of the star shape and Ray-project it along the main sphere shape.
5. Recreate the "jagged star" look seen on the real ball by rotating each star patch **around its own normal** using a small VEX snippet, then re-project the result.
6. Select the border edges of each star patch and **Polyfill** them; split the star "springs" (points) by the initial ID attribute created earlier, and run **Connectivity** so the resulting pieces can be targeted for texturing or further geometry operations.
7. Ray-project everything again so the spherical shape extends correctly across all patches, not just the star centers.
8. In a second loop over the patches: extrude the patches in and out slightly, then bevel the outer edge for a relief/embossed look.
9. Generate UVs and add near-random guide colors to use as a visual reference layout when texturing in Photoshop.
10. **Stitches**: extract the outer edges of the patches and convert them to a curve; clean the resulting shape with **Polypatch**; cut the curve at every point to create individual segments; select every other segment and blast the unwanted ones; finally **Sweep** the remaining curve segments to generate the raised stitch geometry seen between panels.

### Houdini Nodes / VEX / Settings
Platonic solid, Name attribute, Subdivide, Ray (project onto sphere, used repeatedly), For-Each loop (per named primitive), Normal, Pick (along normals), Group Range, Peak, VEX snippet (rotation around normal), Polyfill, Split (by initial ID), Connectivity, Extrude, Bevel, UV generation, near-random guide-color assignment, Polypatch, Cut, Blast (every-other selection), Sweep (stitch geometry).

### Difficulty
Intermediate–Advanced (Ray-projection chaining, per-primitive for-each loops, and the normal-rotation VEX trick assume solid procedural fundamentals, though the result is a compact ~2 minute breakdown).

### Houdini Version
19.5.593 (visible in viewport title bar).

### Tags
platonic-solids, for-each, vex, uvs, sweep, procedural-modeling, ray-project, sports

---

## Related Tutorials
- [Procedural Boat in Houdini](procedural-boat-in-houdini.md) — another compact procedural-modeling breakdown from the same channel using similar for-each/loop patterns.
- [Groups, Patterns in Houdini](groups-patterns-in-houdini.md) — related group-selection patterns (including split-by-attribute and connectivity) used throughout this build.

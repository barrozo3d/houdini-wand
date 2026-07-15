---
title: Useful Vex snippets | Houdini tips and tricks
source: YouTube
url: https://www.youtube.com/watch?v=_C6-g1C--ws
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.760"
tags: [vex, uv-sample, sign-function, connectivity, minpos, vex-snippets, quick-tips]
extraction_status: complete
frames_dir: tutorials/frames/useful-vex-snippets-houdini-tips-and-tricks/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Useful Vex snippets | Houdini tips and tricks

**Source:** [YouTube](https://www.youtube.com/watch?v=_C6-g1C--ws)
**Author:** cgside
**Duration:** 3m20s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, in this video I'll share 5 different Vax snippets to help you improve your workflow,
[0:06] hopefully. All the scenes are up on my Patreon, by the way. So the first one is really simple,


### Move objects to center with vex [0:10]
**Transcript (timestamped):**
[0:12] but effective. I need to place these rocks in the center of the scene to later copy them to points.
[0:19] You could easily do that with a foreign slupe, with a match size with a line set to center,
[0:25] but a simpler way is to pack your objects and since we are dealing with points we can just use a
[0:30] wrangle and place them at zero. So I model this camera and want to place some logos and tags on


### Place labels and logos with uvsample [0:33]
**Transcript (timestamped):**
[0:37] it, and there's a simple line of Vax code that can do that. First I'm converting the Geo to UV space.
[0:45] I also have a texture with all the logos and in this case I am tracing them. From there placing
[0:51] them in the target UV space by using an edit node. And once they are in the correct UV space,
[0:59] I can simply use the UV sample to deform them with the shape of the camera.
[1:04] Another neat trick learned from the CGWiki discord. In this simple example I am using the


### Sign function with vex [1:08]
**Transcript (timestamped):**
[1:10] computed UVs from a sweep to deform the sides of a leaf shape. And since I need the opposite
[1:16] deformations on the left and right, I was creating an if statement so if the position x is bigger
[1:23] than zero deform it with positive offset otherwise make it negative. But turns out you can simplify
[1:30] this by using the sine function that will act here as a multiplier either positive or negative
[1:36] depending on the position x. Another great trick learned from swolch.
[1:41] Now let's say you have a bunch of randomly positioned shapes in this case in Y and want to make


### For each connected piece with vex [1:42]
**Transcript (timestamped):**
[1:48] them lay flat on the grid. And that's easy enough just to afford each connected piece and place
[1:55] a match size inside with the align Y set to mean. And this is the same way of doing it, but for
[2:02] learning purpose I decided to have a Vax alternative. And hopefully you can get some clips from it.
[2:09] So first we need a connectivity node. Then in Vax we gather the values of the class attribute
[2:15] with unique valves. It rate with a forage, filter the group, get the point numbers and also save
[2:22] the bounding box mean. Finally we can iterate over the points and if they are below the grid move
[2:29] them in the positive Y. By the same amount they are below. In this case adding to the position with
[2:36] absolute which will turn it to positive values. Again a bit overkill but always nice to know I
[2:42] believe. Let me know your thoughts in the comments. To finish this one is quite simple. I have some


### Snap mesh to curve with vex minpos [2:45]
**Transcript (timestamped):**
[2:48] road curves created some geo with a top of build and need to snap it to the curves. And that's
[2:54] a job for mean posts. One line of Vax or you can simply use the rain node except to you.


### Outro [3:00]
**Transcript (timestamped):**
[3:00] Okay that was it. This was more like a bunch of unfinished projects mixed together,
[3:06] but I decided to share these Vax snippets since I found them really useful.
[3:12] Grab the files on my Patreon and let's wait for our dnew 20.5 now. Thank you.



---

## Captured Frames

- [0:15] tutorials/frames/useful-vex-snippets-houdini-tips-and-tricks/frame_000.jpg
- [0:40] tutorials/frames/useful-vex-snippets-houdini-tips-and-tricks/frame_001.jpg
- [1:15] tutorials/frames/useful-vex-snippets-houdini-tips-and-tricks/frame_002.jpg
- [1:45] tutorials/frames/useful-vex-snippets-houdini-tips-and-tricks/frame_003.jpg
- [2:30] tutorials/frames/useful-vex-snippets-houdini-tips-and-tricks/frame_004.jpg
- [3:00] tutorials/frames/useful-vex-snippets-houdini-tips-and-tricks/frame_005.jpg

---

## Structured Notes

### Core Technique
Five compact VEX snippets: a one-liner to re-center packed points instead of a for-each+Match Size chain, using `uvsample()` to wrap flat UV-space logos/labels onto curved geometry, `sin()` as a positive/negative multiplier instead of an if-statement for mirrored deformations, a from-scratch Connectivity-driven VEX alternative to "lay flat on grid" (for learning purposes), and `minpos()` as a one-line replacement for snapping geometry onto a curve.

### Summary
Instead of a for-each loop with an internal Match Size (aligned to center) to re-center a batch of packed rock objects before Copy to Points, packed points can simply be moved to the origin with a single wrangle line setting position to zero — since with packed primitives you're really just repositioning points. For wrapping flat UV-space logo artwork onto a curved camera-body mesh: convert the geometry to UV space, trace the logo texture, use an **Edit** node to place the traced shapes in the correct target UV region, then use **`uvsample()`** to deform those flat shapes with the actual 3D shape of the camera. For mirrored deformation on a leaf shape (offset positive on one side, negative on the other along X), rather than an if/else branch testing `@P.x > 0`, multiply the offset by **`sign(@P.x)`** — the sign function itself acts as the +1/-1 multiplier. To make a for-each connected piece + internal Match Size (Align Y set to Mean) "lay flat on grid" setup, an educational pure-VEX alternative is shown: run Connectivity first, then in a detail-only wrangle gather the unique class-attribute values via a for-loop, filter/group per class, get the point numbers, and save each class's bounding-box mean; iterate over points and if a point's Y is below the grid, move it in the positive Y direction by the same amount it's below, adding `abs()` of that offset to the position. Finally, snapping a swept "road" tube onto its source curve is a one-liner using **`minpos()`** (or, more simply, a Ray node set to closest point).

### Key Steps
1. **Re-center packed points**: instead of for-each + internal Match Size (align to center), simply set the packed point's position to `{0,0,0}` in a wrangle — works because packed primitives are just points carrying a transform.
2. **UV-space logo wrapping**: convert the target geometry (camera body) to UV space; trace the logo/label artwork from a texture; use an **Edit** node to place the traced pieces at the correct target UV coordinates.
3. Apply **`uvsample()`** to deform the flat, UV-space-placed logo shapes using the actual 3D geometry's shape — effectively wrapping them onto the curved surface (technique credited to CGWiki Discord).
4. **Sign-function mirrored deformation**: on a leaf shape being deformed using Sweep-computed UVs, replace an if/else branch (`if (@P.x > 0) offset = +val; else offset = -val;`) with `offset *= sign(@P.x)` — simpler and equivalent (credit: swalch).
5. **VEX "lay flat on grid" alternative** (educational): run **Connectivity** to get a per-piece class attribute; in a detail-mode wrangle, gather unique class values via a for-loop, filter/group points per class, retrieve point numbers, and save each class's **bounding-box mean**.
6. Iterate over points: if a point's Y position is below the grid plane, move it in the **positive Y** direction by the same amount it's below, using `abs()` on the offset to ensure it always moves the correct direction regardless of sign.
7. **Snap geometry to curve**: for road-curve-following geometry (e.g. a swept tube), use **`minpos()`** in a one-line wrangle to snap points onto the nearest position on the source curve — equivalently achievable with a **Ray** node set to closest-point mode.

### Houdini Nodes / VEX / Settings
Attribute Wrangle (`v@P = {0,0,0}` packed-point recenter), UV conversion, Edit node (UV-space placement), `uvsample()` VEX function, `sign()` VEX function (mirrored offset multiplier), Connectivity, detail-mode Attribute Wrangle (for-loop over unique class values, group filtering, `pcfind`/point-number gathering, bounding-box mean per class), `abs()`-based directional correction, `minpos()` VEX function, Ray node (closest-point alternative).

### Difficulty
Intermediate (each snippet is a compact, standalone one-liner or short wrangle; the from-scratch Connectivity/class-iteration alternative is more involved but explicitly framed as an educational exercise).

### Houdini Version
20.5.760 (visible in viewport title bar).

### Tags
vex, uv-sample, sign-function, connectivity, minpos, vex-snippets, quick-tips

---

## Related Tutorials
- [Vex Problem Solving in Houdini](vex-problem-solving-in-houdini.md) — companion VEX-tips video from the same channel.
- [Vex Quick Tips 2 - Iterating over Numbers](vex-quick-tips-2-iterating-over-numbers.md) — related short-form VEX tips series from the same channel.

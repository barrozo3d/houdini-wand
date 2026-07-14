---
title: Displacement maps in cops | Houdini 20.5
source: YouTube
url: https://www.youtube.com/watch?v=xOeZncLWztc
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [cops, procedural, texturing, displacement, uv, tips, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/displacement-maps-in-cops-houdini-205/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Displacement maps in cops | Houdini 20.5

**Source:** [YouTube](https://www.youtube.com/watch?v=xOeZncLWztc)
**Author:** cgside
**Duration:** 2m59s | 10 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone, in this video I'll share a few useful workflows when working with cops in the New Odin 20.5.
[0:08] The full scene is available on my Patreon.
[0:11] So the first one is on how to create this chamfer look for your displacement maps, and it's quite easy, you can just use the feather note and play with the distance.


### Beveling with the feather node [0:12]
**Transcript (timestamped):**
[0:23] And this is different from the blur, where it would just smooth out the shapes.


### Isolating rows/columns with tile pattern [0:28]
**Transcript (timestamped):**
[0:28] If you only want one row of shapes with the style pattern notes, you can play with the pruning either by a tolerance value or by every other row or column.


### Mirror node in cops [0:39]
**Transcript (timestamped):**
[0:39] You also have a mirror note in cops, but here you need to set the angle and the distance as offset.


### Segment by connectivity, statistics by id and compare nodes [0:46]
**Transcript (timestamped):**
[0:46] So now I want to fill some shapes with patterns, and for that I am using the segment by connectivity notes, which will create this sort of pattern.
[0:57] Next I can use statistics by ID to isolate similar areas.
[1:02] In the composite view I can inspect the target value and feed it to a compare note in this case I set it to equals 2.
[1:10] And as you can see I successfully isolated the target areas.
[1:15] I have done the same for the middle parts, then just multiply some patterns over those areas.


### Custom points with orientation attribute [1:22]
**Transcript (timestamped):**
[1:22] For this specific star pattern I used a stop-import to create my own points, created a circle with the amount of points I need and also added the normals with wax, along with some custom biscale for every other point.
[1:38] And when I feed it to a stem point I get the expected result.
[1:44] Now tiling it, setting the pattern type to weather bound, which is the alternating setup.
[1:50] Instead of adding too many repetitions to the tile pattern, you can just scale it down and it will keep the tiling.


### Stamp points with custom shapes [1:58]
**Transcript (timestamped):**
[1:58] Since I found the tile pattern a bit hard to control the spacing, for this bottom pattern I created my custom points with a stop-import and used again the stem points, feeding the shape to the stem-import.


### Align patterns with mesh uv's [2:14]
**Transcript (timestamped):**
[2:14] As I need to align the pattern to my OVs I'm importing the original object using a RESTORISE setup to get the UVs position and a RESTORISE GU.
[2:27] Then I can use a blend with the pattern to check where I should translate it to.


### Final displacement/height map [2:33]
**Transcript (timestamped):**
[2:33] And finally connected to the eye channel of my preview material I am also using some ambient occlusion for preview purpose on the base color.


### Outro [2:43]
**Transcript (timestamped):**
[2:44] So I hope this helps you finding your ways in the new cups. It's still all new to me and I'm planning to share more in the future.
[2:52] Stay tuned and check the file in the description. Thank you.



---

## Captured Frames

- [0:15] tutorials/frames/displacement-maps-in-cops-houdini-205/frame_000.jpg
- [0:50] tutorials/frames/displacement-maps-in-cops-houdini-205/frame_001.jpg
- [1:25] tutorials/frames/displacement-maps-in-cops-houdini-205/frame_002.jpg
- [1:58] tutorials/frames/displacement-maps-in-cops-houdini-205/frame_003.jpg
- [2:18] tutorials/frames/displacement-maps-in-cops-houdini-205/frame_004.jpg
- [2:35] tutorials/frames/displacement-maps-in-cops-houdini-205/frame_005.jpg

---

## Structured Notes

### Core Technique
A short round-up of practical COPs workflows for building a cut-glass-style displacement/height map (star bursts, diamond lattice, chamfered facet edges) with correct UV alignment to the source mesh — a rapid-fire tips video rather than a single linear build.

### Summary
Covers ten quick techniques for building complex tileable displacement patterns in Houdini 20.5's Copernicus (COPs). A **Feather** node (not Blur) creates a beveled/chamfered look on hard pattern edges by controlling a distance parameter, producing sharp facet transitions rather than smoothed blur. **Tile Pattern**'s pruning options isolate single rows/columns by tolerance or every-other-row/column. A **Mirror** COP needs both an angle and a distance offset to work correctly. To fill irregular shapes with sub-patterns, **Segment by Connectivity** breaks a shape into labeled regions, **Statistics by ID** extracts per-region stats, and a **Compare** node (e.g. "equals 2", inspected via the Composite viewer) isolates a specific region by its ID to mask in a secondary pattern via Multiply. For a custom star pattern, a **Pop Import** builds custom points (from a circle with matching point count) with hand-authored normal and alternating pscale attributes, fed into a **Stamp Points** node using the "checkerboard"/alternating tile pattern type — scaling the whole setup down (rather than raising repetitions) is the easier way to increase tiling density while keeping spacing control. A second custom-point pattern for a bottom border uses the same Pop-Import + Stamp Points combo when Tile Pattern's own spacing controls prove too coarse. To align any pattern precisely to the mesh's actual UV layout, a **RestoreUV setup** (restorise/UV-position import) plus a Blend node lets you visually check and nudge the pattern's placement against the true UV footprint before finalizing. The finished pattern is wired into a preview material's height/displacement channel, with Ambient Occlusion added to the base color purely for preview clarity.

### Key Steps
1. **Chamfer/bevel look:** apply a **Feather** node (not Blur) to a hard-edged pattern and tune its distance parameter to get a sharp beveled-edge look instead of a smoothed one.
2. **Isolating rows/columns:** in **Tile Pattern**, use the pruning controls (tolerance-based, or explicit every-other-row/column) to keep only a single row or column of the repeating shape.
3. **Mirror setup:** when using the **Mirror** COP, remember it needs both an angle parameter and a distance value used as the offset — omitting either produces incorrect mirroring.
4. **Filling shapes with sub-patterns by region:** run **Segment by Connectivity** on a shape to label disconnected/connected regions, feed into **Statistics by ID** to inspect per-ID stats (viewable live in the Composite view), then use a **Compare** node (e.g. set to "equals 2") to isolate one target region as a mask; repeat for other target regions (e.g. the middle parts), then Multiply a secondary pattern into each isolated mask.
5. **Custom star-burst points:** use **Pop Import** to author custom points from a circle primitive with the exact point count needed, add per-point normal and alternating `pscale` attributes via VEX, feed the points into **Stamp Points**, and set the tiling pattern type to "checkerboard"/alternating ("weather bound" per the transcript, likely a mis-transcription) for the correct alternating layout; scale the whole pattern down rather than increasing repetitions to tighten tiling density while keeping spacing control.
6. **Custom bottom-border pattern:** when Tile Pattern's built-in spacing controls are too coarse to match a desired border layout, build another custom point set via Pop Import and feed a custom shape into Stamp Points instead.
7. **UV-aligned placement:** import the original mesh via a **restorise/RestoreUV** setup to recover true UV positions, then use a **Blend** node to visually compare the pattern against the mesh's real UV footprint and determine the correct translate offset before committing.
8. **Final output:** connect the finished pattern to the preview material's height/displacement ("eye") channel; add Ambient Occlusion to the base color purely to make the preview easier to read (not part of the final shading pipeline).

### Houdini Nodes / VEX / Settings
COPs used: Feather (chamfer/bevel distance), Blur (contrasted against Feather), Tile Pattern (pruning: tolerance / every-other row-column), Mirror (angle + distance offset), Segment by Connectivity, Statistics by ID, Compare (equals comparison, inspected via Composite viewer), Multiply/Blend, Pop Import (custom point generation from a circle, custom normal + alternating pscale attributes via VEX), Stamp Points (checkerboard/alternating pattern type), Transform (uniform scale-down for tiling density), RestoreUV/restorise setup (UV-position import from source geometry), Blend (visual UV-alignment check), Ambient Occlusion (preview-only).

### Difficulty
Intermediate — assumes familiarity with COPs basics and VEX point-attribute authoring (normals, pscale); the ID-based masking and UV-alignment workflow are the most non-obvious tricks.

### Houdini Version
20.5 (explicitly titled "Houdini 20.5"; author notes COPs is "still all new to me").

### Tags
#cops #procedural #texturing #displacement #uv #tips #intermediate

---

## Related Tutorials
Cross-link with other cgside COPs tutorials (custom procedural materials, designer-like materials, cliff shapes in COPs) once extracted from this batch — shares Tile Pattern, Blend, and mask-isolation vocabulary.

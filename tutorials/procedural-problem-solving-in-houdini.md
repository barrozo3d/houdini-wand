---
title: Procedural Problem Solving in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=5Cv1SJRm538
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.311"
tags: [groups, vex, boundary-groups, orient-along-curve, connectivity, hot-air-balloon, procedural-modeling]
extraction_status: complete
frames_dir: tutorials/frames/procedural-problem-solving-in-houdini/
frame_count: 9
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Problem Solving in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=5Cv1SJRm538)
**Author:** cgside
**Duration:** 4m26s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome in this video I'm sharing some tips on procedural problem solving,
[0:05] as always you can grab the files from my Patreon. So we start with a simple one on how to separate


### Boundary Groups [0:08]
**Transcript (timestamped):**
[0:11] multiple boundaries since I needed to manipulate the top one. It's quite simple just grouped by
[0:17] un-chaired edges in points mode and check the option create boundary groups. This will create
[0:22] different groups for each boundary in this case too. Then you can promote to edges or frames for
[0:29] your next operations. This can be useful to close the top boundary and not the bottom one for instance.


### Proed Roll [0:37]
**Transcript (timestamped):**
[0:37] Now the procedural pattern to create this effect I'm first separating each section and creating
[0:43] a connectivity attribute. Then it's rating over each piece and in a wrangle I'm creating this
[0:50] repeating pattern of values using the module along with the iteration value so I can offset the colors.
[1:00] In this case I am also targeting the first and second frames to have a specific value according to
[1:06] my reference. Having the attribute I can remap it with specific colors making sure I set the correct
[1:14] range by creating a maximum of the attribute. You can use your own colors in this case I played with
[1:23] the presets and customized it. Now I needed to create this wire effect to add some details to the


### Wire Effect [1:29]
**Transcript (timestamped):**
[1:32] model so since we have the attribute we can just use group from attribute boundary node to select
[1:39] the boundaries. Later we can use this edge selection to create the wire effect.
[1:47] Another problem I had was on how to place this circle on the edges of the wires.
[1:52] In here I'm creating the wires and also grouping the bottom points.
[2:00] Then in a wrangle targeting that group I can measure the distance from the center to the position
[2:06] of those points and finally feed that value to the circle scale.


### Basket Effect [2:11]
**Transcript (timestamped):**
[2:11] In this one I needed to do the exalternating effect to create the baskets so I'm using the
[2:17] sweep node set to rows to create the horizontal lines. Then a similar approach to the one on
[2:23] the procedural basket tutorial by calculating the normals with the oriental long curve.
[2:29] Next I am grouping every other shape with the module and promoting it to points.


### Final Result [2:36]
**Transcript (timestamped):**
[2:36] Now if I look at the final result you can see that we do have the waving effect but it's not
[2:42] alternating. For that I am targeting the group I created in a sort node and shifting the point
[2:48] order by one. And that's how I solved that problem. Now this one got me thinking I wanted to
[2:56] replace this initial simple object with a simulated one as you can see here. The problem is that


### Orient Attributes [3:02]
**Transcript (timestamped):**
[3:03] can be tricky to get oriental reboots but in this case I had some out from swalch
[3:09] in the CG Wiki Discord that told me that I could simply use the oriental long curve
[3:15] to extract the N and the app, promote it to primitive attributes since we're going to extract
[3:21] the centroid to copy to points. You can also measure the perimeter as p-scale to extract the
[3:27] scaling factor. So this final tip is on how to create these connecting pipes from separate models.
[3:37] So having this curve from the engine I can measure the curvature and group the points with a certain
[3:44] curvature and from there isolate them and fuse it. And since I'm going to connect these ones to
[3:52] other stream that has four points I am replicating the points to have the same amount.
[3:59] Finally adding a attribute to it stream and connect them with an add node set by attribute.
[4:04] And that's all I have for today let me know in the comments if you learned something new


### Outro [4:05]
**Transcript (timestamped):**
[4:09] and if we don't talk till next year happy holidays and big thanks to all my Patreon supporters too.
[4:16] Thank you, see you around.



---

## Captured Frames

- [0:10] tutorials/frames/procedural-problem-solving-in-houdini/frame_000.jpg
- [0:40] tutorials/frames/procedural-problem-solving-in-houdini/frame_001.jpg
- [1:05] tutorials/frames/procedural-problem-solving-in-houdini/frame_002.jpg
- [1:30] tutorials/frames/procedural-problem-solving-in-houdini/frame_003.jpg
- [2:00] tutorials/frames/procedural-problem-solving-in-houdini/frame_004.jpg
- [2:30] tutorials/frames/procedural-problem-solving-in-houdini/frame_005.jpg
- [3:00] tutorials/frames/procedural-problem-solving-in-houdini/frame_006.jpg
- [3:40] tutorials/frames/procedural-problem-solving-in-houdini/frame_007.jpg
- [4:15] tutorials/frames/procedural-problem-solving-in-houdini/frame_008.jpg

---

## Structured Notes

### Core Technique
Seven quick procedural-problem-solving tips applied to a hot-air-balloon model: multi-boundary separation via "create boundary groups," a per-section-connectivity + iteration-modulo color-repeat pattern for the balloon panels, a wire/basket weave reused from a prior wicker-basket tutorial, an Orient-Along-Curve-derived instancing trick for a simulated-object replacement, and a curvature-based approach for joining separate pipe models.

### Summary
To manipulate multiple mesh boundaries independently (e.g. isolating just the top rim of the balloon), Group by unshared edges in points mode with **"create boundary groups"** enabled automatically creates a separate group per boundary loop. For the balloon's colored panel pattern, each gore/section gets a Connectivity ID, then a for-each loop over each piece runs a wrangle creating a repeating value pattern via **modulo combined with the loop's iteration value**, offsetting colors between adjacent gores; the first and second gores get manually forced values to match the reference photo, then the resulting attribute is remapped to specific chosen colors (with a computed maximum for correct range normalization). A wire/rope decoration reuses the group-from-attribute-boundary technique to select boundary edges for the wire pass; a related problem — placing a circle exactly on each wire's edge endpoint — is solved in a wrangle by measuring the distance from center to the point's position and feeding that value directly into the circle's scale parameter. The basket's alternating over-under "weave" is built with a Sweep set to Rows for horizontal lines, using the same Orient-Along-Curve normal-calculation approach as the studio's dedicated basket tutorial, then grouping every-other shape via modulo and promoting to points. To fix the weave not alternating correctly (all waves going the same direction instead of alternating), a Sort node targeting the saved group **shifts the point order by one**, flipping every other row's phase. For replacing a simple placeholder object with a fully simulated one while keeping correct orientation, Orient Along Curve is used to extract the **N** and **up** attributes (a tip from "swalch" on the CGWiki Discord), promoted to primitive attributes so the centroid can be extracted and used for Copy to Points, with perimeter optionally measured as a p-scale scaling factor. Finally, for joining pipes/tubes from separate models, curvature is measured along the connecting curve and points above a curvature threshold are grouped, isolated, and fused; since the two streams being joined have differing point counts, points are replicated to match, an attribute added to identify the stream, and an **Add node set by attribute** connects matching points into new primitives (bridging the gap cleanly).

### Key Steps
1. **Multiple boundary separation**: Group by unshared edges (points mode) with **"create boundary groups"** enabled — automatically creates a distinct group per boundary loop (e.g. two groups for two rim edges), then promote to edges/primitives for downstream operations like closing one boundary but not the other.
2. **Repeating color pattern**: give each panel/gore a **Connectivity** ID; iterate over each piece in a for-each loop, using a wrangle to create a repeating value via **modulo combined with the iteration value**, offsetting colors between neighbors; manually override the first and second gore's values to match a specific reference look.
3. Remap the resulting attribute to chosen colors, computing a **maximum** of the attribute first so the remap range normalizes correctly regardless of gore count.
4. **Wire effect**: since the pattern attribute already exists, use **Group from Attribute Boundary** to select the boundaries, then use that edge selection to build the wire geometry.
5. **Circle-on-wire-endpoint placement**: create the wires and group the bottom/end points; in a wrangle targeting that group, measure the distance from the center to each point's position, and feed that value directly into the circle node's **scale** parameter so each circle matches its wire's endpoint radius.
6. **Basket weave (alternating)**: use a Sweep set to **Rows** for the horizontal lines; calculate orientation with **Orient Along Curve** (same approach as the dedicated basket tutorial); group every-other shape via **modulo** and promote to points.
7. **Fixing non-alternating weave**: since the initial result waves but doesn't alternate direction between rows, target the saved group in a **Sort** node and **shift the point order by one**, flipping the phase so adjacent rows alternate correctly.
8. **Simulated-object replacement with correct orientation**: use **Orient Along Curve** to extract the **N** and **up** attributes (credit: swalch, CGWiki Discord), promote them to primitive attributes, extract the centroid, and Copy to Points; optionally measure the perimeter as a **p-scale** scaling factor.
9. **Connecting pipes from separate models**: measure **curvature** on the connecting curve, group points above a chosen curvature threshold, isolate and Fuse them.
10. Since the two geometry streams being connected have differing point counts, **replicate points** on the smaller stream to match, add a stream-identifying attribute to both, and use an **Add node set by attribute** to connect matching points into new bridging primitives.

### Houdini Nodes / VEX / Settings
Group (unshared edges, points mode, "create boundary groups"), Connectivity, For-Each loop (per-piece iteration), Attribute Wrangle (modulo + iteration-value repeating pattern), Remap (with computed attribute maximum), Group from Attribute Boundary, distance-to-scale wrangle (circle scale from point-to-center distance), Sweep (Rows surface type), Orient Along Curve (N/up extraction), Sort (point-order shift for weave alternation), Attribute Promote (primitive N/up), Extract Centroid, Copy to Points, Measure (perimeter → p-scale), Measure (curvature), Group (curvature threshold), Fuse, point replication (matching stream point counts), Add (set by attribute — stream-matched bridging).

### Difficulty
Intermediate (each tip is a compact, standalone technique reused from or feeding into other tutorials in the same channel).

### Houdini Version
20.5.311 (visible in viewport title bar).

### Tags
groups, vex, boundary-groups, orient-along-curve, connectivity, hot-air-balloon, procedural-modeling

---

## Related Tutorials
- [Procedural Wicker Basket in Houdini](procedural-wicker-basket-in-houdini.md) — source of the alternating-weave Sweep/Orient-Along-Curve technique reused (and fixed) in this video.
- [Groups, Patterns in Houdini](groups-patterns-in-houdini.md) — deeper dive into boundary-group and other group-selection patterns used throughout this video.
- [Procedural Favela in Houdini | Tips and Tricks](procedural-favela-in-houdini-tips-and-tricks.md) — shares the vertex-modulo alternating-edge-selection trick used here for another architectural build.

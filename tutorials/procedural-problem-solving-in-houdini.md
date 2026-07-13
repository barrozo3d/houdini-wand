---
title: Procedural Problem Solving in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=5Cv1SJRm538
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-problem-solving-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Procedural Problem Solving in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=5Cv1SJRm538)
**Author:** cgside
**Duration:** 4m26s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-problem-solving-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Houdini Nodes / VEX / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Houdini Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]

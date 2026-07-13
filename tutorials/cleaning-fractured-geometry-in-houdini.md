---
title: Cleaning fractured geometry in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=n-UAPewvMgQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/cleaning-fractured-geometry-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Cleaning fractured geometry in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=n-UAPewvMgQ)
**Author:** cgside
**Duration:** 4m10s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py cleaning-fractured-geometry-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back! So in this video I wanted to share with you a
[0:04] simple way to clean geometry that looks like this that you can see here and we
[0:12] end up with something like this which is way more clean. So we have all these
[0:21] inside geometry that we need to clean. So let's go from the beginning I'm
[0:31] creating a few blanks wood planks then I'm iterating and creating a
[0:37] fracture and removing some of the middle parts with the bound. So we end up with
[0:45] something like this after the blast. You can take a look at the file on my
[0:52] patron I will be uploading it there and from here we can unpack and we get
[1:02] this. So we can now blast away in this case the wood grain outside. We can keep
[1:14] the wood grain outside as the base then we can fuse the points and dissolve the
[1:22] flat edges. This will get rid of all those edges that we have quite a fault and as
[1:31] you can see inside there is no geometry which is good and in the other branch we
[1:40] need these end pieces. So we need both parts the one that we will keep and the
[1:50] one that is going to be removed. So we can get only this geometry that we can
[1:57] really get from the groups of the fracture. So let's keep the inside here and
[2:06] do the same in here. Then in a wrangle we are setting these variable
[2:15] founds that will search the near points with a very small radius and if
[2:22] didn't find any near points between the two geometries it will remove the
[2:27] points from the first inputs. So that's why we are using actually two
[2:36] inputs. One is used here the input one and the other one which is the main is
[2:45] where we remove the points. So a very simple wax code that will give us this
[2:55] resulting geometry. Then we have some floating edges and we can just use a
[3:03] clean with the fault settings and then we can merge it over the other parts
[3:13] fuse the points and soften the normals and from this to this. So that's
[3:25] basically what I wanted to share with you guys. Just quickly I wanted to let you
[3:31] know that I just released a course called Church Ruins. It's available on the
[3:37] My Patreon shop and it's a download downloadable file. Contains about nine hours
[3:44] of video contents fully step by step and narrate it. If you guys are interested
[3:51] add over to my Patreon shop and you can find it there. So that's basically it. Let
[3:58] me know in the comments if you have another approach to this kind of issue and
[4:03] if this helped you in any way. Thank you and see you in the next one.



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

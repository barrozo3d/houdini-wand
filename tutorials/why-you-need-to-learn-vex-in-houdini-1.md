---
title: Why you need to learn vex in Houdini #1
source: YouTube
url: https://www.youtube.com/watch?v=ntf3zMAez50
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/why-you-need-to-learn-vex-in-houdini-1/
frame_count: 0
frame_status: pending-selection
---

# Why you need to learn vex in Houdini #1

**Source:** [YouTube](https://www.youtube.com/watch?v=ntf3zMAez50)
**Author:** cgside
**Duration:** 5m11s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py why-you-need-to-learn-vex-in-houdini-1 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, in this quick video I wanted to show you how you can create a
[0:03] cross-a interior like this one you see in here. So I covered before how I created
[0:08] the cross-a just with a bunch of exclusions and a sculpt node and then we move
[0:13] into the interior which is the trickiest part. So I start with the sliced
[0:19] cross-a then blast the field polygons and since this is a simple surface we
[0:24] can actually re-sample it. From there I want to transform a spiral into the
[0:29] cross-a interior shape. So I start by having a rest geometry for the spiral
[0:34] which is this unit circle which takes advantage of the sample circle uniform
[0:38] by manipulating the U value that you feed into the function. You can create a
[0:42] circle from the initial cross-a shape and I make sure that they have the same
[0:47] size, the initial surface as the same size of the circle. So I just scale it to
[0:52] fit with a match size and then we take the spiral, the rest geometry which is
[0:56] the unit circle and the forming geometry and we use the surface deform to
[1:01] deform the spiral to this shape. I scale it a bit with a primitive then re-sample
[1:05] it with subdivision curves to smooth it out. Create an oriental long curve with
[1:10] some normals which is basically the tangent along the shape or the curve.
[1:15] This is just a single curve as you can see. Then it starts the clustering. So I
[1:20] first initialize the cluster to minus one because later I will need this
[1:24] value to be negative. Then in here I create some random clusters just a single
[1:31] point with this wrangle. So each random point in here has a different cluster
[1:35] and they are not uniform or linear. They are at random positions and the way I
[1:40] do that is by rating over numbers, setting the number of clusters I want. In
[1:45] this case 128. Then I create like a U value from 0 to 1 based on the iterations.
[1:50] So just like a curve view it's a value from 0 to 1. Then I assign a random
[1:54] position and the random value is based on each iteration. Make sure it's
[2:00] zero centred so between minus one and one and then I just scale it with an
[2:04] amplitude slider with a multiplier that I set really low. Then I make sure I
[2:09] exclude the first and end point and position which will be a value of 0 or 1
[2:15] and I start at the linear value U and add the random position so they are not
[2:21] linear. Then I read that position on the curve using cream UV and the U value
[2:26] and find a nearest point because we can't map it directly to a point. So I find
[2:31] a nearest point and just assign that cluster to root. So if you can see we have
[2:35] different clusters on random points. It's still a bit linear but we are adding
[2:39] that random offset. I also assign a group as you can see to where those
[2:43] clusters are and that will come in and later. Then in here I need to flood
[2:47] fill the selection so I need to fill the random clusters. So what I do is in a
[2:53] detail I grab all the points on the curve so a selection of all the points in
[2:57] the curve and initialize the variable to grab the current cluster so we can
[3:01] flood fill it. Then I will the points in order. So cluster is also ordered by
[3:06] default because the work we've done before. Grab the current cluster value so
[3:10] let's say 0, 1, 2, 3 and make sure when we when we are iterating over the
[3:16] points that we carry forward the last ID until we find a new one. Since the
[3:20] values in between will be minus 1, these max operation will make sure that we
[3:24] fill those values with the last value grab. Then we just update the point at
[3:29] root cluster and we get the flood fill and why we are doing this? Well it will
[3:33] make sense in a bit. So in here I have also an open-shell version but you can
[3:37] ignore this because it's lower. Then I copy a new curve so now we have two
[3:42] curves on top of each other. We have set it from one another so just by grabbing
[3:46] the just by creating a normal attribute that is pointing out and we grab the
[3:53] current normal which is that tangent U that we add that I call it normal and we
[3:58] cross-product with a vector along the Z axis so pointing to us and that will
[4:03] create an out vector that we can use to offset the curves. So just that we
[4:08] can offset a bit more or less and we get that result. Then we the here the
[4:13] trick we fills the points based on that near point group that we add as you
[4:18] can see but we if we don't we do that by default this won't work we need to
[4:22] match the attribute by the cluster so they don't go on top of each other and
[4:26] we get the beginnings of our effect. Then I just polypate to unite the curves
[4:31] and then in a feedback loop so fetch feedback and by count I just resample just
[4:36] like in a sub-solver but in this case we are using a feedback loop and then I
[4:40] attribute to our just one iteration and we get this sort of result. Fuse, polypate
[4:44] and that's basically it. Of course we can iterate more or less but you can see
[4:50] the iterations going over our geometry we can go a bit more if you need it but
[4:55] the attend iterations in here will work fine. As always you can grab the file on
[4:59] my patreon alongside with the with the cross-site and everything and the
[5:03] final effect. Then for mashing this it's a project for another time. I hope you
[5:08] enjoyed. Thank you. See you next time.



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

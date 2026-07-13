---
title: Houdini Tips | Expressions, VEX, Recursive Cuts and more
source: YouTube
url: https://www.youtube.com/watch?v=2Vw6jvHrnBw
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-tips-expressions-vex-recursive-cuts-and-more/
frame_count: 0
frame_status: pending-selection
---

# Houdini Tips | Expressions, VEX, Recursive Cuts and more

**Source:** [YouTube](https://www.youtube.com/watch?v=2Vw6jvHrnBw)
**Author:** cgside
**Duration:** 11m35s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-tips-expressions-vex-recursive-cuts-and-more <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### nprimsgroup Expression [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'll share a few tips and tricks
[0:05] that are not so obvious let's say that I would like to share with you. So the
[0:13] first issue I have in this particular object is that in this extrude side, this
[0:21] part here I have a big chunk of UVs like this a big strip and I would like to
[0:30] divide it into sections. So instead of splitting the geometry and the UV separately
[0:40] we can do the following. We can take a group range and target as a base group
[0:51] that particular those particular polygons and then we can select let's say two
[0:59] out of N-prims and divided by five let's say and as you can see the N-prims in
[1:09] here if I just say N-prims is taking all the prims from the object and not the
[1:18] prims on this base group. So if you want to target that base group you want to
[1:25] use another expression which is N-prims group and say zero and the group is
[1:34] extrude side and then now it's targeting those that particular group and we
[1:45] can divide it by five and we get this pattern. So this is quite useful because we
[1:53] can as you can see I have the same in here then I can promote it to edges group
[1:59] expanded and we have the seams that we can fit to a UV flatten and rectify it and
[2:08] then we end up with the UVs like this as you can see which is much cleaner.


### Recursive Cuts [2:19]
**Transcript (timestamped):**
[2:19] So for this one I would like to show you how I did this let's call it recursive
[2:27] cuts that I did with clip node. So let's go through the setup. I have here a simple
[2:36] example that I will be sharing on Patreon along with other example files that
[2:42] you will see in this video. So as you can see I have the amount of iterations and
[2:49] a seed and more or less mimics the same behavior of this one in here. So this is
[3:02] actually pretty simple. I have an initial mesh which is just one single
[3:10] primitive and then in here I am creating a forage loop by using fetch feedback
[3:25] and by count so you can pick the amount of subdivisions you will have and I'm
[3:34] starting by measuring the area and promoting it to a max area so I can check
[3:42] the largest primitive then I'm grouping that largest primitive then in here I'm
[3:49] scattering a point somewhere in the middle of the largest primitive and I'm also
[3:58] randomizing the normals so I can have a random direction just by setting it to
[4:07] inside sphere and randomizing the normal and using the iteration as a seed as a
[4:16] global seed plus a seed that I have defined in this null and then in the clip
[4:24] nodes which is where everything happens I am clipping and setting the origin to
[4:33] the position of that specific point as you can see this point is in here this
[4:39] scatter point and so I'm using the position position x, y and z and in the direction
[4:50] I'm using the normals as you can see normal x, y and z and this happens for an x
[4:58] amount of times and you always get this look of recursive subdivision let's say or
[5:07] recursive clip so it's actually pretty simple but that is not so obvious out of
[5:15] the box let's say so yeah that's how I did that and at the end I got something
[5:25] like this so as you can see in here I have these curves and I'm doing a polybridge and


### Delete curves with vex (prim intrinsic) [5:29]
**Transcript (timestamped):**
[5:39] I'm left with these with the curves along the geometry and I would like to remove it so
[5:45] I can remove it with a blast and blast just primitive 0 and 1 but that might not be
[5:54] always the case and I can always group them so I am grouping in here so I'm
[6:04] grouping the curves in here I just have one but then when I copy they will be in the
[6:10] same group as you can see curves and I can just blast the curves after the bridge but
[6:19] sometimes you might not have that luxury so what we can see in here in the polybridge if we
[6:27] go to the attributes or the geometry spreadsheet and go to primitives and select in trains x and close
[6:36] you can see the primitive 0 and 1 which are the curves have an open attribute let's say or in
[6:46] the closed is set to 0 so what we can do is an attribute wrangle remove those curves by using
[6:54] this if premium trains it closed premium number is equal to 0 we can remove those frames so that's
[7:04] how you can remove leftover curves from the geometry and this particular suggestion came from
[7:14] Fanoliz on discord so thank you a lot for that okay for this particular digital asset which is


### Res expression from cops [7:18]
**Transcript (timestamped):**
[7:23] pretty simple just takes an image and resizes a plane to fit the same resolution while keeping it
[7:32] in the 0 to 1 range so this is actually the way I'm doing this is pretty simple basically I'm
[7:43] reading an image in a copnet then in the grid I am taking as the x size the res which is the
[7:55] resolution of the the copnet and taking the x resolution so the width and multiplied by 1
[8:07] divided by the x resolution so the the the second part just helps helps me to keep the ratio
[8:16] of 0 to 1 and then for the y is just the same thing but in this case the y-rays and multiply
[8:26] by 1 divided by the x resolution or the width so the height and width and this way we can get the
[8:35] same ratio of an image taken from the copnet you only can you only can do it through a copnet
[8:46] so to to read the resolution you can't really read it in a UV quickshade or attribute from Mac
[8:55] so yeah so in here I'm creating this pillow effect and for that I am welding two pieces of clothes


### Class attribute in vellum ballon setup [8:56]
**Transcript (timestamped):**
[9:07] that are almost touching each other they are actually touching on the unshared edges so I'm welding
[9:17] those unshared edges as you can see I'm shared back and I'm shared front and I'm configuring
[9:28] I am using a configure balloon in the first place but if I set it to the default settings which is
[9:37] from connectivity and I test it now you can see the result is quite different it goes all over
[9:50] the place and even can rush your audience session so let's just wait another frame and as you can
[9:59] see this is all messed up let me cancel this and the reason is when you have two pieces of clothes
[10:12] and they are not in the origin this can cause you a lot of issues so what you can do is say
[10:22] Odini that these two pieces of clothes are part of the same the same piece let's say so what you can
[10:32] do is just use an i-at class equals to one just say that they have the same class as you can see
[10:41] instead of two and in the valum pressure just set when you say define pieces instead of from
[10:51] connectivity just use from attributes and specify the class attribute and then when you assimilate it
[11:01] you will have more predictable results as you can see it's not exploding all over the place like
[11:10] before so yeah guys that's basically what I wanted to share today hopefully you picked up a few tips
[11:20] don't forget you can always grab sample files from my patreon along with exclusive tutorials and
[11:30] yeah see you next time thank you



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

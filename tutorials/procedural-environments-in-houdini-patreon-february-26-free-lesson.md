---
title: Procedural Environments in Houdini | Patreon February '26 Free Lesson
source: YouTube
url: https://www.youtube.com/watch?v=F_xggmIONZ4
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-environments-in-houdini-patreon-february-26-free-lesson/
frame_count: 0
frame_status: pending-selection
---

# Procedural Environments in Houdini | Patreon February '26 Free Lesson

**Source:** [YouTube](https://www.youtube.com/watch?v=F_xggmIONZ4)
**Author:** cgside
**Duration:** 9m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-environments-in-houdini-patreon-february-26-free-lesson <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So this month on Patreon we will be creating this small
[0:04] environment from scratch. Today we will focus on creating this window with
[0:09] broken glass and broken cloth or whatever material that is. And later on we will
[0:15] be moving into creating the brick wall using cups. So all done
[0:21] procedurally. And let's see if in the next month we can probably texture this.
[0:26] So yeah let's get into it. Okay guys now let's move on by creating some
[0:32] damage here some ripping effect on the sides of this asset. So for that I'm
[0:38] gonna use cups so let's create a cup net. And the idea is to create a mask on
[0:47] the side so we can later load it in our mesh. So for that we will use a bit of
[0:55] openCL usually I delete this default code and binding but we can actually use
[1:00] this source and destination as this will be really simple. So there's one thing
[1:05] I want to do is to create a parameter so I'm gonna bind a palm called edge
[1:09] make it optional and make it a float. So I'm gonna create this and what we will
[1:18] do is to create in here an edge parameter based on our X resolution so we
[1:27] want to do it along the X of float E just a variable and we will do at edge
[1:33] multiply by at X rest. So the X resolution and then we will create the
[1:40] mask so floats mask will be while the pixels along the X is less than
[1:48] the edge so let's actually see that if we set this to mask mask and we create
[1:58] this as you can see we are growing a mask from the left side and now we need to
[2:02] do it for the right side also. So let's do or at IX is bigger than the
[2:11] current resolution around the X the X minus the edge and now we should have a
[2:18] mask on both sides but also going to create some noise because we don't have
[2:24] these straight lines so for that I'm gonna create a fractal noise gonna set
[2:30] these to work with a cell or F2F1 gonna change probably the amplitude and also
[2:38] the center to be around this value then I'm gonna offset this
[2:47] something like this change the element size let's say 2.4 and also reduce a bit
[2:53] the roughness so we get something like this and now we connect it in here and
[3:00] we just need to apply it to the edge so we can come in here and between brackets
[3:08] between parentheses we will just add the source oops okay we need to set the
[3:19] source as load and now it works and I'm gonna play in here with the edge size
[3:27] to about 0 to 2 something like this we can play with the offset and yes
[3:35] something like this should work I think and now let's just create a null and
[3:42] name it mask and now we can load it in our mesh so if we come in here and we
[3:51] have the UVs and the UVs are like this so we can easily do a natural from
[3:56] map I'm gonna set it let me see which namely that bit so in this case I'm just
[4:04] gonna call it mask not to the CD so let's see it and we don't want the
[4:12] vector want the float and let's load in here with the obvious syntax and load it
[4:18] we get something like this so not ideal just gonna make sure I set in here the
[4:30] scale to 10 to be more to have these kind of thresholds and maybe I can just
[4:40] play in here with the offset of the noise
[4:46] something like this let's write maybe decrease the intensity and play with the
[5:04] edge something along those lines and now we can just don't visualize it and just
[5:13] do a clip using the mask and a value of 0.1 and we want the other way around
[5:22] maybe this is a bit too much so I'm just going to go in here and play with this
[5:34] and maybe with the noise so yeah I guess something like this will work maybe
[5:44] increase this a bit you know you can play with it I'm just gonna leave it like
[5:54] this maybe increase decrease this a bit yeah something like this will work now
[6:01] we want to do a net smooth and this is a life's node so let's do a net smooth
[6:10] life's edge smooth and let's set it to 99 and four and we want to include the
[6:18] unshared edges and don't show guide so we get this kind of result maybe decrease
[6:26] it a bit something like this and now let's continue by object merging the
[6:38] wolf or the window army and we will just do a match size and set these to
[6:54] none none and mean and the value of 0.1 so let's see that is working yes
[7:02] more or less so there will be some intersection in here but it doesn't matter so
[7:08] now we will divide the mesh into wads so divide this mesh we don't want convex
[7:21] polyons we want to break it and in this case I want it I want to have the squared
[7:29] resolution so I'm gonna create in here a parameter so of loads and call it density
[7:39] I think I've shared this technique before basically we will take the pounding box 0
[7:46] the x size and we will divide it by the number of divisions we want but in this case we want to
[7:58] have both x and y connected so if we do this and come in here and say y size as you can see we
[8:07] need a different resolution that's why we will use this density so I'm gonna set it to 1 and what
[8:12] we can do in here since we need an old number we will divide it by the seal of these pounding box
[8:20] multiply it by the density and now we take these and place it in here and just change it to y
[8:35] and as you can see we will get only this squared resolution I think I'm just gonna leave it
[8:40] default to 1 so we don't really need that to do this but it's just a circle thing to know
[8:46] so I'm gonna attribute the late and clean some of these attributes well I don't have any
[8:56] attribute in here so I guess I don't need to clean anything so it can keep this one now we're
[9:03] gonna do a polyx route and in here we're just going to insert these a bit so point of 32
[9:14] and we will do it based on the individual elements and as you can see we can create this
[9:25] sort of window in here so what we can do is just split by the extrude front and we can also
[9:36] invert the selection so let's create a knot this will be the frame and this will be the windows
[9:43] that were going to break all right let's continue on the next



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

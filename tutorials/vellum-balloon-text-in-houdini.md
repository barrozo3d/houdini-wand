---
title: Vellum Balloon Text in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=T-_L6BeLSkg
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vellum-balloon-text-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Vellum Balloon Text in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=T-_L6BeLSkg)
**Author:** cgside
**Duration:** 9m43s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vellum-balloon-text-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm going to show you step by step how you can create this
[0:07] balloon text effect using Odini and Valon. So let's get into it. So with a fresh Odini scene let's start by dropping the geometry container and


### Tutorial [0:14]
**Transcript (timestamped):**
[0:21] font
[0:24] and
[0:26] I'm gonna write cgs for cg sites
[0:30] and
[0:31] I'm gonna pick a different font
[0:35] that has some rounded corners. So let me pick the font.
[0:43] So this is the font I'm going to use. It is a bit more rounded and it will work better for the effect.
[0:53] So let's extrude it.
[1:00] And we will extrude about 0.2
[1:06] and I'll put the back.
[1:09] Then I'm gonna create a VDB from polygons so we can round it
[1:16] because right now it's just too sharp. We can bevel it but
[1:22] it will work better with a VDB conversion. VDB from polygons.
[1:30] And let's say 0.01
[1:36] and now we will smooth it out.
[1:41] So let's first convert VDB to polygons so we can check the final result.
[1:50] So as you can see it's not looking great.
[1:54] Let's
[1:56] smooth as the F.
[2:01] And now it's looking better. Let's say we want 10
[2:07] and after the smooth I also want to erode it. So let's put on a Rishabes.
[2:18] And let's erode it by
[2:25] something like this should be fine. So we're going from this to this.
[2:34] And now this geometry is not the best for simulation. Let me just save this quickly.
[2:43] So as I was saying this geometry is not ideal.
[2:46] So we will remesh
[2:53] and let me check the amount of remesh I used. So 0.0075
[3:06] this should give us enough resolution.
[3:11] And now we can start our valum simulation.
[3:16] So let's just organize this and put down a valum configuration balloon.
[3:24] This will create the valum plot and the pressure constraint.
[3:31] And let's create a valum solver.
[3:39] And if you hold down j you can drag and connect everything.
[3:47] Now just wait a bit.
[3:52] And let's check the result.
[3:57] And this will fall down. We will need to remove the gravity.
[4:04] So let's remove the gravity.
[4:07] And we will need to set up some things in here.
[4:17] So to start with let's go to our valum plot.
[4:22] And
[4:27] what we need to do
[4:29] is to play with the wrestling scale of the stretch.
[4:38] So in this case I use 0.1.
[4:42] 1.18
[4:46] and let's see what that gives us.
[4:51] Nothing too much.
[4:53] And we will also increase the stretch to 10,000.
[5:08] And while we're here let's decrease the band stiffness to 0.01.
[5:18] Let's see what that gives us.
[5:23] That is giving us these results which is a bit too much.
[5:30] And not very controlled.
[5:32] So what we can do is to play with the valum pressure.
[5:38] So let's go to the valum pressure.
[5:40] And we can say the wrestling scale let's try 50.
[5:49] And we will just use one frame.
[5:52] So we could actually use just this frame, the previous one.
[5:59] So as you can see we already have the effect.
[6:03] This one is a bit too much in my opinion so we can use this one.
[6:10] So you can see it's creating some nice wrinkles in here and here.
[6:16] So I think I'm gonna use this one.
[6:22] Now let's create a valumio.
[6:25] So just to bake the result and we will remove time dependent cats,
[6:33] cache and just save to this.
[6:37] Now we can just have it the frame freeze.
[6:44] So let's create a no just for demonstration purpose.
[6:50] I'm gonna render this out.
[6:55] So we can go to some areas.


### Render [6:58]
**Transcript (timestamped):**
[7:00] And it's top import.
[7:04] And let's import geometry.
[7:08] Let's set it like this.
[7:15] And let's create a material library.
[7:23] And inside let's do a calendar material builder.
[7:29] Let's sort of view and assign to everything.
[7:33] Now we can create a dome light.
[7:35] And let's say it's a let alone.
[7:37] I'm gonna use Christmas photo studio from HDI Heaven or Polyaven.
[7:43] I mean, and let's create the camera settings.
[7:49] Let's change it to exp you.
[7:51] Give it some quality.
[7:53] And let's create a camera settings.
[7:55] Let's change it to exp you.
[7:57] Give it some quality.
[7:59] Let's change it to exp you.
[8:01] Let's create some quality.
[8:08] And the camera freeze the diffuse limits.
[8:12] Reflections and refractions is fine.
[8:18] Let's test these out.
[8:20] Camera exp you.
[8:25] And let's get rid of the background.
[8:28] So display environment lights as backgrounds turned off.
[8:34] Let's change it to dark.
[8:37] Let's go to render and save viewport size.
[8:44] That way if we have a camera we won't render the full resolution,
[8:48] but just the portion of the viewport.
[8:52] So but in this case I'm not even going to bother creating a camera.
[8:58] I'm just gonna do a simple material.
[9:02] So let's change this to some RNG.
[9:10] And increase the metowness.
[9:15] And increase the bit the roughness.
[9:19] So yeah guys it's basically it's nothing to complex.
[9:24] As you can see it's just really easy to set up.
[9:29] And I hope you have learned something new.
[9:32] Let me know in the comments.
[9:35] And I'll see you soon.
[9:37] Thank you.



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

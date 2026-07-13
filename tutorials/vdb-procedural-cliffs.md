---
title: VDB Procedural Cliffs
source: YouTube
url: https://www.youtube.com/watch?v=fBhtlmCGrK4
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vdb-procedural-cliffs/
frame_count: 0
frame_status: pending-selection
---

# VDB Procedural Cliffs

**Source:** [YouTube](https://www.youtube.com/watch?v=fBhtlmCGrK4)
**Author:** cgside
**Duration:** 5m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vdb-procedural-cliffs <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in this video I'm going to show you how to create rocks or cliffs with VBD noises,
[0:09] then walk you through the Solaris setup.
[0:13] This is just an example of the kind of details you can create for rocks or cliffs.
[0:18] I just did this simple example.
[0:22] I started with a box and did some very basic sub-apparations like extruding and bambling,
[0:29] then added a mountain at the end to distort a bit the shape.
[0:34] After that I converted it to VDB and all the cool stuff happens at the volume drop.
[0:41] In the VBD from Polygons it's recommended you change the attribute to density instead
[0:46] of the default surface, it will make our life easier.
[0:51] And of course set the desired resolution, this can get pretty slow so for now let's
[0:56] work with a low rise version.
[0:59] So the volume pop looks like it's pretty confusing if you're a beginner, but it's actually
[1:06] repeating the same stuff over and over.
[1:10] The basic idea is to distort the shape with noises and sometimes add another noises
[1:16] to distort the main noises.
[1:19] Let's start with the first noise which is just displacing the shape overall.
[1:24] So we take the position from the inputs and we feed it to a unified noise.
[1:30] I only experimented with the noise type and changed the frequency or repetition of the
[1:37] noise.
[1:38] Then as mentioned before I am using another noise to distort the main pattern which by default
[1:44] is pretty rigid.
[1:46] Basically taking a noise, manipulating the values with the feed range and adding it to
[1:52] the position inputs.
[1:56] At the end there's just a multiply by constant to control the amount of displacement.
[2:05] So in this second layer of detail I am creating this pattern with a Manhattan cellular and increasing
[2:12] the mean value of the original range quite a bit to add some contrast to the effect.
[2:20] Then again distorting the noise with another one.
[2:32] There's nothing new going on in this third layer, just a different noise and frequency,
[2:37] playing with the values of the feed range.
[2:47] For the last pattern I am creating this cuts in the volume mostly by manipulating the frequency
[2:53] of the noise in one of the axis.
[2:56] Also rotating the pattern in X.
[3:00] And using again the unified noise which being slower than the let's say the turbulence,
[3:07] it has more variety of noises.
[3:10] And yeah this is just an example of what you can create, you can change the source shape
[3:15] and manipulate the noises in different ways to have a completely different output.
[3:21] After converting it to polygons I am creating a mask to scatter some trees.
[3:27] Basically taking the white components of the normal attributes and feeding it to a ramp.
[3:34] Finally just use a bind export to create the attribute.
[3:39] So quickly going through the cellarysetup.
[3:43] I am importing the mesh and applying a material with the trap liner nodes.
[3:50] I am also using a bit of displacement and auto-bam to add some details.
[3:55] Then adding some fog, layering some noises as covered in the 3D environment tutorial.
[4:03] And as far as I know you need to export it as a VLV and import it in a volume node to
[4:10] render in our node.
[4:12] For the trees I used the component geometry to import the different assets using the geometry
[4:19] variant setup as shown in previous videos.
[4:24] Feeding the assets into the instacer and inside I am scaling some points.
[4:31] Using the orientation and scale and using the mask or attribute created before on this
[4:37] pattern node.
[4:38] Finally adding a light, a camera and that's about it.
[4:44] And this was my final result as you can see we can create some nice details on the mesh
[4:49] just by using VDVs.
[4:53] In case you want the file I will upload it to my Patreon and also check out my gamroad
[4:58] where you can find many free tools and an environment tutorial.
[5:04] Thank you and see you in the next one.



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

---
title: Procedural Shading Tips #2 in Houdini 20
source: YouTube
url: https://www.youtube.com/watch?v=r2SSCwpgnVQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-shading-tips-2-in-houdini-20/
frame_count: 0
frame_status: pending-selection
---

# Procedural Shading Tips #2 in Houdini 20

**Source:** [YouTube](https://www.youtube.com/watch?v=r2SSCwpgnVQ)
**Author:** cgside
**Duration:** 4m15s | 9 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-shading-tips-2-in-houdini-20 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello and welcome back. So in this video I'm sharing a few tips on procedural shading in Odin
[0:05] 20. All the techniques shown here can be found as sample files on my Patreon. The first one is


### Assigning random textures [0:11]
**Transcript (timestamped):**
[0:12] on out to assign random textures to the different apartments in the Islam-like building. As you can see
[0:19] I already have a unique attribute for each apartment, but I just want to use three different textures
[0:25] so I need to divide it randomly as seen in this render. The first step is to promote the
[0:30] attribute to detail, set to maximum, this way I have the amount of iterations I need.
[0:37] Then in the wrangle I am running over numbers and the count will be the detail attribute we just
[0:43] created. Then I am saving the primitive numbers with the respective attribute using the find attribute
[0:50] value function. And for each one assigning a random value between 0 and 2 in this case,
[0:56] so three variations to what cast a attribute named Outstexture. And you can easily change the
[1:03] amount of variations and the seed. Now in Solaris I have three different textures to be assigned


### Assigning different textures [1:07]
**Transcript (timestamped):**
[1:10] to the walls. And using a material like switch node I can feed the attribute to the
[1:16] which input to assign the different textures based on the attribute.


### Assigning different room textures [1:22]
**Transcript (timestamped):**
[1:22] So now we can use a similar logic to assign a different room texture to which window interior
[1:28] geometry. As you can see I am assigning a room map frame, just default settings,
[1:33] and in this wrangle running over each frame assigning a random integer value between 0 and 2.
[1:39] In this case I only have three textures to use as an interior. In Solaris you can see that I


### Loading different room textures [1:44]
**Transcript (timestamped):**
[1:46] have each texture divided into three different groups following the attribute we just created.
[1:52] Loading room p tangent u and v as in the last video, but this time using the room offset inputs
[2:00] with our attribute to pick different textures. And the way you do that is by loading different
[2:06] u-dim tiles, in this case I only add three. Now this tip is not necessarily on procedural shading,


### Importing subset groups [2:09]
**Transcript (timestamped):**
[2:13] but still I find it useful to organize our setup. As you can see I have different groups in
[2:20] these assets and need to target those groups to assign different materials. In Solaris we do have
[2:27] the different groups under the name attributes, but it's not loaded by default.
[2:33] So what you need to do is under import data, make sure you're importing the different subset
[2:38] groups, this way you can easily target them in our material assignment.


### Creating a leak map [2:45]
**Transcript (timestamped):**
[2:46] Okay this last one is on the experimental side, but still wanted to share it on how to create a
[2:53] lit map to use in shading. First I'm copying over a few deform spheres that will be the base of our
[3:01] volume fluid, randomizing a bit the viscosity attribute, and then you can create a volume
[3:08] solver to run the sim. Assign a color to the fluid particles and in a solver we can create a wetmap
[3:19] using an attribute transfer. Then we can pick a frame and cache it as we won't need the animation.
[3:26] Instead of subdividing our source geometry we can just render this to a texture using the
[3:32] attribute importing cops. As you can see we have this lick texture over the base.


### Mixing textures [3:43]
**Transcript (timestamped):**
[3:43] And in Solaris the easiest way to mix the texture in is by gaining down the base texture and mixing
[3:50] it with the original using the lick's mask as an input. I'm also adding a bit of noise but that's
[3:58] about it. So yeah hopefully you picked up a few tips and don't forget you can join my Patreon


### Outro [4:00]
**Transcript (timestamped):**
[4:04] and get sample files along with exclusive tutorials. Thank you and see you next time.



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

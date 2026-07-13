---
title: Procedural Animation with RBD
source: YouTube
url: https://www.youtube.com/watch?v=RbiH315adq8
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-animation-with-rbd/
frame_count: 0
frame_status: pending-selection
---

# Procedural Animation with RBD

**Source:** [YouTube](https://www.youtube.com/watch?v=RbiH315adq8)
**Author:** cgside
**Duration:** 6m17s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-animation-with-rbd <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I want to show you how you can fill up a container really easily
[0:08] and along the way also create some nice animation as you can see this barrel getting filled up with the cheese balls
[0:17] So yeah let's get into it!


### Modeling [0:20]
**Transcript (timestamped):**
[0:20] So I started by modeling the barrel, nothing too complicated, just a mix between procedural
[0:29] and direct modeling, this is how it looks
[0:33] So you can have a look at the file on my Patreon if you're interested in that part and in the rest of the configuration
[0:42] So then I'm importing that low polyversion of the barrel
[0:49] Transforming a bit the leads so it's not intersecting with the main barrel
[0:58] Creating an RBD configure, setting the collision shape to convexle and also creating the...
[1:07] In this case creating backfragments, so packing the geometry
[1:12] Then I'm initializing a torque attribute and then randomizing it for the main barrel
[1:22] In this case I had to set a really high amplitude due to the scene scale
[1:27] Then doing the same for the lead, in this case setting it to 85 and playing with the seed
[1:35] Then in the RGB bullet solver I'm just reducing the angular velocity from frame 144
[1:47] So just reducing it by 0.8 and if we have a look at the final result it will look something like this
[1:55] And after frame 144 it will slow down and get to the rest state
[2:06] So now for the feeling of the container


### Filling [2:10]
**Transcript (timestamped):**
[2:11] I'm just blasting the patch group that I've created from the modeling when I filled the polygons
[2:19] Transforming it a bit, scaling it up, then adding some normals
[2:26] So I can in the next step pick it along the timeline so going up as you can see
[2:35] Then I scatter some points in this case 14 and as a global seed I use the add frame
[2:41] So it gets a different result every time, a different seed
[2:45] Then I'm creating the velocity to fit the RGB, the RBD scene
[2:53] In this case by using the cross product between the position and the up vector
[3:04] You can see so it's creating this effect
[3:12] And from there I can just copy two points and it just a sphere, a simplified sphere
[3:20] And it will look something like this
[3:25] Then RBD configure so I can set the collision shape to sphere and also pass the velocity attribute
[3:35] So we can use it in the RBD scene
[3:42] Then I will emit these spheres for every four frames and before frame 120
[3:53] And in this wrangle I'm just setting the found overlap so they intersect along the way


### Simulation Points [4:00]
**Transcript (timestamped):**
[4:00] On the RBD I have nothing, just really default settings
[4:06] And then I'm focusing the points, so the simulation points I can show you
[4:15] The simulation points and it will look something like this
[4:21] So it is going around and filling it up along the way
[4:28] So from there I'm just copying two points with those simulation points
[4:35] I'm deleting everything but the orient attribute so it can properly instance the new geometry
[4:43] Which is just a displaced sphere
[4:49] And it will look something like this
[4:56] Creating this nice, swirly animation
[5:00] And I'm also placing a label on the barrel
[5:04] And this is a node that I created
[5:09] So basically I'm starting by blasting everything but the barrel
[5:16] Then time shifting it to frame 1
[5:20] And I have this node that places a label on the geometry
[5:28] You can find that on my Patreon
[5:31] And then I'm just picking it a little bit and point the forming it so it follows the animation as you can see
[5:39] Nothing to complicate it
[5:42] And then I'm sending these to salaries and rendering with karma
[5:47] But yeah, this was a quick one to show you how you can fill up a container in a creative way
[5:58] And I would like to thank Swalves for suggesting me to do proper animation
[6:04] And not just to stick with the default filling up
[6:09] Because it looks much better
[6:12] And hopefully you can find this useful
[6:14] Thank you for watching and I'll see you next time



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

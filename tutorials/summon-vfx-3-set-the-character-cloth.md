---
title: Summon VFX | 3 | Set the Character & Cloth
source: YouTube
url: https://www.youtube.com/watch?v=bh9PRfO-ebk
author: Houdini
ingested: 2026-07-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/summon-vfx-3-set-the-character-cloth/
frame_count: 0
frame_status: pending-selection
---

# Summon VFX | 3 | Set the Character & Cloth

**Source:** [YouTube](https://www.youtube.com/watch?v=bh9PRfO-ebk)
**Author:** Houdini
**Duration:** 12m58s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py summon-vfx-3-set-the-character-cloth <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Let's continue with the ClothCharacter that is coming through the portal
[0:06] For this one, I took a character from Mixamo, this zombie
[0:13] For the Cloth, we're going to build these patches
[0:21] Here, I'm using some curves for the Houdini creation
[0:30] And then put it together, I'm using some examples for them to be attached later
[0:39] And here, I've used to merge the points
[0:45] And then I'm using the Planner patch from curves to create the mesh
[0:52] And here, I'm putting some interior edge length, which is going to be the density of our mesh
[1:03] And here, I'm mirroring that result and putting another Planner patch from curves
[1:10] And making sure here the important is also renaming everything properly
[1:17] Because then we're going to use a Vellum drape
[1:23] That's going to be pretty useful to have everything properly named
[1:28] So this is the left part of the hood, the right part, then I'm merging those
[1:35] And here, I'm using the same process, doing a bunch of curves to match in pretty much the size of our cloth
[1:49] According to the character
[1:53] And mirror that result, fuse them to avoid these little gaps
[2:01] To merge them, and then I'm using again some other Planner patch from curves
[2:09] To transform these times to have the front and back part
[2:15] And here you will see all the meshes that we will need to start creating our cloth
[2:26] And here, I'm putting a Vellum constraint as the constraint tape cloth
[2:34] And I'm just modifying a little bit the density, the edge length scale, and also some stiffness
[2:46] Then here in the Vellum drape is where we are going to attach everything
[2:53] So here I have a preview of that
[2:58] So here pretty much we check weld additional seams
[3:05] And in the weld seams is where we're going to tell which seam we want to attach to the other seam
[3:14] So for instance, let me disable and enable this one and those will be the seams that are going to get attached
[3:25] So I did that process to all the seams that I wanted
[3:30] And then I'll simulate and we will see the cloth attached according to each seam, like so
[3:44] And here what I did was check frist at frame 50
[3:52] And we can cache that and load from disk.result
[3:57] This is going to be my first result
[4:01] And then with the Vellum brush node I adjust some shapes as I want
[4:13] Now here I'm adding an edge fracture
[4:18] So we can have some pieces for getting rid of it
[4:25] Let me hide that, yeah
[4:28] So the initial pieces that I'm working on will be a 5000
[4:35] And here I'm creating a mask where I'm going to specify which parts we want to get rid of that cloth
[4:47] So we don't have something uniform in those areas
[4:55] Then here I'm putting that mask in a group
[5:00] Having a group in bird, so this group will be our pinpoints for the Vellum
[5:09] And here we are creating the Vellum constraints
[5:14] And here is where I'm going to use those pinpoint groups
[5:21] And here another Vellum constraint, but with a constraint type, weld points
[5:27] This is going to be pretty much for breaking with the threshold of zero
[5:34] So everything that is not in that group we ensure that it's going to fall
[5:41] So here we can see a little bit of that
[5:46] There we go, so as you can see the areas that are not in the group we are getting rid of that
[6:04] And here then I'm using a fuse for merging some areas that we want to keep together
[6:14] Then I tam-chift in the 50 frame, which is going to be the frame that I want
[6:22] For getting rid of all of these small clots that we are eliminating
[6:30] I'm using the delete small parts
[6:34] So this will get rid of those meshes according to certain threshold
[6:41] Then here we are going to clean some attributes
[6:47] So we are going to make longer the pinpoints group
[6:53] Also the point attributes, I'm going to delete those
[6:57] And here I'm going to paint a new mask
[7:01] This is just for having a new pinpoint group
[7:06] This is going to be the new pin groups that we are going to use
[7:10] And then here is where actually we are going to simulate our loopable value movement
[7:21] So here another clots constraint with some normal drag
[7:32] And a little bit of less stiffness and damping ratio
[7:41] And here is where we are going to attach our pinpoints attached to geometry with those pinpoints
[7:51] And for the character here I'm using a bone deform to visualize the animation
[7:59] And here I'm adding a rig pose to manually exaggerating the arms
[8:07] Because I wanted more movement for the clots
[8:12] And here in there I'm adding a blend shape to go into our rest position to the animation position
[8:27] Then I'm doing some cleanup of the mesh
[8:30] So this is the only part of the mesh that actually I want to get included in the vellum simulation
[8:37] Doing a make loop
[8:40] And then I'm doing another blend shape
[8:45] But just for going from the tip pose to our loopable result
[8:53] And that is going to be simulated into the vellum solver
[9:06] As you can see here
[9:09] And inside of this vellum solver what I'm adding is some pop force
[9:14] I'm animating that amplitude a little bit and some pop wind
[9:19] Which is going to be the overall movement of the clots
[9:24] So I'm putting some amplitude and swirl size as well
[9:28] And then a file cache to have the result already cached in the disk
[9:36] So this is going to be our vellum cloth result
[9:41] And then this color is just to pre-visualize it
[9:45] And I'm using another make loop this time from 4,220
[9:52] So let me put here in 40
[9:55] So this will be pretty much the loopable result that we are going to export to Unreal
[10:07] And here on the other side for the character
[10:11] What I'm doing is just some cleanup
[10:15] I'm getting rid of a bunch of geometry and just keeping the important parts that we need
[10:22] Putting it in the make loop
[10:26] And we will have everything together
[10:31] The body and the clots
[10:35] Now for the exportation
[10:42] We will have two laps vertex animation texture nodes
[10:50] One for the clots and another one for the body
[10:54] And here for the clots
[11:00] We are going to export as soft body deformation soft option
[11:07] And our frames will be from 40 to 120
[11:13] And the input geometry will be the clots node that I have over here
[11:21] And for the body will be our body node
[11:29] Same frames, same target engines of body deformation
[11:34] And then we will be good to go to render all the stuff here
[11:43] So you will get a static mesh and the proper textures that we need
[11:53] Here also important to mention that for the Unreal project
[12:00] You will need to have the laps plugin as well
[12:06] So you can go here into the real-time shaders
[12:09] And Unreal Engine Content Plugin and Guides
[12:13] This will open a folder with the version that you need
[12:20] For this tutorial we are doing with 5.7
[12:25] So here we will find the plugin that will go into the Unreal
[12:35] Okay, cool, so now we have everything that we built in Houdini already done
[12:45] So now let's go to the Unreal part where we are going to build all our effects
[12:55] Using what we already have done



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

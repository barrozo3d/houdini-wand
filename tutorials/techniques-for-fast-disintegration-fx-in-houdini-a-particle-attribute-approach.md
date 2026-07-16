---
title: Techniques for Fast Disintegration FX in Houdini – A Particle & Attribute Approach
source: YouTube
url: https://www.youtube.com/watch?v=Syn7XjeCH_8
author: the point and prim
ingested: 2026-07-16
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach/
frame_count: 0
frame_status: pending-selection
---

# Techniques for Fast Disintegration FX in Houdini – A Particle & Attribute Approach

**Source:** [YouTube](https://www.youtube.com/watch?v=Syn7XjeCH_8)
**Author:** the point and prim
**Duration:** 5m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py techniques-for-fast-disintegration-fx-in-houdini-a-particle-attribute-approach <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome. In this breakdown video I'll be walking you through the workflow
[0:08] I used to create this disintegration effect in Houdini. We'll be covering attribute manipulation
[0:13] and particle simulation techniques and how pairing these together can produce an interesting
[0:17] result without long simulation times. I'll also briefly be covering the shading and rendering
[0:23] setup in material X and Karma XPU. This is a breakdown video and not really tutorial,
[0:29] but if you're curious to learn more I'm giving the hip file away for free on my Gum
[0:33] Road. You'll find the link in the description below.
[0:36] Starting with the mask we can use the distance along geometry node and manually select a few
[0:41] points to art direct where the effect spreads from. This node creates a dist attribute
[0:45] which we will then remap to drive the animation. Utilizing the smooth function and animator
[0:50] parameter and the classic rest noise rest technique. We can maintain full control over the
[0:56] timing with simple keyframes. For fracturing we only need one side of polygons. I use a
[1:03] scatter and the near point function to create a class attribute which can then be used
[1:07] for a cheap fracture using the split points node. Next I pack the geometry based off a unique
[1:13] per piece attribute. I convert the class to name but this works with any attribute as
[1:18] long as it's unique per piece. We need to simulate points so let's extract the piece
[1:22] centroids with an ad node. When packing I transfer the dist attribute from earlier. This
[1:26] means the mask point fault can be reused to retrieve the spreading animation. Lastly I'll
[1:32] set the stop attribute. We will want to gradually animate it from 1 to 0 inside the popnet
[1:37] using the mask. This will activate the points over the course of the sim. Inside dops I use
[1:46] a pop wrangle with a simple if statement. This simply reads the mask and the animator position
[1:52] of the source points pre simulation. If the mask has values of anything but 0 the stop
[1:58] attribute is switched from 1 to 0 meaning it becomes active in the simulation. If this
[2:04] condition is not met the points will simply update the positions to match the incoming
[2:07] animation. This is the other important line here. It creates an attribute that will increment
[2:13] on each frame a particle has become and remained active which is useful for manipulation
[2:18] per sim. The rest of this is standard particle simulation nodes. Pop drag pop wind and a pop
[2:24] advec by volumes. I'll come back to this later after we cover the smokes him. Once the
[2:32] particles are cached I copy the packed prims back on the points using the attribute created
[2:37] before. For particle rotations I use the active time attribute from the pop sim to blend
[2:43] from a rest paternion with the spinning one. Without going into a lot of detail this is
[2:49] the rest orient. All of this is the spinning orient and this blends between the two of them
[2:54] using active time as a bias. Moving onto the second layer of the sim, the inner core.
[3:04] I created the points using a simple points from volume, point to form it and applied the
[3:09] same mask. I split the points into two streams using the mask attribute. One will be for
[3:16] sourcing, the other for collision data. I want a source just the leading edge of the
[3:24] mask instead of everything at once. To do this I compare the points on the previous frame
[3:28] and the current one and then extract the difference. These points are then russerized for the
[3:37] smoke sim. The sim itself is very basic. Using only the soft level pirus solver with some
[3:43] wind and turbulence. I keep it very low res as we only need its valve field for evaction
[3:48] and never to render it. The smoke sim is then piped into both pop nets where we utilize
[3:53] the pop evac by volumes node to transfer the movement of our smoke sim onto the particles.
[4:01] A neat trick is to blend off the particle evaction by age. Serve the valve field from the smoke
[4:05] simulation dissipates, the pop wind will take over and you won't have unwanted particles
[4:09] left floating around with no movement. Finally I create some flake geometry with variations
[4:14] and instance one of the points to finish up this layer. I use simple sop imports to bring
[4:24] my geo into Solaris and rebuild the instances for the ash using an internal point cloud
[4:28] from Solaris. You can of course also just import the pack primitives directly if you want
[4:33] to. Moving onto shaders, the hand shader is just a bunch of noises layered together which
[4:38] are also piped into displacement. The only key thing here is that I'm using the rest
[4:42] attribute so the noises don't swim through world space. The inner particle shader is what
[4:48] is doing most of the heavy lifting for this effect. By remapping the age attribute we
[4:52] can drive the strength of a mission as well as blend between colors as the particles age.
[4:56] On here I've just got a simple key and fill light setup. I'm using an LP E-Tag node
[5:01] and enabling this checkbox so that I can split my beauty pass by its light groups and comp
[5:05] which provides a bit more control over the final look. My camera has almost no movement
[5:09] in the shot so I did use some dirty tricks like making some additional atmosparsers by
[5:13] animating and motion blurring some noise in 2D.
[5:16] And that's it for this video, thank you so much for watching. If you'd like to explore
[5:20] the techniques further and encourage you to check out the free hit file available on Gumroad.
[5:25] Bye for now and see you in the next one.



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

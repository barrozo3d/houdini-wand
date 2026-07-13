---
title: Procedural Tips: Flow Maps, RBD Emit and more
source: YouTube
url: https://www.youtube.com/watch?v=XFOiCiljWh8
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-tips-flow-maps-rbd-emit-and-more/
frame_count: 0
frame_status: pending-selection
---

# Procedural Tips: Flow Maps, RBD Emit and more

**Source:** [YouTube](https://www.youtube.com/watch?v=XFOiCiljWh8)
**Author:** cgside
**Duration:** 4m12s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-tips-flow-maps-rbd-emit-and-more <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, in this video I'll share 5 different tips that might help you in your future projects.
[0:06] This full scene is available on Patreon by the way.


### Flow Maps [0:10]
**Transcript (timestamped):**
[0:10] So I have this glass profile that I will revolve, and in order to have an inside selection
[0:16] to create the liquids, I can at least point save that range of points, making sure I resemble
[0:22] to get the points properly sorted, and with a range save out an inside group.
[0:27] And after having the glass geometry, I can still access that group and promote it to primitives,
[0:33] so I'm able to extract the liquid geometry.
[0:38] Now let's have a look at FlowMaps to create the liquid effects.
[0:42] You should be aware that this FlowMap visualized node as a bug if you try to use the viewport shader,
[0:49] but in our case we will use the vertex color.
[0:52] Also setting the FlowMap mode from color, previously created, and for the diffuse texture,
[0:59] I'm loading custom generator from cops. It's a VOP cop generator that uses a noise with another
[1:06] one distorting the position, which comes from the x and y position of the generator.
[1:13] Feeding the noise to a ramp and from the outside adding some blue colors.
[1:19] Then we can copy the nodepad with control C and paste it in the diffuse texture,
[1:24] along with the OP syntax, to import from cops.
[1:29] And as we are using the FlowMap mode as color, there's this point of option
[1:34] rating a noise to control the pattern.
[1:38] Finally, we can keep it animated, or just place a time shift with the desired frame to render.
[1:44] Okay, let's see how to easily create the umbrella effect.


### Umbrella Effect [1:45]
**Transcript (timestamped):**
[1:49] I am starting with the UVs, in this case we want them in a circular pattern to place the stripes.
[1:56] So for that we can use the polar projection,
[1:59] promoting the UVs to point the treewood since we want to use them in a pointvop.
[2:06] And in there it's really simple, just using a Stripes node, and again a turbulent noise to
[2:13] distort the UVs. You can play with the amount of stripes and widths.
[2:19] And in another pointvop I'm just displacing the points with the color from the previous one.
[2:26] Continuing on the umbrella, I'm saving out a position attribute to use in salaries,
[2:31] so I can orient the textures properly. As you can see I'm rotating and transforming the umbrella,
[2:37] and that way I can't have precise control over the rotation of the texture.
[2:42] As you can see I'm using the Carmetrip Lanner to texture the toothpick.
[2:46] And if I remove these nodes I get the wrong orientation.
[2:50] That's why I'm using the previously saved position, plus I rotate 3D, set to rotate 90 degrees
[2:57] along the Z axis. In this case since we are doing a transformation inside salaries,
[3:03] you might already assume it's rotated. And you can replace the custom position attribute just by
[3:11] the material exposition node. Okay, as the final tip let me show you how I created the ice cubes.


### Ice Cubes [3:13]
**Transcript (timestamped):**
[3:17] I extracted the top patch from the liquid and extruded it to create the collision geometry.
[3:24] Created a simple distorted cube and I will emit them using the RBD solver.
[3:30] I am also using the RBD configure to create packed frames and set the collision geometry to a box.
[3:38] Set some initial random rule and in this wrangle for every fifth frame and before frame 72 emit geometry.
[3:50] And finally you can cache out a resting frame. So that's basically the bunch of random tips
[3:57] but that I thought might be useful and worth sharing. The file will be available on Patreon if you
[4:03] want to have a look too. Thank you and see you soon.



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

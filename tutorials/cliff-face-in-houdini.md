---
title: Cliff Face in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=mcP3wLo1lIQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/cliff-face-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Cliff Face in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=mcP3wLo1lIQ)
**Author:** cgside
**Duration:** 11m0s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py cliff-face-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video I'll be showing you how you can
[0:04] create this sort of cliff face in Odini and also how to apply some procedural
[0:12] texturing with cops. So let's get started in the top of the network. I'm


### Tutorial [0:20]
**Transcript (timestamped):**
[0:20] basically creating a grid and scattering some points. Also applying some point
[0:28] cheater on the Z axis and copying some boxes over. Here I'm just randomizing
[0:34] the aperture wood to have random orientations and also the scale, not the
[0:40] p-scale, but the scale with a natural wood noise. Then I'm just applying some
[0:49] overall distortion with a mountain and box clipping. So I can cut off the top
[0:58] in there as you can see and also feeling the nose. Then from here I'm applying
[1:07] let me remove the lighting. I'm applying a mesh sharpen to have these more
[1:15] polygonal look that you can identify better as rock shapes. Then doing a basic
[1:26] BDB conversion so I can unify the mesh and also some some Boolean intersection
[1:37] to cut off some shapes. As you can see near this just will out to give some
[1:46] variation basically with a remesh, a jubot blur, big until a little bit
[1:52] mountain and then doing a Boolean intersection. Then again another mesh sharpen
[2:00] and you start to see the planes of the rocks. That's the idea.
[2:07] And then using a doing again a BDB conversion to have the mesh we in better shading.
[2:19] Now I want to quad remesh it. But as you can see we lose some detail although
[2:27] I'm using 50,000 polygons but before it was 600,000 so I'm subdividing the mesh and then
[2:38] re-projecting it to the original mesh with minimum distance. This way we can get
[2:45] the fidelity but keep the better topology. Then I'm doing some cuts on the rocks with a volume
[3:00] up in a BDB setup. As you can see basically by manipulating the frequency of the noise in this
[3:13] case is just a simplex noise and that's turbulence noise to the position to distort it a bit.
[3:25] And then just fit the values to where these cuts on the rocks.
[3:34] And I'm caching this. This will be my iPoddy. We know you've used for now.
[3:42] So then I'm poly reducing in this case in a loop so it can be a bit faster
[3:49] and quad remesh it as you can see and this will be my loop poly. I just need to do some
[3:57] UVs for that I'm scattering some points creating a attribute with the point number and transferring it
[4:04] to the mesh as you can see. So I have these mesh divided into tiles.
[4:12] Then I'm just promoting it to a primitive attribute and iterating in a loop using a UV
[4:18] flatten and this will UV my mesh and then just lay it out and this will be my final UVs.
[4:32] Then that's my loop poly mesh transferring the UVs over the main mesh
[4:39] and this is how it looks. As you can see it did a pretty good job these labs UV transfer
[4:50] then measuring the curvature and creating an emiotic vision best so I can texture these
[4:59] in the cups. So in cups let's see how this looks so this is basically the texture in which is
[5:14] again pretty basic. I'm importing the iPoddy, restaurizing to UVs in this case set the space to
[5:26] UVs then restaurizing the attributes in this case the the AO, the concavity, the convexity from
[5:35] the curvature and then the alpha. Then create from the AO mask I'm creating a monotone GB
[5:46] as you can see and I sample the texture and then re-sample the ramp using the
[5:57] snippets I shared in the last video on the re-sample color ramps.
[6:03] Then doing it I just we adjust just to color correct a bit the initial colors then from the concavity
[6:20] I'm applying some color correction again I can show you how that looks so on the low poly mesh in
[6:29] this case so basically I'm darkening those concave areas then doing another edges we adjust in
[6:40] this case brightening the the convex areas as you can see if that's not this one this one
[6:54] as you can see I'm brightening those areas and since we have these sort of issues due to our UVs
[7:04] I'm just taking the alpha and extrapolating the boundaries as you can see and that should fix our issue
[7:14] so now for the vines there's nothing to complex really this can get pretty complex if you want to
[7:30] create a growth system and whatnot but I just kept it as simple as possible basically by importing
[7:38] the low poly clip it and scattering some points then sorting them by the y axis group ranging some


### Outro [7:40]
**Transcript (timestamped):**
[7:50] of the top points to be our start and then some of the middle in here connecting edges adjacent pieces
[8:02] adding some costature votes by using some noise and finding the shortest path as you can see
[8:11] fusing the points polypads we sample it with subdivision curves and then create these curve branches
[8:22] which is a lives note that allows you to create some branches I just said it the hda and promoted
[8:30] global seed from here I'm splitting the the branches creating an orientation along curve
[8:42] so I can copy some leaves to it but before that I have the the vines and just sweeping it as you can see
[8:53] and for the the leaves and creating again the orientation grouping some points randomly so where
[9:04] why we'll copy the leaves doing it at your good randomize for the p scale and then for the leaves
[9:16] I'm just drawing the curve as you can see pretty randomly fusing, resembling doing a mesh sharpen to
[9:25] have these sharp corners resembling again creating the geometry deleting the curves remashing
[9:38] and creating some UVs then I'm doing some UV draw sharp to fit the texture to it as you can see
[9:51] and also did some bend and I have three variations of leaves so one darker one more orange and one
[9:59] lighter that I'm doing I'm doing the attribute from pieces so I can randomize the
[10:08] the leaves and in the copy to points I am using the piece attribute in this case class from
[10:16] this connectivity note and attribute from pieces set in this case to piece weights
[10:25] and then I'm just copying the the leaves and altogether it comes something like this
[10:34] and with some lighting it will look even better so yeah guys that was it hopefully you got something
[10:44] out of this and don't forget you can grab all the files from my videos in Patreon on my Patreon
[10:51] and also check out my courses there other than that thank you for watching and I'll see you next time



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

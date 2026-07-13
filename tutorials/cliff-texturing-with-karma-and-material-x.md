---
title: Cliff texturing with karma and material X
source: YouTube
url: https://www.youtube.com/watch?v=WAyk2xCn5rs
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/cliff-texturing-with-karma-and-material-x/
frame_count: 0
frame_status: pending-selection
---

# Cliff texturing with karma and material X

**Source:** [YouTube](https://www.youtube.com/watch?v=WAyk2xCn5rs)
**Author:** cgside
**Duration:** 4m3s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py cliff-texturing-with-karma-and-material-x <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back. So in this video I'm going to show you how you can quickly
[0:05] texture an asset using procedural techniques. But before we jump into the cliff shading,


### Material X [0:08]
**Transcript (timestamped):**
[0:12] let's have a look at the custom material X note that I will be using in this video.
[0:17] You'll be able to access it through the material X menu, CGS TrackLaner,
[0:23] which is the material X version of previous digital asset I posted.
[0:28] But this one has some advantages when it comes to speed and overall experience.
[0:34] At the top you have the signature. Basically use color for albedo, float for roughness and displacement
[0:42] and vector tree for normal maps. Let's connect the texture. You have the option to pick a different
[0:48] one for you chexes. So this is basically a UV randomizer but within a TrackLaner projection,
[0:56] so you don't need UVs at all. You have a seat for the randomization if you don't like the default
[1:02] look, the tiling amount, the TrackLaner blending of the different projections and the UV blending
[1:10] that controls the sharpness between each repetition of the texture.
[1:15] Here I have this scene with two spheres. The one on the left is using my notes and the one on the right
[1:21] the default TrackLaner projection. I have the different channels mapped, just changing the
[1:28] signature and textures inputs, so they all share the same tiling and randomization settings.


### Comparison [1:39]
**Transcript (timestamped):**
[1:39] As you can see the one using the default material X node is repeating the patterns and doesn't
[1:46] work properly on normal maps and even displacement maps due to the blending between projections.
[1:55] And the CGS TrackLaner is doing a better job at hiding the repetitions and works perfectly
[2:02] with normal maps and other channels. You can grab all the scenes from this video along with the
[2:09] TrackLaner node from my Patreon. Let's get to the clip shading, so I created this example


### Shading [2:12]
**Transcript (timestamped):**
[2:16] cliff with some mightfields and VDB as shown before on the channel. Then I'm creating some custom
[2:23] masks to use in texturing, first convexity mask and then in point-vop a slope mask.
[2:31] Moving into Solaris importing the geo and let's see the shader setup. As you can see I'm using
[2:38] the custom TrackLaner node and this is how it looks with everything combined. So in the first
[2:44] TrackLaner I'm loading a mega-scan texture of a cliff and I am mixing with another rock texture.
[2:52] And as the mixing factor I am using the convexity mask but you can also use the
[2:58] concavity one for a different look. This is how it looks both textures combined.
[3:06] Then I am mixing on top the grass texture using the slope mask.
[3:14] As for the remaining channels I am just using the respective textures,
[3:19] making sure I'll love the TrackLaner node share the same tiling and randomization settings
[3:25] using reference nodes. And this is how it looks with displacement.
[3:32] And finally I added a simple ocean and some other elements and you can see the final result of
[3:38] the texturing. This was a quick setup you can create more masks and experiment with different


### Final result [3:40]
**Transcript (timestamped):**
[3:45] textures to get the desired look, add noises and so on. So yeah hopefully this can help you in your
[3:52] next project and feel free to get all the files plus the custom TrackLaner node from my Patreon.
[3:59] See you in the next one!



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

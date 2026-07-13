---
title: MaterialX and Karma | procedural networks
source: YouTube
url: https://www.youtube.com/watch?v=kdpeMWXIGrY
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/materialx-and-karma-procedural-networks/
frame_count: 0
frame_status: pending-selection
---

# MaterialX and Karma | procedural networks

**Source:** [YouTube](https://www.youtube.com/watch?v=kdpeMWXIGrY)
**Author:** cgside
**Duration:** 8m57s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py materialx-and-karma-procedural-networks <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome so in this video I'll be sharing a few tips on how to work with the material X and
[0:08] Karma procedural notes. I will also be showing you how to debug notes, how to solo them and how to
[0:17] combine normal maps and a few more tips and tricks. So let's get started. So as you can see I


### How to solo nodes in karma and repeat textures [0:23]
**Transcript (timestamped):**
[0:25] build this very simple scene to show you some of the procedural notes and let's start by looking at
[0:34] the first tip is on out to debug notes or solo notes. Actually it's pretty simple you just select
[0:42] the notes and press X and you will start to visualize an emission shader, a flat emission shader. So
[0:52] this is really useful when you're trying to debug noises and other types of notes. So as you can see if I
[1:02] disable this notes in here and I look at this one or this output as you can see I have just the text
[1:14] repeating once with the material X image and I can enable this one it won't make any difference
[1:23] is just the texture coordinates then I can multiply it to repeat so 5x5 since it's a square texture
[1:34] but if you look at the interior in here it's offset by half so I can use an add notes
[1:42] and it will move to the center as you can see so just moving the X component by 0.5
[1:53] and I also have a normal map in here as you can see just a wrinkle normal map
[2:03] and anytime you can press X again and you will visualize the main shader
[2:09] so as you can see and I also have an attribute that I'm fitting in a range so increasing a bit
[2:18] the low and multiplying by a scale value that I'm fitting to the scale of the normal map
[2:29] and at the end I have some parts that have more wrinkles and others that have less based on an attribute


### Creating materialX patterns [2:41]
**Transcript (timestamped):**
[2:42] so let's have a look at the second shaders so I will let front and I also have the same texture in
[2:52] here repeating so is this one on the outside ignore this inside so in the same exact position
[3:02] and let's see the first pattern is actually pretty simple it's just agreed as you can see
[3:10] just agreed that I slightly irritated 45 degrees with the material X rotate to D
[3:18] or you can use also a place to D then I'm just extracting one channel
[3:27] and mixing it in this case I'm just inverting it but I could use a material X invert but for some reason
[3:34] I use the mix just set foreground to zero and background to one
[3:40] and then I have a more complex pattern not very complex but let's have a look so if I disable
[3:51] these tree nodes I pressing Q and I look at this one as you can see it's just a material X line
[4:02] which is just a rounded line as you can see I have placed it and sized it accordingly
[4:12] and then if we try to repeat this node it won't actually allow you in the node itself
[4:21] so what you can try is multiply as you can see I'm repeating it 16 by 30
[4:30] but the texture disappears so I'm trying with an add node placing it in the center
[4:37] but that doesn't work and what I need to do actually is use a model to repeat the texture to
[4:44] repeat the pattern and I'm using the scale X divided by two in here since I want it in the center
[4:53] and as you can see these add nodes just makes everything work from the center instead of that
[5:03] random position so yeah that's how you can repeat material X line and other patterns that are
[5:12] known tie-lobe by default so using the module along with the multiply so as you can see if I go
[5:19] in here and change this to 60 it just will repeat more more times so in this case I have to look at
[5:31] this one so I can change the repetition to 60 in this case I want slightly less and I am doing
[5:43] basically the same in here so let's look at this one but in this case this material X line is
[5:50] pointing is oriented along the X axis so manipulating these values and the only difference that I'm
[6:02] doing in here so if I disable these nodes you can see that I will have the pattern along the
[6:13] edges which I don't want so I created a material X placed to the nodes that I'm setting the pivot
[6:22] to the center and scaling it slightly on the Y so I get rid of those edges and the rest is
[6:32] the same I'm just multiplying in this case 30 by 16 doing an ads and playing with the value of
[6:39] the model so I can fit it between the pills as you can see you can have a look at the file on
[6:48] patreon and also how I how I did the modeling is right in here everything is procedural so you can
[6:57] play with it and the final tip is on how to layer bump maps or normal maps how to combine them


### Combine normal/bump maps in karma [6:58]
**Transcript (timestamped):**
[7:08] how to blend them so this is actually pretty simple as you can see I have I have this pattern in
[7:17] here and these max lines that I just use a material X max to combine both in an additive mode
[7:27] then I'm placing that I am connecting that to the height of a material X bump that will just connect
[7:35] to the normal and the second bump map I'm creating another one in here and I'm connecting it to the
[7:46] normal inputs of the master bump map let's say and you can do the same with the material X normal map
[7:55] so yeah that's basically it as you can see very simple setup but that requires a bit of
[8:07] tips and tricks that you gather along the journey mostly I got this from watching Unreal tutorials
[8:16] and you start to learn how to tile nodes how to offset with an add or subtract so yeah that's


### Outro + Promo Patreon [8:24]
**Transcript (timestamped):**
[8:26] basically it as always you can grab the file on patreon and see how I build this in how I did the
[8:35] modeling as you can see you have a back part also that you can try to play with and yeah if you
[8:44] want to support the channel make sure to check out my Odinik course is also that I have on Patreon
[8:50] shop and that's all thank you and I'll see you next one next time



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

---
title: Material alphabet in Houdini: A for Amber | Episode 02
source: YouTube
url: https://www.youtube.com/watch?v=zESg7I8IS4Q
author: Kotov Roman
ingested: 2026-08-06
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/material-alphabet-in-houdini-a-for-amber-episode-02/
frame_count: 0
frame_status: pending-selection
---

# Material alphabet in Houdini: A for Amber | Episode 02

**Source:** [YouTube](https://www.youtube.com/watch?v=zESg7I8IS4Q)
**Author:** Kotov Roman
**Duration:** 6m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py material-alphabet-in-houdini-a-for-amber-episode-02 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey, welcome back to the Material Alphabet series.
[0:03] If you missed the previous part, you can find the link in the description.
[0:06] In this series, I'm creating a different material study for each letter of the alphabet.
[0:10] It's not meant to be a perfect step-by-step tutorial, but more of a process walkthrough.
[0:14] In this part, I'll continue developing the Ember material.
[0:17] And let's start.
[0:19] Internal Shutter pieces don't really look like Shutter.
[0:22] They're way too soft and smooth, in my opinion.
[0:24] Let's see what we can do about that.
[0:27] First, let's drop down the subdivision and see if that's gonna make them more shattering.
[0:31] We can add subdivision later, after the noise.
[0:35] Let's also get the second level of the noise.
[0:38] To make it work properly, we'll have to disable thickness.
[0:45] We will add thickness later, with the second level of Boolean as well.
[0:49] We get a lot of points that aren't connected to the geometry, but that's an easy fix with an add node.
[0:55] Now that's a little bit better.
[1:03] Let's see if we can get wider reflections in the shape.
[1:06] Making lights a bit brighter also helps.
[1:10] I want to get one main reflection a bit to the top and onto the right.
[1:18] That's exactly what I was looking for.
[1:20] This light goes a long way of helping to sell the feel of shininess and glossiness of that material.
[1:26] But it's way too perfect at the moment.
[1:28] Let's see if we can fix that with the help of a few textures.
[1:31] Let's connect one of them directly to the surface to preview.
[1:34] But we don't have any UVs, and that could have been a problem if we had any sort of animation on our geometry.
[1:40] Luckily we don't, so let's carry on.
[1:42] Nice addition to the recent redshift update is UV projections.
[1:46] But I didn't really find much use for them.
[1:49] Tri-planner just gives nicer results for static geometry.
[1:53] Let's wire up several textures into the Tri-planner and connect them to the bump land.
[2:01] And I almost forgot to make a snapshot of a before.
[2:06] Now we can continue with adjusting the bump bumps and check if we make any good progress.
[2:11] This specific texture has to sell the feel of the bubbles directly on the surface of the material.
[2:18] But I don't really like it, so let's change it to another one.
[2:24] This one will be responsible for the bigger dense.
[2:32] Let's see if we can do something with the reflection roughness.
[2:36] I have a texture for it, but I would like to squish it, because it's way too bright.
[2:42] Let's disable all the roughness for a second and see if that's gonna be better.
[2:48] It is not, so I will bring back roughness slowly.
[2:53] Let's disable all the inside geometry for a second, so we can focus on the textures.
[3:02] The trickiest part is to find the right balance between the roughness and the bump strength.
[3:07] Now I will bring back the inside geometry and see if those textures will work with them.
[3:13] It is getting better, and we get a lot more details, but it might be too much.
[3:18] Let's dial it down a bit.
[3:25] I can see that the roughness might be too strong.
[3:30] No roughness at all is actually growing on me. Let's make a screenshot of that.
[3:37] Let's also try a different texture for a roughness.
[3:42] I definitely like the amount of details I get from the bump textures.
[3:47] I think that's enough textures for now. Let's see what we can do with the noises.
[3:51] I will use more annoying noise. Actually, two of them.
[3:55] And plug another one into the global scale of the first one.
[3:58] That way we will get highly detailed areas, and less dense areas as well.
[4:06] Let's plug it into the bump map, and adjust the scale.
[4:13] That's gonna be our main bump map.
[4:17] Let's add a new layer.
[4:19] I will add a new layer, and I will add a new layer.
[4:22] I will add a new layer, and I will add a new layer.
[4:25] That's gonna be our main bump map.
[4:29] Let's get another one for more crystallized surface details.
[4:38] I don't like that it's applied across all of the geometry.
[4:41] So let's mask it out, using another noise and a multiply node.
[4:51] Now it's gonna be applied only on selected areas.
[4:54] Let's make a snapshot of the progress so far.
[4:58] That's quite a progress. I think I will leave it at that.
[5:07] Let's work on the camera, and I think we will be ready to render soon.
[5:11] First, let's enable the lot.
[5:14] I like to enable Apply Color Management before the lot, so it doesn't get too harsh.
[5:18] I would also like to roll down highlights.
[5:21] And to compensate for that, I can increase the exposure.
[5:25] I am wiggling parameters left and right not just for fun.
[5:28] I am trying to assess how much of the effect I need.
[5:31] But it does look funny looking back at the recording.
[5:37] I don't usually do that, but for this specific scene, I would like to crash blacks a bit before color grading.
[5:42] Let's organize scene a bit and set up several cameras.
[5:47] There is not much left to comment here.
[5:50] I will just look for interesting angles and set up cameras.
[5:54] After that's done, I will send everything to render.
[6:00] That's it for the ember material.
[6:02] In this final part, I brought the piece together and finished the main look.
[6:05] As with the rest of the material alphabet series, this was less about making a perfect step-by-step breakdown.
[6:10] And more about showing the process behind the study.
[6:13] If you missed the previous part, the link is in the video description.
[6:16] And if you want to follow the rest of the material alphabet series, I will link the full playlist there as well.
[6:21] Thanks for watching.



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

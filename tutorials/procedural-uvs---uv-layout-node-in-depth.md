---
title: Procedural UVs - UV Layout Node in Depth
source: YouTube
url: https://www.youtube.com/watch?v=7kUDLsNn0iA
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-uvs---uv-layout-node-in-depth/
frame_count: 0
frame_status: pending-selection
---

# Procedural UVs - UV Layout Node in Depth

**Source:** [YouTube](https://www.youtube.com/watch?v=7kUDLsNn0iA)
**Author:** cgside
**Duration:** 5m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-uvs---uv-layout-node-in-depth <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, today I'm going to break down the UV layout node and how to use it with custom attributes.
[0:07] And this file will be available on Patreon by the way.
[0:11] Let's start simple with this example where I have a window frame and want to maximize texture space.
[0:18] You can see that I'm grouping all the edges and then unwrapping.
[0:22] And in the UV layout node, I can use that edge group to cut the UVs into unique islands.
[0:28] This way, maximizing the texture space.
[0:32] You can see the coverage amount from 20% to 70%.
[0:36] Now the island attribute.
[0:38] I start by copying 8 spheres and packing them.
[0:42] Then I can use a wrangle to create an island attribute that will allow us to distribute the islands in a pattern using the module.
[0:49] We also need to promote to a primitive attribute required by the UV layout node.
[0:56] And packing, and you can now see the attribute we just created, a repeating pattern from 0 to 3 along the spheres.
[1:04] With default settings, we get the UVs layout for every sphere, 18 total.
[1:10] But with the island attribute, we are now stacking islands with the same value.
[1:15] We can go back and change the amount of islands we need.
[1:19] This can be useful if you want to increase texture space, but still have some variation on the texture.
[1:25] Now let's look at the target UDIM feature.
[1:28] I have the same geometry from the first example, and in a wrangle assigning in this case two different UDIMs based on the Prims.
[1:36] If we look at the layout node and enable the UDIM target attribute we created, the different islands are distributed into two different UDIMs.
[1:47] And we can always change how many tiles we need.
[1:50] Just make sure you set the targets to pack into UDIMs.
[1:55] And while we're here, we can set some padding around each island, applied to the boundaries also to avoid baking and texturing common issues, and there is also a setting to spread the islands to all the available space.
[2:08] Let's see now this floor tiles example where we can randomize the UVs of set and rotation.
[2:14] So we have some basic UVs that covers all the available space.
[2:20] We're applying some random rotation with these Vax snippets shared by Constantine Magnus.
[2:26] And as you can see the UVs are overlapping, so we can use the UV layout to distribute the islands while keeping some degree of randomness.
[2:36] And to have more randomness we can increase the iterations under advanced settings and play with the random seed.
[2:44] This will work well for some random offset of the texture.
[2:48] You can keep both or just use one.
[2:51] Let's say you need a different texture resolution for each island, for that you can use a scale attribute in the layout node.
[3:00] This is a very simple example, I'm just creating a attribute based on each primitive, adding one, and using it in the island scale attribute to change the scale of each island.
[3:12] Again very simple but you can use this to scale down less visible areas of your model for example.
[3:19] Okay now let's have a look at some more elaborated examples.
[3:24] In this one we're using the layout top to avoid intersections and factoryometry into a shape.
[3:32] The idea is pretty simple, we just take some shapes and copy them to points, in this case using the name attribute.
[3:40] Then in a UV layout instead of packing UVs, we will use the position attribute, set the proper projection plane, and you might want to increase the iterations and play with the seed so you get better results.
[3:55] And here we are using islands from the second input, which is the initial grid, but you can swap it for any geometry.
[4:05] As a final touch we can extract the empty space from the initial layout and pack some more pebbles in between using the exact same settings, then just merge both results.
[4:19] In this final example we will combine the island and you deem attribute so we can have some balance between variation, resolution, and amount of tiles used.
[4:29] So for each repeating geo I have overlapping UVs.
[4:36] As the geo is packed I can use a wrangle long points and distribute the geo into three different islands and you deems.
[4:44] Here we're just combining what we've seen before.
[4:47] Promote to pre-match reboots and unpacking. And with the UV layout node we can use those attributes to lay out islands on top of each other and along three different to you deems.
[4:58] I am also randomizing the point order with a sword so it doesn't create a repeating pattern.
[5:06] Okay guys hopefully this can be useful to you, nothing too overpowered but can definitely be handy sometimes.
[5:13] And as always you can grab all the project files from my videos on Patreon along with exclusive tutorials and courses.
[5:21] Thank you and see you in the next one.



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

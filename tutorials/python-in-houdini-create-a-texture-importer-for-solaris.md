---
title: Python in Houdini  | Create a texture importer for Solaris
source: YouTube
url: https://www.youtube.com/watch?v=zZBkR8rk-_s
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/python-in-houdini-create-a-texture-importer-for-solaris/
frame_count: 0
frame_status: pending-selection
---

# Python in Houdini  | Create a texture importer for Solaris

**Source:** [YouTube](https://www.youtube.com/watch?v=zZBkR8rk-_s)
**Author:** cgside
**Duration:** 4m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py python-in-houdini-create-a-texture-importer-for-solaris <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back.
[0:03] In this video I'm going to show you how you can build your own texture importer for
[0:07] the salaries and material likes context.
[0:10] This is a very simple implementation and it's more like an exercise to introduce Python
[0:15] in Odini if you're used to it in other packages.
[0:19] I'll be uploading the code to Patreon if you guys want to check it out.
[0:24] So here I have my texture folder with a very basic naming convention that has the object
[0:31] name, channel name and color space and that's the information that we're going to use
[0:36] to guide our tool.
[0:38] So in Solaris let's create a material library.
[0:41] This is the starting point and the reference for the script.
[0:45] The first thing we need to do is to import the Odini and OS modules.
[0:50] Next we set a list of channels that in this case is Substance Painter Friendly.
[0:55] Again very basic, ideally you would have dictionaries with lists of different names for
[1:01] albeit roughness and so on.
[1:04] Now we prompt the user for the base name of the object that's baked in the file name
[1:09] like wood, cloth or plastic wheels.
[1:13] You can add some buttons like ok and cancel to complete the operation.
[1:18] If we print it you can see that the output is a list of the index of the button pressed
[1:25] and the given input string.
[1:29] So if the user didn't cancel the operation and the input was not empty we will execute
[1:34] some code.
[1:36] First let's create a variable for the current project path.
[1:43] After that we have another user interaction so the folder of the textures can be selected.
[1:51] Now we start to interact with the current context.
[1:55] Storing the current node selected the material library in a variable.
[2:00] So that later we can add nodes inside.
[2:07] Creating a material x with the create node command you can also rename it here.
[2:12] I noticed sometimes the UVs are required so I'm also creating a texture coordinate
[2:17] node and setting it to Vector2, UNV.
[2:23] And here we are going to iterate over the textures folder so we can filter the right textures
[2:28] to import.
[2:29] We also want to iterate over each channel and if the texture file has a matching base
[2:35] name and a channel name we will continue with the logic.
[2:40] If we bring the result you can see it picked only the three textures that exist for this
[2:45] specific assets.
[2:47] Now we can create a USD texture node or you can use a material x image.
[2:53] Then we save in a variable the index of the channel being processed so we can use it later.
[3:00] Add the name of the texture to the folder path the user picked and finally set the file
[3:05] name with the path we just saved.
[3:08] For organization we can just lay out the nodes inside the material library and as you
[3:13] can see it's working as expected with the file name of the node being set correctly.
[3:20] I mentioned at the beginning that I also have the color space in the file name so we can
[3:26] use it to set the color space here.
[3:32] The way you can check the correct token is in the menu tab of the parameter interface.
[3:39] So now we start to do some connections first the UVs to the texture nodes.
[3:45] Next we check if the channel is the base color and connected to the base color which is
[3:50] the input one.
[3:52] We also need to set the output for the RGB output.
[3:57] Then we do the same for the roughness and normal or I channel creating the necessary nodes
[4:03] and connecting the correct to the correct inputs.
[4:07] The only issue here is that we need to find the correct index of the nodes.
[4:12] For example the normal inputs of the material x is 40 we just need to count it I guess.
[4:21] So that's it then you can create a shell item with the codes and execute it anytime
[4:26] you need it.
[4:27] Or even create a custom radial menu for the python scripts.
[4:31] I hope that you have learned something and check out my Patreon and Gamero if you'd like
[4:36] to support the channel.
[4:38] Thank you and see you in the next one.



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

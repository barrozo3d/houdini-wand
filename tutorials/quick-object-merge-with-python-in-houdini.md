---
title: Quick object merge with Python in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=fDV8SQegEDc
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/quick-object-merge-with-python-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Quick object merge with Python in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=fDV8SQegEDc)
**Author:** cgside
**Duration:** 6m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py quick-object-merge-with-python-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this video I'll share a quick Python script to create an object merge automatically.
[0:07] So you select now let's say and you press an odd key and you will have the the object merge with the relative path.
[0:15] So it should be pretty quick let's get into it.
[0:20] So I'm going to open the Python source editor and first of all I'm going to import the own module.
[0:28] And let's increase this and then we will have to save the selected node.
[0:37] So let's name the variable selection and we're going to use the all dot selected nodes and we will grab the first one.
[0:47] So we print out this.
[0:50] Let's select a node and it will automatically print out the selected nodes.
[0:57] So now that we have the selection we can grab we can create the object merge. So object merge will be equal to selection dot parent dot create nodes.
[1:14] And we will create like me increase this and we will create the object merge.
[1:25] And we also need to position it. So for that I'm going to create in here I'm going to grab the position from the selection.
[1:33] So cell position it will be equal to selection dot position.
[1:40] And we can comment this out and print out the position.
[1:48] So as you can see we have the position of the nodes.
[1:51] And after creating the object merge we can set the position. So all the object merge dot set position.
[2:02] And we will pass all dot vector to and we will grab the exposition.
[2:09] So cell pass zero and we will subtract one to offset it a bit and we will grab the cell position one.
[2:19] So the y axis and we can also subtract one.
[2:22] You can pick the position. I'm just going to do it like this.
[2:26] So now this should create the node. So let's comment out and do it.
[2:34] And as you can see it's creating the object merge away from the node.
[2:39] Now we just need to grab the path. So for that I'm going to after the setting the position we will grab the relative path.
[2:49] And it will be object merge dot relative path to and we will grab from the selection.
[3:00] And then we can just say object merge dot farm since we want to add it to the select me create an object merge.
[3:10] We want to add it this path in here. So it's called object path one. So object merge dot farm.
[3:17] Oh, we J farm path one and we will set it to the relative path.
[3:27] And now this should work. Let's see. So in that, oh, we need to select the node.
[3:34] Relative path to cell. So relative path object merge dot relative path of its upper case.
[3:48] And now if we do this and we should have the relative path there.
[3:53] So we can simple and now we want to transform this into a tool.
[3:57] But in case we don't have a selection, these will erode. So we can just encapsulate these in a try except so try.
[4:06] And we can place this inside the block.
[4:13] And we can just say except index error.
[4:21] And we can call the dot UI dot display message.
[4:29] And we can say no node elected.
[4:36] And let's see if that now works. As you can see, we get these warning.
[4:41] And if we select the node, it should create the object merge.
[4:45] Now it's pretty simple. We just open we just open in here the shelves.
[4:52] And we will copy this, drag it in here, edit the tool, go into options, change the name.
[4:59] So let's say we object merge demo.
[5:07] We can change the icons.
[5:14] Let's speak this one.
[5:18] And we need to change this to python. And we can assign a not key in this case to the network pane.
[5:23] So just come in here and assign a not key. And you should have that already there.
[5:29] Now just let's delete this, apply and accept. And as you can see, I have assigned a not key in here to my previous tool which is this key combination.
[5:40] And now when I when I press it, I get the object merge.
[5:49] So that was basically it. Hopefully you enjoyed this one. Don't forget you can grab the script on my Patreon alongside with all the projects files from my videos.
[5:57] And also exclusive tutorials. Thank you for watching and I'll see you next time.



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

---
title: Add details with regions from image labs tool
source: YouTube
url: https://www.youtube.com/watch?v=qS5uDc8EePQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/add-details-with-regions-from-image-labs-tool/
frame_count: 0
frame_status: pending-selection
---

# Add details with regions from image labs tool

**Source:** [YouTube](https://www.youtube.com/watch?v=qS5uDc8EePQ)
**Author:** cgside
**Duration:** 3m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py add-details-with-regions-from-image-labs-tool <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone and welcome back. So in this video we'll create some quick loading assets using a new lab stool and very basic valum setup.
[0:11] So here I have a new image put together in Photoshop that will be using to create our clouds.
[0:18] It helps to make them different colors so the tool can easily separate them.
[0:23] As you can see I'm using these new regions from image labs tool to automatically create masks.
[0:30] You just have to plug the image and wait for a few seconds.
[0:34] Then you can add a name attribute and rename your pieces as up to here.
[0:40] Getting rid of the black background and also the color associated.
[0:45] As we have a name attribute we can easily loop through the pieces and do some operations.
[0:50] I am resampling remashing and placing it in the center.
[0:55] Then measuring the curvature and in a group node we can select corners based on the curvature attributes.
[1:04] And we also need to subtract the bottom part of this selection.
[1:08] It would also help if we used a group expanding here so it grows the selection to use as pin points in valum.
[1:18] Okay so from here I have simulated and brushed the assets with the valum brush and this is the result I got.
[1:26] I guess these aren't euro props but can work well for me to background objects.
[1:33] I'm just going to quickly demo the workflow adding a valum plot and just changing the bend stiffness.
[1:40] Honestly I don't know what I'm doing here but seems to give me the result I wanted.
[1:46] So then we can create a valum brush, press enter and G to simulate.
[1:53] I forgot to set the pinning on the valum plot.
[1:56] After doing that we can reset the changes and simulate again.
[2:02] As I brush I can see this is way too low-res so let's go back and add some subdivisions.
[2:10] Now we need to add more points pins. I should have grown the selection as I told you before.
[2:16] For now let's just press shift middle click to pin some areas.
[2:21] Now you can brush till you feel it's looking somewhat decent and finally cash it.
[2:30] In this loop I'm just aligning it to the maxin-wise so it's next to the points I have for ending these pieces.
[2:39] Now we just copy the points with an attribute from pieces at random, deleting also randomly a few points.
[2:46] And of course if you have more variations it would look better.
[2:52] But for the amount of work we put into it doesn't look that bad.
[2:57] Okay guys I'll post an sample file on my Patreon and check out my step-by-step courses on procedural workflows.
[3:05] Thank you for watching and see you in the next one.



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

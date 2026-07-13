---
title: Matrix color transform in cops for Houdini 21
source: YouTube
url: https://www.youtube.com/watch?v=ZDlL81gmafE
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/matrix-color-transform-in-cops-for-houdini-21/
frame_count: 0
frame_status: pending-selection
---

# Matrix color transform in cops for Houdini 21

**Source:** [YouTube](https://www.youtube.com/watch?v=ZDlL81gmafE)
**Author:** cgside
**Duration:** 7m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py matrix-color-transform-in-cops-for-houdini-21 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in today's video I wanted to present you a tool that I've been working on and that
[0:07] I'm releasing today.
[0:08] Basically is a way to color correct these HDR images with color shards.
[0:14] So instead of me talking, I'm just gonna show you.
[0:17] So I'm gonna drop a color matrix, matrix color transform.
[0:21] In this case I have an HRI where I have the color shards but I extracted a section.
[0:27] I did this in Affinity Photo and I extracted a section where the color shards is.
[0:31] So I'm gonna connect this to the source image.
[0:34] And if I enter the tool, as you can see we have a Python states in Cops.
[0:39] I developed this user interface and you can undo, redo, everything should work just fine.
[0:45] So I'm just gonna quickly align this.
[0:48] And at the same time I can preview the output color correction as you can see this is
[0:52] real time.
[0:53] And I can connect in here, I can align it.
[0:57] And I can increase the sample area as you can see that will depend.
[1:01] And it's really sampling all those pixels and averaging them out.
[1:06] Can also change the, by default it will resample the image so by 30%.
[1:11] But I can increase it to one and still have a good feedback as you can see.
[1:15] It's a bit slower but I encourage you to done sample.
[1:18] It will help to blur a bit the colors and average them out.
[1:24] But anyways, there's an average algorithm built in.
[1:26] So you can see this is pretty good.
[1:29] So we went from the source image to this color corrected.
[1:34] And now I also have an output in here which is the color matrix.
[1:37] I'm just gonna exit the tool.
[1:40] And as you can see we have the output color correction but I can come in here and place
[1:44] an apply color matrix.
[1:47] And I'm gonna input, let's say I want to color correct now the full HDR.
[1:51] So I'm gonna connect the input image and the color matrix and it will color correct.
[1:56] As you can see and we should have the same colors.
[2:00] And let's say you want to revert back in any case so you can create yet another color matrix.
[2:09] And connect in this case the color corrected one.
[2:13] So you want now to invert the matrix.
[2:17] And now you come back to the original.
[2:20] So there's a way to do a round trip with this workflow.
[2:24] And yeah, there's nothing else much to it.
[2:28] So you have the usual controls and the color swatches.
[2:31] They are color corrected and by the fault this will work with ACCG.
[2:36] So you have to keep that in mind.
[2:38] So the colors match the ACCG workflow.
[2:41] As you can see that I'm using in here.
[2:44] And yeah, you can use these overlays to see how much the colors matched.
[2:49] In this case I have a weird perspective because this is from a let long and it might not
[2:54] align perfectly but it's working fine in any case.
[2:58] So yeah, then you can just apply the matrix to your other assets.
[3:01] Let's say footage or HDR is in this case and you can revert back with these invert
[3:07] matrix.
[3:09] So this is a tool that I'm going to share as part of the Patreon for these months.
[3:16] Instead of doing a tutorial I'm going to share these tools for the top tier Patreon supporters.
[3:22] And if you're not on Patreon I'm also going to make them available as a separate product
[3:28] that you can buy.
[3:29] So yeah, that's basically it will always be cheaper if you are part of the Patreon of
[3:33] course.
[3:34] So instead of doing a tutorial this month I'm going to share these tools.
[3:38] So this one is pretty simple, it's just apply matrix.
[3:40] This one is the one that has more work into it.
[3:45] And I can walk you through how I did all this setup.
[3:49] This involves quite a bit of a setup.
[3:51] So I started in subs where I did just an add note that is connected to the controllers.
[4:01] Then I'm calculating a matrix in here so I can show you that.
[4:06] So let me actually visualize it as an axis.
[4:09] So I'm just showing this because you might have interest in it.
[4:12] But anyways you can grab the tool right away and don't skip this part.
[4:16] So I'm calculating the matrix on both states.
[4:19] One, where is I just use the bound to get a pretty rectangular shape.
[4:24] Then I'm calculating the difference matrix and apply the matrix to this point so I can
[4:28] always deform the swatches.
[4:30] Then I'm loading a color chart of the color attribute.
[4:34] Make sure we set it to linear to have the ACG colors.
[4:38] So basically this chart I have in here as you can see.
[4:42] So yeah, after that we have the points with the colors and I can load that into sampling
[4:49] algorithm in here.
[4:52] As you can see and I can increase the radius of the sample and as you can see it will
[4:57] average out.
[4:59] There's a lot to it.
[5:01] Basically I'm iterating through all the points and getting the point position, getting the
[5:06] color and compare it to the sampled color.
[5:10] So there's some some complication to it.
[5:13] Then I'm calculating the matrix in here and I make sure I set it just one pixel by one
[5:18] pixel.
[5:19] This way it can be pretty responsive and in order to calculate the matrix we use the
[5:24] least squares algorithm.
[5:27] And as you can see it's not much, it's just a simple code and after that we apply the
[5:32] matrix which is just this bit of code and I'm also packing the matrix in three vectors.
[5:38] So I'm using the cable pack to output as a color matrix and that way I can use this
[5:44] apply color matrix which is just this code and yeah that's basically it.
[5:48] Then of course and I'm showing this because you can actually take these, take these tool
[5:55] and take it apart and learn from it.
[5:58] As you can see we have we have vexed in here a bit of vex so in order to calculate the
[6:06] up and tangent to apply the matrix.
[6:09] We have quite a bit of open CL, a lot of things that I've learned working on this tool, mostly
[6:15] about the atomic functions.
[6:18] And yeah.
[6:20] And we also have of course the Python states.
[6:28] Of course we are working on these images.
[6:30] We have of course these Python states where I'm doing the user interface and this is new
[6:36] to all the 21, these Python states for cops.
[6:41] So I can show you a bit of that so as you can see there's still a bit to it as you can
[6:47] see there's about 400 lines of codes.
[6:52] And again if there is any interest in this I might create a new video covering how I
[6:59] done this tool.
[7:00] I gave you a brief overview but yeah you can let me know if you want me to show you a detailed
[7:07] version of this because I think this is the area of identity that is pretty cool to explore
[7:12] and know about because you never know when you might need a custom tool to work on your
[7:18] project.
[7:19] So yeah guys I will leave you with that as always you can grab the tools if you are a
[7:23] patron supporter of the top tier where you get the tutorials this month you will get these
[7:26] two tools, these two HDAs.
[7:30] And yeah that's it guys thank you for watching I hope you have enjoyed and like my new tool
[7:37] I had a lot of fun doing it and learned a bunch and if you have any questions please
[7:42] leave them below and I'll see you next time.
[7:45] Happy new year!



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

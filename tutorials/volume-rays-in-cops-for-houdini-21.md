---
title: Volume rays in Cops for Houdini 21
source: YouTube
url: https://www.youtube.com/watch?v=nCS6sy53_aw
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/volume-rays-in-cops-for-houdini-21/
frame_count: 0
frame_status: pending-selection
---

# Volume rays in Cops for Houdini 21

**Source:** [YouTube](https://www.youtube.com/watch?v=nCS6sy53_aw)
**Author:** cgside
**Duration:** 6m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py volume-rays-in-cops-for-houdini-21 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in today's video I wanted to share a new tool that I've been working on called Volume
[0:06] Race.
[0:07] That basically selects the brightest areas of the image and creates these ray effect.
[0:11] You can interrupt in the viewport with a tool or you can manually place it by adjusting
[0:18] the center of set and you can easily animate this of feed.
[0:23] Let's frame between 1 and 45, between 0.3 and 0.06 and 0.3.
[0:34] Let's see, that works.
[0:37] So as you can see it will animate.
[0:38] Of course you can do a key framing because you have the easing options and it will look
[0:43] a bit better.
[0:44] But there's the option.
[0:46] There's also this option to do flickering that will add a noise to the source.
[0:51] And here I'm just ticking effect only if I want to multiply a noise or anything with
[0:57] the effect.
[0:59] And you can also animate in the offset of the noise.
[1:02] So at time multiply by 0.3, let's see.
[1:09] As you can see it will animate the flickering and it will create some nice effects.
[1:13] But again you can play with it.
[1:15] You have the viewport interaction.
[1:17] And you select the luminance range which is doing like a lumaki so we select the brightest
[1:22] areas of the image.
[1:23] You can also re-sample the image.
[1:25] So let's say by default is 0.3 but it will blur a bit the input so you can increase the
[1:30] resolution.
[1:31] Let's say 2.5.
[1:33] You have the iterations which internally this is just repeating the pixels along a direction.
[1:38] So you can increase more if you want but you also have the step scale which is a multiplier
[1:43] of that repetition.
[1:45] But again you start to see some art effects so it's better to decrease it.
[1:51] And you also have a decay that is just like a fading effect as you can see.
[1:58] Then you can have this option just to have the default volume raise and let me increase
[2:04] this.
[2:06] And you can add in here some flickering.
[2:09] And of course you will need to blend it a bit more.
[2:12] So what else?
[2:13] We have some contrast for the flickering.
[2:15] You can play with the noise element scale so you have bigger rays or smaller ones.
[2:21] Again the offset of the noise X and Y.
[2:23] Some contrast then you have some post effects like some blurring, the glow threshold where
[2:29] it starts, the glow brightness and of course the blending.
[2:32] And if you take effect only you don't have that blending option because you will need
[2:36] to manually blend it.
[2:39] So this tool is pretty fast even with animation.
[2:41] It's really a simple effect but it can add a lot of detail to your final renders.
[2:47] So this will work fine on slap comps and whatnot for doing basic compositing.
[2:52] Since now the need doesn't shift necessarily with these effects I thought that I would
[2:58] recreate it and share it for this month's Patreon.
[3:02] So this tool will be available for all the top tier Patreon supporters as part of the
[3:07] subscription.
[3:09] So basically sometimes I share a tutorial, other months I share a tool, this month I will
[3:13] share this tool for free with the Patreon supporters.
[3:16] And but if you are not part of Patreon you can still get it on my Patreon shop.
[3:21] Of course for patrons it will be cheaper.
[3:24] So yeah that's basically it's you can play with the settings and you have also the option
[3:30] to have different signatures.
[3:33] You can have RGB, mono or RGB.
[3:36] You can pick it depends on the input you feed it.
[3:39] It will automatically recognize.
[3:41] So I think I explain all the settings and yeah you can play with it and I hope you enjoy
[3:47] this tool and let me just give you a small update on another tool.
[3:53] So regarding the matrix color transform HDA I just added the UIscale multiplier that
[3:59] you can basically resize the handles.
[4:01] That's an ND feature.
[4:03] If you are zooming in or you have a smaller area to sample and as always you can sample
[4:12] the defined area and play with resolution of the image.
[4:16] But yeah basically if you zoom in a lot you can decrease this and have the desired handle
[4:22] size.
[4:23] Also I added a bit the code of the HDA basically before that I was starting with the shape.
[4:31] Then creating a bounce, creating a matrix as I shared and a different matrix and then
[4:36] apply that to the points that I'm creating by dividing the mesh into 24 sections and
[4:42] extracting the centroid and deforming.
[4:44] But I found a cheaper solution which basically involves again the same add and then do a
[4:50] bounce, sort the points, do some basic UVs from the bounding box and do the same on these
[4:55] sides.
[4:56] And then just generate a grid of points in this case I just generated them at the center
[5:01] and do an XYZ distance from that target position and then I can just attribute interpolate
[5:07] with the X-prem and the X-UV and you can basically play with it and it will have the exact
[5:13] same effect but much cheaper and less work because I was creating transform matrix and
[5:20] applying a different matrix which was just so much.
[5:24] In the years just simple we create a grid of points in this case six columns and four
[5:28] rows, create the column and row ID fitting to the scale of the input mesh.
[5:35] So I'm doing this by numbers 24 and I just create the point at the center because it will
[5:40] be cheaper, it will be a cheaper operation then I can just attribute interpolate and it
[5:44] will interpolate the position, the UVs and whatnot.
[5:47] So that's basically what I'm doing inside this matrix color transform so as you can see
[5:54] and just loading the colors and whatnot.
[5:57] It should be faster and it was already fast but this way it's even a bit faster.
[6:04] So yeah guys I hope you enjoyed the applet and grab the files on Patreon as always thank
[6:10] you so much for all the Patreon supporters and I hope you found this video helpful.
[6:14] I'll see you next time thank you.



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

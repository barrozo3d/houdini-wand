---
title: Karma and Solaris Tricks I wish I knew before
source: YouTube
url: https://www.youtube.com/watch?v=fbRhHne8x4E
author: cgside
ingested: 2026-07-30
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/karma-and-solaris-tricks-i-wish-i-knew-before/
frame_count: 0
frame_status: pending-selection
---

# Karma and Solaris Tricks I wish I knew before

**Source:** [YouTube](https://www.youtube.com/watch?v=fbRhHne8x4E)
**Author:** cgside
**Duration:** 6m13s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py karma-and-solaris-tricks-i-wish-i-knew-before <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Karma, Rainport, E2V, IntrinsicQV coordinates, UnV, X and Y, U-Inverted, Minimum Output, X and Y, MirrorEffect
[0:27] Y, Minimum Output, BOTH, 1 to 0, 1 to 1, SIGNASLIDER
[0:41] From here you can put it all together into an HDA and sell it on GANROTE.
[0:46] So in this one I want to show you how you can use a light to project textures in Solaris or using Karma.
[0:53] So as you can see I'm projecting a texture using this light.
[0:56] And of course you can set the contribution of the light of the diffuse and specular to 0 so it doesn't affect your scene.
[1:03] In this case I'm just using flat shading, but yeah.
[1:06] So you start with the light, you position it and then in a wrangle you can extract the local transform using the primitive path that you place in here.
[1:14] In this case I'm using light's light1 and then you set the prim var in this case I'm naming it X-Form and I'm saving that matrix which means that now in my light I should have a prim var called X-Form.
[1:33] No sorry, I'm targeting in here another primitive which is my mesh where I want to receive the projection.
[1:39] So if we come in here we should see somewhere, here it is, prim var X-Form.
[1:44] You can name it wherever you want.
[1:46] Then it comes the shading part which is a bit more complex, maybe there are easier ways but it's not that difficult.
[1:52] So we start with position, so this is just the position attribute in object space.
[2:00] Then we import the matrix in here with a prim var reader, so we import the X-Form that is in our mesh.
[2:06] Then we transform the position into the local space of the light by inverting the matrix and doing a transform matrix.
[2:15] So now the position attribute is on the light's local transform if that makes sense.
[2:22] And from here we just create a square mask by separating both the X and Y and manipulating it to a mask.
[2:34] So like this.
[2:36] And then of course this is projecting on both sides so what we can do is take the normal,
[2:41] do the same, extract the Z-axis of the matrix, the Z-component and do a dot product between that and the normal.
[2:49] So we get this sort of mask.
[2:52] Then we can tighten the mask with an if greater and finally multiply it with a square mask.
[2:58] And now we have a perfect mask for our texture sampling which we will do next by combining the X and Y components of the transform position.
[3:07] And then we just fit it to be on the correct spot.
[3:10] And if we sample the image, in this case I'm just using the default button fly, and then we can just mix it with another color in the background.
[3:19] And from there you can just place your light wherever you want and the projection will follow and works in XPU and also in CPU as you can see.
[3:28] Of course it won't work while in the viewport because we are dealing with matrices and what not.
[3:33] Well at least it doesn't work on my viewport but you can test it on your own.
[3:38] So this is just an excuse to not buy my texture projection tool so you can use this workflow.
[3:44] So this is how you can make your light look at any object in the thin, any hero object.
[3:49] So as you can see I have this light and I'm constraining it to my hero object which is the rubber toy.
[3:55] And I can place it on top, on bottom and move it around really easily.
[3:59] And the way I'm doing that, so I'm just importing the rubber toy, then I'm creating the light and I move it wherever I want.
[4:06] Then with the look at constraint I set my look at to the rubber toy and then my source to the light.
[4:12] So I'm just setting the source and the look at primitives or the target primitives.
[4:16] Then you can set the orientation, you can set the axis to look at, in this case minus Z, and then the up axis.
[4:24] And the up back is the Y axis. So I hope that makes sense.
[4:27] And then you just place your light wherever you want and that's how you can constrain the light to a hero object.
[4:34] So a quick tutorial to substance where I was painting some textures.
[4:38] And I was using the ACS workflow because you know, the NEI'm also using ACS and I want to render there.
[4:44] So in my project settings I started with the open color IO as color management and ACS 2.0.
[4:50] The other are the default ones.
[4:52] Then in order to, I was having some trouble where the color of the textures wouldn't match.
[4:57] So what I did in the end is when I export the textures I created a custom template and made sure I include, so...
[5:05] As you can see in here I didn't have the color space variable and you can enable those in here.
[5:11] So you can append and also if you're using Yudim workflow you want also to append the Yudim tag.
[5:17] So, but the most important is the color space because that will make sure we append the suffix called ACCG or RAW or any other sRGB or something like that.
[5:27] And when we export them and report them into Rodini, as you can see we have that tag.
[5:34] And if we go to color preferences, OCIO, as you can see any pattern that matches ACCG or sRGB or in this case RAW.
[5:46] We'll have the correct color space because this one in here doesn't seem to do anything.
[5:51] So you have to rely on the names on your textures on these tags.
[5:55] So that's how you can match your colors from substance into karma.
[6:00] So as always thank you for watching guys. These were the tips that I wanted to share today.
[6:04] I hope you have learned something new and you can grab the files on my Patreon also if you're interested.
[6:10] And yeah, thank you for watching and I'll see you next time.



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

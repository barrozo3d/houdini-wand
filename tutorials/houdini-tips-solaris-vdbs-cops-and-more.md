---
title: Houdini tips : Solaris, VDB's , COPS and More
source: YouTube
url: https://www.youtube.com/watch?v=WwwTwtlKm0A
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-tips-solaris-vdbs-cops-and-more/
frame_count: 0
frame_status: pending-selection
---

# Houdini tips : Solaris, VDB's , COPS and More

**Source:** [YouTube](https://www.youtube.com/watch?v=WwwTwtlKm0A)
**Author:** cgside
**Duration:** 7m35s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-tips-solaris-vdbs-cops-and-more <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back in this video I'll share a few tips from compositing to
[0:06] salaries and working with volumes and attributes. I believe you'll get away with
[0:12] something that you didn't know before. Hopefully. So the first one is on how to get
[0:20] these nice thumbnails on your layout asset gallery. As you can see they look
[0:26] just like the the renderer image. And the way you do that you set up your
[0:32] component builder and then in the component output you go to thumbnail and you
[0:41] choose render in this case I am using camera XPU and camera and scene I'm
[0:48] choosing the second inputs and I input a light a camera and the render settings.
[0:54] In this case I needed to increase the refraction limit so I can see well the
[0:59] glass. So that's basically it and now you have these nice thumbnails that you
[1:07] can layout as you can see that I'm doing in here. So now I have these geometry,
[1:20] these chocolates and I want to transfer an attribute while doing a VDB
[1:25] conversion. So as you can see I have the attribute in here called mask is for the
[1:31] interior of the chocolate and then I'm doing a conversion to VDB so I can
[1:40] smooth out the shape and I still have the attribute as you can see. And the way
[1:49] you do that is on your VDB from polygons your pass surface attribute in this
[1:56] case is called point dot mask and I give it a name then I do my VDB
[2:04] operations and use a attribute from volume connecting the second input to the
[2:10] volume and I just paste the attributes and give it a name. Keep in mind if you
[2:22] import these into salaries it will be a tree float so if you want to use it for
[2:30] shading you will need to separate them into different components to use as a
[2:36] mask. So I created these lemon slice from boolean as you can see in here I just
[2:48] have this geometry and boolean out sphere and I get something like this then
[2:57] I'm blasting one of them and creating a attribute with the group created from
[3:03] the boolean the groups and now I want to quad rematch it but you know we
[3:10] lose the attributes so what we can do is an attribute transfer but if I do it
[3:18] with default settings without the subdivision I get some weird results so what
[3:27] we can do is before the attribute transfer subdivide your geometry the more
[3:33] you subdivide or at least at until some points you'll get way better result and
[3:41] we can just attribute blur and we get the correct attributes then we can
[3:51] split it and do the UVs and we wind up with this more clean geometry so now a
[4:06] very quick tip on how to do vignetting in cops basically you create a let me
[4:15] start from scratch you create a ramp you'll get something like this then you
[4:22] have you need to set the same resolution as your input image so what we can do
[4:29] is to steal from the input image by connecting the input now we have the
[4:37] correct resolution and then you go to concentric and in this case I want to
[4:48] invert it so white and black and you can play with the interpolation this
[4:57] case I chose is out and then you can just that's what I have in here then you
[5:04] can just multiply over your render and you get the vignetting effect you can
[5:10] also play with the color of your ramp so you get more or less darkening so yeah
[5:21] that's basically it so I created this buff with valum with some collisions
[5:31] into the initial geometry and right here I am mixing between the valum result
[5:40] which is a bit all over the place and I'm using the the initial geometry before
[5:50] the valum simulation and mixing it mixing the position with the valum geometry
[5:59] and the way I'm doing that is just by in a point of op connect the valum geometry
[6:07] and input geometry and I also have an attribute in here called mask let's see
[6:15] that I'm creating with just an attribute creates and then blurring it by
[6:23] sampling the points of the spheres that I have on the object then I'm creating
[6:32] the mask and blurring it and then in the point of op let me just disable this
[6:39] in the point of op I am mixing between the first input position and the
[6:46] second input position and as a mixed factor I'm using that mask as you can see
[6:53] and I'm also playing with the falloff so I can get these effects these wrinkles but at the same time
[7:04] flattening the valum results as you can see is a bit too much so this way I can flatten
[7:15] these areas and keep the wrinkles so yeah guys that's basically it feel free to
[7:25] grab the files from my Patreon and thank you everyone that joined so far see you
[7:32] next time



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

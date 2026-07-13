---
title: Using Substance Designer nodes for Houdini
source: YouTube
url: https://www.youtube.com/watch?v=ObBXMX-VH90
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/using-substance-designer-nodes-for-houdini/
frame_count: 0
frame_status: pending-selection
---

# Using Substance Designer nodes for Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=ObBXMX-VH90)
**Author:** cgside
**Duration:** 8m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py using-substance-designer-nodes-for-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this video I wanted to show you how I used the
[0:05] new Substance Designer textures for our DNA by Powell Kaboosh to create this
[0:12] sort of rocky material and also combine it with the Pegasus nodes to create some
[0:20] textures. So from the beginning I'm starting with the shape from the circle, from
[0:29] the circle, then extruding it, exactly one unit to have the full range when I
[0:35] connect it to the Substance Designer texture, promoting the extrude front
[0:41] group and fusing and placing it on the positive X. So when I connect it it will
[0:53] be aligned with the Substance Designer texture. You can see if I have it as
[0:59] height, I will have this sort of shape but I want it as a grayscale. Then I have
[1:09] gradients with Substance Designer tile sampler and then I just blend it. We
[1:19] can move it to a minimum. Then using a tile sampler and here is where you
[1:28] will increase the repetition and play a lot with the offset random disorder and
[1:35] random amplitude and scale and also introduce some rotation. As you can see I
[1:44] have set it to input pattern and connected to the second input. Then just doing
[1:51] an auto-levels and I can show you how it looks. So if I connect it to the
[1:58] visualization node, the height visualization, this is the current setter. So doing
[2:07] an auto-levels, then I am wrapping a bit the texture and you can see what
[2:18] that is doing. Then doing a blend to carve a bit the shapes. So with a
[2:31] Berlin levels and doing a blend set to a minimum and you can see I can carve more or less.
[2:46] Then doing an overall rope as you can see by using a Berlin and in this case playing
[2:59] with the angle and in here I'm doing another plans to create the surface details
[3:12] by using a Voronoise set to crystal and a Berlin in a sloppler and then just
[3:22] blend it set to minimum and reducing the opacity to have these sorts of effects.
[3:28] Then just doing another sloppler in here to create even more variation let's say
[3:39] with a Berlin. So that's our id map. Now in order to use id field nodes since we are
[3:50] in a very small scale and a different orientation we will need to rotate this shape, this volume
[3:59] or this id field and scale it up quite a bit. So the default scale for the id field is about
[4:07] 1000. So in an id field transform I increase the scale to 1000 and rotate it minus 90 degrees.
[4:17] So in the end we will have something like this around 1000.
[4:24] And now we can use the new Pegasus nodes to load some diffuse and displacement textures and playing
[4:33] oops. And playing with the scale as you can see I love that this mega-scan texture.
[4:47] Then I'm introducing another one if I can show you if I disable the marks this is the
[4:55] the most texture I'm introducing in the cavities and for that I'm using a visualized with the
[5:02] faulty tinting and doing a night field mask by feature set to occlusion. And then I'm just
[5:12] blending the two materials as you can see. Then in order to have a proper range for the id map I
[5:22] am scaling it down again to a size of one. So as you can see I have a size of one
[5:35] and just doing a match size to have it on the center. And I can create a night field output
[5:45] save the texture. And in the channels I'm inputting the RGNB
[5:55] id fields or volumes as you can see for red RGNB. And for the alpha I can use the id so I can save
[6:08] in only one texture. So after you save to this it's pretty fast. In this case I used two K-map.
[6:19] And let's go to salaries. And if you render this I am just loading a simple
[6:29] quad sphere and this is the result of the material. In the texture I'm loading the texture as you
[6:38] can see. In this case I'm just repeating once. And then for the id or for the displacement I'm
[6:46] separating using a separate color for since this is a loaded color for for the alpha channel.
[6:56] And the id will be on the alpha so I'm connecting that to the displacement. If I disconnect it
[7:02] you can see we have no displacement. And for the color I'm just doing some basic color correction
[7:11] and loading also random normal map just to add some surface detail. Hopefully you can see it
[7:19] in the even with YouTube compression. So yeah guys feel free to download these new nodes from
[7:29] the link in the description. I will link the outer page on Github. And if you want this particular
[7:38] file you can also find it on my Patreon. And alongside with dozens of project files and
[7:48] some tutorials, some exclusive tutorials and also some courses in the Patreon shop.
[7:57] Thank you for watching and I'll see you next time.



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

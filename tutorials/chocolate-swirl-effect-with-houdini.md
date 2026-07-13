---
title: Chocolate Swirl Effect with Houdini
source: YouTube
url: https://www.youtube.com/watch?v=4PjTMogFWqQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/chocolate-swirl-effect-with-houdini/
frame_count: 0
frame_status: pending-selection
---

# Chocolate Swirl Effect with Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=4PjTMogFWqQ)
**Author:** cgside
**Duration:** 11m14s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py chocolate-swirl-effect-with-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm gonna be breaking down how I
[0:06] did the effects of this worldly shoplot candy. So yeah let's dive into it. So here's
[0:16] the final result. As you can see it's a very small network. So we're starting
[0:26] with a quartz sphere. Then I'm clipping it and feeling the polygons. Then I'm
[0:36] creating two masks along with a group expand. So here's the first mask and I'm
[0:42] blurring it. This mask is going to be used on a mountain as a blended attribute.
[0:50] Then I have a second mask. Mask 2. Then I'm also blurring and is being used as a
[1:00] displacement in a point verb. So just a display is along normal. Then in the
[1:06] mountain I'm creating this simple mountain and is being blended by that
[1:13] initial mask. So this mask in here. This one. So that's about it for the geometry
[1:24] operations. Now we're going to start with the PDVs. So I'm creating a PDV from
[1:33] polygons. And I'm doing a volume deform and when you create a volume deform it
[1:44] will automatically create this lattice from volume. And in here after the lattice
[1:52] from volume that creates all of these points I'm creating a wrangle to get
[1:59] the topmost point. So as you can see I have it in here. If this wants to
[2:07] collaborate. So right in here as you can see these points. And then I'm doing two
[2:21] soft transforms to create the swirl effect. As you can see this one is already
[2:27] creating it. So if I disable this one and look at this. So this takes a few seconds to
[2:36] cook. So as you can see I'm doing this soft transform by grabbing the top point
[2:42] that I selected that I grouped in here. And then I'm rotating it from that group
[2:50] center and playing with the soft radius. And then I have another one.
[2:59] And as you can see this one is a bit more intense just playing with the radius and rotation
[3:05] along the eye. And you get this sort of result which is really nice.
[3:11] And now I want to incorporate a tip in here. Let's call it a tip. So what I'm doing is creating a line
[3:23] and transforming the line to a line with the topmost point that I've saved in here.
[3:33] Re-sampling it to have more subdivisions. Then doing a rig wrangle as you can see.
[3:45] So deform into some sort of spiral. Then doing a second one to bend it a bit more. I could use
[3:56] the bend the former but it wasn't giving me the correct result. I had some interpolation issues
[4:07] when I combined two or more. So that's why I opted for the rig wrangle.
[4:15] Then I'm deleting some attributes and sweeping the shape as you can see.
[4:22] We will lose some detail but it's there anyways. So I'm filling it and placing it along
[4:35] the shape as you can see. This is a bit of manual work so I can color it red.
[4:44] Then I'm transferring a mask to the initial geometry.
[4:54] Let's just visualize the mask as you can see. Then creating a VDB from polygons
[5:03] and passing the mask that I'm going to use as a mask in the VDB smooth.
[5:09] I'm also creating a VDB from this shape and re-sampling the original shape to the same amount of
[5:22] the second VDB which is a bit higher. Then I'm doing a VDB combine. As you can see, but the
[5:33] the interpolation is not the best. As you can see we have these are transitions.
[5:39] So what we can do is do VDB smooths from that mask that we saved
[5:49] and we get these sort of results which is not perfect but it will do.
[5:57] Then I'm doing a convert VDB and saving it out. From here I can convert it to a quad mesh or
[6:11] a better quad mesh and then subdividing it and re-projecting to get the initial details as you can see.
[6:21] So from here that looks a bit jagged, all the edges a bit uncontrolled and then with the ray
[6:32] and a subdivision we get a more smooth surface. As you can see with this color. Hopefully you can see it
[6:42] even with the compression. Doing a slight blur on the position, softened the normals
[6:50] and it's ready to be sent to render. Then in here I'm creating the outer shell.
[7:03] There's nothing to complicate it. I just want to mention in here that I have a mask for
[7:11] the displacement that I'm going to use in shading and doing a UV project as polar which is also
[7:21] important. Let me just disable this mask and as you can see we have a polar projection of this shape
[7:30] that will allow us to have this stretched look around this shape in here. I will show you in shading
[7:43] in just a little bit. So this is our geometry. Let's move into the shading part.
[7:52] So as you can see by this rendering you can see the stretching that we get in here
[8:03] which is on purpose to have this look. The way I'm doing that is by using the UVs
[8:13] that were created using a polar projection as I told you. Then in here I am using a X-style texture,
[8:26] a Karma X-style texture. So in the UV mode not triplanar and I'm loading the texture coordinates
[8:35] and playing with the amount of repetitions of the UVs along the UVs.
[8:45] And from here I can mix it with the mask and remap it. This texture is just a random displacement
[8:56] that I found on Megascans. Remapping it and I can show you how it looks. Let's have a look.
[9:09] So as you can see in here the displacements of the inner chocolate. So I can show you node by nodes
[9:21] with these unlit and removing the displacements. Let's see if I change this to one and one.
[9:33] As you can see it will repeat with the same amount. If I change this let's say to six. As you
[9:46] can see it will stretch and it will do the circular pattern or the polar pattern because I did the UVs
[9:56] that way. So let's set it to default. So just loading the texture and mixing with the mask in here.
[10:07] As you can see this is the mask. This is the texture
[10:14] and then just mixing it. We end up with something like this.
[10:23] So let's load the final material. The rest is just a bit of subsurface scattering and some
[10:38] chocolate color. There's nothing to complicate it. You can have a look at the file on Patreon. I'm
[10:46] going to be uploading to there and if you have any questions you can also ask me there.
[10:54] So yeah that's about it guys. I hope you have learned something new. As always if you have any
[11:02] questions you can ask me over on Patreon or send me an email and let me know your thoughts in
[11:09] the comments below. Thank you and see you next time.



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

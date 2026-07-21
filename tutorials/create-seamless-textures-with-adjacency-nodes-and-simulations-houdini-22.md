---
title: Create Seamless Textures with Adjacency Nodes and Simulations | Houdini 22
source: YouTube
url: https://www.youtube.com/watch?v=XKpfGoQVvQY
author: Inside The Mind
ingested: 2026-07-20
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/create-seamless-textures-with-adjacency-nodes-and-simulations-houdini-22/
frame_count: 0
frame_status: pending-selection
---

# Create Seamless Textures with Adjacency Nodes and Simulations | Houdini 22

**Source:** [YouTube](https://www.youtube.com/watch?v=XKpfGoQVvQY)
**Author:** Inside The Mind
**Duration:** 9m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py create-seamless-textures-with-adjacency-nodes-and-simulations-houdini-22 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] One of the most exciting features in Houdini 22 for me at least
[0:03] is the ability to rasterize things that are on your mesh, whether they're attributes or whatever,
[0:10] and have them be seamless. So let's look at some of the new adjacency nodes that are in Houdini 22
[0:16] and how we can go about doing this.
[0:23] So I'm in a copnet here. I'm just going to start off. There's actually some
[0:27] like test geometry in here now. So we've got the pig head, we've got the rubber toy,
[0:32] we've got the shader ball, you know, Tommy, and we've got some of the different ones here.
[0:36] So we can start off with the rubber toy, I guess. And I'm actually going to scroll down
[0:44] over here and just disable this little button right here, which is going to turn off our UVs.
[0:50] So these have some things just by default on them. So we've got our geo, our base color,
[0:55] and our specular. So before in Houdini 21, we would do a rasterized setup.
[1:02] We would rasterize this into the UVs. Then we do rasterized geometry.
[1:10] And then we would pipe that into a fractal noise 3D with our position. So we'll do our position
[1:20] and wire that into our position here. And actually one of the other new things that are in
[1:25] Houdini 22, normally to preview this on a mesh in 21, we would need a preview material
[1:32] and we would have to wire this in. That's actually not needed anymore. We can just select this little
[1:38] box right here, which is the 3D output. And then we have this being displayed on whatever nodes that
[1:43] we have selected. So if I select anything else, fractal noise here, you know, we can preview
[1:52] any material on that. And if we want to swap back and forth between our 3D view and our 2D view,
[1:59] we can be in our network here and press X. And you can see that we switched back and forth.
[2:04] So a little hot key there to switch back and forth, which is pretty sweet. So looking here,
[2:10] this is how we would kind of try to do this before. And we would run into, you know, issues,
[2:17] we'd have to do some things to try to get this to clean up. Right. So this doesn't
[2:22] exactly work super well. But with Houdini 22, we have the new adjacency nodes. So we've got this
[2:30] geometry to adjacency. I can wire in our geometry into the geometry input here. And this is going
[2:36] to give us this little setup right here, which we can then wire into another adjacency node. So
[2:44] this time it'll be the attribute sample with adjacency. And we'll wire in this cable
[2:50] into our adjacency, which gives us a slightly different looking setup here. And then if I
[2:57] make a copy of this fractal noise, and wire this into our position here, preview this, press X here.
[3:03] And now you can see that we no longer have any of those seams. So we want from this
[3:10] to this, where we have these seams that have now disappeared. And this works for any geometry. So
[3:15] if I just type in like the pig head here, and wire that up here and set our flag there, you can see
[3:25] that we get the same thing there. Versus here, we've got some seams going on. So we get this nice
[3:33] seamless and this is not a seam, but it's just how the geometry looks. So one other thing that we
[3:40] can do if we do a soft geometry, or one other thing I guess I want to point out here, if I jump
[3:45] inside here, and we do like the test geometry of the head, the template head.
[3:54] If I do something like the measure node, and we set this to like points here,
[4:01] if I take a look at this, you can, which by the way, you can theme these out as well.
[4:09] It looks weird. I don't know why I did that kind of bugged out, I guess. But you can apply a theme
[4:14] to this as well. If you come up to edit and then preferences, this network editor option,
[4:20] there is a node info theme that you can change. And that'll change the theme for this one as well,
[4:26] which is kind of interesting. Just found that out today. But anyway, so if we take this and we
[4:32] set this instead of area, let's set this to curvature. And if we just re look at that,
[4:42] you can see that we have our curvature on this mesh. So let's go ahead and pop back up in our
[4:47] cop net here. Let's wire this into one of these geo two adjacencies, and this attribute sample.
[4:57] All right, this in here.
[5:01] And if we try to do this now with our fractal noise,
[5:06] if I preview this template head, and then I take a look at this, you're gonna see that we don't
[5:14] have this actually displaying on our mesh. So you can see that we've got this actually on
[5:20] our 2D view, but we don't have this displaying on our mesh. And the issue here is if I look at this
[5:25] and I come over to, if I select our geometry and I come over to our primitives, we have this
[5:31] material applied to this. So you have to actually delete that out. So if I do an attribute delete,
[5:36] and we delete that off of our primitives.
[5:42] Now you can see that we have this actually displaying on our mesh. And I can
[5:47] mess around with the amplitude here. And there we go. No seams or anything on this as well.
[5:54] Super, super nice with that. And then there is one other thing that we can do with this. So there
[5:59] are certain nodes that are going to be adjacency enabled. One of those is the reaction diffusion
[6:08] block. So if I take this adjacency right here, and we pipe this into the adjacency here, and just
[6:17] for fun, let's go ahead and wire in this noise to our activation here.
[6:29] If I look here, I can go ahead and press play.
[6:34] And we get this reaction diffusion across our mesh, and we don't have any seams here as well.
[6:40] So this does only work with nodes that have this adjacency faster in there. So like,
[6:46] unfortunately, the flow block is not one that has this. It only has that pass through. So
[6:53] we can't use the flow block. I'm looking into trying to figure out if there's a way that we can
[6:59] hack around that, but I haven't found it yet. There is the new ripple solver that has that,
[7:05] which we're not going to look at, but I'll just show you that it does exist on here.
[7:09] So there are some nodes that are adjacency enabled. So just keep an eye out for that.
[7:13] If you see that, then you can use this adjacency, and then we can use this to
[7:19] drive this reaction diffusion setup. And then we can also, if we take this
[7:25] attribute sample, I'll just make a copy of this one actually. And instead of
[7:30] doing our position here, we have that curvature on our geometry. So if we come back to our points
[7:37] here, we have this curvature. So if we want that curvature actually on, or to be used in
[7:43] SOPs or in COPS, then we can just type in curvature here.
[7:50] And it's going to give me an error. So if you pop this open,
[7:54] seems like there's some issue with the new node info. But there is an error that pops up here.
[8:01] It's trying to think that this is a float three. So if we set this to mono, then we get this
[8:06] that is popping up, which is basically exactly what it looked like inside of
[8:15] SOPs here. So if we went from that,
[8:19] oops, to this here in COPS. Pretty cool stuff. Just turn, I wonder if that still displays
[8:29] if you hop up, it does. So you can see that's what we get here. So pretty interesting stuff.
[8:36] So you can play around with this and get some interesting results. There's also a couple of
[8:42] other adjacency nodes, which I will take a look at in the future, but I just wanted to cover this
[8:47] because this is kind of the bare essentials to get started with the adjacency. So play around with it,
[8:53] have some fun, and hopefully this has helped you out. Thank you guys for watching. I will be doing
[8:58] a bunch more videos on who you're going to. So if you want to learn more about some of the new features,
[9:04] definitely stick around and keep an eye out for those. But anyways, thank you guys for watching
[9:08] and have a good day.



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

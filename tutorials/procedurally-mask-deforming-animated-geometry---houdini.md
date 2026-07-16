---
title: Procedurally mask deforming / animated geometry - Houdini
source: YouTube
url: https://www.youtube.com/watch?v=UL-VdOBmXgE
author: the point and prim
ingested: 2026-07-16
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedurally-mask-deforming-animated-geometry---houdini/
frame_count: 0
frame_status: pending-selection
---

# Procedurally mask deforming / animated geometry - Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=UL-VdOBmXgE)
**Author:** the point and prim
**Duration:** 8m57s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedurally-mask-deforming-animated-geometry---houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone, and sorry for the long absence. In this video we are continuing with smooth
[0:08] function masks. We are going to expand on the last video's method, so if you haven't
[0:12] seen it, you'll find the link below. We are now going to go through how to apply this
[0:16] effect to curved and deforming surfaces from any and multiple angles. If you want this
[0:21] hip file, grab it on Gumrood. If you downloaded the last one already, the product has been updated
[0:25] to contain this project as well. Link in the description. I am just starting off here
[0:28] with this model that has been subdivided and remest, so that is comprised of triangles.
[0:33] One quick tip is that the USD Import node tries to re-import on every frame, so make sure
[0:38] to set it to a static number, or it will attempt to cook the entire tree every frame. The key
[0:43] node for this effect is the distance along geometry node. Let's wire that up, manually select
[0:48] some start points temporarily, and visualize the output disk attribute. So what is actually
[0:52] happening here? The Docs definition reads as, measures the distance of the shortest path
[0:57] along the geometry's edges or surfaces from each start point. What does that even mean?
[1:02] Why can't I just use some basic vector maths or point cloud functions like attribute transfer?
[1:06] And the answer is simple. Simply measuring the distance between points or using point
[1:10] clouds like attribute transfer, both work entirely by measuring distance in world space,
[1:15] regardless of the connectivity or topology of the geometry. Distance along geometry respects
[1:19] these aspects, and that's why he can see how the attribute visualizer flows along the
[1:23] contours of the geometry. Back in the example, let's visualize our disk attribute. Our main
[1:28] problem now is that the attribute is not mapped between 0 and 1, as it returns the exact
[1:32] values that are measured along the geo. In this case, the attribute is mapped between
[1:35] 0 and roughly 0.6. In order to work with the smooth function easily, we will have to
[1:40] remap this between 0 and 1. A simple way to do this is to use an attribute promote, set
[1:45] to detail and maximum. Then we drop down a point for and wire it into the second input.
[1:50] Let's just clean this stuff up and bind in the disk attribute from the first input.
[1:54] Then we will want an import detail up to get the promoted disk attribute from the second
[1:57] input, and then a fit range with the promoted attribute piped into the source max, and we
[2:01] can bind up the new normalize data. That's now fit nicely between 0 and 1.
[2:07] Let's grab the visualizer again. We can see the full heat map is now visible. If that
[2:11] doesn't make sense, we have our disk attribute and the ramp is mapped between 0 and 1, but
[2:15] the disk attribute only occupies the range between 0 and around 0.6, which doesn't encompass
[2:19] the full range of the ramp. All we did with the promoted attribute is push the new maximum
[2:23] up to 1, remap in the attribute to a full 0 to 1 range. We won't get as complex with
[2:27] the smooth function remap this time as we covered it in the previous video. If any of
[2:32] this doesn't make sense, check that out first. I am just piping in the new disk attribute
[2:36] and exposing a parameter that I will animate. This time I am adding with an exposed parameter
[2:41] that I will name with that will let me control a softer looking fall off.
[2:46] As done previously, in order to break up the uniform band, I am just going to add some
[2:50] noise to the min value which will distort the edge. You probably already know this, but
[2:56] a nice way to get more interesting noise patterns is to use a different noise on the input
[2:59] position of your main noise. I am leaving it quite basic in this demo, but play around
[3:03] with stacking a bunch of them together and you can get some pretty nice results. One of
[3:07] the great advantages of this method is that you can change where the mask spreads from
[3:10] simply by changing the selection of the start points, allowing for easy art direction.
[3:15] This will work in multiple start points and from any angle as long as the geometry is
[3:18] connected. One of my favourite ways to proceduralize this is to set an ID on the points and then
[3:25] sort them randomly and blast out a range of them. Then I set a group with an on creative
[3:33] name such as start and copy that back into the main stream setting ID in the match by
[3:37] attribute field. If we turn on the group visualizer, we can see that the points have copied
[3:41] over in their exact locations from the second stream, which you can see here when we turn
[3:45] on the disks as well. If we come down to our distance along geometry node and replace
[3:49] the manual selection with the start group, you can see that the heat map interpolates
[3:53] between all of these start points. And of course, the animated mask will then work with
[3:56] our new start group. There is another important concept that we need to talk about and that
[4:00] is applying this to animated deforming geometry as the order of operations is important to
[4:04] maintain performance. So what I'm doing here is just making a grid and remashing it until
[4:10] we reach about a million points so that we can see a visible difference in terms of speed.
[4:15] Now let's just grab the nodes from the other example and paste them onto our new geo.
[4:19] Everything is working as intended as we have proceduralized the start group. We need
[4:23] some defamation to demonstrate this, so let's just put down a twist node and set a couple
[4:27] of keyframes. Everything is working fine until we go down to our distance along geometry
[4:31] node and let the timeline scrub. This footage is sped up by 300% and look how slow it is.
[4:37] This is because the node is performing quite an expensive calculation on every frame.
[4:41] The solution for this is to calculate the disk attribute only once and then copy the
[4:45] attribute onto the animated stream, which can be done easily here by just repositioning
[4:49] the twist node. As you can see, we instantly get our real time playback again. I'm just
[4:54] setting two keyframes on the mask parameter to match those from the twist. And the effect
[4:59] works nicely synced up now. The only issue is the noise button buzzing and that is caused
[5:03] by the noise swimming through world space. And of course, that is easily solved by setting
[5:07] a rest attribute before the animation and then using that to drive the noise instead of
[5:10] P. If we play the animation now, the buzzing issue has been rectified. We will now do a surface
[5:16] level walkthrough of this project to see how flexible this technique is. As with the last
[5:21] video, this will contain some more advanced techniques that I won't go through in depth
[5:24] here, so I encourage you to grab the hip file if you want to explore further.
[5:29] I start off with a circle animated with dollar F. This is all I'm using to get the flow
[5:33] effect along the curves. Then I just give it a 180 twist, rotate it, and merge the copies
[5:38] together. Here I am just applying a subtle animated noise and sweeping the curves into
[5:42] several rows. I apply another noise which is offset by each curve and sweep the curves
[5:47] again with a square profile. I am using connectivity to get a class attribute for the curves, which
[5:53] will be needed in the next steps. So now I am using a single frame of both the swept geometry
[5:58] and its original curves. The latter is assigned a group as I will need to split in the loop
[6:02] below. So we are looping over each of the curves according to the class attribute from
[6:06] before. It is hard to see in the wireframe, but essentially we have two streams now. The
[6:10] polygonal data and the original curve. I am creating the scale geometry by using a few
[6:15] tricks such as divide with compute dual and a primitive soft to scale each prime separately,
[6:21] and just extruding the pieces. I am setting rest here as we will need it for noise later,
[6:25] like the demonstration before. Over here I set the start group to an arbitrarily selected
[6:30] point number, and pipe that into a distance long geometry node, which I will attribute
[6:35] transfer to the scales geo. Now the stream that contains the curve, I am using this for
[6:40] one purpose mainly, and that is to open a point cloud where I will fill to P and use that
[6:44] to calculate a vector that is pointing away from the center of the curve. The last line
[6:48] is just retrieving the class attribute from the curve as I did replace it with a separate
[6:52] class attribute that I didn't actually end up using. So after we let this run over each
[6:57] piece, we have our original class attribute, the dist attribute, by directionally mapped
[7:01] along the length of each curve, as well as this vector attribute for displacement. Something
[7:05] to note is that I am fully aware that I am able to do this sort of thing with some clever
[7:09] manipulation of attributes along tangent U, but I have decided to save that for a future
[7:13] video as is another topic on its own. So now I simply apply this move function mask
[7:18] via the dist attribute. This is almost completely identical to what we did in the demonstration
[7:22] before, except I have some random offset via the class attribute, and I am just controlling
[7:26] the mask width inside the point bump. After that, it is simply a case of point forming
[7:30] the geometry using the animated swept curves from before. Important to note is that I am
[7:35] using the class attribute in the point forms that each curve deforms individually. This
[7:39] is the bulk of the work and the slowest calculation, so I pack the geometry and write it to
[7:43] disk. I calculate the velocity and then remove all points that have a color value less than
[7:47] 0.1. In this wrangle, I am applying some displacement based off of the direction vector I created
[7:52] earlier. I actually did an account for the fact that I deformed the geometry but did not
[7:57] update the attribute to match, which caused this shearing effect instead of the scales
[8:00] moving directly outwards, but I opted to keep it as I thought it looked interesting.
[8:04] The final point for up down here is a bit of noise break up, which uses rest like in
[8:08] the example, so that it doesn't swing through world space as the geomobes. I am not going
[8:12] to talk about the particle sim as it is out of scope of the video. It is a modified
[8:16] vex version of a technique featured by Simon Fiedler and the fantastic antagonist team,
[8:20] who explained the concept perfectly. I will link the video in the description. If you
[8:24] want to have a look at the rendering setup or study the effects setup further, please
[8:27] do grab the hip file. As mentioned in the intro, if you already have access to this product,
[8:31] I have updated it to now contain this project too. Please note that I have now set a suggested
[8:36] price of $10 as I have been completely consumed by greed, but you can still get it for free
[8:40] by just replacing it with a zero. That wraps up this chapter on smooth function masks.
[8:44] I hope you got some useful information out of these videos. Thanks so much for watching
[8:48] and see you in the next one.



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

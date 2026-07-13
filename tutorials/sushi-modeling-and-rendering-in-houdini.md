---
title: Sushi Modeling and Rendering in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=c1tO7581nOM
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/sushi-modeling-and-rendering-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Sushi Modeling and Rendering in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=c1tO7581nOM)
**Author:** cgside
**Duration:** 17m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py sushi-modeling-and-rendering-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this video I'm gonna be breaking down how I did this sushi shot
[0:07] We will be focusing more on the subs part and
[0:12] if you're interested in the
[0:15] File itself you can find it on my patreon. So let's get started
[0:22] So here's the final geometry and some UVs
[0:27] Let's start from the beginning. So first I'm going to model the rice and
[0:36] For that I'm starting with the line and then sweep it
[0:40] with
[0:43] With some scaling along the curve. So
[0:47] ticker in the middle and also I'm using the end cap type as grid
[0:54] To add this round part
[0:57] But as you can see this is too uniform. So I'm doing a bend
[1:03] But now I want this part to be flat so for that I'm creating a mask on
[1:10] the bounding box
[1:12] as you can see in here bounding box and
[1:17] Set to X and then I'm just blending both shapes
[1:21] So the banded one and this straight one with a large function as you can see and
[1:29] then you can play with this
[1:33] Mask in here
[1:36] So then I'm subdividing and using the quad remasher to have a better topology
[1:46] That will smooth nicer because right here we have this pole
[1:52] which can cause some issues
[1:55] So I'm just doing a quad remasher and if we feed the sort of geometry to a valum sim
[2:03] It will be a bit too slow. It will be a bit slow
[2:08] So for that I'm doing a poly reduce at 50%
[2:12] to have some proxy shape and
[2:15] I'm also grouping the eye poly. It's not really eye poly but I call it eye poly
[2:22] then I'm merging both and
[2:24] From here, I'm just creating the sushi part the
[2:30] the shape for the rice and
[2:33] I'm doing that with a circle then clipping and adding some thickness
[2:39] removing the bottom primitive and
[2:43] Beveling it to have this sort of shape
[2:46] which I will then
[2:49] scatter some points and
[2:51] Randomize the normals in this case just set to inside sphere
[2:58] Then I'm animating the p-scales you can see from frame 1 to frame 12 from point 15 to 1 and
[3:07] I'm also doing some random scale in here and
[3:12] Creating a connectivity attribute which is pretty important to replace the low poly version later
[3:19] As you can see this is the result of the copy to points with the animated p-scale
[3:27] After the copy to points I'm splitting the
[3:32] low poly geometry to feed to the valum sim and
[3:37] And
[3:40] In here I add colliders so from this initial shape I'm filling the polygons adding a normal
[3:48] then
[3:50] extruding these outs and
[3:52] extruding this one in and this will be the bounce of our
[3:58] This will be the collision geometry
[4:02] so I'm also
[4:05] remaching and applying some noise so we don't have a very uniform distribution and
[4:15] So this is our colliders and we have to as you can see they are all intersecting so we will use a valum sim to
[4:24] Salted for that. I'm creating on the geometry a valum shape match
[4:30] Just default settings set the valum constraints to shape match and then in the valum solver
[4:42] Oops
[4:47] Place it on the frame one in the valum solver
[4:51] Inside I have a valum resplend loading at each substep the
[4:56] animation of the rice so this null in here after the copy to points and
[5:05] If we check how this is going
[5:12] Might be a bit solving the beginning, but it's just from frame one to frame 12
[5:18] So
[5:20] As you can see it's growing and it will avoid intersections and at the end you will have something like this
[5:29] Which is intersection free
[5:33] So just run the sim for 12 frames and then
[5:37] Use a valum I owe to cash the last frame and
[5:42] Here is where we replace the
[5:46] Let's call it iPoly by the law poly so as you can see
[5:52] We replace the
[5:55] geometry and we do that by loading in from this split
[6:00] the iPoly and time shifted to frame 12 which is where the
[6:06] The grains are the rice is fully grown and
[6:10] Then we use a valum transform pieces and use the piece attribute class which is the one that we saved in here and
[6:20] Then we just replace using the valum geometry and the valum constraints
[6:27] This is similar to the transform pieces, but it's
[6:32] Unique to shape match constraints
[6:35] Then we just delete the attributes we don't need and
[6:40] In here I am
[6:43] I think the empty spots with this interior shape
[6:48] Because we might have some holes in here that
[6:54] Will not work so we just use this shape and merge it over the rice or under the rice
[7:04] So now we will make quickly the sushi so for that I'm loading this shape and
[7:11] Lacing the bottom primitive and subdivided quite a bit so when the geometry rests rests on
[7:19] On here it will be quite smooth
[7:25] So for that's from the rice I'm extracting a bound as a rectangle as you can see and
[7:33] And rolling it a bit
[7:35] then doing some remesh and
[7:39] Running the using a valum cloth as you can see this is a these are my values which is
[7:47] basically the fault settings and
[7:50] Running the same as you can see
[7:57] And then I'm time shifting
[8:00] on print
[8:03] 30 then quad remesh in it
[8:08] Which for this sort of shape the the Aldini quad remesh is pretty good
[8:14] Then creating a rest attributes and flattening the shape
[8:21] And in here I'm just creating a mask
[8:25] With the distance along geometry
[8:27] So I can have thicker in the middle and
[8:34] And a thinner at the edges
[8:37] We will do that in a bit, but for now I'm doing a mountain along the peak
[8:41] so I can create these jagged edges and
[8:46] Then just point the forming again to the shape
[8:51] Then I can pick it a little bit and do two exusions
[8:57] So one thicker and one thinner and then just blending them with that mask and we will get something like this
[9:11] Then I'm doing some babbling in here to have these edges
[9:18] Sharp and not very smooth
[9:22] so
[9:24] We will subdividing here and you can see we will have a sharper transition
[9:30] Instead of this rounded look
[9:34] And for the UVs I'm just saving the extrude back group
[9:39] And doing a group from attribute boundary on that specific group
[9:44] And then use that in the UV flatten as a sims group
[9:48] And it will work pretty well as you can see
[9:53] Just default settings and that's it
[9:56] Then subdividing adding the normal and
[10:00] adding the name attributes
[10:03] For both pieces and we have the sushi done
[10:09] From here
[10:11] We can create some random random rise
[10:15] We can add some random rise on the floor
[10:19] And also create some chopsticks and place them around the scene
[10:26] And this is our final result from the modeling part
[10:34] So I'm gonna be showing you the materials so for that
[10:39] I'm gonna disable a few of these things like the table, the chopsticks
[10:46] And the rice and let's focus on these material first
[10:52] The salmon material
[10:55] So let's load that as a render
[10:59] And as you can see it's pretty simple
[11:01] I'm just loading a PBR material
[11:05] PBR set of textures that I found online
[11:09] And using the place to denotes
[11:13] To scale as you can see
[11:17] I can scale the texture
[11:21] Because by default it will be something like this
[11:26] As you can see
[11:28] And I just scaled it
[11:31] And I can show you I did some color correction in here
[11:38] So defaults to this
[11:41] And I did not do color correction in here actually
[11:46] So this is our roughness
[11:49] And here is the translucency which I did some airy color correction
[11:58] And then we have the normal which is just a bumpy little texture
[12:05] And for the displacement which is where I could a bit more work
[12:14] Which doesn't allow me to show you exactly
[12:18] Because it's not connected to the shader
[12:21] So we can do this surface and lat
[12:27] And
[12:28] So this is the default displacement texture that comes with it
[12:36] Then I'm inverting because I want these parts to go in and these go out
[12:45] Then I'm remapping to minus 0.5 and 0.5 since this is
[12:54] The default value for this texture is around 0.5 just like mega scans
[13:04] And then I'm loading this mask texture if you remember from the edges
[13:11] And I'm multiplying with the displacement after the remap
[13:18] So I can have
[13:21] Plast displacement or no displacement around the edges
[13:27] But you don't have to do that it's just something I did
[13:33] And that's basically the textures
[13:38] And for the shader I'm just using quite
[13:44] Glossy material
[13:47] And a lot of subsurface and the scale around 0.02
[13:54] If I remove this subsurface
[13:58] You can see it will look very flat
[14:05] And let's focus now on the rice
[14:09] Which will be a bit more slow
[14:20] So maybe we can focus here on an area
[14:26] So the rice material
[14:29] Let's see
[14:32] I'm loading first the texture as you can see
[14:36] Then I'm playing with the range with the material X range
[14:44] And then I'm mixing two colors
[14:46] One slightly darker
[14:49] And one more white
[14:54] And I'm using that both as a base color
[14:58] And the subsurface color and radius
[15:02] And these are my subsurface and scale settings
[15:08] And
[15:12] As you can see
[15:14] We have this sort of
[15:17] Of translucent low-con the rice
[15:22] And the roughness is around 0.1
[15:26] I noticed that it's pretty glossy
[15:30] And I also have some bump if I can show you
[15:33] I will do a small render
[15:36] And
[15:40] And pause the recording
[15:43] Or I can just show you in here
[15:45] As you can see
[15:46] I'll translucent the end specular
[15:50] The material is
[15:52] And if you notice here you can start to see some of the bumpiness
[15:57] That you get typically on the rice
[16:02] So apart from that
[16:04] We have the shopsticks
[16:08] And the table which is just
[16:12] A default material so nothing to show you in here
[16:16] And also we have the lighting
[16:20] So I can show you the lights
[16:23] We have a
[16:27] A dome light which with a very small intensity
[16:30] Just to add some ambience
[16:32] And a top light
[16:34] Here a front and a back light
[16:39] That's about it
[16:41] And render settings
[16:44] I am just changing it to 512
[16:47] XPU
[16:48] As always
[16:50] Increasing a bit the SSS limit on the rice
[17:00] And
[17:02] I am also using the Audin Denoiser
[17:07] So that's about it guys
[17:09] Hopefully you picked up some tips
[17:13] And you can download the full scene on my Patreon
[17:18] Let me know if you guys enjoyed this one
[17:21] And I'll see you next time
[17:23] Bye



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

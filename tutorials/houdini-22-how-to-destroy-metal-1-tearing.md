---
title: Houdini 22 | How to Destroy Metal | 1 | Tearing
source: YouTube
url: https://www.youtube.com/watch?v=x-N5I4XS7Q4
author: Houdini
ingested: 2026-07-18
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-22-how-to-destroy-metal-1-tearing/
frame_count: 0
frame_status: pending-selection
---

# Houdini 22 | How to Destroy Metal | 1 | Tearing

**Source:** [YouTube](https://www.youtube.com/watch?v=x-N5I4XS7Q4)
**Author:** Houdini
**Duration:** 15m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-22-how-to-destroy-metal-1-tearing <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this tutorial, you will learn how to use the new metal destruction workflows in Fudini
[0:09] 22.
[0:11] You can follow along by opening up the RBD Metal Start01 file and then we can just jump
[0:18] into the Jumperger container and in here you would find the Garage Jumperry and also I
[0:26] have the animated crag that I transformed and retimed so it basically aligns with the
[0:33] door and it will help us in our destruction demonstration.
[0:39] So in this Garage file you would find some groups so we are going to isolate the metal
[0:47] door. Let's press Tab and type Split and in here in the group I'm going to choose Metal
[0:59] Door. So now we have Metal Door that we can fracture. Let's press Tab and type RBD
[1:06] Material fracture and we are going to connect it after the split. So basically I'm going
[1:16] to put this to Manual and we are going to change the Material type to Metal and if we go
[1:25] to Fracture you can see that it is going to scatter 100 points. Right now I am in
[1:31] Manual mode so nothing is updating. So for now I'm just going to drop this value down
[1:37] to 50 points. We don't really need that many and I'm going to put the Display Flag to
[1:42] RBD Material fracture and set it to Auto Update. We should see our fragments. I can press
[1:50] W on the keyboard to see the fragments. After this step once you are happy with the initial
[2:00] amount of fragments we can go to Details tab and we can adjust some of the Edge details.
[2:07] Again if I'm going to be changing these values it's going to start updating as soon as
[2:13] I stop clicking so I usually go to Manual mode. I set this to some lower detail size
[2:20] to get more subdivisions, maybe a higher noise height and I'm going to change the Elements
[2:25] to 215 and now if we watch closely I'm going to go to Auto Update. I'm going to have more
[2:34] details along the edges. There we go. Now you can see we have more details. So after this
[2:46] step we can basically inspect how the constraints are built. So right now we have two types of
[2:53] constraints. One is glue which would be the initial constraint and then after the glue
[3:00] breaks we would have the soft constraint that would basically mimic the bending behavior
[3:08] on the metallic pieces. By default usually these constraints are set a little bit too high
[3:16] so I usually like to lower the glue strength to something like maybe a thousand and we
[3:25] can basically proceed with setting up some of the additional simulation parameters. Let's
[3:32] press Tab and type RBD configure and we can connect all three inputs to the RBD configure
[3:44] and what I usually want to do is I don't want to have this whole section as active piece. I want
[3:51] to basically pin it on the top part and on the sides so we can turn on active attribute
[4:01] and then use bounds. Basically you can use a bounding box that you can just press Tab
[4:07] Bounds and then you can plug it into this last input or you can also use the built-in
[4:16] bounding geometry. So if you go to Bounds change this to bounding box you would see this red
[4:20] bounding box and we can actually interactively change this in the viewport to capture the area
[4:28] that we want to be active. Change this. Alright so I actually have some values that worked pretty
[4:39] well with this demonstration. I'm going to put them in here. So I took 0.7, 1.35 and 4.72. Just so we're all
[4:51] using the same setup. And then what is also quite important and can change how your simulation looks
[5:04] is this physical attribute. So if you're simulating metal it would make sense to change this to
[5:09] metal and also we can change the type and this will adjust the density parameter and believe it
[5:16] or not this could actually change the look of your simulation and how heavy the metal is and how
[5:21] easily it bends. We're now I'm going to change this to aluminum and basically we can proceed with
[5:28] the simulation. So I'm going to press Tab and type Rdb Bullet Solver and let's connect our high
[5:37] res, let's connect our constraints and let's connect our proxy geometry. And if I press play
[5:47] you can see everything is standing still because we pinned the top. I'm going to go to the Collision
[5:56] tab and I'm going to turn on ground plane so we have infinite ground and lastly for this to work
[6:04] we are going to connect our crack character to the collision geometry input.
[6:12] Okay let's press play and see what we have. So basically we are getting the hammer
[6:22] destroying these fragments but they are not actually flying away. So if you take a look at
[6:30] the constraints tab the pieces wouldn't be able to detach unless the distance is higher than
[6:44] this value and we can basically lower this to something like 0.1 and let's go to the first frame and
[6:53] do another approximation. So now you can see we're getting a much better behavior the fragments
[7:00] actually able to be detached and we are getting this interesting shape as a result. But this is not
[7:11] really the final look in order for this to work. We need to add an additional node which is called
[7:17] RBD deform pieces. So let's plug all three here. And as you can see this also doesn't look
[7:29] amazing because it is trying to keep all the fragments together. This would work great if you
[7:34] just want to have some kind of denting without allowing the pieces to be detached but if we change
[7:42] this boundary connection from cluster attribute to constraints now you can see we are getting quite
[7:48] an interesting shape in here. Alright let's make a quick preview of what we have. So I'm going to
[7:57] zoom out. Let's press control shift onto the template flag so we can see the crack character
[8:04] and there is actually a camera here that you can use for your flip books. So I'm going to give
[8:10] myself a little bit more room and I'm going to click and hold onto the flip book with new settings
[8:17] and I'm going to hit start and I'm going to pause the video and come back. Alright we are back and
[8:23] let's check our result. So overall everything is working but the metal is a little bit too jiggly
[8:31] and springy and we can actually control this with a dampening parameter. Okay so let's go back and
[8:41] in the RBD material fracture we can adjust some of the constraints properties to make this look
[8:50] much more stable. Okay so usually what you can do you can increase the dampening ratio. I'm going
[8:58] to multiply this by 4000 so we get this value and I'm also going to reduce the angular dampening
[9:09] because I actually want this to be bent more outwards and I'm also going to reduce the
[9:15] angular stiffness. So we basically want more bend but we want to stable behavior so it kind of
[9:21] bends out fast and then freezes with this dampening ratio. Sometimes reducing the glue strength
[9:28] can also help getting more fragments to be detached or dented in words. Alright so let's now do
[9:38] another flipbook. I'm going to take the second out from this press tab type null and I'm going to
[9:47] hold control shift and click on the template flag so we have more or less similar view and let's do
[9:54] another flipbook and I'm going to pause the video and come back. Alright let's check our result.
[10:04] So now you can see we are getting a much more stable metal tearing and also we're getting a much
[10:11] nicer shapes. They're basically kind of bent outward and freeze into this interesting form.
[10:17] Okay now let's take a look at one more setting that can change how your metal behaves
[10:24] when it's getting destroyed. So in the RBD material fracture you've probably noticed that
[10:31] we are operating at a complete thin surface so let me just press the template flag onto this one.
[10:39] So you can see that this is not extruded thick geometry. So this is completely thin surface and
[10:50] RBD material fracture under the metal can actually do a really nice job.
[10:57] But what if you want to have a thicker metallic wall? Right so let's mimic that scenario. Press tab and
[11:04] type holy extrude. Okay let's connect the output of the thin door. Press the display on
[11:14] poly extrude and we're just going to use the transform extruded front and set it to minus 0.01
[11:22] and we also need to make sure the output back is on. Okay let's make sure we have
[11:30] reverse text normals and then we need to reverse them. So let's put down reverse.
[11:39] Okay we need to add another normal node.
[11:44] So it looks correct. Alright let's set this to 10. Alright so now we have our
[11:52] surface. So let's now put another RBD material fracture. I can actually copy this first one.
[11:59] So let me go to manual mode. So we don't wait. So control C, control V.
[12:08] And let's take a look at this one. So I'm going to go back from manual to our update.
[12:14] So you can see there's some kind of remaching and stuff. I'm going to quickly hit escape.
[12:24] And I'm going to change this to solid. And I'm probably going to give it less fragments.
[12:31] So we don't need 50. I'm going to set it to 10. And let's wait.
[12:37] Okay let's press W. So you can see we still have all the fragments. If I put the exploded
[12:50] view, you can see these are now thicker metallic fragments. Okay and everything is pretty much
[13:00] the same with the constraints. We just reduce the amount of pieces. You can probably also reduce
[13:06] the detail size because this is going to be a little bit slower. It has to add extra details on
[13:14] the thicker surface. So something like this should work quite nicely. And after this one, we can
[13:22] basically proceed with our setup. I'm actually going to copy some of these nodes. So we can just
[13:29] reuse this whole setup. I'm going to select these nodes from our first one. Control C,
[13:34] and show V. And let's just connect these. Okay now we have the same RBD configure.
[13:49] Everything is pretty much the same. The metal is aluminum. And let's see how this is going
[13:58] to behave. Let's put the camera and let's press this clip flag on RBD.
[14:06] The form, I'm going to maybe even just merge these together with the crag.
[14:19] Okay and let's do a flip book. Let's see how this looks.
[14:28] Okay, let's check out the result. So you can see the fragments are a little bit more stiff
[14:36] and not all of them are breaking it as easily. So we can probably go ahead and adjust some of the
[14:44] constraints. So you can see the glue is set to 1000. I'm going to set it to 100. Basically to allow
[14:51] more of the fragments to break away. And let's do another flip book and check it out.
[14:57] Okay, we're back. So you can see with the reduced glue we're allowing more of these kind of
[15:05] fragments to bend inward and outward. And we're actually getting some really nice details
[15:11] along the edges. You can also play with the RBD deform pieces. So if you adjust the maximum points,
[15:20] so for example if I set it to 10, if I set to the maximum to 100, maybe we can also adjust the
[15:29] radius. You can see that we're getting a little bit of a different blending between them.
[15:36] So definitely play around with these settings and see what you get.
[15:42] Some of them can give you a more rough surface and some of them can give you a smoother surface.
[15:46] And basically this is how you can fracture and tear metal in Houdini 22.



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

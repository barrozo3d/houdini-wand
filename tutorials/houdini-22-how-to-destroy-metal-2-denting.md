---
title: Houdini 22 | How to Destroy Metal | 2 | Denting
source: YouTube
url: https://www.youtube.com/watch?v=R4YVz0FcCOw
author: Houdini
ingested: 2026-07-18
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-22-how-to-destroy-metal-2-denting/
frame_count: 0
frame_status: pending-selection
---

# Houdini 22 | How to Destroy Metal | 2 | Denting

**Source:** [YouTube](https://www.youtube.com/watch?v=R4YVz0FcCOw)
**Author:** Houdini
**Duration:** 15m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-22-how-to-destroy-metal-2-denting <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Now let's quickly take a look at how we can replicate this second example where we see
[0:08] these Canon metallic balls bending and denting this metal wall.
[0:17] And I have prepared this metal balls Canon setup which is pretty much a simple sphere,
[0:24] press space bar G to get back to this.
[0:28] And you can see I'm just doing some poly beveling, then just subdividing it, making sure
[0:33] it sits on top of the grid.
[0:35] And I'm just transforming it into the launch position compared to this wall.
[0:44] And I'm also adding some additional velocities in the point velocity so you can check these
[0:49] if you click on I and then use V attribute in the viewport.
[0:54] I mean, I need to make sure that the visualizer is on.
[0:58] You can see we have some kind of velocities.
[1:02] I'm also adding the additional multiplication on them based on alligator noise.
[1:07] So some of them should stronger, some of them will shoot with less velocity.
[1:15] And then if you take a look at this delete node, it's basically set to delete the sphere
[1:20] every 10 frames.
[1:23] So basically $F module 10 expression will make the sphere appear on the 10th frame, then
[1:28] on the 20th, then on the 30th and so on.
[1:31] So this will help us emitting it with staggered kind of timing, right?
[1:37] And rather than just emitting sphere on top of sphere every frame.
[1:42] And then the Canon is just like a simple Canon.
[1:46] You can also change your viewport lighting to have some nicer representations.
[1:53] So for example, if I look at this garage here, so we can go back to our camera and I'm
[2:04] going to change this, I'm going to click and hold on the work lights and I'm going to
[2:09] set this to dome light.
[2:11] And then you can actually attach an HDRI to your dome light.
[2:15] So if you click and hold on this again and click on properties, you can go onto file and
[2:20] then go to Foudini HDRI.
[2:23] And then I'm just choose this garage HDRI and up the exposure.
[2:28] So this will give us some nicer lighting and results.
[2:32] We can also turn on some ambient inclusion in the viewport.
[2:36] And this is basically how this was created.
[2:41] Okay, so basically we can continue from this same setup you would have this file that
[2:48] would bring in the garage door and then we're just splitting it and preparing for fracturing.
[2:54] So let's do a new RBD material fracture.
[3:00] So let's press tab and type RBDE material fracture.
[3:08] So this time I want to change the fracturing method.
[3:13] So first of all, let's change the material type from concrete to metal and I'm going
[3:19] to hit escape again just so we don't wait for this and let's change the mode to manual
[3:25] and let's go to fracture tab.
[3:28] So in here you can see that we have worked with this initial density previously but there
[3:34] is also a secondary fracture option.
[3:38] So let's set our main density to something like 2 and I'm going to switch from manual
[3:45] to auto update and let's press W to see our fragments.
[3:51] And then I'm going to enable secondary fracture.
[3:55] So it looks like it did something but we don't really see any of the fragments that should
[4:01] be added to the secondary fracture and that's mainly because this proxy only mode is turned
[4:07] on.
[4:08] So if we check out the proxy geometry, if I press tab and just do it now here, you can see
[4:14] that we actually have more fragments in here.
[4:19] And let's say if I turn off the proxy mode, our primary geometry would also be cut into
[4:28] the pieces.
[4:29] But this is actually done intentionally.
[4:32] There is a very interesting workflow that you can follow.
[4:35] Basically we will only fracture the proxy geometry and then it will allow the bigger fragments
[4:44] to bend and this way we can get a much more interesting deformation and much more details
[4:52] in the dented and deformed pieces.
[4:56] So I'm going to adjust some of the constraints.
[5:02] So let's go to the constraints tab and let's set the glue to something like 500.
[5:10] We also want to increase the dampening as we know from the previous example, this would
[5:14] help to stabilize everything and the rest should be fine.
[5:19] Alright, so let's do a first initial test on how these metallic balls would interact
[5:27] with this and then see what we can also do to add more details to the dented.
[5:35] So I'm going to actually start with the sphere.
[5:38] So let's go to the tenth frame.
[5:42] And basically we're just going to put down our VD configure.
[5:45] It's a pretty simple setup and we want this sphere to be emitting based on this RBD
[5:56] emitting attribute and I'm going to change the type to metal and I'm going to set this
[6:01] to something heavier like steel.
[6:05] And so this is good.
[6:08] Now for the wall we can basically reuse the same RBD configure that we did in the first
[6:16] example so I'm going to select this control C and then control V.
[6:28] And in this one we actually also have to enable the emission attribute but we need to set
[6:37] this to zero because we will be combining merging both of these and once we enable the
[6:43] emit option on the RBD bullet solver it needs to basically have a clear emit attribute
[6:53] on both objects.
[6:55] There's also another way to do this.
[6:57] We could have just combined the two and set groups and then by group we would have emit
[7:04] on or off but this is just visually more clear to do.
[7:11] And again this RBD configure comes in with the active area only in the middle set to
[7:17] metal aluminum and with emit set to zero.
[7:21] So let's now do RBD pack.
[7:30] So we are just going to combine the two and let's merge these.
[7:40] Alright so after we merge usually it's the next step to be RBD unpack.
[7:51] RBD unpack and then I usually just make sure that the transfer attributes and transfer
[7:57] groups are enabled just in case and then we can go ahead and place RBD bullet solver.
[8:07] Okay so let's now take a look at the bullet solver.
[8:12] Let's go to the first frame and let's go to our camera and let's hit play and see what's
[8:17] going to happen.
[8:19] So nothing is emitting because we didn't turn on the emit RBDs and once we turn it
[8:24] on it will basically take this attribute and emit from the spheres but not from the wall.
[8:31] Okay let's turn emit RBDs on and let's see.
[8:34] So you can see that our mesh disappeared and we also have the spheres actually going
[8:42] through the ground but let's take a look at the proxy geometry.
[8:45] I'm going to press tab and type no.
[8:49] You can see our proxy geometry is actually there and the high-res geometry isn't visible
[8:58] but if we do the RBD deform, so RBD deform, RBD deform pieces we would see that there
[9:10] is some denting but it's very minimal and that's mainly because you can see that the
[9:17] fragments actually allowing for more bending but since there are no details to support
[9:27] that in the deformation we're not really seeing a lot of the bending result.
[9:34] So what we can do now is go to the RBD material fracture on the wall and we can turn on the
[9:42] refinement.
[9:43] So let me just untape everything.
[9:48] So you can see there is nothing in here to support that extra deformation from the proxy
[9:53] pieces that actually have more on the inside.
[9:58] So once I set this to something like Bricker, I find Bricker works best.
[10:03] It will give me an initial subdivision that we can also adjust with the size parameter
[10:11] but this usually works pretty well.
[10:13] So now we would have some extra polygons to support that deformation from the proxy cluster
[10:20] pieces.
[10:21] So let's take a look at this one more time and I'm going to hit play and of course this
[10:26] is going to disappear.
[10:27] Let's look at this one.
[10:29] Okay, so we're getting same deformation pretty much.
[10:37] On the secondary fracture but now if you take a look at the deform, there are now more
[10:45] polygons to support this deformation.
[10:49] And this is actually becoming very useful.
[10:52] We can again change the amount of points to make the result a bit smoother.
[11:00] Maybe something like that.
[11:03] Right, so now we're getting more denting in here.
[11:08] Now if we allow this to go and play to the end and what you can also do, you can just set
[11:16] this first output to Blast and we can say I just want to blast the metal door and we can
[11:27] probably combine this, just merge this with the output of this.
[11:33] The spheres would need some normals.
[11:39] Probably just maybe those actually needs to be unpacked.
[11:50] Yeah, there we go.
[11:52] You know, so color them in a darker way so you'll just see them a bit better.
[12:03] Okay, so now if we take a look, we're getting some nice bending on this.
[12:10] Now additionally what you can do, you can allow some of the dented parts to be tiered along
[12:23] the primary fractured cut.
[12:29] So if you look at the fractures, so you can see there's this fracture primary cut.
[12:37] The secondary fracture would be all parented to this piece.
[12:42] So now if you go and in the fracture, you can also see that we have a fracture ID.
[12:49] So the primary fracture would have metal fracture and then the secondary would have something
[12:54] like metal fracture 2.
[12:56] So in the RBD bullet solver, we can go to constraints and we can say I only want metal
[13:03] fracture.
[13:04] So basically if we select this one, sometimes if it would not be visible, you just have
[13:09] to scrub the timeline.
[13:12] But we basically are saying that we're only allowing the primary fracture cuts to be affected.
[13:22] So basically the constraints would only be deleted along these cuts.
[13:27] And the secondary fracture would just stay there.
[13:31] We can keep the distance quite high so the fragments wouldn't detach.
[13:38] So now if you look at this one, let's press W to get out of this mode and let's press
[13:46] play.
[13:49] So we should see some denting.
[13:50] Maybe let's take a look through the merge.
[13:53] We can also actually enable the ground plane so the sphere doesn't go through the ground.
[13:58] Let's go to collision, ground plane.
[14:01] Let's do it properly and let's take a look from the camera one.
[14:08] So we can see there are some dent.
[14:14] But now since we have that constraints deleted along the primary fracture, we can
[14:23] actually also enable it through the denting.
[14:29] So in the RBD, the form pieces you can see, the boundary connection, if it doesn't find
[14:37] the cluster attribute, it would just have all the pieces combined basically.
[14:43] But if we tell that we want to use that parent piece and that parent piece is that same attribute
[14:50] that is set on the secondary fracture, it will basically allow the cuts to happen along
[14:59] the primary fracture, but the secondary fracture would just be there for the bending part.
[15:04] So you can get basically a very interesting behavior for your simulation.
[15:14] And this basically wraps up how you can use the new RBD metal fracturing workflows for
[15:21] your metal denting or deformation or tearing.
[15:27] And take a look at this file and most importantly have fun.



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

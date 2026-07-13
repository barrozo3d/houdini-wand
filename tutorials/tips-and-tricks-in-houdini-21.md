---
title: Tips and tricks in Houdini 21
source: YouTube
url: https://www.youtube.com/watch?v=gv_gXOSjCN0
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tips-and-tricks-in-houdini-21/
frame_count: 0
frame_status: pending-selection
---

# Tips and tricks in Houdini 21

**Source:** [YouTube](https://www.youtube.com/watch?v=gv_gXOSjCN0)
**Author:** cgside
**Duration:** 12m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py tips-and-tricks-in-houdini-21 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back! So in today's video I'm gonna be sharing a few tips and tricks for Aldini.
[0:06] They are always very practical and you can experiment with it right away.
[0:12] So I'm gonna start with this project that I actually never finished, but there are some tips that I wanted to let you know.
[0:20] So this is like a book lamp animation that I saw somewhere on Pinterest and I thought it would be cool to recreate, but I can never finish this.
[0:29] But there are some cool things I wanted to share.
[0:33] So these all starts with a fold that I do with a rig wrangle.
[0:39] And the bit that I wanted to show you is that as you can see I have some normals that I calculated with these oriental curves.
[0:46] They are just pointing up.
[0:48] And then I'm calculating since I'm going to do bands after, so as you can see these bands, the normals, as you can see, don't follow that band.
[0:59] So what you can do is to calculate a transform with a look at function from with the attenetributes and that will look something like this.
[1:09] And let's get rid of the normals.
[1:11] And when we band it, as you can see the transform will go with it.
[1:16] And then in order to have, since I'm going to use these axes later, this is like a normal attribute, I can extract it from the transform.
[1:27] Just by multiplying the transform by the axes you need.
[1:31] So this is how you extract an axis from matrix.
[1:36] So in this case I want the Z axis, so I place a vector on the Z axis and multiply it by the transform, which results as you expect by this vector that you can see in here.
[1:48] So later down the line I can do transforms based on that normal attribute.
[1:55] And in this case I'm just replicating the shape.
[2:00] So that was the first tip, how to extract a vector from a matrix.
[2:06] So still in the same example, as you can see I have the start of the animation.
[2:12] And I want to move it up because right now is below due to the modeling, it was done below the origin.
[2:20] So if I place in here a match size, and I move it to the center, if we look at the front view and I scrub through here, as you can see it's moving in there.
[2:32] It's not sticking to really to the center because we have this animation going on and the match size is calculating every frame.
[2:40] So what we can do is to place a time shift on the end frame.
[2:46] And then in this wrangle we can simply get the bounding box center of the freeze frame and then just subtract from the bounding box center this way.
[2:55] We always get these origin fixed as you can see.
[3:01] So instead of calculating every frame for the match size and not getting an accurate result, we can easily use the bounding box mean also.
[3:11] So we move it to the main position, but in this case I'm using the bounding box center.
[3:18] So this is another example scene where I had to model a fork and as a challenge I tried to do it procedurally.
[3:25] And so the bit that I wanted to show you after extracting the disease done from a sweep as you can see and manipulating the curves, then I'm selecting in here the parts for the dense blasting.
[3:42] And then I need to scale the tips and this was the most difficult part to do procedurally.
[3:49] So and even without doing it procedurally if you want to do this manually it might be a bit tricky to have a local axis on each dense.
[3:57] I'm calling it dense, I don't know if that's the correct name.
[4:00] Anyways so how I'm doing this is first of all I'm selecting the middle points just by doing some metting here and offsetting a bit by the select amount.
[4:12] Then I'm creating a UV flatten to get the UVs flowing on this geometry that will look something like this.
[4:22] From there I'm measuring the gradients of these UV attributes in this case the x component which means we will have a gradient that looks if I never actually the visualization a gradient that will go along the geometry.
[4:37] But we actually need a vector that points out in each direction or points in depending on the way you set it up.
[4:46] So what am I doing in here in the scale tips?
[4:49] First of all I have a Primro attribute from the sweep which looks something like this. So in this case it's Primro.
[4:58] So it alternates between 0, 1, 2, 3 but in this case I've deleted some in the middle so this will be 0, 1, maybe 0, 1, 2, 3, 4, 5 something like that.
[5:10] So what am I doing in here? I'm reading that Primro and getting the bounding box center of each of those IDs.
[5:19] Then I'm also selecting the points expanding the points group of these points that we will use later.
[5:26] Calculating a mask along the Z but we'll get there in a bit. The gradient is just the gradient we measured.
[5:35] Then we do a cross product between the gradients and the negative Y axis which will give us if I disable all of these,
[5:48] it will give us a value vector pointing in that direction on the negative X.
[5:56] But then we can do a sign for every other Primro but that won't still get us there.
[6:05] And from there of course we need to multiply by the sign but that will also count for the middle points we have in there.
[6:14] So we just want to do it on the unchair ledges.
[6:17] And for that we can really find the points, find all the points that are not in that middle group that we selected previously
[6:28] and multiply the vector also by that sign, let's say.
[6:34] And then we have the vectors pointing out that we the mask along the Z axis which is just a relative point bounding box along the Z.
[6:41] We can multiply offset the position and create an M multiplier that will just scale down along the tips because we have the vector pointing out in this case I'm doing minus.
[6:54] So we could also have it pointing in but in this case it's pointing out is not perfect as you can see on the tips but is somewhere close.
[7:04] And that's how I did this procedural fork.
[7:09] And then at the end we should have something like this with a subdivision and what not.
[7:15] And you can see even on the tips topology is perfect.
[7:18] Again you can have a look on Patreon all these files that I'm sharing.
[7:22] I'm going to be posting there if you work yours how I did the rest.
[7:26] But again this was the most interesting part. I hope it was clear.
[7:33] So this was a question that got me thinking on how you can take an input geometry where you have no access to the history or the creation in this case I have because I built it in here.
[7:43] But let's say you don't have you just got some geometry and you have to manipulate it.
[7:49] And the way we need to manipulate it is to have a control to change the thickness along the let's call it ribbons or whatever you want to call it.
[8:01] So you can do all these manipulation and as you can see is only happening in one of the axis and on multiple object multiple object also.
[8:10] So let's see how that set up after creating the geometry and we have let's say we have this baked.
[8:16] Then we can first of all enumerate to create an ID for each point because later we will need it.
[8:24] In here this point this group is selecting the art edges as you can see so we can do a UV flatten.
[8:31] And this UV flatten is using a rectify group on all so we get these flowing UVs and they look something like this.
[8:39] Which means that we can easily create a u-watt-ribute or a curve u along our shape.
[8:46] So if we now split the UV seams and promote to a point attribute and in this case in here I'm creating the u-watt-ribute based on the uv.x.
[8:58] So I can actually show you how that looks if I assign this to a attribute and if we look at it, oops.
[9:08] As you can see we have like a curve view along our geometry but in this case I am manipulating it with a ramp and creating this sort of shape.
[9:19] So that's fine now in this case I'm not doing anything in here.
[9:23] To select these polygons that we want to move we can measure the area and promote it to a minimum in detail mode because they will be more or less the same.
[9:35] This is the polygon in here.
[9:37] And then in a group expression we can use that area and the min area to select within a tolerance.
[9:47] And I can see that it's selecting more than I want so I'm going to decrease these in here.
[9:52] And as you can see we have a tolerance to select all those polygons in there.
[9:57] Then it's simple, right now the geometry is plated so what we can do we can do a pick and now the pick node in the node in it 21 allows us to input some hash attribute which I'm using that u that we created.
[10:09] And I'm doing that only on the group, this group of polygons.
[10:13] Then we can simply fuse this by creating we can even disable the snap distance and just to match a tribute by index which means that we can come in here and even pick it even more.
[10:26] Or manipulating here the curve as you can see.
[10:31] So a very specific case but hopefully this will help you out in a future situation.
[10:39] So in this last example I wanted to show you how you can create quickly some reliefs.
[10:44] Let's say for coins and the type of geometry in this case is just using normal so it's like a fake effect.
[10:49] But if you want you can move this into the depth channel and do based on height and create these reliefs but these normal setup works pretty well in my opinion.
[10:58] So you will start with the geometry that you want to imprint create the normals and then create the coin geometry and match it and put and place it in the front of the mesh that you want to imprint.
[11:10] You do a basic remesh because we will need some geometry and do a UV texture just not a graphic projection along the z axis.
[11:18] Then you add a normal and this is let's say is our low mesh and this is our I mesh that we were going to use in a baked geometry textures.
[11:27] So you place the high which will be the imprinting geometry and you place the coin as low and then you can simply render the normal which is in near world normal.
[11:40] And as you can see this will give you this result and then you can plug the coin geometry to the material and you'll get and you'll connect it the output to the normal channel and you get this sort of result as you can see.
[11:56] Which can be enough to fake to do some fake effects so hopefully you found this useful.
[12:03] And that's basically it guys hopefully you found these examples interesting.
[12:08] I hope I can continue with this series of doing tips and tricks in Odin when I don't have a specific project to show.
[12:16] And if you want to support me you can do so by subscribing to my Patreon and where you can find all the project files including the ones from this video and all the other ones alongside with exclusive tutorials.
[12:30] I also have a Patreon shop if you want to have a look where I have procedural courses in there or courses on procedural modeling and animation and whatnot.
[12:39] So as always thank you for watching and I hope you to see you next time.



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

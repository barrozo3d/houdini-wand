---
title: Morph Anything with VDBs in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=QUnkozOK4Ro
author: Voxyde VFX
ingested: 2026-07-21
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/morph-anything-with-vdbs-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Morph Anything with VDBs in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=QUnkozOK4Ro)
**Author:** Voxyde VFX
**Duration:** 23m23s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py morph-anything-with-vdbs-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] SDF volumes are extremely useful in a lot of cases but they're especially useful when it comes to any kind of morphing effect and transitions or in this case revealing the pattern of the soul of a shoe.
[0:12] So this comes up a lot in VFX but especially in motion graphics, SDF volumes are crucial when creating any sort of transition and this is mainly because we're not dealing directly with geometry.
[0:24] So usually what happens when we try to create these kinds of morphing effects on geometry directly, we have a lot more constraints than when dealing with SDS because we need the objects that we are trying to morph in have a consistent
[0:39] typology which can be extremely hard to maintain and if you want to create effects like a slight pushing out along the transition like we have over here we deal with all sorts of geometry intersecting, behavior and we have to deal with normals and all kinds of stuff that really makes this effect difficult to set up by working directly through geometry.
[1:03] So this is where we can use SDF volumes instead because we don't really have to worry about any of this stuff.
[1:09] We just have to be a little bit careful on how we set up the effect and these SDF techniques really have a lot of carryover to a lot of different effects.
[1:16] But in this tutorial I'm just going to show you how to create this revealing pattern and we'll start from scratch.
[1:21] Here I am inside the project file.
[1:23] So I will include this if you want to check how I set up everything including the camera animation, including the Solaris setup for rendering.
[1:32] And we'll do a walkthrough over the Solaris setup as well.
[1:36] But let's go ahead and start recreating this effect from scratch.
[1:39] I will start from all the way at the top.
[1:42] So here I have a shoe model.
[1:45] So this model is from Sketchfab by user AR41K.
[1:50] Go ahead and check it out.
[1:51] Download the model as well if you want to follow along.
[1:54] It's honestly a really good model.
[1:56] It has a lot of definition, a lot of pretty good resolution.
[2:00] So it is kind of close to what you would find in production.
[2:03] But let's go back over here.
[2:05] So we bring in our shoe geometry.
[2:08] We do some UV transformations, not really important.
[2:10] And then we do a match size so it's flat on the ground.
[2:13] And let's say that we're working in the studio and this is what we would get from the model in the department.
[2:17] So from here we have to separate our sole part of this model.
[2:23] Now it's going to be a lot easier if we pack all of our geometry instead of working with polygons.
[2:29] This will make the selections a little bit harder.
[2:31] So let's go ahead and from here I'll actually duplicate this setup.
[2:35] So this will be our start.
[2:37] And from here let's do an assemble and let's pack everything.
[2:40] We're going to go ahead and create packed primitives.
[2:43] So now if I press S we can see we have we can do a selection like this.
[2:47] So usually we can use a clip node or in this case it's going to be faster if we just go into a front view.
[2:53] I'll press S and I'll just select maybe select everything from the sole.
[2:57] I can press delete here.
[2:59] Let's do delete no selected.
[3:00] And really we're just trying to isolate only this part here right at the bottom.
[3:05] So I'll press S again and I'll get rid of this middle part of the sole.
[3:09] Let's press again delete.
[3:11] And now we are left with this which is essentially the geometry for our pattern.
[3:15] So from here we can start working with SDFs.
[3:17] So before we turn this into an SDF let's go ahead and unpack this.
[3:21] So we have back our polygons.
[3:23] Now in order to work with SDFs we need to close off this geometry.
[3:27] We can see that this is hollow.
[3:29] So for this we can do a poly cap.
[3:32] So I'll use the poly cap which is a polyfill preset with all of the right settings that we need.
[3:38] And we can see luckily for the most part this will give us a pretty good solution.
[3:42] So now we can safely turn this into an SDF.
[3:45] Now this will depend on the model you're using.
[3:48] You might not be able to get away with this poly cap or you might not need this poly cap in general.
[3:53] This is where you might have to ask for a special version from the modeling department or if you're modeling this
[3:58] yourself then you can just do some custom adjustments to get a filled geometry.
[4:03] But we have our geo here.
[4:05] So if we do hopefully a VDB from polygons we can see that everything works.
[4:10] Now we will have to lower the voxel size here.
[4:13] If we go low enough we will get back our details for our final resolution.
[4:18] We'll use something like 0.005.
[4:20] We can see that this really gets most of our details from our original geometry.
[4:26] So this will be OK.
[4:28] While we are doing this we will work probably with a higher version here.
[4:32] Let's do something like 0.02 or actually let's go to 0.01 for now.
[4:36] Now one is to happen is we simply want to blend between two different versions of our SDF.
[4:44] So we need a version with a pattern which we already have and we need a smooth version
[4:49] without all of these indentations from the pattern in our soul.
[4:54] Now this is something that again if we look at our geometry we would be able to
[5:00] essentially get this costume made from the modeling department or we would do it
[5:05] ourselves.
[5:06] We will simply ask for a version of the mesh without all of these details in our soul.
[5:13] Now in our case we'll just do this ourselves.
[5:16] But usually this is something that you would have to ask for regardless.
[5:20] If we go back to our VDB from Polygon's here we can let's do a separate version
[5:26] for our smooth SDF.
[5:28] So from here we have an SDF.
[5:31] We want to do a VDB reshape SDF.
[5:34] We will push this out slightly.
[5:36] Let's do something like 2.
[5:38] And then from here we can do a VDB smooth SDF.
[5:42] We can probably increase the iterations here.
[5:46] Let's maybe increase our filter voxel radius.
[5:49] We want something like this.
[5:51] We'll want to also template our geometry.
[5:55] We want to make sure that we roughly maintain the boundaries of our geometry.
[5:59] From here we can do another VDB reshape SDF.
[6:02] But this time we can run on a road and now we can see we're kind of getting the
[6:06] outline of our original mesh back.
[6:09] So this won't be really one to one matching.
[6:12] It won't be perfect, but this will be the limitations of doing this ourselves.
[6:17] As far as recreating this smooth surface.
[6:19] So this should be good enough.
[6:21] We will probably come back here to readjust if necessary.
[6:25] So we have our pattern VDB and our smooth VDB.
[6:29] We can probably draw some nose here as well.
[6:32] We can do here we can say VDB smooth and here we can say VDB.
[6:37] Let's do VDB pattern.
[6:39] So we will want to transition from this to this using a mask.
[6:43] Let's actually increase our smoothing a little bit more.
[6:46] And maybe I'll push this out as well.
[6:48] It's something like this.
[6:50] So let's do a volume VOP from our VDB smooth and reference our VDB pattern in
[6:57] the second input.
[6:58] And what we can do for this is if we go inside.
[7:02] So to read the information from our pattern SDF.
[7:06] Normally, if we would be working with the geometry and we would have the same
[7:11] topology and point count, we would be able to simply do an import point attribute.
[7:16] And reading the position data based on our point number.
[7:19] In this case, we don't have any points.
[7:21] And to read the information from our second SDF, we will need a volume sample.
[7:27] So if we drop a volume sample, we'll sample from our current Voxel position.
[7:32] And we want to reference our second input, which is our pattern.
[7:36] We don't really need density because we want to export to our surface volume.
[7:41] So here we'll do a bind export and we'll set the name here to be surface.
[7:47] And if we just plug the result from our volume sample, if I plug this over here,
[7:52] we can see now that our smooth SDF becomes our pattern SDF.
[7:57] So what we have to do is do a bind on our current surface value.
[8:02] And if we do a mix between our current values and the values that we find with
[8:10] the volume sample, we'll plug this to export as our final output.
[8:14] And now with this mix value, we can see that we can control the transition
[8:17] between these SDFs.
[8:19] Now, just in case, when usually when you do these kinds of transitions or
[8:24] interactions between volumes, we want to make sure, first of all,
[8:28] that we are running on the same size on both of these SDF.
[8:32] So if we go up after this VDB smooth, let's go ahead and do a VDB resample.
[8:39] And we'll do here, let's set this to using voxel size only.
[8:44] And then whatever size we use here should match the size that we have over here.
[8:48] So I will just copy parameter on this VDB from polygons and let's paste the same
[8:53] size over here, so paste relative references.
[8:55] And now if we increase the size here, the resolution on our pattern SDF,
[9:01] we'll set this to 0.005, we will have the same version on our smooth SDF as well.
[9:05] So this is one of the things.
[9:06] And the other thing is we want to increase the bounds of the SDF so we can just do
[9:12] VDB activate SDF and we can set this to use WorldSpaceUnits.
[9:17] Let's maybe just make sure that we have enough information around our voxels here.
[9:23] We'll set this to 0.2.
[9:24] We can see that this will also expand our bounding box so you can preview this with
[9:28] Shift W and let's also run the same kind of activation.
[9:32] Let's run this on our pattern as well.
[9:34] And because this isn't an animated process, even though this activation takes a little
[9:40] bit, we really only have to compute this once.
[9:42] So now back in our volume VOP, we can see that everything works.
[9:45] If we were to do a VDB convert, we can convert this back to polygons.
[9:50] So now we are able to render this assigned materials.
[9:53] But if we go back inside our volume VOP, we just have to control this bias value
[9:58] with a gradient mask that travels across our soul.
[10:01] So this will be simple to set up.
[10:03] Let's first go back and maybe work with a lower resolution.
[10:07] So this loads faster.
[10:09] So we'll do 0.02 for now and we'll go back in our volume VOP and I'll just
[10:14] duplicate this global node here and let's run from the position.
[10:19] We'll do a relative to bounding box.
[10:21] We'll split this.
[10:22] Let's do a vector to float and we want to grab the Z value here.
[10:27] So let's go ahead and grab our third component.
[10:30] We'll do a feet range and in between we'll do an add.
[10:34] And for our feet range, let's actually promote our second input for the add.
[10:39] And this will be our let's do offset or maybe we can label this as animate.
[10:44] And for our feet range, we'll promote our source max.
[10:49] And this will be let's do here with now.
[10:52] Usually if we were working with geometry, we would be able to preview this mask
[10:55] directly in the color or create some sort of visualizer.
[10:58] In the case for SDF, we don't have a visualizer for this.
[11:02] So we'll just have to plug this directly into our mix value and see what we get.
[11:06] And I can see already that we might have messed up our axis here.
[11:10] If we go up, we can decrease our weight here to make this a little bit sharper.
[11:14] And then with our animate value, we can see that we create this transition.
[11:18] Now we want this to go on the let's see here.
[11:22] I think the actual orientation here should be X.
[11:26] So I'm going to grab the first component of this vector to float and plug this
[11:30] into the add. And now I think we're getting the correct result.
[11:33] So we can control this with this animate value now.
[11:36] So this mask setup that we just created over here is something that we use all the time.
[11:41] We have a new workshop coming soon,
[11:43] motion graphics in Houdini, where we really use this setup in a million different ways
[11:48] and also use a lot of variations of the setup.
[11:50] But really, it's just a very simple way to set up a mask and it will give us
[11:54] really good results with SDFs as well.
[11:56] We can also introduce a little bit of noise on this as well.
[12:00] So if we run a turbulent noise here, let's do a 3D noise.
[12:03] We'll set this to add.
[12:05] We'll plug this over here and we can let's also maybe right click and create input
[12:11] parameters so we can also control our noise.
[12:13] We might want to bomb this up slightly.
[12:15] And this is really much the core of this effect.
[12:18] But another really cool thing that we can do here is also create maybe more of a
[12:23] ridge where our transition happens.
[12:26] So I would like to just slightly push out our SDF to give it kind of like a leading
[12:32] edge on this effect.
[12:33] So if we go back inside, if we look at our surface,
[12:37] if we want to push out our SDF, we can do an add operation here.
[12:43] And if I just promote this for now to a constant, if I were to subtract values,
[12:48] we would push out and expand our SDF.
[12:51] And this is why we need to also activate our voxels around our regions.
[12:56] In case we want to do stuff like this, the voxels need to be activated so we can
[13:00] push in values in those voxels and we can also do erosion.
[13:06] So if we were to increase this value here, we can see how we can start to slowly
[13:10] erode our geometry.
[13:12] So this is also something very useful.
[13:13] In our case, we just want to expand this.
[13:16] So we'll want to push this out a little bit.
[13:18] So we will set this to a negative value, something like negative point zero two
[13:24] should be okay.
[13:25] But again, we want this to only happen at the ridge.
[13:29] So with our mixed value that we get with our mask set up from over here,
[13:34] we get zero to one value.
[13:35] So currently this value will be zero over here and one over here.
[13:39] And what we want to do is this gradient from zero to one is remap it to zero and
[13:44] then one and then zero again when it's a full value of one.
[13:48] So we can do a ramp parameter here.
[13:51] We can set this to a spline ramp.
[13:54] We'll plug this from our fit and let's go ahead and plug this as our add
[13:59] operation and we'll also do a multiply and promote our second input.
[14:04] So this will be our actual push out value here.
[14:07] So we can do here.
[14:08] We'll just do a push and then we can go up.
[14:11] And again, we want a zero to one and then back to zero ramp.
[14:15] So we can do something like this.
[14:17] And for our push value, we mentioned that we want to use something like negative
[14:21] zero point zero two or something like this.
[14:23] So now we can see if I were to decrease this even further.
[14:27] We have this bump right here where our transition happens.
[14:30] And if we were to animate this, let's actually go to the first frame and just
[14:36] do a very simple animation here.
[14:37] And let's start from roughly negative.
[14:41] Let's do here something like negative nine.
[14:44] We'll add a keyframe and we'll go to frame 120 and we'll just increase this until
[14:49] it completes our soul.
[14:51] We'll do something like point 14 in my case.
[14:53] So we can have our animation here and we can see this nice ridge that we get along
[14:58] our transition, which gives us this nice leading edge.
[15:01] And we can further control our ramp here.
[15:04] If we set this to a B spline, we can control exactly where this ridge happens.
[15:09] So maybe I want this more in the front here.
[15:12] Let's maybe do something like this and we can control the amount if we want.
[15:17] And this is really all that we have to do.
[15:19] Let's set this noise first of all to simplex here.
[15:22] We can control the roughness now and we can see how really simple this is to get
[15:26] some really cool results and transitions here.
[15:29] So we can now increase our final resolution.
[15:32] We'll just go to our initial VDB from polygons.
[15:34] We can set this in the original file.
[15:37] I think I use something like point zero zero five to get some really something
[15:42] really close to the original geometry so we can do something like this.
[15:45] And we can see we get some pretty cool results.
[15:47] And it's not really running that slow considering we're dealing with around
[15:53] 600,000 points and really this is the effect.
[15:57] This is how we can set this up.
[15:59] We can go to our volume.
[16:00] Move up. Maybe we can increase our weight transition here.
[16:03] We can play around with the timings and our ramps.
[16:06] We already have a lot of control to redirect this however we want.
[16:10] So this entire setup, this is something I've used a lot in production when I was
[16:15] working at the studio.
[16:16] This really came up a lot or at least different versions of this.
[16:19] I know I had to do a version exactly for a shoe like this to reveal the pattern.
[16:25] So I hope you found this technique useful.
[16:27] Again, when we are dealing with SDFs, we don't have to worry about any kind of
[16:31] geometry intersections and stuff like that.
[16:33] So for example, if we had just our geometry like this and we want to push out this
[16:38] geometry, if I were to do this with a peak node and increase the distance,
[16:42] we would have a lot of weird issues happening here.
[16:46] This kind of inflation.
[16:47] We can see that really quickly our polygons start to intersect with each other.
[16:51] And especially if we want to do any kind of erosions, this really won't work.
[16:55] So this is where again for morphing, for transitions, for transforming kind of
[16:59] liquid-ish effects, SDFs are really the way to go.
[17:03] And now to really quickly go through the rest of the setup, we can see that this
[17:08] is the geometry that I'm referencing in Solaris.
[17:10] So this is the effect that I did originally, the one you saw in the render.
[17:14] We have our sole geometry over here.
[17:17] We have the rest of our shoe over here.
[17:20] You can also check out how I set up the camera with some targeting,
[17:24] with some transitions between target.
[17:27] There's really a lot to talk about cameras.
[17:29] And we talk a lot about cameras and advanced camera setups like this in the new
[17:34] workshop coming, so beyond the lookout for that.
[17:36] But we have our geometry ready.
[17:39] So if we head over to Solaris and you can see this in the project file yourself,
[17:44] it's a really simple setup.
[17:45] It's pretty bare bones.
[17:46] I set this up really quickly just so I get a cool render of this effect.
[17:51] But if we go over the setup quick, we have our camera with a scene import.
[17:55] We bring in our shoe geometry without the sole and we have our material.
[18:01] So this is provided with the shoe asset.
[18:03] We merge this with our camera.
[18:05] And then we have our sole geometry.
[18:07] And this is where I created a costume material for this.
[18:10] I just created this texture.
[18:13] I tried to recreate this from the original shoe model.
[18:16] So this pattern here I created with a simple cop network,
[18:19] which looks something like this.
[18:21] So it's really just a diamond shape with some feather with a little bit of detail
[18:28] in the middle. We do a shape scatter on this so we can title it.
[18:31] And then we export our maps.
[18:33] We have our normal, our height and a little bit of color here.
[18:37] Very simple setup.
[18:38] We just a little bit of noise.
[18:39] We bring all of this inside this material builder here.
[18:43] We merge this with our original shoe.
[18:46] And then for lighting, I just have a few lights.
[18:49] We got let's check this real quick through our camera.
[18:54] We have a if I go over these one by one, we have a rim light.
[18:59] Then we have a fill light, another secondary rim light to get some sharp,
[19:04] contrasty details and a little bit of color.
[19:06] And then finally, this light here for the shoe,
[19:09] it's mostly a rim light for the end of the sequence here.
[19:13] And then I also added just a simple sphere, which we have assigned a simple noise
[19:20] material on this just to get a really quick background and the default render
[19:24] looks something like this.
[19:26] So if we just render this for a second, this is the default result that we got.
[19:30] And in comp in Yoke, I recreated the beauty by splitting up all of the AOVs.
[19:35] And I animated some lights turning on and off across the entire animation.
[19:40] It's just a lot easier and a lot faster to do these kinds of effects,
[19:44] especially when you need to animate a light.
[19:46] I would much rather do this directly in Yoke and I just added a little bit of
[19:50] post-process effects and just really adjusted all of the gradings for the lights.
[19:54] So feel free to check out the project file.
[19:56] You'll find the download link in the description.
[19:58] I hope you found this technique useful and stay tuned for more tutorials.
[20:01] I will see you next time.
[20:03] So of course, I decided to change everything less minute.
[20:05] So this was the original render and after compositing, just shuffling out all of
[20:12] the AOVs and adjusting the grading, we end up with something like this.
[20:16] So this is kind of like the light version.
[20:19] But then I decided since if I'm just previewing the reflection
[20:23] RIM pass for the render, it looks something like this.
[20:27] So this by itself already looks really cool.
[20:30] And I decided to try to do something with this.
[20:33] This is really the power of compositing.
[20:34] So really, if you're not using Nuke to improve your 3D renders, I really suggest
[20:41] you start learning Nuke.
[20:42] We have a free intro to Nuke course, which you can take.
[20:46] I'm really surprised how many 3D artists don't really actually use compositing.
[20:51] It's really, really easy to improve renders with really simple methods.
[20:56] So just based on this AOV, I decided to also do a dark version.
[21:01] And really all I did here was I re-rendered everything, but it's mostly the same setup.
[21:08] Only the rim lights I tinted towards green and I removed the depth of field here
[21:14] because I added it directly in comp with this bokeh node over here.
[21:19] Because I found that the bokeh really provides some really good results.
[21:24] And it's also something that we can adjust in real time here in Nuke.
[21:28] But if we look at our render now, we just shuffle a bunch of our passes, but we're
[21:34] mostly using our combined reflection passes, which is going to be this rim light over here
[21:40] and one for the other side of the shoe and then the sharp one.
[21:45] So again, it's mostly going to be the same lights only.
[21:48] I'm tinting everything towards, I'm desaturating everything so it's black and white.
[21:52] And from here we have a base and then I'm shuffling out.
[21:57] Here I'm not actually using the AOV, but I'm shuffling out the sharp light,
[22:01] setting this to black and white because I'm merging some other passes as well.
[22:06] So here I'm using the facing ratio.
[22:08] I just flip the colors around and remove the background.
[22:12] So really, I think these are just the two passes that I'm using.
[22:15] So this black and white mask, we're tinting towards green and then we're just adding
[22:20] the glow and then we're placing this on top.
[22:22] And then on top of this, we get the bokeh and a little bit of grading.
[22:27] And on top of everything, I'm actually borrowing the background that we had in
[22:31] the first render and I'm doing a darker green version of it.
[22:35] And I'm placing this on top, some APV net, a diffusion.
[22:38] And we probably could have added some grain as well.
[22:41] But really, this is everything I did.
[22:43] So I just wanted to include real quick this nuke part as well.
[22:47] And this is why most of the time I do prefer to do a lot of the look that
[22:51] process directly inside of nuke because you can experiment with different looks
[22:57] on the fly, get different results and then if necessary, you can just go back
[23:02] to re-render certain elements to fit your new look.
[23:05] But it's just easier and a lot faster to iterate on different kinds of vibes
[23:10] and looks directly in comp.
[23:11] So this is really the last part of the tutorial.
[23:14] Hope you enjoyed and I will see you next time.



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

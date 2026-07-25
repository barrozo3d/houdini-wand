---
title: Fantasy FX in Houdini | DRAGON FIRE
source: YouTube
url: https://www.youtube.com/watch?v=xu0zRT-L2aE
author: Rebelway
ingested: 2026-07-25
houdini_version: "[PENDING]"
tags: []
extraction_status: needs-review
frames_dir: tutorials/frames/fantasy-fx-in-houdini-dragon-fire/
frame_count: 0
frame_status: pending-selection
---

# Fantasy FX in Houdini | DRAGON FIRE

**Source:** [YouTube](https://www.youtube.com/watch?v=xu0zRT-L2aE)
**Author:** Rebelway
**Duration:** 127m25s | 32 section(s)

---

## Raw Data (for Claude Code extraction)

## Ingest Safeguard Report

_Auto-generated at ingest/frame-capture time — explains why `extraction_status` may be `needs-review`. Safe to delete once reviewed._

- **CRITICAL:** Empty transcript in chapter 'Flipbook'

---

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py fantasy-fx-in-houdini-dragon-fire <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] MiraG NOT THAT Esteemed
[0:25] Hi everyone.
[0:26] We're back inside our initial setup scene because what we're going to do now is just
[0:32] start creating the main effect for this week which is going to be the dragonfire.
[0:37] I've made a few small changes, I've just updated this bridge with our new bridge model and
[0:44] I've also brought in our sky and sun from the environment section.


### Save as [0:52]
**Transcript (timestamped):**
[0:52] And now the first thing I want to do is let's just save as and let's create a new folder
[1:00] and call it shot1 and let's call this file also like shot01 and let's call it dragonfire
[1:15] and version1.


### Delete [1:18]
**Transcript (timestamped):**
[1:19] So now that we're inside this new file we can actually just delete everything that we
[1:25] don't need.
[1:28] So let's just delete all these cameras and just leave the camera for the shots.
[1:41] Another thing we can do is let's just change the frame range because if we look at the
[1:48] camera it's from frame 1001 up to 1133 so I just adjust this like that and hit apply.
[2:11] And before we start creating the effects I usually prefer to set up the collisions.
[2:21] So let's start by doing that.
[2:25] Let me just arrange things a bit.
[2:31] But yeah let's create a new geo and let's call it collision and terrain and let's bring
[2:46] in the terrain we have.
[2:49] The drop down and object merge and over in the terrain let's bring in the null here and
[2:58] into this object.
[3:08] Now when we have this kind of terrain we don't want to use all of it as a collision object
[3:14] because we just don't need it.
[3:18] We're gonna need this section here around the dragon where we're gonna have the fire
[3:25] and having all of this terrain being calculated as collision object will just slow down things
[3:31] too much and it's just really unoptimized.
[3:40] So let's drop down our delete and I actually want to use delete by bounding volume.
[3:55] And let's just give it something quite big for start and also give it some height.
[4:11] So this is not bad maybe we can try 150.
[4:22] Let's go for 160.
[4:31] And this kind of covers all the area that we need and let's just select delete non-selected.
[4:48] Next what I want to do is let's just drop down an extrude volume and what this does
[4:56] is it just you can see it extrudes everything down and gives us kind of a closed geometry
[5:08] and just drop down a normal to fix the viewport.
[5:22] And now we can just drop down a collision source and also drop down two nulls.
[5:35] So we'll call this one geo and we'll call this one VDB.
[5:45] Another thing I like to do is just take a look at your VDB for this collision geometry
[6:01] and just take a look that everything is working properly.
[6:06] You did see it takes quite a while to just calculate it.
[6:09] We actually don't need all this detail.
[6:14] So let's just go over here to volume and make the voxel size a bit bigger.
[6:20] So maybe 0.2.
[6:27] And yeah I think this will work fine for this section.
[6:36] So that's it for the terrain.
[6:40] Let's also give it a green color and let's drop down a new geometry.
[6:50] Let's call this collision dragon.


### Collision [6:57]
**Transcript (timestamped):**
[6:58] And the same as before let's object merge the dragon.
[7:15] And yeah like before I don't want a collision object for the whole dragon.
[7:22] We just need a collision object for the head that's breathing fire.
[7:31] So let's just select this.
[7:33] As you can see it's packed so let's just convert it to polis.
[7:43] And now I just want to select this head.
[7:51] So let's just do something like this.
[7:55] Just make sure to select everything.
[8:06] And also make sure not to select anything else.
[8:16] This should work.
[8:18] Let's press delete and delete non-selected.
[8:28] And let's just close this opening here.
[8:32] So we'll use a polyfill.
[8:40] And let's just use a triangle for this.
[8:53] And let's drop down a collision source.
[9:02] And again we can drop down two nulls.
[9:05] Let's call this one geo head 01.
[9:14] I'll call this one vdb head 01.
[9:27] And this seems fine.
[9:30] You can actually give it some more resolution.
[9:39] Probably not necessary but why not.
[9:42] It's quite fast to calculate.
[9:52] And let's also give it a green color for collisions.
[9:58] And you can turn these off.


### References [10:01]
**Transcript (timestamped):**
[10:03] Now that we have the collisions ready, just before we start creating the dragon fire, I
[10:09] wanted to bring up these two references and kind of just take some points and see what
[10:16] we want to create and see what kind of elements we want to also incorporate into our scene.
[10:26] So if we look at this reference first, there's a few things I really liked.
[10:34] And first of all you can just see the way it looks.
[10:41] We get this kind of really thin stream of fire moving really fast.
[10:47] So it's almost like in a straight line.
[10:51] And when it hits the floor and the collision object, it kind of moves almost like a flip
[10:59] simulation.
[11:02] It kind of flows along the ground and only then it kind of billows up and creates fireballs.
[11:12] We can do this maybe using a flip simulation or just regular particles.
[11:22] And another thing I really liked is just this coloring.
[11:28] We get this blue flame over here and only then it gradually goes into the yellows and
[11:33] oranges.
[11:35] So that's definitely something I also want to incorporate into our sim.
[11:43] And also the general, you know, you see the general look of the frame.
[11:47] We get these really wide glows.
[11:51] We get fire is quite overexposed.
[11:55] And we also get these kind of embers and lingering smoke being lit up.
[12:04] And if we look at this reference, the main thing I wanted to get from this reference
[12:08] is just the speed of the initial burst.
[12:15] So if I'll just play it, you can just see how fast it moves.
[12:19] It kind of really shoots it out and it gives a really powerful feeling to it.
[12:27] And another thing we can look here is once it's actually hitting something, you can see
[12:34] it's shooting out really fast and then it kind of stops and creates this fireball.
[12:40] So that's another behavior that I would like to achieve.
[12:46] And just a small note for next week, if you look at the exposure right now, everything
[12:53] is overexposed with the fire.
[12:55] And as the fire lingers in the frame, you can see the camera kind of getting darker.
[13:05] Everything else is getting dark.
[13:07] And then we actually see the flames inside, like all the detail.
[13:12] So that's another nice touch to add to our shot.


### Dragon Fire [13:18]
**Transcript (timestamped):**
[13:20] So let's go back inside Houdini and continue and actually start creating the dragonfire.
[13:29] Let's start creating the effect.
[13:31] Let's drop down a new geo.
[13:35] We'll call this effects dragonfire and we'll give it 0-1 for now.
[13:46] Because I do know that we have three heads and later on what we're going to do is just
[13:52] duplicate this setup and apply it to the two other heads as well.
[13:57] So let's go inside here and drop down an object merge.
[14:03] And let's just bring in the dragon.
[14:07] So if I'll just draw here for a second.
[14:19] What I want to do is we need an emitter over here inside the mouth.
[14:25] And we also need a vector pointing outwards.
[14:31] And we need them also to be moving together with the animation.
[14:34] So we'll all be facing the right direction when the dragon moves.
[14:41] And to do this, we can actually just select one point here and one point here and then
[14:50] calculate the centroid position.
[14:56] And this will give us a floating point inside the mouth.
[15:00] And we can also do the same thing for the end of the mouth.
[15:05] And once we have these two points, we can just calculate the vector between them.
[15:12] So we'll just subtract this position from this position and we'll get this vector pointing
[15:18] out.
[15:20] So let's start doing this.
[15:27] First of all, let's just convert this dragon to polygons.
[15:35] And let's select our points here.
[15:45] So for inside the mouth, let's just select maybe this one here.
[15:52] And this one over here.
[15:57] And let's just press delete and select delete non-selected.
[16:10] And now that we have these two points, let's just use extract centroid.
[16:18] This will give us one point in the center.
[16:24] Just delete this name attribute.
[16:29] And you see, we get this point.
[16:33] And also when the dragon moves, it's moving with it.
[16:39] So let's do the same thing for the tip of the mouth.
[16:46] I just go to this blast and select two different points.
[16:56] So let's select this one here.
[17:02] And this one here.
[17:05] And press enter.
[17:12] And now the extract centroid gives us this point here.
[17:21] So now that we have these two points, we can actually just calculate the vector between
[17:27] them.
[17:28] So let's do this using a wrangle.
[17:33] And we'll connect the first point here and the second point to the second input.
[17:41] And we also want this vector to be velocity.
[17:44] So let's type v at v.
[17:52] And let's type point, press 1, 1 meaning this input.
[18:04] And we want p for that position at ptinam.
[18:12] And we want to subtract it from our current position.
[18:17] So we'll type at p.
[18:23] And if we look over here, we have this new attribute for v.
[18:37] And when we have the animation moving, it's still pointing in the right direction.
[18:48] Now let's just copy a sphere here.
[18:52] So let's drop down a sphere.
[18:57] And I want it to be polygon.
[19:01] And let's just use copy to points.
[19:12] And you see once the sphere moves here, it actually picks up the velocity.
[19:21] And let's just give it a half frequency.
[19:27] And let's just lower the scale quite a bit.
[19:34] Remember the references, the stream should be coming out in a very thin line.
[19:43] And this can work well for that.
[19:48] Another thing I want to do is let's just add another wrangle.
[19:53] And what I want to do now is just add some controls.
[20:00] Just something to control the velocity.
[20:05] So we can just do v at v.
[20:07] And let's do multiplied equal.
[20:11] And we'll create this channel float.
[20:14] And we'll call it vel mult.
[20:18] So it will be a velocity multiplier.
[20:22] Let's create this parameter.
[20:29] And you can actually see it controls the velocity.
[20:33] And we want it to be quite strong.
[20:34] So let's just give it a value of 15 for now.
[20:39] And we can change it later on.
[20:43] And what I want to also add is another wrangle.
[20:46] And this one will be a control just for the direction.
[20:51] I want to be able to kind of control the up and down if we need to make some tweaks for
[21:00] the particles later on.
[21:03] So for this, we can use a vector.
[21:08] We call it deer for direction.
[21:13] And let's just set.
[21:16] And we'll use a zero for the x.
[21:20] We'll use a channel float for the y, which will be the up and down.
[21:24] So let's just call it up.
[21:29] And we'll use zero for the z.
[21:35] And we want to apply it to our velocity.
[21:38] So we'll do v at v plus equals deer.
[21:46] And let's just create this.
[21:50] And you see what we have now is we have this control that moves everything up and down.
[21:58] So we'll just leave it at one for now.
[22:00] And we can drop down the pop net.


### Botnet [22:08]
**Transcript (timestamped):**
[22:09] Before we start on the pop net, you can see just calculating all these frames.
[22:17] Let's just have a quick look and decide when we want to start emitting the particles.
[22:33] So maybe frame 1068.
[22:38] Let's just go over here and set the start frame.
[22:52] Now another thing we can do is you see when we go inside the pop net, we can't see what's
[22:57] happening outside.
[23:00] And it's kind of helpful to see everything in context.
[23:14] Let's just pin the view over here.
[23:18] And now we can go inside and start working on it.
[23:29] The first thing I want to do is let's just go over here to the source and adjust the
[23:36] life of the particles.
[23:38] We want to be something quite small.
[23:41] Let's use maybe 0.1.
[23:49] And let's give just a tiny variance as well.


### Breathing Fire [23:58]
**Transcript (timestamped):**
[23:59] We also want the dragon to stop breathing fire eventually when he finishes his animation.
[24:16] Maybe on this frame.
[24:17] So let's just go over here on the constant activation on type $FF is smaller than 1000
[24:28] and 106.
[24:41] And you see now he stops breathing the fire.


### Particle Speed [24:48]
**Transcript (timestamped):**
[24:49] I also want to go over here and just basically want the particles to go faster.
[25:00] Maybe three.
[25:05] Maybe a bit more.
[25:15] Because I want the particles to actually interact with the ground as well.


### Keyframing [25:22]
**Transcript (timestamped):**
[25:23] So this looks good.
[25:27] But you can see the first frame is kind of too strong.
[25:34] We can actually just key frame it.
[25:40] So let's give it one key frame at the frame 1070.
[25:46] And on the first frame let's just take it down to maybe 3.5.
[25:52] This way we get this kind of shorter burst.
[25:56] And it just ramps up a bit as he starts breathing the fire.
[26:05] Now another thing you can see here.
[26:08] We get this kind of stepping.
[26:11] So let's just go out and give it a few more sub steps.
[26:17] We can try it with two.
[26:20] You see this is better.
[26:24] But still we got these stepping issues.
[26:29] Let's just give it four stop steps.
[26:31] It's quite a simple simulation anyway.
[26:37] And that fixes it.


### Gravity [26:43]
**Transcript (timestamped):**
[26:44] Now another thing I wanted to incorporate from the reference is just adding some gravity.
[26:50] So we get kind of an arching shape.
[26:55] So let's just add a pop force.
[27:03] And let's give it something quite large.
[27:07] And it's 50.
[27:12] Because everything is moving so fast we probably won't even see it.
[27:17] But I do think it kind of gives us a slight arching shape here.


### Collisions [27:28]
**Transcript (timestamped):**
[27:28] Now what I want to do is let's just bring in the collisions because you can see it's
[27:34] going through the ground.
[27:37] So let's drop down static object.
[27:46] And over here let's just go to collision terrain.
[27:52] Over here we'll select the geo.
[27:55] For the object path let's just select collision terrain.
[28:03] And over on the collisions tab we just need to go and change the mode to volume sample.
[28:12] And then in the proxy volume we just select the VDB.
[28:21] And let's just merge it together.
[28:50] Now let's just remove this.
[28:53] We don't need it to display.
[29:00] Another thing that's happening here it's just importing the collision object as well.
[29:05] So let's just do here a pop object.


### Pop Drag [29:13]
**Transcript (timestamped):**
[29:14] And this way it only imports the particles.
[29:18] Like it will import this pop object.
[29:26] And you can see we're actually getting some collisions here.
[29:36] I want them to stay quite close to the ground.
[29:41] And not kind of spray upwards like this.
[29:47] So what we can do here is let's just add a pop drag on these particles.
[29:54] So to do this we need to go to the pop solver and if we'll go to collision behavior we can
[30:05] just create a group for the hit particles.
[30:10] So we'll just call this hit.
[30:15] And over here we can just add a pop drag.
[30:24] And then just tell it to use the hit group.
[30:29] So any particle that hits the ground it goes into this hit group.
[30:35] And then we apply this pop drag onto it.
[30:39] So let's just use 0.4 for now.
[30:51] Let's just try something really big just to see that it's working.
[31:00] Can definitely see everything is sticking to the ground.
[31:05] Let's just use 0.4 for now.
[31:13] And just see if it's too much we can always increase this later on.
[31:22] Now that we have this particle system working you can see it's starting at the correct time.


### Noises [31:44]
**Transcript (timestamped):**
[31:53] And it stops according to the animation.
[32:00] What I want to do now is just apply some noises and kind of create a more interesting source
[32:08] for the pyrocym.
[32:12] You can try and do it inside the pop net but it's much easier to keep it simple over here.
[32:19] And then apply all these kind of noises afterwards.
[32:23] So let's just start by dropping down a trail.
[32:33] And let's just give it a length of 4 and lower the increment to 0.5.
[32:42] And this just gives us some more points and it makes it a bit wider as well.
[32:49] Now a small thing you can see it takes everything a bit down so if we just use a transform we
[32:57] can just bring it back to the center.
[33:05] So maybe 0.2.
[33:10] And now I just want to create lines from these points.
[33:13] So let's drop down an add and we'll use the particle IDs to connect these points.
[33:25] So let's go to polygon by group and if you go to by attribute you can just use the particle
[33:32] ID.
[33:35] And then we get these lines connecting the points.
[33:47] Let's drop down a resample and resample these lines.
[33:53] And you can see we're just getting much more points now.
[33:59] And I also want to create a curview attribute.
[34:06] This is an attribute that gives you a value from the start of the line to the end of it.
[34:12] So we have 0 over here and by the end it will be 1.
[34:16] So we can kind of use it to control some of the noises.
[34:26] And now we can just drop down a point pop.
[34:34] And inside here we'll just, let's call it just add noise.


### Antiallies [34:43]
**Transcript (timestamped):**
[34:44] And let's just go inside here and start setting up the noise that we want to use.
[34:52] Let's drop an anti-alloy noise.
[35:01] And we can just connect it to the position with an add.
[35:15] And let's just make the amplitude a bit higher.
[35:21] And you can see it's acting a bit strange so we need to change it to be a 3D noise and
[35:28] this gives us the correct behavior.
[35:39] Now what I want to do, I don't want the noise to be applied near the mouth.
[35:47] If we remember the reference we want it to be kind of a straight stream over here.
[35:55] So what we can do is we can use the age and the life.
[36:01] And when the particle is birthed the noise will be lower and when it dies it will be
[36:09] the strongest.
[36:10] So to do this we just drop down a divide.


### Mold Amp [36:18]
**Transcript (timestamped):**
[36:18] And if we divide the age by the life we get the normalized age.
[36:28] And now we can just plug this into our amplitude.
[36:35] You can actually see it's straight over here.
[36:40] And as the age goes up the noise becomes stronger.
[36:47] Now let's drop down a control for this.
[36:49] So we'll just drop down a multiply.
[36:55] And drop down a parameter for this multiplier.
[37:05] Let's call it a MULT, AMP.
[37:12] And if we go outside here we can just give it a higher number.
[37:18] And you can see the way it's not affecting the positions over here.
[37:24] And over here it's much stronger.
[37:26] So let's just use 8 for now.
[37:31] And yeah, let's add another control for this.


### Curve View [37:37]
**Transcript (timestamped):**
[37:44] We can actually just bring in the curve view that we created before.
[37:49] So if we use a bind and choose a curve view we get this value from 0 to 1 depending on
[38:00] the length of the line.
[38:07] And then we can just drop down a multiply and just multiply the noise by this value
[38:13] as well.
[38:20] And just so we have control over it we can just use a ramp.
[38:29] And let's just use a spline ramp.
[38:31] And we'll call it ramp curve view.
[38:45] So you see if we play around with this ramp.
[38:55] We can actually kind of control the shape of it.
[39:04] But let's just set it like this for now.
[39:19] And I just wanted to make these values available outside.
[39:25] So let's just right click and create input parameters.
[39:33] So let's just check what kind of frequency will work.
[39:41] I think one was actually quite good.
[39:48] Let's use a 1.2.
[39:52] And we can also add some animation to the offset.
[39:56] So let's just type in dollar t four times by five.


### Creating the Source [40:09]
**Transcript (timestamped):**
[40:10] So it looks like it's working nicely.
[40:14] And you can just see this shape is much nicer as a source as opposed to this straight line.
[40:24] So just by using this shape with the PyroSIM we'll get much more interesting results straight
[40:30] away.
[40:35] Let's create the source now.
[40:36] So drop down a PyroSource.
[40:49] And over here we just want to initialize burn.
[40:52] So this will give us the burn and the temperature attributes.
[40:58] And another thing you can see here we're losing quite a bit of the detail.
[41:04] So let's use a surface scatter.
[41:12] And this will just scatter points on the shapes that we have over here.
[41:19] Now you can see it's quite slow just to move between the frames.
[41:25] And we just have way too many points.
[41:26] Like almost two million.
[41:29] So let's just lower the particle separation a bit.
[41:37] You can just lower it until you see it affecting the shape.
[41:41] So this is maybe a bit too much.
[41:46] This is much more reasonable.
[41:51] And you can just see moving between the frames.
[41:53] It's much faster as well.
[41:59] So now we can just drop down our volume rasterize.


### Rasterizing [42:08]
**Transcript (timestamped):**
[42:09] And let's connect it.
[42:13] And we want to rasterize the burn and the temperature.
[42:28] And just see first of all the particle scale is way too big.
[42:34] We're actually losing all these shapes.
[42:37] So let's just lower it down.
[42:49] And use maybe 0.16.


### Checking Velocity [43:02]
**Transcript (timestamped):**
[43:03] And let's also duplicate this.
[43:06] And we'll use this one for the velocity.
[43:12] I usually prefer to do the velocity separately just so I can easily check it.
[43:19] So if we drop down a volume trail and drop down a scatter.
[43:28] So we can actually take, create points inside our volume, connect it and connect it to the
[43:40] velocity volume here.
[43:50] And you can just see that everything is working properly.
[43:55] And we have proper velocities.
[43:58] So let's just merge these volumes together.
[44:07] And now we can just plug it into a power solver.


### Making Adjustments [44:16]
**Transcript (timestamped):**
[44:17] Let's start working on the power solver now.
[44:21] So just highlight it.
[44:23] And I've actually let it calculate for a few frames.
[44:27] Just so we see that everything is working.
[44:31] And you can see we're getting quite nice looking shapes straight away.
[44:38] But yeah, let's start making some adjustments.
[44:41] The first thing I've noticed is we're hitting the bounds of the sim.
[44:47] So if we just go to the bounds tab and over in the padding, you can just give it something
[44:53] quite large, maybe like 10.
[44:59] And this just gives it much more room to actually expand and move about.
[45:05] And we won't need to worry about it hitting the edges.
[45:11] And another thing I want to change is just the start frame.
[45:15] You can see currently we're just calculating all these empty frames.
[45:19] So we can actually take the start frame from the pop sim.
[45:25] So just copy this parameter.
[45:29] And over here just paste relative references.
[45:36] And now the sim will start at this frame.
[45:47] Now I'll just let it run for a few more frames so we actually see what's happening.
[45:54] Let's just go to the setup tab and give it a larger voxel size.
[46:09] So maybe 0.25 for now.
[46:15] And this is just so we can actually work faster.
[46:19] So straight away we can see we're getting the velocities are just too high.
[46:28] Let's also switch to smooth shaded just to remove this banning box.
[46:35] But yeah, you can see the velocities are really high and we're getting these kind of blobby
[46:43] mushroom shapes.
[46:47] So let's just go to the sourcing tab and change the velocity, the incoming velocity to 0.25.
[47:18] Another thing I can see here is just the buoyancy.
[47:21] It's like barely rising and it's fire and it's hot so it should move a bit upward.
[47:33] So let's just go to the shape tab and let's just give it a buoyancy of 2.85.


### Creating a Camera [47:46]
**Transcript (timestamped):**
[47:46] Also just want to let's just create a camera to kind of frame the action and so we can
[47:57] actually iterate it.
[48:01] So maybe something like this.
[48:05] Also let's press D and go to the background and switch to a dark background.
[48:16] Maybe something like this.
[48:18] Now you just press control and click on this camera and it will create a camera in the view.
[48:37] Let's just create a flipbook.
[48:44] Let's make sure to leave play bar at the last frame and remove this resolution.
[48:52] And let's hit start.
[48:59] Let's just stop this and just set the start frame to be 1060.
[49:29] And I can see here a few problems straight away.


### Problems [49:36]
**Transcript (timestamped):**
[49:43] One of them is we actually need more subsets here just because everything is like we have
[49:50] quite a strong velocities coming in and everything is also moving quite fast.
[49:57] So you can see this kind of stepping we're getting.
[50:02] You get this kind of big blobs and it's as if there's not enough information inside
[50:10] the sim.
[50:14] And another thing that's happening here.
[50:17] It's rising a bit too much in my opinion because I do want to stay kind of close to
[50:23] the ground.


### Setup [50:28]
**Transcript (timestamped):**
[50:29] Let's just lower the reference temperature to 2000.
[50:36] And over at the setup tab let's just give it some more subsets.
[50:39] So we'll give it a minimum of 2 and a maximum of 3.
[50:50] And I also want to bring in the collisions.
[50:54] So we wanted to collide with the ground and also with the dragon head.
[50:58] So let's just drop down an object merge.
[51:07] And we'll select the VDB.
[51:13] And let's duplicate this and bring the VDB head 1 for the dragon.
[51:25] Now drop down a merge and connect these two together.
[51:31] And now we plug this into the collision section here.
[51:41] And just on the power solver you just need to go to the collision tab and switch it to
[51:46] use SDF plus volume velocity.
[51:52] So let's run a new flipbook and see what we get.


### Flipbook [51:54]

### SIM Comparison [52:05]
**Transcript (timestamped):**
[52:06] I've just stopped the sim.
[52:10] So we can actually compare the two different versions.
[52:14] And you can just see straight away we're getting all these stepping issues are kind of gone.
[52:22] Not completely but it's much better than before.
[52:28] And it just fills up all this volume and it actually also adds more detail inside the
[52:35] sim.
[52:36] You can see over here.
[52:39] We're now getting all this.
[52:41] And this is just by adding some more sub step.


### Ground Explosion [52:45]
**Transcript (timestamped):**
[52:46] So the next thing we can do is just go to the shape tab and start adding some disturbance
[52:53] and turbulence and shredding and just kind of work on the look of the sim and try to
[53:02] add more details.
[53:05] But I'll just show you what I kind of like doing in these situations.
[53:11] I kind of like using the shelf tool.
[53:15] We just tap ground explosion.
[53:19] So we have this Pyro configure ground explosion.
[53:24] Let's just drop it in.


### Pyro [53:28]
**Transcript (timestamped):**
[53:29] And it just builds up this setup for like this kind of preset ground explosion.
[53:38] But what we want to take from this is let's just take this Pyro.
[53:43] This is a Pyro bake volume just for the look.
[53:48] And I also want to take this solver because it just has in it all kinds of nice presets
[53:58] can also delete all this here.
[54:08] It's kind of already figured to give some nice looking results straight away.
[54:13] And we can just plug it in.
[54:26] And yeah, let's just get rid of all these keyframes.
[54:29] We don't need them.
[54:30] We know our time scale needs to be 0.75.
[54:35] Let's lower the voxel size to 0.2.
[54:40] The start frame can just take it from here.
[54:46] Copy this parameter at the start frame like this.
[54:55] That's for the subsets that set it to be 2 and 3.
[55:03] And also in the shape WC they have kind of these keyframes.
[55:08] Let's just delete them.


### Flip Book [55:16]
**Transcript (timestamped):**
[55:17] And you know, just run a flipbook just to see what we're getting with this kind of with
[55:23] these settings.
[55:27] And I'll just pause the video and come back when it's done.


### Sim [55:34]
**Transcript (timestamped):**
[55:35] So I'll just stop the sim over here.
[55:37] You can already see there's a few things that we want to adjust.
[55:46] But you can see it's already feeling much more explosive and it billows out and just
[55:53] feels a bit more violent and massive in scale.
[55:58] And that's mostly because we have some flame expansion and we also have some divergence
[56:07] that is helping it expand like this.
[56:11] But actually you want to just remove this.
[56:15] We also have the velocity here.


### Adjustments [56:17]
**Transcript (timestamped):**
[56:21] Let's just switch it to add and lower it to 0.25 like we had before.
[56:32] That's for the burn that just set it to 1.
[56:38] We don't have these trails so we can remove this.
[56:43] And we also don't have density.
[56:44] We have a burn field coming in.
[56:46] So let's just switch this to burn and then we'll get some smoke, just a small amount
[56:52] that might add some nice details.
[56:59] As for the dissipation, we want something quite high because I don't really want any
[57:04] smoke here.
[57:12] And the temperature can also be quite high.
[57:14] We want it to kind of cool off quite fast and stop rising up.
[57:28] And as for disturbance, you can see right now the block size is set to 0.2.
[57:35] Now if we go out and just create a box and we'll just move it near the dragon head just
[57:47] where the fire is located.
[57:54] You can see this is a size of 1 and currently it's set to 0.2.
[57:59] So this tiny dot is the disturbance size and it's way too small and we actually won't really
[58:05] see anything unless we have a really high resolution for the sim.
[58:12] So we can go for something a bit bigger like maybe 0.4 or 0.5.
[58:22] So for now let's just double it to be 0.4.


### Disturbance [58:29]
**Transcript (timestamped):**
[58:30] Another thing we can see here is just we barely see any break up.
[58:36] So let's give it a much higher disturbance.
[58:39] So let's set it to 75 for now.
[58:45] You can see this preset also gives us like it actually turns on the speed field and it's
[58:53] at these kind of controls for this speed field that when it's moving slower you get less
[59:02] disturbance.
[59:05] And we can adjust these values as well but let's just leave it for now.
[59:12] As for the turbulence, I actually want it to be really low.
[59:18] Usually I use turbulence only for simulating kind of large swirls of air moving.
[59:26] So I tend to keep it quite low maybe 0.1.
[59:31] And as for the swirl size, currently it's set to 15 which is really big so it will give
[59:38] us these kind of movements.
[59:45] Maybe 4 would be a good value for the turbulence.
[59:49] So let's set the swirl size to be 4.
[59:58] And for the shredding, you can actually just give it a higher value as well.
[60:07] And let's just run another flipbook.
[60:21] I'll just stop the sim here.
[60:30] Trying to feel really nice.
[60:32] We get this kind of rolling effect for the fire.
[60:38] I actually feel like I want this area to be a bit bigger as well.
[60:45] So we can just control this by the flame expansion.
[60:53] So I'll maybe set it to double like 1.5.
[61:06] Maybe lower the flame range to 0.5.
[61:14] And at this stage I actually just want to see how it looks like with a higher voxel size.
[61:24] So let's just set it to 15.
[61:29] And I'll just run a new flipbook.
[61:39] The sim is still going but you can see it's looking quite good.
[61:46] I really like all this rolling fire that we're getting here.
[61:55] And let me just stop the sim here.
[62:03] And another thing we can do is if we want to see a bit more detail, we can just press
[62:07] D and go to the texture tab.
[62:11] We have this limit resolution for the viewport.
[62:16] Depending on your graphics card, you can just remove this or set it to something a bit higher.
[62:22] Maybe 500.
[62:25] And this will actually allow us to view higher resolution volumes in the viewport.
[62:30] So just to refresh the view, we can move one frame back.
[62:35] You can just see everything looks a bit sharper.
[62:40] And you can just see the detail a bit better like this.
[62:45] Just before we cash this out, I want to make a few more small tweaks that I think we can
[62:53] get some more detail out of this.
[62:56] And there's a few things I've forgotten to adjust.
[63:01] So first of all, we can adjust the balance.
[63:04] We used 10 before.
[63:06] So let's just switch it to 10.
[63:10] And also for the collisions, just switch it to SDI plus volume velocity just so it will
[63:19] be using the VDBs here.
[63:34] Over in the fields, like what I see here is we're kind of getting quite a lot of smoke.
[63:43] And I want it to be mainly fire.
[63:44] So just the emit form flame.
[63:48] Let's lower it.
[63:54] And also let's lower the range a bit.
[63:59] Something like that.
[64:07] This seems to be fine.
[64:15] And the buoyancy we used before is 285.
[64:19] So let's just set this.
[64:27] And in the disturbance, we can just maybe add a bit more roughness just to make it a
[64:33] bit more chaotic.
[64:36] And also the speed range.
[64:39] And just set it to be zero maybe.
[64:51] So it will always affect some of the smoke, even if it's really slow.
[65:00] Because you can see it's kind of staying quite static at some points.
[65:06] Over here.
[65:07] It's barely moving.
[65:10] So we want to keep on affecting it.
[65:16] Now for the turbulence, we can also give it a bit more roughness.
[65:27] And for the speed field, maybe make the range a bit larger.
[65:34] Because you can't see it kind of affecting it here.
[65:40] You can see how it kind of swirls it about.
[65:47] I feel like it's a bit too strong.
[65:50] So you can just make the range a bit larger.
[65:53] That will help it.
[65:57] And for the shredding, you can see the block size.
[66:00] I haven't actually touched it.
[66:01] So let's just give it something a bit bigger.
[66:07] We're using 0.4 over here.
[66:10] Just make it a bit bigger than the disturbance.
[66:17] And also let's give it a bit more roughness.
[66:25] And yeah, and also for the flame expansion.
[66:32] I kind of feel like this range is too high in a way.
[66:42] I want it to expand a bit more.
[66:45] And just below out a bit more.
[66:48] Let's just set this to be 1.
[66:54] And this maybe 0.35.
[67:04] And yeah, just another thing I wanted to adjust here.
[67:07] We can just change that Vection type here.
[67:12] If we switch it to BFECC, it's just a different type of calculation.
[67:20] And I kind of feel like it gives, in a way, a bit more details.
[67:25] And it just helps the simulation kind of roll on itself.
[67:29] And because it's fire, I also like to, I want to add two more microsolvers.
[67:34] It will be Vortex Boost and Gas Vortex Confinement.
[67:41] And what they do, again, they just affect the way the swirls work.
[67:49] And the rolling motion.
[67:51] It's like a Vortex Boost that just kind of finds Vortexies.
[67:57] And it just boosts their strength.
[68:01] So we'll just get some more rolling details.
[68:04] So to do this, let's just go inside the solver here.
[68:11] And we have this force output.
[68:15] And here we just need to use Gas Vortex Boost.
[68:22] And we can add the Gas Vortex Confinement.
[68:28] And if we just merge these together and connect them, they will be added to the sim.
[68:40] So for the Vortex Boost, we can just, you can see we can adjust the swirl size and the strength of it.
[68:48] But let's just leave it at the default.
[68:53] And for the Confinement, I just let's set it to 1.
[69:02] And I'll just run one more sim before we cash it out.
[69:07] Just to see these kind of changes.
[69:14] I've just stopped the sim here so we can compare the two versions.
[69:19] And you can see just doing these kind of small adjustments.
[69:23] I think the flame expansion really makes a big difference.
[69:27] You can see especially here, this one is much more explosive.
[69:33] And we also get some nicer detail here, just a bit more breakup on the shapes.
[69:40] And I think if we just play them together, this just feels much more large scale.
[69:52] And much more powerful.
[69:54] You can actually feel it kind of slowly moving along.
[70:03] Even here, you can see all the detail inside the fire.
[70:13] It just feels much better.
[70:15] So let's start.
[70:18] We can delete this old power solver.
[70:23] And let's just call this one Dragon Fire.
[70:33] Let's connect the file cache.
[70:42] Switch it to Vexplicit.
[70:46] And switch the Hip to Job.
[70:51] And inside the Geo folder, I just want to call this one Dragon Fire.
[70:59] And inside the Geo folder, I just want to create another folder named Shot01.
[71:06] So all of the caches for this shot will be in one folder.
[71:14] And I want this cache to be in its own folder as well.
[71:17] So we'll just do doraOS.
[71:20] So this way we create a folder with this name.
[71:25] And then the file names will have this name plus the frame number and the BGO.
[71:32] So let's just change the name here to be Cache Dragon Fire 01.
[71:44] Let's just start caching this.
[71:45] And I just want to show you the difference between caching a sim like this
[71:53] as opposed to caching it as a VDB and just applying some optimizations to it.
[71:59] So let me just stop it here.
[72:06] And if I go to my Geo folder, we have now a Shot01 folder.
[72:11] We have this folder here.
[72:15] And let's just look at the frame 1077.
[72:21] It's 57 megabytes.
[72:25] And if we look on the power solver, we have this output tab.
[72:32] And it has this post-process options.
[72:39] And this is basically exactly the same as we have this node, Pyro post-process.
[72:47] You can see it has the same settings.
[72:50] They just incorporated it into this power solver.
[72:55] And yeah, we have this checkbox to convert it to a VDB.
[73:00] What this does, it takes all the empty voxels and kind of gets rid of them.
[73:07] You can also use a 16-bit float.
[73:10] This converts it down from 32 float.
[73:15] And again, with no visual difference, you get much smaller file sizes.
[73:22] And another big offender is just the velocity volume, which can be quite heavy.
[73:32] So if we resample it down, you can save a lot of space like this.
[73:38] So we can do it by two times, but we can also do it by four.
[73:44] And the only thing it affects here is the way it looks when rendering with a motion blur.
[73:50] And with the test size done, it's barely noticeable.
[73:55] And over in the file cache, just change the ending here to VDB.
[74:03] So let's save it again.
[74:07] And just compare the file sizes.
[74:10] And you can see the same, these are the same frames.
[74:16] And now it's only like two megabytes, as opposed to 58, which is quite crazy.
[74:23] So always use these settings when saving out your sims.
[74:31] Especially in a big project like this, where we have a lot of smoke and fire.
[74:37] And if you're also happy with your sim, let's just go over to the solver here.
[74:44] And just switch the voxel size to 0.1.
[74:49] And save it out like this.
[74:55] The sim has finished caching.
[74:57] And I've just added this null here.
[75:01] And I've just added this null here.
[75:03] And I'm also viewing the sim through this PyroBake volume.
[75:09] And yeah, this is just to get some nicely looking shading in the viewport.
[75:15] And another small change is I went to the voxel size and change it to 0.15.
[75:22] And that's just because I wanted the sim to finish faster.
[75:27] Just because I want to continue working.
[75:31] For next week, I will resim this at a value of 0.1.
[75:35] So we will get nicely looking flames and details in general.
[75:42] And I've also created this flipbook here.
[75:45] Just so we can see how it turned out.
[75:48] And I'm quite happy with the result.
[75:50] It's looking quite powerful.
[75:54] And we're also getting some nice motion for the flames and all these kind of details.
[76:04] And of course, it will look even better once we resim this.
[76:09] That's it for the dragon farm.
[76:13] If we go out now, let's just give this node a purple color.
[76:19] And this will represent our sims and setups.
[76:24] So I just hope you enjoyed this section and I'll see you in the next video.
[76:32] Let's continue and start creating the setup for the groundfire.
[76:37] So for this, let's drop down a new geo.
[76:41] And we'll call it FX Groundfire01.
[76:47] And let's also give it a purple color.
[76:54] First of all, we need to create the source.
[76:58] And for this, we're going to need the terrain and this dragonfire.
[77:03] So let's drop down an object merge.
[77:09] And let's bring in the dragonfire.
[77:14] And also let's bring in our terrain.
[77:18] So for the terrain, let's go to the collision terrain and bring in the geo.
[77:38] And now what we want to do is we want to transfer some information from this volume to this terrain.
[77:46] So to do this, we have a node called attribute from volume.
[77:58] And here we just give it the terrain and the volume.
[78:04] And let's just turn off the fire.
[78:06] And you can actually see where it's hitting the ground.
[78:10] We're getting this color.
[78:17] We want the flame.
[78:24] And it's currently set to a size of three.
[78:27] We can set it to be one.
[78:29] And that will be a number of different colors.
[78:32] And also in the infant range, let's also just take the range down.
[78:37] So we'll get like a stronger colors.
[78:45] And you see we're getting this kind of leading edge according to the fire.
[78:52] And we're getting this kind of leading edge according to the fire.
[78:57] But there are a few problems.
[79:00] Mainly we can see just the point counts are all over the place.
[79:07] We have different resolutions.
[79:14] So first of all, let's just fix this terrain and try to get the terrain.
[79:21] And first of all, let's just fix this terrain.
[79:27] And try to get a more consistent source.
[79:33] So instead of the geo, let's bring in the VDB.
[79:45] And now we can just convert it back to polygons.
[79:51] And you can see this kind of brings everything back to the same resolution.
[80:07] And now we can just remove all this bottom part.
[80:12] So let's just drop down a clip.
[80:22] And let's lower the distance a bit.
[80:31] Let's try minus two.
[80:36] And this can work.
[80:40] And now if you just drop down a scatter.
[80:42] And let's give it quite a few more points.
[80:54] You can just see the distribution now is even.
[80:58] And yeah, it's much better.
[81:02] So let's just remove this relax iteration and give it a lot more points.
[81:12] So let's start with this number seems to be seems to give a good coverage.
[81:20] And it also retains the detail.
[81:26] And if we have a look at the attribute from volume now, you can see it's working with the points.
[81:37] And we're actually getting a bit more detail as well.
[81:46] And what I want to do now is let's just delete all these black points.
[81:51] We don't need them.
[81:52] So drop down a blast.
[81:55] Set it to points and let's type at CD smaller than 0.01.
[82:10] And now we're only left with these white points.
[82:17] Now in order to just paint this section, we can just use the white points.
[82:24] We can use a pop net.
[82:28] And basically just emit particles wherever the white points appear.
[82:37] So let's just go inside.
[82:39] I'll just set the start frame to be 68 here.
[82:48] And inside the pop net, if we just go to the emission type,
[82:53] we can set it to use all points.
[82:55] This way just emits particles on each of the points.
[83:02] And we can also go over here to just remove overlapping and just set it to with existing.
[83:10] And then we won't get any overlapping points.
[83:14] And you can see we're getting this kind of source being painted on.
[83:27] And of course it's all being affected by the fire.
[83:38] What we can do now is just drop down our pyro source.
[83:45] And for the fire, I just want to use density.
[83:55] Now you can see we also get all these attributes from the pop net.
[84:00] So let's just clean this before we move forward.
[84:04] We'll use an attribute, delete.
[84:11] And let's just remove everything.
[84:14] And we can also delete these groups, but it doesn't matter.
[84:30] Let's just press on this density.
[84:35] And currently everything is red just because the density is at 1.
[84:41] Now that we have these points and the source is kind of ready, let's start working on the pyrosolver.
[84:50] And let's try and get some nice looking flames and then we can apply it to this source.
[84:58] So kind of like what we've done in the dragon fire, I want to use one of the presets that comes with Houdini.
[85:07] So let's drop down our pyro configure.
[85:11] And you can see Houdini comes with all these kind of presets.
[85:17] And I'm using this mostly just to save time.
[85:20] Let's drop down our bonfire preset and see what we get.
[85:29] I'll just let it run for a bit.
[85:33] But you can see it just gives us this kind of fire setup with all kinds of values dialed in that give kind of a good starting point.
[85:45] And yeah, it can save you time.
[85:47] You don't need to create everything completely from scratch each time.
[85:53] And if you just go in and make a few tweaks and changes, we can get something that looks really good.
[86:03] Let's just go over what we get here and see how they build it and make our changes.
[86:20] Now if we just take a look at the setup here, all this stream here is just meant to add some embers.
[86:30] We don't really need it. So we can just delete everything here.
[86:41] And if we just take a quick look at what's happening here, you can see we have this tube as an emitter.
[86:49] And we have a pyro source creating some attributes.
[86:55] And then we have these attribute noises, which basically just give some variation to the source.
[87:08] We have one of them for the density, one for the temperature and one for the burn.
[87:13] Now just to keep this setup simple, I kind of prefer just to use one attribute, which is going to be the density.
[87:22] So I'll just delete these two.
[87:32] And then we just use a volume rasterize to convert these points to a volume.
[87:43] If we take a look at the size of this compared to the source that we have,
[87:50] it's quite small.
[87:56] This voxel size is way too small.
[87:59] So I'll just switch it to something a bit bigger and also for the pyrosolver.
[88:07] Let's just switch to a voxel size of 0.1 for now.
[88:20] Let's also take just a section of this source.
[88:27] So maybe this amount.
[88:33] We want to work on a small size just so it will be faster and we can kind of dial in the look.
[88:41] And then we can create the same for the whole sequence.
[88:49] So just for testing, let's drop down a timeshift node.
[88:56] Just delete these channels.
[89:00] It will freeze the source in place.
[89:09] And we can use this one.
[89:12] So let's just connect this attribute noise.
[89:16] We can delete these two.
[89:20] And you can see here the noise is way too small.
[89:26] Let's just use maybe 1.5.
[89:38] And you can see we have this ramp here.
[89:41] And just play around with it a bit.
[89:47] Maybe switch it to Beastline.
[89:54] And we can kind of make it a bit more contrasty like this.
[89:59] We can also give it 0.75 for the roughness.
[90:10] So it will be a bit more interesting.
[90:16] Now in the volume rasterize, let's just delete everything except for the density.
[90:29] Also, let's make sure that on the sourcing tab, you can see right now it's looking for a temperature field and a burn field.
[90:54] So let's just switch it to be density.
[91:00] And now we're getting the fire.
[91:07] So I'll just let it sim for a bit and we'll see what we're getting.
[91:16] The first thing I see here, we're getting smoke.
[91:21] And I actually want it to be a smokeless fire.
[91:29] So first of all, let's just delete these densities that are coming in.
[91:38] And if we run it again, we're still getting this black smoke.
[91:46] So if we go to the fields tab, we have this density section.
[91:52] And this emit from flame basically creates smoke from the flame.
[91:58] Let's just turn it off.
[92:05] You can see now we're getting just fire with no smoke at all.
[92:11] So that's good. I'll just let it run and we'll see what we get.
[92:16] I've just created a new flipbook so we can actually see how the fire is behaving.
[92:24] And you can see currently it's just moving really slow and it feels really calm.
[92:32] And what I imagine for this fire is we want to create something that feels really big and chaotic.
[92:40] Because it is being lit by dragon fire, which is supposed to be something really hot and powerful.
[92:48] And we also have this big dragon here that's just landing.
[92:53] So I would assume the wings will create strong winds and vortices as well.
[93:00] So let's start adjusting some of the values here and just try and improve this.
[93:09] We can start by going to the setup tab and let's just make the time scale a bit higher.
[93:16] So use 1.5 just so everything will move a bit faster.
[93:23] And for fast moving simulations, we also really should give a few more subsets.
[93:30] So let's just use 2.
[93:32] And you can see the speed that everything is moving up is quite slow.
[93:42] So let's just go to the shape tab and we have the buoyancy here.
[93:48] And buoyancy basically just controls the strength and the speed that the fire is being pulled up.
[93:55] So let's use 1 for now and see how it feels.
[94:02] And you can also see we get this flame expansion and viscosity.
[94:07] Now viscosity basically tells the flames to kind of stick together and create one big shape.
[94:15] So it can work for maybe smaller scale fire, maybe like a match or a big fire.
[94:22] But with this kind of large and chaotic fire, I want these big licks of flame to break apart and give us all kinds of small detail.
[94:31] So let's turn the viscosity off.
[94:34] And we also want to turn off the flame expansion.
[94:38] Flame expansion is a way to help mostly smoke, but it's not a big deal.
[94:44] And it kind of makes everything below out as time progresses.
[94:50] Let's turn these two off.
[94:58] And you can see straight away everything is moving up and down.
[95:03] And you can see that everything is moving up and down.
[95:07] And you can see that everything is moving up and down.
[95:11] And you can see straight away everything is moving faster.
[95:16] We're also getting these nice breakups now, just by removing the viscosity and the flame expansion.
[95:24] So we're actually getting a bit more smaller details inside the flame.
[95:32] But what you can also see here is just the source. It's quite boring.
[95:37] I think if we play around with the noises a bit and just add a bit of animation and maybe inject some velocities,
[95:46] we can just break it up a bit and give it a more chaotic look.
[95:54] So let's just go over here to this noise and visualize the density.
[96:02] Also just create a camera so we can keep creating flipbooks from this view.
[96:11] Just uncheck this lock.
[96:19] Let's maybe add, give it a higher amplitude.
[96:25] And what I want to do now is I kind of like these shapes, but I don't want them to change.
[96:33] I want to add animation on top of them.
[96:36] So if we just duplicate this noise and let's just give it an amplitude of one.
[96:48] And we can also remove this ramp.
[96:50] So I want this second noise to kind of affect these initial shapes.
[96:58] And we can add the animation on this one.
[97:01] If we just go to the animation, turn it on.
[97:06] Let's just see what we're getting.
[97:08] And you can see it just makes it a bit more dynamic.
[97:13] Let's increase the false length to 0.3.
[97:21] And also let's make the element size smaller by half.
[97:31] You can see here we're kind of retaining these shapes,
[97:35] but just adding some animation on top of them.
[97:42] And we can also maybe just increase the amplitude a bit more.
[97:52] And this looks a bit better.
[97:55] Another thing to note is because we increased the amplitude here,
[97:59] if we check the spreadsheet here,
[98:01] we can see now we're getting densities in a range of 0 to 10.
[98:07] And I want to keep the densities in a range of 0 to 1.
[98:11] So to do this, we just can just go to the post-process tab here.
[98:19] Let's just turn it on.
[98:21] You can see now we're getting densities, like our highest density is 1.
[98:25] So let's just turn it on.
[98:27] You can see now we're getting densities, like our highest density is 1.
[98:36] Let's also duplicate it again.
[98:41] But this time let's use it on a velocity field.
[98:50] So even if we don't have a velocity attribute here,
[98:54] just by adding this attribute noise and specifying v,
[98:59] we'll get this v attribute, which is for velocity.
[99:06] Let's just set it to be a vector.
[99:12] And select operation to add.
[99:16] And we want it to be zero centered.
[99:23] Let's also add some animation.
[99:37] This is quite chaotic and fast, but it might work.
[99:42] Let's use a post-duration of 0.5.
[99:46] And also make the element size smaller, so maybe 0.5 as well.
[100:00] So this should be quite good.
[100:05] Let's rasterize this attribute.
[100:10] So just press V.
[100:15] And just drop down a merge.
[100:21] And merge these two volumes together.
[100:24] So we have density and velocity.
[100:34] Let's just go to our new camera here.
[100:37] And just check that everything is working.
[100:46] Now I don't feel the velocity affecting it at all.
[100:51] You can see the density, like the new values give us more flames, which is good.
[101:04] But if we just go to the, we'll call it noise v,
[101:12] let's just increase the amplitude to 10.
[101:21] And just see it's affecting it.
[101:24] And you can see straight away it's pushing the flames in different directions.
[101:28] So that's good.
[101:36] You can see just by making a few changes to the source,
[101:40] we're getting a much nicer result.
[101:43] It feels more chaotic and we also get some more flames.
[101:49] And what I want to do now is let's add a bit more turbulence,
[101:54] like a large-scale turbulence just to simulate some wind.
[101:59] And we can also play around with maybe adding some shredding
[102:05] just to kind of break up these shapes further.
[102:11] So let's just go to the Shape tab and turn on the shredding.
[102:20] And I know that the value of 15 worked for our dragonfire.
[102:24] So kind of this kind of scene scale.
[102:27] And this value is good.
[102:31] And let's maybe use a block size of 0.1.
[102:36] Just because I want it to be kind of small,
[102:41] like we want small details
[102:43] and we want to break the existing flames to smaller shapes as well.
[102:52] And we can also compare it to the previous flipbook.
[102:56] And you can see the shredding, what it does,
[103:01] it kind of creates sharper-looking flames
[103:08] as opposed to just stop it here.
[103:20] You go to frame 45.
[103:23] You can see the difference.
[103:26] Like here it's a bit more blobby.
[103:30] Or let's find a better frame.
[103:36] Maybe frame 29.
[103:43] You can see all these shapes are basically kind of stretched
[103:48] and kind of like a little bit more.
[103:53] And pull the part.
[103:56] And yeah, it just gives a bit more of a fiery look to it.
[104:04] Now I want to add another turbulence.
[104:06] Now we have this one here.
[104:09] So to add some more microsovers,
[104:12] we just go inside the power solver here.
[104:17] And if we just drop down a gas turbulence,
[104:22] we can add a second one here.
[104:27] I want the scale to be quite strong.
[104:31] And I also want the swirl size to be quite large as well.
[104:35] Maybe set it to 8 for now.
[104:52] Actually it doesn't look like it's even affecting it.
[104:57] So make sure.
[105:00] Yeah, you can see it's set by default to work on the density field.
[105:06] And we want it to work on the flame.
[105:10] Because we don't have, sorry, flame.
[105:14] We actually don't have any more.
[105:17] It's better to directly affect the flames.
[105:21] So let's give it a stronger scale, like maybe 2.5.
[105:25] And just see how it affects it.
[105:33] So you can see straight away,
[105:35] it's definitely a little bit more than 2.5.
[105:39] So let's go ahead and add some more.
[105:43] So you can see straight away,
[105:45] it's definitely pushing things about.
[105:54] If we just go out here,
[105:58] and we have our box.
[106:01] So we can just,
[106:07] maybe 12 will be a good value.
[106:10] Because I kind of want these big rolling motions for the wind.
[106:19] So let's try a value of 12.
[106:34] We can also increase the force length.
[106:38] Because we want it to be quite slow moving.
[106:55] Let me just create a new flipbook.
[106:58] And you can see this turbulence that we added,
[107:02] really gives the feeling of some strong winds in the environment.
[107:07] And I think it's working really nicely.
[107:11] I think in general the fire is almost done.
[107:15] There's only a few changes I want to make.
[107:18] So let's go back to the previous video.
[107:22] And I think we can see that the fire is almost done.
[107:26] So let's go back to the power solver.
[107:30] The first thing is over in the advanced tab.
[107:34] Let's just switch the advection to BFECC.
[107:39] Like we did in the dragon fire section.
[107:43] And also inside the power solver.
[107:47] Let's just drop down a gas vortex boost.
[107:53] And a gas vortex confinement.
[108:03] And I'll just drop down a merge.
[108:06] And connect these all together.
[108:16] And what the boost and the confinement will do is,
[108:21] they will kind of tackle these long licks of flames
[108:25] and break them all apart.
[108:30] So it should give us nicer detail.
[108:35] And just break up all these kind of big shapes.
[108:42] So let's give it quite high numbers.
[108:45] Maybe give it a boost of 4.
[108:51] And for the confinement scale, let's use 10.
[109:06] And I'll just create a new flipbook with a new name.
[109:12] Just so I can easily compare it to the previous version.
[109:21] I'll just let it run and we'll be back once it's finished.
[109:32] I've just stopped the sim here.
[109:36] And you can see now that we've added the vortex boost and the confinement,
[109:41] it really breaks up the shapes and gives us a lot of high frequency detail.
[109:47] And I think also in the movement it just feels much more natural now.
[109:54] And I'll just show you the previous version that we had.
[109:58] You can actually see the difference.
[110:02] I'll just go to the same frame.
[110:07] And you can see where we had these kind of big flames over here.
[110:12] We're still getting them, but everything is broken apart
[110:16] and we just get a lot more detail.
[110:20] So this is looking good.
[110:26] I actually forgot to do it before, but let's just bring in the collisions.
[110:33] So we'll drop down an object merge.
[110:36] And let's just go to the collision terrain and bring in the VDB.
[110:46] And just plug it into the output for the collisions.
[110:52] And over in the power software, let's just go to the collision tab
[110:57] and switch the collision type to SDF.
[111:08] You can see we're getting a lot less fire.
[111:16] Because these points are on top of the ground,
[111:20] when we convert them to a volume,
[111:23] it means half of the size of the volume is inside the ground.
[111:29] So when we bring in the collision,
[111:32] the source is basically half in size.
[111:39] So let's just go to the sourcing tab
[111:42] and maybe increase the flame amount to 1.5.
[111:49] And we can also go to the fields tab.
[111:53] And in the temperature, let's make it cool down a bit slower.
[111:57] So it will just linger for a bit longer.
[112:03] So I'll just run it again.
[112:12] And we're getting less flames than before.
[112:36] But anyway, I felt like it's kind of too big over here.
[112:43] Especially when we look at it through our camera
[112:47] and compare it to the dragon in the scene.
[112:51] But this is looking quite nice.
[113:01] I think we'll go with this.
[113:03] So what I want to do now is just disable this time shift
[113:09] and just run a simulation for the full duration of the shot.
[113:17] And let's just see how it behaves.
[113:24] Let me just stop the simulation now.
[113:28] Because I can already see what's happening.
[113:31] You can see everything is working really nice.
[113:35] We're getting some nice movement on the flame.
[113:40] But it also feels quite uniform.
[113:44] So I would like to break up the shape.
[113:48] And I think we're also at the stage where we can just cache it out.
[113:52] So first of all, let's just go to the power solver and to the output.
[114:01] And let's just check the convert to VDB, use 16-bit float.
[114:08] And also re-sample the volumes, like the velocity volume.
[114:14] And we'll do it by 4.
[114:31] You can see we actually don't get anything in the viewport now.
[114:37] I think it's because we turned it to a VDB.
[114:41] So let's see what's happening here.
[114:45] I think it has something to do with the density.
[114:50] Just go to the bindings here.
[114:57] And if we use for the smoke volume the flame,
[115:01] actually show the smoke volume,
[115:03] let's just go to the bindings here.
[115:07] And then we'll go to the power solver.
[115:10] And you can see how the smoke volume is working.
[115:14] And if we use for the smoke volume the flame,
[115:17] actually show up.
[115:27] So yeah, that's converted to VDB.
[115:30] Also just set up this pyro bake volume.
[115:37] Also here we can go to the binding.
[115:42] Let's use a flame for the density.
[115:53] And we don't want any scatter.
[115:57] We want quite a low density value, so maybe 2.
[116:03] We don't want any color.
[116:07] And let's set the intensity scale on the fire to 50.
[116:16] And another thing I wanted to do is
[116:19] just to break up these shapes a bit more,
[116:24] on a larger scale.
[116:28] Let's just view the density.
[116:37] Let's just duplicate this.
[116:42] And kind of multiply it again with a larger element size.
[116:52] Let's just remove the animation.
[116:59] And maybe just use a ramp.
[117:07] It might be too much.
[117:14] I just want to create a few pockets
[117:17] and just reduce the incoming amount.
[117:22] The incoming amount.
[117:33] It might be a bit too much even now.
[117:51] Let's try something like this.
[117:56] And also let's go back to our dragonfire.
[118:03] I just want to grab this file cache.
[118:07] So I'll copy it.
[118:11] I'll paste it over here.
[118:22] We'll call this Groundfire.
[118:27] Because we have this $OS set up, it will work properly.
[118:38] And yeah, that's just cache it.
[118:43] The sim has finished caching.
[118:45] And I've went ahead and created this flipbook
[118:47] just so we can see what we got.
[118:50] I really like the dynamic feeling this file has.
[118:54] It's very chaotic and we're also getting a lot of nice,
[118:58] small details and breakups.
[119:03] Especially like this area here, where we have this kind of big flame
[119:08] and the way it just breaks off into smaller flames.
[119:13] And yeah, just one more note for this section is
[119:18] I've simbed it at the voxel size of 0.1
[119:22] and it took about 5 minutes on my computer.
[119:25] So obviously this is really fast
[119:27] and we can resim it at the voxel scale of 0.05 perhaps.
[119:33] And this way we'll get nicer details.
[119:36] Everything will look sharp.
[119:39] And we'll probably get also more of these smaller flames.
[119:44] For next week, I will resim this.
[119:48] And that way when we work on the rendering
[119:51] we'll just get an even nicer looking sim.
[119:56] So I think this is all for the Groundfire.
[119:59] I hope you enjoyed this section.
[120:01] And I'll see you in the next video.
[120:10] Just before you start cashing out your fire
[120:13] I've found out there's a small problem with the setup here.
[120:17] So first of all, just because we're using only the flame
[120:24] we actually don't need to export the temperature.
[120:27] So you can just tick it off and just save some disk space.
[120:33] And another thing, if you look over here
[120:36] our density field is 0.
[120:39] Now this Pyro Bake volume
[120:41] it displays properly in the viewport.
[120:47] But if we go to the render view
[120:49] and just do a quick test render
[120:54] you will actually see that it's not rendering.
[121:02] Basically this Pyro Bake volume needs a density field
[121:06] so let's just fix this.
[121:12] We can actually take the flame volume
[121:15] and just rename it and replace this empty density.
[121:22] So to do this let's drop down a blast.
[121:29] And first of all let's just delete this empty density field.
[121:36] And I'll just duplicate this blast.
[121:39] And now let's just isolate the flame field.
[121:46] Now let's just rename it.
[121:48] So drop down a name.
[121:50] We'll call it density.
[121:56] And now let's just drop down a merge
[122:00] and connect these two together.
[122:05] And you can see now we have the density
[122:07] that's exactly like the flame field.
[122:10] So if I'll just connect it here
[122:14] and just do a quick render
[122:25] you can see it's rendering properly.
[122:30] And it's looking good.
[122:32] So just do this small fix before you cash out your fire
[122:37] and you'll be ready for next week.
[122:44] Just before we conclude this week
[122:46] and move on to the assignments
[122:48] I want to quickly show you how to
[122:51] apply these setups that we've created
[122:54] on the different dragon heads.
[122:58] So it should be quite obvious
[123:00] just in case.
[123:02] What you need to do is just duplicate this setup here
[123:08] and if we go inside
[123:10] now what we need to do is just update all these settings
[123:14] and just apply them on a different head.
[123:21] So let's just hide everything
[123:23] and say I want this dragon head to breathe fire now.
[123:30] Let's just select two points inside of his mouth.
[123:36] So select this one and
[123:41] maybe this one
[123:45] and let's select two points
[123:49] at the tip of his mouth.
[123:51] And now we have this emitter.
[124:06] And like we've done before
[124:09] let's see when the dragon is
[124:14] starting to breathe fire.
[124:16] So perhaps on frame 78
[124:22] on the pop sim
[124:24] let's update the start frame
[124:28] and it will finish breathing fire
[124:32] perhaps on frame 100.
[124:36] So let's just go inside
[124:41] and over here on the birth tab
[124:44] let's update it to 100.
[124:49] We also got these keyframes
[124:52] so let's shift them over
[124:57] and let's just see that everything is working properly.
[125:07] You can actually see we're getting these strange collisions.
[125:11] Let's
[125:17] for now just
[125:20] lower the bounce
[125:24] and maybe disable the drag force.
[125:29] Of course I'm doing this quite fast now just to show you the concept.
[125:35] Spend some time and make sure that everything is working properly
[125:38] and looks good.
[125:42] So this feels a bit more natural
[125:50] and if we take a look at the
[125:54] fire sim
[125:57] we should be getting fire.
[125:59] Fire.
[126:07] You can see it's a really easy
[126:10] and fast way to reapply this same setup
[126:14] just to a different head.
[126:18] And once you see everything is working properly
[126:21] and you're happy with the result
[126:24] just recache it
[126:26] and of course make sure to
[126:29] change the name of the cache
[126:31] because if not it will
[126:33] overwrite your previous cache
[126:35] which can be painful.
[126:38] So change the name of the cache
[126:42] and once this is done
[126:45] you can do exactly the same thing for the ground fire
[126:49] so just duplicate it
[126:51] and
[126:54] over here just update it
[126:56] to use the second dragon fire
[127:01] and over here
[127:03] change the cache name
[127:05] and you can just press
[127:07] save to disk and everything will
[127:09] start calculating and saving out the files.
[127:16] So this is it for the effects for week one.
[127:19] I hope you had fun
[127:21] and I'll just see you in the
[127:23] assignment section.



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

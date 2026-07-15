---
title: Bird Flocking Simulation And Rendering In Houdini | Pro Karma Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=k2fZVt9ezQo
author: Rebelway
ingested: 2026-07-15
houdini_version: "19.5.716"
tags: [pop-network, flocking, karma-fog, ocean-spectrum, solaris, birds, rebelway, simulation]
extraction_status: complete
frames_dir: tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/
frame_count: 10
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Bird Flocking Simulation And Rendering In Houdini | Pro Karma Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=k2fZVt9ezQo)
**Author:** Rebelway
**Duration:** 39m3s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome to Rubbleway.
[0:24] My name is Sabar Chalasi and today we're going to be learning how to create this bird flocking
[0:28] effect. Now this is going to be a two-part tutorial. The first section I'm going to show how to create the rendering shading in
[0:36] Solaris and Karma and the second part is going to be taught by Jason Slabber who's going to show a very clever way of
[0:43] creating this flocking behavior just using simple techniques in pops. So let's get started.
[0:53] Hello everyone and welcome again. Let's take a look at the scene and break it down. It's fairly fairly simple.
[0:59] So I have the lake surface which is simply a flat plane with some ocean displacement and I have a mountain, a 3-D geometry of a mountain that I built
[1:10] procedurally in Houdini and this mountain here you see in the all the way in the background is simply in HDR.
[1:17] I've added a caulk, a Karma fog around the entire environment that helps blend in all of this together.
[1:25] This is pretty much a raw render with very little composing to add just a veneer to darken the borders.
[1:32] Now let's take a look at the scene and the scene is fairly simple. I'm going to go over how it's done and then provide this.
[1:40] So you guys should be able to follow along if you need anything.
[1:45] So for the mountains I tried to create something similar to the HDR which has sharp peaks.
[1:52] I'm not going to be rendering any details so I just created something that gives me the silhouette that I need.
[2:02] So I started off with the grid and added some overall noise like so.
[2:07] And then use this pattern called Chebyshev Cellular which gives me this pattern and then I overlay the second one on top with another noise pattern.
[2:20] Sorry, I overlayed another noise called spark convolution just to break it down a bit.
[2:26] And then I flattened out the front part and the way I did this is I used a soft transform.
[2:37] I'm going to disable all of this so I can select the points easily. I'm going to select this.
[2:44] Actually before we do this, it's better to create the soft transform while you have a selection so it can set the centroid properly.
[2:53] So I'm going to select the front edge and hit soft transform.
[2:58] And let's plug it here, enable back my noise and just going to set this to zero.
[3:05] You can see now we're flattening all of those and increase the radius and flatten this out.
[3:14] So 150.
[3:17] There's too much so let's just set it to 80.
[3:20] And now we have a nice starting area and then we get into the mountains.
[3:25] And I help blend in the ocean over the lake with the mountains.
[3:28] And that's what I did here.
[3:31] And then I duplicated that, scaled it up and moved it and combined both of them.
[3:36] So I have more depth or more mountains in the back.
[3:40] So that's for the mountains.
[3:42] For the lake, I just created a plane, a tube by tube lane.
[3:47] And we don't need resolution when we know we're going to use displacement.
[3:52] We don't need to have high res mesh.
[3:54] We just need a polygon or two to describe where the area of the ocean is going to be.
[4:00] And then everything else is going to be handled through displacement.
[4:03] Now for the ocean, we just need to create an ocean spectrum pile.
[4:07] And I have an ocean surface here, which is basically a copy of that geometry
[4:13] just with more resolution so we can see it.
[4:16] I'm going to let this calculate, it's going to take a few seconds, and I'm going to dive inside.
[4:20] So I have a grid here.
[4:22] It's a pretty much a square version of my final lake geometry.
[4:28] And what I did is I used the spectrum, ocean spectrum pile.
[4:32] And I set the resolution pretty high because I want to capture all the fine details.
[4:36] So 13 is pretty high, but it works quite well when you have a lot of small details
[4:42] that you want to capture.
[4:44] And I do not plan to displace this.
[4:46] I'm going to use it as a bump.
[4:48] I will show where the settings are.
[4:50] So here for the default ocean spectrum.
[4:55] And I changed the resolution.
[4:57] 11 to 13 will start to give you really high details.
[5:02] And 13 is pretty high.
[5:05] So to get this to look like a lake, let's do some tweaks here.
[5:10] And maybe lower the resolution of my display grid, so it's not too slow to preview.
[5:17] So this is the default ocean.
[5:20] I'm going to set this to 25 because I want a lot of fine details.
[5:24] I'm going to change it to Philips because it works better with small details.
[5:29] Now you see how it started pinching and flipping the geometry.
[5:32] We don't want to get this as part of the file.
[5:35] We want to make sure that this doesn't happen.
[5:39] Otherwise we're going to get black artifacts.
[5:41] So we can remove or reduce that by removing by lowering the chop value.
[5:46] So 0.5 looks pretty good.
[5:49] We're going to change the amplitude to 0.5 and the wind speed to 1.
[5:56] So this might look like there's not much details.
[6:00] But it's simply because we don't have enough resolution to see all the details.
[6:05] Now I'm going to take this file and save it to this as a geo file.
[6:09] I'm going to call it Spectra 6.
[6:11] And this is my original spectrophile.
[6:15] And I just save one frame and load that in the shader.
[6:20] So that's pretty much it for the scene.
[6:23] The particle simulation is going to be taught in the second part of this video
[6:27] by Jason Sliver and has done a fantastic job to create a super clever
[6:32] and efficient way to do this effect without any crazy calculation.
[6:38] So let's go to the log context where I've done all the karma work.
[6:44] I'm going to dive inside and simply walk through the steps.
[6:47] And like I said along with the hip file, everything should be easy to understand.
[6:51] I'm going to disable the soft grid.
[6:55] I also changed this to Dini Open Geo.
[7:00] And what I have here is, let me see, to make sure that the geometry is visible.
[7:10] So it's imported.
[7:12] And I'm using a scene import to bring stuff from subs into karma or salaris.
[7:18] And this is my, this is the geometry I need, the lake geometry and the mountains.
[7:24] And I have a fog which I'll explain in a second.
[7:29] And here this is importing the cameras and I have an HDR.
[7:33] So let's take a look at the HDR.
[7:40] So this is what it looks like.
[7:42] And it's called Shudu Lake.
[7:44] And you can find this on poly Haven.
[7:47] It's free, it's a free map you can grab.
[7:50] So for the shaders, let's dive inside.
[7:53] Or actually, let's just take a look at the scene.
[7:56] So this is what it looks like.
[7:58] And let's look through the camera.
[8:04] And this is what it looks like.
[8:06] Now we don't have any shaders assigned.
[8:08] And we just need some diffused for the mountains and an ocean surface for the lake.
[8:15] Now I'm going to dive inside the interior library.
[8:18] So I have created a free shader simply by typing them.
[8:21] So I have done a mountain, I've done a bird.
[8:24] And for the ocean surface, we use, we can use the algae shortcut to get the library.
[8:30] And then we can just drag and drop the shader here.
[8:33] And it's called ocean surface.
[8:35] So this is what we need.
[8:36] It's going to allow us to load in a displacement file or ocean spectrum.
[8:41] And then we'll do all the displacement at render time.
[8:44] Now I'm not going to execute this because it might take a few seconds.
[8:47] And the only option or the only settings I need to change is turn through displacement.
[8:52] I don't want this to be displaced because I want this to be blazingly fast.
[8:57] So turn off through displacement and that's going to use it as a bump.
[9:03] So no displacement happening.
[9:06] I'm going to take on add bump to the shader displacement which will give me more accurate reflection in the vendor.
[9:14] So that's it for the ocean shader.
[9:17] And for the shader itself, it's just a principal shader for a principal core.
[9:26] And no defuse, just pure reflective, 100% reflective.
[9:32] And roughness is .05 at the leaf.
[9:35] So that's all we need.
[9:37] And what I've done is say I create a new ocean surface.
[9:42] And all these extra stuff I don't need.
[9:44] So what I'm going to do is just dive inside.
[9:47] And inside this part here it says classic shader.
[9:51] I'm going to create a principal core or a principal shader, whichever you're more comfortable with.
[9:59] They both do the same thing.
[10:01] I'm just going to connect the layer into the layer and layer to the layer.
[10:05] Now all the wave and coloring and stuff is not going to affect us.
[10:10] So I'm just set the shader here.
[10:13] 0.05 for glossiness.
[10:15] No defuse, just reflective.
[10:17] Maybe we increase the IUR to 1.8 or something.
[10:22] And that's all we need.
[10:24] Now let's do a test render here.
[10:28] I'm going to change it to, well, it's a reading comments.
[10:32] So I'm going to enable the calculation.
[10:35] And I've already assigned the shader.
[10:37] So birds, get the bird shader, the mountain, get the mountain shader, and the ocean surface get the ocean.
[10:43] Now it's going to take a few seconds for it to show up because it's running in the background, the ocean spectrum evaluate.
[10:49] And this is a great workflow because you only have to cache the ocean once.
[10:53] And then in the shader it's going to re-value I think if you're a different pattern.
[10:57] So here I didn't cache the ocean spectrum sequence just a single frame.
[11:01] And by default it's going to be super fast.
[11:04] So to slow it down we can just go inside the shader.
[11:09] Here under displacement and there's the time here we can just divide this by four.
[11:14] And that will make it four times slower or five times slower.
[11:18] Now this is a rendering live in karma.
[11:21] And the last thing you want to add is a karma fog box.
[11:27] You can type in karma. And this is just a VDB that you can scale.
[11:32] And I'm going to show you from different angle.
[11:36] So this is my fog volume.
[11:39] And a head entry you can see I have a uniform.
[11:43] I have controls to scale it and I made it bigger.
[11:48] Then the scene all the way to just left out some parts here.
[11:52] So they are super dark.
[11:54] And if I look through the camera and disable this, this is my fog.
[11:59] I can control the me copy this.
[12:02] We can play with the density.
[12:05] Make it super dense.
[12:07] And we can control the shadow density separately.
[12:10] So we can have more denser environment that it lets light through more.
[12:16] Or we can make it less dense.
[12:20] Increased shadows.
[12:21] So there's a lot of control here.
[12:24] And the great thing is I'm using this to actually change how the light,
[12:30] what how much light is reaching the surfaces.
[12:34] So that's why I'm getting this nice blend because it's actually changing the illumination of the HDR.
[12:40] And you can see without this, it's just a typical 3D render with the fog.
[12:45] Everything blends in nicely and it feels much more realistic.
[12:48] Now the last piece is to add the birds.
[12:53] And I'm going to enable that.
[12:55] Again, this is just a simple shader.
[12:59] And looking at preferences, almost you get this black spots flying in the scene.
[13:07] And that's what the look I was going for.
[13:10] Now there's one last thing I'm going to show.
[13:14] And the next thing I want to do is make this look a bit more realistic.
[13:21] You can see as they come, as they change direction,
[13:25] you can see the points are getting thinner and wider.
[13:28] And that's because they have an actual geometry that represents a bird silhouette.
[13:35] So I just created something like this.
[13:40] Again, because we have a normal and velocity, we can orient that geometry along.
[13:48] And we get this sheet.
[13:50] And that's just going to, once it's facing the camera,
[13:54] we're not going to get the illumination, it's facing away, it's going to capture more light.
[13:58] So we get that nice change in the point size.
[14:02] And when they are grouped together, we get more denser and darker.
[14:08] So that's the effect.
[14:09] And then this is the particle same, which I'm going to explain in a second.
[14:13] I think that's it for this scene.
[14:18] Let me show the final settings.
[14:22] I used no diffusion, no global illumination, no motion blur and nothing.
[14:32] Under the advanced tab, I changed the sampling to path freeze and I used 196.
[14:39] That's all I did.
[14:41] And then I render 360 frames and it took about 5 minutes per frame to render,
[14:46] which is fairly fast to be honest.
[14:49] And this is the render again.
[14:51] And I'll leave you guys with Jason and good luck. Talk to you soon.
[14:55] Bye-bye.
[16:01] I'm going to put this in a circle.
[16:06] Let's just put this on the Z plane here.
[16:11] And I just want to scatter some points on here.
[16:15] Let's just set this to around about 3000.
[16:19] Just for a little bit of interest, it's quite low-stall, but good to start off with.
[16:24] Now I want to create my little follow object.
[16:27] I'm just going to use a single point.
[16:29] So let's create an add node.
[16:31] Just toggle this on.
[16:34] Right, let's just view it.
[16:37] So now I just want to do some basic lazy man's animation.
[16:40] So for this, I'm just going to do a sine wave and give it a dollar of f for frame.
[16:46] Now you'll see my point.
[16:48] Let's just turn this on.
[16:50] It's traveling from one to negative one to a little bit slow.
[16:54] So I'm just going to speed this up a little bit.
[16:56] It's multiplied by two.
[16:59] Just going a bit quicker.
[17:00] But now it's not traveling very far.
[17:02] So I wanted to come further out.
[17:04] So let's multiply this whole value by five.
[17:07] And you'll see now my point's going R2, five, and negative five when my grid here.
[17:17] It's pretty decent.
[17:19] What I'd like to do now is all that is just visualize this a little bit better.
[17:23] And for this, he has another little lazy man's hack.
[17:27] You can use the Rigverse, which is basically just copying this visualizer to the point.
[17:33] If I have the scale, you can see now I've got a little neat little visualizer.
[17:42] Right, that's cool.
[17:45] Now let's just go ahead and create my popnet.
[17:51] What it will make work is connect my meta up to the first one.
[17:56] And I want to create add my follow object to the second input here.
[18:03] Just going to view this and I'm going to dive right inside.
[18:08] Right, so it's the basic setup.
[18:10] So just before I start with this, I just wanted to show you there is a popfluck that shops with you, Dini.
[18:19] Which isn't too bad, but it obviously doesn't have the follow object that we need.
[18:25] So it's kind of a, not really what we want to use currently.
[18:30] But what you can do is if you're editing of contents and if you dive inside, you can see how it's been built.
[18:36] So this is just basically a pop attract and a pop interact.
[18:42] Now what's interesting about this, there's some values that are unconnected.
[18:46] So like for instance, there's velocity force, which kind of averages out your velocity positions.
[18:52] Now I'm not to show if this is a bug or if it's just a not connected setup, but it's not really working for.
[19:01] I need some just going to go out and delete this.
[19:05] Then what I'm going to do is just trash out this pop wires into, yeah, I just, I never work like this.
[19:11] I always just work from a top-down approach. I'm just going to trash this out.
[19:16] Okay, now for my emission point, I'm going to go to source.
[19:21] I want to use those incoming scattered points. So I'm going to use all points.
[19:25] Let's first context geometry.
[19:28] My birth, I just want to birth on one frame.
[19:31] And for this, I like to use dollar simulation frame.
[19:35] Equals equals one.
[19:37] Simulation frame means that any frame your simulation starts on, it will start on that simulation frame, if the frame equals one.
[19:48] It's just a little bit easier than using the dollar F equals equals one, because then you might change your simulation time.
[19:54] And then your simulation doesn't really start when it's supposed to.
[19:59] So moving on, I'm going to go to the attribute tab.
[20:04] I don't have any income velocity.
[20:08] So I'm going to set an initial velocity, but I want to make this look super low.
[20:13] So let's just make it zero point, which is zero point zero one or so.
[20:18] So it's like super small.
[20:21] I'm going to go ahead and turn off these guides because they annoy me a little bit.
[20:26] So now we have a basic setup, nothing really happening, just a bit of tiny bit of variance in the velocity.
[20:36] So let's start off now with the pop follow and I'm going to use my hop attract.
[20:43] The start is, let's just name this to follow.
[20:50] For this setup, I want to use points.
[20:54] So this allows me to grab the position of the points coming in from the outside.
[21:02] So I'm going to set this to the second context, which is the second input here of the pop net, which is pointing to that output, obviously.
[21:11] And then yeah, so we'll just have this basically this whole system will try and follow at one point.
[21:19] Now we just need to change some settings on this.
[21:22] I want to set it to follow, just gives me a little bit more parameters to play with.
[21:26] Right off the bat, I'm just going to go and set the force to 10.
[21:30] I know for the scene scale, I need to bump it up a bit more.
[21:34] You'll see nothing's really going to happen yet.
[21:37] What I need to do is I need to set an ambient speed.
[21:41] The particles generally to move to.
[21:44] So just set this to one for now.
[21:47] And you can see I'm starting to get some motion happening.
[21:52] Now obviously I can't really see my little follow object.
[21:58] So let's just sort that artwork.
[22:00] I'm going to jump out of the pop net here.
[22:03] And what I want to do is I want to lock this plane,
[22:07] sorry, to the current viewpoints.
[22:10] So if I dive right in, I'll still see this area.
[22:14] But then what I just want to do is I want to control, click on this Vizrig.
[22:18] On the template.
[22:20] I can control, click, you can now see it.
[22:22] Let's just change the color here a little bit.
[22:25] Over I join color.
[22:27] Let's put the color yellow.
[22:29] There we go.
[22:30] So now we can see.
[22:31] So now if I dive back in here,
[22:33] you can still see my visualizer.
[22:38] And you can see the follow objects not really working too well yet.
[22:41] So what I want to do is just start missing with these settings.
[22:45] So on the bump of the speed scale,
[22:48] but I can see it's really starting to do stuff.
[22:51] But it's going way past.
[22:53] So I'm just with the ambient speed 9.
[22:56] I said this to 5.
[22:57] I see now it's like, oh, it's going crazy all the way around here.
[23:02] So this is obviously way too much.
[23:05] So I'm basically just going to dial down the ambient speed a bit
[23:09] because I don't want it to follow 100%.
[23:12] I just want it to feel a little bit more organic.
[23:15] Let's just take this down to two.
[23:18] And I'm going to take the scale down to five again.
[23:23] I'm starting to get, it's not quite hitting the market.
[23:29] Let's just bump my speed up a bit more.
[23:34] It's not too bad.
[23:37] Let's make it seven, minus three.
[23:43] It's not too bad.
[23:44] I think the ambient speed is maybe a little bit higher.
[23:47] I know.
[23:48] So let's make it 2.5.
[23:51] I'm always too much time playing with these settings,
[23:54] but that's kind of what I want.
[23:57] You can see over time the sign to get over too heavy though.
[24:03] Let's start with this back down again.
[24:06] Alright, two.
[24:09] Let's just stick with that for now.
[24:12] It's kind of falling, but not falling.
[24:15] Okay, so let's just move on now.
[24:17] We want to create a little bit more interest.
[24:20] So I'm just going to start over the pop force here.
[24:26] So this is essentially what I want to do.
[24:29] I want to create some noise and this starts to create this kind of these interesting hatchens.
[24:36] Essentially birds are flying around.
[24:40] But now the problem I had with the basic pop force is this amplitude is controlling X, Y and Z.
[24:50] All in one go.
[24:52] So if I want to bump up my force scale,
[24:57] it's basically creating noise up and down.
[25:00] And for the shot I was working on, I wanted it really built to control the noise a little bit more only on the X and Z axis.
[25:11] Essentially my birds with kind of one hovering over a cross plane.
[25:16] So this obviously wouldn't work when you got too much noise at this level.
[25:22] So for that I'm just going to disconnect this quick.
[25:26] I created a custom force using a cool noise.
[25:31] And for that I used a VOP.
[25:36] You got pop VOP.
[25:39] So let's just connect this and connect this and start right inside.
[25:46] So what I want to do is use a cool noise.
[25:51] And I'll just connect the position of the particles to the cool noise.
[25:55] I'm going to be affecting the force.
[25:57] So for now I'm just going to connect force to force.
[26:00] So basically any incoming force will still apply.
[26:06] And I just want to add to this incoming force.
[26:09] So now in order to do the two planes,
[26:14] what I want to take this cool noise is giving me a vector.
[26:17] So I just want to change this to a float.
[26:20] So I'm going to do a vector to float.
[26:24] And this will basically give me my X, Y and Z axis in three components.
[26:32] And then if I do a float to the vector,
[26:39] this allows me to basically combine them again.
[26:42] So I'm going to take my X axis and plug it in.
[26:45] And my Z axis, which is third one, and plug that in there.
[26:49] And you'll see if I don't connect this component value,
[26:54] which is Y, is set to zero.
[26:57] Now if I add this,
[27:01] drop that node,
[27:04] I'm going to add this noise to my current force.
[27:09] And now you'll see I start getting noise,
[27:12] and it's only really happening on the 2D plane,
[27:16] which is a little bit more what I want.
[27:20] I'm just going to go ahead and change this.
[27:23] I've played around with quite a few values based off.
[27:26] I just want to keep it based off the scene I was using.
[27:29] So for this, I use just this analytic, some flex noise.
[27:35] I just found it great.
[27:37] Some interesting patterns.
[27:39] I just want to reduce the frequency a bit.
[27:43] I want a bit more slowly,
[27:46] a bit tight tab, one noise.
[27:50] Not too bad.
[27:52] I just want to reduce the roughness.
[27:55] I just want to bump up the frequency a little bit more.
[28:03] It's interesting.
[28:05] Alright, so now if I just bump up this amplitude,
[28:08] you'll see it starts getting quite crazy,
[28:11] but it's giving me this nice 2D kind of noise.
[28:16] This is obviously way too much.
[28:20] It's making about 3 for now.
[28:23] That's quite cool, I think.
[28:27] I'm getting my little follow object.
[28:32] Obviously now this is quite chaotic still.
[28:36] Doesn't have any sort of nice following.
[28:40] It's probably a little bit more like a swarm rather than a bunch of birds flocking.
[28:47] So let's just start adding some extra stuff to this.
[28:50] Right, for now let's go.
[28:53] I went to after my pop follow,
[28:55] I just want to do another pop attract.
[29:00] This is essentially I want to make little clusters of follow objects.
[29:07] I'm going to set this to particles, which basically is themselves.
[29:11] It's got this number of clusters and the number of clusters currently is set to 1.
[29:17] Let's just show you what that's doing if I disable this pop follow.
[29:23] Let's just disable this noise.
[29:28] Okay, we've got one cluster.
[29:32] Let's just bump up this force a bit so we can see really what's going on.
[29:37] Now I've essentially got all the particles they're trying to get to the center.
[29:41] Obviously this is just one cluster.
[29:44] If I set it to two, you'll see now I've got two little clusters and they're trying to follow a pick one basically one point
[29:54] and they're trying to follow that point so they're going off in the direction that they still sort of averaging around themselves.
[30:05] What you can do and what I find quite nice is this reversal distance.
[30:12] I must create these hollow pockets and if you look at the memorations you'll see it feels like there's a bit of wallowing
[30:19] and I guess that's where they almost try to avoid each other and not coming too close.
[30:25] If I bump this up to just give it a random value for now you see now I'll start to get a bit higher for this example.
[30:40] Now you'll see a moment's getting in like swears of birds and without them sort of getting to the center.
[30:50] Which is pretty interesting.
[30:55] Okay, so let's just move on from here.
[30:58] I can come back to these settings and we're just going to set this to one for the moment.
[31:04] It's just enabled my force and my pop follow so we can start dialing in some settings.
[31:11] I see I've got a noise happening, I've got these hollow pockets, these two formations happening.
[31:22] The forces might be a little bit strong so they're kind of separating a bit much but it's quite interesting for now.
[31:32] So now we just want to start working on them sort of averaging around each other and not getting too close to each other.
[31:39] So this is where the pop into act comes in.
[31:44] Pop into act.
[31:48] Right, so now we'll just see.
[31:53] Immediately see they sort of starting to feel a little bit more uniform in their shape and kind of spread apart a bit.
[32:04] I'm just going to set this pop attract the goal.
[32:08] I just want to set the clusters to one again.
[32:10] It's just a little bit quicker to work with.
[32:12] This gets quite slow than the more clusters you have and I'm only working on my laptop which is a little bit slower.
[32:19] So just easier to dev with one point and kind of get the idea of what's going on.
[32:25] Right, so let's just dial in some settings here.
[32:29] I just want to help my position force and this is kind of our strong particles trying to keep away from each other.
[32:41] You can dial it up and out.
[32:43] It's actually becoming a little bit more swarming again.
[32:48] It might be a little bit much.
[32:50] Let's just dial it down.
[32:53] Right, and then what I want to do is this velocity force.
[32:56] This is quite cool because this is what almost what the birds are doing is they trying to fly together.
[33:02] So they if velocity is essentially averaging almost together.
[33:07] So when you start dialing this up.
[33:12] You'll see now you start getting this they all kind of really moving at the same speed.
[33:19] That's obviously way too high.
[33:21] It's the one a little bit of chaos and a bit of separation.
[33:25] So I'm just going to dial this back down.
[33:29] Let's make it just one just over one.
[33:34] That's not too bad.
[33:35] I'm getting kind of.
[33:38] One's we're that's still kind of averaging each other out here.
[33:43] So just on the bumpers force up just to see what this does.
[33:48] So they're kind of pushing away from each other a little bit harder.
[33:53] Maybe we can increase this radius and this fall off radius is just softens at our little bit as well.
[34:02] So it's getting a little bit more interesting.
[34:06] Quite liking that setting.
[34:08] So let's just now go back and look at the pop of tracks.
[34:14] Let's go the force term and see what we've done here.
[34:17] Versal distance we could probably set this up higher.
[34:23] Again, just to maybe create a bit more separation.
[34:28] So now they're really spreading out.
[34:32] They almost like.
[34:34] All jar when they come too close.
[34:37] It's quite interesting.
[34:39] Maybe a bit much.
[34:40] Let's just make it 1.5.
[34:48] I think this.
[34:50] Force scale is actually probably a bit higher because it's kind of almost overriding this a bit much.
[34:55] So I'm just going to hold this and see what this does.
[35:00] You can see now I'm getting a little bit more of a follow action happening again and still got some separation happening.
[35:08] Which is quite cool.
[35:10] Start off this.
[35:12] This is really you start playing around with the settings and just seeing depending on your scene scale.
[35:19] You know, just to get that look and feel of what you want.
[35:25] That's quite cool.
[35:26] Let's just bump up my clusters to 2 again.
[35:37] It's starting to look quite interesting.
[35:40] Interesting shapes happening.
[35:46] Maybe what I can do is try and get them to follow the follow object a little bit closer.
[35:52] I'm just going to go back to my follow here.
[35:55] I'm just going to bump up this scale a little bit here.
[36:00] This is the overall scale on everything.
[36:05] Yeah, just.
[36:09] Yeah, matching a little bit better now.
[36:12] And there's the ambient speed quite low.
[36:15] So you're getting these like ones almost kind of falling away.
[36:19] If I drop this down, you'll see I get quite a lot of break up around the edges.
[36:27] So this is kind of this ambient speed is a nice way to control that sort of overall ambient speed.
[36:35] You see there over the pop-up track is kind of taking over now.
[36:40] And if I bump this right up, you'll see my ambient speed now.
[36:44] They all really just going to follow this super closely.
[36:48] So if you really want to type following cluster around your follow object,
[36:55] bump up this ambient speed and that kind of works.
[36:58] Look for this case.
[36:59] I just want to dial it back down again.
[37:05] So the last thing I wanted to do was just add a bit of drag into this.
[37:13] So by default, you'll see it's kind of creating drag of all the particles,
[37:17] which is an ideal way to kind of randomize the drag.
[37:21] So for this, we just can use a basic fix expression.
[37:27] Just for ease, I'm just going to show you.
[37:29] You can just drag this onto here and you'll get the name of this parameter.
[37:35] Obviously, we don't have the full parts, so you can just delete it.
[37:39] Or just, if you hover over here or see the parameter's name,
[37:43] and you can just type it out.
[37:46] So what we're going to do here is do a randomize each particle ID.
[37:52] And then we're going to fit it to a range using this area.
[37:56] So just to simply boss it, we'll do a start off with a 501,
[38:02] which is kind of a fit range between 0 and 1 value.
[38:07] And then I'm going to get my random ID.
[38:16] And then so now I've got the random ID, which gives you a value between random value between 0 and 1.
[38:22] I just want to fit this to just say 1 and 0 for now.
[38:31] Let's hit play.
[38:33] You can see it's still got quite a lot of drag on some places and no drag.
[38:38] You can see some of these particles moving quite fast so those don't have any drag.
[38:43] Because it's like really high, so I just want to create a really small value.
[38:48] Just to vary it up a little bit.
[38:56] And I think that's pretty much all that I might be with that.



---

## Captured Frames

- [3:05] tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/frame_000.jpg
- [5:20] tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/frame_001.jpg
- [8:04] tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/frame_002.jpg
- [12:02] tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/frame_003.jpg
- [13:03] tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/frame_004.jpg
- [22:14] tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/frame_005.jpg
- [26:00] tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/frame_006.jpg
- [29:32] tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/frame_007.jpg
- [33:00] tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/frame_008.jpg
- [38:33] tutorials/frames/bird-flocking-simulation-and-rendering-in-houdini-pro-karma-tutorial/frame_009.jpg

---

## Structured Notes

### Core Technique
A two-part production breakdown: Part 1 (Solaris/Karma) builds a lightweight lake-and-mountain environment with a Karma volumetric fog box driving the HDRI illumination for atmosphere, plus an efficient Ocean Spectrum-as-bump (never displaced) shader for a fast-rendering lake; Part 2 builds bird-flocking behavior entirely from stock POP nodes (Pop Attract, Pop Interact, a custom Pop VOP noise force) rather than a scripted boids solver, using a single "follow" point and clustered sub-goals to fake cohesive-but-organic group movement.

### Summary
The environment starts from a simple grid sculpted into sharp mountain silhouettes using layered Chebyshev Cellular and Spark Convolution noise, then a **Soft Transform** (created with a point selection pre-made so its pivot centers correctly) flattens the front foreground area into a usable "beach" zone before the noise ramps into peaks; a duplicated, scaled-up copy of the same mountain adds background depth. The lake surface itself is kept at minimal polygon resolution since all visual detail comes from a **Ocean Spectrum** file (resolution 13, Philips spectrum type, chop value lowered to prevent wave self-intersection/pinching, amplitude 0.5, wind speed 1) cached to a single frame and referenced by an **Ocean Surface** shader with **Through Displacement disabled** — the ocean's fine detail is used purely as a bump map (with Add Bump to Shader Displacement enabled for correct reflections) rather than true geometric displacement, keeping renders fast; the underlying shader is just a Principled Core node with zero diffuse, ~100% reflective, 0.05 roughness. Environment lighting comes from a free "Shudu Lake" HDRI (Polyhaven) plus a **Karma Fog Box** (a scalable VDB volume) whose density and shadow-density parameters are tuned separately — the fog is the key trick that sells realism, since it visibly reduces how much HDRI light reaches distant surfaces, creating natural atmospheric falloff without extra lighting rigs. Birds are rendered as camera-facing oriented cards (built from normal + velocity so silhouette width changes correctly as they turn) shaded with a simple black-silhouette material; final render settings use no diffuse GI or motion blur, Path Tracing sampling at 196 samples, 360 frames at ~5 min/frame. Part 2's flocking system starts from ~3000 scattered points on a plane plus a single animated "follow" point (driven by a simple `sin($F)` expression scaled up for range) that acts as the flock's shared target — visualized cheaply via a **VisRig** copied onto the point through a right-click "Edit Contents"-style visualizer trick. Inside a custom POP network (built from scratch rather than using the stock Pop Flock HDA, which has an unreliable/disconnected Velocity Force input when inspected), particles are birthed once on `$SIMFRAME==1` from the scattered source points with a near-zero initial velocity, then a **Pop Attract** (set to "Follow" mode) pulls all particles toward the single follow point, with **Force** and **Ambient Speed** as the two key tuning knobs — Ambient Speed acts as a general speed-matching factor that, cranked high, makes the whole flock track the follow point tightly, while low values let particles drift/break apart at the edges for a looser, organic feel. A custom **Pop VOP** wires a Curl Noise's output through a Vector-to-Float / Float-to-Vector split so only the X and Z components of the noise are added to the incoming force (zeroing Y) — this constrains the chaotic wander noise to a horizontal plane instead of also bobbing birds vertically, which looked wrong for this shot's composition. A second **Pop Attract** (mode set to Particles, with a Number of Clusters parameter) creates emergent sub-flocks: with clusters=1 all particles converge on one shared centroid; raising clusters to 2+ splits the group into independently-targeting sub-clusters that each aim for their own averaged center, and that node's **Reversal Distance** parameter pushes particles away from their cluster center once they get too close, producing hollow, swirling "murmuration" pockets rather than a solid ball. Finally a **Pop Interact** node adds separation/cohesion refinement between all particles via its Position Force (keep-apart strength), Velocity Force (velocity-averaging/alignment strength — the more "flying together" feeling), Core Radius, and Falloff Radius, all balanced against the earlier Follow and Cluster-Attract forces to land on a look that's cohesive but not robotically uniform. A final touch adds per-particle drag variance using a one-line VEX-in-parameter expression: `fit01(rand($PT_ID), 0, 1)` (fit the per-particle-ID-seeded random value into the drag parameter's range) so different birds decelerate at slightly different rates instead of uniformly.

### Key Steps
1. **Environment (Part 1):** sculpt mountain silhouettes on a grid using layered Chebyshev Cellular + Spark Convolution noise; use a pre-selected-point Soft Transform to flatten a foreground "beach" area before the peaks ramp up; duplicate/scale for background depth.
2. Build a minimal-resolution lake plane; generate an **Ocean Spectrum** file (resolution 13, Philips type, lowered chop value to avoid pinching/self-intersection, amplitude 0.5, wind speed 1) and cache a single frame.
3. Build an **Ocean Surface** shader referencing that cached spectrum with **Through Displacement disabled** (bump-only, not real displacement) and Add-Bump-to-Shader-Displacement enabled for correct reflections; base shader is a Principled Core with 0 diffuse, ~100% reflective, 0.05 roughness.
4. Light the scene with a free Polyhaven HDRI ("Shudu Lake") plus a **Karma Fog Box** (scalable VDB) — tune density vs. shadow density separately to control how much HDRI light reaches distant geometry for atmospheric falloff.
5. Shade and orient birds as camera-facing cards driven by normal + velocity (so apparent width changes correctly with turning), simple black silhouette material; render with no diffuse GI/motion blur, Path Tracing at 196 samples.
6. **Flocking (Part 2):** scatter ~3000 points on a plane; build a single animated "follow" point using a scaled `sin($F)` expression; visualize it cheaply with a VisRig copied onto the point via Edit Contents.
7. Build a custom **POP network** (not the stock Pop Flock HDA, whose Velocity Force input is unreliable): birth particles once at `$SIMFRAME==1` from the scattered points with near-zero initial velocity.
8. Add a **Pop Attract** in "Follow" mode targeting the single follow point; tune **Force** and **Ambient Speed** — Ambient Speed controls how tightly the whole flock tracks vs. drifts/breaks apart at the edges.
9. Build a custom **Pop VOP** noise force: Curl Noise → Vector to Float → Float to Vector, feeding only X/Z components (zeroing Y) into the existing force, constraining wander noise to a horizontal plane.
10. Add a second **Pop Attract** (Particles mode, Number of Clusters ≥ 2) to split the flock into independently-targeting sub-clusters; use its **Reversal Distance** to push particles apart once too close, creating hollow murmuration-like pockets.
11. Add a **Pop Interact** node to fine-tune separation (Position Force) and alignment/cohesion (Velocity Force, Core Radius, Falloff Radius) between all particles for a natural, non-uniform group look.
12. Add per-particle drag variance via a VEX parameter expression (`fit01(rand($PT_ID), 0, 1)`-style) so birds decelerate at slightly different rates instead of identically.

### Houdini Nodes / VEX / Settings
Grid, layered noise (Chebyshev Cellular, Spark Convolution), Soft Transform (pre-selection pivot trick), Ocean Spectrum (resolution 13, Philips type, chop/amplitude/wind-speed tuning), Ocean Surface shader (Through Displacement off, Add Bump to Shader Displacement), Principled Core (reflective-only setup), Karma Fog Box (VDB density/shadow-density), Polyhaven HDRI, Path Tracing render settings, camera-facing bird card shading (normal+velocity orientation); POP network: Add (single follow point), `sin($F)` expression, VisRig visualizer copy trick, Pop Source (`$SIMFRAME==1` birth, initial velocity), Pop Attract (Follow mode: Force, Ambient Speed; Particles/cluster mode: Number of Clusters, Reversal Distance), Pop VOP (Curl Noise, Vector to Float, Float to Vector, force-add), Pop Interact (Position Force, Velocity Force, Core Radius, Falloff Radius), per-particle drag VEX expression (`rand($PT_ID)`, `fit01`).

### Difficulty
Intermediate/Advanced (the environment/shading half is approachable default-node work; the flocking half requires understanding several interacting POP force nodes and tuning them against each other for an organic result).

### Houdini Version
19.5.716 (visible in viewport title bar: "Houdini FX Education Edition 19.5.716").

### Tags
pop-network, flocking, karma-fog, ocean-spectrum, solaris, birds, rebelway, simulation

---

## Related Tutorials
- [Quick CGI Integration with Houdini and Solaris](quick-cgi-integration-with-houdini-and-solaris.md) — shares the HDRI-driven environment lighting and Karma render-setup approach used here.
- [Procedural Environments in Houdini | Patreon February '26 Free Lesson](procedural-environments-in-houdini-patreon-february-26-free-lesson.md) — shares a course-style breakdown format from a different channel, useful as a comparison of production-lighting/environment approaches.

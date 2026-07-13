---
title: Cookies and chocolate | Modeling, shading and Sim
source: YouTube
url: https://www.youtube.com/watch?v=c90ervPv5ro
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/cookies-and-chocolate-modeling-shading-and-sim/
frame_count: 0
frame_status: pending-selection
---

# Cookies and chocolate | Modeling, shading and Sim

**Source:** [YouTube](https://www.youtube.com/watch?v=c90ervPv5ro)
**Author:** cgside
**Duration:** 25m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py cookies-and-chocolate-modeling-shading-and-sim <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in today's video I wanted to share this project with you guys.
[0:05] So from the modeling of the cookie to the texturing and also the liquid that wraps around.
[0:11] So as you can see by the final result is nothing too exciting, but hopefully I will share some techniques I will I never shared before.
[0:18] And that might be interesting to learn about. So let's get into it.
[0:23] So the first thing I did was to model the cookie. It looks something like this. So let's go through the techniques.
[0:31] So I start with the tube, then do a basic polybable and rematch it with some smoothing.
[0:37] Then I do a VDB from polygons. I chose this resolution to start with and then do a VDB smooth to smooth out the result.
[0:44] And then do a re-sample in this case, duplicating the voxel resolution to have enough voxels to create the overall details.
[0:56] So this might be a bit scary, but this is the network of the cookies. So let's get one step at a time. I'm gonna disable the last layer and the other ones.
[1:06] And also this one. And also this one. So we the first step is to create, as you can see, we start with this tube, tube like shape.
[1:17] And I wanted to create this cookie shape. And the way I'm doing that is by taking the relative point bounding box, splitting the y-axis in here.
[1:26] So we get the mask along the y of the mesh of the tube. And then with the ramp, I can shape the final shape again of the cookie.
[1:39] And then in here I just use a snippet and taking the position. I just affect the position.tax and position.tax to create this tapering effect.
[1:47] And at the end of the core of our technique, we do a volume sample. So we sample the position and we affect the position with these nodes.
[1:58] And we do the same for basically distortion. So this noise distortion, as you can see, is basically a turbulence noise.
[2:05] And then I just remove most of the y-component of that noise. Otherwise it will be a bit all over the place.
[2:13] So I'm using snippets in here because it's easier to isolate the different channels.
[2:19] So again, this is feeding to the volume sample. Instead of adding over the density, I'm using a volume sample. So I can distort the original position.
[2:29] And then I do again another distortion in here. So we actually skip this noise for now because we are working with this Worley's cellular F2F1, I believe.
[2:39] Yeah, F2F1, I mean, inverting it and just distorting it with another 3D noise, in this case a turbulence noise with zero centroid per length.
[2:47] And we, of course, we fit it. So we close the bit to shape and we just multiply the effect down otherwise it will be too much.
[2:54] Then I'm just doing some masking so I don't want to affect the bottom part so much. So for that I'm using some masking in here.
[3:02] No, in this case I'm not using masking. I'm just, yes, I'm using masking in here with this ramp along the y-component of the relative point bounding box.
[3:14] So in this case I'm just masking the, let's see, I'm just masking the bottom part. Yeah, I don't want to affect the bottom part. That's what I'm doing in there.
[3:23] So I'm just mixing, mixing between the previous result. So without this noise and with the noise and using the mask to mask out the bottom part.
[3:34] So that's it. Then after the volume sample I want to create an overall effect. So I'm not doing on the volume sample before the volume sample.
[3:41] I'm doing afterwards and it's creating the starvalent noise. So just adding over the density.
[3:47] And what I'm doing in here is basically creating a unified noise, adding some fractal, complimenting the noise. So I'm just importing the noise, creating a control for the repetition, so the frequency.
[4:02] And then doing a fit and clamp. So it's not the normal fit range is the unclamped one, which will not claim the final result and create those.
[4:13] A result like this one where I'm using a, you can see it cuts off in here because I'm using a clip to range, a fit range, a normal fit range in here. I'm using an unclamped.
[4:24] And that creates the desired effect of continuing the shape out. So you can see my values in here. And then I just multiply over some masks in this case, a mask along the way to mask out the bottom.
[4:35] I just manipulated here with a fit range to move it to the correct spot. And I also do a distance between the bounding box center and the current position to mask out a bit the center.
[4:47] So in this case, I'm asking a bit to center so it doesn't, doesn't create too much noise in there. That's a desired effect. And again, just multiply constant to reduce the effect.
[4:58] And finally, I'm adding another layer and the final layer, which is just some overall broken parts in here. So just eating a bit the shape in the end, which is just an again, another unified noise with some fractal, changing the offset, inverting the noise and doing a basic fit range and multiply.
[5:16] It's a bit hard to see with all these masks in here, but basically it's creating these little spots. And again, this was just a quick way to put it together there. You can layer how many effects you want.
[5:29] You just have to look at some reference and keep increasing the amount of noises. So, but in the end, I thought this was a nice result and I was happy about it.
[5:40] Then we convert this to geometry, but we don't want, as you can see, we have 400,000 polygons in here and we don't want to use this mesh for final render. In this case, it will be okay to render this.
[5:51] But then again, to create UVs and textures, it would be a mess to use these kind of mesh, this polygon count. So what I do in here, after the volume, I just do a volume re-sample to reduce the amount of voxels.
[6:04] Do a smooth and convert this to a mesh and this will be our low polybase where we will bake the ira's mesh. So that's basically it.
[6:14] Then what it comes next, I want to add some of these decorations that you can see in here. So I'm going to go pretty quickly on how I do this.
[6:25] I start with a line, you can, so I start with a line, do a basic re-sample and create a rig wrangle in here. I've covered this technique many times before.
[6:32] This case, I'm sheeting a little bit over the ramp to create this kind of effect in here. But basically, we start with curvy, which is this vertex curve per amp. We shape the curvy with this ramp.
[6:44] We create a parameter for the angle, so we can do the rotation on the transformatributes and we rotate around the x-axis. So the x-axis in here is pointing to the front.
[6:55] And then we just introduce some offset so I can control where the bend starts. So nothing too exciting. And then we just do a sweep, making sure we delete the transformatrib, otherwise it would break everything.
[7:08] So we just do a sweep and create a scale ramp in here to create this shape. Then I do an exercise quad remasher to mash basically the bottom and do a smooth, to have this mode shape. And this is our decoration.
[7:21] Then we want to copy this to the cookie. So what I'm doing in here is finding the, how is it called? So the values of the cookie so I can copy the decorations to there. So I do a mask by feature and do it based, I believe, on ambient occlusion. Yes, and I just remap the ramp. Then I do a scatter over the mask.
[7:42] But again, it's selecting some other areas that I don't want. So I blast everything where the mask is smaller is not closer to one. Then I just since the scatter will randomize the point order, I can just select three or four points in this case. I'm selecting four.
[7:58] Creating some p-scale randomizing the p-scale, then randomizing just controlling the overall p-scale, randomizing the orient and copying the points. So this is randomizing the orient is applying the overall scale and some random scale also. Maybe this is not very realistic because this would look exactly the same. So there's a standard for it. But anyways, I'm just randomizing between point eight and one.
[8:20] Then we want the idea is to create some indentations on the cookie so as you can see in here, to place the different decorations. I'm calling decorations, I don't know the correct name.
[8:33] But so in order to create this depromation, you usually create your decorations and then you convert it to a VDB and you subtract from your VDB cookie. So this one in here.
[8:45] But I don't want to convert back and whatnot. So I did a very ship technique, which is after the copying these two points, I'm injecting a near a circle sphere and packing transforming it a bit up and creating a VDB from it. And then in here, I'm just deforming the cookie instead of creating a VDB subtract or SDF difference. I'm just doing a very basic technique, which is sampling the SDF from the second input. So the spheres.
[9:10] And then if the spheres are inside the cookie or if the cookie is intersecting the spheres, I calculate the gradient and move the points along the gradient.
[9:22] And there's one something else I'm doing. I'm lurping between flats, the web blurred position. So you can see in here the second input position and the current position.
[9:34] So where when I create the indentations, I get the flat mesh. So I can get a bit more a bit softer look, let's say creating a name and catching the cookie. And in the second input, I just collecting here the copy to points, creating a name, merging it over, deleting some attributes and that's our out cookie.
[9:59] Then we have in here the iPoly and I have the low poly base if you remember, which is just this. I'm quite remaching it. So you can use it in this one. In this case, didn't work so well. So I use the exercise clipping around the y axis and saving the clip edges and doing a basic UV flattening here based on the clip edges. So it's it's quick and dirty. You this then trouble transferring the UV transferring the to the original batch since I don't want this clip.
[10:27] And then I just place a normal, which is necessary for the baking, which I'm doing in here. So let's have a look. This will take a second to cook. So this is more or less the texturing. Let me get rid of the ambient occlusion.
[10:41] So what I'm doing in here is loading the load, the low poly and the iPoly and the way in a bake geometry.
[10:48] The textures and I'm baking almost everything. So the curvature, the occlusion, the cavity, the thickness, most of it, I don't use it, but I'm just doing that. Then cable packing everything and this is my bake.
[10:59] Then I imported in here with a fetch unpack it and from here, I just do the texturing, starting with noises, doing some warping. And then at the end, I do a basic one or two RGB and this is the base texture.
[11:12] Then I blend in some masks from the cavities and whatnot and adjusting the colors in here. This is our albito and of course we import the it since I also baked it.
[11:25] And just adding some of that black and white texture of the albito, adding some bits of that to the it. If I visualize it here, you can actually see how it looks.
[11:38] So this is just the it that I baked from the it but of course we need these low values for the rendering in here just looks black. But anyway, Stan, we in here, I'm just previewing, but the final result will look a bit different.
[11:52] But as you can see, this is the basic texturing that I'm using. What you can take from here is just use the baked textures to bake the it and all the other maps.
[12:01] So this was just we can dirty texturing, but in the end it works. Okay. So that's about it for the cookie and then we will look.
[12:11] We will have a breakdown of the of the fluid. So let's do that next.
[12:17] Okay guys, now let's look at the fluid, which just wraps around the cookie and creates this sort of underlating effect, which I wanted for my final result.
[12:27] So we start with the cookie, which is at the origin, we unpack and do a low poly VDB from polygons because I still want these decorations in here.
[12:40] So I VDB everything out and do a basic convert VDB to convert it to a mesh.
[12:48] Then I transform it to the position and save the transform attribute because I will use it later. So these transform attributes, this is my cookie and I create a collision source, which is the geo and the VDB.
[12:59] Then I create two velocity fields, which basically one.
[13:04] So one is creating a velocity field to wrap around not to wrap around to move the fluid uniformly around the shape, which I will cover in a bit.
[13:13] And the other one just creates some normal pointing some normal pointing to the cookie in here is a bit out to see, but basically is just some normal pointing into the cookie. So it attracts to the cookie.
[13:25] So before I cover the flip, I will cover these velocity fields. So from the cookie, I'm creating a remesh and selecting one point to bound in box max Z axis.
[13:39] Then doing distance from geometry from that point to create this mask.
[13:43] From here, I create a VDB from polygons and activate a velocity VDB with that reference VDB and then create the velocity, which will look something like this. So the normal pointing direction pointing to the cookie.
[13:57] And that's easy as sampling the gradient from the from this VDB, normalizing and inverting it. So it points in.
[14:04] The gradient is basically the normal pointing out from an SDF. In this case, I want to point it in. So I just negated in here.
[14:11] And that's I that's what I'm doing in here in this volume wrangle. Then I copy the X form from the cookie, transformed and I transformed by a trip to move it to place. And this is my first velocity vector.
[14:21] I'm just visualizing in here.
[14:23] We by merging the cookie, doing a bound points from volume and visualizing. But now I want to look at this one, which is slightly more complicated. So we have three inputs in here.
[14:33] So let's look at the final result. But basically I'm taking the base of our velocity VDB. So I'm reusing instead of duplicating and taking also the SDF and taking also the mask for some reason.
[14:50] Yes, I'm also taking the mask so I can sample it. And in this volume wrangle, so let's look at the final result.
[14:56] What I'm doing in here is sampling first the mask. So this mask that goes from red to blue. So from one to zero along the along from that reference point to the mesh.
[15:09] And I'm also sampling in the second inputs. So one, two, so this one, which is the SDF. So I'm just sampling the SDF. And I'm also sampling from the SDF to gradient. So the normals.
[15:23] Then I do a basic distance check. I'm not using this one, but this is just a distance between the voxels and the bounding block center.
[15:31] Then this one I'm not also using, which is measuring the length of the gradient. Then I create in here a distance. So a distance along the Z axis, because in here is transformed by this transform by attribute. But in here is the Z axis is flat on the ground.
[15:47] So I'm taking an initial direction, then doing a relative pounding box, which will give me a mask along the Y, the Z and the X. Then I'm manipulating in here the different mask.
[15:59] So the in this case, the bounding box X, which I'm using to, let me see, in this case, I'm not using the Z bias.
[16:13] So I'm not using the Z, yes, I'm using the Z bias in here. So basically, the Z bias is just remapped ramp of that mask that we had.
[16:24] And I'm just in here manipulating it and then creating so from the initial direction, I'm just creating a rotation in here. So with a pattern, you're taking that mask and rotating it around Y.
[16:36] And also creating a signed offset. So from to the right, it should rotate like this and to the left, it should rotate like this.
[16:44] And then I just do the rotation. And I'm also doing a LERP between the first direction, which is this one around, in this case, the Y, and the second direction, which is this rotation in here.
[16:58] And for Z bias, I'm using this, this ramp in here. So I can manipulate in here how it moves, how it rotates. I mean, in here, I'm just moving it so it moves down the liquid and then it wraps around the shape of the cookie.
[17:12] So it's a bit low level. I tried with, as it calls, flow field is not potential flow. That's it. So I tried with this one, but it was creating some directions outside the boundaries of the cookie.
[17:27] And honestly, it was my first or second time using that and I couldn't manipulate it. So I did it manually with this. I did a poor explanation, but it's basically taking a reference vector and rotating it with a ramp using a mask as an input.
[17:42] So that's basically it. You can also have a look on the full file on Patreon. I'm going to share the scene there and you can explore. And if you have questions, I will do a better job at explaining when I'm not recording.
[17:54] So then in here, I'm going to create a fog volume mask so I can mask my velocity field in the end. So that's the last step before we move into clips. So I just take a BDB from polygons and also connect in here, create a fog volume for the mask if you remember that we had in here, this mask.
[18:16] So I'm also, uh, depending that mask, creating a visibility to white mask and in here, I'm just taking the mask and doing a basic, uh, basic sign. So I'm taking, I'm using the sign, manipulating the frequency.
[18:32] So the sign is based on the mask and I'm manipulating in here the repetitions with these attributes, I'm multiplying before the sign and then just using some masks to mask up the bottom and the little part on the top.
[18:45] And I'm not putting, uh, also the masking here. So writing to it, which will look something like this. So it will have low values on the indentations and I values right in here one into these sections, which I want to bulge out.
[18:59] So that's basically what I'm doing, then just doing a transform attribute to move it to the position and that's our mask in here. I'm just blasting the surface, the SDF.
[19:09] So let's move into flip a stock with a sphere, move it to the top and to the back a bit, do a mountain and animate the noise. So we these animate feature doing a flip source, which is really basic, connecting in here and the particle separation of the flip object,
[19:23] jittering the seeds and in here I'm adding the surface of the flip source of the SDF and this wrangle just creates an animated, so an animated velocity, which will look something like this, which is again using a quaternion starting with an initial direction for the velocity, which is minus one. So negative why loading here the time where I'm manipulating out with animates. So I'm multiplying time by the frequency and do a basic offset.
[19:52] Then I take, I create an angle for the quaternion, which is a scene of the time multiplied by a max angle. So how much the max angle of this rotation and just do the rotation of the initial vector. So pointing out I just rotated around that, then I multiply the overall velocity by a multiplier in here and assign it to. So this is setting initial velocity.
[20:16] I'm also setting in here a density attribute for the for flip because I'm going to do density by attributes and this is our source. So let me actually get rid of this and go back to the frame one. So I cover all the velocity fields. So now we're going to move into the top.
[20:33] So I'm going to do the top. In here I'm loading flip objects, setting the particle separation, doing some viscosity and that's basically it in here. Also I decrease the grid scale to have more resolution of the volume and then do a volume source. So I'm just emitting until frame 168 and doing in here just
[20:51] where is that initialized and source flip and I'm loading the first contact geometry. So it emits constantly until this frame. So then I do a basic volume sample of that mask volume. So this one.
[21:05] And I manipulate the density, which I'm doing in here density by attributes as you can see. And I'm going to relate to density between two values. So one, it will be more dense. So the fluid will flow more quickly and they are the one the other one will be smaller. So the fluid will get stuck.
[21:22] Then I do the right velocity, which just wraps the liquid around the cookie. So again, now I'm doing a volume sample V because I want to get that velocity field, which points, which is a direction, a direction that points against the cookie.
[21:38] Then I just add to the velocity with a multiplier. So this one is the one that points to the cookie. So it wraps around in here. I'm just loading that velocity field. Then we have that strange rotated velocity field, which I'm doing the same and just adding to the velocity.
[21:53] As you can see, we have this value push to push the liquid. So because at the first I was getting only fluid flowing in the center and I wanted to add that wrapping around of the cookie.
[22:04] And then in here, I'm just multiplying the velocity field so with the gas field wrangle into the volume velocity.
[22:10] So I'm just basically decreasing the velocity where it creates those indentations. And that's basically adding some surface tension density by attribute, of course, enabling viscosity and setting in here some volume limits. So this was too much.
[22:24] But anyways, static object, which is loading the collider, the geometry, the VDB, doing a volume sample and connecting the division size to a year, as you can see.
[22:36] So then, stopping partying the flip, doing a fluid compress and caching the fluid. So this will be packed points. Then we do a particle fluid surface to x-rat the points.
[22:50] So it looks something like this as you can see, it's create those indentations and I just stand away to to mesh the fluid VDB from particles VDB small VDB reshape and convert it to a mesh then creating some normals, smoothing out the position, blurring a bit normals, which I said to points and converting these two polygons.
[23:09] So I'm not even a turbo transferring the velocity because well, I just did a basic render I didn't care about motion blur so and the liquid is moving really, really slowly so I didn't even care.
[23:24] And this is just some random project so is nothing too serious so I was not worried about motion blur. So this is our fluid then of course I merge everything together, apply the transform to move the cookie, create some normals, merging in the liquid out-lops and exporting to USD.
[23:45] Then let's move into sublarge which is really basic.
[23:50] So sublayering the exported mesh.
[23:55] And of course I'm not rendering the iPoly this is the low poly. Creating some dicing on the cookie so I increase the dicing might not even be that important.
[24:03] Creating some lights in here so I can show you so is just an area light pointing in here to the side some dome lights to create some reflections with a low intensity and creating a camera also which you know how to do render settings expo and then the materials so let's have a look in here.
[24:20] The materials so let's look at the cookie I'm just importing the I'd from that copnet not even playing with the scale because the standard I'd be it was baked on the same scale.
[24:34] Importing the normal map might not be even necessary and importing the albedo which I'm doing some game a down to create some more contrast for the cream of course in here on the cookie I'm also connecting the albedo to the subsurface which is everything that I'm using and producing a bit of scale.
[24:50] For the cream so the chocolate is just subsurface with this scale with this color nothing too crazy and for the decoration again same thing really lazy just some chocolate color and some subsurface so yeah that's basically it because you can see the final result.
[25:09] Again I hope you have learned something new from this I will upload the full scene to patreon where you can find all the project files from my videos including this one of course.
[25:17] And yeah let me know if you learned something from this it was just like free overview of the project and if you want to grab it you can do so on my page and thank you for watching and let me know your opinions in the comments thank you see you next time.



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

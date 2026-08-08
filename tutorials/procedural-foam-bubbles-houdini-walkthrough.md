---
title: Procedural Foam Bubbles Houdini Walkthrough
source: YouTube
url: https://www.youtube.com/watch?v=eQBSMVwHB40
author: newa
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-foam-bubbles-houdini-walkthrough/
frame_count: 0
frame_status: pending-selection
---

# Procedural Foam Bubbles Houdini Walkthrough

**Source:** [YouTube](https://www.youtube.com/watch?v=eQBSMVwHB40)
**Author:** newa
**Duration:** 17m26s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-foam-bubbles-houdini-walkthrough <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone!
[0:02] Recently I've been playing a bit with bubbles in Houdini and I wanted to share the setup that I'm using for some of the renders.
[0:10] Here is the result of the file that I'm going through right now.
[0:15] So we start out with basic grid, get normal UVs and do extra subdivide.
[0:24] Here in my Copnet I have a logo that I get the alpha off.
[0:30] And I here use the SDF to get a smoother transition.
[0:38] Then this is my height, if I put it in my material. This is the height that I'm getting.
[0:44] So here I'm doing the height on the grid.
[0:50] Then in here I'm just displacing it by the attribute.
[0:54] And when we... oh yes, wait.
[1:00] And when we then do attribute from map from this volume, make sure to have the correct name.
[1:08] Then I just displaced the grid using that attribute.
[1:12] Normalize, do normal second-o-mash and delete the color because this one also creates a color.
[1:20] So then I have a nice smooth mesh.
[1:24] Then I get the ambient occlusion for this because I wanted to have a better outline of the bubbles.
[1:34] Then here I just make the mask 1 minus the height.
[1:42] Then here, this is like the first mask because I didn't want bubbles in the center.
[1:48] Then do a minimum of just some noise. Then add some more noise on top of it.
[1:55] Then remove the ambient occlusion here.
[2:02] We get the minimum of the mask, the invert of the ambient occlusion and the height for the bottom part.
[2:10] So I have three sizes of points, let's say, that I'm using because you could use a dart throwing algorithm.
[2:20] I want to have more control of the shapes and distribution.
[2:25] So here I just draw some zero values from a mask because I don't need points over there.
[2:33] Then I create a scatter with some points using the mask.
[2:38] Then create a p-scale attribute and I placed two extra bubbles because I wanted to have them there.
[2:46] I'm using this to visualize my points as spheres.
[2:50] You could also probably use disks here but it's less good.
[3:02] Or you can do this first so you don't even need this basically.
[3:10] So these are the big bubbles.
[3:14] Then here I'm just setting a frequency for the remesh bubbles.
[3:18] So the bigger ones have more density than the smaller ones so everything has an equal mesh density.
[3:25] Let's say I just give them a group for later on.
[3:29] Then here I draw my mask for the... I know I do a minimum again on the mask to scatter more bubble points.
[3:40] I fix the p-scale here by getting the near points in a certain radius.
[3:46] Then if it's not the current point, then we get our point, we get the position of that point,
[3:55] we get the distance from our current point to that point and then we calculate the p-scale.
[4:02] So this p-scale is just the distance to the closest point divided by two.
[4:08] Then here you could also just do an attribute that just floats and not even this.
[4:14] But here I did some overlapping to get some better bubble shapes.
[4:19] Then here the mask is adjusted.
[4:23] So I look in a certain radius, I create my mask and then for each point in the radius,
[4:32] so like for the 100 points in the 1 radius, I also get the distance from our current point to the point that we found.
[4:41] I get the p-scale of that point and if the distance is smaller than our current p-scale divided by two
[4:51] and the other point p-scale, then mask is 1.
[4:56] So that means if I then remove the points based on the mask, I don't have overlapping points inside of here.
[5:08] And then here I also just set the frequency and create a group for the medium size points.
[5:16] Then here I again have my mask attribute and I create the edge.
[5:25] If you visualize it, it's just like this using the height basically the relative point box.
[5:32] Again, do some noise on the mask, some more noise.
[5:37] Then say then add the edge back on the mask, but make the less bit strong.
[5:43] And then scatter a lot of points here using the mask again.
[5:49] Then we again do the p-scale fix by setting the p-scale to like the closest point that it can find.
[5:56] So they never overlap.
[5:58] But then again, adjust it a bit using some noise.
[6:02] Then here random to get some more variation in sizes.
[6:08] Then here I just do if it's too big then just delete them.
[6:13] I don't know if it's not doing anything even.
[6:16] Then here we again do the same with these points so we don't have points inside of there.
[6:23] So if we then blast these points, we get the non-overlapping points here.
[6:31] And then here yes, it's frequency and a group again.
[6:35] So when we merge everything, some bubbles overlap because that's how bubbles are.
[6:41] But it's not like there are a lot of bubbles inside each other then.
[6:47] Yeah, this was again to preview it.
[6:50] Then here make them overlap a bit more.
[6:55] I use this node to do some camera calling.
[6:59] So if this is my camera, I don't have like points everywhere.
[7:04] You just need to be careful with the reflection of your bubbles that you don't see like that there's nothing anymore.
[7:09] Here I just save my p-scale again because in the remesh bubbles it doesn't transfer the p-scale attribute.
[7:16] So I just created an extra one.
[7:18] Then when we do the remesh bubbles, we get our bubbles.
[7:24] And they are nicely bubbly.
[7:29] So yeah, here yeah, this doesn't matter anymore because we set our frequency ourselves.
[7:39] Then I just added some bulge, made them a bit smoother and did a very small offset for like, get a bit more gaps.
[7:50] Then this group is like the small.
[7:54] And then get the intersecting small ones with when the p-scale is like too big for like the biggest points in the small group to give them some more resolution otherwise like here.
[8:10] You could see like the faces when they're too big so I just simplified them once extra.
[8:17] So then these are like our main bubbles.
[8:20] But I wanted to have like, so here I have my grid.
[8:28] Then I just extruded to have like my soap bar.
[8:33] But I didn't want my bubbles to intersect with the mesh.
[8:37] So what I did was I got my volume and then I displaced the position of the bubbles by the volume.
[8:47] So when we do a clip just on the zero axis like this and then we get our rest position back.
[8:55] We have like the nice cut out otherwise without this.
[9:03] We would just have a flat thing and when we would place it on our soap bar then if you look inside.
[9:13] It's just flat and it's not going inside the thing anymore.
[9:19] So I just add the same displacement to my bubbles, clip it and then just put them back to the rest position.
[9:29] This was a very handy trick because first I was doing it with Booleans but that was way too long to look.
[9:35] So this was a good solution.
[9:37] Here I remove every attribute except these, save my rest position and my rest normals.
[9:44] And these are my bubbles.
[9:48] And yeah, then I just promote this.
[9:51] Do some naming for insularis that I can use.
[10:00] Because I wanted to try and optimize it a bit.
[10:03] I don't know if I still used it but to not have like HRI reflections on the small ones and only on the bigger ones.
[10:11] Because on the small ones you probably wouldn't see it.
[10:13] So that's why I needed names.
[10:15] But then here we can merge the bubbles with our displaced grids.
[10:22] So then we can...
[10:25] Here I got the index.
[10:27] I don't know if I really needed my setup.
[10:31] I was doing some fine attribute fell probably.
[10:35] So that's why I needed the index but I think it's fine without.
[10:41] So what I do is I get my ambient occlusion.
[10:51] Like this.
[10:53] Then I wanted to add some very tiny noise.
[10:58] So yeah, I originally had this.
[11:02] I blur it and I get the difference between the two.
[11:05] And then there's a blend for noise but I don't think it really does anything.
[11:13] So then I have my bubble attribute here.
[11:18] So just like where there's ambient occlusion.
[11:22] That's where the foam is going to be by the way.
[11:25] Then we do some noise again on top of that.
[11:29] And then do our...
[11:31] Yeah, because I didn't want like here some of the down things to make it more still have the original shape.
[11:41] Then I cleaned it.
[11:43] Scattered it.
[11:45] Scattered some points on it.
[11:47] Okay, so yeah, I recorded this but when I was recording my scatter and density were too high of a resolution.
[11:55] And my Houdini or like my recording was lagging.
[11:59] So this was the value I'm using here but I'm going to reduce both of them a bit.
[12:05] And I also already reduced my scatter.
[12:08] I first had 4 million but now it's 1 million.
[12:13] So this is my scatter.
[12:16] Then in this attribute fob I'm doing the density of the points.
[12:23] So like the max points and then fitting the points found from 1 and this value to 0 and 1.
[12:33] So where it's like more dense we get brighter colors and where it's like less dense.
[12:41] It's darker.
[12:43] So then we can map this to the p-scale.
[12:46] The little color.
[12:48] Do some more curling.
[12:51] Then a VDB from particles.
[12:54] Now you don't almost see anything but if you do a pyro bake we can see the foam.
[13:00] So this is a lower resolution than I originally used.
[13:03] I used 0,0,0,9 but for the recording I lowered it a bit.
[13:09] Then a smooth.
[13:11] Do smooth the mesh a bit like the volume.
[13:16] So yes.
[13:18] And then here I'm just looking if my density is inside the SDF.
[13:24] Then I'm setting the density to 0 so we don't have any foam inside or bubbles.
[13:31] So yeah this is the SDF I'm using.
[13:35] Then here this is the result.
[13:39] It's a lower resolution so maybe more gets deleted now.
[13:43] Then here I just add some very small noise by multiplying it and then multiplying this with the original density.
[13:53] And because we want some specular on our volume we also need the gradient of the volume.
[14:00] This is like similar to the normals.
[14:04] It's like the normals of the volume basically.
[14:07] And then we merge these so we have our density and gradient and to optimize it a bit I resampled my gradient so it's less, it's like a higher voxel size.
[14:20] So and then I cache this and then this was my result with the high resolution.
[14:27] So yeah.
[14:29] Then in the materials.
[14:31] So then the materials are pretty simple.
[14:36] Let's check.
[14:38] I import my camera that I had for the calling.
[14:41] I reference to the SD file of the bubbles.
[14:44] I set here bubbles.
[14:47] Then this is just the volume that's pointing to the cache.
[14:53] And then here yeah the switch is just on this one.
[14:57] Then here is just also reference to the soap bar UC file.
[15:03] The materials also pretty simple.
[15:07] The soap bar is just, yeah no wait.
[15:16] Yes, yeah the soap bar is just some subsurface and stuff.
[15:21] The bubbles, I am doing some stuff with the bubbles.
[15:26] Wait, maybe disable this for.
[15:31] So for the bubbles I'm using a noise as the thin film thickness but normally this has more of the spurly type noise patterns.
[15:44] So what I'm doing is if you visualize it here.
[15:51] Yeah this is a noise pattern I'm using but it's just two noises mixed.
[15:57] And then these noises I'm using as the position for my other noise here.
[16:04] So it gets a bit distorted and then ranging this from the minimum thickness to the max thickness.
[16:13] And also blending it a bit with another noise and 600.
[16:17] So the average is 600 then.
[16:20] Yeah just transmission roughness low.
[16:24] So yes.
[16:26] Okay so yeah this is the volume shader.
[16:30] And it's just like, it's a preset white water material.
[16:36] So here we need our gradient.
[16:38] Then here it's just scattering color density.
[16:41] I remap it to a larger number.
[16:47] I get some reflection color here.
[16:50] Set the roughness to 0.15 and then the stroke to minus 0.4.
[16:57] And if we add everything together then.
[17:03] We can see now it's like a very dark volume.
[17:07] But it's because you don't have enough volume limit when not breathing in the Karma Render setting.
[17:14] So when you preview it here with enough limits we can see it gets white and it's fine.
[17:20] So yeah that's the work through of the setup.
[17:23] Hopefully it was useful and thanks for watching.



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

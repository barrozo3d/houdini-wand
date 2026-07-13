---
title: Custom Procedural Materials with Houdini and Karma
source: YouTube
url: https://www.youtube.com/watch?v=M6W_EP48BaI
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/custom-procedural-materials-with-houdini-and-karma/
frame_count: 0
frame_status: pending-selection
---

# Custom Procedural Materials with Houdini and Karma

**Source:** [YouTube](https://www.youtube.com/watch?v=M6W_EP48BaI)
**Author:** cgside
**Duration:** 16m15s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py custom-procedural-materials-with-houdini-and-karma <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Creating the pattern [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm going to show you how to create something like this.
[0:08] Because some material made with Odini and in material X.
[0:14] So let's jump in. So the first thing we will have a look is on how to create this pattern in here.
[0:23] That will end up creating this bulging effect on the...
[0:29] This is supposed to be an old mattress. So let's start looking in here.
[0:38] We start with a circle then we carve it.
[0:42] And save out the bounding box size of this curve.
[0:49] Then I'm copying it a few times using the... the bounding box.
[0:55] Then placing it in the center. Now I can box clip.
[1:02] So I can extract the... the tiling pattern.
[1:06] That's our goal to create the tiling pattern.
[1:10] So I'm using the dead attribute we saved of the bounding box X and Z.
[1:18] Then as this is not actually joined, I'm creating a polypads.
[1:24] Then grouping the center points and cutting them.
[1:29] So I get these four different shapes.
[1:34] And this is our pattern.
[1:36] Now we need to transform it if we have a look at the size here.
[1:43] It's not squared. So we need to make it square so we can bake it to a texture.
[1:51] So in the transform we take the X size which is the largest one.
[2:00] And divided by the Z size which is a smaller one.
[2:05] And we target the X as this scale.
[2:10] And now that we have a square pattern, we can save out again the bounding box size of this pattern.
[2:22] So we can use it later.
[2:24] And we copy it a few times and place it in the center as we have done before.
[2:35] Because I want to create some geometry from this.
[2:42] So now I am sorting the primitives by proximity to points.
[2:48] And in a range I can select the four last primitives that I want to blast.
[2:57] Then I'm grouping one of the elements.
[3:03] And blasting everything else.
[3:06] Ginding the pads.
[3:09] And now I can polyfill it.
[3:12] And blast away the curves.
[3:15] Rematch it.
[3:17] And now I want to create a mask.
[3:19] So I can create that bulging effect, that displacement effect.
[3:24] So far that I'm going to group the unshared edges.
[3:27] The unshared points I mean.
[3:29] And then create a distance along geometry to create the mask from those points.
[3:38] And I'm blurring a bit the mask.
[3:40] And in a point of I'm just displacing the with that mask with that distance that you would.
[3:54] Saving again the bounding box size of this pattern.
[3:59] And copying it a few times.
[4:04] Generating a connectivity for some reason.
[4:11] And clipping it again using the bounding box size that we saved in here.
[4:19] No, that we saved before.
[4:24] And now in order to bake a color map.
[4:30] We need obviously to add some color.
[4:32] So I chose blue, which is an easy color to key.
[4:37] And it shows red for this part, which I'm going to cover now.
[4:45] So from this pattern we had before.
[4:49] I'm cutting all the points.
[4:53] Cutting all the primitives by the points.
[4:57] So creating separated primitives.
[5:01] Then in a wrangle I'm creating a attribute for every second-brim.
[5:05] So we can have a look.
[5:08] So red, blue, red, blue.
[5:12] And from there we can carve by attribute.
[5:17] This is new to all in the 20.
[5:20] You can also blast, but just let's use carve by attribute since we have it now.
[5:28] And then we can sweep.
[5:32] And we will have something like this.
[5:38] Then we can box sweep everything, give it a color.
[5:43] And this is what we're going to bake to a texture.
[5:49] So for the iris we plug this.
[5:54] And for the lower as we can just create a bound as a rectangle.
[6:00] And group some vertices, the top vertices.
[6:09] So in the UV flatten we can properly orient the UVs.
[6:16] As you can see I'm using those pin-ed vertices.
[6:22] And that's why I am grouping the vertices.
[6:27] And then just adding some subdivisions because sometimes it helps for the baking process.
[6:34] And in here I'm just baking.
[6:39] I am baking the eye and the color.
[6:43] And I can show you how that looks.
[6:50] So this is the color that I baked.
[6:56] And this is the displacement which doesn't look like much, but if we normalize it or equalize it, you can see how it's looking.


### Creating the texture [7:10]
**Transcript (timestamped):**
[7:11] Now let's see how to create something like this.
[7:14] This stitching pattern.
[7:18] So I'm starting with a trace of an image I had.
[7:24] And placing it on the ground.
[7:30] Then I am dividing horizontally along the Z axis I believe.
[7:37] Yes.
[7:39] And what I'm doing in here is taking the Z size of the pounding box and dividing it by the number of divisions I want.
[7:49] As you can see I have, I can change this to 150 or more or less.
[7:57] And you can do this for all the axis.
[8:02] Then I'm grouping the inner edges using this mean edge angle.
[8:12] And dissolving everything.
[8:17] I mean I am grouping all these edges and creating curves from that group.
[8:30] And then fusing polypads to create single primitives.
[8:36] And then re-sampling it.
[8:41] Then I can use a polycut to cut all the primitives just like we have done before.
[8:47] And in here just instead of using the curve I am just removing every second cream.
[8:54] Then sweep it and that's basically it.
[8:59] And I can import the texture with an attribute from map.
[9:05] And since it is so flat you won't need much geometry.
[9:10] The colors will spread out well.
[9:14] At least good enough.
[9:17] And then I can promote it to primitives to have a better flat shading.
[9:26] And that's basically it.
[9:28] I want to add a background line so it doesn't render transparent.
[9:37] And then you bake out the, in this case I am baking out the normal and the color map.
[9:49] And again the same thing for the low resolution mesh.
[9:58] When you are baking just using a flat plane.
[10:02] You can see all these looks.
[10:04] They can be overlapping. There is no problem.
[10:07] Because we have a max-res distance here.
[10:13] You can set it to a value that makes sense.
[10:19] If we have a look at it and show individualize there is plenty of space to bake out the texture.
[10:30] And when you have it baked, we can have a look.
[10:37] We will have something like this.
[10:46] We will have this flowering pattern that I found online.
[10:51] And it's okay to use an external file as long as it is at least styleable.
[10:58] And you can manipulate it in a way that fits your needs.
[11:04] So that's totally fine to use styleable textures in a procedural workflow.
[11:13] And of course we also have the normal map that we baked.
[11:18] So it's looking nice.
[11:21] No errors of that whatsoever.
[11:24] So we can move to shading now.


### Shading [11:28]
**Transcript (timestamped):**
[11:29] So this is our final shader.
[11:32] And let's break it down right now.
[11:35] So let me connect the unlit material to the surface.
[11:47] And we start with the noise.
[11:56] We start with this noise that I created by using the unified noise.
[12:03] Set to worldly and displacing it a bit with or disturbing the noise with another one, which is a fractal.
[12:16] And from there we can import our baked textures.
[12:22] So first this one in here, that is the flower pattern.
[12:31] And in order to separate them, we can use a separate tree or a vector to float.
[12:39] And we need to remap them and clamp them somehow to extract the different channels.
[12:46] So in this case I want to extract the red and the green.
[12:56] And then I'm using that with the color mix.
[13:02] So the first one we're colorizing these leaves.
[13:09] And then in the other one we are colorizing the flowers.
[13:18] And all of that mixed together we get something like this.
[13:28] And also adding a background color, this beige color.
[13:36] As you can see in here.
[13:40] And for the mix I am using the two masks added together.
[13:55] Then I'm also adding the stitches, adding some color to the stitches,
[14:05] by importing that particular mask that I've picked.
[14:11] And then just multiplying the noise on top.
[14:22] And we get something like this.
[14:32] And let's switch to the shader, main shader.
[14:42] And as you can see for the I am using two normal maps in here.
[14:54] So in order to connect them you can create a normal map.
[15:02] Import the image, create a normal map and then connect the second normal map to the normal of the first one.
[15:11] So I believe I'm using these normal map in here.
[15:17] And a textile normal map for the main color.
[15:29] And of course we're using the displacement as you can see in here.
[15:33] It's creating this waving effect and also the stitching.
[15:38] Which is a bit too big, but I guess now I won't change it.
[15:48] So that's basically it.
[15:52] I hope you have learned something new.
[15:55] As always you can get the files on my Patreon.
[15:59] And thank you everyone that is supporting me over there.
[16:03] That helps me to continue to create these tutorials and share project files with you guys.
[16:11] Thank you for watching. See you next time.



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

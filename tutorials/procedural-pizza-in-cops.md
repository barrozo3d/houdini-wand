---
title: Procedural Pizza in COPS
source: YouTube
url: https://www.youtube.com/watch?v=mL2TkAB_Rqc
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-pizza-in-cops/
frame_count: 0
frame_status: pending-selection
---

# Procedural Pizza in COPS

**Source:** [YouTube](https://www.youtube.com/watch?v=mL2TkAB_Rqc)
**Author:** cgside
**Duration:** 12m56s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-pizza-in-cops <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Creating the pizza crust [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this tutorial I'm gonna be breaking down some of the parts of this procedural piece of material in Cops.
[0:09] If you want to have access to the full scene you can download it from my Patreon, but I will break down the most interesting parts. So yeah let's get into it.
[0:19] So we will start from the beginning. The first thing I did was to play around with the Crest material and the displacements to have this rounded look.
[0:30] And the way I'm doing that I start with the ring, play with the size, compared to the SDF to a mono and also smooth it a little bit.
[0:39] So I can have that typical rounded look and I can connect this to a preview material and connect this to the height.
[0:48] Let's right away play with the size, 0.01, change this to grid, divisions to 500 and let's see how that looks.
[0:57] So as you can see it doesn't look like that, so I need to increase this to 0.01 let's say.
[1:03] And as you can see this will give us this pointy shape which is not ideal.
[1:10] So the way I'm solving that is by blurring, but as you can see it will blur everything.
[1:16] Then I blend it with minimum modes with the original texture and I get this sort of result and then I just blur it a little bit more.
[1:25] And I get the desired result. If I increase these a little bit to 0.2, you start to see the results.
[1:32] So it's not perfect but it was the way I found to create these rounded look while keeping some sort of sharp corners.
[1:40] Then I'm also distorting this shape, so I'm creating this distortion, but I don't want the effect on the interior to be the same as the exterior part.
[1:51] So I'm creating a masking here to change the scale of the distortion.
[1:58] And if we look at the final result it will look something along those lines.
[2:04] And then I'm also adding some breaks on the crust and it's funny how I did that.
[2:12] I started with this asterisk shape which thinking about it doesn't make much sense to use these in any project, but in this case it was useful.
[2:22] So converting it to mono, blending with some noise, eroding it a little bit, transforming it and distorting it.
[2:29] And then when we blend it with the original shape we get this sort of result which will look something like this.
[2:37] In this case it will look to random, but when blended over the blurred result and the other materials it will look something like this.
[2:48] So as you can see in here it will have these breaks on the crust which was the sort of look I was after.


### Procedural leaf generation [2:55]
**Transcript (timestamped):**
[2:56] So the most challenging part was definitely the leaves, these leaves that go on the pizza and I'm gonna be breaking down how I did that.
[3:05] So I'm creating them in soaps and this is the powerful thing about cops that you can combine it with the other parts of Odini in this case soaps.
[3:16] And then resurrecting it to create the materials in cops.
[3:22] So I'm starting with the line with sampling and creating the curvy attribute, then deforming it to a leaf shape just by setting the normals and deforming it along the normals, play with the ramp, mirroring and from here I'm creating a polypath to unify the shape,
[3:40] polyfill it to have some geometry and adding some normals and then removing the curve.
[3:47] So this is the leaf base and for the lines I'm just copying two points a few lines.
[3:53] First of all I'm carving a little bit the top and bottom so I can control the position of the veins let's say.
[4:03] Then reassembling it and in here I'm setting the normals and let's have a look how I did that.
[4:10] Basically I'm creating the normals between one and minus one in the X axis and also creating the the aperture both the same way so I can rotate it later.
[4:24] And it's really simple we just use the modelo so we have 0 and 1 repeating and then scale it multiplied by 2 and subtract 1 to have 0 centroid offset so minus 1 and 1.
[4:36] This way it will alternate between the points minus 1 and 1.
[4:41] Then I'm doing a attribute adjust factor and rotating randomly the app the normals along the aperture boot as you can see that's why it was important to create that aperture boot.
[4:52] And then just playing with the p-scale and we get this sort of result if I can add your normals.
[5:01] And then we can re-project it to the the leaf mesh as you can see to create the veins re-sampling it and I'm also creating some vectors in here with the cross product so I can deform it down along the curve you as you can see in here.
[5:18] And then we can re-sample it again to have less points and re-sampling less time and set it to subdivision curves and we get this sort of result.
[5:30] So this is a very basic leaf that that will work for our purpose.
[5:35] I also did something here so after getting the interior part of the leaves I'm creating along after remaching also the leaf.
[5:45] I am creating a near-point group and along with the unshared.
[5:51] So in here I'm combining the two groups so I can create a mask to play with the interior parts of the leaf as you can see in here.
[6:01] If I normalize the attribute you can see the result and I'm doing that by using the surface distance function we covered that before we start with the group of points.
[6:11] And then we measure the distance between the group and the interior part.
[6:17] Then we do a attribute blur and we have everything we need for our stamping or our restoration let's say.
[6:25] So I'm re-sampleizing here the alpha which will be just the leaf and the leaf interior because I also have a attribute set in there as you can see in here, life interior.
[6:37] And also the surface distance as you can see this will help us to create that bump effect on the interior parts of the leaf.
[6:46] Creating the color and in here I'm applying a distortion to both to weld the shapes and also creating some noises for the shading.
[6:59] And I'm applying the distort to weld the attributes so I can stamp them within the same position and still have access to them as you can see that way I can blend the different layers later or the shading and the displacement also.
[7:15] So as you can see in here if I check the stamp we have the stamp we have the final result but if I look at the ID we have a different ID for the interior parts that way I can come in here, here we have.
[7:28] So if I check this compare I gave the ID of the interior parts the veins an ID of 999 so I can isolate that with a compare and then we can just blend in that attribute.
[7:43] So that's basically how I've done those leaves then I blend I also created some I also created some curling on the leaves or some band as you can see they are not flat and the way I'm doing that is by is by extracting the UVs that we have in here let's see.
[8:08] So we have here the UVs and then in here I am creating a ramp from the UVs with this inverted yield ramp and then I just blend it over our displacement map.
[8:21] So in this case I am blending them in here in here as you can see I'm multiplying over to the leaf shape to have that curling effect.
[8:32] So yeah that's mainly how I created the leaves hopefully you got some tips out of this and let's move on.


### Cloth material techniques [8:40]
**Transcript (timestamped):**
[8:40] So now I wanted to show you how I created the cloud material which on itself is quite boring but it can show us a feature or two about the scops workflow.
[8:54] So let's look first at this top import where I'm creating the points to do the stamping.
[9:00] So I'm starting with the grids with four primitives and if you look at the primitive numbers we have 0, 1, 3, 2.
[9:09] So I want this in a circular pattern so I can iterate over each two sections each two primitives and create the stamp attribute so we can overlay different colors in cups.
[9:20] So first of all I'm sorting them in a circular pattern the way I'm doing that is just by reversing the primitive order of the second and third primitives so 0, 1, 2, 3.
[9:30] Then I'm doing a 4-inch, it is called 4-inch count for each number.
[9:35] 4-inch number and I'm setting these two 4 iterations since I want four sections out of this grid.
[9:41] Then in a group range I'm selecting two primitives out of four and as an offset I'm using the 4-inch count the iteration attribute as you can see in here.
[9:51] And these will iterate over each two sets of primitives.
[9:57] Then blasting those isolated primitives in the group range is writing this and troid and here I'm setting the stamp attribute to be the iteration attribute as you can see.
[10:08] And we will have 0, 1, 2 and 3 so after each iteration and these will merge the points so we will have eight points.
[10:18] And now in here we can do the stamping and I'm stamping the first stamp will be the first and last stamp will be this white color and the second and third will be this blue.
[10:29] And if we set it to default we will have this sort of result but we've unsorted that weighted over we get this blending effect of the different stamps.
[10:42] And then we can move it to the center by translating in x and y 0.5 and then just repeat it with the uniform scale transform as you can see.
[10:52] And finally we can add some noise over the top some noise that is scaled along the X as you can see.
[10:58] And so the main takeaway is this stamp ID that we can blend with these as you can see we can change it in here the blending and get some different results.
[11:11] So yeah that's how I created the cloud material and other than that if you are interested in this full scene you can check it out on my patron how I did the normals and everything.
[11:27] And hopefully if I showed you the most interesting parts you can look in there how I did the slicing of the piece because I'm also creating that in sobs and then blending over the we can actually go over that.


### Finalizing pizza slice [11:41]
**Transcript (timestamped):**
[11:42] So in this case to do the slicing I'm starting with a circle which is white dancing divisions but it's a number that we can divide easily.
[11:55] And then doing a class attribute in here to divide it by 8.
[12:01] Blasting the part I want in this case I can change the piece in this case I chose 5 remove the unchared and doing a basic inset so I can have an attribute to play with in in cops.
[12:17] So that's basically how I've done that slicing then I'm in here I'm isolating that slice and isolating the rest transforming the slice and blending it over.
[12:30] And this is how it looks the final albedo texture as you can see.
[12:35] So yeah a lot of work it looks somewhat decent again if you are interested in the material check out my patron where you can find lots of tutorials exclusive tutorials.
[12:46] Courses and all the project files from my videos let me know in the comments if you found this useful and I guess I'll see you next time.
[12:54] Thank you.



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

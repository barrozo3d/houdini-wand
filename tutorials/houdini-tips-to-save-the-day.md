---
title: Houdini tips to save the day
source: YouTube
url: https://www.youtube.com/watch?v=lT0b8D6LmtM
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-tips-to-save-the-day/
frame_count: 0
frame_status: pending-selection
---

# Houdini tips to save the day

**Source:** [YouTube](https://www.youtube.com/watch?v=lT0b8D6LmtM)
**Author:** cgside
**Duration:** 10m27s | 4 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-tips-to-save-the-day <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I wanted to share a few tips and tricks.
[0:05] I haven't done one of these in a while, so hopefully you'll get away with some new techniques.
[0:11] So I wanted to start with this simple example where let's say you want to scatter or some
[0:17] out-transform the outside parts or the ins or only the inside of this geometry and you
[0:23] have no access to the full network. So this could be easily done by targeting the
[0:29] prims facing the positive Z or the negative Z. But let's say you don't have access to
[0:35] the previous part and you only have this geometry. So the end goal is to create this sort
[0:41] of mask, so either outside or inside part and then we can clip it. And the way I'm
[0:48] going to do that, so we have the geometry. We calculate a connectivity, so just a class
[0:53] attribute on prims. Then we extract the centroid we add by group and we orient along the curve
[1:03] and we create some custom normals. In this case I don't want to save it as normal, I want
[1:07] to save it as underscore N or any other name. So that way I can copy that attribute to
[1:13] normals to the geometry and we will have that attribute as you can see. And in order to
[1:19] target the outside parts I can just do a comparison of the normals and that's normal attribute
[1:26] with that out product. And if we output that as a mask we have the outside part and if we
[1:32] invert the sign in here we get the inside that we can like very clip by a attribute as you
[1:38] can see. So I want to go back to a subject that we have explored before on orienting UVs


### UV Orientation [1:40]
**Transcript (timestamped):**
[1:46] up, as you can see. In this case I have this rough light shape and I have on purpose changed
[1:53] the rotation of the UVs. But even if we just do a UV flatten some of the islands might
[2:00] be become inverted as you can see, especially if you have a mirrored light shape. And this
[2:07] HDA that I created that I'm going to show you next can easily orient the UVs up and even
[2:14] if you feed a more complex geometry as you can see I have the UVs sort of scrambled in
[2:21] here and I can just place this one and it should orient properly up. So let's have a look
[2:28] at that HDA I'm going to switch to the simple geometry so this one in here and let's see what UVs
[2:36] I'm going to pick this one. So the idea is still the same we create the connectivity by UV
[2:44] islands and we will have an ID 40 challenge. Then we use the relative point bounding box to get
[2:53] the Y component so we have a value going on the Y direction and as you can see we just use
[3:02] the relative point bounding box and extract the Y component. Then we measure the gradient of that Y
[3:09] valve by piece attribute so by these islands and instead of using the default one of the position
[3:16] attribute which is P we use UV so we can do it in UV space. So this way we don't need to convert
[3:23] this geometry to UV like UV equal or P is equal to UV and after do the measuring there we can just
[3:32] do it in place in here by using the position attribute as UV. Then we just orient the UVs up with
[3:38] these vax snippets which we get the I'm saving these up tangent and we get that we using the
[3:47] prime function. Then we create in here a geo variable that we will unwrap the geometry in place
[3:58] that way we can get the bounding box on the bounding box center in UV space. So we can later subtract
[4:07] the that bounding box center rotate the UVs and get back to the original position
[4:14] after doing the rotation of course. Then we calculate the angle of that with the 8.2 and we do
[4:21] the rotation along the Z axis which is the axis that UVs operate on and that's how we do
[4:29] these UV oriental vz and we can change it to a more complex geometry. So in this one I wanted to


### Uniform Distribution [4:38]
**Transcript (timestamped):**
[4:39] talk about how to do some uniform distribution of shapes. So in this case if I come in here I have
[4:46] just a circle the form along the x axis or scale down and I'm copying these two points as you
[4:53] can see they have a uniform distribution but if I disable these and disable the p-scale they
[5:00] will still have the same uniform distribution but let's say I want to add some random some p-scale
[5:05] along the in this case the x axis. So I'm just mirroring here the bounding box x. So it gets
[5:12] scale down at the ends and more at the bottom at the middle and in order to redistribute them I can
[5:19] use a similar ramp in here but inverted with a resampled by density and I can change the the
[5:27] amount of segments I want then I would need to change the p-scale of course but in this case
[5:32] setting it to 4 and I can come in here and align this better and I can even distribute them the way
[5:37] I want if I want to change that but generally speaking you want to have a similar shape you have
[5:45] on your p-scale. So in the end I have this basic geometry that I build from just those shapes you
[5:53] have in here. You can have a look at the file on patreon if you're interested.


### Conform [5:59]
**Transcript (timestamped):**
[5:59] So let's say you have some geometry in this case I have these towers and I want to
[6:03] conform it to the to this tube. A simple way you can do that is by creating a grid then
[6:11] re-projecting the grid to the tube and use a lattice in point mode. We have a we have a look at
[6:17] this before. Use a lattice in point mode and play with radius and project that's the
[6:23] towers to the shape or conform it to the tube. Another way you can do this is by using the surface
[6:29] deform and as you can see it works a bit better although in some situations it might deform too much
[6:36] the shape. So that's a way to conform a shape to another without because the re-project here it
[6:45] wouldn't work since it has a thickness. So let's have a look at a more complex approach. So in this
[6:52] case let's see I have a circle fusing and sweeping just to get the rows in this case resembling
[7:01] any near I'm saving a prem ID that I probably won't use. Then I'm calculating an aperture
[7:07] boot as you can see in here to point out just by normalizing P and that will be important in a bit.
[7:15] Then I'm sweeping in near some rounded corners like a rectangle and I get this sort of look.
[7:27] Now let's say I want to conform this shape to the sphere so they wrap around.
[7:36] We can use the same approaches in here, use a grid and use the surface deform or the lattice but
[7:42] here the lattice won't work very well. So what we can do or the lattice or the surface deform will
[7:49] deform it too much. So in this case I'm doing after doing this sweep I'm doing another one in here
[7:56] set to ribbon. Then I'm assigning the up to the normals so I can easily re-project it to the sphere.
[8:06] And this is the deform geometry, this is the rest and this is the geometry to be deformed.
[8:11] Then with a simple point deform we can get this sort of look. If I use a surface deform I believe
[8:19] this gives a different result so we back to rest and the deformed as you can see it's not bad,
[8:28] it's just another just another way to do it but as you can see it will look much different. This one
[8:36] this one will have a more bulged out effect so in this case this one may work even better.
[8:43] So that's another way. So as you can see you can use more complex geometry and multiple shapes and
[8:48] these will hold up. I also have a custom one in here that is using a deformation matrix.
[8:57] Basically I wanted to show you in here so let's see how much different that is.
[9:04] So it's not much different but I wanted to show you something in here. So after calculating the
[9:09] matrix by using the normals in an aperture boot I am reading that deformation matrix by using
[9:16] the UV sample and since I have UVs in here because I UV flatten those ribbons I can simply read
[9:26] the position or sample any attribute by using the UVs but in this geometry I don't have the same
[9:36] UVs, I don't even have UVs. So what I can do is to UV sample based on position the UV attribute
[9:44] as you can see and we do get stretched UVs but that won't matter because we can now use the same
[9:51] UV sample to deform to reading that matrix that we calculated by using the UVs again and if we
[9:58] haven't calculated those UVs this wouldn't work as you can see. So just UV sample is such a powerful
[10:05] function that you can apply to reading normals and read any attributes you might want.
[10:12] So yeah guys all the project files will be available on my patreon alongside with exclusive tutorials
[10:19] if you are interested in learning more and as always thank you for watching and I hope to see you
[10:25] next time. Thank you.



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

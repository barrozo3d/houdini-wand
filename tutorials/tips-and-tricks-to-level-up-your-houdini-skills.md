---
title: Tips and Tricks to level up your Houdini Skills
source: YouTube
url: https://www.youtube.com/watch?v=DV0ABu_-yvc
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tips-and-tricks-to-level-up-your-houdini-skills/
frame_count: 0
frame_status: pending-selection
---

# Tips and Tricks to level up your Houdini Skills

**Source:** [YouTube](https://www.youtube.com/watch?v=DV0ABu_-yvc)
**Author:** cgside
**Duration:** 11m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py tips-and-tricks-to-level-up-your-houdini-skills <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome in this video I'll be sharing tips and tricks to level up your
[0:05] Aldini skills from simple Vex snippets to less known subs. Hopefully you'll get away
[0:09] with something worth it. Let's get started.
[0:13] So in this part example I wanted to show you how you can use the rest space to split
[0:18] Prims in half, basically by creating the roofs that you can see in here and also how to
[0:24] do these random rotations also to fit the clip notes. So basically as you can see in
[0:30] here I have these clip notes and just one we don't need to iterate over each frame to
[0:36] clip it in half and each one has a random orientation as you can see.
[0:41] And the way I'm doing that is by setting up after isolating the Prims I'm setting a normal
[0:47] attribute in here, a vector. That is using the sample direction uniform to create a
[0:52] step-or-y-hand attribute. So basically each 90 degrees you should have a random rotation
[0:58] on each frame. So I'm using the Prim num as the seed plus a random number and I can
[1:03] come in here and play with a different seed and get a different result. After that I'm
[1:09] creating a rest attribute. So basically getting the bounding box center of each frame, then
[1:15] saving the current position as a rest attribute or a rest variable. Then from that rest I
[1:21] subtract the center to move every frame to the center as you can see. And then I do the
[1:27] rotation using that normal attribute we just saved and also to wing the rotation in here
[1:33] on the rest. Then and this will mean that if I assign this to the position we will have
[1:44] them in there on the center as you can see and also with the random rotation. So we can
[1:49] actually don't need to do that because we can clip by attributes and using that rest that way
[1:55] we have the Prims split at the end of because we have the rest attribute at the center of the
[2:00] world and with random rotation. We can come in here, play with the random with the seeds and as you
[2:06] can see if I apply this to position we will get just a random cut in here. Not random just a cut
[2:13] on the center of the world but in this case in rest we can apply to every frame as you can see.
[2:20] So yeah that was the first tip. So for this project I was trying to do a procedural
[2:27] summon texture for the sushi piece and the way I ended up doing it was with cops so by importing
[2:37] the piece of geometry with UVs and instead of going through the rest of the setup and
[2:42] rest of the geometry I am using the UVDs function to rest of the original position which allows me
[2:51] to have some expansion, some edge bleed, some padding along the edges so this way it doesn't create
[3:00] that problematic issue on the edges that the rest of the geometry does so as you can see I can get rid
[3:06] of the edge so as you can see this is perfectly fine if I set this to zero well it won't work but if I
[3:14] set this really low you might start to notice some issues but not in this case. So anyways I'm
[3:19] restaurizing the original position which is the position that we have in 3D space by using UVDs
[3:26] and premium UV we have looked at this before. Then I'm extracting a mask along the X using the
[3:32] relative point bounding box and pointing at the geometry and doing that relative bounding box
[3:37] which will look similar to this so just a mask along the X axis as you can see but in this case
[3:47] I'm going to use that this mask to rotate the original position around the Y axis so that's what
[3:55] I'm doing here as an angle I'm using that mask and which means that my original position will be
[4:02] rotated and when I create the salmon pattern I will have this pattern like this as you can see
[4:12] along the X it will get more and more rotated so if I don't do that so if I just use V at
[4:24] RHP in here as you can see it will be straight but I wanted that rotation so I'm using that
[4:31] rotated version to create the pattern and the pattern isn't too hard either so what I'm doing in
[4:38] here is taking that X mask that we saved which I'm doing in here again and feeding that into a
[4:48] scene and also make it absolute and in this case I wanted to invert it so I made it 1.0-
[4:55] multiplied by pi to have the correct amount of repetitions in this case then and also introduced
[5:00] some noise in here to distort a bit the pattern as you can see if I disable that you will see that
[5:07] we have a perfect pattern going on but I wanted that noise then we just need to play with the mask
[5:17] so we can grow or shrink the effect and then modulo in this case I'm doing the modulo
[5:24] I don't think it's needed in here yeah it's the same so we don't need that modulo because we
[5:30] are already using the scene and the absolute function maybe I was playing with something different
[5:35] at the time and yeah that's basically it then I'm blending in some noise and some a mother type of
[5:42] noise in this case a worldly noise converting it to RGB and that's my albedo basically so if I
[5:50] connect this in here and I also have a night texture that I'm creating using this black and white
[6:01] version but yeah that's basically it for the salmaning texture as always you can grab the full scene
[6:07] on my patreon and you will be able to see how I put these all together so still on this project I
[6:16] add these avocado pieces that are simulated with RBD to be in the center of the sushi as you can see
[6:24] in this case I'm doing a transform at the end but yeah I have these pieces simulated and I want to
[6:29] replace them with iPodly geometry so the first thing I'm using in order to use RBD you need
[6:37] packed objects so in the copy to points where I'm copying the first set of pieces I'm going to pack
[6:43] an instance this way it will get from so it will get from this transform it will pack them and save
[6:51] that pack transform then also RBD will will compute that pack transform and then I'm saving that
[7:00] enough i'll catch after the simulation and then I can just import the original pieces
[7:07] in this case I'm doing a pick a subdivide and a mesh sharpen and I'm going to pack them again
[7:12] using the name attribute that I've said attribute promotes to a point attribute the name
[7:18] and in here I can just use a pack inject and it will replace the low poly geometry with the
[7:25] iPodly one that I've created in here again using the original transforms before the copy to points
[7:32] like I showed you in here so as you can see this is the same geometry that I'm bringing in then
[7:38] you can transform it and I'm also saving a name attribute here somewhere so yeah I have the name
[7:43] attribute from the Voronife Ractor as you can see since I started with this avocado shape
[7:49] so yeah pack transform pack inject I mean it can be frustrating at times that it doesn't work
[7:55] but just bear in mind that it needs the intrinsic transform attributes that we do have in here
[8:02] if we look at the frames and pack transform so let me see transform as you can see
[8:10] and in this case is a tree by tree but we should have a packed full transform that is a 4x4
[8:18] and as you can see we have translation we have rotation and scale also
[8:21] so yeah that's the tip I wanted to share back inject
[8:28] so I started working on this procedural building project two days ago and although I'm not going
[8:35] to release it right now I'm going to show you a tip in here that is on how to create this piece
[8:43] of geometry in here so basically we can start at the top I'm isolating a prim then resemble
[8:51] in it two or segments and transforming to be oriented towards the Z axis just removing the geometry
[8:58] with an add-on delete geometry but keep points then I do an enumerate and create an ID for each point
[9:04] copy and transform these around to to the top and set the scale to zero so we we have four points at
[9:11] the top and four points at the bottom if we add by attribute we should have these lines connecting
[9:16] and now I want to create that effect of trans bulging it out and the way I'm doing that is
[9:24] after resembling the curves of course because we need enough geometry we can create a tangent
[9:30] and tribute in this case I'm setting it as normal so it's just tangent going along the curve with
[9:36] an oriental on curve then in here is where I'm creating that bulging effect and basically I'm
[9:43] using the curve view or in this case using vertex curve par which is the same as curve view and
[9:50] remapping that curve view with the ramp I want so I can change the way these deforms as you can see
[9:57] so I can come in here and change the settings then I'm creating a normal enlist several of that
[10:04] normal so if I set this to v at underscore and so the personal normal is just a cross product
[10:11] between the normal which is the tangents and the negative y axis and that would look something
[10:17] like this so let me resize this is just a vector pointing a wave through the x axis let's say
[10:27] with the local x axis of the curve and then I'm doing the double cross product between the normal
[10:32] and that calculator then which will look something like this so pointing out and this way I can
[10:41] deform the curve along this normal so v at p plus equal v at n along this normal by u and I'll also
[10:49] have an amp slider that I can change in here and I can manipulate in here the curve so I say we want
[10:55] something like this so yeah that's basically the tip I wanted to sharing this one
[11:00] and as always you can grab sample files on my patreon and also have access to exclusive tutorials hours and hours of exclusive tutorials
[11:11] and about this project which I should be sharing it some more information soon I hope to release it
[11:18] in the next weeks again thank you for watching and I'll see you next time



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

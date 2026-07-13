---
title: Vex Problem Solving in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=Fiw_NedtssQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/vex-problem-solving-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Vex Problem Solving in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=Fiw_NedtssQ)
**Author:** cgside
**Duration:** 9m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py vex-problem-solving-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript:** Kind: captions Language: en hello everyone and welcome back so in this video I will be showing you two different solutions for some specific problems I faced and hopefully it you will find it useful and apply it to your future projects so let's get into it so I've been working on this IV generator tool it's not really finished or very good right now but hopefully in the future I will get it done but I will today show you how you can approach a specific problem I had so basically I'm scattering some points on the surface some initial points and I have some Target positions to to those points to to reach let's say and I need the points to be constrained to the geometry so for that I'm using a sub solver and the first thought would be to use um a ray project with the mode set to minimum distance so loading the geometry into second input and R projecting the points but as you can see they they will get stuck if I enable the r project they will get stuck around those concave areas so if I show you the geometry again so they will get stuck right here in these areas when doing the the r projection Ray projection so an approach I found was to use instead an SDF a smoothed out SDF so this is the initial geometry converted to VDB and then if I apply a smooth basically a bevel and I save this I output this as an SDF then in the sub solver I can load that SDF in the second input and in this Wrangle I'm basically moving the points where the SDF value is zero so along the surface and if I enable that as you can see the points will the green points which are the initial points that are traveling will not get stuck because we have that big bevel or that big VDB smooth so then you might ask well uh now the point will not respect the initial geometry so these these concave areas and whatnot so what we can do then after doing the trail we can uh do like an explosed view on the points by moving them along the normal and then we add the points and we can Ray project again using the same uh logic but this time using the the original SDF in this case I moved it a bit out so with the dilate that way the The Vines don't don't get inter don't intersect with the geometry so and if we do this with the same stdf projection we end up with the with the vines along the surface and not intersecting and most of and for the most part is respecting the original geometry so yeah that hopefully this was useful to you and let's get into into the second case so now we will get back to a familiar scene if youve been following this channel basically I have a mesh that has been converted from VDB operations and uh it will be difficult to select the Sims and do manual UVS so today I'm going to show you a similar approach when it comes to the orientation of the ovs but uh a different one when it comes to selecting The Sims which might be useful to you so I'm starting with a mesh with no UVS then I'm doing a remesh so we can work with less polygons this way the calculations will be faster and more easy to control then doing a basic R projection just to make sure the the corners are sharp enough and if you remember and if you watch that particular video um we use the shortest P to select the the corner points or the the hard edges but in this case I'm going to use the cluster node based on the normal so if I show you that attribute and disable this gradients you can see that is isolating the different pieces pretty well by using the normals and the way I found this works best is by using setting Computing the normals on the vertices with a cangle of zero and then promoting it to point with the promotion method set to modes you can try other approaches but modes work really well for me then just promoting these to A Primitive primitive attribute and then we can just select the boundary edges as you can see with this group from Atri boundary and we already have the seams for the UV flatten so if you don't care about the orientation this is this will give you already a pretty good result but I want to approach today how to do the UV rotation so the UV orientation in this case to set the the UVS properly so first of all we are creating a mask along the Y so using the relative Point bounding box y components so from 0 to one this way we can clearly uh see which way is up creating a connectivity based on the UVS so which UV Island will get uh a different ID we promote the UVS to a point attribute while splitting them also and then we move this to move the UVS to 3D Space by using at P equals V at UV and we also storing a rest position before that so later we can we can get get the initial mesh back you can see that this gradient this mask along Y is telling us which way is up so the red values so we need to rotate them somehow and for that I'm first going to measure the gradient of that mask based on a piece attribute in this case cluster so I can show you that gradient so it's looking something like this so you can clearly see if I show you also this one so it's pointing in the red Direction so if you watch this one is pointing down that one is pointing sideways and now we just need to calculate the the angle so that's what I'm doing in this Wrangle so we get the gradient Prim attributes so by using the prim num and then we can calculate the angle and this select uh function is like an if statement so if the length of the gradient because if I show you this gradient so in here in these pieces I don't want to rotate them and since the gradient here because they are facing the Y AIS since the gradient here is less than this threshold value in this case I found 0.1 worked well uh I will if if they are not bigger than 0.1 the length of the gradient is not bigger than 0.1 we set the the angle rot the rotation angle to zero otherwise we calculate the angle between the X component and the Y component then we get the UV Island Center and finally we do the qu quion Mets by creating the the quion first so with the the angle to rotates and the axis which will be around the Zed axis then we make sure we rotate from the center so we need to subtract the current UV position by its pivot that's why we Sav this UV Island Center and then we we rotate we rotate them using that quaternion and from that position and finally we just uh multip we just add the rotation and the pivot back so if we check the final results we get the is oriented properly then we can just attribute swap the P for the rest and we get the position back and since the UVS might be overlapping due to the rotation as you can see we can just UV layout them making sure we set to no rotations and the axis alignment to none so it doesn't rotate our Islands then just promote the point the UV attribute to vertices and fuse the point and finally we transfer back the UVS to the original mesh as you can see so going from this one to this one so yeah that's basically what I had for you today hopefully this was useful let me know in the comments and don't forget you can grab the sces on my patreon alongside with hours of exclusive tutorials and I also have some courses in there so yeah make sure to check that out thank you for watching and I'll see you next time f



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

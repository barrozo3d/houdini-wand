---
title: Making Trash in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=KCy4Sw3nbcQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/making-trash-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Making Trash in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=KCy4Sw3nbcQ)
**Author:** cgside
**Duration:** 11m47s | 5 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py making-trash-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So I've been building this environment in
[0:04] Odini for a tutorial and in today's video I wanted to show you how I did this
[0:09] trash assets. So nothing to complicate it but it might have a few tips for you.
[0:16] So let's dive into this trash and as you can see I have this variation so far.


### Trash [0:17]
**Transcript (timestamped):**
[0:25] It's not too much but it's also since I'm building this from scratch it takes a
[0:31] little bit of time to do them. So let's see. Since I had this scan from a
[0:36] previous tutorial I'm reusing it so it's nothing really complicated just a
[0:41] curve with a profile and then revolving and we will do that in the last
[0:45] assets but I'm starting with this one and then I quad-remesh it also. So I'm
[0:50] starting with this base. You can ignore this since I tried first doing this
[0:55] with Vellum then I'm doing the UBs by selecting the seams in here because I have a
[1:00] group of the seams as you can see really simple. You can ignore this then I'm
[1:09] going to do these with RBD to squash the can as you can see. So for that I have
[1:16] the input then I'm scattering 500 points and doing a simple Varunovic
[1:21] fracture. We get something like this. Then I'm pinning part of these constraints
[1:27] since these Varunovic fractures also output the constraints and I'm pinning part
[1:32] of it so the top so I can actually show you how that looks like. So I'm pinning
[1:40] those top points by using the relative point pounding box and I can select
[1:45] more or less this case I just want to top part so it doesn't deform. Then
[1:50] RBD configure I'm not using these bounding box just changing a bit the
[1:56] collision padding in here and a shrink amount. Then I'm converting the
[2:00] constraints to surface points that usually works better. From here I am setting
[2:06] the constraints properties, setting to soft and enable the switch constraints
[2:12] to be glue. So at the end I want to switch them to glue these are my settings
[2:16] you can increase or decrease these and play with it. I don't think plus this
[2:20] is plasticity in here is enabled yeah. So then on the top can I'm setting those to
[2:28] be soft but quite high as you can see the same for the glue and then I'm just
[2:38] simulating these and switching the constraints that frame 18 so we
[2:42] I simulate this and of course I have also a box crashing the acting as the
[2:51] collider and it will look something like this. So as you can see my box is
[2:55] coming down and acting as a collider to crush the the can. So as I told you at
[3:02] frame 18 I'm switching to the ars constraints. Then it's simple as using the
[3:06] RBD deform pieces and I can deform the incoming geometry with the constraints
[3:13] and with the proxy geometry which in this case will be just for geometry. Then
[3:18] just time shift it and this is my can. Match size it to have a real world size
[3:26] and that's my can. Then moving into the back which looks something like this.
[3:34] So this is supposed to be a bag of ships. For that I'm starting with a
[3:39] planner patch. Then planner inflates this is a new logo for the new 20.5.
[3:46] Saving the boundary edges so these edges in here because I'm gonna use it
[3:51] later for UVs. Clipping a bit of the end as you can see. Yoviflaton and I'm using
[4:00] as sims those boundary edges and we have perfect UVs or close to it. Then
[4:07] doing a simple valum cloth and a valum solver in here that will do something
[4:11] like this effect. And inside the valum solver to have this effect I could have
[4:17] used a pop attract but in this case I just used the just manipulator here the
[4:23] velocity by getting the bounding box center creating a vector from the bounding
[4:30] box center minus the P so a vector pointing in and I added also some zero
[4:35] center offset noise in here to the position so I get some sort of random effect
[4:41] as you can see so it's not very uniform. Then just multiplying a bit the
[4:45] velocity so it's not so quick let's say. So that's basically the effect and I
[4:52] valum post process adding some subdivision and also some thickness just
[4:58] than just time shifted and cashed. From there I can just place it on the floor as
[5:05] you can see. So now let's move into the cup we have two versions this one and


### Cup [5:06]
**Transcript (timestamped):**
[5:12] this one. So for this one I'm starting with the tube then I have a sphere which
[5:20] I transform into a VDB and I also smooth it a bit and then the form the geometry
[5:25] with that VDB. So in this case by doing the volume sample and a volume gradient
[5:31] and moving the position along the gradient multiplied by the SDF and we get
[5:38] this sort of effect. So just like a big deformer or something like that. Then I'm
[5:43] grouping in here a center loop just by selecting 12 points out of the
[5:52] these 12 points are also the columns of the tube and I'm selecting that from
[5:58] multiple points and then offsetting by in this case the same amount of columns
[6:03] times three I can increase in here which I can select in here which one I want
[6:07] just by offsetting this one. Then subdividing your Veon rap cylinder which will
[6:12] work fine for this case. Then in here I'm grouping the unchair points and also
[6:19] saving the boundary groups promoting those two edges. Then on the first one I am
[6:24] polyfilling and polybippling as you can see I'm selecting that one of the
[6:28] boundaries for the other boundary I'm converting into a line and sweeping and
[6:32] we get the cup then I transform it down match size it to the correct size in
[6:38] this case something like that. Then for the second version I'm object merging
[6:43] this mesh and then with that range that we selected in here this middle one I'm
[6:50] just soft transforming that in along an axis and playing with the soft radius as
[6:55] you can see. Pending a little bit transforming it to place and match sizing. So
[7:01] that's cup B. So for the container so the container is something like this as
[7:08] you can see and I'm just doing off of it because I'm lazy. So I'm starting with


### Container [7:10]
**Transcript (timestamped):**
[7:14] agreed in set it a little bit transforming that in that the extruded front
[7:20] group polybippling everything to give that rounded look. So actually unshared
[7:27] edges. Poly extruding those unshared edges in a curved way as you can see
[7:32] because I'm coming in here and I'm extruding those unshared and setting in this
[7:38] case the shape to be curved and then I go into spine control and playing with
[7:46] the magnet in here as you can see and with all these parameters. Cleeping
[7:53] in off on both sexes so I can subdivide it better. UV flatten really simple
[8:00] just don't need to give any sort of seams subdividing because right now I'm
[8:09] going to create the noise so I can clip it with clip by attribute that specific
[8:16] noise as you can see. So in here just come and clip it to have some some of
[8:22] dissolves. Poly extruding to have some thickness and also I'm probably reducing
[8:28] because I don't need those many polygons. I just wanted that to to have enough
[8:33] geometry for the enough subdivisions for the noise to work. Match sizing and
[8:38] that's my container. I also have in here an experimental second version which is
[8:45] by merging in the single side geometry then remaching. Scalch it a bit with
[8:52] flattened brush and with the move brush to have this sort of result and
[8:58] subdividing and doing a mesh sharpen to start to have this crumblet look. Then I
[9:05] do another attribute blur set to proximity which is very similar to the
[9:09] mesh sharpen and from there I can I don't want this sort of geometry at the end
[9:16] because it's still broken and cursed so I'm going to remach it. Measure the
[9:22] curvature to get those sharp edges and from here I can create a target mesh
[9:30] size so I can remach it by attribute as you can see it's added to adaptive and
[9:35] in the target mesh size I'm just decreasing the value of those convex areas
[9:41] convex areas yeah and then re-projecting it to the original version. This
[9:47] doesn't too much but then I do a small mesh sharpen and soften normals and
[9:52] calculate the UVs again and then just transform it in place and we get
[9:59] something like this. So not very successful but anyways so the last one is the


### Bottle [10:05]
**Transcript (timestamped):**
[10:06] bottle and here I just started with a curve, resample it, selecting one of the
[10:12] points and this will become Andy in later stage then revolving, fusing, top
[10:21] transform to squash it a bit so I'm just selecting that group as you can see
[10:27] that group that expanded so if I go into points as you can see this group in
[10:32] here expanded to this loop then I'm doing the sub-transform and scaling
[10:39] along the Z I could play with the sub-radios and do a bit more then I'm group
[10:44] expanding so I can promote it to primitives and bless the label that I can
[10:50] pick a little bit merge it and subdivide it and we should have the label in
[10:55] here as you can see maybe I should give it a color. From here just
[11:00] transforming it down and this is the bottle. So a lot of work and we get
[11:05] something like this which in the environment it should when I scatter it
[11:14] around it should look something like this. So let me know if you guys want me to
[11:19] cover this environment on the next video I might part a new series and yeah if
[11:27] you want to grab the files from this video the trash setup you can do so on my
[11:33] patreon alongside with exclusive tutorials hours of exclusive tutorials and
[11:37] all the project files from my videos. Please let me know your thoughts in the
[11:41] comments and other than that thank you for watching and I'll see you next time
[11:45] thank you



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

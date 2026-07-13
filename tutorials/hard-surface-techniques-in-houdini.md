---
title: Hard Surface Techniques in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=qtzO_NoQbtE
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/hard-surface-techniques-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Hard Surface Techniques in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=qtzO_NoQbtE)
**Author:** cgside
**Duration:** 10m22s | 7 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py hard-surface-techniques-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So I decided to model this object in Odini that is by the artist CG gear in art station.
[0:10] As you can see this is the original object. And I decided to model it in Odini to see what the challenges were.
[0:21] And I've got some tips that I want to share with you guys today.


### 3D clip on curved surfaces [0:26]
**Transcript (timestamped):**
[0:27] So for the cloud pads I have these sections in here.
[0:32] And the way I'm doing that is after the basic extruding and beveling I am blasting as a group.
[0:43] And then I'm selecting this in this case you can ignore this range.
[0:49] And what I'm doing in here is creating an image reboot for each 8 primitives.
[0:58] So dividing the primnum by 8. But since I want them aligned in a specific order I am also sorting, so shifting by 4.
[1:09] So I have them in the correct position. So just shift the primitive order.
[1:16] Then in a loop I am creating this setup in here. So for each named primitive I am creating a rest position.
[1:27] Then selecting the bottom and converting it to vertices and doing some UVs with the UV flatten.
[1:38] Then I promote the UVs to points and I assign to the position the UV attribute.
[1:45] So I can have it flat. That way I can use a box clip to clip part of it which wouldn't be really possible with curved surface as you can see.
[1:58] So basically I want to clip the sides and that's what I'm doing in here with this box clip.
[2:07] Then I am again extracting the rest position and sending it back to the original position as you can see it's curved.
[2:17] But now it is clipped.
[2:22] Then just doing a quad remesh and re-project it.
[2:27] So it keeps the same position let's say.
[2:31] Because with the quad remesh it softens a bit the shape.
[2:36] Then I am using a ray to align it better to the original position.
[2:43] So that's basically it.


### Randomizing vellum cloth patterns [2:46]
**Transcript (timestamped):**
[2:48] Now for this slot seam I have identical parts as you can see.
[2:55] So they would end up giving the same exact pattern if I show you in here the version one.
[3:03] As you can see they have almost the same pattern which is not nice and doesn't resemble our reference.
[3:12] So as you can see in this second version they no longer have the same patterns.
[3:19] They are slightly different at least different enough as you can see.
[3:27] And the way I'm doing that is by creating a bend stiffness attribute before the seam.
[3:35] With the noise pattern as you can see just changing the min value to not be zero and the element size.
[3:46] And then in the volume cloth I am assigning to the bend stiffness scaled by attribute and using that attribute in here.
[3:55] And that way I can get a slightly different result on each pad.
[4:04] So for this specific object I am using the exercise quad remeshier.


### Quad remesh control by groups [4:05]
**Transcript (timestamped):**
[4:11] And if I show you an option in here use primitive groups boundaries.
[4:16] If I disable this you can see I will get corners all jacked up.
[4:22] And if I enable it you can see how clean this looks and how useful it can be.
[4:31] Because before that I had basically this result which is not nice for subdividing it.
[4:41] So the way I'm doing those basically this is using all the primitive groups that you have before the quad remeshier.
[4:50] And it will use them to split the quad remeshier let's say.
[4:57] So I have a Boolean and from there I can create a group using the min edge angle.
[5:04] As you can see to select the art edges let's say.
[5:08] Then I'm doing an edge concept of those edges so separating the mesh by edges.
[5:14] Then I can use a connectivity of course and I will have a different class for each of those primitives.
[5:26] Then I can do a group from name and use the class attributes and give it in a prefix.
[5:34] Deleting any groups that are not in those that I set here.
[5:41] Fusing the points and then doing the quad remesh.
[5:46] And as you can see that gives a pretty good result that we can later combine
[5:54] and get something like this.


### Crease corners in Houdini [6:00]
**Transcript (timestamped):**
[6:01] So coming back to the objects I have these art corners in here, these sharp corners.
[6:08] And I would like to subdivid it.
[6:11] And if I subdivided I will get these rounded corners.
[6:18] And because I have these inner extrusion in here, these insets.
[6:25] So the way I'm avoiding that I'm group combining some of the edges, mostly the corner edges.
[6:33] And then I'm doing a crease on that group and increase it quite a bit.
[6:40] Then when I'm subdividing, I won't get that rounded corner look.
[6:48] And also I will get a smooth transition in here because I'm not applying the crease on there.
[6:56] But I am applying in here which is totally fine, it's just on the corner, but not in the center or in this rounded part.
[7:05] So that's how you can do the grising.
[7:09] Because if I overwrite the look, you will start to see, let me change the mat cap.
[7:17] You will start to see the low poly look, let's say.
[7:25] And if I remove it, we will get a smooth look.


### Snap orient with vex [7:31]
**Transcript (timestamped):**
[7:31] Okay, in these particular objects I have created these from curves and doing a bridge between the curves.
[7:44] And then I want to boot you out the middle part so as you can see in here.
[7:52] And the way I'm doing that is of course by using a box.
[7:57] But I need to orient it somehow to this point here in the middle that I manually selected.
[8:03] So the way I'm doing that, as you can see, is by using some Vex.
[8:08] And a script that I shared before, just snippets that I shared before here on the channel.
[8:16] And basically I'm taking the, I have a base-prem in here.
[8:21] So as you can see, this primitive in here that I'm more yending to that specific point.
[8:29] So I'm getting the primitive number of that base-prem and getting the normal.
[8:39] Then from this target point in here, I am extracting also the normals and doing a rotation matrix from the base from this polygon in here to the target point normal.
[9:02] And then just getting the position from this point and orienting the box as you can see.
[9:13] You can get a pretty similar result with copy two points, but you will need to play with the app.
[9:21] And you will need to mess with the rotations of the initial object.
[9:25] Or you can do it also in Vex, but it's just another way to do things.
[9:31] And you get it pretty aligned in the middle, which is also nice.


### Outro and Shop promo [9:37]
**Transcript (timestamped):**
[9:38] Okay guys, that was it. I hope you have found this useful.
[9:43] And as always, you can grab this thin file on my Patreon.
[9:48] And you can also check out my courses page or the shop page on Patreon,
[9:57] where I just released a new course on creating this procedural cookie and the fluid simulation or valence simulation, I should say.
[10:06] And I also have other ones that I released in past, so if you're guys interested, as you can see, they are really cheap.
[10:14] And that's it. Thank you, and I'll see you around.



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

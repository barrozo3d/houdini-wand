---
title: Houdini tips and tricks #2
source: YouTube
url: https://www.youtube.com/watch?v=rVduzdrKYZg
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-tips-and-tricks-2/
frame_count: 0
frame_status: pending-selection
---

# Houdini tips and tricks #2

**Source:** [YouTube](https://www.youtube.com/watch?v=rVduzdrKYZg)
**Author:** cgside
**Duration:** 6m5s | 6 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-tips-and-tricks-2 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. In this video we'll have a look at 5 different
[0:05] tips in Odini that I believe are interesting to know. So let's start on how to


### Spherical hdri projections in Houdini [0:09]
**Transcript (timestamped):**
[0:10] project a spherical hdr ion onto geometry in case you want to do some
[0:17] spatial lighting. As you can see I have this hdr I projected into a simple
[0:23] geometry and for the material I am using the material X and LITS with the image
[0:28] connected to the emission color. So the idea here is to start with simple shapes
[0:35] like a grid and adjust your projection to fit the floor then you can start to
[0:41] extrude the walls and create other shapes. In the UV project set the type to
[0:47] polar which is a spherical projection. Then looking at your image you can
[0:52] transform the projection accordingly with the translate and rotations
[0:56] gizmos. And I am adding some simple assets and a shadow catcher at the end. In
[1:04] this case I will recreate the lighting so it makes sense to make the set geometry
[1:08] invisible in the final render but still contributing to the lighting. You do that
[1:13] with the render geometry settings and under render visibility set it to
[1:20] invisible to primary rays. Adding the lights and a camera then you want to
[1:28] preview your backplate in the render for that use a background plate node and
[1:33] your shadow catcher object and the image. And in the end you'll have your
[1:40] objects added to the backplate. This is a very simple setup but should give you an
[1:45] idea of the workflow. So the second tip is about track planer projections. As you


### Fixing triplanar projections on multiple geometries [1:48]
**Transcript (timestamped):**
[1:53] might know in order to change the dialing we need a position node with a
[1:57] multiply. As for the offset you can use an add node. And as you can see by the
[2:04] fault we have quite a repetitive pattern along the seats. The first thing we
[2:10] can do to avoid repetition is to set the position node space to world but
[2:15] still we have repetition. So what we can do is use the add node to introduce
[2:22] some random offset and that's what I'm doing with this attribute. Each seat
[2:28] will have a different offset in the x, y and z position for the track planer
[2:33] projection. And you probably know how I have created that attribute just with a
[2:41] netribute randomized. Don't forget to pack your geometry if you have multiple
[2:47] meshes so it creates a point for each object. In this one I am just sharing


### Camera match in Houdini with fspy cam loader [2:51]
**Transcript (timestamped):**
[2:52] someone else's work that created an awesome HD8 to import FSPY files into
[2:58] Odini. Basically you will line your imagine FSPY and save it as a JSON file.
[3:04] In Odini you will add the FSPY Camloader HTA, add the JSON and image file and
[3:12] finally just read file and create camera. It can also do camera projections.
[3:18] Having the camera and image in place you can start to do your image based
[3:22] modeling. I live a link in the description. It's totally free. So this one is


### Random rotations with vex [3:27]
**Transcript (timestamped):**
[3:29] actually an update to what I have shared already on the channel. It's about
[3:34] random rotations and how to have control over the orient attributes when
[3:39] scattering geometry. I have a box that I want to scatter in this terrain but
[3:44] would like to give it some random rotation where I can control the angles and
[3:50] possibly orient them along the normal. So between the scatter and the
[3:55] copy to points I have this wrangle. As you can see I can control the rotation
[4:00] mean and max for all axis. Ever see value if I don't like the results? I can
[4:06] also orient the instances along the normal of the terrain without losing the
[4:11] initial rotation and finally offset the geo from the terrain in case we have
[4:17] floating instances. The code is quite basic as I'm still learning Vex but works
[4:24] pretty well. Basically we are creating a vector from the random rotations
[4:29] along with some UI channels for the mean and max rotation. At the beginning I
[4:36] have a channel to control the surface orient. Then in the statement if it's
[4:42] checked I can use this function to set the orient attributes. In a new variable I am using the
[4:49] alert to quarter nune's function to convert the values in degrees. And finally we can
[4:56] multiply the existing orient attributes with the new one. At the end I just
[5:01] have an offset along the y axis or the normal.
[5:05] So let's say you want to add some color or gain variation to leaf symmetry but the geometry


### Color variation on merged geometry [5:07]
**Transcript (timestamped):**
[5:14] is merged. First you need to isolate the target geometry and create a connectivity node.
[5:20] Then in a wrangle you can create a attribute between 0 and 1 giving the class attribute from
[5:27] the connectivity as the seed. Pretty simple but works well I have done the same thing for the
[5:35] leaves. And in salaries I am controlling the gain of the leaves with the attribute connected to a ramp.
[5:45] Using it also for the fruits but this time to set the base color. So yeah hopefully you got
[5:52] something out of this and don't forget to check my patreon where I share project files and
[5:57] exclusive tutorials and tools. Thank you for watching and see you in the next one.



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

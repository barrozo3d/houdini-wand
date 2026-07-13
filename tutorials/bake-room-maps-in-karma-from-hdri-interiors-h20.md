---
title: Bake room maps in karma from HDRI interiors H20
source: YouTube
url: https://www.youtube.com/watch?v=6hbyMIxU1oI
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/bake-room-maps-in-karma-from-hdri-interiors-h20/
frame_count: 0
frame_status: pending-selection
---

# Bake room maps in karma from HDRI interiors H20

**Source:** [YouTube](https://www.youtube.com/watch?v=6hbyMIxU1oI)
**Author:** cgside
**Duration:** 5m47s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py bake-room-maps-in-karma-from-hdri-interiors-h20 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm gonna show you how you can
[0:04] take an interior like this and interior scene you can have geometry in here
[0:10] but in this case I'm just projecting an HDR interior to the geometry and then I
[0:20] can bake it to a texture to a cube map let's say or an interior map and then
[0:35] we can apply it to some geometry and we would get something like this this
[0:43] parallax effect. So let's see how it's done. I'm starting with a subcreate
[0:52] creating a box and we will need to subdivide it otherwise we will get this
[1:02] distorted projection as you can see. So place a sub divide in violinier mode in
[1:11] this case is a very simple interior but you can elaborate more. Then I'm
[1:17] reversing the normal so I can see the interior by taking remove back faces.
[1:25] Then I am your view projecting and at the same time using a quickshade with my
[1:33] HDR so I can see the result and I can manipulate the rotation and play also
[1:46] with the box scale to see where it fits better as you can see. It's really easy
[1:55] to do this kind of image-based modeling and I have an output in here called Geo and
[2:09] from there I'm creating a material library with an unlead surface and just a
[2:15] material like the image loading my HDR and this step is really important
[2:22] otherwise you will get a lot of grain in your final image. So then I'm creating
[2:30] a camera and setting the view is just default 000 to position and in the view I'm
[2:38] setting the aspect ratio to 1 to 1 since I want to render a square texture and
[2:44] in the karma tab I'm using a lens shader that you need to create inside a
[2:50] matte network, a material network as you can see in here. So then in the
[2:57] caramel room lens shader in the different variables here the X-min, Y-min, Z-max,
[3:07] I'm inputting the bounding box and the corresponding bound so the X-min, the X-max
[3:17] and so on and also adding a very small value of offset you will need to play
[3:24] around to see where it lands the perfect result because sometimes you get some
[3:33] noise and you also need to increase a bit the samples to get rid of some of
[3:39] that noise. So then if you render you will have a perfect or near perfect room map.
[3:52] And finally you can create a plane and attach the room map frame just default
[4:01] settings create a material and attach the room map that we rendered and the
[4:11] corresponding attributes, room beat, engine view, engine view and that's about
[4:20] it you have your room map working as you can see. We have the ceiling and the walls,
[4:32] the floor. In this case I didn't use a square grid to render to a geometry to
[4:46] render this effect because otherwise I would get stretching so what I did was
[4:55] in the sub-create on the grid I loaded as a spare input my geometry my original
[5:01] geometry where I projected the HDRI and used the bounding box size Z-x and Y so it
[5:10] creates a similar ratio to the original geometry but you don't need to do that
[5:19] because I was getting some stretching in some areas and this is better this way
[5:27] but you can totally make it square and from distance this looks pretty convincing.
[5:36] So yeah you can grab the file on my Patreon and thank you everyone that joins
[5:43] so far and I will see you soon thank you.



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

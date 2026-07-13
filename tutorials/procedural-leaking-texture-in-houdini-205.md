---
title: Procedural Leaking Texture in Houdini 20.5
source: YouTube
url: https://www.youtube.com/watch?v=8iK3GD3yeCE
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-leaking-texture-in-houdini-205/
frame_count: 0
frame_status: pending-selection
---

# Procedural Leaking Texture in Houdini 20.5

**Source:** [YouTube](https://www.youtube.com/watch?v=8iK3GD3yeCE)
**Author:** cgside
**Duration:** 10m11s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-leaking-texture-in-houdini-205 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'll be showing you how I created
[0:06] this procedural leak mask. I have done this previously by using a simulation but
[0:13] this time I will be showing you how to do it with Cops and some simple
[0:20] Vax. So yeah let's get started. So I will be showing you the workflow in some
[0:28] simple geometry so it's easier to follow along. So basically I'm starting with
[0:35] the box, did some extrusion, to create some windows and this inner extrusion.
[0:42] Added some normals in this case point normals and subdivided the mesh because
[0:49] the next thing we're going to do is to measure the curvature and for that we
[0:54] need some resolution unfortunately because we don't have these nodes at
[1:01] shading level. So now we have the convexity and also the concave areas which
[1:12] will help us to create the leak mask. So or the leak origin let's say where it
[1:21] should streak down. So basically we won't leak on these areas here, here at the
[1:30] bottom of the windows and also here and on the top. And for that we need to do
[1:37] some mixing of attributes and we have almost everything we need. Now we just
[1:43] need two directional masks. In this case using the dot product between the
[1:50] normal and an up vector in this case the Y. So here's the first one so all the
[1:59] faces, all the frames facing up and we have a second one which all the
[2:06] frames facing down. And from here we just mix both the both directional masks
[2:16] with the convexity and with the concavity. And in the end we end up with this
[2:22] mask. So I'm not an expert on this but this looks like where the legs should
[2:29] start at least in a conceptual way but I'm open to suggestions. So next we create
[2:43] some normals on the vertices and create a p-scale attribute. It's like a
[2:50] natural bit randomized for each of the points that we will scatter on these
[2:56] areas. So we have bigger and smaller legs but we will see that in a bit. Then
[3:04] I'm creating also two masks on at the vertices level because I want them to be
[3:12] super sharp as you can see. So this one at the bottom, using again the dot
[3:17] product is the same workflow and one at the top. As you can see they are super
[3:24] sharp because they are on the vertices. Then I'm unwrapping. So let me just get rid
[3:33] of this. I'm just creating a UV unwrap and these are my UVs. And you notice
[3:43] that all the UVs are super well aligned and this will not create some
[3:54] possible issues. If we feed other type of geometry where we have UVs facing
[4:01] sideways and upside down and so on. So basically we need a natural boot that
[4:07] tells us which way is down. So where the legs should streak down. So for that
[4:15] just to simulate that problem, that problem of the UVs facing other
[4:21] directions, I'm selecting your set of primes, assigning a new color and
[4:29] transforming it, rotating it upside down as you can see. And now we will create
[4:42] a natural boot, a mask that goes from top to bottom. So a gradient as you can see
[4:51] in this by using the relative point bounding box. If I remove this as you can
[4:58] see this is from 0 to 1. And now we need to transform this to UV space. So I'm
[5:09] splitting the UV seams and promoting to a point attribute the UVs and placing them
[5:18] assigning the UV to the position. And we can just remove the visualization. And as
[5:26] you can see this face right here if I showed the attribute again. As you can see
[5:34] is not from white to black as it should be. As you can see this is the front
[5:43] space. This one is slightly darker to white so it's upside down. And the idea
[5:51] here suggested by Swalsh on the CGWiki Discord which I am very grateful is to
[5:59] measure that the gradient of that mask that we created. And if I show you that
[6:09] so mask white and we have here the gradient white. And as you can see this
[6:18] particular face the vector is pointing down because we rotated it. So if I
[6:28] remove this UV transform you can see what is doing. And this is what we want to
[6:35] orient our streaks which we will do next. So the idea now is to scatter some
[6:42] points on that mask that we created with the convexity and directional masks.
[6:51] And we create the attributes in this case the normal since we want to orient
[6:58] the the streaks. In this case I am using the gradient white and setting the
[7:05] up along the z and moving into cops. We can start by importing the points and
[7:15] resturizing the setup so we can move it from negative one to one which is the
[7:22] space that the cops operates. And creating an SDF shape let me resize this. In
[7:31] this case I am just using a line and creating this streak. And converting it
[7:38] to mono, transforming it a bit. And I am just stamping the points. And as you can
[7:44] see that particular tile if you remember it's upside down and the leaks are
[7:51] facing this direction, the up direction. And that's because we have that
[7:58] normal attributes that we just created in here. With that gradient we measured.
[8:08] So this is basically done. Now we just use those masks if you remember that we
[8:16] created the vertex two vertex masks with the top and bottom faces our frames. We
[8:24] maximise the two attributes in words and multiply over those areas as you can
[8:32] see is removing some streaks we don't want. Then we can for instance use the
[8:41] streaks blur, streaks blur, invert it in this case and just preview it. And here we
[8:49] have the final result which is the streaks. And they are obviously two uniform and as
[8:59] you can see this is very simplified. You could load the map and randomize it, add
[9:10] some color, you name it. So yeah that's basically it. That's the same I have
[9:17] done in this particular setup if I can show you as you can see this is the same.
[9:27] But for other set of geometry as you can see we have the windows and it's
[9:35] streaking down and also on the top areas. So where I think it makes sense but I
[9:44] might be wrong with the formula so feel free to correct me in the comments. And
[9:51] that's basically it. You will be able to find this particular setup in my Patreon
[10:00] on my Patreon so feel free to grab it there and other than that thank you for watching
[10:07] and I'll see you next time.



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

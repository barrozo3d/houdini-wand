---
title: Environment Creation with Houdini - Part 1
source: YouTube
url: https://www.youtube.com/watch?v=nGKGXKw4_Zw
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/environment-creation-with-houdini---part-1/
frame_count: 0
frame_status: pending-selection
---

# Environment Creation with Houdini - Part 1

**Source:** [YouTube](https://www.youtube.com/watch?v=nGKGXKw4_Zw)
**Author:** cgside
**Duration:** 11m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py environment-creation-with-houdini---part-1 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey there and welcome back. So in this video we're going to create the basis for the image you see
[0:06] creating the terrain and do some initial scattering. It will be a good opportunity to learn not any basics
[0:14] from for loops to height fields and also some simple wax.
[0:21] Let's start by creating a night field changing the dimensions
[0:27] and apply some initial noise.
[0:33] Blaring a bit the result as we don't need detail for this part.
[0:38] We need to somehow divide the terrain, the back hills and the fields in front.
[0:44] So I'm creating a line positioning in the center
[0:48] and also copy the width of the height field and add a small value to it.
[1:00] I also want the back hills to be around 40% of the entire terrain so let's copy the depth of the
[1:07] height field and position the line 10% from the center. Adding a point cheater to proceed
[1:14] really shape the line and only displacing along the Z axis.
[1:23] When you're happy with the shape add a re-sample mostly to smooth out the curve with the subdivision curves option.
[1:35] Now let's create a mesh from this curve by doing a few explosions and mirroring the results at the end.
[1:42] We will use these to mask the height field but also to cut the geometry later.
[1:51] Load the mesh we just created in an object merge and do a mask by object.
[1:58] Now we have a mask to separate the different sections of the terrain.
[2:03] Add a night field noise and play it with the attributes we want to create some small mountains in the back.
[2:12] You will also need to blur the mask with the transition.
[2:23] After blurring a bit the result we can start to play with some erosion.
[2:28] I am not changing much only the overall amount.
[2:36] I also want to distort a bit the result with a low frequency.
[2:41] Here I am just going back as I am not yet happy with the result mostly changing the seat of the offset of the noise.
[2:58] Let's now create a path on our terrain by using a more traditional way drawing a curve.
[3:04] Re-sample the curve to smooth out the points.
[3:12] And let's project it on our terrain with a ray and create a mesh with a sweep.
[3:22] Now we can create a mask from the path.
[3:25] Having the mask we can carve the road on the terrain by using a night field project.
[3:35] We will need a negative transform in the way to carve the path and also play with the combined methods of the projection.
[3:46] Let's save this mask to a layer using the copy layer node.
[3:51] We will also need a mask for the sides of the road to scatter some trees around.
[3:57] So let's expand the road mask and subtract the original mask from it.
[4:07] We need also to save it to a new layer to use later.
[4:13] As the transition is a bit harsh between the road and the terrain let's manipulate a bit the
[4:18] mask's two-blur that transition.
[4:29] And finally we can cover the eye field to a mesh.
[4:46] Let's move on by creating a bullion between the back shape and the terrain.
[4:59] In the next step we will use a Voronoi fracture to divide the front part into fields.
[5:05] So start by scattering a few points for the fracture.
[5:09] We want to disable creating the rear surfaces in the Voronoi and now we have the base for our fields.
[5:24] Around the different patches I want to scatter some bushes so let's group the unshared edges and convert them into curves.
[5:32] We will need to fuse the points and then create a mesh from it.
[5:42] But as you can see we have double geometry so let's go back and fuse the unshared edges group we created.
[5:55] Okay now I want to mask this sweep mesh on the terrain but let's make sure we
[6:01] re-project the mesh as by now it's flat.
[6:07] Alright moving to the last part of this long tutorial I want to divide the pieces from the Voronoi into
[6:14] different groups so I can scatter different meshes later. Let's pack the geometry with the
[6:21] assemble nodes. Now we will need a bit of wax to create a random index of the packed frames.
[6:28] Carty of Leninmost Prime user on reddit. Basically we're creating a natu-boot with some controls
[6:36] for the number of groups we want and also the seed value. Let's group by attribute to visualize what we've done.
[6:52] Now we can use a name to transform the groups into an attribute.
[6:56] I'm realizing now that maybe I don't need these much steps but it was the way that it was working for me.
[7:04] Let me know in the comments how would you have done it. Promoting the point attribute to primitive
[7:11] so we can use it in the next step. Now we will use a for loop to scatter different meshes into
[7:18] the tree groups of fields we created before. We want to change the method to extract this
[7:25] our points. Make sure you set the name attribute in the loop and node, piece attribute.
[7:35] I made a small mistake before the loop but we will fix it in a bit. For now let's unpack the
[7:42] geometry and combine the road masks so we can feed it to the density attribute on the scatter.
[7:49] We will also need a metadata node to use it the iteration or index of the loop.
[7:56] And before correcting the small mistake I made let's invert the mask as we want to scatter outside
[8:03] the road. The missing part here is in the name attribute. We need to set the class to point and
[8:12] not primitives. Let's create the tree scatters for the tree groups we have and use the mask we
[8:23] just combined as density. Now we need a way to select the different scatter node at each iteration.
[8:31] So using a switch node feeding it the iteration attribute should do the trick.
[8:37] And we can use a copy to points and place different objects at each group of patches.
[8:46] Let's reuse this switch node and place a few different colorate boxes for now.
[8:51] Finally let's combine the result with the original terrain and we are done with the fields.
[9:08] The only thing left to do is to scatter some bushes around the patches and trees on the roadside.
[9:16] So let's start with the curves we had before and split it with a polypads. I am doing this
[9:23] because I want to remove some of the back lines. Creating a shape from it and scattering a few points
[9:31] making sure we remove the ones on the roads.
[9:34] Lastly, with a copy to point we can insert a few boxes for now.
[9:49] The only thing left to do is to distribute some trees on the sides of the road.
[10:04] Create a cylinder and place it on the grid with the H-Gripped code Y-min.
[10:10] Scatter a few points on the roadside and use a copy to point to instance the tube.
[10:24] Let's just make the trees face up by setting the normal attribute.
[10:30] And the very last step is to rotate the tube so it sits up.
[10:35] And that's everything I wanted to share with you for now. Hopefully you learned something new.
[10:42] I certainly did doing this small project. And the next step is to take everything we've done
[10:48] to Salaris context and do some shading, lighting and rendering. Let me know if you would be
[10:55] interested in that. Thank you and see you in the next one.



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

---
title: Art directing large scale RBD sims in Houdini using the up-res method
source: YouTube
url: https://www.youtube.com/watch?v=M6E3f3yY824
author: the point and prim
ingested: 2026-07-16
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method/
frame_count: 0
frame_status: pending-selection
---

# Art directing large scale RBD sims in Houdini using the up-res method

**Source:** [YouTube](https://www.youtube.com/watch?v=M6E3f3yY824)
**Author:** the point and prim
**Duration:** 11m49s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py art-directing-large-scale-rbd-sims-in-houdini-using-the-up-res-method <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. In my last video I talked about doing some R&D into
[0:11] RBD uprising and that is exactly what we're going to talk about today. If you are unfamiliar
[0:16] with what uprising is it is the concept of working with a horrifically low polysim like
[0:21] this one which is very fast to iterate and therefore control. The low res sim is then
[0:25] used to guide a high res sim to achieve a predictable high res result. This is not a golden
[0:31] bullet which reduces the final sim time of the high res but is intended to maximize your
[0:35] valuable hours as an artist. This project file is quite large so we won't have time
[0:39] to cover all of it within the constraints of this video. Instead we'll be focusing on
[0:44] the core concepts. These are the base fracture, the guide sim, secondary fracture and most
[0:52] importantly the upper system. I will also be covering the rendering setup in Solaris
[0:57] and Karma CPU, touching on topics such as subsets, efficient authoring of USD for heavier effects
[1:02] like this and some shading and render setting notes. There isn't anything too complicated
[1:07] going on in that department but enough useful information to help you tie a shot like
[1:11] this together yourself. We are about to go through the core techniques of how to get
[1:15] this effect up and running but if you would still like to learn more or look at the other
[1:18] setups inside the hip file that we don't have time to cover in this video the project
[1:21] file is available on Gumroad, link below. In a stand and workflow you would typically
[1:28] sim at the required resolution evaluate the result and iterate. After all these sims
[1:32] we still might not have the desired result. This quickly gets frustrating as the feedback
[1:36] loop takes around 42 minutes ago in this theoretical example. On top of this our feedback
[1:41] loop is limited by how fast, hour or our studio's hardware can compute the data which
[1:46] can be very slow at production quality. The upper is approach instead focuses spending
[1:51] the bulk of our time iterating and then submitting a high-risk sim with a lot more confidence
[1:55] that the movement will match what we desire. So if you've done RBD before you will be familiar
[2:03] with the commonly promoted workflow of simulating the proxy geometry and then transforming
[2:06] the high-risk fracture pieces using the orientation and translation of the proxy points.
[2:11] You will be used to working with high-risk chunks that look like this. In the upper is method
[2:14] we will then fracture the high-risk pieces a second time and then reapply the transform
[2:18] from the proxy points. This is where things start getting trickier. The twice-fractured
[2:22] chunks will then be simulated again and we will need to manipulate the active and animated
[2:26] attribute so that the pieces at the edges of our chunks gradually get activated as the
[2:30] sim progresses. The terrain is just a grid displaced for the texture map from Gaia. You
[2:37] can of course just use who do any height fields if you want. I call out everything outside
[2:41] of camera frostum so I can maximize the resolution in camera. I use the rest noise rest technique
[2:47] and Vorono fracture this planar geometry, doing the extrusion after it to avoid who
[2:51] Danny cooking a 3D fracture. These chunks then go into a for loop where I remesh the inside
[3:00] group and add some noise displacement. I lurp the points of the outside back onto the
[3:04] original position so I don't modify the terrain surface. I generate a mask with the same
[3:08] outside group and blur it a tiny bit. Then use a lurp once again to a slightly smaller
[3:12] version of the chunk to get this tapered look. This fracturing method allows us to get
[3:16] nice displaced edges and inside faces as well as a nice overhanging edge that will work
[3:20] nicely later when we will eat into it with the upper assimilation. Now that we have our
[3:27] base fracture we can set up the proxy sim. First we need to create the proxy geometry of
[3:32] the pieces. I do this by looping over the pieces, shrink wrapping them and retrieving
[3:36] their name attribute from the incoming iteration of the loop. You can also use the convex
[3:42] decomposition node to do this but I found I was getting better performance by manually
[3:46] building the loop. After this I am using an assemble to pack the pieces and then deleting
[3:50] the pack prims with an ad node in a separate stream so I can work with the points for building
[3:55] the activation and velocity impulse. If we swap to top orthographic and enable this
[3:59] mask attribute we can see what is being used to drive the impulse. This is done using
[4:04] the simple wrangle. We can use the rail bee box function to get the relative bounding
[4:07] box of this geometry using its x component inside a smooth function. By animating the
[4:12] first value in the smooth and adding a tiny amount to the second we can create a really
[4:15] tight, animatable mask. If that made no sense to you then this might. Anything below
[4:21] range bottom returns a zero and anything above range top returns a one. Anything in
[4:25] between is a smooth interpolation from zero to one. If we shift the values around it
[4:29] squeezes all the loose ends of the values meaning if range top is equal to range bottom
[4:33] plus something really small we will get a super tight, basically non-existent easing
[4:37] between the two values. Next I time shift this animation back one frame and compare
[4:41] its mask attribute to the current frame, allowing me to isolate and group whatever has
[4:44] just gained the mask attribute. I use this group to add some velocity onto those points
[4:48] only while I use the masks to set the active attribute from zero to one. You may notice
[4:53] I have these border points around the edge that aren't being affected by the mask and
[4:56] that is because I use the border of the terrain geo to group those points by distance and deactivate
[5:00] them. After this you simply copy your attributes back over to your pack prims. You can use an
[5:05] add node again to validate if they copied correctly. Inside dops you'll need a simple pop
[5:10] wrangle to update the attributes each frame. Just remember you want to set active and add
[5:13] to v. That is it for the proxy sim. I won't spend more time in it as you will want to
[5:17] build your shot differently. Just remember you are going to spend the bulk of your time
[5:20] on the proxy sim in this workflow so it's worth investing extra time into making this
[5:23] part of your node graph easy to use. So now we've catch the proxy sim out as points
[5:29] and it is working as intended transforming the high res pieces. In order to set up the
[5:33] up res we need to fracture the geometry a second time but when we run our second sim we
[5:37] will need a name attribute for those pieces to behave independently. Yet we still need
[5:41] to retrieve the transforms of our proxy sim. This essentially means we need two name
[5:44] attributes. We can do this by renaming the name attribute of the proxy sim to something
[5:48] else on both the pieces and the points. I use x form name but it can be whatever you
[5:53] want as long as they both match up. Now that all the weird name attribute stuff is
[5:58] out of the way I use a connectivity node to generate this chunk attribute which will
[6:01] be essential later so don't forget it. The up res fracture itself is very simple. It
[6:05] is just the rest noise rest technique again using points scattered on the outside group
[6:09] which then pipe into another varanoi. This time I didn't find a way around it. This
[6:12] fracture can get pretty slow depending on your incoming geometry. Let it cook and go
[6:16] to get yourself a couple of coffee. After the up res fracture is complete make sure
[6:20] to validate it by checking it with the proxy points again to make sure the new pieces
[6:23] transform correctly with the new name attribute. In order to simulate this we want to create
[6:26] proxy geo again so we can just repeat the same shrink wrap loop trick. This time we retrieve
[6:31] name x form name and chunk. Cache that out and check your attributes are working as intended.
[6:41] Buckle up because this is going to be theory heavy. First we need to set ID for these pieces
[6:45] as we will need this in a second. This wrangle is the cornerstone of the entire system.
[6:49] Let's have a look at it. So the idea behind the up res is that we calculate the distance
[6:52] between points of neighboring chunks and if that passes a certain threshold we will activate
[6:56] those pieces else it will just follow the proxy sim animation. That means we need to find
[7:00] a way to measure the distance between pair IDs dynamically. If we grab a bunch of these
[7:03] pieces and move them over here we can see the border pieces accumulate and attribute.
[7:09] So we have three beautiful chunks, 0, 1 and 2. We read this in at the top of the wrangle.
[7:13] We have the secondary fracture so our pieces actually look like this. We will operate
[7:16] on just one piece for demonstration purpose. We use the near point function to open a point
[7:19] cloud. Find all nearby points within a certain distance and store them in an array. Next
[7:24] we will loop through all items in the array. Remember we want to find a pair ID on the
[7:27] neighbor chunk, not an current one. We can do this by checking what chunk attribute
[7:31] the array point returns. If it is the same as our current point we continue the loop.
[7:35] As soon as it finds a point on a different chunk it registers that point as a pair ID
[7:38] and breaks a loop, discarding the rest of the items in the array. This means 0.8 and 0.36
[7:43] and our pair together. This will of course repeat over all of the points in the geometry
[7:46] so that all of them will pair up. This doesn't account for unique pairs only as I didn't
[7:50] find it necessary for this shot but you can program in that behavior if needed. Now we
[7:55] can just read the position of the pair ID and compare that to the current position and
[7:58] write that out as an attribute. This will measure the separation between the two. I use
[8:02] a time shift on frame 1 and then create a group based on the pair distance to hard set
[8:05] which points will be allowed to activate as I don't want to eat too far into the chunk.
[8:09] So far our pair distance has values greater than 0 at frame 1 which makes it annoying to
[8:13] control. I normalize this by subtracting the current pair distance by the time shifted
[8:16] pair distance. If we visualize this now we can see the value start on 0 and then increase
[8:20] as the pieces move away from each other. I use the exact same time shift trick from the
[8:24] proxy sim except I compare length and velocity this time. I will create an integer attribute
[8:28] which I use to force some pieces to become active on the first frame for better impact.
[8:32] Now that we have all this we can pipe it into a solver which will dynamically control
[8:36] the active attribute. We are reading the current distance and setting a threshold. We want
[8:42] to compare the distance to the threshold and if it's greater or less than that value
[8:46] accumulate an attribute which is controlled by this rate parameter multiplied by some random
[8:49] resistance. Once that accumulated value goes past a certain point we simply set the
[8:53] active attribute to 1 and the animated attribute to 0. Prior to this all pieces were set
[8:58] to only animate meaning they followed the movement of the proxy sim and that's it for
[9:02] the core elements needed for this system. In Dops we just read the active and animated
[9:06] attribute like we did with the proxy. Over in stage we start by sub importing the
[9:18] RBD pieces we will want to set the layer save path. It's important to do this as it will
[9:22] speed up the RBD procedural later. We also want to scroll down to the bottom of the import
[9:26] data tab and enable subset groups. This will convert our inside and outside group from
[9:30] the fracture into subsets for separate material assignments.
[9:33] Next up we use the RBD procedural lock to correctly set up our RBD simulation for USD. We
[9:37] point to the prime here and read the points directly from disk. As pointed out by her
[9:42] and Yanno this is a lot more optimised when dealing with large amounts of data. We
[9:45] can also check that our subsets are working by making a couple of flat shaders and applying
[9:49] them to test them out. Finally we want to cache this to disk so we can sublay her
[9:52] it back in later. Thank you lazy cinephile for this tip. I do need to mention there is
[9:57] a bit of fiddling around to get the RBD procedural lock to work. I created an entire video dedicated
[10:01] to this so if it gives you any grief make sure to check it out. Link below. We didn't
[10:05] cover the debris simulation in this video but I instanced my prims directly on other
[10:09] points from sops and then cache them out as well as importing the terrain and converting
[10:12] it to USD.
[10:16] Now we can read all our layers back in. We can use the Houdini Preview Procedural node
[10:19] to visualise the procedural. If you leave it off the RBD's won't move in the viewport
[10:23] but it is great for performance. On the right we've got our lights and materials which
[10:27] we graphed into our geometry branch. Shader wise I am mixing the colour map from Gaia
[10:35] with a little bit of noise. I use a different noise to randomly rotate the UV's which
[10:41] I plug into a texture for displacement which I've got disabled in the IPR for speed.
[10:46] I've got a second material for the inside subset which is just using the rest attribute as
[10:54] a position input for a triplanar texture. Nothing crazy here. There are very basic
[10:57] separate shaders for the dust and debris but we won't be covering those now. The last tips
[11:02] I've got for this are that I like to use a render geometry settings node to dial down the
[11:05] Dicing a bit as the default setting is sometimes too brutal for my home machine to handle.
[11:09] You can completely disable it by setting it to zero which is great when you're setting up
[11:13] shaders. Lastly I always use an LBE tag node and standard render vise to split my lights
[11:18] up into separate passes for comp. And that's it for now. I hope there is enough information
[11:23] in this video to start implementing RBD UPRESS techniques yourself. There are several other
[11:28] elements in this project file that I didn't have time to cover here. If you are still curious
[11:32] about this or would like to take a deeper look at these techniques the hip file is available
[11:36] on Gumroad. Link in the description. Thanks so much for watching and see you in the next one.



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

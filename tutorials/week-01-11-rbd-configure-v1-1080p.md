---
title: week 01   11   rbd configure v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=dIBS14jw25k
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/week-01-11-rbd-configure-v1-1080p/
frame_count: 4
---

# week 01   11   rbd configure v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=dIBS14jw25k)
**Author:** The VFX School Archive
**Duration:** 10m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Right, let's drop in RBD configure. So this will pack and prepare all of the geometry for the simulation. I'll click to just tidy this up a bit. Like that. Okay, let's visualize that. Now straight away what I'm going to do, just drop a delete node. Just do isolate one of these pieces. If I just come in here and grab one of these, so just grab that delete that's actually two delete nodes there and delete non-selected. So we're just isolating that and then drop a RBD bullet solver again here. The reason I'm doing this is just what I want to see the collision geometry. It's always a good idea to look at your collision geometry by default. You don't see it. So you've got to turn it on, come into the visualized tab and show geometry representation. Then we can see it's quite a lot bigger than our actual geometry. That's controlled by either got it here, solver, your collision padding. Okay, so if I put that to zero, you can see there's nothing there. Put that back to default. Or you can do it here, which is what I'm going to do. Go into collision shapes. You can change the collision geometry representation. You can use a box which is really fast or a sphere, which is I think the best. Obviously, this has no relation to the shape of our piece. So I'm going to stick to convex hull, but bring down the collision padding considerably. I'm going to bring this down to point one, I think. Okay. So it's still a little bit there, almost imperceptible, but it's better than nothing. It's important I find to, if I'm visualizing lots and lots of pieces and trying to see the geometry representation, I find who do any, who do any crashes. So just isolate one piece and then configure it to that. And I'm going to turn this off. Just get rid of them and now actually another thing we're going to do is play around this active attribute. So anything which is active is can be affected by forces and other active objects. They can move around and be actually simulated. If they're inactive, they'll just be static, they'll stay in place or they will be animated if there is animation on there, which we will have. So for this active attribute, we're going to use bounds, which is like a group or this bounding geometry. So we're going to plug something in here. So the middle will be, we'll make a group here, which will grow out towards the edges over time. Right? So for that geometry, maybe can we visualize the active group? Didn't like that for some reason? Let's see, can we make a visualizer with this? No, I don't know why that's not showing up. Let me drop a no here. And maybe we could do it there. Let's see, we should have an active attribute there. Click on that. Where's that working? Tell you what, easy way to do it, delete. And add active. Zero. Okay, did selected, delete. Oh, set this to points. Non-selected, okay. So if I just drop a box in here now, plug it into there. If this box is way bigger like that, you can see what it's selecting becomes active now, okay? Because anything in the box is active. Anything out to the box is not active, right? So all of these pieces now will have an active attribute of one. There, okay. So back to the scene view, and let's make a more interesting shape with this box. Okay, I'm going to template that, view the box. And let's bring it back down to one here and then I'm going to make it five by five. And just move it over a bit. And I'm actually going to make the size and X to be zero. So if it starts off with nothing being selected in, you know, nothing in the group. Okay. And I'm going to set this to polygon mesh that way. I've got some divisions. And because I want to add some noise to these faces, just do this to 100. That should be enough for us. So let's drop a mountain on this. Okay. And you can see we've got negative values there. That's why it's going inside out. So turn off center noise. That means it will be added on top of the current position. So it's just move it, you know, along the normals in the positive, only into positive values. Okay. Let's give it a bigger element size. So each piece is bigger. I'm going to change the noise to flow and get rid of the roughness. So I don't want any roughness there. And I'm going to animate the height. Okay. So at the beginning, the height is zero. Again, selecting nothing on the first frame. And then of frame 75. There. I'm going to push the height up to 10. Go up, not the height. Sorry, element size, the height to 10. And then I'll click on that again. So that way it will grow over time. And you can see we've got some kind of ease in, ease out there. So just go into your animation editor. Select both these keyframes and set this to linear. Okay. And then after that, so I like it to keep growing, but not change the, you know, this noise. I want this noise to stay the same. So we need a group for this front part and this back part. And it's easy to do that before the mountain. I'll show you why. So here if I do this by normals, set the direction to X and then bring the spread angle down. You can see it's just selecting the faces on this side. Just call this back. Then do another and then just change the direction to minus one and then call this front. The left and right doesn't matter. Really just different name for each of them. And then drop a transform after the mountain. Okay. And select back or France doesn't matter. And then so that mountain, if we remember the animation stops at frame 75 and I'd like it to continue moving, but you know, from that frame from frame 75. So alt-click on the X component. Okay, select that back attribute and then move up, up, yes, in this direction to six. That's something that looks good. Oh, sorry, we need to zero on six and then go to frame 200 and push this up to six. Alt-click actually make that change. Okay, so there you can see it will grow from frame zero. But actual noise will grow and then that noise will stay the same, but be transformed along the line. And again, we've got that problem with the easing in and easing out. So just select that. Set it to linear, put it back to the scene view and then just do the same thing. Alt-click and drag on that transform. But go to that last key frame on frame 200 and set this to minus six. Now, so it goes in the other direction and grab the other group. Go to the front and delete the back group from that. Okay, so now, there we go. So they grow together from nothing at the beginning and then grow together out to the end. But I don't want these to go all the way to the end. Okay, I'd like to leave a chunk at the end which is not being selected, which never becomes active. You know, we're leaving kind of a rough edge at the end of our geometry. And we can also, if we go back here to about this, you know, that first key frame is just looking at what's being selected there. We've got, I'd like to bring these by these kind of peaks over. So we can play around with this offset just to, you know, make a different selection. Maybe something like that. There we go. That's good. Big chunk on the edge. And you know, we've got a nice bit of difference between the two. Okay, so, you know, the pieces at the front here will become active before these pieces. And they will fall and they'll give us a more interesting edge to our fracture, right? So that's ready to go into the here. And then if we visualize the active there now, turn that off, just play that through. And see how that grows in an interesting way. Okay, so these pieces will be active and will fall. They'll still say glutes to the other pieces and kind of allow some nice bending and, you know, will collide with the active attributes, with the active, inactive pieces also. Okay. Okay, so that's all good and ready to go now.

**Frame:** tutorials\frames\week-01-11-rbd-configure-v1-1080p\frame_000.jpg


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

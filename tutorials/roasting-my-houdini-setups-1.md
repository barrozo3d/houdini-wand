---
title: Roasting my Houdini Setups #1
source: YouTube
url: https://www.youtube.com/watch?v=rvDsbo3slXc
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/roasting-my-houdini-setups-1/
frame_count: 0
frame_status: pending-selection
---

# Roasting my Houdini Setups #1

**Source:** [YouTube](https://www.youtube.com/watch?v=rvDsbo3slXc)
**Author:** cgside
**Duration:** 13m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py roasting-my-houdini-setups-1 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So I've been digging into my old setups, mostly setups that I've shared on Patreon and on YouTube, and I wanted to see if I would do it differently today.
[0:13] Mainly getting rid of poor loops and unnecessary operations. So in this first file I have this I start from a sphere and I get this sort of animation.
[0:26] This was part of a Patreon tutorial about a year ago. So basically I will go through the file and show you what I would change in year.
[0:37] So first of all I transform the sphere to have this sort of shape and the first operation I'm doing this for loop is to extract the group, these are horizontal lines.
[0:49] And the way I'm doing that is iterating over each ID that I set in here so I can show you that ID. So I divide these intersections and I iterate over them.
[1:00] And what I do is to do a group by range and select one of every other vertex. But as you can see when I promote it to wedges, it also selects this part because this one in here it collapses to a single point.
[1:13] So it messes up our selection and then I just do a very cheap max edge length in here to subtract or to intersect with the existing group.
[1:22] And that works but we have to do this in a loop, which is not ideal loops are complicated. You have to think twice before you drop a loop.
[1:32] There are situations you really need it needed like feedback loops and whatnot or to divide the operations into chunks like doing a poly reduce, a multi-traded poly reduce, for example, but most of the time we can avoid them.
[1:45] So in order to select this group, that's by the way I need to create the rig. So when I come in here and do the rig as you can see, I need to divide these intersections.
[1:57] And this files will be available on Patreon by the way, but how did I overcome the loop?
[2:04] So what I'm doing in here is selecting all the vertices that have a neighbor count less than five. So in here we have five. So I just want to select all the vertices, all the vertices, but these ones at the extremities.
[2:23] Then I do the final selection, so one out of two by finding the current vertex number in that group we just selected.
[2:32] And if we found if we found a vertex in that group and is every other one, we can select, we can append it to the group.
[2:41] And finally we just need to promote it to edges and there you go. You have the group clean that we can later use to do the reading.
[2:48] So that was easy, right? Now what's next? In this next example, I have this geometry and this geometry prepared for rigging.
[2:58] And in order to use the rig doctor, we need to have individual pieces, but also these middle sections connected to the field with these horizontal sections.
[3:11] So for that in a loop again, I write over them, I field the points as you can see.
[3:16] So as you can see, I field the points and then I polypads and this is necessary, a necessary operation to have a proper rig doctor.
[3:25] And again, we did it, I did it with a for loop, but there's an easier way since we have a class attributes or in this case I call it prem ID.
[3:34] We can just promote it to a point attributes and call it point ID and then we fuse and match the attribute point ID this way.
[3:42] We don't fuse points between between each ID and then we polypads and as you can see the rig doctor will not complain if we don't fuse by ID.
[3:50] As you can see, this will not work because it couldn't rebuild the hierarchy.
[3:56] So that was also very easy and the last step which is a bit more complicated is when we do the capture by proximity.
[4:04] So we have the rig, we have the geometry to capture and since we are doing a capture by proximity, if we don't do it in a loop, so isolating each piece and the same in here and doing the proximity, this won't really work.
[4:21] I can actually show you, so if I duplicate this capture and connect in here and connect this to the rig and I do this and then I append it to here.
[4:30] If I do the bond the form, as you can see, it will not separate the parts and it will be a mess.
[4:37] But when we do it in a loop, so let me show you, as you can see, this will work.
[4:43] But how can we avoid the loop? So that's what I did in here. But we need to, as you can see, I have, let me show you first, as you can see, I have this working in here perfectly without the loop.
[4:55] But in order for that work, we need to move the geometry, we need to separate the geometry and move it to a rest space.
[5:03] So as you can see in here, I have this rest space and I have the same for the UV, so they are separated enough that we can do the capture by proximity and then we can swap it back to the rest position that I'm saving in here.
[5:14] And as you can see, this will work just fine because we capture in a rest position where there's enough space to do the capture by proximity.
[5:22] But how am I creating this geometry? So this is the UV geometry actually.
[5:28] So if we go above where I have this geometry, I do a simple UV flatten and I get this sort of UVs, then I orient the UVs up with this HTA and by the way, let me allow editing of contents.
[5:41] I share this before, but in case you don't have it, you will have access to on Patreon.
[5:45] So this is something I share before this UVs up, this just orient them up and then I do a UV layout and I lay them out this way by using a fixed size and just playing with the settings in here with the scale.
[5:59] This way I can have enough space. Then it's simple, we just promote the UVs to a point attribute and do a natural but swap UV to be or just in a wrangle or something like that, you can do the same.
[6:10] And we do the same in here, you have to be and as you can see, those UVs that we created above, they will propagate to the rig geometry, to the curves because we extracted, we constructed everything with the same geometry.
[6:27] And that's the beauty of proceduralism because we can keep creating geometry and having the attributes transferred and everything in the end works pretty well.
[6:38] So as you can see now everything is working in here.
[6:42] So yeah, that was the first example and then I wanted to show you an extreme case.
[6:48] Okay guys, now in this last example I wanted to show you an extreme case where I have animated geometry and I am doing the loops on the animated geometry.
[6:57] I wasn't very proud at the time but I didn't found another solution in time and I had to release the tutorial.
[7:03] So let's have a look at what I would do today.
[7:06] So the first thing I do in here after creating the simple animation of the jellyfish in this case, I wanted to create variation.
[7:15] So in a forward loop, I do basically a time of sets and I speed up or slow down a bit of the animation ending up with different variations that I can later copy to points and have different variations of the same jellyfish.
[7:32] And how can we avoid doing this loop with animated geometry which is a pain.
[7:39] So what I ended up doing was doing a live file cache and creating in this case three variations the same as we have in here.
[7:47] So I did three copies in here.
[7:49] So labs file cache which includes wedge, wedge feature, same as we have in top.
[7:56] But this one is really simple to set up so you set the wedge count and I create an attribute called seeds that I can feed to the time shift to offset in a random frame and to a time blend that I can use to speed up or slow down randomly each variation.
[8:12] And then at the end I can just load all the geometry, all the variations and also wedges to merge.
[8:19] I set to all wedges so it loads every single variation as you can see.
[8:24] And now I also need in this case I have this copy num so an ID for each variation and in order to create that ID in the file cache you have these let me see file ID X that I later renamed to copy num to play well with my copy to points.
[8:42] So if we go in here as you can see we have about 120 frames per seconds if we do the first solution we get about 40 as you can see then with the copy to points everything gets slow down but that is normal.
[8:53] Okay guys that was the first example of these labs file cache know this really amazing I have to use it more.
[9:01] Now it comes a very hard part that I had no idea how to do this in a proper way basically I have these trails so let me show you first in here I have these trails that I simulated with volume let me slow it down and I want to mesh it with a sweep but without a proper up attributes I can't really have them stable because they are rotating all around and whatnot so what I need is the.
[9:30] Now I have a attribute that points into the geometry and now I did that previously was by creating a group expression and selecting the first point of each curve then group expanding to a flood field geometry and save a step attribute like the CG wiki video that I will link below that does this so we can later fuse.
[9:52] So I can show you you can fuse and study to average and match vegetables tap and this will create a curve in the middle that we can later use with an oriental along curve to create the normals using this banking how is it called banking curves so if I don't do this we get this sort of result which will not be stable for our sweep so we do this and I do this in a loop and we get all the variation but this is animated loop which I really don't.
[10:21] So what I ended up doing was promoting I have a premium ID as you can see on each variation and I promote that to a point attribute called ID X and then in here I take the step attribute from this group expand I take the step attributes and the ID X and I just multiplied by a big value so we have in a variation for the step attributes so it's not the same on every curve and then I just fuse.
[10:51] And we can do this without a loop so we fuse by that step attribute.
[10:56] The thing is when let me set this to zero and go in here and let's see how much the performance of this so let me increase so we get pretty good performance with a loop which I didn't worry too much at the time so it was performing well but when we do this without the loop look at this we get down to 40 frames per second and I was wondering why is that.
[11:20] So the reason is if I enable the second option we get about the same performance back as you can see and what's the difference both are using that match attribute but this fuse the one that performs well is using a snap distance so we feel constrained the fuse to a snap distance even if you're matching by attribute it's always a good idea to use that snap distance so the fuse no doesn't have to calculate an infinite infinite radius let's say.
[11:49] So you can see how much difference that makes from about the max frames per second to all the performance or something like that so as you can see that makes a lot of difference and then later so if we set this to one the green one and we compare it at the end as you can see we have a stable orientation
[12:13] everyone there why your sweep geometry is rotating around normally well that's because you don't have a stable attribute and normal so that's what I'm doing in here although I'm using also some roll to twist it a bit in the sweep but anyways that is basically it's.
[12:30] So guys I really hope you enjoyed this it was something I wanted to share with you.
[12:37] Of course with time we learn new things and we we can improve but hopefully this was helpful also to you and I encourage you to go through your old files and try to improve them again I really advise you to avoid for loops when you can and do it in a more with subs or with wax and try to optimize your setups as always you can grab the files on my Patreon please leave a comment below because I don't ask for life or substrations or anything like that but I always like to wear your feedback.
[13:06] I always like to wear your opinions in the comments so if this was useful to you or you have something to add please let me know in the comments and as always thank you for watching and I guess I'll see you next time thank you.



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

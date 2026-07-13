---
title: Procedural Materials in Houdini 21 | Patreon December '25  - Free Lesson
source: YouTube
url: https://www.youtube.com/watch?v=iZwfnJGQUlI
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-materials-in-houdini-21-patreon-december-25---free-lesson/
frame_count: 0
frame_status: pending-selection
---

# Procedural Materials in Houdini 21 | Patreon December '25  - Free Lesson

**Source:** [YouTube](https://www.youtube.com/watch?v=iZwfnJGQUlI)
**Author:** cgside
**Duration:** 11m20s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-materials-in-houdini-21-patreon-december-25---free-lesson <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone and welcome to this month's Patreon tutorial.
[0:04] In this one we will be generating a tiling pattern by combining the power of subs with
[0:08] cops in Odinut 21.
[0:11] There will be many tips and tricks along the way so I hope you join me in this one.
[0:15] I will also post a freeless on your own YouTube.
[0:17] Thank you.
[0:20] And now we will work on subdividing this geometry to look like cobblestones but it's
[0:28] easier said than done because in order to...
[0:33] we could easily do this let's say with a side fault remission.
[0:39] So let me just change this and let's say...
[0:44] So interrupt and change this to this one.
[0:50] And this can work but also we need to reduce this.
[0:57] And as you can see this works but not everyone has access to this.
[1:01] So I'm gonna do width in a custom way.
[1:04] I'm gonna leave these in here just in case and we're gonna do these in a different way.
[1:10] First of all I'm gonna populate the connectivity.
[1:15] And this should be on brims.
[1:20] And then I'm gonna iterate over this.
[1:23] So for each name print deal.
[1:29] And let's name this class.
[1:33] And now the idea now is to create some UVs on this and then move with...
[1:39] move the position to the UV geometry and do the subdivisions in there and then move
[1:45] it back to the...
[1:46] this deform shape.
[1:48] So I'm gonna start by doing a yellow time to D to extract the...
[1:55] the color from it.
[1:58] So in this case I'm just gonna change the resemble size.
[2:02] I can get rid of these and do a resemble size of point of three.
[2:10] And from here I just need to make sure I don't have any values going over zero on the
[2:17] life.
[2:21] Because we might have some values in there.
[2:26] And we're gonna do a re-sample.
[2:30] So as you can see this is following the shape more or less.
[2:34] And I'm gonna do a value of point of five.
[2:36] It's fine.
[2:37] Then just delete some attributes and we don't need it.
[2:45] Finally we're gonna create some normals.
[2:51] So as you can see the disc curve doesn't go fully to the end of the geometry and this
[3:00] will create some problems.
[3:02] So we need actually to extend this curve and for that I'm just gonna create some normals
[3:07] along the tangents.
[3:09] So we're gonna do a trick in here to extend this.
[3:15] If you notice we have in here on point group new ones.
[3:19] The list is created from this skeleton to the normed.
[3:23] So we target those points.
[3:27] And as you can see we have zero and nine.
[3:33] So let's try something.
[3:36] Let's do load sign.
[3:40] It will be called I add ptnm module of two.
[3:45] And we solve every other point.
[3:48] And we move.
[3:50] And subtract one to have zero centred offset.
[3:54] Now we multiply the normal sign.
[3:58] Let's see.
[3:59] And yeah we get the same result.
[4:01] I was doing it in a different way but this one will be much simpler.
[4:04] Because we have this even number in here and odd in there.
[4:09] So this will work.
[4:11] Now we can do a single bit.
[4:16] And we will be the new ones and connect them.
[4:20] Just over it so point over to five.
[4:24] It's fine.
[4:25] Then we can just delete the geometry roots.
[4:29] And do a sweep.
[4:34] And this will be a ribbon.
[4:39] And we want to compute the v's of course.
[4:42] Because we want to transfer them to the original geometry.
[4:46] And we can just set the size of the six.
[4:52] We might need to invert this.
[4:55] Yeah.
[4:56] Let's go to section.
[4:58] The rest is fine.
[4:59] Then we can do a bomb the mesh.
[5:06] We can do a sub-bomb the mesh.
[5:11] See how much I use.
[5:12] So point one.
[5:14] Now let's do a live CUB transfer.
[5:22] And as you can see we will have these UVs.
[5:25] So we might need to wait with the settings in here.
[5:28] So other than sub-bomb we will work better.
[5:32] And now as you can see since we have this flat geometry we can move it to the position.
[5:39] And then do the cutting in there.
[5:42] So for that I'm just going to go in here and create here and off.
[5:47] Maybe it orange me.
[5:49] Since we want to define this a bit later.
[5:52] And now I also want to do a UV flat.
[5:56] And this way smaller.
[5:58] So I'm just going to do Preserve Sims and Preserve Island Chips.
[6:02] And I did that.
[6:03] So it moves to the zero to one space.
[6:09] Then I'm going to do a measure on the area.
[6:13] So we have consistent polygon size at the end.
[6:19] Measure throughout some of the whole area of the geometry.
[6:23] Split UV Sims and promote this.
[6:32] Then we can attribute swap promote this to the position.
[6:36] So from UV position let's have a look at that.
[6:44] Then we can simply edit and remove shared edges.
[6:54] And see what needs a normal view just in case that's normal.
[7:01] Let's get rid of this.
[7:04] And now we can simply divide these along the edge.
[7:07] So divide nodes.
[7:11] Now we need to do a breaker polygon and then convex.
[7:15] And in this case we can do based on the bounding box
[7:21] exercise, B box zero, D exercise, the bar that let's say by 10.
[7:32] And we have this result maybe by something like this.
[7:38] And now we can do the same.
[7:44] We can do the same as we did in the example above.
[7:49] So this is on.
[7:51] And with the exercise it is function.
[7:57] So let's take this.
[8:01] And the rest it will be after the attribute swap.
[8:04] So let's see what's going on.
[8:07] And then this rest.
[8:09] And let's move this one here.
[8:12] This one here.
[8:16] And let's connect this.
[8:19] And we get this result.
[8:23] Let's do everything.
[8:25] But as you can see, if we don't do it based on the area,
[8:29] we will have inconsistent polygon sizes.
[8:33] So it will work well in these ones because they are identical,
[8:36] but nothing here.
[8:38] So the problem is the area is too small.
[8:43] So we could have normalized it.
[8:44] But let's just do this in a simple way.
[8:49] And I need to divide this by an integer number.
[8:51] So what I can do is do a seal and reading the area,
[8:56] some green zero, negative zero, we find,
[8:59] we want to read the area, the component zero,
[9:02] and then just multiply it by a big number, let's say, 3000.
[9:06] And we get now a consistent size of polygons
[9:10] independent of the size of the yacht.
[9:14] So as you can see, the form is just the same as before.
[9:16] They act like it is function and reading
[9:18] from the original position.
[9:22] So let's find.
[9:24] And now we can just achieve this.
[9:28] So let's do this.
[9:33] And we can actually do it.
[9:37] And we can do everything.
[9:41] And we can also group it.
[9:46] And we can do it.
[9:48] So we need to do this, but also to margin this.
[9:54] Let's create a match.
[9:58] And merge this in near.
[10:04] And as you can see, we have now the full shape then.
[10:10] Let's just do some cleanup work.
[10:14] I just want to create an ID for a couple of different
[10:19] languages on the primitives.
[10:22] So I add ID, it will be the print number,
[10:26] and it will increase by one.
[10:29] Because the background will also be zero.
[10:32] So we need to use one.
[10:35] And this goes on primitives.
[10:37] Let's do this.
[10:39] You can see there we do unique points,
[10:44] to separate the geometry.
[10:45] And finally, we have primitive properties
[10:49] and do a small transformation.
[10:52] So we decrease this to my 35.
[11:00] And let's just create another.
[11:03] And this will be our final output.
[11:07] So guys, this is basically done.
[11:09] The next step is to move these into cups
[11:12] and do the final material.
[11:13] Let's do that now.



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

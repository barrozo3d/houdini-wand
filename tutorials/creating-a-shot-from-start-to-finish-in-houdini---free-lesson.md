---
title: Creating a shot from start to finish in Houdini - Free Lesson
source: YouTube
url: https://www.youtube.com/watch?v=mweYGIlmD_Q
author: cgside
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/creating-a-shot-from-start-to-finish-in-houdini---free-lesson/
frame_count: 0
frame_status: pending-selection
---

# Creating a shot from start to finish in Houdini - Free Lesson

**Source:** [YouTube](https://www.youtube.com/watch?v=mweYGIlmD_Q)
**Author:** cgside
**Duration:** 11m56s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py creating-a-shot-from-start-to-finish-in-houdini---free-lesson <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome to this month's Patreon tutorial.
[0:03] In this one we will be creating this thing from start to finish, from modeling of the
[0:08] grapes to simulation with Vellum and some particles for the drops, and in the end we
[0:15] will put everything together in Solaris and render the final scene.
[0:19] There will be a free lesson on YouTube, so if you're watching this on YouTube there
[0:22] will be a sample lesson.
[0:24] If you want to watch the full workflow, make sure to look for my Patreon in the description,
[0:29] and I will see you there.
[0:30] Thank you.
[0:33] So now that we have our geometry and animation, I want to do some basic texturing for the
[0:37] grapes.
[0:38] So let's copy this freeze frame, so Ctrl C and create a copnet and do a sopping port.
[0:47] Nope, sopping port.
[0:49] Let's paste it in here.
[0:52] As you can see our UVs are not very famous, this is for the stems and this is for the
[0:56] grapes.
[0:59] But I want to proceed with this, so let's see what kind of issues we might have.
[1:02] So let's drop an adjacency node, so geometry to adjacency.
[1:07] We get this sort of result and now let's sample the attribute and we will need position
[1:18] and we will also need normal.
[1:22] Now let's try to do a basic, let's preview this and do a basic fractal 3D noise.
[1:29] And the first effect I want to create is to have some stripes on the grapes.
[1:36] So for that, let's try to do it one way, which is basically by reducing, let's say, this
[1:43] lead axis that works for that axis, but that's not what I want.
[1:49] So let's try to reduce it on the X and that does that.
[1:52] But as you can see, it's in world position, it's not following the shape of the grape
[1:55] or the orientation of the grape.
[1:57] So we can't really do it like this because this will be incorrect.
[2:03] So what we need in the end is to sample a rest position, but unfortunately I didn't
[2:08] save a rest position in here.
[2:11] And I don't want to go back and resimulate everything and whatnot.
[2:14] So what I'm going to do is take, for example, let's see if we have it here.
[2:22] So on the grapes, we should have an orient attribute for the valomere.
[2:26] So for the stems, and we can use that to create a rest attribute on the grapes.
[2:35] So let's copy in here, let's object merge this.
[2:41] So let's make sure we have the orient attribute and we do.
[2:46] Now we also need to apply the same offset for the time shift.
[2:50] So let's copy this.
[2:51] Let's alt-shift, alt-shift, alt-ctrl-alt-shift to create a reference copy and paste it in
[2:58] here.
[3:00] And now we will freeze the first frame.
[3:02] So with the time shift, let's make sure right here is animated.
[3:07] So we will time shift the first frame.
[3:10] Valor f-start, that's fine.
[3:13] Now let's isolate where we have the orient attribute on the stems.
[3:20] So let's have a look at that orient attribute and let's reduce it.
[3:24] So my idea is to take one of these last points on the stems and use it to reorient the grapes
[3:33] or to reset the transform of the grapes.
[3:35] So this is what I'm going to do.
[3:38] Now unfortunately I didn't save the tip attribute so we don't have it anymore.
[3:44] We have the tip ID but we don't have the tip point.
[3:48] So I will have to copy where I, before I delete it.
[3:52] So I believe I delete it in here.
[3:54] Yes.
[3:55] So let's object-munch this and this is already frizzed.
[3:59] So let's see.
[4:00] Let's also blast the grapes and let's see if we have in here the tip and we do have.
[4:08] So it's the point before but it's okay, it doesn't matter.
[4:11] So we can use that.
[4:12] So what we can do now is to do an attribute copy and we don't want to copy the CD.
[4:21] We want to copy this tip.
[4:25] Let's see if that works, it does.
[4:26] And now let's isolate that, that specific point.
[4:31] So let's make sure it's point and add this tip.
[4:36] This tip is equal equal to one.
[4:40] And now we should have the oriented attribute there and we also have the tip ID which will
[4:47] help us.
[4:49] So if I get rid of the orient we have the tip ID which should help us to target the correct
[4:57] orient for each ID.
[4:59] So what we can do now is to get this one in here, this time-shifted frame, which is the
[5:09] initial frame.
[5:12] And let's again blast, but this time the grapes.
[5:16] Blast the stems I mean and keep the grapes.
[5:19] And now let's reset the transform on the grapes.
[5:21] So let's, we want to work with the grapes of course and let's use those points.
[5:26] As you can see we also have the tip ID on the grapes.
[5:29] So we can easily use the find attribute valve function to find the correct point on the
[5:34] second input.
[5:36] So this one will be reset X-forms.
[5:39] Now let's increase this and start by wearing the point.
[5:45] So we find attribute valve, find attribute valve on the first input.
[5:51] It's a point attribute.
[5:53] It's called a tip ID and we can pass I at tip ID.
[6:00] This will give us the point, the correct point on the second input.
[6:03] And now we can simply grab the orient.
[6:05] So vector 4.1, we want to grab the orient using that point we found.
[6:15] And we also want to grab the position, I mean I think, yeah, the position of that point.
[6:28] And now let's create a matrix from it.
[6:30] So matrix, empty acts will be equal to Q convert.
[6:34] This will be easier to work with an orient.
[6:39] And now let's just V at P multiply and re-invert that transform.
[6:45] What am I missing here?
[6:51] So what am I missing?
[6:57] Line 3.1.
[6:59] Oh, vector 4 P, sorry.
[7:04] Vector 4 orient.
[7:07] Now we also need a translation to reset it to the origin.
[7:10] So for that let's just translate these matrix by the position of those points.
[7:18] And now we get something like this.
[7:20] We get the grapes transform reset.
[7:24] And we can also create a rest attribute.
[7:26] So V at rest, it will be equal to V at P, this current position.
[7:32] And if you want you can also create an orient attribute, but I'm not going to bother.
[7:36] So that's all the work done.
[7:37] And now we can create a null and name it OutRest.
[7:42] All right, let's copy this path and let's go to the covenet.
[7:50] And let's now import the same.
[7:54] And I don't have to 3D preview, just want this.
[8:00] And we will do the same in here.
[8:02] So let's copy the adjacency and the position.
[8:07] We could either grab the position or the rest, it will be the same.
[8:11] So let's just grab the rest, it will be the same.
[8:14] And now what we can do, let's preview this in here.
[8:18] And as you can see, we have a single rest attribute for everything.
[8:21] What we can do now is to let's try to do the same fractal noise thing.
[8:28] And we have point one on Y.
[8:31] And as you can see, now it's oriented, but I don't want this way.
[8:35] So let's do this one, but it also is not what I want.
[8:38] So let's try another one and maybe play with this.
[8:43] But as you can see, we will never get the correct behavior.
[8:48] So let's try...
[8:50] We will never get the...
[8:53] So let me see.
[8:56] As you can see, it's stretching on this side.
[8:58] Let me increase the resolution to 2K, maybe 4K, because the UVs are way too small.
[9:05] As you can see, it's stretching the way we want, but it's kind of collapsing in the ends.
[9:09] So we can't really use this, we will need to work around.
[9:11] Basically, we will need to create some custom UVs.
[9:15] So for that, let's channel split the position.
[9:22] And we get here the X and the Y and the Z.
[9:28] And in this case, we want to channel join the Y of V attributes, the X and the Y.
[9:37] And we get some UVs.
[9:45] But still, this won't give us much.
[9:47] What we need to do is to transfer this from UV to Polar.
[9:52] And now we should get what we need.
[9:55] And if we, for example, now use this map and repeat it around, we will get those stripes we always wanted.
[10:02] So for that, I'm just gonna multiply constant this angle.
[10:07] Let's say by 25.
[10:12] And now we can just modular with a function node.
[10:16] So let's do modules and there we have the stripes.
[10:21] You can create some watermelons with this.
[10:23] Also, we can repeat it more maybe.
[10:27] Let's keep it like this.
[10:28] Now I just want to add some noise also.
[10:31] So for that, let's grab this noise and use this position.
[10:38] And for this noise, let's reset this and set the value of 0.2.
[10:45] Let's maybe increase a bit this.
[10:48] And we want an RGB since we want to, or in this case UV, I mean, since we want to distort the UVs.
[10:55] And now where we can do it is right here before we do the UV to Polar.
[11:00] So with an add node.
[11:02] And let's preview this.
[11:04] And let's preview this.
[11:05] We can just distort these and maybe reduce the effect to something like 0.2.
[11:13] No, that's fine.
[11:14] So you can increase more or less.
[11:18] And that's fine.
[11:19] Now we can just blur it a bit.
[11:23] Not so much maybe.
[11:25] So 0.285.
[11:29] Maybe a bit more.
[11:31] So something like this.
[11:33] And maybe repeat it even a bit more.
[11:36] So in the multiply constant, let's set it to 40.
[11:40] And as you can see, it's following the orientation of our grips.
[11:44] So in the next lesson, we will, in the next part, we will start to work on the other parts of the texturing.



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

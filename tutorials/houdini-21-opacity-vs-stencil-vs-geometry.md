---
title: Houdini 21 | Opacity vs Stencil vs Geometry
source: YouTube
url: https://www.youtube.com/watch?v=ha85low9Bmo
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-21-opacity-vs-stencil-vs-geometry/
frame_count: 0
frame_status: pending-selection
---

# Houdini 21 | Opacity vs Stencil vs Geometry

**Source:** [YouTube](https://www.youtube.com/watch?v=ha85low9Bmo)
**Author:** cgside
**Duration:** 8m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-21-opacity-vs-stencil-vs-geometry <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome.
[0:02] So in this video, I wanted to compare
[0:04] the new stencil feature to render opacity-based lips
[0:08] compared to other workflows.
[0:10] So we will compare first geometry
[0:13] without opacity maps, then we will do
[0:15] with opacity maps, then the stencil
[0:18] and finally geometry-based.
[0:20] So to not waste your time, I'm going to write away
[0:22] the test in front of you.
[0:24] And after that, I can show you my little setup.
[0:28] So I just have this demo scene that I put together quickly.
[0:31] And I'm going to load the first test.
[0:33] So the first test is just the leaf.
[0:35] So I'm going to show you in here.
[0:37] It's just the leaf, the lips with no opacity maps.
[0:39] As you can see, we have all the geometry.
[0:43] So let's compare that.
[0:44] Let's run the render and it shouldn't take too much.
[0:49] So it will take about, I don't know, 15 seconds maybe, maybe more.
[0:55] So we took 26 seconds.
[0:57] Let's map it and save it.
[0:59] Now we will render opacity-based.
[1:01] So I'm just going to change in here the material
[1:04] and set the opacity.
[1:06] And let it do a render.
[1:08] And make sure we restart.
[1:09] This is a bug in Audini 21.
[1:11] As you can see, the time to the first pixel
[1:14] it will be a bit slower.
[1:15] Let me pause and come back to you.
[1:17] So I almost finished.
[1:18] And that took two minutes and 35 seconds.
[1:21] Let's map it.
[1:23] And now let's go for the stencil option.
[1:26] So I'm going to change again the material
[1:28] for the one with opacity and enable the stencil map
[1:33] in here in the render geometry settings, stencil map.
[1:36] And I'm going to enable that and we render.
[1:40] And I need to restart the render.
[1:43] And as you can see is going, let me pause.
[1:46] So that took 27 seconds with the stencil map.
[1:51] And now let's change again to the geometry-based.
[1:56] So without stencil and without opacity maps, just making sure.
[1:59] And now let's do a grid render.
[2:01] Make sure we restart.
[2:04] And let me pause.
[2:06] And as you can see, that took only 16 seconds.
[2:09] So I think we have an issue in here.
[2:11] So for the first one, we had 26 seconds.
[2:14] And the last one, we had 16.
[2:16] But let's do another test.
[2:19] Without with the first geometry.
[2:22] And making sure we don't have any issue.
[2:25] So let me just restart.
[2:27] Because I think it's taking longer than was expected.
[2:31] So let me pause.
[2:32] So we know it makes more sense 15 seconds.
[2:35] So let's snap that and delete the first one.
[2:38] Can we move this one? No.
[2:40] So without opacity maps and stencils, it took 15 seconds.
[2:44] Then with opacity maps, it took two minutes and 36.
[2:48] With stencil 27 seconds.
[2:50] And with opacity-based lips, only 16 seconds.
[2:53] So with geometry, it takes the same amount of time.
[2:56] But this one, as the right cut out.
[3:01] And this one is just the basic geometry being opacity-based.
[3:06] So you can compare for yourself.
[3:08] The stencil is still worth it.
[3:10] So 27 seconds.
[3:11] But you can see how these will scale up.
[3:14] So it's still the better option is to use opacity-based lips.
[3:18] Or you can just render full geometry without the opacity map.
[3:22] And if it's far from far away, it will still be okay.
[3:26] So there you have your tests.
[3:29] Now I'm gonna show you how I set this up.
[3:33] So let me switch in here to the initial layout.
[3:36] And let me have a look at the tree in here.
[3:39] So this is my tree, nothing special.
[3:41] But let me make sure I disabled it so you can see.
[3:44] So this is the best tree I did with the simple tree tools.
[3:50] Nothing too special.
[3:51] We have done this before.
[3:52] Then I have a lips scatter, which I'm packing.
[3:55] So I'm using instances.
[3:57] As you can see, quite a lot, 6000 instances.
[4:00] Or the proxy.
[4:01] I'm doing unpack.
[4:03] Getter a few points.
[4:04] VDB from particles.
[4:05] Convert VDB with an eye adaptivity.
[4:08] And then poly reducing it.
[4:10] And then I export this as a proxy.
[4:12] And then for the tree, I noticed we have an issue right now.
[4:17] You know, in 2021, this is the first version also.
[4:19] That if I merge the trunk and the branches with the lips,
[4:24] I get no stencil map working.
[4:26] So I have to separate the branches from the lips.
[4:30] So that's what I'm doing in here.
[4:32] I'm exporting in here the trunk and branches in one file.
[4:36] Then in another file, I'm exporting just the lips.
[4:39] And make sure I set it to create pointy instanceer in the pack primitives.
[4:43] And then for the opacity, for the geometry based one,
[4:47] as you can see, we have in here the Atlas processor.
[4:49] And we have the geometry around.
[4:53] And if I enable the HTA that I'm going to share on Patreon,
[4:57] this just creates from opacity to geometry.
[5:01] Puppacity based lips or vegetation.
[5:03] And convert it to geometry.
[5:05] So this is a new version of my HTA that I'm going to share.
[5:09] But you can totally use something custom.
[5:12] And then I'm doing the lips scatters,
[5:15] like we did for the opacity based ones.
[5:19] And I'm exporting that in this case as tree lips meshed.
[5:25] And as always, create pointy instanceer.
[5:27] Then in Solaris, let's have a look at all that setup.
[5:30] So let's go to obj.lopnet.
[5:35] And look at the geometry spreadsheet.
[5:39] So in this case, I have a switch between the opacity based lips and the meshed lips.
[5:46] So I'm just referencing here the trunk and branches, the lips and the proxy,
[5:51] and doing the same in here, but the meshed lips.
[5:53] Then I'm putting these in a render folder, as you can see in here.
[6:01] And also doing the same for the proxy in a proxy folder.
[6:05] Then just setting the purpose, render and proxy.
[6:09] As you can see, if I change in here, I find able the purpose.
[6:13] One is proxy and the other is render, the other two.
[6:18] And if you still have this issue of both meshed displaying, just reset the report.
[6:23] And it will go away so you can switch between the final render and the proxy.
[6:29] From there, I'm creating a collection and doing a basic instance in using that collection.
[6:34] I'm doing it in the first input so I can, in this case, I'm doing the materials after,
[6:40] but I could have done the materials before and that way it will propagate to the instacer.
[6:44] So then doing the instacer, as you can see, applying the materials, which one,
[6:49] just as the albedo roughness, normal and translocency,
[6:55] and the opacity-based one as the opacity connected right here to the opacity.
[7:02] So opacity.
[7:03] And I'm also using DINWOLD on both and playing a bit with the exposure and U of the albedo.
[7:10] I have also a trunk material, just very basic.
[7:13] And then in here, I'm doing the stencil thing that we tested.
[7:19] And yeah, that's about it. I'm also increasing a bit the SSS limit.
[7:23] And I just left the pad trace samples to default.
[7:28] So as you can see again, we go from 16 in geometry-based renders,
[7:33] but the other geometry-based as the advantage of having the real cutout.
[7:37] Then we go to opacity, which increase quite a bit the render time.
[7:43] And finally, we do the stencil, which is still much better than the opacity-based,
[7:48] but is also slower than the geometry-based.
[7:53] So I hope that was clear. Sorry for not doing a video on Audini 21 features,
[7:58] but I'm having some bugs. I already reported them.
[8:02] I'm trying to do some new videos on cops and on other things.
[8:06] But for now, I just wanted to compare these stencil-new work-clothes.
[8:11] So I hope you find this useful.
[8:13] And as always, you can grab the full scene on Patreon,
[8:15] or find with exclusive tutorials.
[8:17] Other than that, please leave your comments below,
[8:19] and I guess I'll see you next time. Thank you.



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

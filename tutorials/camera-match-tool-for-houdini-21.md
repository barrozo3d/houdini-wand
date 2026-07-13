---
title: Camera Match tool for Houdini 21
source: YouTube
url: https://www.youtube.com/watch?v=NkVT9NtRMk0
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/camera-match-tool-for-houdini-21/
frame_count: 0
frame_status: pending-selection
---

# Camera Match tool for Houdini 21

**Source:** [YouTube](https://www.youtube.com/watch?v=NkVT9NtRMk0)
**Author:** cgside
**Duration:** 11m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py camera-match-tool-for-houdini-21 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome, so in this video we're gonna have a look at a new tool that I'm sharing today, which is a camera matching tool similar to Webspy but inside of Inny, which is with its own solver.
[0:12] So I'm gonna share this tool as part of the Patreon Benefits for this month, so if you wanna learn how these tool works, stick till the end of the video, and I will be showing you a few examples.
[0:24] Okay guys, in here I have a folder with the different images we're gonna use for two vanishing points, one vanishing points, so we're gonna start by just copying the pet in here.
[0:37] And let's drop camera match here in the object context, and we're gonna load in our image, so in this case it's this one and we're gonna enter the tool.
[0:48] And by default it will be on one vanishing point mode, in this case we can actually increase, hit the brightness and reduce the opacity if you want, and enable to disable the background image.
[1:00] And let's change these to two vanishing points, because we're actually using, we actually have two vanishing points, one for the x, one for the z, the y looks pretty straight, so it's not a tree vanishing point.
[1:15] And I know also that these are portraits, so the aperture usually refers to the horizontal film back, so in this case we want to change it, and a good way to calculate that is just take the resolution x, and paste in here and multiply by the film back horizontal size, so 36 and divide it by the resolution y.
[1:40] This is just a formula that you can keep in mind, so it will give us 24, so if you know the film back size, you know already that it will be 24, but in case you have a crop image, you can use this formula to calculate the proper aperture.
[1:55] So the focal length will be computed from when we drug the different perspective lines, and everything else we can leave to default.
[2:04] So let's start dragging this point, so I'm going to drag in here, and at any point you can zoom in with provide pressing that the that key, and I'm going to drag this one here.
[2:18] And let's zoom in, I'm going to do this one with you, and then I can skip this part for the other examples, so let's place one in here.
[2:27] And also in here, and drag maybe it is one round here, and we can extend if needed, and then we can grab the origin and drag it let's say to here, and now we have a night reference, you can see that the camera it is about is less than one meter, so you can just grab it, until you feel these measures like one meter, which is a reference size that you can increase or decrease is going to leave it to default.
[2:52] Let's say this is about one meter, and is computing a focal length of about 40 camera, let's maybe increase this, so the camera it usually is the human height not always, but you can use that as reference.
[3:06] And let's see how this looks, so if I decrease the opacity, you can see that it's working pretty well, and maybe it's a bit more, or just to be precise, you can do it like this, and as you can see the lines are aligned really well with the grid.
[3:30] So now that we have this, we can just create the camera, and we will have a new camera with all the settings applied, including the focal length and everything, and we can press age and switch to the shot cam, and we can start to do whatever we need to do, like image based modeling or something like that, so you have the option to export the camera with this button, which will be named shot cam, you can rename it for everyone.
[3:57] So that's the two point two vanishing points or two point perspective, and next we will do another example.
[4:06] So now let's have a look at one point perspective, so I'm going to look in here an image for one vanishing point, and I'm going to enter the tool, and it's on one vanishing point by default, so what I can do is just increase the background brightness, and I'm going to drop the horizon line.
[4:28] So in this mode, the tool doesn't excimate the focal length for one point perspective like X-Fide, so you kind of have to eyeball it, so you can probably place an object along the boundaries of your image, your viewport, and then you can excimate the focal length by playing with different values and see which one fits better.
[4:52] In this case, I know a value of 44 is about right, but then for this kind of one point perspective, you have to guess the focal length.
[5:02] So in the next step, we will look, we've been using this principle point, which is the central point of the image plane of the camera, we've been using the midpoint, which is by default, but we can also set it to manual, and what this means is that the image might have been cropped,
[5:19] and you need to play with the principle point to have proper soul. So let's look at an example of that, so for that I'm going to use this example in here.
[5:30] So as you can see, I can drop in here to manual, and the principle point will still be the same as midpoint, so by default it's the middle point.
[5:39] What I will do is to copy this path and create a nearer copnet, just to crop the image and do a test.
[5:47] So let's do a file, let's load in this one, and we can actually record where that original middle point has been placed, so I'm going to do just a quick snippet that I have in here.
[6:03] So center point, principle point, and you can see 12 drop of points in there in the middle of the image, and then I'm just going to crop.
[6:11] And I'm going to do on texture space and increase these, let's say, to point tool and decrease this one to point nine. So now the principle point is no longer in the middle of the image, because if we drop again another one in here, you can see that will be upset.
[6:29] So we need to refer back to this principle point to have a proper soul. So let me just drop image output this, and I'm going to write it as, let me just copy the name from this path.
[6:43] And name it, I'm just going to render. Now I'm going to place another one. So just for clarity.
[6:56] And let's grab the finishing point, and as you can see, you know, this is also our portrait mode. So we need to copy the same expression.
[7:08] So let's just copy and paste it in here, and this will be different because the resolution is also different. So let's actually enter the tool and let's change this to two points.
[7:20] And let me just increase the brightness and making sure I have this correct, more or less.
[7:30] And place another one in here. And for this one, we can place it in here.
[7:38] So let me actually extend this and for the ZX-ish, we can place it right here.
[7:47] And let's drop the in here and show the grid. And let's play with the size. What about these much?
[7:56] And let's see, let me decrease the opacity. As you can see, it's kind of a lining, but it could be better.
[8:03] So let's place these in manual mode and move these to the principal point, original.
[8:13] And let's have a look at it now. You actually decrease. You can see if you look at this line, you can see the lining much better.
[8:21] So let's actually switch between one and another. And as you can see, it's a lining pretty, pretty well.
[8:30] So that's the manual mode and in the last. And by the way, you can, so if I do this, I can undo redo. It should work. So if I move these, I can undo.
[8:40] And it should calculate everything again. So that's fine.
[8:44] And another thing, you can set your measuring axis to be in a different axis. So for example, on the X, on the Z, in this case, I'm going to set it to Y.
[8:55] And yeah, let's just type a look at the principal point calculated from a third vanishing point. Let's look at it now.
[9:03] So let's drop another camera match and let me load the three vanishing point image. So the recised one.
[9:12] And we can also do the same in here. So the same expression.
[9:19] And let's place these at two vanishing points and third vanishing point from the principal point.
[9:28] Place these ones.
[9:33] Now let me increase the brightness to.
[9:38] Let's go for the X axis.
[9:45] Same as in here.
[9:49] And finally to set the axis, we can place this one. It's good to place the lines at the different, not very close to each other.
[9:58] So we get a better picture.
[10:01] A better soul, I mean.
[10:04] So let's drag these in here.
[10:07] And let's say this is about one meter.
[10:13] And that you can see if we switch between manual, which is just using two point perspective.
[10:19] Let's actually see the ground. As you can see, it's aligning.
[10:24] If we switch to from third vanishing point, it's much, much better.
[10:28] In this case, this is a three vanishing point image.
[10:31] And as you can see, it's working pretty well.
[10:33] You can of course do a better job aligning these. I just leave this quickly.
[10:37] And you can place your different eyes.
[10:40] The shape always check the computed camera. I'd for reference.
[10:44] And you can also play. If, for example, you want to, you know, the eye of this building, you can place it here and just drag the line along that move the point and drag the line along that direction.
[10:53] So usually the measure axis to why it will work well, but in any case, you can switch for a different route.
[11:01] So yeah, guys, that's about it.
[11:03] You can grab this to less part of the Patreon benefits for this month.
[11:07] See, so this is what I'm going to share this month instead of a tutorial.
[11:11] And if you don't want to subscribe to Patreon, you can also grab it on my Patreon shop.
[11:16] And yeah, thank you for watching. And I hope you enjoyed this new tool. Thank you.



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

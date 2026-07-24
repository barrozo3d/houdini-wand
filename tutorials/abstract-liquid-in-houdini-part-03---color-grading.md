---
title: Abstract liquid in Houdini | Part 03 - Color Grading
source: YouTube
url: https://www.youtube.com/watch?v=YqS517Rvhzo
author: Kotov Roman
ingested: 2026-07-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/abstract-liquid-in-houdini-part-03---color-grading/
frame_count: 0
frame_status: pending-selection
---

# Abstract liquid in Houdini | Part 03 - Color Grading

**Source:** [YouTube](https://www.youtube.com/watch?v=YqS517Rvhzo)
**Author:** Kotov Roman
**Duration:** 9m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py abstract-liquid-in-houdini-part-03---color-grading <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello! Today we will be looking at the third and the final part of the three-part tutorial series.
[0:06] We've done the simulation in the first part and rendered it out in the second one.
[0:10] Let's finish it in After Effects with some light color grading.
[0:13] If you missed first two parts, the links are in video description. And let's get to it.
[0:19] Let's drag and drop our renders into the project window.
[0:22] If we're done, we'll click on any of the renders we can preview it. But as you can see,
[0:26] the colors look wrong. That's because I was rendering in linear, but after effects,
[0:31] sRGB by default. There are several ways of fixing that. The easiest one is clicking control-LG
[0:38] on the footage. And going into the color tab and checking on preserve RGB.
[0:44] Let's do that for both of our renders. Now let's create compositions from those renders.
[0:50] You can drag and drop them on the comp icon or in the timeline. Let's make some more space to work with.
[0:57] Now we can view our render and see what adjustments we can make to make them better.
[1:01] The first one I see is they should be denoised. We can click control-Alt-Y to create a new adjustment
[1:07] layer. Let's call it denoise. I'm using effects console from video compiler to search for plugins.
[1:13] And my favorite one for denoising is reduce noise. Let's add it to an adjustment layer.
[1:19] And open it up. But actually before doing that, we should find the frame with the most noise in it.
[1:26] That will ease the noise pattern recognition. Now that I have that frame, let's open it up again.
[1:32] To start with, you select an area with the most noise in it. I think this one will work for me.
[1:38] And click build profile. Now I can go into the adjustment preview tab and
[1:42] tell plugin exactly what I want from it. You can navigate before the middle mouse button.
[1:47] It also temporarily disables the plugin so you can see the before.
[1:51] Let's see how many frames I want the plugin to use for denoising.
[1:54] The more frame we use, the cleaner the results are, but we also lose details.
[1:58] Let's stop at two frames before and after. Now we can go into the spatial tab and reduce the
[2:03] noise level. So we can bring back some of those details. We also will be bringing back some of
[2:09] that noise, so it's a bit of a trade-off. I think for how noisy that render was, those settings
[2:13] will be fine. Let's check if we get some obvious artifacts from denoising. And so far it looks
[2:20] good. Now we can add a new adjustment layer and call it CG for color grading. I forgot the name of
[2:28] After Effects color grading plugin, Lumetri Color, so I will be starting with the curves.
[2:33] First, let's make a standard S curve. That makes the image a bit darker, so let's add an exposure
[2:38] and crack it up a bit. I'm also seeing that the darks are clipping, so let's maybe raise that S
[2:45] curve and lower it a bit. That just adds a bit of contrast into the image.
[2:52] Let's see what else I want to add here. I'm thinking mask to darken front and far away
[2:56] particles would be nice here. Let's add exposure and drop down the gamma. I will call it layer mask
[3:04] and add a mask to it. I will also recolor the mask so it's easier to see and reposition it slightly.
[3:11] I will add feather to the mask and invert it as well.
[3:16] After some adjustments to the mask, I think I will add hue and saturation as well.
[3:21] And drop down saturation. Now I want to mimic some artifacts from the edges of the lens.
[3:27] Let's drop down new adjustment layer and search for chromatic aberration.
[3:32] Most likely that's not gonna work. In the hand side, I should have used VR chromatic aberration
[3:36] instead. Let's drop down radial blur and see what types of work I'm with. I think I will stop
[3:42] on the tagging zone. We want the effect to be slightly visible, so let's stop at 15. Rename
[3:47] the layer to zoom blur and add a mask to it. I will do the same adjustments to that mask as I
[3:52] did the previous one. I will recolor it, add feather and invert it. And I can see that the
[3:58] amount is a bit too much, so let's drop it down to 3. That will give us just a bit blurred in
[4:02] stretch corners. Let's collapse all of the layers. We could also use U shortcut and add
[4:08] Lumetri color to color grading adjustment layer. In there, I will increase vibrance
[4:14] and lower down saturation. Maybe add a bit of faded film to raise those black spots.
[4:24] Now let's scroll down to the color wheels. I want to make shadows just a bit colder
[4:30] and highlights a bit warmer. It doesn't need to be a huge difference, just a bit is enough.
[4:38] We can also try lowering the shadows on the color wheels.
[4:47] And a few adjustments later, I'm happy with the results.
[4:51] Let's make a new adjustment layer and call it Unsharp. It will be used for sharpening our image.
[4:56] Let's zoom in a lot to really see the details. I doubt you will be able to see that through
[5:01] the compression, but the Unsharp tool doesn't really need much. Around 20 on the first one
[5:06] will be just enough. Let's drop down the second one, change the radius to 2, and the amount for it
[5:11] will be even lower. It will add just a bit of crisp to the highlights. Now let's add noise before
[5:25] the sharpening. 5% might be too much. I usually set it to 3%. After that, I would like to drop
[5:35] down at grain. Set the viewing mode to final output. Size is larger than I would want,
[5:41] so let's drop it down to 0.4. An intensity to 0.15.
[5:48] Let's maybe drop down intensity to 0.12. A nice amount to 2%.
[6:02] Let's see if we can add something better to the zoom blur.
[6:06] I will drop down Fast Box Blur and set it to really low blur radius.
[6:12] As you can see, all of those small adjustments add up. Now we can work on the second composition.
[6:17] Let's create one and copy all of our effects into it.
[6:22] It will need some adjustments to match up. To make it easier, let's create a second viewport
[6:26] so we can see them side by side. Let's go through each layer one by one and see what
[6:31] adjustments we can make. I will start with the Curves.
[6:37] The contrast looks already closer. Let's make some more room.
[6:42] And let's tackle down those reds. We can use Hue vs Hue Curves to slightly change the colors.
[6:48] Let's choose a red with a color picker and see what we can do. I also would like to use
[6:52] Hue vs Saturation. Let's do the same. Choose the color and drop down saturation on the red.
[6:58] I feel like red might be a bit too bright, so let's use Hue vs Fumon and drop down luminosity on the red.
[7:04] I will go between them for quite some time. The final result will be dependent on the temperature
[7:09] and the angle of the lights you have, so you don't have to follow my setup exactly.
[7:18] Now let's go and check all the other layers.
[7:25] Seems like they're working nice they're supposed to and don't need any further adjustments.
[7:30] Let's create a master comp for rendering. Drop both of our compositions inside.
[7:36] You can match them however you want. I will go with the standard ABA thing.
[7:41] I will start with the camera one, get the cut to the second camera and get back to the first one.
[7:48] Now let's hit shortcut control M and set up render settings for that composition.
[8:02] Now all is left to do is choose the render location and render it out.
[8:07] And that's a wrap for this series. I wanted to say thank you for sticking around.
[8:11] And a special thanks for those who liked outros. I've prepared a small edit of me trying to match
[8:16] the reds of those cameras. Enjoy!



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

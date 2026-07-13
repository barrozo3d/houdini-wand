---
title: Houdini Heightfields and Cliffs
source: YouTube
url: https://www.youtube.com/watch?v=fF01Lyg_G48
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-heightfields-and-cliffs/
frame_count: 0
frame_status: pending-selection
---

# Houdini Heightfields and Cliffs

**Source:** [YouTube](https://www.youtube.com/watch?v=fF01Lyg_G48)
**Author:** cgside
**Duration:** 11m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-heightfields-and-cliffs <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'll share a few tips on how to
[0:05] create terrains in Odini, especially using the new Pegasus tools to colorize the
[0:14] terrain and also how to incorporate some cliffs in your terrain. So let's get
[0:23] started. I'm starting with the Night Fields which is 500 by 700. Then I'm adding
[0:34] a noise and this noise typically looks like this like if it was a desert but in
[0:47] this case I used which is the Worldly Cellular F1. In this case I used the
[0:52] compliment so I can get these shapes and then I can distort it and you will
[1:06] start to get some interesting results. The distortion is just a color with a very
[1:13] high element size and some amplitude. We get something like this. Then I want to
[1:23] incorporate some raw formations. This is similar to a video I shared before but
[1:30] just in case you didn't watch it. I'm basically taking a very distorted shape
[1:39] and projecting it to my battlefield. Then I'm using a mask expand set to
[1:46] height instead of mask and I get the square-doubt shapes and yeah that's
[1:55] basically it. Then I'm incorporating in the terrain with the battlefield layer and
[2:03] in here I'm distorting only the cliff or the raw formations and in here I am blurring the bottom
[2:15] by using again a Night Fields layer with manipulating the masks and then blurring it and I can
[2:24] blur the bottom. So it incorporates better into the terrain. That I'm saving this to mountain
[2:32] layer and in here I'm creating a volume knob to add some custom noise. In this case I'm using
[2:42] a cloud noise and bind exporting it to the mask and I can use a remap and you can see we got
[2:52] we start to get this cloudy look in the terrain which will help in the erosion stage.
[3:00] So in the remap I just increase the output max, compute range and then increase the output max.
[3:08] And I'm clearing the mask and doing a first pass of erosion.
[3:16] And we start to get these valleys but still is not in a resolution. As you can see we only have
[3:26] 2 million vuxels which is low. Then I am again loading the mask with a copy layer by
[3:38] specifying the source as mountain and this nation as a mask. Then I'm blurring the result from
[3:47] the erosion on the mountain, on the raw formations. Then I'm resampling it
[3:56] to a higher resolution as you can see 40 million vuxels.
[4:02] And then I'm just creating a mask of the terrain so I don't erode too much the raw formations
[4:13] and I'm doing a second pass of erosion.
[4:16] And as you can see we start to get way better results with these typical rock shapes
[4:28] with a lot of valleys. And then I want to flatten more these areas and remove these noise that we have
[4:40] and just overall flatten them. So I'm using a mask by feature.
[4:46] We mask last load to get these flat areas and I'm using an i'd field flatten.
[4:56] And we should get these results as you can see. We go from these to these flatten areas.
[5:05] So this is where we catch the results and we have quite interesting terrain and some rock
[5:18] formations. And this is where I will start to use the Pegasus tools. Mainly the i'd field material
[5:28] that you can use to colorize the terrain. In this case I'm creating a mask by i'd just selecting
[5:36] everything and just adding some terrain texture, some base texture. Then in the second one I'm adding
[5:51] some darker value on the occlusion. So I'm just layering the mask and then mask by feature.
[6:00] In this case I'm using occlusion and tending the result as you can see.
[6:10] And we start to get some more interesting results.
[6:13] Then in this one I am masking the more flat areas and adding some grass as you can see.
[6:29] This is pretty simple. You just plug the color and the height if you want to add some height.
[6:35] And then you can play with the distortion so the texture doesn't rip it so obviously.
[6:43] So in this case I am tending a bit the grass mask, the grass texture I mean. And then
[6:56] remapping it or increasing the tinge value. But in here what I'm doing is creating a mask noise
[7:05] on the previous grass mask so I can remove some areas. And then tending it with a gradient.
[7:15] As you can see from green to yellowish white. And then just increasing the value of the tinge.
[7:25] This is a pretty useful node.
[7:27] And you can see we start to get this interesting result.
[7:38] Then in here I am masking more the cliff areas and adding some texture there.
[7:47] And doing again the same in here. Some more details.
[8:01] And I am also increasing the brightness of those cliffs.
[8:07] And now I am creating an occlusion mask I believe.
[8:16] Yes an occlusion mask really tight. And tending the resulting texture.
[8:27] By a gradient you can see if I increase the strengths we get a more
[8:35] occluded look. But in this case I wanted to be subtle.
[8:41] And that's basically it for the terrain.
[8:47] So there's only one thing I wanted to share to finish this video.
[8:53] Which is as you can see the texture of this cliff won't really hold up even for
[9:03] mid-distance. So what we can do is separate the cliff from the terrain. And if you remember
[9:14] we have that attribute in here. We have that point attribute which is the mountain.
[9:21] As you can see we have it here. So we can split the mountain after converting the attribute.
[9:35] And isolate it. And we keep the terrain in here.
[9:43] And then we can merge it over the top.
[9:51] And in this case I am just what remashing the cliff. So we can get some displacement at
[10:02] render time using the new triplaner node in the 20. And I am doing that just by
[10:10] probably reducing in this case in a loop. And then what remashing it we get some nice
[10:22] result, nice quad mesh. And then in the salaries I can target this specific geometry.
[10:32] So as you can see we have the idtl terrain and good topology cliff so that we can
[10:45] displace it at render time. So yeah that's basically what I wanted to share with you today.
[10:53] And I hope you have taken something out of this. Again if you want more details on the
[11:01] idfield material and all the other Pegasus nodes I encourage you to watch that master class or that
[11:11] series of tutorials. It's definitely really interesting and informative. So if you want to
[11:20] grab the file feel free to do it on my Patreon page and I'll see you next time. Thank you.



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

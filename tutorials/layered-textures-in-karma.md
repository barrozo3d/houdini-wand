---
title: Layered Textures in Karma
source: YouTube
url: https://www.youtube.com/watch?v=GQMsl6TiFXY
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/layered-textures-in-karma/
frame_count: 0
frame_status: pending-selection
---

# Layered Textures in Karma

**Source:** [YouTube](https://www.youtube.com/watch?v=GQMsl6TiFXY)
**Author:** cgside
**Duration:** 8m26s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py layered-textures-in-karma <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in today's video I wanted to introduce you to a new node I'm releasing for Karma and
[0:05] MaterialX, which is this LayerX node.
[0:09] It's a native MaterialX node, so no subnet or something like that is really I compiled
[0:13] it for MaterialX and Karma, and it allows you to layer different textures over your diffuse,
[0:19] your albedo, your roughness and what not even for displacement.
[0:23] It works.
[0:24] So for example, I have this graphite in here.
[0:25] I can disable or I can change the blending mode to a normal, or in this case I'm going
[0:30] to set it to overlay.
[0:31] We have possibility for alpha blending and you have for example I can enable in your
[0:36] new layer and blend it a bit with the previous ones or change the blending mode.
[0:43] So but yeah, we will be back to this in a minute.
[0:45] Now let's look at the first I wanted to share the initial setup that I did for this
[0:50] scene.
[0:51] So I just don't promote this.
[0:52] I'm going to give you some tips before that.
[0:55] So let's go to the Geocon text.
[1:00] Any near, if you remember we modeled this water tower previously on a video and I wanted
[1:05] to give it some textures.
[1:07] So for just to clean it up a bit, I'm going to delete most of the attributes and I only
[1:15] have normal and UVs.
[1:16] Then I use my HGA to orient the UVs up and do a basic UV layout with these settings.
[1:22] Then I do a connectivity in here.
[1:24] So in this case, I didn't save a name attribute for the different parts and I really need that
[1:29] for shading later.
[1:31] So as you can see here in the trust for example, it has all different pieces and the same
[1:36] for the leather.
[1:37] So what I did in here really quickly was to using the class attributes that I saved on
[1:43] primitives.
[1:44] I'm isolating the different parts just by pressing 9, just by entering this, pressing 9 and
[1:51] selecting by class and then I selected some of them and I'd each section.
[1:57] So the trust, the leather, but for that I also did an exploded view so I can easily select
[2:03] the different parts.
[2:04] Then I disable it and I select everything, including the ceiling, the body and the body
[2:08] B.
[2:09] Now I run a python script that basically looks for all the visibility nodes in the inputs
[2:15] in all the notes in the previous nodes and reads the group parameter and set the data
[2:22] attributes with those values of the group.
[2:25] So something like this.
[2:27] So in here we have an array and in the first element we have the first selection and so
[2:32] on.
[2:33] Then it's easy.
[2:34] We set a new visibility node just to show all the primitives and we set a new class based
[2:39] on that visibility groups array.
[2:42] Basically checking if the current prime number is in the selected group that we are iterating
[2:47] over and assigning the class to a new class that I'm just using the iterator in here.
[2:54] So that's basically it.
[2:55] That's how I'm cleaning up and this can be useful to isolate different parts as we will
[2:58] do in shading.
[3:00] Then I'm just cleaning again some attributes, doing a soft and normal, setting a basic name
[3:05] and outputting the cache.
[3:09] In a copnet I also did something a bit specific because if we are going to procedural
[3:13] shaders in Solaris we don't have access to many nodes like ambient occlusion and
[3:19] be ready dirt for example which is a very useful node in be ready.
[3:22] We don't have that kind of luxury.
[3:24] So it's a good idea to set up a copnet and in this case I'm baking some attributes like
[3:31] ambient occlusion for example as you can see and I can use that in shading so I'm creating
[3:36] an output for the AO but no that I can reference and that way I can use it in Solaris.
[3:43] You could of course output curvature, edge, cavity and all the other maps but for example
[3:47] position and world normal we have that in Solaris so we don't need it.
[3:51] In this case I did a quick and dirty job and I'm just using occlusion and it's not even
[3:56] that noticeable.
[3:58] So that's about it for this setup.
[4:00] Hopefully I run through pretty quickly but you can have a look at the file on Patreon
[4:05] and you will be able to go through more slowly.
[4:10] So let's go through the Solaris.
[4:12] In here I'm just importing the geometry and creating a dome light and some render settings.
[4:19] So for the material let's quickly have a look.
[4:23] So these material X node, the layer X node you can find it.
[4:27] Let me see here on material X and compositing and you will find it here.
[4:30] So it's a native material X node as I told you before and it's pretty simple.
[4:35] So let me disable all these layers.
[4:42] You have, I also have some roughness in here but that's not really that important right
[4:47] now.
[4:48] So besides that we have a base that we can set to a different color and then we can enable
[4:53] a new layer and in this case I'm loading an alpha so you can see in here.
[4:58] I don't have any color.
[4:59] The color is set here so I can set it to a different color for example.
[5:02] But as an alpha I'm loading from a mega scan structure which is this one.
[5:07] I'm loading the texture, doing some color correction and then just playing with the range as
[5:11] you can see.
[5:15] So now I did karma see you sorry.
[5:17] So that's pretty simple.
[5:19] I'm just loading that as an alpha and I can play with the color in here and pick the
[5:23] color I want.
[5:24] So let's say it's this.
[5:26] Then we have another layer.
[5:27] So layer two we enable that and that just goes as color arrest texture in this case from
[5:34] mega scans also and as an alpha I'm using a tri planner which looks something like this.
[5:42] So that's my alpha and we need to restart the render because this visualized node is
[5:47] broken in node in it 21 for some reason.
[5:50] So that's why so we have layer two and of course we can change the planning mode.
[5:54] So for example to overlay or to multiply but since we were using an alpha that's not
[5:59] really that important in here.
[6:01] Then I'm loading in here a grid texture.
[6:04] So let me make that really noticeable.
[6:07] Basically is the let me see where I have that is the grid node.
[6:12] So let's see it's a grid node that I just added some fractal to break out the edges.
[6:18] Then I do I X route only one channel and I multiply it over my class.
[6:24] So in here I'm reading that class that we created converting to a float and doing if equal.
[6:29] So for example I'm comparing to this value in here.
[6:33] So if class two I want to mask around that different section in this case is the class
[6:38] number one.
[6:39] So I'm just outputting white or black depending on the class.
[6:42] So it looks something like this.
[6:43] So I can change in here which section I want to target.
[6:47] And of course I did a pretty simple job in this section with all this information and
[6:51] more cops baking.
[6:52] You can you can elaborate as much as you like.
[6:56] So let's keep enabling this in this case I'm just reading the ambient occlusion in here.
[7:00] So yeah I can actually play with that.
[7:03] So let me make that even more noticeable with the range node.
[7:07] So I'm just reading the ambient occlusion in here.
[7:09] Then we have the graphite.
[7:12] So let me set that to normal and that is in here.
[7:17] So I'm just loading some graphite decals I have I bought on art station and I'm since
[7:23] this is a PNG image with an alpha I'm setting it to color for and using the place node just
[7:28] to place it where I want with the offset and scaling it up or down in this case and making
[7:33] sure I set the address mode you and V2 constant so it doesn't repeat around.
[7:37] Then I'm extracting the alpha in here with a separate color for and using that as an alpha
[7:43] in the layer five as you can see in here hopefully it's visible.
[7:47] Then I'm just multiplying down a bit the alpha since I don't want so much blending so
[7:51] as you can see and you can set that to overlay and play with the alpha so just some post
[7:56] process and we get the sort of result.
[8:00] So yeah guys I'm really thinking this for Patreon if you want to grab it and I'm also
[8:07] releasing this scene there if you want to have a look on how I did all of this setup.
[8:11] Of course this was pretty quick and dirty you can do a much better job but I find these
[8:15] nodes pretty useful if you want to layer up to different textures and effects so let
[8:21] me know your opinions in the comments and I hope to see you next time.
[8:24] Thank you.



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

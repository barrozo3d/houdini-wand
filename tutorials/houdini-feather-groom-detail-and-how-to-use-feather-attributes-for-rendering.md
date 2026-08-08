---
title: Houdini Feather Groom Detail and how to use Feather Attributes for Rendering
source: YouTube
url: https://www.youtube.com/watch?v=kSIn2FCzW0c
author: Alexander Weber
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering/
frame_count: 0
frame_status: pending-selection
---

# Houdini Feather Groom Detail and how to use Feather Attributes for Rendering

**Source:** [YouTube](https://www.youtube.com/watch?v=kSIn2FCzW0c)
**Author:** Alexander Weber
**Duration:** 7m31s | 2 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-feather-groom-detail-and-how-to-use-feather-attributes-for-rendering <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### How to use the Node [0:00]
**Transcript (timestamped):**
[0:00] So you created your beautiful feather using the feather template, maybe also the feather width, and then you try to create some more detail with the feather noise and feather clump, but this just wasn't enough, and that's why I created the feather boom detail.
[0:18] So you're just gonna throw it down and right off the bat you could adjust the shaft width, but yeah, you don't have to, and then let's just dive inside. So the way this works is that it just decomposes everything, it's not like a workflow that I came up with, but it's just out there and this not just implemented quite well.
[0:43] So you now have curves, and with those curves obviously you can use all of Houdini's tools to adjust them and shape them in whatever way you want, and for example there's guide process and all the Gumi nodes which work quite well with this, so you can just plug this in, maybe connect everything.
[1:02] So now you can see already those just adjust the length, and if you go back up and look on this node, you already have this detail on there, and yeah, with these examples that I plugged down, you can just copy them over and then adjust them or you can come up with stuff on your own.
[1:22] So let's plug this in. So one thing that I noticed, and I don't know why because I'm not that much of a Guma, you can grab this, is that you also need to connect the shaft as the skin up here, and for whatever reason then those nodes work again.
[1:39] So as you can see here I did the hair gen and then just bend those hairs and in the end use the hair clump to get this detail onto my barbs, so you don't want to change the number of barbs you have and the point count and whatever, this just doesn't work.
[1:59] So if you are going to do some heavy adjustments like I did here, then you always have to use a node that transfers those adjustments onto your actual barbs. This is what the hair clump node does for me right here.
[2:12] And sometimes you might also want to split which hairs you're just going to affect, so this is a way to split. Then you also have mask which basically do the same but yeah, sometimes you need this and sometimes you need that.
[2:27] Then you can also do random groups and frizz and whatever, you can just adjust those curves in whatever way and this node will transfer onto the visualized barbs.
[2:41] So this is basically already it. There's another feature which I'm going to quickly show. I have one prepared here. Let me just disable this again. So this is also not something which I spent too much time achieving, but we can also have a quick look inside.
[3:00] So yeah, that's basically the same I guess. And over here I actually used the split node and then I guess I'm just adjusting the barbs down here and merging them back together.
[3:14] And yeah, this just transfers everything over here. And then sometimes you want to take an image and basically work on that image. These images you can find easily on the featherbase.info.
[3:29] It's like a nice website where you can, if you know the names of the biological names or whatever the science of birds is called, you can search them up and then choose the bird that you want.
[3:42] Let's take this one and then you get all the feathers. So if you want to make a specific bird then this website is really nice to see how the feathers of these birds look.
[3:54] And yeah, so sometimes you take the image and want to base it on that. So you can plug the image in here. This is just a cup network that you just do a file and then sometimes you have to adjust the rotation a bit and whatever.
[4:07] So and then if you are doing that, I have this little checkbox which enables quickshade and then you get this image onto your feather.
[4:16] This already creates the UVs in a way that those images will always fit your feather.
[4:21] And in case you don't want to use it for rendering in the end because this obviously doesn't look too good, then you can also create your own UVs with the normal projector V-node which is included in here.
[4:33] That's already basically it. Be free to ask any questions if they come up and maybe this node is also not perfect. I haven't tried it around with it too much so it could be that they have some flaws in it. Just let me know.


### Using Attributes for Rendering [4:45]
**Transcript (timestamped):**
[4:45] So I just realized that I haven't talked about this channel yet and how to transfer attributes that aren't usually on your barbs onto your barbs. So I'm going to real quick show you how to do that.
[5:02] So I just took a few as an example. So just resample nodes then you get this nice gradient from root to tip of your barb.
[5:10] Obviously if you do this, don't ever actually resample those. I mean you could but we don't want to do that because this probably breaks some stuff. I haven't actually tried it.
[5:21] But there's no need to do this. You can do the upstream so don't do it.
[5:26] And yeah I did that on both sides obviously. So then if we go up, you might be wondering, okay there's no curvy on here and this is what this channel is for. So just plug curvy in here and then this automatically creates the curvy which in this case goes from root to tip of the shaft which is not really what we had inside.
[5:52] But it also creates curvy for barb L and barb R so left and right side. Sadly you cannot really inspect this here but this is also true for the width and the UVs.
[6:03] All those channels, okay obviously UVs is different but yeah if you have a channel that's on barbs you cannot really inspect those.
[6:11] And you can just quickly import this into lobs and I'm going to show you how this setup works. It's just default feather setup but yeah.
[6:19] So just create a primitive for the feather then import your feather. Then we use the Houdini feather procedure. Then you use the feather primitive. Then your goom that you imported.
[6:34] One thing that I always do is uncheck velocity because I don't use the deforming of this node. If you use the deforming of this node then obviously you want the velocity but if you don't do it, use it then this will overwrite your velocity that you might have on your feathers already.
[6:50] And yeah that's going to cause some problems. Then you just have to plug the curvy in here. You don't need to add the barb L or barb R just a normal curvy and then this node knows how to convert those back to being a normal curvy.
[7:05] So you can just use this in a shader. So I just use the curvy, call it with a prim bar. This is render man but yeah I'm sure you know which nodes can do that for a karma or whatever else.
[7:19] And then if we hit up the renderer let's quickly do that. And you can see the curvy works while rendering. Yeah and that's basically it.



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

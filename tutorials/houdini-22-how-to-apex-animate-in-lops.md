---
title: Houdini 22 | How to APEX Animate in LOPs
source: YouTube
url: https://www.youtube.com/watch?v=-7aIsTQc6kg
author: Houdini
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-22-how-to-apex-animate-in-lops/
frame_count: 0
frame_status: pending-selection
---

# Houdini 22 | How to APEX Animate in LOPs

**Source:** [YouTube](https://www.youtube.com/watch?v=-7aIsTQc6kg)
**Author:** Houdini
**Duration:** 8m40s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-22-how-to-apex-animate-in-lops <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] In this video, we're going to learn how to animate APEX characters directly inside of Solaris or LOPs.
[0:09] So what we have here is just a very simple scene, just a few things from the asset browser and a quick floor with some COPs, textures, and some lights as well.
[0:22] Just to kind of give ourselves the impression of having a very, very cool scene and desperately wanting to animate our characters in that scene with our lights, etc.
[0:33] So to get started, let's throw down a SOC create.
[0:38] Alright.
[0:40] Now within here, I'm going to put down Electra.
[0:45] Okay.
[0:46] And let's make sure we're outputting an APEX character.
[0:50] So check this out. This is pretty interesting. If I jump out, right, press U and jump back into Solaris and flag our SOC create here, we get this.
[1:00] Now you might be asking yourself, what on earth could this possibly be?
[1:05] And if you're in the know how, then you realize that, yes, this is the actual APEX rig.
[1:11] So Solaris by default doesn't really know exactly what to do with APEX rigs, because it's all just packed geometry.
[1:21] And again, this is the actual rig, right? All of the rig logic is written to points.
[1:27] So by default, it's actually pretty cool looking.
[1:30] But by default, it Solaris just draws everything, right? The geometry, the skeleton and the rig.
[1:38] So Solaris doesn't know what to do with this.
[1:41] Okay, so we have to tell it explicitly what to do with that information.
[1:47] If you want to hide this, there's one little trick that you can do, right?
[1:51] So we can work within this node and not really necessarily worry about jumping back and seeing this kind of craziness.
[1:58] One thing I like to do is I just like to throw down a cube and put this into an output node.
[2:05] Okay, now it doesn't matter if this is flagged, right?
[2:09] Once we jump back out, that box is always going to be the output of this node.
[2:15] So it just kind of cleans things up a little bit.
[2:18] So now let's jump back into here and I'm going to put this into a null.
[2:22] You don't have to. It just kind of keeps things a little bit more tidy.
[2:26] And we'll call this Electra.
[2:29] We'll jump back out.
[2:33] And I'm going to put down an Apex character import.
[2:37] You can see that all this stuff is in beta at the moment, but it works.
[2:44] So we're going to actually take that null that we made and I just copied and pasted the null and just pasted it into here.
[2:52] Okay.
[2:55] Or let me see.
[2:57] I have to copy that and then paste it.
[3:01] There we go.
[3:03] So now we have that within our SOP path.
[3:06] We have our character ready to go.
[3:08] And now if I just merge this, right, the character with the actual scene, now I have that character in the scene.
[3:16] And I can put down an animate node and start animating.
[3:22] So now I'm in Apex. I'm in Solaris and life is good.
[3:31] So let's explore a couple different ways of how we can work with this.
[3:36] Some different workflows in combining SOPs and Solaris.
[3:40] So I'm going to exit the state and let's jump back into the SOP create.
[3:46] Let's throw down another Electra.
[3:50] I really like using Electra in this case.
[3:54] And we'll call this Electra B.
[3:58] So same thing as before. I'm going to take this null, copy it.
[4:03] And we're going to import that other Electra.
[4:09] Paste that into there.
[4:12] Let's see.
[4:14] Oops. I did not output the Apex character.
[4:21] Okay. Yeah, Solaris is explicitly looking for that Apex character.
[4:26] So now if I just drop this in the chain here and go back to my Apex animate, you can see that now we have two Electras in our scene.
[4:39] And now we're just building up our scene as we would anything else.
[4:43] We can add lights, we can add objects, or we can add entire Apex characters.
[4:49] Which is very cool.
[4:52] But let's say we actually just want to animate in SOPs and then import everything into Solaris afterwards, right?
[5:00] Kind of like round tripping the entire process.
[5:04] So we'll do it this way.
[5:07] Let's take our scene and I'm going to pipe it into the SOC create.
[5:11] And then once I jump into the SOC create, you can see that now I have just a very simple representation of my scene.
[5:17] Okay. So now I can animate in here with my objects, all that good stuff.
[5:25] So let's take these. I'm going to delete these two nodes.
[5:28] And I'm not going to need these anymore, right?
[5:31] So I don't want any trouble with those. So I'm just going to go ahead and delete those.
[5:36] Let's go back to the SOC create and we'll build out our Apex scene here.
[5:40] So we're going to do Apex add character.
[5:47] Electra goes into the second input and we'll say Electra A.
[5:55] Just drag that out and make another one.
[5:58] Call this Electra B.
[6:02] Cool.
[6:04] Now I can start animating here.
[6:08] Okay.
[6:11] Because SOPs, things might feel a little bit more snappy.
[6:14] Maybe you're just a little bit more comfortable in SOPs and you want to do all your animation here.
[6:18] It's perfectly fine.
[6:21] Right. So now we can animate these two interacting with each other.
[6:25] Something like this. You want to hold hands.
[6:29] Yeah, sure. Something like that.
[6:32] So now we have our animation, we have our scene, and we want to output this.
[6:37] So let's put this into a null.
[6:40] So we can set this path. So we'll say Apex scene out.
[6:45] I'll copy this, jump back up.
[6:49] And we're going to do the SOP import Apex scene, which is also beta.
[6:55] We'll flag that and we'll paste that into the SOP path.
[7:00] And we'll do this.
[7:03] And I can start animating below this if I'd like.
[7:07] Or I can just pass this into this merge.
[7:10] And now if I jump into the animate.
[7:15] And we lose that previous animation that we had before, because all of our information was baked onto this Apex animate node.
[7:22] So let's put down another one.
[7:27] Let me see.
[7:31] Okay.
[7:32] Exit the state.
[7:34] Do that.
[7:35] We'll jump into here.
[7:38] And let me try and reset the animation.
[7:41] There we go.
[7:43] Okay.
[7:44] Yeah, you just had to explicitly tell the animation node to just take in that animation.
[7:49] And you can see here that the actual base animation is grayed out.
[7:54] And that means we can't touch it, right?
[7:56] Whatever animation is playing on here, we can't actually touch that.
[7:59] So if you want to add animation on top of this, you just select all your controls and add a new animation layer.
[8:07] So just call it like fix or whatever.
[8:11] So now this is pretty slick because now we have all of our lights.
[8:14] We have our characters.
[8:15] We have our original animation.
[8:17] And now we can make some final adjustments if we need to within Solaris.
[8:23] With all of our lights in our scene and everything.
[8:26] Very cool.
[8:28] So yes, that is how you animate Apex characters, including multiple Apex characters within Solaris with your scene with your lights and all that good stuff.



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

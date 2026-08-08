---
title: Houdini 22 | How to Procedurally Deform Rigs
source: YouTube
url: https://www.youtube.com/watch?v=BRSJx1lWlJM
author: Houdini
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-22-how-to-procedurally-deform-rigs/
frame_count: 0
frame_status: pending-selection
---

# Houdini 22 | How to Procedurally Deform Rigs

**Source:** [YouTube](https://www.youtube.com/watch?v=BRSJx1lWlJM)
**Author:** Houdini
**Duration:** 8m33s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-22-how-to-procedurally-deform-rigs <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Everybody, in this video, we're going to learn about a very powerful technique within APEX, where you can take your animation out of APEX,
[0:09] apply procedural motion to your skeleton, and then bring it back into APEX for further animation.
[0:16] So, to start off, we can look at our scene here, and we just have Harry.
[0:22] Harry doing his little heel-pop-hello thing.
[0:27] So, to get to my APEX skeleton, there's a few things I need to do, because you might notice that even though I have this node selected,
[0:34] there's nothing I can do, I can't select anything, right?
[0:37] Because everything is still packed into my APEX scene.
[0:42] So that means I need to reach into that scene and grab certain elements.
[0:47] In this case, I need the animated skeleton.
[0:51] So, there's a nifty little node that you can put down called the Unpack APEX character, APEX Unpack character.
[1:02] So, now, within here, within the character name, we want to grab our character, which in this case is Harry.
[1:10] So, we have all these outputs coming out from this Unpack character.
[1:14] So, if you look at the first output, it's just passing through, right?
[1:18] It's just the APEX scene passing through.
[1:20] So, I could put down another scene animate, keep on animating, etc.
[1:26] The second is the rest.
[1:31] I don't want to null here. Let me try that again.
[1:34] So, the second is the rest. Okay, it's just the rest geo of our character.
[1:41] The third is the rest skeleton, and the last is the one that we're going to want to mess with, which is the actual animated skeleton.
[1:50] So, let's apply some motion to this.
[1:53] Okay, and in this case, I'm going to use an attribute bop, just to show you that we could really kind of do whatever we want here in this stage.
[2:02] Because, again, this is all just geometry.
[2:05] All of our skeleton is made up of geometry, of points.
[2:10] So, we can manipulate these points in any way that we want, and then pass it back into my rig.
[2:17] So, I'm going to jump in here, and let's put down an anti-aliased flow noise.
[2:25] Okay, we're going to plug the position of our points into the position of the flow noise, and then we'll just add it back into my position.
[2:37] I'll put that to the final position here. You can see that now we're getting this crazy looking thing.
[2:43] Let's make sure that within the flow noise, this is set to 3D motion.
[2:47] And finally, let's take our time, and we'll plug this into the flow value. So, now we get something like this. This nice animated motion.
[2:56] So, let's plug all of this into a bone deform, just so we can see what we're getting.
[3:03] And this is just a nice quick method of just seeing what it's going to look like in the final result.
[3:11] So, we get something like this. You can see that we're already starting to layer up our animations, right?
[3:16] You can see that that animation that we created before is underneath that wild procedural motion.
[3:24] So, this is already looking pretty cool, but we want to get back into Apex.
[3:29] So, let's actually animate this a little bit.
[3:32] I'm going to go into the amplitude, and I'm going to promote this parameter so I can jump up and I can animate this.
[3:40] I can set some keyframes on this amplitude here.
[3:44] So, I'm going to set this to 0.
[3:47] Now, what Harry does is a little pop. Maybe what we can do is sort of like jiggle a little bit, right?
[3:53] So, he lands his heels. I'll set a keyframe here.
[3:58] Go forward a couple of frames. Go to about 0.6, and then just turn it off.
[4:06] So, we get something like this. Dink. Something kind of weird, but I think we'll get the idea once we see where this goes.
[4:15] So, now we could see our animation, but we still can't animate this, right?
[4:19] We don't have access to our controls or our Apex rig.
[4:22] So, the next step is to get this animated skeleton back into Apex, right?
[4:28] With our layered procedural motion on top of it.
[4:33] So, we're going to use what's called the animation from skeleton.
[4:37] Now, this is a very, very powerful node.
[4:40] I use this node constantly, and it really just bridges this gap between the world of Apex and the world of SOPs or Kinefx, right?
[4:50] So, we can do all this procedural motion over here, right?
[4:54] Our nice procedural motion block, and then just plug it back into my rig, which allows me to continue animating later within Apex.
[5:04] So, I'm going to take this output here. That's going to go into the first input of our animation from skeleton.
[5:11] Now, we're going to get some errors for now, but let's just go over the actual node.
[5:16] So, we need our rig path, right? Which is going to be the hairy character base rig.
[5:21] Skeleton path, which is the base skeleton.
[5:25] And we can look at the actual frame range, and I'm actually going to cut it down.
[5:31] Let's look at the bone deform, and we only need about 150.
[5:36] And this node could take a bit of time, because it has to run through and take all that animation data and convert it to channel primitives, right?
[5:47] That something like Apex can actually read.
[5:51] So, it takes a little bit of time, but trust me, it's worth it.
[5:55] And the clip name, we're just going to leave it as default in this case, right?
[5:59] So, it's going to write that animation to the default clip on our scene animate.
[6:04] And the layer name is important, right?
[6:08] Because now we're going to add this animation to a new layer.
[6:11] So, let's call this, let's see, what can we call this?
[6:15] Just proc motion, right?
[6:19] Proc for procedural, and then just motion.
[6:22] And controls, we can specify the certain controls that we want to use.
[6:26] In this case, I'm just going to leave that blank, and it'll just apply to everything.
[6:31] All right, so let's grab our animated skeleton, and we'll plug that into the second input.
[6:39] Now, you can see that it's driving our animated controls, or rather, our rig.
[6:48] So, now let's plug this into a scene animate.
[6:51] Okay, we'll jump into the viewer state.
[6:57] Let's see, enter. There we go.
[7:01] Great.
[7:02] So, now we have our nice little procedural motion driving the animation.
[7:08] And again, it's on a different layer, so I can turn it off.
[7:10] I can mess with the weight, right?
[7:12] Maybe I just want a little bit.
[7:14] And I can even select all my controls at a new layer above.
[7:20] Call this fix or something like that.
[7:23] And then I can go in and start animating on top of this.
[7:27] So, again, the possibilities here are pretty limitless.
[7:32] You could do just about anything you want within this nice little golden section here, right?
[7:38] You pull out your animated skeleton, add some procedural motion to it.
[7:44] Animation from skeleton to apply to your apex rig.
[7:48] And then you just continue animating as you were before.
[7:53] And of course, all this could be turned into a tool if you'd like.
[7:57] Right? Of course, this could be turned into a tool, an HDA, that then you can put onto a marketplace, something like that.
[8:05] Or just have it your own tool or an internal tool within your team.
[8:11] But again, this is a very, very powerful workflow that allows you to apply procedural motion
[8:17] to your apex rig at any point.
[8:20] And it's very non-destructive, which is very nice.
[8:24] And it's very flexible and allows you to create interesting solutions for interesting problems.



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

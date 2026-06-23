---
title: week 02   07   starting the vellum sim v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=cecNdA8cLTo
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/week-02-07-starting-the-vellum-sim-v1-1080p/
frame_count: 4
---

# week 02   07   starting the vellum sim v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=cecNdA8cLTo)
**Author:** The VFX School Archive
**Duration:** 8m7s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Now let's drop a Valum configure cloth. There we go. Okay, I'll click this into the first inputs. You can see this generating constraints for us. Okay. Let's see, now we want cloth. Distance along edges is fine. Don't need a group. It's going to be the same for everything leave. These kind of doer, these work by defaults now as of Houdini 18. I think they work really easily for us. No, Houdini 17.5. I think this calculate varying and thickness really helps out. Okay. What else do we want? Are we going to set up these pin points? Okay, so that pin group we just made and this match animation is really important as well. So they follow around. Okay. So there's stretch stiffness. We'll leave that on. So that's really, really stiff by default. Now, something important here, the rest length scale. I'm going to drop this down to 0.8. Okay. So that means these want to be shorter than they are now. Okay. So the rest length is shorter than their current length of these constraints. So what that does, it means when the simulation starts, there'll be under tension. There'll be pulling on themselves, which makes sense for our simulation. It's a bridge with cables and the cables should be under tension. So that when they break, when they're released from the road, they spring up. And you know, kind of we get some nice behavior from that. Okay. So that's good. Good. This compression stiffness, oops, let me turn that back to 0.8. And I'm going to turn this compression stiffness, sorry, up to, up to pretty much the maximum value. So they don't kind of compress together. This bend stiffness, I'm going to raise this a bit, but not too much to, let's do to a million. Okay. Which sounds like a lot, but you'll see they'll, they'll still bend plenty substantially. In fact, okay. Now, let's drop an object merge and bring in the bridge. So the bridge simulation, bridge, sim, we want the bridge out, bridge, sim. Okay. Grab that and now connect this up to the collision geometry there. And we also want a vellum attached to geometry. Okay. Make sure to connect up all these. So there's our collision geometry coming through constraints. So similar to the Abidi workflow, but we only have the one line for the actual simulation geometry. We've got constraints and then a collision geometry on the right. Okay. So vellum attached there. So I think we'll need to unpack this geometry first for it to work properly. Yeah. We'll unpack it. There we are. And let's configure this. So we want it to not be connecting the whole thing. We need to kind of, let's do, let's see. There we go. Max distance. So turn on this max distance. Okay. So we're connecting this geometry to this geometry here to the collision geometry. Let's do a .01. Okay. So they're just connecting around the bottom there. That's fine like that. And then we want everything here is fine by, sorry, default. Let's, I'll put this group. Pull this. Attach. Okay. So that we can break them later or work on breaking them later. Yeah. Well, we do want to break them. So we'll turn this on. I'm going to drop that to .01. So that when they are stretched, when the stress on these constraints is beyond a certain amount, they'll break. Okay. So that's great. Let's drop our volume solver into the bottom here. Great. I also want to join into this at the bottom here into this element. Attach the s. Okay. Maybe I'll just copy this over just to make it a bit tidier. Okay. Okay. So let's take a look at what happens with that. So let's visualize those tests of geometry constraints. Maybe just play through this. See them, hopefully, breaking. I'm going to stop it and run a flipbook because it's going to be a pretty slow. Okay. Let's go back. Just run a flipbook from there. All right. I've stopped it there because what we can see is right. We can see the attached to geometry constraints there and just right away they're breaking, but nothing's coming free. Okay. They're still attached. Now, the reason that it is is because this geometry is intersecting the collision geometry down here. So we need that to be able to be released is it is actually going through the other geometry. So what we can do is use a something a attributes on this geometry to say that it can be released at, you know, at first anything that's intersecting at the beginning of the simulation once they're free after that they will collide again. So basically it's called disable external I think it is. So it's an integer because at I add disable external set that to two, I believe it was. So if we set it to one, then it will just won't collide with anything external at all. We set it to two, then it will be disabled at the beginning, but then once they're released, then they will collide with everything else still. Okay. So let's try that again. And yeah, let's just see if they they should just pop off now. So we're in another flip up on that. So now you can see at the beginning they are released, they fly up and you can see that they're under tension there. So I by setting the rest length to less than, you know, to less than one to point eight is going to be. As I said, they're under tension they just pop up a little bit. We obviously need to work on that. We don't want them breaking straight away like this. And we want a bit more of a lively break, you know, when they get pulled apart, we want them to fly up and bend and, you know, go all over the place. But we're on the right track so far.

**Frame:** tutorials\frames\week-02-07-starting-the-vellum-sim-v1-1080p\frame_000.jpg


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

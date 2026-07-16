---
title: Houdini USD RBD Procedural LOP in under 5 minutes
source: YouTube
url: https://www.youtube.com/watch?v=ixJvo0iShiM
author: the point and prim
ingested: 2026-07-16
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-usd-rbd-procedural-lop-in-under-5-minutes/
frame_count: 0
frame_status: pending-selection
---

# Houdini USD RBD Procedural LOP in under 5 minutes

**Source:** [YouTube](https://www.youtube.com/watch?v=ixJvo0iShiM)
**Author:** the point and prim
**Duration:** 4m18s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-usd-rbd-procedural-lop-in-under-5-minutes <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome. So over the last week I've spent my mornings doing some R&D into some techniques for appresing RBDs.
[0:08] I'll be featuring those techniques in a future video, but basically this involves doing a lower SIM which then influences a much higher SIM.
[0:17] As you can imagine this geometry gets heavy pretty quickly. Even in my R&D tests I'm hitting over 2 million points and that's not even production quality.
[0:26] Thankfully there is this magical node called Transform Pieces.
[0:29] If you've done RBD in any serious capacity before you will know all about it.
[0:34] It allows us to load our Render Fractura just once and then apply the transforms from a point cloud onto it.
[0:39] Wish us super efficient and lightweight on disk compared to saving the entire geometry per frame.
[0:45] Great so that's that problem solved and life is good right?
[0:48] Wrong. The problem rises when we start rendering this with Karma.
[0:54] Lops will convert this geometry into USD as soon as you import it into Solaris.
[0:59] Heavy geometry is fine if it's just a static frame but if you have a heavy effect sequence like this it will actually import and do the conversion on every frame which becomes really cumbersome.
[1:08] Thankfully side effects are thought about this and as built the Houdini procedural RBD Lop which emulates the behavior of Transform Pieces in Solaris.
[1:18] You would expect this node to work like Transform Pieces out of the box but sadly it doesn't due to some USD specific quirks.
[1:25] On top of this the documentation is convoluted and confusing.
[1:29] The good news is that we can summarize this entire document with just two Wrangles.
[1:33] I've got a fresh scene here with some Fractura Geo for demonstration purpose.
[1:38] I've got the Proxy Geo Sim here, the Hyrus Fractura that will be rendered on this side, and the RBD points which are being used to apply the transforms of the lower range.
[1:46] Usually we use the name attribute to retrieve the orientation and translation from the points so all we would need to do is make sure the attribute matches on both.
[1:56] When importing our geometry to Solaris both the path and the name attribute are reserved by Houdini for building the Prim hierarchy with path taking precedence and name serving as a backup.
[2:06] This means we can't just use the name attribute like always.
[2:09] Side effects build a workaround for this directly into the procedural in the form of the piece name attribute which is what the giant document is for.
[2:16] So let's build our version of this. Here I have my render Geo making sure it is unpacked.
[2:22] Then I have a Wrangle declaring the path attribute. In this case just slash Geo slash Taurus. Note that I still have the same name attribute here.
[2:31] We then use an attribute swap to move the name attribute into piece name. You can use whatever method you want just make sure the original name attribute gets deleted.
[2:40] In the other stream we've got our RBD points.
[2:43] In this Wrangle we are just fetching the path attribute from the first Wrangle and adding the points name attribute to it to construct piece name.
[2:50] Again making sure we clean up the original name using an attribute delete here. This means on the points we only have the piece name attribute which is the path attribute from the geometry plus the name attribute.
[3:00] Here is a recap of the attributes you will need along with a nice blurry screenshot of the note graph.
[3:07] Let's bring these elements into lots. We can import both these using SOP imports for now. Make sure to check the singrof to validate if your prim hierarchy is correct for your needs.
[3:18] Now drop down a Hedunny RBD procedural lump. Select the Geo prim in the RBD primitive field and the points in the point primitive.
[3:29] You also have the option to reference the points from SOPS or directly from disk with the latter providing large speed improvements with heavier simulations.
[3:36] The next most common question after doing this is going to be how do I get motion blur on this thing. Luckily that is easily solved with a render geometry settings node.
[3:45] Select the geometry itself and not the RBD procedural. If we plug in some lights and a material we can see that that is working as expected.
[3:54] If all of this is still not making sense, I am giving away the Taurus hip file for free on my gumroot so you can download that to inspected further.
[4:03] Link below. I hope you found this video helpful and good luck smashing some RBD shots. Bye for now.



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

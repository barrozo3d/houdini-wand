---
title: module i   week 02   17   fixing post sim fix and rbddisconnectedfaces node v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=R-ay-5fX_Os
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [rbd, post-sim, glass, disconnected-faces, blend-shapes, destruction, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p/
frame_count: 4
---

# module i   week 02   17   fixing post sim fix and rbddisconnectedfaces node v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=R-ay-5fX_Os)
**Author:** The VFX School Archive
**Duration:** 10m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Right, so to demonstrate the glass thing, so to delete those primitives there, we need to, well, you don't need to, but I find it easier to show with if we apply a shader to it. So I'm just going to quickly make a glass, a principal shader with the glass preset, turned on, okay, I'm just going to call this glass, just leave it at that, you know, we're not wearing it's just to show you, I'm also going to hide all these for a moment. Maybe let's drop a quick environment lights as well. Just again, just for visualization, right? Okay, give it avert, let's jump in here. Yeah, so right away you can see we got the metal there, so we need to delete that because we've already, you know, we've done everything we need with the metal. So on the points and it's going to be name is, it was just a big metal we want to get bread off. So name is big metal. Goodbye, okay, and yeah, keeping the small metal bits and the wood and the glass. So good, and then let's split the glass. So name is glass. And this needs to be, I don't know why we have to select the group for it to work there, okay. Cool, and then the material, give it that glass material. And there we go, so we can see the cracks there now. And now if I, trust my RVD material, no, connect disconnected faces, that's the one, connect that up, we don't see anything yet. We need to set this to smooth shade it so we don't actually see the polygons at all, okay. And now if we come here, we don't see anything yet. And if I, I hope, cross my fingers and go to delete connected, there we go, they disappear, right. So this is transparent, you can see that we're looking through the top. And then as I progress forward, as I progress forward, you can see those polygons come in, okay. So that's what we can great, if I, and then if I turn this off, you can see them kind of popping in and out, right. So that's great. And now for the wood, I'm just going to drop a null here to visualize the wood. And I want to show you something, I'll need to split out actually, just the wood as well. So I'm going to come here and say, that name is wood. Okay, and then if we visualize that, set that to points again, there we go. Okay, I'm actually going to invert it, just because I want to, you know, we need to do some, some stuff on the wood here. So if I come, if we watch this, and then if you notice, see, when the wood breaks, it kind of joltes as a funny bounce to it, which doesn't look very natural. So I want to try and get rid of that. So what we're going to do is blend between two frames that we like. So about here and here, okay. So we're going to get rid of the animation between it and blend between the two, which will look much smoother. So what we need to do, I'm going to grab a time shift, set this to clamp to last, delete this channel and set it to 41. So what this will do, it will play all the animation normally up until 41 and then stop there. Okay, and then we're going to drop another time shift and turn that the clamp off, delete this channel and set it to, let's see, I think for him, 44 is good. And then we're going to blend between these two, right? So I'm going to drop a blend shapes underneath. And you notice now what I can do is blend between the two and the more in a smoother way, right? And you can see it's blending with between the rotations as well, not just the point positions. Right? So, yeah, and then I'm just going to animate this value. So from frame 41, which is what I've got here, give it frame 41, set the key frame there and then the other one was 44. Set another key frame here and we watch that, but I don't want the, you know, we'll have an ease in the notes. We go to animation editor, press H, I don't want this curve, so I'll just set this to linear. Great. And then, so to get that back to the normal, same after frame 44, we'll just use a switch and just put in dollar F, more than 44. Okay, so when the frame is more than 44, we will switch over to this input and it will continue as normal. Okay, so if you notice there now, the difference, maybe if I template this, hopefully we'll see the difference there now. So you'll see, oh no, because, it's because we're, yeah, we're viewing the other outputs. I drop a null on this, template that. There, you can see that jump there, which is templated and we don't have that. We've got a nice smooth simulation now. Okay, so that's great. We can merge these together. We've got the glass, the wood and try and make some space and the metal bits here. Right. Let me try and just make this retire here, maybe like that. And then the collider, let's maybe, we'll probably want to give some color to everything as well. So make the collider black. I'm also going to unpack it. So I think everything else is unpacked. Give it some normals. Open that over and subdivide it, just to smooth it out a bit. Okay, the color there's not coming through, put it after the unpack. There we go. Looks good. And then we can merge that in. These over. Just tidy up these wires a bit. And then, let's merge everything together. Obviously, you'd want to be setting up your materials on the other components as well. Maybe for now I'll just set up some colors. So on the metal here, let's do like a gray. And then we've got the glass on the other side. So I'll copy that material for the glass here. I've stolen that, put it back there. And then for everything else, let's do, let's get the glass for this. Oh yeah, let's do a color for the wood. Some kind of woody color. Something like that. Looks good. And then for the other metal pieces, maybe blue, why not? Okay. Change lighting. Well, put it on something a bit more simple. There we go. And then visualize that down here. So we've got some, we had normals going on with this. Let me set up. Where's that? We'll pack there. Because of this color for some reason. We'll just set it to white. There we go. There we go. And then we have it. Everything there together ready to, well, if you want to set up your materials obviously, ready to go. Let me zoom in a bit. We'll do a final playblast of this. Just see how it will work. Come on from about there. It's fine. I do find it a bit weird. You know, if I turn this, we could try it on this mode, but I kind of like it like that. And then just wait for that playblast to come out. Flipbook, sorry, not playblast. There we go. So that's all done. Assume in. So I'm focusing on the woods now. So you can see we don't get that weird popping anymore. It's just kind of, it's a bit, it's much smoother. You can play around with that. And also if you find any other pieces, maybe like this chunk of glass there, it's kind of vibrating. You know, if you wanted, you could use the same technique on that. We just grab that specific piece or anything else. If you find that, you know, in the metal breaks, it does kind of pop. But, you know, I kind of like that. I think it would happen in real life anyway. And I really like how, you know, we've got this, the bits of wood kind of just breaking in the middle there. The glass is settling on the floors we said before, but yeah, it looks good.

**Frame:** tutorials\frames\module-i-week-02-17-fixing-post-sim-fix-and-rbddisconnectedfaces-node-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Post-sim finalization: RBD Disconnected Faces node progressively reveals fractured glass faces over time (delete-connected hides interior faces until they're exposed by breaking); Blend Shapes trick between two Time Shifts smooths out a jittery wood break; final merge of glass/wood/metal/collider with materials and colors.

### Summary
10m44s finishing lesson for the Week 2 bus stop project. Covers: splitting geometry by name attribute into metal/glass/wood streams; RBD Disconnected Faces node (set to "delete connected") for progressive glass crack reveal; blending two frozen simulation frames with Blend Shapes + animation + Switch to fix a jarring wood jitter at break moment; final merge of all components with materials/colors and flipbook preview.

### Key Steps

**1. Split Geometry by Name**
- Delete by expression: `name == "big_metal"` → removes the heavy metal (already handled)
- Split node: `name == "glass"` → separates glass stream; assign glass shader
- Split node: `name == "wood"` → separates wood stream

**2. RBD Disconnected Faces (Glass Crack Reveal)**
- Node: RBD Connect Disconnected Faces (after glass split)
- Set to "smooth shade" display mode to see effect properly
- "Delete connected" option: interior faces hidden when fragments are touching; visible faces appear as glass cracks/breaks
- Result: glass looks intact at start, cracks progressively appear as fragments separate over time

**3. Wood Jitter Fix (Blend Shapes Trick)**
- Problem: wood breaks with a jarring jolt/bounce at the break frame
- Solution: isolate the problematic frame range (e.g., frames 41–44) and blend through it smoothly
- Time Shift A: `$FSTART = 41`, "clamp to last" → holds frame 41 (state just before break)
- Time Shift B: `$FSTART = 44`, clamp off → plays from frame 44 onward (state just after break settles)
- Blend Shapes: blend between Time Shift A and Time Shift B; animate blend value 0→1 over frames 41–44
- Animation editor: set blend curve to linear (remove ease-in/ease-out)
- Switch: `$F > 44` → after frame 44, switch back to normal sim; before 44, use blended result
- Result: smooth transition through the break moment, no pop/jolt

**4. Final Assembly**
- Unpack collider geometry → Add Normals → Subdivide → color black
- Assign colors per material: metal = gray, glass = glass shader, wood = brown, small metal = blue
- Merge glass + wood (blend-fixed) + metal bits + collider → out_final
- Flipbook/preview full sequence

### Houdini Nodes / VEX / Settings
- **Delete SOP by Expression** — `name == "big_metal"` etc.; filter by name attribute per geometry stream
- **RBD Connect Disconnected Faces** — hides interior (connected) faces of glass; "delete connected" = progressive crack reveal as fragments separate
- **Time Shift SOP** — freeze/clamp to specific frame for blend shapes trick
- **Blend Shapes** — interpolate between two geometry states; animate blend value 0→1
- Animation editor: linear interpolation (remove default ease curves)
- **Switch SOP** — `$F > 44` expression to revert to normal sim after blend window
- **Unpack SOP** → **Normal SOP** → **Subdivide** — finalize collider geo for render
- Principal Shader → glass preset for glass visualization

### Difficulty
Intermediate

### Houdini Version
H18.5

### Tags
[rbd, post-sim, glass, disconnected-faces, blend-shapes, destruction, intermediate]

---

## Related Tutorials
- module-i-week-02-15-starting-the-post-sim-setup-v1-1080p1.md (post-sim setup)
- module-i-week-02-16-point-deforming-the-metal-and-glass-v1-1080p.md (point deform step)

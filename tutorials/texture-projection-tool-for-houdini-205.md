---
title: Texture Projection Tool for Houdini 20.5
source: YouTube
url: https://www.youtube.com/watch?v=t9ldXkD7oqA
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [hda, python-states, cops, texture-projection, uv-less, tool-development, product-packaging]
extraction_status: complete
frames_dir: tutorials/frames/texture-projection-tool-for-houdini-205/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Texture Projection Tool for Houdini 20.5

**Source:** [YouTube](https://www.youtube.com/watch?v=t9ldXkD7oqA)
**Author:** cgside
**Duration:** 5m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in today's video I wanted to share with you a tool that I've been developing for the past week.
[0:09] It's basically a texture projection tool that works with cops in the background.
[0:15] And yeah, I'm gonna be demoing this tool and let's see how it works.
[0:23] So one thing I should warn you about is that this tool is still in beta as you can see from the name.
[0:29] And there might be some potential issues mostly with the umduke you.
[0:35] I try to figure that out, but it's one of my first times developing such complex tool with Python states that there might be some issues.
[0:43] And if you have a bipolar geometry, these might not be the fastest tool.
[0:48] So I'm gonna enter and you will have a check saying all good if you have vertex UVs and know your deems.
[0:53] So this tool doesn't support your deems unfortunately because cops doesn't support your deems and these runs on cops.
[0:59] So I'm gonna place a texture and I'm gonna write away change this to another feature I have in here.
[1:06] So in this case the old in a logo, I'm gonna hold control and rotate it.
[1:11] And maybe go in the front view and scale it.
[1:15] And as you can see, it will clip in here so you can play with max distance.
[1:19] This is just a mess so it doesn't project on the back as you can see if I reduce this.
[1:25] So if I increase instead, it will project on the back.
[1:29] It's still a working progress. So I'm gonna increase this a bit and make sure it doesn't project.
[1:34] Yeah, and I'm gonna scale this a bit down.
[1:37] And that's fine. Now I can place another point.
[1:40] And you can also change the near point radius which means that will grab that point as you can see.
[1:46] And if you are close to a point, that's the radius you have in here.
[1:51] If you want to place, if I reduce it, I can place one in here as you can see.
[1:55] Now this is, I'm using left mouse click.
[1:59] Left mouse click and drag.
[2:01] And I can use middle click to remove the projection.
[2:04] So I'm gonna change in here the texture.
[2:07] So I'm gonna use this one, let's say, or another one.
[2:11] So I'm gonna bring this in here and shows maybe this one.
[2:15] And scale it down and drag it.
[2:18] So now the near point radius is too small. So I'm gonna increase it and drag it.
[2:22] As you can see, it's not the fastest tool in the world, but it can help you out in some situations.
[2:28] I'm gonna scale this low go out.
[2:30] So it's also lower resolution right now.
[2:33] You can increase the resolutions to one K, let's say.
[2:37] So I'm gonna place another one in here and pick, let's say this one.
[2:41] So I can increase it or decrease it, drag it around and you can always go back and drag this one in here.
[2:47] And hopefully the undo will work.
[2:49] So I just placed a point. I'm gonna control Z and control Y to redo.
[2:54] So that should work.
[2:56] And in some situations, it might not work perfectly.
[3:01] So for those situations, what you can do, if I can place this one, I'm gonna scale it down.
[3:09] You can just remove all and it will reset the tool or I can undo and we'll have it back.
[3:14] So that's basically it.
[3:16] Now you have a path to the to the cop network that you can copy with this button.
[3:22] And you can just place these on your image texture in salaries, but make sure you make it transparent.
[3:29] So you can overlay these over other textures or materials, what not.
[3:35] And you can also change the background color just for visualization purpose.
[3:40] And you can also turn on and off the projections just to just to preview it.
[3:47] You can also change the texture, play with the scaling here.
[3:51] And you can enter manually the rotation if you want.
[3:54] So if I change this to zero, I want that at 90.
[3:58] And it's cool because you can come in here and drag it, scale it and rotate it.
[4:04] You name it.
[4:05] So that's basically it.
[4:07] You can grab the tool on my Patreon.
[4:09] I'm gonna be sharing for free with all the Patreon supporters.
[4:14] I can show you in salaries.
[4:17] So I'm gonna move these to salaries.
[4:19] Hopefully this doesn't crash my own.
[4:22] And as you can see, I have in here a demo scene.
[4:25] And the way I'm bringing that tool is by bringing the textures is by grabbing the.
[4:31] So let me pin this.
[4:33] I'm just going in here and I can just copy this one.
[4:37] So we can change it.
[4:39] And in the material, I'm just loading a material like the image and I can paste it in here.
[4:45] And hopefully this will change.
[4:47] So let's make sure.
[4:49] Oh, it's not in here.
[4:51] Sorry.
[4:52] This is not the material which one it is.
[4:53] I didn't name this.
[4:54] So I don't know which one it is.
[4:56] Let me change this.
[4:58] So is this one.
[4:59] Yeah.
[5:00] And as you can see, it's bringing with transparency.
[5:02] And I can use a mix to place another color in the background.
[5:06] If you render and don't forget you can increase the resolution at the end.
[5:10] So that's how you.
[5:12] Why is this this color?
[5:14] I'm wondering.
[5:16] Oh, I believe I know why because I didn't make it transparent.
[5:22] So if you come in here and make it transparent, now it should load the background color as you can see.
[5:27] And it will overlay.
[5:28] It will merge over the top.
[5:30] The base material.
[5:32] So yeah, that's basically it.
[5:34] Hopefully you found this cool.
[5:36] And as always, you can grab the scene files.
[5:39] I'm going to share this bottle model I did on Patreon.
[5:42] So you can play around with the tool.
[5:44] And if you find any bugs, especially the Patreon supporters, where I will be sharing this beta tool.
[5:50] If you find any bugs, please hit me up and let me know so I can potentially fix it.
[5:56] That's basically it.
[5:57] Thank you.
[5:58] And I'll see you next time.



---

## Captured Frames

- [1:05] tutorials/frames/texture-projection-tool-for-houdini-205/frame_000.jpg
- [1:35] tutorials/frames/texture-projection-tool-for-houdini-205/frame_001.jpg
- [2:23] tutorials/frames/texture-projection-tool-for-houdini-205/frame_002.jpg
- [3:20] tutorials/frames/texture-projection-tool-for-houdini-205/frame_003.jpg
- [4:20] tutorials/frames/texture-projection-tool-for-houdini-205/frame_004.jpg
- [5:40] tutorials/frames/texture-projection-tool-for-houdini-205/frame_005.jpg

---

## Structured Notes

### Core Technique
Demo of a custom, interactive **texture-projection HDA** (built with Python States) that lets an artist click-drag-drop label/logo textures directly onto a UV-less 3D bottle mesh in the viewport, with the actual projection compositing happening under the hood in **Cops** — no manual UV unwrapping required.

### Summary
This is a tool demo/showcase rather than a from-scratch build tutorial: the presenter walks through a beta HDA that projects flat textures (logos, labels) onto arbitrary geometry interactively. The tool checks the input mesh for vertex UVs and no UDIMs (a "check" indicator shows "all good") since the underlying compositing runs in Cops, which doesn't support UDIMs — meaning highly non-planar or UDIM'd geometry isn't the fastest use case. Interaction is fully viewport-driven: left-click-drag places and moves a projected texture, holding Ctrl rotates it, scaling is done by dragging handles, Max Distance controls how far the projection reaches around curved geometry (too low clips the projection on the front face only, too high wraps it onto the back), Near Point Radius controls how close the cursor must be to an existing placed point to grab/edit it versus placing a new one, and middle-click removes a projection. Multiple textures can be placed independently (different logos/labels at different scales/rotations/resolutions, e.g. up to 1K), each keeping its own settings editable after the fact by dragging its handles again. Standard Ctrl+Z / Ctrl+Y undo/redo is supported, and a "Remove All" button resets the whole tool if a placement goes wrong. The tool exposes a copyable path to its internal Cop network output node, which is then wired directly into an Image texture node inside Solaris/Karma (with the source geometry material set to transparent) so the projected decals overlay cleanly on top of any other base material — demonstrated live by importing the projected bottle into a LOP network, loading it into a material's transparent Image node, and confirming the projected logo renders correctly blended over the base packaging texture.

### Key Steps
1. Apply the (beta) Texture Projection HDA to a mesh; confirm it reports vertex UVs present and no UDIMs (a requirement since the tool composites through Cops internally, which doesn't support UDIMs).
2. Left-click-drag in the viewport to place and position a texture projection directly on the mesh surface.
3. Hold **Ctrl** and drag to rotate the placed projection; drag the corner/edge handles to scale it.
4. Tune **Max Distance** to control how far around curved geometry the projection wraps — too low clips it to the front face only, too high bleeds it onto the back side.
5. Tune **Near Point Radius** to control how close the cursor needs to be to an existing placement point before it's grabbed for editing instead of creating a new projection.
6. Middle-click to remove an individual projection; use **Remove All** to reset the entire tool state, or standard Ctrl+Z/Ctrl+Y to undo/redo point placements.
7. Place multiple independent texture projections (different images, resolutions up to 1K+, rotations, and scales) on the same mesh, each remaining individually editable afterward.
8. Copy the HDA's internal Cop-network output path via its provided button.
9. In Solaris/Karma, load that path into an **Image texture node**, set the source material to transparent, and layer it over the base material so the projected decal composites correctly on render — verified with a live render showing the logo blended over the bottle's base packaging texture.

### Houdini Nodes / VEX / Settings
Custom HDA ("Texture Projection", beta) built with Python States for viewport interaction (click-drag placement, Ctrl-rotate, handle-scale, near-point-radius point-grabbing, undo/redo), internal Cop network for projection compositing (works around lack of UDIM support in Cops), Solaris/LOPs Image texture node fed from the HDA's exposed Cop-output path, transparent material setup for decal overlay.

### Difficulty
Beginner (as a user of the tool — this is a feature demo, not a from-scratch build walkthrough); the underlying HDA itself (Python States + Cops compositing) is Advanced, but that implementation isn't shown here.

### Houdini Version
20.5.

### Tags
hda, python-states, cops, texture-projection, uv-less, tool-development, product-packaging

---

## Related Tutorials
- [Quick CG integration with Houdini and Karma](quick-cg-integration-with-houdini-and-karma.md) — uses this exact Texture Projection tool to add an Houdini logo decal onto a bottle for a CGI-integration render.
- [Shoe Laces in Houdini VEX and Vellum](shoe-laces-in-houdini-vex-and-vellum.md) — shares the same Python-States-driven custom viewport-interaction HDA approach for artist-friendly placement tools.
- [Interactive tools with Houdini Python States - draw pts on geo](interactive-tools-with-houdini-python-states-draw-pts-on-geo.md) — companion Python States tool-development tutorial covering the underlying interaction pattern used by tools like this one.
- [Volume rays in Cops for Houdini 21](volume-rays-in-cops-for-houdini-21.md) — another custom Cops-backed HDA tool demo from the same channel.

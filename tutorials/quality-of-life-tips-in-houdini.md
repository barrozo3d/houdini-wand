---
title: Quality of life tips in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=iQql20c4Gio
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.701"
tags: [workflow, hotkeys, poly-hinge, connectivity, enumerate, selection-modes, matcap, viewport, quality-of-life]
extraction_status: complete
frames_dir: tutorials/frames/quality-of-life-tips-in-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Quality of life tips in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=iQql20c4Gio)
**Author:** cgside
**Duration:** 6m13s | 11 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back, in this video we will have a look at several quality of live tips in Odini.


### Start orientation picking: snap objects [0:06]
**Transcript (timestamped):**
[0:06] So let's say I want to snap an orient and object to the windshield of this took took.
[0:11] Going to set up the main model as reference by Ctrl clicking on the flag and drop a box in the network.
[0:19] Now I can enter the tool state by pressing enter and with a not key I can pick the location target and just let click.
[0:28] Finally I can resize my box and do any further modifications to it.
[0:33] And of course you can pick any location on the model.
[0:37] So the default dot key doesn't work on my keyboard which is Shift semicolon I believe.
[0:43] Just search for start orientation picking in the odd key manager and assign your desired dot key.


### Poly hinge node procedurally in Houdini 20 [0:51]
**Transcript (timestamped):**
[0:51] Okay now let's look at the new bolly engine node and how to set it up procedurally.
[0:56] I just created a circle and dropped the node and to enter the procedural mode you need to change it to position an orientation.
[1:06] I'm picking an angle of 90 degrees and you just need to move it in this case along X.
[1:13] The older way of doing this is by creating a few copies and divide the angle by the number of copies minus 1.
[1:21] Move the pivot and finally skin the shapes.
[1:25] And you can see we have identical results.


### Reorder your class attribute with enumerate [1:29]
**Transcript (timestamped):**
[1:29] Let's fill the shape and extrude the patch group so we can look at some more scenarios.
[1:36] So for that I'm going to create a connectivity node on the Prims and pick the patch in the include group.
[1:44] And we have now a class value for each part.
[1:47] Ready if we check the geometry spreadsheet we ended up with some random values.
[1:54] The easier way to organize them is by using the enumerate nodes with the mode set to enumerate pieces.


### Poly hinge with expressions [2:02]
**Transcript (timestamped):**
[2:02] Now enter the select tool and pick the custom class attribute as a filter.
[2:07] In this case I'm going to select the class with value of 2 and isolate it with the blast.
[2:13] Drop a new inch node and select again the same class.
[2:17] And when we set it to position and your orientation we have these default results.
[2:23] So what we can do is to pick the centroid of the isolated class and immediately we will have the polygon snap to that location.
[2:34] Finally we can adjust the position in Y to move it up.
[2:38] It might be a bit difficult at first to understand but in the end it should make sense.


### Smooth mesh preview in Houdini [2:45]
**Transcript (timestamped):**
[2:45] So with other odd keys the default keyboard combination for smooth mesh preview doesn't work on my keyboard.
[2:52] But as you can see I set up another key and I'm able to switch between the smoothed version and default.
[2:59] You just need to go to the odd key manager and search for subdivision.
[3:04] Then change the keys in my case I pick the keypad plus and minus.
[3:09] And if you press the on the viewport under the geometry tab you can change the level of detail for a smoother version.


### Selection modes tips [3:18]
**Transcript (timestamped):**
[3:19] Now let's look at some selection modes in Odini.
[3:22] You can double click to flood fill to connect the geometry but as I work with a tablet pen that doesn't work all the time.
[3:30] So for those situations you can press H and select to flood fill connected geo.
[3:36] To make our life easier we can select by 3D connectivity and easily select multiple pieces of geo.
[3:43] You can see I'm trying to select the battery but I was also picking geo on the back of the model and to avoid that you can enable select visible geometry only.
[3:55] And since this is a model I did in Maya and was exported with different pieces I also have an Olympic pet attribute which in this case is not very organized.
[4:06] But it's another option to separate organized and possibly apply different materials.
[4:11] And the last selection tip is on how to select between boundaries.
[4:16] I'm going to select this edge loop and another one on the right side.
[4:20] Now I can press shift edge in between and it will flood fill the selection.
[4:26] I can also press only H to select the polygons in between.


### Edit node and transform tools [4:31]
**Transcript (timestamped):**
[4:31] When working with the added node it can be frustrating switching between the select tool and the transform nodes.
[4:38] To avoid that you can uncheck secure selection and it will allow you to select even if you're using the transform tools.


### Camera and viewport tips [4:46]
**Transcript (timestamped):**
[4:47] Okay if you're in the camera tool pressing 1, 2, 3 and 4 will switch between camera views.
[4:53] But let's say you are on the left view and you need the right one.
[4:57] Well just press again the same key and it will alternate between the right and left views.
[5:02] Same for top, bottom and front back.
[5:06] Another common problem is when you accidentally tilt the camera and now you can't really have control over your tumbling.
[5:14] A quick fix is to press H and it will reset to the home view.
[5:19] Really useful odd key.
[5:22] To zoom into a region you can pick the region with control alt and drag.
[5:28] Another way to zoom is to double-left click on the part of the geometry you want to zoom in.


### Custom Matcaps in Houdini [5:35]
**Transcript (timestamped):**
[5:35] And the final tip is on how to use custom matcaps in Odinit to check your shading issues.
[5:41] You can enter the matcap mode and if you press D under the material tab you'll find a matcap texture
[5:48] and pick your downloaded matcaps.
[5:51] I have this from PixelFondue which work great in Odinit.


### Outro [5:54]
**Transcript (timestamped):**
[5:55] And that's about it, let me know in the comments if you learned something new and don't forget you can check out my Patreon page where I share all the project files from my videos.
[6:05] You can also find my procedural courses on Patreon shop, links below.
[6:10] Thank you and I'll see you next time.



---

## Captured Frames

- [0:10] tutorials/frames/quality-of-life-tips-in-houdini/frame_000.jpg
- [1:00] tutorials/frames/quality-of-life-tips-in-houdini/frame_001.jpg
- [1:40] tutorials/frames/quality-of-life-tips-in-houdini/frame_002.jpg
- [2:15] tutorials/frames/quality-of-life-tips-in-houdini/frame_003.jpg
- [2:55] tutorials/frames/quality-of-life-tips-in-houdini/frame_004.jpg
- [3:40] tutorials/frames/quality-of-life-tips-in-houdini/frame_005.jpg
- [4:20] tutorials/frames/quality-of-life-tips-in-houdini/frame_006.jpg
- [5:50] tutorials/frames/quality-of-life-tips-in-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
A grab-bag of eleven viewport/workflow quality-of-life tips demonstrated on a tuk-tuk model: snap-orient object picking, the new Houdini 20 **Poly Hinge** node used procedurally (position-and-orientation mode) instead of the old copy/divide-angle/skin workflow, Enumerate for reordering random Connectivity class IDs, several selection-mode tricks, and hotkey fixes for keyboard-layout-incompatible defaults.

### Summary
To snap-orient a new object (e.g. a box) onto part of a reference model, Ctrl-click the reference's display flag to set it as the pick reference, drop the new object, press Enter to enter the tool state, and use the (potentially remapped) "start orientation picking" hotkey plus left-click to snap position/orientation to any point on the model. The new **Poly Hinge** node, when switched from its default mode to **Position and Orientation**, can procedurally sweep/hinge a profile around an angle (e.g. 90°) along an axis directly — replacing the older manual technique of duplicating the shape, dividing the angle by (copies − 1), moving the pivot, and skinning the results, with an identical outcome. When Connectivity assigns class IDs to fractured/grouped pieces, the resulting values are effectively random; running **Enumerate** with mode set to "enumerate pieces" reorders them into clean sequential IDs. Poly Hinge combined with a custom class-attribute selection filter (select tool set to pick by that attribute) lets you isolate one piece via Blast, then hinge only that piece — using the isolated piece's **centroid** as the hinge's position input snaps it immediately to the correct spot, after which fine Y-offset adjustments complete the placement. Additional tips cover: fixing keyboard-incompatible default hotkeys (Smooth Mesh Preview, Toggle Comments, Orientation Picking) via the Hotkey Manager; using **H** to flood-fill-select connected geometry when double-click doesn't register (e.g. with a tablet pen); **Select by 3D Connectivity** combined with **Select Visible Geometry Only** to avoid accidentally grabbing backside geometry; using an imported "Olympic" (per-piece) attribute from Maya-exported models as an alternate selection/material-assignment target; **Shift+H** ("edge in between") to flood-fill-select the polygon strip between two selected edge loops; unchecking **Secure Selection** on the Edit node so selection doesn't require constantly re-toggling out of the Transform tool; camera-view hotkeys (1/2/3/4 toggle between opposite views on repeated press), **H** to reset/home a tumbled/tilted camera, Ctrl+Alt-drag to zoom into a region, and double-left-click to zoom to a piece of geometry; and finally loading custom **Matcap** textures (e.g. from PixelFondue) under the Material tab in Matcap shading mode for quick shading-issue diagnosis.

### Key Steps
1. **Snap-orient object picking**: Ctrl-click the reference model's display flag, drop a new object (e.g. Box), press **Enter** to enter tool state, use the (possibly remapped) orientation-picking hotkey + left-click to snap position/orientation to any point on the reference geometry, then resize/adjust as needed.
2. **Poly Hinge procedural mode**: drop a Poly Hinge node on a profile (e.g. Circle), switch its mode to **Position and Orientation**, set the hinge angle (e.g. 90°) and move along an axis (e.g. X) — produces identical results to the older manual technique (copy, divide angle by copies−1, move pivot, Skin) but in one node.
3. **Reordering random class IDs**: after Connectivity assigns essentially-random class values to grouped/fractured pieces, run **Enumerate** with mode set to **Enumerate Pieces** to reassign clean sequential IDs.
4. **Poly Hinge with a custom class filter**: enter the select tool, pick the custom class attribute as the selection filter, select a specific class value, Blast to isolate it, drop a new Poly Hinge selecting the same class, set to Position and Orientation, then feed the isolated piece's **centroid** as the hinge position so it snaps immediately to the correct location; fine-tune with a Y offset.
5. **Fixing incompatible default hotkeys**: for Smooth Mesh Preview, search "subdivision" in the Hotkey Manager and rebind (author uses keypad +/−); the viewport's geometry tab also exposes a manual level-of-detail control for the smoothed preview.
6. **Selection mode tips**: press **H** to flood-fill-select connected geometry when double-click doesn't register reliably (e.g. tablet pen use); enable **Select by 3D Connectivity** for multi-piece selection, paired with **Select Visible Geometry Only** to avoid grabbing hidden backside geometry; note that Maya-exported models may carry an "Olympic"/per-piece attribute usable as an alternate selection/material target even if poorly organized.
7. **Boundary selection**: select one edge loop, then another on the opposite side, and press **Shift+H** ("edge in between") to flood-fill the polygon strip between them; **H** alone selects just the connecting polygons.
8. **Edit node + Transform tool friction**: uncheck **Secure Selection** on the Edit node so you can select geometry directly while a Transform tool is active, without switching back to the Select tool each time.
9. **Camera/viewport tips**: in camera tool mode, press 1/2/3/4 to switch camera views, and press the **same key again** to toggle to the opposite view (left↔right, top↔bottom, front↔back); press **H** to reset a tilted/tumbled camera to home view; use **Ctrl+Alt+drag** to zoom into a specific region, or **double-left-click** on geometry to zoom to it.
10. **Custom Matcaps**: enter Matcap shading mode, press **D** under the Material tab to find the matcap texture parameter, and load a downloaded matcap (author uses PixelFondue matcaps) for quick shading-issue diagnosis without full material setup.

### Houdini Nodes / VEX / Settings
Hotkey Manager (orientation-picking, subdivision/Smooth-Mesh-Preview, Toggle Comments rebinding), Poly Hinge (Position and Orientation mode), Connectivity (class attribute), Enumerate (Enumerate Pieces mode), Blast (class-filtered isolation), Extract Centroid, select-tool custom-attribute filtering, Select by 3D Connectivity, Select Visible Geometry Only, Edit node (Secure Selection toggle), viewport camera hotkeys (1/2/3/4 toggle, H home reset, Ctrl+Alt zoom-region, double-click zoom-to-geo), Matcap shading mode (Material tab texture parameter).

### Difficulty
Beginner–Intermediate (pure workflow/UI tips; the Poly Hinge procedural technique is the most substantively useful modeling shortcut).

### Houdini Version
20.5.701 (visible in viewport title bar).

### Tags
workflow, hotkeys, poly-hinge, connectivity, enumerate, selection-modes, matcap, viewport, quality-of-life

---

## Related Tutorials
- [Time saving tips in Houdini](time-saving-tips-in-houdini.md) — companion workflow-shortcuts video from the same channel, also covering hotkey fixes for incompatible keyboard layouts.
- [Tips and Tricks for a Better Houdini Time](tips-and-tricks-for-a-better-houdini-time.md) — likely another grab-bag workflow-tips video from the same channel.
- [Tips and tricks in Houdini 21](tips-and-tricks-in-houdini-21.md) — another grab-bag production-tips video from the same channel, focused on VEX/UV/matrix techniques instead.
- [Procedural Graffiti in Houdini and COPS #mardini](procedural-graffiti-in-houdini-and-cops-mardini.md) — shares the Houdini 20.5-era new-node showcase spirit, here featuring Planar Inflate and Clip by Attribute.

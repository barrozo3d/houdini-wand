---
title: Quick object merge with Python in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=fDV8SQegEDc
author: cgside
ingested: 2026-07-13
houdini_version: "Not specified"
tags: [python, hou-module, shelf-tool, object-merge, hotkey, tool-development, workflow-automation]
extraction_status: complete
frames_dir: tutorials/frames/quick-object-merge-with-python-in-houdini/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Quick object merge with Python in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=fDV8SQegEDc)
**Author:** cgside
**Duration:** 6m2s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this video I'll share a quick Python script to create an object merge automatically.
[0:07] So you select now let's say and you press an odd key and you will have the the object merge with the relative path.
[0:15] So it should be pretty quick let's get into it.
[0:20] So I'm going to open the Python source editor and first of all I'm going to import the own module.
[0:28] And let's increase this and then we will have to save the selected node.
[0:37] So let's name the variable selection and we're going to use the all dot selected nodes and we will grab the first one.
[0:47] So we print out this.
[0:50] Let's select a node and it will automatically print out the selected nodes.
[0:57] So now that we have the selection we can grab we can create the object merge. So object merge will be equal to selection dot parent dot create nodes.
[1:14] And we will create like me increase this and we will create the object merge.
[1:25] And we also need to position it. So for that I'm going to create in here I'm going to grab the position from the selection.
[1:33] So cell position it will be equal to selection dot position.
[1:40] And we can comment this out and print out the position.
[1:48] So as you can see we have the position of the nodes.
[1:51] And after creating the object merge we can set the position. So all the object merge dot set position.
[2:02] And we will pass all dot vector to and we will grab the exposition.
[2:09] So cell pass zero and we will subtract one to offset it a bit and we will grab the cell position one.
[2:19] So the y axis and we can also subtract one.
[2:22] You can pick the position. I'm just going to do it like this.
[2:26] So now this should create the node. So let's comment out and do it.
[2:34] And as you can see it's creating the object merge away from the node.
[2:39] Now we just need to grab the path. So for that I'm going to after the setting the position we will grab the relative path.
[2:49] And it will be object merge dot relative path to and we will grab from the selection.
[3:00] And then we can just say object merge dot farm since we want to add it to the select me create an object merge.
[3:10] We want to add it this path in here. So it's called object path one. So object merge dot farm.
[3:17] Oh, we J farm path one and we will set it to the relative path.
[3:27] And now this should work. Let's see. So in that, oh, we need to select the node.
[3:34] Relative path to cell. So relative path object merge dot relative path of its upper case.
[3:48] And now if we do this and we should have the relative path there.
[3:53] So we can simple and now we want to transform this into a tool.
[3:57] But in case we don't have a selection, these will erode. So we can just encapsulate these in a try except so try.
[4:06] And we can place this inside the block.
[4:13] And we can just say except index error.
[4:21] And we can call the dot UI dot display message.
[4:29] And we can say no node elected.
[4:36] And let's see if that now works. As you can see, we get these warning.
[4:41] And if we select the node, it should create the object merge.
[4:45] Now it's pretty simple. We just open we just open in here the shelves.
[4:52] And we will copy this, drag it in here, edit the tool, go into options, change the name.
[4:59] So let's say we object merge demo.
[5:07] We can change the icons.
[5:14] Let's speak this one.
[5:18] And we need to change this to python. And we can assign a not key in this case to the network pane.
[5:23] So just come in here and assign a not key. And you should have that already there.
[5:29] Now just let's delete this, apply and accept. And as you can see, I have assigned a not key in here to my previous tool which is this key combination.
[5:40] And now when I when I press it, I get the object merge.
[5:49] So that was basically it. Hopefully you enjoyed this one. Don't forget you can grab the script on my Patreon alongside with all the projects files from my videos.
[5:57] And also exclusive tutorials. Thank you for watching and I'll see you next time.



---

## Captured Frames

- [0:55] tutorials/frames/quick-object-merge-with-python-in-houdini/frame_000.jpg
- [1:40] tutorials/frames/quick-object-merge-with-python-in-houdini/frame_001.jpg
- [2:30] tutorials/frames/quick-object-merge-with-python-in-houdini/frame_002.jpg
- [4:20] tutorials/frames/quick-object-merge-with-python-in-houdini/frame_003.jpg
- [5:50] tutorials/frames/quick-object-merge-with-python-in-houdini/frame_004.jpg

---

## Structured Notes

### Core Technique
A short `hou`-module Python script, wired to a shelf tool with a hotkey, that automatically creates and wires up an Object Merge node pointing at whatever node is currently selected — turning a multi-click manual operation into a single keypress.

### Summary
The script grabs the current selection with `hou.selectedNodes()[0]`, then creates an Object Merge node as a child of the selected node's parent (`selection.parent().createNode("object_merge")`). To avoid the new node overlapping the source, it reads the selected node's position via `.position()` and offsets the new Object Merge by `-1` in both X and Y (`hou.Vector2(sel_pos[0]-1, sel_pos[1]-1)`) before setting it. The relative path from the Object Merge to the selected node is computed with `object_merge.relativePathTo(sel)` and written into the Object Merge's `objpath1` parameter, so the reference works correctly regardless of network location. Since running the tool with nothing selected would throw an `IndexError` on `selectedNodes()[0]`, the whole block is wrapped in a `try/except IndexError` that calls `hou.ui.displayMessage("No node selected")` instead of crashing. Finally, the script is turned into a reusable tool: copied into a new shelf tool (via the Shelf editor's "New Tool" + paste), given a name/icon, its language set to Python, and bound to a keyboard shortcut scoped to the Network Editor pane — so selecting a node and pressing the hotkey instantly creates a correctly-positioned, correctly-wired Object Merge referencing it.

### Key Steps
1. Open the Python Source Editor and `import hou`.
2. Grab the current selection: `sel = hou.selectedNodes()[0]`.
3. Read the selected node's position: `sel_pos = sel.position()`.
4. Create the Object Merge node as a child of the selection's parent: `obj_merge = sel.parent().createNode("object_merge")`.
5. Offset the new node's position so it doesn't overlap the source: `obj_merge.setPosition(hou.Vector2(sel_pos[0]-1, sel_pos[1]-1))`.
6. Compute the relative path from the new node to the selection: `rel_path = obj_merge.relativePathTo(sel)`.
7. Set that relative path on the Object Merge's first object-path parameter: `obj_merge.parm("objpath1").set(rel_path)`.
8. Wrap the whole block in `try/except IndexError:` calling `hou.ui.displayMessage("No node selected")` so running the tool with an empty selection fails gracefully instead of erroring.
9. Open the Shelf editor, create a new tool, paste the script in as its Python script, rename it, pick an icon, and assign a keyboard shortcut scoped to the Network Editor pane — the tool now runs on a single hotkey press with a node selected.

### Houdini Nodes / VEX / Settings
`hou.selectedNodes()`, `hou.Vector2`, `node.parent().createNode("object_merge")`, `node.setPosition()`, `node.relativePathTo()`, `node.parm().set()`, `try/except IndexError`, `hou.ui.displayMessage()`, Shelf Tool editor (Python script type, custom icon, Network-Editor-scoped hotkey).

### Difficulty
Beginner (a short, self-contained Python/`hou`-module script — approachable for anyone comfortable with basic Houdini Python scripting).

### Houdini Version
Not specified.

### Tags
python, hou-module, shelf-tool, object-merge, hotkey, tool-development, workflow-automation

---

## Related Tutorials
- [Procedural Duct Tape in Houdini](procedural-duct-tape-in-houdini.md) — uses this exact quick-Object-Merge shelf tool while wiring up the deformation-reference geometry.
- [Time-saving tips in Houdini](time-saving-tips-in-houdini.md) — shares the same shelf-tool-hotkey and Python-scripted-node-creation productivity approach.
- [Resample Color Ramps in Houdini](resample-color-ramps-in-houdini.md) — another short, self-contained `hou`-module Python utility script from the same channel.

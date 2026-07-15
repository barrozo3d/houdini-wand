---
title: Time saving tips in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=Mxg-zhwdNlE
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.301"
tags: [python, hotkeys, karma, materialx, triplanar, workflow, automation, hou-module]
extraction_status: complete
frames_dir: tutorials/frames/time-saving-tips-in-houdini/
frame_count: 6
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Time saving tips in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=Mxg-zhwdNlE)
**Author:** cgside
**Duration:** 2m55s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone and welcome back, today I'll share a few time saving tips in Odini.
[0:05] So to start with our about not-o-update switch that you can assign to an otkey and toggle
[0:11] between manual and auto-update mode.
[0:15] This is extremely handy for more complex scenes and even to open eeps that you just want
[0:21] to check a simple setup.
[0:23] So to create this toggle you will need to create a shelf tool with the following code that
[0:29] I found online.
[0:31] Then go to the otkey step and set a global otkey.
[0:36] In this case I use the combination control plus dot.
[0:40] Very useful in my opinion, let me know your thoughts below.
[0:44] So the other day I came across a video on how to toggle comments in wax and bighton.
[0:50] The only problem I found is that the combination of keys doesn't work on my particular keyboard
[0:55] language and also in the US based keyboards.
[1:00] To change that you can go to the otkey editor and search for comments and you'll find toggle
[1:06] comments where you can assign a otkey that works with your keyboard.
[1:12] Now you can toggle comments in one line or multiple lines.
[1:17] Okay, the final tip is on how to automate material creation in salaries.
[1:22] Finally on how in the world you can create a karma material builder with bighton which
[1:28] already contains all the initial notes inside.
[1:31] So I found some code online on how to query the script of the shelf tools that we can use
[1:38] in our advantage by passing the correct name in this case the VOP karma material like
[1:43] subnet.
[1:45] And if we execute this code we indeed get the code snippet to create the material which
[1:51] comes from the VOP utilities dot by.
[1:54] But if we run this code we are missing the quark's arguments so we need to rebuild them
[2:00] somehow.
[2:01] So after some digging in the docs I found the necessary arguments to pass in this case
[2:06] we will need to, we will need the network editor as viewer and how to place the material.
[2:14] And this is the easiest way to recreate this behavior otherwise you would need to rebuild
[2:19] all the nodes inside and mask the subnet and so on.
[2:24] So for my patrons I have a triplanar material in port where you can simply select a folder
[2:29] with your textures and it will create all the necessary notes, connections and expression
[2:35] linking.
[2:37] This is a good resource to learn from by the way and if you have any questions you can
[2:41] always message me in there.
[2:44] So yeah let me know if you found these word sharing.
[2:47] Thank you and happy new year.



---

## Captured Frames

- [0:10] tutorials/frames/time-saving-tips-in-houdini/frame_000.jpg
- [0:40] tutorials/frames/time-saving-tips-in-houdini/frame_001.jpg
- [1:15] tutorials/frames/time-saving-tips-in-houdini/frame_002.jpg
- [1:40] tutorials/frames/time-saving-tips-in-houdini/frame_003.jpg
- [2:10] tutorials/frames/time-saving-tips-in-houdini/frame_004.jpg
- [2:40] tutorials/frames/time-saving-tips-in-houdini/frame_005.jpg

---

## Structured Notes

### Core Technique
Three quality-of-life shortcuts: a shelf-tool hotkey toggling auto-update mode on/off, a remapped hotkey for toggling VEX/Python comments that works across keyboard layouts, and a Python script that queries a shelf tool's own source code to reconstruct the exact `hou.vopNetUtils`/`hou.vopUtils` arguments needed for scripted Karma Material Builder creation.

### Summary
Manual/auto-update mode is normally menu-driven, but binding a small shelf-tool script to a global hotkey (the author uses Ctrl+.) makes toggling it a one-key action — handy for complex scenes or quickly inspecting simple setups without full cook overhead. Separately, Houdini's default "toggle comments in VEX/Python" hotkey combination doesn't work on some keyboard layouts (including the author's and standard US layouts); the fix is to open the Hotkey Editor, search for "comment," find **Toggle Comments**, and rebind it to a working key combination — after which both single-line and multi-line comment toggling work as expected. The most involved tip automates **Karma Material Builder creation via Python**: since a Karma Material Builder subnet needs several specific internal nodes pre-populated (which normal `createNode()` doesn't set up), the author finds and adapts code online to **query the shelf tool's own source script** by name, then executes it to see the actual code Houdini uses internally — revealing the correct function is under `hou.vopNetUtils`/`hou.vopUtils`, requiring specific arguments (network editor as viewer, and how to place the resulting material) that had to be reverse-engineered from the shelf script since running it directly failed with a missing-argument error. This scripted approach avoids manually rebuilding all the internal nodes and connections a Karma Material Builder subnet requires. As a bonus for Patreon supporters, the author has a Triplanar material importer tool that builds a full triplanar network and wires connections automatically from a folder of texture files.

### Key Steps
1. **Auto-update toggle**: create a shelf tool containing a small script (found online) that toggles Houdini's manual/auto-update mode; assign it a global hotkey (author uses **Ctrl + .**) via the Hotkey Editor.
2. **Fixing comment-toggle hotkey on incompatible keyboards**: open the **Hotkey Editor**, search for "comment," locate **Toggle Comments**, and assign a new key combination that actually works with the user's keyboard layout (the default doesn't work on the author's language layout or standard US layouts) — afterward both single-line and multi-line comment toggling function correctly in VEX/Python editors.
3. **Scripted Karma Material Builder creation**: find code online that queries the **script of a shelf tool** by name (passing the correct internal name, e.g. the VOP Karma Material subnet's shelf tool identifier).
4. Execute the queried code to retrieve the actual Python snippet Houdini's shelf tool runs internally — this reveals it comes from `vopUtils.py` and specifically uses **`hou.vopNetUtils`/`hou.vopUtils`** functions rather than a plain `createNode()` call.
5. Running the extracted code directly fails due to **missing keyword arguments**; dig through Houdini's docs to find the required arguments — specifically the **network editor as the viewer** and how the resulting material subnet should be **placed** — and rebuild them manually.
6. With the correct arguments reconstructed, the script successfully creates a fully-populated Karma Material Builder subnet (with all its internal default nodes) via pure Python, avoiding the need to hand-build the subnet's internals or mask/wire it manually.
7. (Mentioned, not built in this video) A Patreon-exclusive **Triplanar material importer** tool: point it at a folder of textures and it auto-generates all the necessary Triplanar nodes, connections, and expression linking.

### Houdini Nodes / VEX / Settings
Shelf Tool (custom Python scripts bound to hotkeys), Hotkey Editor (global hotkey assignment, "Toggle Comments" rebinding), Python `hou` module (querying a shelf tool's script via its internal name, `hou.vopNetUtils`/`hou.vopUtils` functions for Karma Material Builder subnet creation, network-editor-as-viewer + placement arguments), Karma Material Builder (VOP subnet), Triplanar (mentioned Patreon tool).

### Difficulty
Intermediate (the auto-update and hotkey tips are trivial; the scripted Material Builder creation requires digging through `hou` internals and shelf-tool source code).

### Houdini Version
20.5.301 (visible in viewport title bar).

### Tags
python, hotkeys, karma, materialx, triplanar, workflow, automation, hou-module

---

## Related Tutorials
- [Python in Houdini | Create a texture importer for Solaris](python-in-houdini-create-a-texture-importer-for-solaris.md) — related Python-automation-for-shading tutorial from the same channel.
- [Quality of Life Tips in Houdini](quality-of-life-tips-in-houdini.md) — companion workflow-shortcuts video from the same channel.

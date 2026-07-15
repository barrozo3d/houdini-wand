---
title: Python in Houdini  | Create a texture importer for Solaris
source: YouTube
url: https://www.youtube.com/watch?v=zZBkR8rk-_s
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.403"
tags: [python, solaris, materialx, hou-module, automation, texturing, scripting]
extraction_status: complete
frames_dir: tutorials/frames/python-in-houdini-create-a-texture-importer-for-solaris/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Python in Houdini  | Create a texture importer for Solaris

**Source:** [YouTube](https://www.youtube.com/watch?v=zZBkR8rk-_s)
**Author:** cgside
**Duration:** 4m44s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back.
[0:03] In this video I'm going to show you how you can build your own texture importer for
[0:07] the salaries and material likes context.
[0:10] This is a very simple implementation and it's more like an exercise to introduce Python
[0:15] in Odini if you're used to it in other packages.
[0:19] I'll be uploading the code to Patreon if you guys want to check it out.
[0:24] So here I have my texture folder with a very basic naming convention that has the object
[0:31] name, channel name and color space and that's the information that we're going to use
[0:36] to guide our tool.
[0:38] So in Solaris let's create a material library.
[0:41] This is the starting point and the reference for the script.
[0:45] The first thing we need to do is to import the Odini and OS modules.
[0:50] Next we set a list of channels that in this case is Substance Painter Friendly.
[0:55] Again very basic, ideally you would have dictionaries with lists of different names for
[1:01] albeit roughness and so on.
[1:04] Now we prompt the user for the base name of the object that's baked in the file name
[1:09] like wood, cloth or plastic wheels.
[1:13] You can add some buttons like ok and cancel to complete the operation.
[1:18] If we print it you can see that the output is a list of the index of the button pressed
[1:25] and the given input string.
[1:29] So if the user didn't cancel the operation and the input was not empty we will execute
[1:34] some code.
[1:36] First let's create a variable for the current project path.
[1:43] After that we have another user interaction so the folder of the textures can be selected.
[1:51] Now we start to interact with the current context.
[1:55] Storing the current node selected the material library in a variable.
[2:00] So that later we can add nodes inside.
[2:07] Creating a material x with the create node command you can also rename it here.
[2:12] I noticed sometimes the UVs are required so I'm also creating a texture coordinate
[2:17] node and setting it to Vector2, UNV.
[2:23] And here we are going to iterate over the textures folder so we can filter the right textures
[2:28] to import.
[2:29] We also want to iterate over each channel and if the texture file has a matching base
[2:35] name and a channel name we will continue with the logic.
[2:40] If we bring the result you can see it picked only the three textures that exist for this
[2:45] specific assets.
[2:47] Now we can create a USD texture node or you can use a material x image.
[2:53] Then we save in a variable the index of the channel being processed so we can use it later.
[3:00] Add the name of the texture to the folder path the user picked and finally set the file
[3:05] name with the path we just saved.
[3:08] For organization we can just lay out the nodes inside the material library and as you
[3:13] can see it's working as expected with the file name of the node being set correctly.
[3:20] I mentioned at the beginning that I also have the color space in the file name so we can
[3:26] use it to set the color space here.
[3:32] The way you can check the correct token is in the menu tab of the parameter interface.
[3:39] So now we start to do some connections first the UVs to the texture nodes.
[3:45] Next we check if the channel is the base color and connected to the base color which is
[3:50] the input one.
[3:52] We also need to set the output for the RGB output.
[3:57] Then we do the same for the roughness and normal or I channel creating the necessary nodes
[4:03] and connecting the correct to the correct inputs.
[4:07] The only issue here is that we need to find the correct index of the nodes.
[4:12] For example the normal inputs of the material x is 40 we just need to count it I guess.
[4:21] So that's it then you can create a shell item with the codes and execute it anytime
[4:26] you need it.
[4:27] Or even create a custom radial menu for the python scripts.
[4:31] I hope that you have learned something and check out my Patreon and Gamero if you'd like
[4:36] to support the channel.
[4:38] Thank you and see you in the next one.



---

## Captured Frames

- [0:20] tutorials/frames/python-in-houdini-create-a-texture-importer-for-solaris/frame_000.jpg
- [0:55] tutorials/frames/python-in-houdini-create-a-texture-importer-for-solaris/frame_001.jpg
- [1:30] tutorials/frames/python-in-houdini-create-a-texture-importer-for-solaris/frame_002.jpg
- [2:10] tutorials/frames/python-in-houdini-create-a-texture-importer-for-solaris/frame_003.jpg
- [2:55] tutorials/frames/python-in-houdini-create-a-texture-importer-for-solaris/frame_004.jpg
- [3:30] tutorials/frames/python-in-houdini-create-a-texture-importer-for-solaris/frame_005.jpg
- [4:20] tutorials/frames/python-in-houdini-create-a-texture-importer-for-solaris/frame_006.jpg

---

## Structured Notes

### Core Technique
A from-scratch Python script that batch-imports a folder of naming-convention-based texture files (object/channel/colorspace encoded in the filename) into a Solaris Material Library, auto-creating a MaterialX Standard Surface network with correctly wired and color-space-tagged texture nodes.

### Summary
Working inside a Material Library node (the script's starting reference/context), the script imports `hou` and `os`, defines a list of Substance-Painter-style channel names, and prompts the user via `hou.ui.readInput()` for the object's base name (e.g. "wood", "cloth") baked into filenames, followed by a folder-picker for the texture directory. It grabs the currently selected node (the material library) as the creation context, creates a MaterialX Standard Surface subnet via `createNode()`, and a Texture Coordinate node set to Vector2/UV. It then iterates the texture folder, filtering files whose name matches both the base name and a known channel name, creates a `mtlximage`/USD texture node per match, sets its file path, lays out the network, and — using the color-space token embedded in the filename — sets the correct color space per texture (checked via the parameter interface's menu tab for valid tokens). Finally it wires UVs into every texture node and connects base-color texture RGB output to the shader's base-color input (with index-based wiring for roughness/normal since MaterialX Standard Surface's normal input index had to be counted manually, e.g. index 40).

### Key Steps
1. Set up a **Material Library** node in Solaris as the reference context for node creation.
2. `import hou, os`; define a list of expected channel names following a Substance Painter-style convention (base color, roughness, height, opacity, displacement, etc.).
3. Prompt for the object base name via `hou.ui.readInput()` with OK/Cancel buttons; the call returns a tuple of (button index pressed, entered string) — proceed only if not cancelled and the string isn't empty.
4. Store the current `hou.hipFile.path()`-derived project path for later use; open a second folder-picker dialog for the texture directory.
5. Store the currently selected node (the material library) in a variable to use as the node-creation context.
6. Create a **MaterialX Standard Surface** subnet via `context.createNode(...)`, renaming it as needed; create a **Texture Coordinate** node and set its type to Vector2/UV (needed since some texture setups require explicit UVs).
7. Iterate the texture folder's files; for each expected channel, check whether a file matches both the base name and that channel name — filtering out non-matching files (verified by printing the filtered result showing only the 3 relevant textures for a given asset).
8. For each match, create a **USD Texture** node (or MaterialX Image node), store the channel index for later wiring, build the full file path (folder + filename), and set it on the texture node's file parameter.
9. Lay out the nodes inside the Material Library for readability; check the file name is being set correctly on each created node.
10. Parse the **color space token** also embedded in the filename and set it on the texture node — the correct parameter token is found by inspecting the parameter interface's **menu tab**.
11. Wire connections: UV output → each texture node's UV input; if the channel is base color, connect its RGB output to the shader's base-color input; repeat similarly for roughness and normal, manually counting the MaterialX Standard Surface's input index for the normal input (found to be index 40).
12. Save the finished script as a **shelf tool** to execute anytime, or bind it to a custom **radial menu** entry for quick access.

### Houdini Nodes / VEX / Settings
`hou` Python module (`hou.ui.readInput()`, `hou.ui.selectFile()`, `hou.node()`/`createNode()`, `hou.selectedNodes()`), `os` module (folder iteration, filename parsing), Material Library (LOPs), MaterialX Standard Surface subnet, Texture Coordinate node (Vector2/UV), USD/MaterialX Image texture nodes (file path + color space parameters), manual input-index wiring for shader connections, Python Source Editor, custom shelf tool / radial menu integration.

### Difficulty
Intermediate (assumes basic Python familiarity; the main challenge is discovering the right `hou` API calls and MaterialX node parameter/input names).

### Houdini Version
19.5.403 (visible in viewport title bar).

### Tags
python, solaris, materialx, hou-module, automation, texturing, scripting

---

## Related Tutorials
- [Python Multi Asset Loader in Houdini](python-multi-asset-loader-in-houdini.md) — companion Python-automation tutorial from the same channel using similar `hou`/`os` file-iteration patterns.
- [Python in Houdini | Absolute to relative paths](python-in-houdini-absolute-to-relative-paths.md) — related Python file-management automation script from the same channel.

---
title: Python multi asset loader in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=RQ3kSr5u16A
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.303"
tags: [python, hou-module, automation, solaris, geometry-variants, asset-loading, scripting]
extraction_status: complete
frames_dir: tutorials/frames/python-multi-asset-loader-in-houdini/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Python multi asset loader in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=RQ3kSr5u16A)
**Author:** cgside
**Duration:** 3m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back. So in this tutorial I'm gonna show you how you can create a multi-asset
[0:06] importer in Odini using basic python. So this is the final result of the tool where every
[0:14] asset gets its own subnet so you can easily load it into Solaris for instance. I'll show you
[0:21] that at the end. There's a more complete version of this tool with more features and an interface
[0:29] that I will be sharing on my Patreon in case you're interested. Where you can load files from
[0:35] subfolders with custom prefix and LOD filter or you can simply load all files in a particular folder.
[0:45] Okay let's start by creating the asset loader. The first step would be to import the necessary modules
[0:52] in this case Odini and OS. We can also set the default folder for the explorer window.
[1:01] So here we launch the file explorer window setting the type to folder and give it an initial
[1:07] location that we defined previously. Now if we actually select the folder and not the cancel
[1:15] button we will continue the logic. In this case set an initial context of eJ and create a geometry
[1:24] container. Now we will iterate over the files within the selected folder and if I print out the
[1:34] result you can see the target folders the different variations. We check if the folder starts with
[1:40] a specific name var. You can adapt to your own scenario. Next we will dive inside the var folders
[1:48] and grab the LOD 0 which is the one I am going to use and as you can see by the output we have
[1:56] selected the correct 3D files. Now we get rid of the file extension just grabbing the file name
[2:04] itself and we will need the absolute paths of the file. We can simply recreate it with the variables
[2:12] from before. We will also create a file software to actually load the files with the create node
[2:21] command and accept the parameter file to the file path we declared. But as you can see it's a bit
[2:29] disorganized with a bunch of file nodes so we can actually create a subnet from each file
[2:35] with an appropriate name. In order to do that we can use the collapse into subnet command
[2:42] and pass it the nodes to collapse and the respective name. Just to finish we can lay out everything
[2:49] so it's a bit more readable in the network. Now you have everything working as expected and again
[2:56] you will have to adapt it to your own naming conventions and file structures.
[3:01] Or you can use the tool I am providing on Patreon that covers more file structures and naming
[3:08] conventions. Just to show you how you would load these into salaries you can create a component
[3:14] geometry dive inside and load a single variation. Now you can use the geovariant index variable
[3:22] to load in everything along with the component geometry variance set to number and with the correct
[3:29] amount of variations. And you can use an explore variance to check that it's loading all the different
[3:35] variations. All right I hope you got something out of this. I know that you can import multiple files
[3:42] with a dini but I don't like the way it organizes it into different geopontainers and it doesn't
[3:49] have the possibility to load from multiple folders at once. So yeah thank you for your time
[3:55] and see you in the next one.



---

## Captured Frames

- [0:15] tutorials/frames/python-multi-asset-loader-in-houdini/frame_000.jpg
- [0:55] tutorials/frames/python-multi-asset-loader-in-houdini/frame_001.jpg
- [1:35] tutorials/frames/python-multi-asset-loader-in-houdini/frame_002.jpg
- [2:15] tutorials/frames/python-multi-asset-loader-in-houdini/frame_003.jpg
- [2:55] tutorials/frames/python-multi-asset-loader-in-houdini/frame_004.jpg
- [3:30] tutorials/frames/python-multi-asset-loader-in-houdini/frame_005.jpg
- [3:50] tutorials/frames/python-multi-asset-loader-in-houdini/frame_006.jpg

---

## Structured Notes

### Core Technique
A Python script that batch-imports every 3D file from a selected folder (filtering by an LOD/variant naming convention) into individually named subnets — one per asset — so the result can be directly consumed by Solaris's Component Geometry Variants workflow without manual per-file File node creation.

### Summary
Rather than accepting Houdini's built-in multi-file import (which dumps everything into separate Geometry containers with no folder/naming-convention support), the script opens a folder-browser dialog, creates a Geometry container, and iterates the selected folder's subfolders. It filters to subfolders starting with a configurable prefix (e.g. "var"), dives into each variant folder to grab only the **LOD 0** file (stripping the extension for use as a clean node name), reconstructs the absolute file path from stored path variables, creates a **File SOP** per asset with the file path parameter set, then uses `collapseIntoSubnet()` to wrap each File node into its own appropriately-named subnet — producing a tidy per-asset network instead of a pile of loose File nodes. The result is demonstrated loading directly into a Solaris **Component Geometry** with **Component Geometry Variants** set to the matching variant count, verified via an Explore Variants node cycling through all loaded assets.

### Key Steps
1. Import `hou` and `os`; optionally set a default starting folder for the file-browser dialog.
2. Launch a **folder-select** file browser (`hou.ui.selectFile()` with type set to folder) with the default starting location; if the user doesn't cancel, continue.
3. Set the working context to `/obj` and create a **Geometry** container node.
4. Iterate the files/subfolders in the selected root folder; print results to confirm the target subfolders (asset variations) are being found.
5. Filter subfolders to only those **starting with a specific prefix** (e.g. "var") — adaptable per project naming convention.
6. Dive into each variant subfolder and grab only the **LOD 0** file (the resolution level used for this workflow), confirmed via printed output showing the correctly selected 3D files.
7. Strip the file extension to get a clean base name for the node, and reconstruct the **absolute file path** from previously stored path variables.
8. Create a **File SOP** per asset via `createNode()`, setting its `file` parameter to the reconstructed path.
9. Since this produces a cluttered network of loose File nodes, use **`collapseIntoSubnet()`**, passing the nodes to collapse and the desired subnet name, to wrap each asset's File node into its own clean, appropriately-named subnet.
10. Lay out the resulting network for readability.
11. In Solaris: create a **Component Geometry**, dive in, load a single variation to start; use the `geovariant_index` global variable together with **Component Geometry Variants** (set to the correct variant count) to load all variations at once, and verify with an **Explore Variants** node cycling through each.
12. Author notes their paid Patreon tool extends this with subfolder prefix filters, LOD selection UI, and a "load all files in a folder" simple mode.

### Houdini Nodes / VEX / Settings
`hou` module (`hou.ui.selectFile()` folder mode, `hou.node()`/`createNode()`, `collapseIntoSubnet()`), `os` module (`os.listdir`, path/extension parsing, path reconstruction), File SOP (per-asset geometry import), Component Geometry (Solaris/LOPs), Component Geometry Variants (variant count), `geovariant_index` global variable, Explore Variants node.

### Difficulty
Intermediate (straightforward Python/os iteration; the useful non-obvious trick is `collapseIntoSubnet()` for clean per-asset organization).

### Houdini Version
19.5.303 (visible in viewport title bar).

### Tags
python, hou-module, automation, solaris, geometry-variants, asset-loading, scripting

---

## Related Tutorials
- [Python in Houdini | Create a texture importer for Solaris](python-in-houdini-create-a-texture-importer-for-solaris.md) — companion Python-automation tutorial from the same channel using similar `hou`/`os`/folder-iteration patterns.
- [Quick Object Merge with Python in Houdini](quick-object-merge-with-python-in-houdini.md) — related Python scripting shortcut from the same channel.

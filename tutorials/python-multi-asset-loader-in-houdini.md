---
title: Python multi asset loader in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=RQ3kSr5u16A
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/python-multi-asset-loader-in-houdini/
frame_count: 0
frame_status: pending-selection
---

# Python multi asset loader in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=RQ3kSr5u16A)
**Author:** cgside
**Duration:** 3m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py python-multi-asset-loader-in-houdini <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

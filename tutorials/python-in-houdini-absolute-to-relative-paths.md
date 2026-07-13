---
title: Python in Houdini | Absolute to relative paths
source: YouTube
url: https://www.youtube.com/watch?v=N5DN6SwYFVs
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/python-in-houdini-absolute-to-relative-paths/
frame_count: 0
frame_status: pending-selection
---

# Python in Houdini | Absolute to relative paths

**Source:** [YouTube](https://www.youtube.com/watch?v=N5DN6SwYFVs)
**Author:** cgside
**Duration:** 5m29s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py python-in-houdini-absolute-to-relative-paths <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome back. So in this video we're going to create a simple python script
[0:05] to make all the references in our scene relative to the project. This way if you're uploading
[0:12] the project to someone or to render clouds you don't face the issue of missing textures or models.
[0:21] So for this particular project I used Megascans textures and two different assets for the ground cover
[0:29] and as you can see in the file dependencies I don't have them relative to the project.
[0:33] Instead they are in the models and textures folder in my computer.
[0:39] And you should be able to drag and drop the models and textures to the respective folder in the
[0:44] in the editor and it will automatically copy the files from the original location and set the new
[0:51] path in the notes. With the dollar job variable. But for some reason it's giving me an error for
[0:58] models and I didn't find any solution for it so I thought it should be easy to write a python script
[1:05] as I have done something similar in my before. So let's open the python source editor and write
[1:14] the script. Let's import the OS and oddini modules. We will also need the IEP and Home variables
[1:22] that will output the absolute path of each directory. Now using the file references command
[1:30] to get all the dependencies in our scene and I also want to filter the references to only 3D
[1:37] objects and textures. There is no need for USD or other type of data as usually it's relative
[1:44] to the project by default. So the file references command outputs the oddini.param object
[1:52] and also the paths in disk. We will iterate over the items and get the different parameters that
[2:00] will be useful. As I stated before we want to replace only 3D models and textures so we can just use
[2:07] a statement to filter our file types. We can get a lot of information from the param object like the
[2:14] parameter name, the path of the notes and the note itself. Let's set them as variables that we can
[2:22] use later. Also we can remove from the equation all the dependencies that already are relative to
[2:30] the project or IEP with this if statement. But we also have the Home variable to take into consideration.
[2:40] As it's pointing to the documents folder which is outside of our project's structure,
[2:46] let's deal with that in a minute. Setting a variable to get the file name and extension from
[2:52] the original file path and now we need some out to organize the assets into different folders.
[3:00] First we can relocate the textures to the text folder in the project. As for the geometries we can
[3:07] use the Geofolder. The problem with setting it only to the Geofolder is that I have two different
[3:13] mega scans assets with different variations and they all share the same naming convention.
[3:21] So if I paste them all inside the Geofolder, only one of them will be copied or we will get
[3:28] a narrow for duplicate file. So to solve this I decided to create a subfolder,
[3:34] getting the name from the paths of the note.
[3:40] In order to get rid of the underscores and numbers after the asset name I found a regular expression
[3:47] online that takes care of that, as I don't really need a different folder per variation.
[3:54] Now this part deals with the own directory as we need an absolute path to copy and paste the files.
[4:06] This section deals with the creation of the subfolder in our project for the mega scans assets.
[4:14] And we can now set the full destination path including the file name and extension.
[4:20] Check if the file already exists and we can copy the original file to the destination folder using the
[4:28] Chatel module. The only thing left to do is to make the destination path relative to our project
[4:36] and replace the parameters of our nodes with the new path.
[4:40] After running the code we can now see that the image nodes and files have been replaced with the
[4:50] new files copied to the project folder. We can also check the dependencies and all the textures and
[4:58] models are green meaning that they are relative to the dollar job variable as we intended.
[5:05] Now you can drag the code to a custom shelf and execute it anytime you need it.
[5:13] So yeah, I hope you can take something out of this.
[5:16] This script will be available on Patreon if you guys want to grab it and support the channel.
[5:23] Thank you for your time and see you in the next one.



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

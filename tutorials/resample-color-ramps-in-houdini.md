---
title: Resample Color Ramps in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=P-2FPlUJO60
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.319"
tags: [python, hou-module, ramp, cops, scripting, automation, quick-tip]
extraction_status: complete
frames_dir: tutorials/frames/resample-color-ramps-in-houdini/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Resample Color Ramps in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=P-2FPlUJO60)
**Author:** cgside
**Duration:** 2m18s | 3 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome! So in this quick tip I wanted to show you how you can use Python to
[0:06] re-sample your color ramps. So going from this to something like this. And this is actually pretty simple.


### Tutorial [0:15]
**Transcript (timestamped):**
[0:17] We first saving the selected node so we need to have the node selected that we want to change the
[0:28] parameter. Then we access the parameter ramp which if you can see in here is called actually ramp.
[0:38] And then we just evaluate it to gather the values. And then we need to make three lists which are the
[0:48] base of any color ramp. So the interpolation, the position and the values which in this case are
[0:56] colors. So the interpolation will be a list of the ramp basis how it's called. And then for the
[1:05] position it's called keys and for the colors is the values as I told you. Then we set the amount
[1:12] of points we want to end up with. In this case I chose 10. Then we create a list of evenly spaced
[1:23] values for the new positions. So these positions in here. And finally we we we sample the previous color
[1:33] at that specific position with the lockup command. And at the end we just set the audio
[1:41] in a little tramp to use the basis which we didn't change. The new keys, the evenly spaced positions.
[1:52] And the new values which are the sampled colors from this variable. Then we just set it at the end.


### Outro [2:00]
**Transcript (timestamped):**
[2:00] So yeah that's basically it. If you want you can grab the script on my Patreon alongside with
[2:07] all the project files from my videos and exclusive tutorials. So make sure to check that out.
[2:14] And thank you for watching. See you next time.



---

## Captured Frames

- [0:10] tutorials/frames/resample-color-ramps-in-houdini/frame_000.jpg
- [0:40] tutorials/frames/resample-color-ramps-in-houdini/frame_001.jpg
- [1:10] tutorials/frames/resample-color-ramps-in-houdini/frame_002.jpg
- [1:40] tutorials/frames/resample-color-ramps-in-houdini/frame_003.jpg
- [2:05] tutorials/frames/resample-color-ramps-in-houdini/frame_004.jpg

---

## Structured Notes

### Core Technique
A short Python script (runnable as a shelf tool) that re-samples any `hou.Ramp` parameter on the selected node into a fixed number of evenly-spaced keys by evaluating the original ramp's color at each new position with `hou.Ramp.lookup()` and rebuilding a new `hou.Ramp` object from the results — useful for cleaning up a messy/irregularly-keyed color ramp (e.g. one authored in Cops/Copernicus) into a tidy, evenly distributed one.

### Summary
The script grabs the currently selected node via `hou.selectedNodes()[0]`, accesses its ramp parameter (named "ramp" in the example, e.g. on a `mono_to_rgb`-style Cops node), and calls `.eval()` to get the live `hou.Ramp` object. Three lists are extracted from it: `ramp.basis()` (interpolation type per key), `ramp.keys()` (key positions), and `ramp.values()` (the actual colors) — these are the three components any Houdini ramp parameter is built from. A target point count is chosen (10 in the example), a list of evenly-spaced new positions is generated across the 0–1 range, and for each new position the **original ramp's color is sampled** via `ramp.lookup(position)`. Finally, a brand-new `hou.Ramp` is constructed using the original basis list (unchanged), the new evenly-spaced key positions, and the newly sampled color values, and set back onto the parameter with `.set()` — replacing the original ramp's irregular keys with a clean, evenly distributed version that preserves the same visual gradient.

### Key Steps
1. Get the selected node: `node = hou.selectedNodes()[0]`.
2. Access the ramp parm and evaluate it: `ramp_parm = node.parm("ramp")` (or `parmTuple` depending on the parameter type), then `ramp = ramp_parm.eval()` to get the live `hou.Ramp` object.
3. Extract the three components that define any ramp: `bases = list(ramp.basis())` (interpolation per key), `keys = list(ramp.keys())` (positions), `values = list(ramp.values())` (colors).
4. Set the desired output point count, e.g. `num_points = 10`.
5. Generate evenly-spaced new key positions across the ramp's range, e.g. `new_keys = [i / (num_points - 1) for i in range(num_points)]`.
6. For each new key position, **sample the original ramp's color** at that position using `ramp.lookup(position)`, building a `new_values` list.
7. Construct a new `hou.Ramp` object using the **original basis list** (interpolation types are kept as-is), the new evenly-spaced keys, and the newly sampled values.
8. Set the new ramp back onto the parameter with `ramp_parm.set(new_ramp)` — the parameter now shows a clean, evenly-spaced ramp with the same visual gradient as before.

### Houdini Nodes / VEX / Settings
Python `hou` module (`hou.selectedNodes()`, `hou.Parm`/`hou.ParmTuple`, `hou.Ramp` — `.basis()`, `.keys()`, `.values()`, `.lookup()`, constructor, `.set()`), shelf tool packaging, demonstrated on a Cops/Copernicus `mono_to_rgb`-style color ramp node.

### Difficulty
Beginner–Intermediate (a short, self-contained `hou.Ramp` scripting pattern).

### Houdini Version
20.5.319 (visible in viewport title bar).

### Tags
python, hou-module, ramp, cops, scripting, automation, quick-tip

---

## Related Tutorials
- [Quick Object Merge with Python in Houdini](quick-object-merge-with-python-in-houdini.md) — related short Python scripting shortcut from the same channel.
- [Python in Houdini | Create a texture importer for Solaris](python-in-houdini-create-a-texture-importer-for-solaris.md) — related `hou` scripting automation tutorial from the same channel.

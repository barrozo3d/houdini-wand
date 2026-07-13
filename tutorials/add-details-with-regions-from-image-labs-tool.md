---
title: Add details with regions from image labs tool
source: YouTube
url: https://www.youtube.com/watch?v=qS5uDc8EePQ
author: cgside
ingested: 2026-07-13
houdini_version: "H20.5+ (Labs Regions from Image tool)"
tags: [vellum, cloth, labs-tools, procedural, texturing, image-based, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/add-details-with-regions-from-image-labs-tool/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Add details with regions from image labs tool

**Source:** [YouTube](https://www.youtube.com/watch?v=qS5uDc8EePQ)
**Author:** cgside
**Duration:** 3m12s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone and welcome back. So in this video we'll create some quick loading assets using a new lab stool and very basic valum setup.
[0:11] So here I have a new image put together in Photoshop that will be using to create our clouds.
[0:18] It helps to make them different colors so the tool can easily separate them.
[0:23] As you can see I'm using these new regions from image labs tool to automatically create masks.
[0:30] You just have to plug the image and wait for a few seconds.
[0:34] Then you can add a name attribute and rename your pieces as up to here.
[0:40] Getting rid of the black background and also the color associated.
[0:45] As we have a name attribute we can easily loop through the pieces and do some operations.
[0:50] I am resampling remashing and placing it in the center.
[0:55] Then measuring the curvature and in a group node we can select corners based on the curvature attributes.
[1:04] And we also need to subtract the bottom part of this selection.
[1:08] It would also help if we used a group expanding here so it grows the selection to use as pin points in valum.
[1:18] Okay so from here I have simulated and brushed the assets with the valum brush and this is the result I got.
[1:26] I guess these aren't euro props but can work well for me to background objects.
[1:33] I'm just going to quickly demo the workflow adding a valum plot and just changing the bend stiffness.
[1:40] Honestly I don't know what I'm doing here but seems to give me the result I wanted.
[1:46] So then we can create a valum brush, press enter and G to simulate.
[1:53] I forgot to set the pinning on the valum plot.
[1:56] After doing that we can reset the changes and simulate again.
[2:02] As I brush I can see this is way too low-res so let's go back and add some subdivisions.
[2:10] Now we need to add more points pins. I should have grown the selection as I told you before.
[2:16] For now let's just press shift middle click to pin some areas.
[2:21] Now you can brush till you feel it's looking somewhat decent and finally cash it.
[2:30] In this loop I'm just aligning it to the maxin-wise so it's next to the points I have for ending these pieces.
[2:39] Now we just copy the points with an attribute from pieces at random, deleting also randomly a few points.
[2:46] And of course if you have more variations it would look better.
[2:52] But for the amount of work we put into it doesn't look that bad.
[2:57] Okay guys I'll post an sample file on my Patreon and check out my step-by-step courses on procedural workflows.
[3:05] Thank you for watching and see you in the next one.



---

## Captured Frames

- [0:23] tutorials/frames/add-details-with-regions-from-image-labs-tool/frame_000.jpg
- [0:40] tutorials/frames/add-details-with-regions-from-image-labs-tool/frame_001.jpg
- [1:04] tutorials/frames/add-details-with-regions-from-image-labs-tool/frame_002.jpg
- [1:18] tutorials/frames/add-details-with-regions-from-image-labs-tool/frame_003.jpg
- [2:21] tutorials/frames/add-details-with-regions-from-image-labs-tool/frame_004.jpg

---

## Structured Notes

### Core Technique
Uses the **Labs Regions from Image** tool to auto-generate separate named pieces from a flat color-coded reference image (e.g. a clothing flat), then curvature-selects corner points on each piece and pins/brushes them into shape with basic Vellum cloth simulation.

### Summary
A quick workflow for turning a 2D color-coded reference image (made in Photoshop, with each intended piece painted a distinct flat color for easy separation) into a set of simulated cloth props. The Labs Regions from Image node auto-detects each color region as a separate named piece, which are then resampled/remeshed, corner-selected via curvature analysis, pinned, and brushed into a draped pose with Vellum. The presenter is explicit this is a fast/rough workflow suited for background props, not hero assets.

### Key Steps
1. Prepare a reference image in Photoshop where each intended piece (e.g. a shirt, a pair of pants) is painted a distinct flat color — flat, separable colors are what let the tool auto-detect regions correctly.
2. Add the **Labs Regions from Image** node, plug in the image, and wait a few seconds for it to auto-generate one region/piece per distinct color, discarding the black background and its associated color.
3. Add a **Name** attribute and rename each generated piece so they can be looped over individually afterward.
4. In a for-each loop over the named pieces: **resample** and **remesh** each piece, then recenter it.
5. **Measure** curvature (Gaussian) on each piece, then use a **Group** node to select corner points based on the curvature attribute values — subtract out the bottom-edge selection since it isn't a real corner.
6. **Group Expand** the corner selection to grow it slightly — these expanded points become the pin points for the Vellum sim (the presenter notes forgetting this step initially, which they had to fix afterward).
7. Set up a **Vellum Cloth** constraint network, then use the **Vellum Brush** tool (radius/mode/simulation controls in the brush's floating panel) to interactively drag/simulate each piece into a draped pose — press **Enter** then **G** to simulate as you brush.
8. Set **Pinning** on the Vellum constraints (a step that was initially missed and had to be corrected) so pinned points stay anchored while the rest of the cloth simulates/drapes.
9. If resolution looks too low/blocky while brushing, go back and add more subdivisions to the source mesh before re-simulating.
10. For quick manual pinning during brushing, use **Shift + Middle-click** to pin specific areas directly in the viewport.
11. To place multiple copies efficiently: use a for-each loop that copies points-with-attribute from the finished pieces at randomized positions, and randomly delete a few points for variation — more source variations would improve the final look further.
12. Bend Stiffness on the Vellum cloth object was adjusted ad hoc ("I don't know what I'm doing here but it gave the result I wanted") — treat as a trial-and-error parameter, not a prescribed value.

### Houdini Nodes / VEX / Settings
**Labs Regions from Image** (auto region/name generation from a flat-color reference image) → for-each loop: Resample → Remesh → recenter Transform → **Measure** (Gaussian curvature) → **Group** (corner selection by curvature, minus bottom edge) → **Group Expand** (grow pin selection) → **Vellum Cloth** constraints + **Vellum Brush** tool (Mode/Radius/Simulation controls, Enter+G to simulate, Shift+Middle-click to pin) → Bend Stiffness (manual tuning) → copy-points-with-attribute loop for randomized multi-placement.

### Difficulty
Intermediate — assumes familiarity with Vellum cloth setup and for-each/attribute-driven loops; the Labs tool itself is simple to use but the surrounding pin/curvature workflow requires some Houdini experience.

### Houdini Version
Not explicitly stated; the **Labs Regions from Image** node is part of the Houdini Labs tools (H20.5+ availability).

### Tags
#vellum #cloth #labs-tools #procedural #texturing #image-based #intermediate

---

## Related Tutorials
No other indexed cgside tutorial currently covers the Labs Regions from Image tool or this image-driven piece-separation technique — cross-link with any future Vellum cloth or Labs-tools tutorials once extracted from this batch.

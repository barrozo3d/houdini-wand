---
title: Procedural Modeling  | First steps with Houdini
source: YouTube
url: https://www.youtube.com/watch?v=L3Rvvv6pZ_8
author: cgside
ingested: 2026-07-13
houdini_version: "19.5.398"
tags: [beginner, boolean, revolve, groups, architecture, gothic, polywire, procedural-modeling]
extraction_status: complete
frames_dir: tutorials/frames/procedural-modeling-first-steps-with-houdini/
frame_count: 10
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Procedural Modeling  | First steps with Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=L3Rvvv6pZ_8)
**Author:** cgside
**Duration:** 16m51s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back to the channel. So I've been playing around with Odini for the past few days
[0:06] And I thought would be nice to share with you what I've learned so far
[0:13] So let's dive in
[0:15] Let's start by creating a geometry container and inside let's create a circle to start with give it a few subdivisions
[0:25] And let's clip it in the y-axis, which is the axis selected by default
[0:33] What we want to do is to boolean out two similar shapes
[0:40] So we can create a
[0:43] typical arc
[0:47] Of gothic cathedrals
[0:50] So as you can see I'm booleaning out two shapes one was transformed in the x-axis
[0:59] And now I'm using the curve notes to select parts of the
[1:05] the shape
[1:07] In this case you want to enable the second you also
[1:12] And play around with the keep outsides and inside
[1:19] you have to find the exact numbers
[1:31] So in the next step we are going to transform the shape back to the origin
[1:38] And
[1:43] And let's also clip all of it so we can use the revolve nodes to create the mesh
[1:56] In this case, I am just resembling the curve
[2:01] So we have a smother output
[2:03] And
[2:05] Now we can finally revolve the shape around and
[2:11] It's important to
[2:13] The number of subdivisions you're going to give to the this shape because later we win we need to do some meds
[2:23] So let's just fuse the points
[2:26] It's important and you will see why in the next steps
[2:31] This is just like a merge vertices in my am
[2:37] And now let's clip it in the z-axis negative in this way in this case
[2:46] Let's take the time also to save out our progress
[3:01] You can eat shift L to align all the nodes
[3:07] Just a good way to organize your graph
[3:12] So now we want to select the middle faces and for that I
[3:18] Know I want to select first lets enable the primitives or faces this number display
[3:26] So we know what we're dealing with and I want to select four of 14 in
[3:34] The range filter in this case if I disable the fused nodes you can see we have some issues at the top and
[3:42] Finally, you can just offset it by five in this case and we have the selection we we desired
[3:49] Let's just delete the non selected with group
[4:03] And now we need to create a shape to bullion out
[4:12] To create the panels
[4:14] So
[4:16] Let's just transform this original shape from the bullion output
[4:24] We want to set it back to the origin and scale it a bit down
[4:29] Let's group the bottom edges in this case. I'm going just to use the bounding regions and
[4:54] We can extrude those bottom edges
[4:57] selecting the group and setting to global and extrude it to the grid
[5:08] Now we can extrude again, but this time in the Z axis
[5:14] We can just use the distance attribute
[5:18] You may want to output the back, but in this case I believe I
[5:24] didn't
[5:26] Because I needed to delete that particular polygon later on
[5:36] So let's just disable the output back in the second poly extrude
[5:43] And now we can finally bullion out the two shapes
[5:54] So as you can see is a bit out of place. So let's place a transforming between and move it back in the Z axis
[6:04] And now we have the desired output
[6:14] So one important step here is that you can
[6:19] output
[6:22] the ab seams which is basically the those edges we where we where the shapes intersected
[6:31] So we can now use it to extrude back
[6:37] By selecting the group
[6:40] And as you can see it's just extruding those particular edges
[6:45] Let's just change the amount and set the scaling to Z to zero as we want a flat end to this shape
[7:04] And we can also add a bit of beveling again, we're using the same group
[7:10] 0.005 looks fine and let's add a few subdivisions so we don't have to deal with those
[7:20] annoying normal issues
[7:23] You still have a little bit but
[7:27] We can probably fix it later
[7:31] So let's select the bottom edges again in this case the keep by normals is isn't working as I wanted
[7:48] So I'm just using the bounding regions again
[7:55] And in the next step we will extrude it
[8:00] Selecting the group setting you to global and extruding it in the y axis in the negative y axis
[8:31] So now we want to divide 360 by seven in the y axis
[8:38] So we can
[8:40] duplicate the shape around and in this case the the seven is coming from the
[8:48] The amount of divisions we add in the original revolve you just basic met
[8:56] So we divide 360 by seven in the left panel and
[9:03] We make it negative in the right panel
[9:08] By multiplying by minus one
[9:11] Now we want to fuse the points as the shapes are were not merged
[9:17] And
[9:22] And let's tap would be to create those
[9:28] panels
[9:30] But before that let's select the
[9:34] The outside faces
[9:39] We can just stack to group by ranges and
[9:45] And in the second one we can set it to union union we did existing so we can
[9:58] So we can
[10:02] Select the boats off the sides of the shape
[10:09] And we can also delete the
[10:11] The
[10:13] The other parts
[10:18] Once again we're selecting the bottom edges to extrude down
[10:42] And let's add it back to the main merge node
[10:49] And as you can see we have the remaining parts of the
[10:54] The arc
[11:04] So now we want to create the
[11:07] The back panel to finish off the shape
[11:11] So let's select the
[11:14] The back face
[11:17] In this case we can use keep by normals and in the
[11:22] Z axis set it to minus one
[11:28] Blasts or delete the
[11:31] Non-selected
[11:34] Let's reverse also the polygons and group again the bottom edges to extrude it down
[11:56] Let's give it a few subdivisions also
[12:04] And now we can merge everything
[12:14] In this case I want to copy the same transforms
[12:20] So we can later attach the
[12:24] designs to the back panels
[12:27] And
[12:29] As we have a fuse node in between we don't want to
[12:34] To have the two shapes together
[12:56] Let's just take the time to select a few edges to create some sort of paneling
[13:05] In this case is the first time I'm going to use the
[13:09] The viewport to do it
[13:12] As I found this was this was much easier this was much easier this way
[13:20] So let's just
[13:23] click on an edge and
[13:25] Control shift a to select the edge loop
[13:31] This way you have more control over the edges that gets selected
[13:47] And now we can create a group in the viewport when you
[13:51] When you're in the viewport select it tab and create a group it will automatically be added to the graph
[14:01] And now we can create a
[14:04] D-solve node
[14:06] Play around with the settings we just want to output the curves
[14:13] In this case we need to dissolve non-selected
[14:20] And create curves
[14:25] Later I'm going back to disable
[14:31] Some settings and
[14:34] Finally we can create the
[14:39] The polywire
[14:44] And let's go back and remove unused points
[14:48] Let's just add a few subdivisions
[14:54] And we have the desired shape created
[15:01] And that's basically it
[15:06] Now I'm just going to walk it through the other shapes I created this would be just too much to
[15:14] To fit in a tutorial this is already going for some time
[15:22] So basically I'm creating some shapes with beveling and with some curves some lines
[15:31] Merging them
[15:35] And then moving them around
[15:41] In the end I have this result
[15:45] Creating some geometry from it and beveling out the edges
[15:55] Here I'm creating this flower shape just by creating a cylinder with four sides
[16:02] Coping a circle not a cylinder but a circle and copy two points
[16:09] four circles
[16:12] And then creating some other simple shapes too
[16:17] Merging it back with the back panel and in the end we have something like this
[16:26] So let me know what you guys think and if you would like to see more old iniconthent for the next videos
[16:34] I'm still going to make videos about Maya and by frost
[16:39] So yeah, let's let's see what's next. Thank you for watching and see you next time



---

## Captured Frames

- [0:20] tutorials/frames/procedural-modeling-first-steps-with-houdini/frame_000.jpg
- [1:35] tutorials/frames/procedural-modeling-first-steps-with-houdini/frame_001.jpg
- [3:30] tutorials/frames/procedural-modeling-first-steps-with-houdini/frame_002.jpg
- [4:50] tutorials/frames/procedural-modeling-first-steps-with-houdini/frame_003.jpg
- [7:10] tutorials/frames/procedural-modeling-first-steps-with-houdini/frame_004.jpg
- [8:10] tutorials/frames/procedural-modeling-first-steps-with-houdini/frame_005.jpg
- [10:10] tutorials/frames/procedural-modeling-first-steps-with-houdini/frame_006.jpg
- [13:10] tutorials/frames/procedural-modeling-first-steps-with-houdini/frame_007.jpg
- [14:20] tutorials/frames/procedural-modeling-first-steps-with-houdini/frame_008.jpg
- [16:30] tutorials/frames/procedural-modeling-first-steps-with-houdini/frame_009.jpg

---

## Structured Notes

### Core Technique
A beginner's first-steps walkthrough building a Gothic cathedral window/arch from scratch: the classic pointed-arch profile via two offset-Boolean'd circles, Revolve to loft the arch into a solid frame, then a long chain of group-based panel/tracery extrusions, Boolean cutouts, and finally hand-picked edge-loop selections converted to curves and Polywired into stone mullions.

### Summary
Starting from a subdivided circle clipped in Y, two copies are Boolean-subtracted (one offset in X) using Curve nodes to select portions of each circle (playing with "keep outside/inside" toggles) to produce the classic pointed Gothic arch profile. The profile is transformed back to origin, clipped, resampled for smoothness, and Revolved into a solid frame; points are fused (important for later steps) and the mesh is clipped again to remove the back half. Middle faces are selected procedurally via Group by Range using primitive-count math (`4 of 14`, offset by 5) rather than hardcoded indices, then deleted to leave the frame shell. A second Boolean pass (scaled-down copy of the original shape) carves the recessed window panels, using "output back" and B-seams groups to extrude the intersection edges back for a beveled inner reveal. Panels are further divided by duplicating the arch around Y using `360/7` (matching the original Revolve's column count) for radial repetition, then various group-by-range + bounding-region selections carve side/back faces and extrude them into the tracery framework. Finally, individual stone mullions/panes are hand-selected in the viewport using Ctrl+Shift+A (edge loop select) and Tab-created groups, then run through **Dissolve** (non-selected → curves) and **Polywire** to generate the rounded stone bars, finishing with a subdivision pass. The author notes the remaining shapes (rosette window, etc.) use the same beveling/curve/merge techniques repeated at a faster pace due to video length.

### Key Steps
1. Build the Gothic arch profile: Circle (subdivided) → Clip (Y-axis) → duplicate and Boolean-subtract two copies (one X-offset) using Curve nodes to select portions of each circle, toggling "keep outside"/"keep inside" to dial in the exact pointed-arch shape.
2. Transform the profile back to the origin, Clip fully, Resample for a smoother output, then **Revolve** around the shape to create the solid loft.
3. **Fuse** the points (important groundwork for later steps — "merge vertices" equivalent) and Clip again in -Z to remove the unneeded back half.
4. Select the middle faces procedurally: enable primitive-number display, use a **Group by Range** with a formula like "4 of 14" and an offset, rather than hardcoding indices — accounting for any Fuse-related topology quirks.
5. Delete the non-selected group to leave just the frame shell, then build a second shape (transformed back to origin, scaled down) to Boolean out the recessed window panels.
6. Group the bottom edges via Bounding Regions and **Extrude** them to the grid (global mode, using a distance attribute); a second Extrude along Z (with "output back" disabled where a polygon needs to be deleted later) creates depth, then Boolean the two shapes together — fixing any offset with an intermediate Transform.
7. Output the **AB-seams** group from the Boolean (the edges where the two shapes intersected) and extrude it back with scale-to-zero on Z for a flat-capped reveal edge, plus a small Bevel (0.005) with extra subdivisions to avoid normal artifacts.
8. Repeat the bottom-edge-group extrude technique (using Bounding Regions again since "keep by normals" didn't behave as expected) to extend the frame downward in -Y.
9. **Radial repetition**: divide 360 by the column count used in the original Revolve (7, in this case) to duplicate the left/right panel shapes around the arch, negating the angle for the mirrored side; fuse points since the duplicated shapes aren't merged by default.
10. Carve the outside/back faces using Group by Range (Union mode) plus Keep-by-Normals selections, extrude bottom edges down again, and merge the resulting panel geometry back into the main frame.
11. Build the back panel similarly: select the back face via Keep-by-Normals on Z, reverse polygons, extrude bottom edges down, subdivide, and merge (using a saved copy-of-transform so paneling designs align on the back too).
12. **Stone mullions/tracery**: manually select edge loops in the viewport (click an edge, then **Ctrl+Shift+A** for edge-loop select), Tab-create a group directly in the viewport, then use **Dissolve** (dissolve non-selected, output curves) and **Polywire** to generate rounded stone bars; remove unused points and add subdivisions for a clean result.
13. Author notes the remaining decorative shapes (flower rosette, etc.) reuse the same bevel/curve/merge/copy-to-points techniques shown earlier, applied repeatedly at a faster pace to keep the video manageable.

### Houdini Nodes / VEX / Settings
Circle, Clip, Boolean (two-pass: profile carving + panel recessing), Curve (selection on circles), Transform, Resample, Revolve, Fuse, Group by Range (primitive-count formulas, Union mode), Delete (by group), Bounding Regions selection, Extrude (grid/global mode, distance attribute, output-back toggling), AB-seams group extraction, Bevel, Keep by Normals, radial-duplication math (`360/columns`), Merge, viewport edge-loop selection (Ctrl+Shift+A) + Tab-created groups, Dissolve (non-selected → curves), Polywire, Subdivide, Copy to Points.

### Difficulty
Beginner-to-Intermediate (explicitly framed as the author's own early Houdini learning process; techniques are foundational but the overall Gothic-arch build is fairly involved).

### Houdini Version
19.5.398 (visible in viewport title bar).

### Tags
beginner, boolean, revolve, groups, architecture, gothic, polywire, procedural-modeling

---

## Related Tutorials
- [Procedural Bricks with Houdini](procedural-bricks-with-houdini.md) — direct continuation applying a parametric brick pattern to this same Gothic cathedral tower's base.
- [Procedural Modeling tips for beginners](procedural-modeling-tips-for-beginners.md) — companion beginner-tips video from the same early period of the channel.
- [Groups, Patterns in Houdini](groups-patterns-in-houdini.md) — deeper dive into the group-selection patterns (Group by Range, Bounding Regions, Keep by Normals) used extensively throughout this build.

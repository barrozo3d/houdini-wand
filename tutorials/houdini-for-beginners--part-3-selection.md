---
title: Houdini for Beginners-  Part 3:  Selection
source: YouTube
url: https://www.youtube.com/watch?v=9n4qDqi5qjc
author: Jordan Allen
ingested: 2026-08-08
houdini_version: "20.x"
tags: [beginner, selection, points-primitives-vertices, select-tool, lasso-select, area-select, row-selection, loop-selection, flood-fill, grow-shrink, jordan-allen]
extraction_status: complete
frames_dir: tutorials/frames/houdini-for-beginners--part-3-selection/
frame_count: 10
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini for Beginners-  Part 3:  Selection

**Source:** [YouTube](https://www.youtube.com/watch?v=9n4qDqi5qjc)
**Author:** Jordan Allen
**Duration:** 8m26s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Okay, let's talk about selection, right?
[0:02] There's gonna be a ton of this.
[0:04] Obviously, you've got to select what you want to edit if you're gonna do any editing.
[0:08] So I have a little scene here.
[0:09] We've got a camera, we've got a light, and we've got a sphere.
[0:12] Let's dive into the sphere here, and let's click on this little arrow right here.
[0:16] This is our select tool.
[0:18] With this active, we can click and drag and select the pieces that comprise our geometry.
[0:23] Now, when I say pieces that comprise our geometry, what do I mean?
[0:27] All geometry, if we open up our info here, and I'll click this little pin icon so it
[0:31] doesn't go away when I click away, we'll pin it to our screen, you can see that geometry
[0:37] is comprised typically of points, primitives, and vertices.
[0:42] Now we do have this little blue polygons thing at the bottom here, but this just refers to
[0:46] the type of primitive that the geometry is made of.
[0:49] If we switch this from primitive polygon to primitive nirbs, a different type of surface,
[0:56] and we can see here, when we update this, that now we have one primitive, and it is
[1:02] a nirbs surface primitive.
[1:05] I'll switch this back to polygon.
[1:07] In fact, I'll switch this back to polygon mesh.
[1:09] I like that shape better.
[1:11] Polygon gives us triangles, and polygon mesh gives us quads instead.
[1:17] So I'll stick with quads, we'll refresh this, and we can see that this sphere is comprised
[1:23] of 266 points, those are these things, you know, these big beautiful blue dots, 288 primitives,
[1:31] which are these things, these faces, and 1104 vertices, right?
[1:38] I can't remember where I heard this, but to me it's the best definition of what makes
[1:41] up geometry.
[1:42] You can almost think of it like a tent.
[1:44] The points are the nails.
[1:47] The vertices are the little loops that link into the tarp, and the primitives are the
[1:53] tarp themselves.
[1:54] You can think of each primitive as an infinitely stretchable tarp, but at the end of the day,
[1:59] however far you stretch it, we have to pin it into a place in 3D space somewhere in order
[2:05] to make up a shape.
[2:06] So here we can see, first we've got our tarp, right here, stretched to four distinct corners.
[2:14] We've got our points, our nails that are pinned into the ground, so to speak, our position
[2:19] in 3D space, and we have the vertices that are the little loops that the tarp is hooked
[2:25] onto that are connecting the two together.
[2:30] The vertices we do not edit very much, at least I don't in my workflows, so we're not
[2:33] going to worry too much about that.
[2:35] We want to manipulate mainly the points and the primitives.
[2:38] The vertices come more into play when we're dealing with UVs, which is going to be down
[2:42] the line a little bit in this tutorial series.
[2:44] For now, let's just focus on the points and the primitives.
[2:46] Again, with that select tool active, which you can just press S to activate, press 2
[2:50] on the keyboard, we can highlight our points, press 3 on the keyboard, we can highlight
[2:55] our edges, press 4 on the keyboard, we can highlight our faces.
[3:00] Now there's multiple ways to activate that besides 2, 3, 4.
[3:03] Those are just the ways that I use, I like them a lot, but you can also click up here.
[3:08] Whenever you have a tool or something active, if this area above the scene view is populated,
[3:14] typically it is in a way you can think of it as the tools parameters, ways to change
[3:19] the way that the tool operates.
[3:21] We'll be using stuff in there throughout the tutorial series, so you will get reps with
[3:24] that.
[3:25] But just know that these icons are there and they do change based on what you're doing
[3:28] in your scene.
[3:29] So we can select here, we can also click and hold over here and choose, hey, I want to
[3:34] select points or edges or primitives, etc.
[3:38] There's also additional tool parameters in each of these, if you click and hold.
[3:42] You can kind of see there's a little arrow to the bottom right of this icon.
[3:46] That indicates that by clicking and holding on it, it will reveal its parameters to you.
[3:51] So a good example for this is this area select visible geometry only.
[3:55] Now also note there are shortcuts for all of these on the right hand side if shortcuts
[4:00] are set by default for Houdini.
[4:01] So if we click and hold this box, hover over the area select visible geometry only and
[4:06] let go, it will check box it.
[4:11] I pointed to the screen like you could see my finger, which is just an insane thing to
[4:14] do.
[4:15] But point is it is check boxed it, which means now that parameter is active in our tool.
[4:19] So if I go to click and drag and highlight, you will notice it only selected the visible
[4:25] geometry base drop.
[4:27] That's pretty cool.
[4:28] Right.
[4:29] And if we hit shift V to get rid of that, now when I do the same exact thing, it selected
[4:35] all the geometry.
[4:36] So these are little tool parameters that you can utilize to best navigate and select in
[4:40] your scene.
[4:41] Now when it comes to selecting itself, let's say the box is not the ideal choice.
[4:45] You know, let's say something is very close to this object and we want to kind of, you
[4:49] know, drag around and navigate a little bit nicer in the points or the primitives that
[4:55] we're selecting.
[4:56] When I had to switch back to point mode, and then if I click and hold on the arrow key,
[4:59] because we can see there's other options, this bottom right black arrow, if we click
[5:03] and hold on this, I'm going to choose lasso picking instead.
[5:06] Could have just pushed F3 if I wanted, but I'm going to let go on lasso picking and now
[5:11] round them up or I can brush select instead.
[5:17] You know, lots of different options.
[5:18] You'll also see, look, area select visible geometry only is here as well.
[5:22] This is what I was saying earlier where on Houdini, there's so many different ways to
[5:24] do these things.
[5:25] Like there's different ways to access these tools.
[5:27] There is no right or wrong answer.
[5:29] It's more just getting comfortable in the options that you have and finding what's best
[5:33] for you.
[5:34] Now let's say click and drag is not the way that I want to select these things.
[5:37] Let's say I want to select this face and this face.
[5:41] Well if I hold shift and click, I can add additional faces or points or edges to my
[5:45] selection.
[5:46] If I control and click, I can get rid of those from the selection.
[5:49] I can also click and drag with shift to add additional things.
[5:54] If you don't hold shift, it will replace your selection every single time.
[5:57] So shift is how you additively add to your selection and control is how you can remove
[6:04] from that selection.
[6:06] Another handy thing is selecting lines of polygons.
[6:08] Right.
[6:09] A lot of the times are if our topology is clean, we may want to select a clean streak of polygons
[6:14] for whatever reason.
[6:15] If you click, hold shift and a at the same time.
[6:19] That's essentially if you think about it, a is short for all.
[6:22] So if you're holding shift, you say I want to add while holding a down as well as saying
[6:25] I want to add all the polygons between that first selection and this next one.
[6:30] You then left mouse button click and congratulations.
[6:32] You've got a row.
[6:33] But if you click, hold shift and a and middle mouse button instead, it will select a loop.
[6:40] Right.
[6:41] I won't go into too many more of these because I don't want to overwhelm you with them.
[6:44] But those two in particular shift, shift and a and click and shift and a and middle mouse
[6:52] button click are very, very handy.
[6:54] So they're good to kind of put in the back of your mind.
[6:57] There's also helpful things like holding shift and G to grow or shift and S to shrink.
[7:03] Right.
[7:04] G for grow as for shrink.
[7:06] Most of the shortcuts in Houdini are pretty well thought out.
[7:09] I think.
[7:10] And then the last one that I'll give you here, if you hold shift and a middle mouse button
[7:14] click, we've got another loop now.
[7:16] If I hold shift and H, this is the flood fill.
[7:20] I mean, you can actually see here at the bottom while I'm holding it.
[7:23] Look, hold a to select full middle mouse button on partial left middle mouse button on loops
[7:28] like we talked about, or hold H to select by flood fill.
[7:32] That basically just says, you know, this is actually a better example.
[7:36] I'll highlight this.
[7:41] And I'll highlight this and by holding shift and H now we are going to flood fill everything
[7:48] between the two selections.
[7:50] So in this way, you're essentially coloring in the edges of your object and then fill
[7:57] selecting the center of that.
[7:59] Right.
[8:00] Now I know I'm going into a lot of detail, so don't stress yourself out over memorizing
[8:03] all of this.
[8:04] And I may make this reminder a few more times.
[8:06] This is more just so you know some of the capabilities that we will be tapping into
[8:11] in the future.
[8:12] So take it by surprise.
[8:13] If you enjoyed this video and you want to learn more, head to doublejumpacademy.com
[8:17] slash Jordan for the full course.



---

## Captured Frames

- [0:12] tutorials/frames/houdini-for-beginners--part-3-selection/frame_000.jpg
- [0:37] tutorials/frames/houdini-for-beginners--part-3-selection/frame_001.jpg
- [1:31] tutorials/frames/houdini-for-beginners--part-3-selection/frame_002.jpg
- [2:50] tutorials/frames/houdini-for-beginners--part-3-selection/frame_003.jpg
- [4:06] tutorials/frames/houdini-for-beginners--part-3-selection/frame_004.jpg
- [5:06] tutorials/frames/houdini-for-beginners--part-3-selection/frame_005.jpg
- [5:41] tutorials/frames/houdini-for-beginners--part-3-selection/frame_006.jpg
- [6:19] tutorials/frames/houdini-for-beginners--part-3-selection/frame_007.jpg
- [6:40] tutorials/frames/houdini-for-beginners--part-3-selection/frame_008.jpg
- [7:48] tutorials/frames/houdini-for-beginners--part-3-selection/frame_009.jpg

---

## Structured Notes

### Core Technique
Foundational selection mechanics: what points/primitives/vertices actually are, the component-mode shortcuts to select each, the Select tool's own toggleable parameters (visible-geometry-only, picking style), additive/subtractive selection with Shift/Ctrl, and several higher-level selection shortcuts (row, loop, grow/shrink, flood fill) for working with clean topology.

### Summary
With the Select tool active (shortcut **S**, the arrow icon), geometry breaks down into three component types, explained with a tent analogy: **points** are the nails (pinned positions in 3D space), **vertices** are the loops connecting the tarp to the nails (rarely edited directly — mainly relevant later for UV work), and **primitives** are the tarp itself (the actual face/surface, infinitely stretchable until pinned down by its points). The node-info panel (pinned open via its pin icon) confirms exact counts — e.g. a default sphere shown here has 266 points, 288 primitives, 1104 vertices — and also shows the primitive type at the bottom (switching from Polygon to NURBS changes the sphere to a single NURBS-surface primitive; switching between Polygon [triangles] and Polygon Mesh [quads] changes the underlying tessellation — the presenter prefers Polygon Mesh/quads).

**Component mode shortcuts:** with Select active, press **2** for Points, **3** for Edges, **4** for Faces/Primitives (equivalently clickable/holdable from the mode icon in the tool's parameter row above the viewport, which also exposes each tool's own sub-parameters via click-and-hold — indicated by a small arrow in a tool icon's corner). One useful toggle there: **"Area Select Visible Geometry Only"** (shortcut **Shift+V**) — enabled, a drag-select only grabs components actually visible/unoccluded from the current camera angle; disabled (default toggle state varies), a drag-select grabs everything within the 2D marquee regardless of occlusion, including geometry hidden behind the near side of the object.

**Picking style:** click-and-hold on the selection-mode arrow icon reveals alternatives to the default box/marquee select — **Lasso** picking (shortcut **F3**) for freeform region selection, and **Brush** select for painting a selection by dragging over components.

**Additive/subtractive selection:** a plain click/drag **replaces** the current selection. **Shift**+click or Shift+drag **adds** to the selection; **Ctrl**+click **removes** from it.

**Row and loop selection (clean topology):** with two components already selected, **Shift+A held, then left-click** a third component selects a straight **row** of polygons/edges between the first two selections ("A" mnemonic: add-all-between). **Shift+A held, then middle-click** instead selects a full **loop** (e.g. a ring band around a sphere) rather than just a straight segment — the on-screen hint text spells this out live: hold A + left-click for a partial/row selection, A + middle-click for a full loop.

**Grow/shrink/flood fill:** **Shift+G** grows the current selection outward by one ring of adjacent components; **Shift+S** shrinks it inward by one. **Shift+H** is flood fill: select two separate regions/boundaries first, then Shift+H fills in and selects everything topologically "between" them — described as effectively coloring in the boundary edges and then fill-selecting the interior.

The presenter repeatedly notes there's no single "correct" way to select in Houdini — multiple UI paths (keyboard shortcuts, toolbar icons, click-and-hold sub-menus) reach the same result, and the point of this video is exposure to the options rather than memorization.

### Key Steps
1. Activate the Select tool (**S**).
2. Switch component mode with **2** (points) / **3** (edges) / **4** (primitives/faces), or via the mode icon in the tool-parameters row above the viewport.
3. Toggle **Area Select Visible Geometry Only** (**Shift+V**) when you want drag-selects to ignore occluded/hidden-side geometry.
4. Switch picking style via click-and-hold on the select-mode icon: default box/marquee, **Lasso** (**F3**), or **Brush**.
5. **Shift**+click/drag to add to a selection; **Ctrl**+click to remove from it; plain click/drag replaces it.
6. With two components selected, hold **Shift+A** and **left-click** a third for a row selection between them, or **middle-click** for a full loop instead.
7. **Shift+G** / **Shift+S** to grow/shrink the current selection by one adjacency ring.
8. **Shift+H** to flood-fill select everything between two already-selected boundary regions.
9. Check the node-info panel (pinned open) to confirm exact point/primitive/vertex counts and current primitive type (Polygon/Polygon Mesh/NURBS) on any geometry.

### Houdini Nodes / VEX / Settings
Select tool (S) with component-mode toggles (Points=2, Edges=3, Primitives=4, also Vertices=5, Breakpoints=9 per the shown menu), tool-parameter toggles: Area Select Visible Geometry Only (Shift+V), Area Select Fully Contained Geometry (Shift+C), Select Front/Back Facing options, Select Groups/Connected Geometry, Select Whole Geometry, picking-style submenu (Lasso F3, Brush), selection modifiers Shift (add) / Ctrl (subtract), Shift+A+LMB (row), Shift+A+MMB (loop), Shift+G (grow), Shift+S (shrink), Shift+H (flood fill). Sphere node's Primitive Type parameter (Polygon vs. Polygon Mesh vs. NURBS) as a demonstration example. Node-info panel (pin icon to keep it open) for point/primitive/vertex counts.

### Difficulty
Beginner — no procedural technique, pure selection-tool/keyboard-shortcut reference.

### Houdini Version
Not explicitly stated; part of the same Houdini 20.x beginner series as Part 2.

### Tags
beginner, selection, points-primitives-vertices, select-tool, lasso-select, area-select, row-selection, loop-selection, flood-fill, grow-shrink, jordan-allen

---

## Related Tutorials
- [Houdini for Beginners - Part 2: Navigation](houdini-for-beginners---part-2-navigation.md) — same beginner series; that part covers viewport/UI navigation and node flags, this part covers component selection mechanics.
- [Houdini for Beginners - Part 4: Tools](houdini-for-beginners--part-4-tools.md) — same beginner series; this part covers component selection, that part covers the transform/handle tool and node creation.

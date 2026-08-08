---
title: Houdini for Beginners-  Part 6:  Visualisers
source: YouTube
url: https://www.youtube.com/watch?v=ebFJhYj54Cg
author: Jordan Allen
ingested: 2026-08-08
houdini_version: "20.x"
tags: [beginner, visualizers, display-options, uv-grid, display-normals, point-trails, point-numbers, primitive-numbers, background-color-scheme, particle-display, jordan-allen]
extraction_status: complete
frames_dir: tutorials/frames/houdini-for-beginners--part-6-visualisers/
frame_count: 11
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini for Beginners-  Part 6:  Visualisers

**Source:** [YouTube](https://www.youtube.com/watch?v=ebFJhYj54Cg)
**Author:** Jordan Allen
**Duration:** 10m19s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Now, for this next section of the right-hand toolbar, I'm going to create a test geometry.
[0:05] There's a lot of very helpful test geometries in Houdini that you can use for various purposes.
[0:10] They're basically built as a starting ground for testing.
[0:13] You know, if you're testing your systems and you want a specific setup piece of geometry,
[0:17] you can do that. I'm going to create my absolute favorite inside of Houdini.
[0:20] I think it's everyone's favorite. It's the pig head.
[0:23] This beautiful monstrosity right here. We're going to work with this for the next section.
[0:28] Because right here, we have something that is on by default.
[0:32] And if you hover over it, you'll see what it is. It says display material on objects.
[0:36] Now, this object, the way that it's constructed and its internals, right,
[0:40] it has a material already assigned to it. So that's why we're seeing it in the viewport,
[0:45] versus just if I created a sphere, it has no texture, it has no UVs. It's like not set up for it.
[0:50] But this test geometry is preset up with all of these things.
[0:54] So we can see its material here, but there are times where we don't want to be
[0:58] encumbered by seeing the material. And so this button right here, we'll toggle that on and off.
[1:04] A sibling to this button is the one down here, which visualizes the actual UVs.
[1:10] It creates a very helpful grid pattern that lets us understand kind of how our UVs are divided.
[1:15] Again, this is something we are going to go into, into great detail on in the future.
[1:19] But in order to have a material tethered to your object in any
[1:24] sensical way, the object needs to have UVs to tell it how to apply that material.
[1:30] Right? It's okay if that doesn't make sense. Now, point is, if I turn off the material
[1:34] and I toggle this on, we will see, well, we see nothing. Okay, so I'll click and hold
[1:40] and I'll actually let go on UV grid gray or UV color. Okay, we're having some weird glitch here.
[1:47] That's okay. Typically, if you toggle that, it'll show up, but I'm kind of glad you saw that,
[1:50] because if it doesn't, just go ahead and click and hold and then just reset it by
[1:54] selecting something different. These are all just different visual variations of the same thing,
[1:58] but we can see the grid pattern that I'm talking about. This is how the UVs are constructed.
[2:02] Now you can have these both on at the same time. This is not how it should look.
[2:08] This is as good as time as any. Sometimes the scene view will jank the heck out.
[2:14] It's very strange. It doesn't happen nearly as much as it used to,
[2:18] at least in my experience. But if this ever happens, you can reset the viewport very easily.
[2:24] By going up to this labs tab, you can just click reset viewport. And now it'll basically
[2:30] relaunch the whole thing and say, okay, I don't know where we got lost there, but let's start over.
[2:35] Why don't we start this relationship over again, keep it healthy. So now you can see,
[2:38] yeah, you can have both active there at the same time. It doesn't really matter. Again,
[2:43] these are just visibility preferences. So what else do we have down this right hand side? Well,
[2:47] we have, we have some very helpful visual displays. Now you've heard me talk about
[2:54] visualizers a bunch to this point, right? With the handles and whatnot. Working in Houdini
[2:58] is predicated largely on being able to understand the information that you're looking at, right?
[3:02] And there are so many ways to do that. And there are so many different visualizers that you can
[3:06] even make to make sense of your scene. And right out the gate, there are some helpful ones that
[3:10] they have prepared for us. One is display points, right? This is comprised of lots of different
[3:16] points, but I can't see any of those points. The other geometry is in the way. So how do I
[3:21] know, right? If I go into select mode and I press two, I can see those points.
[3:25] But what if I want to see those points while I have the transform tool active? Well,
[3:28] by clicking display points, that visualizes the points no matter what, right? It will
[3:34] prioritize the visualization of the points in the mesh, which is very helpful.
[3:38] If we go down, we have display normals as a quick overview of what normals are. I'll give you
[3:45] my rendition of how I like to think of them. It's basically directional information from the surface
[3:51] that is conveying to the lights in the scene, what direction the light should bounce kind of conveying
[3:56] which direction is out. So if we create a normal node here, this will generate normals. Let's just
[4:03] change add normals to points for the sake of this visualization. Now, if we click this
[4:07] visualizer button for display normals, we will see a look. There are normals that are pointing
[4:12] essentially out and away from the surface. We'll use these a ton, but this is a very quick and
[4:17] easy way that we can visualize what our normals currently are, right? We can visualize our points
[4:22] and our normals. We can also visualize point trails. Point trails are essentially the opposite
[4:28] of the way normals are constructed. Normals point in the direction that they're aiming, whereas
[4:32] trails point in the direction that they just were. Where is this useful? Well, if we add some motion,
[4:39] so let's keyframe animate our pig here. I'll move it over here. We've got some motion there. The
[4:47] point is not the animation here. The point is that it is moving, right? And if we then create
[4:54] the trail node to create some velocity, basically what we are doing is we're computing
[4:59] where it was in the previous frame, where each point was in the previous frame,
[5:03] and are calculating a velocity value for that. We can visualize that with this trails button
[5:08] right here, display point trails. So what you're seeing is where we came from,
[5:17] which is helpful. Now, if I increase this value, just so we can see it, if I make it way more
[5:26] dramatic, moving way, way faster, you'll see that the point trails have gotten bigger too,
[5:32] right? They are essentially showing exactly where those points were the previous frame before,
[5:36] which is good when we're trying to navigate motion blur and we're trying to navigate other things
[5:40] in Houdini. So just know this is how to display point trails. You can also visualize the point
[5:47] numbers. This will become very important down the line, but each point has a unique number that
[5:52] is associated with it is how Houdini tracks all the data and information that's going on in the
[5:56] scene. We can visualize that with this down here. We can also display the primitive numbers, right?
[6:01] They also have associated number values. So Houdini knows what to do with those as well,
[6:05] because remember the points, the vertices and the polygons are all separate entities that are
[6:09] working together to create this geometry, but they all have their own unique identification. So
[6:14] Houdini knows what is what. And then the other major thing that I use all the time is this right
[6:18] here visualization. This tab we will go into as we actually create things in our scenes.
[6:24] By right clicking on this, we can see a lot of gobbledygook that probably doesn't make any
[6:29] sense to us right now, but just know that this tab is to toggle on and off the custom visualizers
[6:35] that we make, because again, these are all presets for our pleasure, so to speak, but we may want
[6:40] to create custom ones to visualize in the way that we want to visualize because we are free entities
[6:46] up in Houdini. So this is how we toggle that on and off once we've created them. So we will
[6:51] definitely play with that quite a bit moving forward. Would you believe me if I told you
[6:56] this was just the tip of the iceberg? Do you remember up here in the shelf where I click the
[7:00] plus button and all of a sudden there's a whole bunch of other shelves that aren't visible? Well,
[7:04] the same is true for the display settings, right? We've got all of these options here that are
[7:08] pertinent and important, and that's why they're promoted to the surface for us to interact with
[7:12] them this way. If you select the scene view and you press D, we get a pop up of our display options,
[7:18] right? These are these. How do we know that? For example, well, if we check to show point numbers
[7:25] in here, we can see that the point numbers toggle activates here. These are interconnected. A lot
[7:31] of these are interconnected. The normals are interconnected. The point visibility is interconnected,
[7:36] but we also have access to a whole host of additional controls that we don't on the
[7:41] toolbars, right? Just due to space real estate, really. One of the most important is in the
[7:46] background tab here. You can even see that these are organized very nicely. Markers, guides, geometry,
[7:51] scene, camera, like these display controls are organized in a way that makes finding them very,
[7:58] very simple, but there's a great deal of flexibility that exists. For example, one of the major ones
[8:03] that I use all the time is in the background tab. We have the color scheme of the display section.
[8:08] If you are working with white smoke and you have a light background, oftentimes it makes it difficult
[8:13] to judge the density of that smoke in the window. You can easily change from a color scheme of light
[8:19] to dark, right? Or gray. You can even customize if you want to get real fancy with it. I don't do
[8:25] that myself. But point is there's a ton of options in the display pop up that we can use to further
[8:31] help visualize our scene. I'll give you one more example. If we drop another sphere down,
[8:36] I'm actually going to go inside this and I am going to add an ad node, which, you know, has this
[8:43] very helpful toggle where I can delete all the geometry, but keep the points. So, you know,
[8:47] basically point is I just want the points from this sphere for now. I'm going to toggle off this
[8:51] visibility here and just see the points as they are in the scene. Now let's say I want to make
[8:55] these points more visible. For example, well, there's no options on the right hand side for that.
[8:59] But I know that in the display options in the geometry tab, I have control over the particles
[9:05] themselves, at least how they're visualized. So here we have display particles as points.
[9:11] And then we have a point size by clicking and dragging this. I can actually increase
[9:15] the size of the points in my scene. If I have a massive point simulation that we'll see later,
[9:21] we may not want to visualize them as points at all because the points are too big and doesn't
[9:25] give us a good understanding of the shape and dimensionality of our simulation, in which case,
[9:30] we can change the actual display to instead of being points, be no bigger than pixels. Now,
[9:35] right now, I don't have nearly enough. But if you have enough particles stacked on top of each
[9:39] other, visualizing them as pixels instead of points is very, very helpful in understanding
[9:44] what we're looking at. So just be aware, we don't need to know a great deal of this right now. We
[9:50] will use it sparingly throughout the duration of this course. And you'll start to, you know, pick up
[9:55] little tricks along the way. But just know that this is here, right? A deeper well of display
[10:01] control for us in terms of navigating the information inside of our scene view.
[10:06] If you enjoyed this video and you want to learn more, head to doublejumpacademy.com
[10:10] slash Jordan for the full course. Links in the description. You just click away. Click it.



---

## Captured Frames

- [0:23] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_000.jpg
- [1:40] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_001.jpg
- [3:21] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_002.jpg
- [4:07] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_003.jpg
- [5:08] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_004.jpg
- [5:26] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_005.jpg
- [5:52] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_006.jpg
- [6:01] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_007.jpg
- [7:18] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_008.jpg
- [8:19] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_009.jpg
- [9:11] tutorials/frames/houdini-for-beginners--part-6-visualisers/frame_010.jpg

---

## Structured Notes

### Core Technique
The rest of the right-hand viewport toolbar's display/visualizer toggles (material + UV grid display, viewport reset, per-attribute visualizers for points/normals/point-trails/point-numbers/primitive-numbers, custom visualizer stashes) plus the much deeper **Display Options** popup (**D** key) that houses everything not promoted to a one-click toolbar icon, including per-scene background color scheme and particle/point display size — all viewport-only conveniences for reading a scene's data, unrelated to render output.

### Summary
Demonstrated using Houdini's built-in **pig head** test geometry (one of several premade test-geometry presets meant as starting points for testing systems) — unlike a bare primitive (e.g. a default sphere), it ships with a material and UVs already set up, so it displays shaded/textured by default. **Display Material on Objects** toggles whether that assigned material renders in the viewport at all; its sibling, the **UV grid visualizer**, overlays a checker/grid pattern derived from the object's actual UV layout so you can sanity-check UV distribution without a real texture — both toggles can be active simultaneously, and picking a different option from the click-and-hold submenu (UV Grid Gray / UV Color) can also serve as a manual "reset" if the viewport visually glitches (which the presenter notes still happens occasionally, though less than it used to) — a persistent glitch can also be cleared via the **Labs** tab's **Reset Viewport** command, which fully relaunches the viewport display.

**Attribute visualizers:** **Display Points** forces point markers to stay visible regardless of which tool/mode is active (normally you'd only see points in Select mode + points sub-mode) — handy when you want point visibility while, say, the transform handle is active. **Display Normals** shows each point's normal as a directional line pointing "out" from the surface — conceptually, the direction information a surface uses to tell lights which way is outward-facing (demonstrated by adding a `normal` node first, since raw geometry may not have normals authored). **Display Point Trails** is the inverse idea: rather than showing where a point is currently facing, it shows a line back to where each point *was* on the previous frame, computed via a `trail` node that derives per-point velocity from frame-to-frame position differences — demonstrated on a keyframe-animated pig; scaling the trail node's velocity value up produces visibly longer trail lines, and this is specifically useful for reasoning about motion blur and other velocity-dependent effects. **Display Point Numbers** and **Display Primitive Numbers** overlay each point's/primitive's unique index — Houdini identifies and tracks every point, vertex, and primitive by such an ID internally, and these visualizers surface that bookkeeping directly in the viewport (useful later once VEX/expressions reference points and primitives by number). A separate **visualizers tab** (right-click for existing/preset visualizer definitions) is where custom, user-authored visualizers can be toggled on/off — a deeper topic that gets its own attention later in the series.

**Display Options popup (press D with the Scene View focused):** the toolbar only has room for the most common toggles; D opens a full popup covering everything else, organized into tabs (Markers, Guides, Housing, Geometry, Scene, Camera, Lights, Material, Fog, Grid, Background, Texture, Optimize as shown on screen). Toggles here are two-way synced with the toolbar buttons already covered (e.g. checking "Show Point Numbers" here lights up the same toolbar icon). Two examples highlighted: (1) in the **Background** tab, the viewport's **color scheme** (light/dark/gray, or fully custom) — useful for e.g. judging white smoke density, which is hard to read against a light background and easier against dark; (2) in the **Geometry** tab, **Display Particles as Points** plus a **point size** slider for enlarging how big points render in the viewport — and, for genuinely massive point counts (large simulations), switching the display mode to render points **no bigger than pixels**, since oversized point markers on a dense simulation can obscure the actual shape/silhouette you're trying to read.

### Key Steps
1. Toggle **Display Material on Objects** to show/hide a geometry's assigned material in the viewport (only meaningful if the object actually has a material + UVs, unlike a bare default primitive).
2. Toggle the **UV grid** visualizer (UV Grid Gray / UV Color via click-and-hold) to sanity-check UV layout without a real texture; re-picking an option here can also clear a visual glitch, or use **Labs → Reset Viewport** for a full reset.
3. Use **Display Points** to force point visibility regardless of active tool/mode.
4. Add a `normal` node and use **Display Normals** to visualize surface-outward directions per point.
5. Add a `trail` node (after some keyframed motion) and use **Display Point Trails** to visualize where each point was on the previous frame — scale the trail's velocity value to make trails more/less pronounced; useful for reasoning about motion blur.
6. Use **Display Point Numbers** / **Display Primitive Numbers** to see each component's unique index directly in the viewport.
7. Check the right-click **visualizers tab** for existing custom visualizer presets (authoring your own is covered later in the series).
8. Press **D** in the Scene View for the full **Display Options** popup when you need a setting not on the toolbar — notably the **Background** tab's color scheme (helpful for judging density against light-colored volumetrics like smoke) and the **Geometry** tab's particle/point display size and pixel-sized rendering for very dense point sets.

### Houdini Nodes / VEX / Settings
Test geometry presets (pig head demoed), **Display Material on Objects** toggle, UV grid visualizer (UV Grid Gray / UV Color), Labs tab → **Reset Viewport**, **Display Points**, `normal` node + **Display Normals**, `trail` node (frame-to-frame velocity from position deltas) + **Display Point Trails**, **Display Point Numbers**, **Display Primitive Numbers**, visualizers tab (right-click, for custom/preset visualizer toggles). **Display Options popup** (**D** key): tabs Markers / Guides / Housing / Geometry / Scene / Camera / Lights / Material / Fog / Grid / Background / Texture / Optimize; Background tab's viewport color scheme (light/dark/gray/custom); Geometry tab's **Display Particles as Points** + point-size control + pixel-sized display mode for dense simulations. `add` SOP (used here with its delete-geometry-keep-points toggle to isolate a sphere's points for the particle-size demo).

### Difficulty
Beginner — pure viewport-display/UI reference, no procedural technique explained in depth.

### Houdini Version
Not explicitly stated; part of the same Houdini 20.x beginner series as Parts 2-5.

### Tags
beginner, visualizers, display-options, uv-grid, display-normals, point-trails, point-numbers, primitive-numbers, background-color-scheme, particle-display, jordan-allen

---

## Related Tutorials
- [Houdini for Beginners - Part 5: The Viewport](houdini-for-beginners--part-5-the-viewport.md) — same beginner series; that part covers shading modes/layout/camera-lock/viewport lighting, this part covers the remaining display/attribute visualizer toggles and the full Display Options popup.

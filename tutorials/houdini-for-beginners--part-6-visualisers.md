---
title: Houdini for Beginners-  Part 6:  Visualisers
source: YouTube
url: https://www.youtube.com/watch?v=ebFJhYj54Cg
author: Jordan Allen
ingested: 2026-08-08
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-for-beginners--part-6-visualisers/
frame_count: 0
frame_status: pending-selection
---

# Houdini for Beginners-  Part 6:  Visualisers

**Source:** [YouTube](https://www.youtube.com/watch?v=ebFJhYj54Cg)
**Author:** Jordan Allen
**Duration:** 10m19s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-for-beginners--part-6-visualisers <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


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

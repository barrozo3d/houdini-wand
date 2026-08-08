---
title: Houdini for Beginners-  Part 8:  The Geometry Spreadsheet
source: YouTube
url: https://www.youtube.com/watch?v=KnUXXm7YVSU
author: Jordan Allen
ingested: 2026-08-08
houdini_version: "20.x"
tags: [beginner, geometry-spreadsheet, attributes, points-vertices-primitives-detail, attribute-create, blast-node, random-attribute, color-attribute, jordan-allen]
extraction_status: complete
frames_dir: tutorials/frames/houdini-for-beginners--part-8-the-geometry-spreadsheet/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini for Beginners-  Part 8:  The Geometry Spreadsheet

**Source:** [YouTube](https://www.youtube.com/watch?v=KnUXXm7YVSU)
**Author:** Jordan Allen
**Duration:** 7m19s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Alright, so moving on, there is one more tab that I want to introduce you to.
[0:03] You can see up here, there are a collection. There's six total.
[0:06] The only one that I want to cover right now really is the Geometry Spreadsheet,
[0:10] because this is one that we're going to be using a lot.
[0:12] If we go ahead and click on this, we can see
[0:15] what really appears to be a whole lot of gobbledygook.
[0:17] I'm going to move this over here.
[0:20] A lot of data on this sheet.
[0:22] This sheet really is the hub of Houdini's brain.
[0:27] It is letting you know all the data that exists in your scene.
[0:31] We can maybe contextualize this a little bit more and help make sense of it.
[0:35] In the Sphere node itself, I am generating a color randomly
[0:40] based on the primitive, meaning every single primitive in this scene
[0:43] has been assigned a random color.
[0:45] Now, in the viewport, we are seeing that color, and that's all well and good.
[0:49] But what is the color comprised of?
[0:51] Well, a color attribute is comprised of three values.
[0:56] You can think of it as a red, blue and green value.
[0:58] You may be familiar with this in other DCCs, other softwares
[1:03] where you can create any combination of colors by assigning it a red value
[1:08] between zero and one, a green value between zero and one, and a blue value
[1:12] between zero and one.
[1:13] Now, in this way, it has assigned random values to the red, blue and green channel
[1:19] for the primitive.
[1:20] If you can think of any color as a combination of three values between zero and one
[1:25] in a red, blue and green channel, then it makes sense that the color
[1:29] that we're seeing is just a combination of those numbers.
[1:32] Those numbers are stored in the geometry spreadsheet.
[1:35] So I will toggle this button.
[1:37] I will toggle this button, sorry, to display the primitive numbers.
[1:41] Right.
[1:42] And we'll go to the top here and we can find number zero right here, zero, one,
[1:49] two, three, four.
[1:49] Yeah.
[1:50] So with zero active, we can see it's kind of like a purpley pinky color.
[1:55] You can see I did a lot of color study based on my deep knowledge of color
[2:00] names.
[2:01] But if we go over to the geometry spreadsheet and we go to the zero, well,
[2:06] the one thing I will show you right out the gate though is the geometry
[2:10] spreadsheet is separated into the points attributes, the vertices attributes,
[2:17] the primitives attributes and the detail attribute.
[2:22] Now the points, that's every point in our scene, vertices, every vertex
[2:26] in our scene, primitives, every primitive in our scene, but detail.
[2:30] That's the overall geometry.
[2:31] So we can assign attributes to the whole geometry as well, but just know
[2:35] that that's the breakdown.
[2:37] So considering that in our scene, I have color on the primitive class that is
[2:43] randomly being assigned.
[2:44] If we go to the geometry spreadsheet, right out the gate, you'll see
[2:47] there's no, there's no value at all.
[2:48] What is this?
[2:49] This is position of the points in 3d space or position X position,
[2:54] Y position Z, right?
[2:55] So that's where it is in 3d space.
[2:57] That makes sense.
[2:58] But if we go over to the primitives tab, now we can see CDR CDG and CDB.
[3:06] Right.
[3:06] This is the color for the red, blue and green channel.
[3:09] And we can see this is the color combination for the red, blue and green
[3:14] that makes up this color right here.
[3:17] And more so, we have every single primitives color combination, but attributes
[3:23] are not in any way limited to color.
[3:25] In fact, they're not limited to anything at all.
[3:27] You can create an attribute value from anything for anything.
[3:30] The point of these attributes, for example, is for, let's take the points.
[3:35] Each point in the scene to hold on to an important bit of information that
[3:39] can be used later in order to do another thing with that information.
[3:44] For example, if you have a particle simulation, you will have them hold on
[3:49] to their individual age, how long they have existed for in frames or seconds.
[3:54] And then you can delete particles that exist beyond five seconds
[4:00] because each particle knows how long it existed for.
[4:02] Points are very responsible adults.
[4:04] We give them a value and then when we call out that value, we say everyone
[4:08] with a value above X step forward.
[4:10] Those points step forward.
[4:11] The rest step back, right?
[4:12] It gives us control over a lot of different things and we can create
[4:17] them in a lot of different ways.
[4:18] For example, I will use an attribute create node right here.
[4:21] I'll turn off the bypass.
[4:22] I'll go down.
[4:23] I already created this, but you can see in the name.
[4:26] I created an attribute called new with a value of zero.
[4:31] Now it is going to create this on every single point, right?
[4:36] Class point in our scene and we can see that in the geometry spreadsheet.
[4:40] If it's bypassed, it doesn't exist, but the minute that we activate it,
[4:43] it has created an attribute that is called a new with a value of zero
[4:48] on every single point in our scene.
[4:50] And if I change that value to one, it's updated.
[4:54] It's updated across every single point.
[4:58] This by itself is not very useful, but like the examples I was talking
[5:00] about earlier, let's look at a useful use case.
[5:04] Let's say, for example, we have this geometry and for whatever reason,
[5:08] we want to delete randomly half of the polygons on the geometry.
[5:12] This may happen if you have too dense of a point cloud with a particle
[5:17] simulation and you just want to randomly call half of the particles.
[5:20] How can we do this?
[5:21] Well, we'll go in and we'll go into this node later, but there's
[5:25] a very simple bit of code here where I'm basically creating a random attribute,
[5:30] a random float attribute.
[5:32] And on that attribute, I am randomly assigning a value between zero
[5:36] and one to each primitive on my geometry.
[5:39] Don't let this intimidate you.
[5:41] We will go into detail and this very soon will make a whole lot of sense.
[5:45] The point of this is that on the geometry now on the primitives in particular
[5:50] because that's where I ran it over.
[5:52] I have created a random value between zero and one.
[5:56] We can see that throughout the entirety of my geometry.
[6:00] Then what I'm doing is with a blast node.
[6:02] It's a simplified version of Houdini's delete node.
[6:04] You'll use it a lot.
[6:06] I am entering another little bit of code into the group that I want this to
[6:11] run over.
[6:11] I'm saying, Hey, if your attribute random that was assigned to you is greater
[6:15] than 0.5, I want you to get deleted.
[6:20] Step forward primitives.
[6:21] If your value is greater than 0.5 and they do, and then we delete them.
[6:25] So in this way, I have assigned a random value and then I have used it to delete
[6:29] geometry over the duration of this course.
[6:32] You will truly start to unlock the power of these attributes right in the geometry
[6:37] spreadsheet and then this way the geometry spreadsheet is very, very important
[6:41] to have on screen at all time.
[6:42] Now right now in its current configuration, we have to either see our scene view
[6:46] or see the data.
[6:48] Now wouldn't it be great if we could see both at the same time?
[6:50] Wouldn't that be fantastic?
[6:51] Well, that's exactly what we're going to do in the next video again,
[6:54] particularly for this topic.
[6:57] Please do not worry if this doesn't make full sense.
[7:00] It will because if I can understand it, I guarantee you with enough exposure to it,
[7:05] you can too.



---

## Captured Frames

- [0:20] tutorials/frames/houdini-for-beginners--part-8-the-geometry-spreadsheet/frame_000.jpg
- [1:49] tutorials/frames/houdini-for-beginners--part-8-the-geometry-spreadsheet/frame_001.jpg
- [2:47] tutorials/frames/houdini-for-beginners--part-8-the-geometry-spreadsheet/frame_002.jpg
- [3:06] tutorials/frames/houdini-for-beginners--part-8-the-geometry-spreadsheet/frame_003.jpg
- [4:21] tutorials/frames/houdini-for-beginners--part-8-the-geometry-spreadsheet/frame_004.jpg
- [4:48] tutorials/frames/houdini-for-beginners--part-8-the-geometry-spreadsheet/frame_005.jpg
- [5:32] tutorials/frames/houdini-for-beginners--part-8-the-geometry-spreadsheet/frame_006.jpg
- [6:02] tutorials/frames/houdini-for-beginners--part-8-the-geometry-spreadsheet/frame_007.jpg

---

## Structured Notes

### Core Technique
Introduces the **Geometry Spreadsheet** tab — described as "the hub of Houdini's brain" — as the raw-data view into every **attribute** on every point/vertex/primitive/detail in a scene, and uses it to make concrete what an attribute actually is (a named per-component value) via two examples: a built-in random-per-primitive color, and a hand-built random-float attribute used to drive conditional deletion.

### Summary
Houdini geometry is organized into four **attribute classes**, each with its own tab/section in the spreadsheet: **Points** (every point — e.g. `P` / position X, Y, Z by default), **Vertices** (every vertex), **Primitives** (every primitive — e.g. a Sphere node here has a "color by primitive" option turned on, which shows up as `Cd.r` / `Cd.g` / `Cd.b` columns, three float values 0-1 each combining to form the random per-primitive color seen in the viewport), and **Detail** (attributes on the geometry as a whole, not any individual component). Turning on **Display Primitive Numbers** and cross-referencing a specific primitive's index against its spreadsheet row is how you confirm which viewport color corresponds to which row of `Cd.r`/`Cd.g`/`Cd.b` data.

Attributes aren't limited to built-ins like color or position — **any name, any value, on any class** is fair game, and this is the core mechanism used throughout Houdini for passing information between nodes/steps. Canonical example given: a particle sim where each point holds an "age" attribute (frames/seconds it has existed), later used to delete any particle whose age exceeds a threshold — "points are very responsible adults... we give them a value, and then when we call out that value, we say everyone with a value above X, step forward."

**Manually creating an attribute:** an **Attribute Create** node lets you author a new named attribute (demoed: an attribute called `new`, value `0`, applied to every point) — bypassing/unbypassing the node makes the attribute disappear/reappear in the spreadsheet live, and changing its value updates every point that has it simultaneously.

**Practical pattern — random deletion:** to delete a random ~half of a geometry's primitives (motivating example: thinning an overly dense particle/point cloud), two nodes are chained: (1) a small VEX/wrangle snippet assigns a random float attribute between 0 and 1 to every primitive (not explained in depth here — flagged as a topic covered later in the series, just shown as a working example not to be intimidated by), then (2) a **Blast** node (described as a simplified version of the Delete node, used constantly) is given a group expression checking that random attribute — e.g. "if this primitive's random value is greater than 0.5, delete it" — which primitives satisfying the condition then get removed. This demonstrates the general pattern: assign a per-component value via an attribute, then reference that same attribute later to conditionally act on components (delete, select, drive a parameter, etc.).

The video ends by flagging a real limitation: right now you can only see either the Scene View or the Geometry Spreadsheet, not both at once — solved in the next part of the series with a custom split layout.

### Key Steps
1. Open the **Geometry Spreadsheet** tab to inspect all attribute data on the current node's output.
2. Understand the four attribute classes: Points, Vertices, Primitives, Detail — each row/column breakdown corresponds to a different component granularity.
3. Cross-reference a specific component (e.g. via Display Primitive Numbers in the viewport) against its spreadsheet row to connect a visible result (like a color) to its underlying attribute values (`Cd.r`/`Cd.g`/`Cd.b`).
4. Use an **Attribute Create** node to manually author a new named attribute on a chosen class, with a starting value applied to every component of that class.
5. To conditionally act on geometry based on a value: assign a per-component attribute (e.g. a random float via a wrangle), then reference that attribute in a downstream node's group expression (e.g. a **Blast** node's delete condition) to select/act on only the components matching a threshold.

### Houdini Nodes / VEX / Settings
Geometry Spreadsheet tab (Points / Vertices / Primitives / Detail attribute-class views), Sphere node's "color by primitive" random-color option (produces `Cd.r`/`Cd.g`/`Cd.b` primitive attributes), Display Primitive Numbers visualizer (cross-referencing viewport components to spreadsheet rows), **Attribute Create** node (name + starting value, applied across a chosen attribute class), a wrangle assigning a random float attribute (0-1) per primitive (implementation deferred to later in the series), **Blast** node (simplified Delete node; group expression referencing an attribute value, e.g. `random > 0.5`, to conditionally delete matching primitives).

### Difficulty
Beginner — conceptual introduction to attributes and the spreadsheet; the random-attribute VEX snippet is shown but deliberately not explained in depth yet.

### Houdini Version
Not explicitly stated; part of the same Houdini 20.x beginner series as Parts 2-7.

### Tags
beginner, geometry-spreadsheet, attributes, points-vertices-primitives-detail, attribute-create, blast-node, random-attribute, color-attribute, jordan-allen

---

## Related Tutorials
- [Houdini for Beginners - Part 7: Timeline and Animation](houdini-for-beginners--part-7-timeline-and-animation.md) — same beginner series; that part covers the timeline/keyframing/Flip Book, this part introduces the Geometry Spreadsheet and attributes.
- [Houdini for Beginners - Part 9: Layouts](houdini-for-beginners--part-9-layouts.md) — same beginner series; this part introduces the Geometry Spreadsheet and attributes, that part builds a custom layout so the spreadsheet and Scene View are visible together.

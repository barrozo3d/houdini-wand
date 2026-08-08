---
title: Houdini for Beginners- Part 10:  Contexts
source: YouTube
url: https://www.youtube.com/watch?v=i_xuEjjQtDc
author: Jordan Allen
ingested: 2026-08-08
houdini_version: "20.x"
tags: [beginner, contexts, obj, sop, chops, cops, mat, out, shop, tops, wedging, solaris, stage, usd, network-box, sticky-note, houdini-help, jordan-allen]
extraction_status: complete
frames_dir: tutorials/frames/houdini-for-beginners--part-10-contexts/
frame_count: 11
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini for Beginners- Part 10:  Contexts

**Source:** [YouTube](https://www.youtube.com/watch?v=i_xuEjjQtDc)
**Author:** Jordan Allen
**Duration:** 13m59s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Inside of Houdini, there are lots of different boxes where different work goes on.
[0:05] Now, those boxes, metaphorical boxes, so to speak, are contexts.
[0:11] You can think of it as, you know, in a school, there's a room for math, there's a room for English, there's a room for history.
[0:16] These are dedicated rooms to do dedicated things, but the students go between each of these rooms.
[0:22] So too can the information inside of Houdini be passed between these contexts.
[0:27] But it's more of an organizational structure in my understanding as to why it is laid out in this way.
[0:33] I'm sure there's probably some reason in the hood that I don't know about, but to me, I just like to think of it as, as organizationally based.
[0:40] Right? So for example, we are very familiar now with our OBJ level, right? Our geometry, our scene view, so to speak.
[0:46] And if we hop inside of one of these geometry nodes, now we enter the SOP contexts, right?
[0:52] Surface operators. This is the room dedicated for working on the internals of what makes this geometry what it is.
[0:59] We hop back out and we've got our scene view, our room dedicated to organizing our scene.
[1:05] But there are others. If you click on this dropdown right here, there is the CH room. What is this?
[1:11] This is the motion effects network. You can see in the top right, it actually tells you what the context is.
[1:16] This is known as CHOPs, channel operators, animation channel operators to be specific.
[1:22] And we're not going to go into vivid detail as to how to use all these things right now.
[1:27] I just want to introduce you to the rooms. We will be using this primarily when we do crowd stuff at the end of the entire course.
[1:36] There is the image context, also known as COPS, compositing operators.
[1:42] This is where you can actually do compositing. And I know Houdini is pouring a lot of resources into their compositing, right?
[1:47] Because there's a lot of power and potential. I still use Nuke myself for all of those things.
[1:51] So I don't really use the compositing context. But if you look by creating an image network and heading inside of it,
[1:57] you can create a compositing setup to get a final image if you want.
[2:02] For example, if I hit Tab and I type file, hit enter. By default, it loads this picture of a butterfly.
[2:09] I have no idea why or where this came from. It's kind of iconic at this point, though.
[2:14] Whoever came up with that, I wish it was the pig head, personally.
[2:19] But we've got our file that we can load in all the parameters for that.
[2:23] And then if we hit Tab again and type in color correct, hold shift and hit enter, now we can actually make changes.
[2:30] But we can't see where it is. Well, that's because the compositing context needs the compositing viewport.
[2:37] In this case, the composite view. It's one of the ones we closed earlier.
[2:41] If you hit plus and head over to Viewers, we can see composite view here.
[2:45] Just like the motion effects section would need the motion effects view in order to see what's going on.
[2:51] So now with the display flag over the file, we see the butterfly.
[2:55] And then with the display flag over the color correct, as we make changes, we can see the effects that that is having.
[3:02] We can make all the changes we want and then, you know, render out new imagery and whatnot.
[3:06] We've got the material context.
[3:09] The material context or matte context, as I'm sure you can expect, is for creating materials.
[3:15] This is going to be our little work zone for creating and generating materials that we can apply to our objects.
[3:22] If we hit this drop down again, we head on over to the OVJ. We know this one.
[3:26] So we'll move on to the out context. Now this is what Mantra used to use.
[3:31] I mean, it still does. I'm acting like it's dead. It's not dead. Mantra is still a thing.
[3:36] But again, they are slowly phasing it out in lieu of karma, the replacement.
[3:41] But this is where you would create and establish your Mantra settings.
[3:48] Gosh, I can't decide what to say with that.
[3:51] I'm going to go with Mantra. You can establish your Mantra settings, your ray samples,
[3:56] and all the different things that go into the final image.
[3:59] We will also not be using this, which is crazy because I've used this for the majority of my time in Houdini.
[4:04] But times change, and we got to change with them.
[4:07] There is also the shop context. Speaking of yesteryear, this was replaced with the matte context.
[4:14] Now my understanding is they still left this in here because people still have workflows
[4:17] and can design some really cool shaders inside of this context.
[4:21] I've never actually explored it because by the time I started getting into Houdini,
[4:25] Matt was already the dominant force there.
[4:28] You can do all the work that you needed in here.
[4:31] Just be aware, shop is that context. We also will not be touching on that.
[4:35] I'm going to skip stage because I'm going to go back to that one, but the task context,
[4:40] also known as Tops, task operators, this is where you can generate work items.
[4:46] Now that may make no sense to you at all, and that's fair because it is kind of a confusing concept.
[4:52] But inside of a top net, a task operator network, what you can do essentially,
[4:57] at least the only real use cases I've used it for is something called wedging.
[5:02] What does that mean? Wedging is basically taking multiple values for a parameter.
[5:06] Let's say how sticky a liquid is, for example.
[5:10] We got a stickiness of 1, a stickiness of 10, and a stickiness of 100.
[5:14] I want to see the results from all of those.
[5:16] Now, I can choose to one by one input those parameters and then see how it looks,
[5:22] or I can use task operators to let it know I want to try all three
[5:27] and allow that to generate work items that will iterate through each of those parameter values.
[5:33] Now that is the most simple version of a task operator structure.
[5:38] So I don't want to get too into the weeds there, but we will be using task operators to some degree
[5:44] over the duration of this course. So we will revisit these concepts.
[5:48] The last context I want to look at is the stage context.
[5:51] It's also known as Solaris.
[5:53] Solaris is Houdini's answer to USD workflow.
[5:58] Now, what is USD?
[5:59] USD is universal scene description.
[6:01] It is a file type, just like an OBJ or an FBX or a .abc, an Alembic file.
[6:07] It is a way of storing not only geometry like those structures,
[6:11] but you can also store a whole lot more cameras, materials, lighting, the universal scene.
[6:17] It is a description of the universal scene.
[6:19] The promise of this is the idea of sharing these USD files between softwares as well.
[6:25] So everything is speaking the same language.
[6:28] Don't worry about what that means in the larger scale.
[6:30] What I want you to take away from what the stage or Solaris context is,
[6:34] is this is your context for bringing in any aspects of your geometry, lighting or cameras
[6:40] from the OBJ context, bring them over here and prepare them for render.
[6:45] So typically my workflow is do all the geometry work and camera operation work in the OBJ level,
[6:51] import that into the stage or Solaris context, and then prepare it with lighting and materials
[6:58] and do all the final aspects in this context for render.
[7:01] I know that's a lot.
[7:02] It's a lot to go over.
[7:03] So just to hone focus a little bit here, the main ones we will be using are the OBJ context,
[7:09] and the stage context.
[7:11] Those will be the two that we bounce between the most.
[7:14] Okay, and as a final stop on this whirlwind tour of UI, I want to take a look at some of these helpful toggles
[7:23] that exist inside of the network view, because we're talking about organization, right?
[7:28] In the previous video, boxes for organization.
[7:30] But your workflow should also be organized visually.
[7:33] It's very helpful.
[7:34] It's very helpful specifically when revisiting past projects or by passing on a project to somebody else,
[7:40] they're able to more easily identify what it is that's going on.
[7:44] And there's only a few things I want to cover here.
[7:46] Inside of this, the OBJ context, we have our sphere, and it is displayed as just a white box node.
[7:51] If we create a light, for example, you'll notice not only is the shape different,
[7:56] shape of a light bulb, very clever, but it's also yellow by default.
[8:01] If we create a camera, we can see it's again a different shape and a different color.
[8:06] Well, these are defaults that Houdini have set up in order to, you know,
[8:10] illustrate more easily when you're looking from far away what's what.
[8:13] But we have total flexibility over the customization of all of these things, and it's very, very easy to do.
[8:19] If you're in the network view, you can press C for the color palette pop up,
[8:25] and you can just click and drag to expand or shrink that color palette.
[8:31] And now when I highlight a node and I click a color, it becomes that color, right?
[8:37] In this way, we can design our very own color coding system,
[8:40] or maybe the studio you're working at has a color coding system that just makes everything from a macro perspective a little easier to understand.
[8:46] The same is true by hitting Z. You get these shape pop ups, and now I can choose whatever shape I want.
[8:54] You'll start to see over the duration of this course that I have a very specific way of organizing these things,
[9:00] and you may love it or you may hate it.
[9:02] So feel free to change it if it's not your cup of tea, but it works for me.
[9:06] So I'm into it.
[9:07] Either way, we can just reset this very easily back to white in a box.
[9:11] I know I said I was going to talk about the buttons.
[9:13] I just want to show you this one shortcut real quick.
[9:15] If you highlight all the nodes that you want to order a little bit more, hold A, click and drag to the right or left.
[9:23] You'll see it drew them into a straight line.
[9:25] If I hold A and click and drag down, it will order them in a straight line top to bottom.
[9:32] So you can go left, right.
[9:34] You can go top to bottom.
[9:36] And you can do that for any of them, whatever one you're dragging on.
[9:39] You can use that as the anchor, so to speak, for your organization.
[9:44] I'm going to undo that so that it's a little more chaotic.
[9:47] I'll even drag these around.
[9:48] You can also hit L in your scene.
[9:51] And what it will try to do is order your nodes in a helpful way.
[9:56] This is hit or miss, right?
[9:58] This is a dangerous toggle because it could jack up your entire aesthetic and make your entire network view very, very confusing, very quick.
[10:05] So, you know, better to organize it yourself.
[10:09] I'm going to put all these back.
[10:12] I'm going to hit C to collapse that color palette there and head back over to the toggles at the top of this window.
[10:18] The next one I want to do is create network box.
[10:20] You can hit shift O to do that, or you can just click the button.
[10:24] If you highlight nodes and you click this, it will create a box around it that you can click and drag and expand.
[10:30] If you click on that box, hit color, you can also color code the box as well.
[10:35] By double clicking this right here, you can then name it box or geometry or lighting or whatever you want in order to keep it structured.
[10:44] And now by clicking this minimize button and plus button, we can expand and contract that again, further control over the visuals that we're seeing in a network view.
[10:53] The last one I want to look at in here is the sticky note.
[10:55] I use it all the time.
[10:56] If you click that button for the sticky note, you get a floating sticky note pop up this too.
[11:01] If you click on it, you can change the color.
[11:04] And then if you click inside of it, you can leave a note here.
[11:11] For a future artist, if there is something that they need to know, you can attach a sticky note for some helpful information.
[11:17] You can also right click on this and choose how big you want that to be.
[11:22] I use these all the time for all sorts of reasons, especially when I'm leaving the project for a day.
[11:27] I mark it in red and I say, re render this in the morning or something like that.
[11:36] Just so I know exactly what my task is for that day right when I get started.
[11:40] Now I would be remiss if I didn't mention this other helpful toggle here.
[11:45] You'll see it at the top of a lot of these different display windows, right?
[11:48] This question mark.
[11:49] This opens up access to the Houdini help, which you can access in other ways and we will look at that.
[11:55] But the Houdini help is unmatched in the 3D world as far as thorough documentation.
[12:04] It is rich with sweet, helpful information that will change your life.
[12:10] I was never one to look at documentation until getting into Houdini and I'm a changed man.
[12:15] I'm not going back.
[12:16] You can't make me.
[12:17] But just to show you an example of this, if I head into the sphere itself and then I create, let's say, I create a mountain note.
[12:28] I'm also going to turn off the lighting here.
[12:33] In fact, I'm going to delete the lighting.
[12:35] Let's just get rid of that.
[12:36] I create a mountain note.
[12:37] A mountain note will basically displace each point along a noise pattern.
[12:41] But if you ever have any questions about the mountain note itself and you're like, how does it work or what do these parameters really mean?
[12:47] If you hover over the parameter, it will give you a breakdown of what that parameter is and what it does.
[12:52] Sometimes it doesn't, though.
[12:53] It's not, it's not, it doesn't bat 100%, but it's really, really impressive.
[12:57] It's batting average.
[12:58] If we head over to here, though, and click for help, what this will do, we'll open up a little pop up window for us here that we can go ahead and expand.
[13:06] And then it will populate with the attribute noise geometry, which if you look over here, the mountain, I guess that's a slang term for it.
[13:15] Because right here we have the real name attribute noise, the attribute noise geometry node, and it will give you tips.
[13:21] It will give you an overview and it will give you an understanding of every single parameter that exists in it.
[13:28] I mean, look at the detail.
[13:30] This is the Sistine Chapel of help documentation.
[13:34] It is incredible.
[13:36] So if you were ever lost, ever confused, ever alone in the wilderness with no one to call, call Houdini help.
[13:43] Not literally, again, just, you know, this documentation.
[13:51] I'm just warning for the full course.
[13:53] Link's in the description.
[13:54] You just click away.
[13:55] Click it.



---

## Captured Frames

- [1:11] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_000.jpg
- [1:47] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_001.jpg
- [2:23] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_002.jpg
- [3:22] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_003.jpg
- [7:51] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_004.jpg
- [8:25] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_005.jpg
- [8:46] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_006.jpg
- [9:23] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_007.jpg
- [10:24] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_008.jpg
- [11:01] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_009.jpg
- [13:06] tutorials/frames/houdini-for-beginners--part-10-contexts/frame_010.jpg

---

## Structured Notes

### Core Technique
Closing entry of the "Houdini for Beginners" series: a guided tour of every top-level **context** ("room") in Houdini — what each is for, at a high level — plus Network View organization tools (node color/shape, alignment, network boxes, sticky notes) and the built-in Help documentation system.

### Summary
Contexts are described via a school-rooms analogy: dedicated areas for dedicated work, with data able to pass between them. Tour, via the context dropdown near the network breadcrumb:
- **OBJ** — the scene/object level already covered extensively (Parts 2-9).
- **SOP** — inside a Geometry node; "surface operators," where an object's actual geometry gets built (also already covered).
- **CHOPs** ("motion effects network," Channel Operators / animation channel operators) — needs its own Motion Effects View to visualize; the series will use this later specifically for crowd work.
- **COPs** ("image context," Compositing Operators) — a real compositing system inside Houdini (load an image with a `file` node — defaults to a stock butterfly test image — then chain e.g. a `color correct` node to adjust it); needs the **Composite View** pane (one of the tabs closed in Part 9) to actually see results, and each node needs its display flag set to preview that step. The presenter notes Houdini is investing more in this area but personally still uses **Nuke** for compositing rather than COPs.
- **MAT** (Material/Matte context) — where materials are authored/assigned.
- **OUT** — legacy **Mantra** renderer settings context (ray samples, etc.); still functional but being phased out in favor of Karma, and not used in this series.
- **SHOP** — an older shader-authoring context, superseded by MAT; still present for legacy workflows but not covered here.
- **TOPs** (Task Operators, inside a "topnet") — generates **work items**, primarily useful for **wedging**: automatically iterating a node network across multiple values of a parameter (e.g. testing liquid stickiness at 1, 10, and 100) instead of manually re-running with each value by hand. Described as confusing in the abstract but will be revisited later in the series.
- **Stage** (also called **Solaris**) — Houdini's USD (Universal Scene Description — a cross-application file format/scene-graph standard for geometry + cameras + lights + materials together) workflow context. Framed as the destination for final lighting/materials/render prep: typical workflow is do geometry and camera work at the OBJ level, then import into Stage/Solaris to light, shade, and prepare for final render. Along with OBJ, this is called out as one of the two contexts the series will live in most.

**Network View organization tools** (separate from the context concept, but grouped here as "final UI tour" material): node type/purpose is visually distinguished by default shape/color (e.g. a light is a yellow lightbulb-shaped node, a camera has its own distinct shape/color) — fully customizable: press **C** in the Network View for a color-palette popup (click-and-drag to resize it) to recolor a selected node, or **Z** for a shape popup to change a node's icon shape; both can be reset back to the default white box. Holding **A** and dragging left/right or up/down on a set of selected nodes snaps them into a straight horizontal or vertical line (whichever node you're dragging on acts as the anchor). **L** attempts automatic layout of the whole network — flagged as "hit or miss" and potentially network-scrambling, generally safer to organize manually. **Shift+O** (or its toolbar button) draws a **network box** around selected nodes that can be resized, recolored, renamed (double-click its title), and collapsed/expanded via a minimize/plus button — useful for grouping related nodes (e.g. "Geometry," "Lighting") visually. A **sticky note** button drops a floating, recolorable, resizable (right-click for size options), freely-editable text note directly in the network — the presenter uses these constantly, e.g. leaving a red note reading "re-render this in the morning" before ending a work session, so the next task is obvious on return.

**Houdini Help:** the **?** icon present in the corner of most panels opens Houdini's built-in documentation, praised as unusually thorough for 3D software. Hovering most node parameters shows an inline tooltip explaining that parameter (not 100% coverage, but close). Clicking a node's help icon opens a full documentation page for that node (demonstrated on a `mountain` node — internally the "Attribute Noise" geometry node — which displaces points along a noise pattern), covering an overview, usage tips, and a breakdown of every parameter.

### Key Steps
1. Recognize each context by what room/purpose it serves: OBJ (scene), SOP (per-object geometry), CHOPs (animation channels, e.g. crowds), COPs (image compositing, needs Composite View), MAT (materials), OUT (legacy Mantra render settings), SHOP (legacy shading, superseded by MAT), TOPs (task/work-item generation, e.g. parameter wedging), Stage/Solaris (USD-based final lighting/materials/render prep).
2. For COPs work: build a node chain (e.g. `file` → `color correct`), open the **Composite View** pane, and toggle display flags per node to preview each step.
3. For quick multi-value parameter testing without manual re-runs, look to **TOPs/wedging** later in the series.
4. Plan on spending most time bouncing between **OBJ** (geometry/camera work) and **Stage/Solaris** (lighting, materials, final render prep) per the presenter's stated workflow.
5. Use **C** (color) and **Z** (shape) in the Network View to customize or reset node appearance for visual organization; use **A**+drag to align a set of nodes in a row/column; use **L** cautiously for automatic layout.
6. Use **Shift+O** for a network box to visually group and label related nodes; use the sticky-note tool to leave notes for your future self or teammates directly in the network.
7. Use the **?** help icon (or hover-tooltips on parameters) whenever a node or parameter's purpose is unclear — Houdini's built-in docs are unusually complete.

### Houdini Nodes / VEX / Settings
Context dropdown (near the network breadcrumb) listing OBJ / SOP / CHOPs / COPs / MAT / OUT / SHOP / TOPs / Stage. COPs example: `file` node (defaults to a stock butterfly image), `color correct` node, Composite View pane, per-node display flags. TOPs/topnet (work-item generation, wedging use case). Stage/Solaris context (USD-based). Network View organization: **C** (node color palette), **Z** (node shape palette), **A**+drag (align selected nodes in a row/column), **L** (automatic layout, unreliable), **Shift+O** (create Network Box: resizable, recolorable, renameable via double-click, collapsible), sticky-note tool (floating recolorable/resizable text note). Houdini Help (**?** icon per panel; hover-tooltips on parameters; per-node full documentation pages) — demoed on the `mountain` node (internally `attribute noise` / Attribute Noise Geometry node).

### Difficulty
Beginner — high-level conceptual orientation to Houdini's context system plus pure UI/organization tooling; no context is explored in technical depth here (each is explicitly deferred to later in the series or flagged as out of scope).

### Houdini Version
Not explicitly stated; final part of the same Houdini 20.x beginner series as Parts 2-9. Explicitly frames Mantra/SHOP as legacy, Karma/MAT/Solaris as current.

### Tags
beginner, contexts, obj, sop, chops, cops, mat, out, shop, tops, wedging, solaris, stage, usd, network-box, sticky-note, houdini-help, jordan-allen

---

## Related Tutorials
- [Houdini for Beginners - Part 9: Layouts](houdini-for-beginners--part-9-layouts.md) — same beginner series; that part builds a custom pane layout, this part (the series finale) tours all of Houdini's contexts and network-organization/help tooling.

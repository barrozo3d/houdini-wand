---
title: Compiling nested loops in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=g6PQu2FRKGo
author: cgside
ingested: 2026-07-13
houdini_version: "any modern (H18+)"
tags: [vex, for-loop, optimization, performance, procedural, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/compiling-nested-loops-in-houdini/
frame_count: 5
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Compiling nested loops in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=g6PQu2FRKGo)
**Author:** cgside
**Duration:** 3m5s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hey everyone and welcome back, so in this video I'm gonna show you a few tips on how to compile your loops
[0:06] and to add a bit more complexity to it I will be using nested loops.
[0:13] So I'm working on a Roman bridge procedural model which is full of bricks and I have some sort of
[0:21] brickify setup that I shared before in a video. And in order to have different variations across
[0:27] the pillars I am looping through each individual shape. So trying to make this process faster I
[0:33] wanted to compile it. I did struggle a bit to get it working but thanks to wafer by tom and
[0:41] fanolis on this court I was able to do it. The first rule is that nodes can't read from
[0:47] direct inputs you need to use sparing puts. As you can see in this add node I have size attributes
[0:54] that I need to read below so I created a sparing puts and in the resemble I can use a point
[1:00] expression referencing it. You also can't reference geometry by specifying the name you'll need
[1:07] sparing puts. Another rule is that you can't use local variables and expressions like bebox
[1:15] you need to use wax instead. So instead of reading the bebox size expression I am using a
[1:22] wrangle to start the bounding box size. So now for the nested loops the first thing you should do
[1:29] is to color them differently that way you know which one is which. Inside the nested loops I am
[1:36] accessing the methane port node where I have the iteration attribute. So in order to access it
[1:44] you can duplicate the begin node set it to fetch inputs and connect it to the methanol from the main
[1:51] loop. This way you have node dependencies going through the block boundary only through begin
[1:57] node set to fetch inputs. And then inside the loop I can use a sparing put to reference the
[2:02] begin node and access the methanol iteration attribute. And you need to follow this rule of not
[2:09] having cross lines in the nested loops in this case I have another red nested loop and in order to
[2:16] access the methanol from the main loop I need to pass it through the first blow loop again using
[2:22] begin node set to fetch input. Also make sure you set the end nodes to multi-traded when compiled.
[2:32] I just wanted to show you another example where I would like to scale down the bricks but having
[2:37] the pivot in the center of the object. Since you can't use the centroid expression you can create
[2:44] the wrangle with the get bounding box center function and then I access it with the point expression
[2:50] in the transform node. So yeah that's basically it. Hopefully this was helpful and as always you can
[2:58] grab an example ePfile on my patron. Thank you and see you in the next time.



---

## Captured Frames

- [0:54] tutorials/frames/compiling-nested-loops-in-houdini/frame_000.jpg
- [1:22] tutorials/frames/compiling-nested-loops-in-houdini/frame_001.jpg
- [1:51] tutorials/frames/compiling-nested-loops-in-houdini/frame_002.jpg
- [2:16] tutorials/frames/compiling-nested-loops-in-houdini/frame_003.jpg
- [2:44] tutorials/frames/compiling-nested-loops-in-houdini/frame_004.jpg

---

## Structured Notes

### Core Technique
A rules checklist for successfully **compiling** for-loop blocks in Houdini (including nested loops) to speed up per-piece variation processing on a procedural Roman-bridge brickify setup, covering the specific restrictions compiled blocks impose versus normal SOP networks.

### Summary
Compiled loop blocks execute much faster than normal for-loops but impose several hard restrictions that aren't obvious until you hit them. The core rules demonstrated: (1) nodes inside a compiled block **cannot read from other nodes via direct/named references** — any cross-reference (e.g. an Add node needing size attributes from elsewhere) must go through a **spare input** instead, referenced via a point expression; this applies to referencing other geometry by node name too. (2) **Local-variable/component expressions like `bbox()` don't work inside compiled blocks** — anything like that must be rewritten in VEX (e.g. storing bounding-box size into an attribute with a wrangle instead of reading it via an expression). (3) For **nested loops**, color-code each loop level differently for clarity, and to access the outer loop's iteration metadata (methane/iteration attribute) from inside an inner loop, duplicate the outer loop's Block Begin node, set its Method to **Fetch Input**, wire it to the outer loop's own Block Begin, and reference *that* duplicate via a spare input inside the inner loop — this is the only way node dependencies are allowed to cross a block boundary. (4) This fetch-input relay must be **chained through each nesting level** — a doubly-nested loop needs the pattern repeated once per level, since "crossing lines" directly between non-adjacent loop levels isn't allowed. (5) Always set **Block End nodes to "Multithreaded when Compiled."** A bonus tip: since the `centroid()`-style expression isn't available either, get a shape's true center via a wrangle computing `getbbox_center()` and feed that into a Transform node's pivot via a point expression, for correctly pivot-centered per-piece scaling.

### Key Steps
1. **Rule 1 — no direct/named references inside a compiled block**: if a node (e.g. Add, for setting size attributes) needs data from elsewhere in the network, create a **spare input** on it and reference the incoming data via a point expression instead of a direct wire/name reference. The same applies to referencing other geometry streams by node name.
2. **Rule 2 — no local-variable/component expressions (e.g. `bbox()`)**: rewrite anything that would use such an expression as an actual VEX wrangle instead — e.g. computing and storing bounding-box size as an attribute (`f@size = getbbox_size(0)`-style) rather than reading it via an expression at the point where it's needed.
3. **Rule 3 — color-code nested loops**: give each nested loop level (Block Begin/End pair) a distinct color so it's visually clear which nodes belong to which loop level, especially once fetch-input relay nodes are added.
4. **Rule 4 — accessing outer-loop iteration data from inside an inner loop**: duplicate the outer loop's **Block Begin** node, set its **Method to "Fetch Input"**, and wire it to the actual outer loop's Block Begin node. Inside the inner loop, use a spare input referencing this duplicated fetch-input node to access the outer loop's iteration/metadata attribute — this fetch-input relay is the *only* way a dependency is allowed to cross a compiled block's boundary.
5. **Rule 5 — deeper nesting needs the relay repeated per level**: with a third (innermost) loop needing the same outer-loop data, you can't "skip ahead" directly — pass the fetched value through each intermediate loop level's own fetch-input relay in turn, since compiled blocks don't allow dependency lines to cross directly between non-adjacent nesting levels.
6. **Rule 6 — Block End settings**: make sure every Block End node involved has **"Multithreaded when Compiled"** enabled to actually benefit from compilation's performance gain.
7. **Bonus: correct pivot for scaling**: since `centroid()`-style expressions also aren't available in compiled context, compute the true center with a wrangle (`f@bbox_center = getbbox_center(0)` or similar, as a vector) and feed that value into a Transform node's pivot parameter via a point expression — this lets you scale each looped piece down around its own geometric center rather than the object's origin.

### Houdini Nodes / VEX / Settings
For-loop **Block Begin / Block End** pairs (nested, color-coded) → spare inputs + point expressions (replacing direct/named node references) → Attribute Wrangle (`getbbox_size()`/`getbbox_center()`, replacing `bbox()`/`centroid()` expressions) → duplicated **Block Begin set to "Fetch Input"** (relay pattern for crossing block boundaries, chained per nesting level) → Block End **"Multithreaded when Compiled"** option → Transform node (pivot driven by a point expression referencing the computed bbox center).

### Difficulty
Intermediate / Advanced — the individual fixes are simple once known, but understanding *why* compiled blocks impose these restrictions (and debugging why a network suddenly breaks when compiled) requires some familiarity with how Houdini's compiled-block execution model differs from normal cooking.

### Houdini Version
Not stated explicitly; compiled for-loop blocks and the "Fetch Input" Block Begin method are long-standing Houdini features available in any modern version (H18+).

### Tags
#vex #for-loop #optimization #performance #procedural #intermediate #advanced

---

## Related Tutorials
No other indexed cgside tutorial currently covers compiled for-loop blocks specifically — cross-link with any future performance/optimization-focused tutorials once extracted from this batch.

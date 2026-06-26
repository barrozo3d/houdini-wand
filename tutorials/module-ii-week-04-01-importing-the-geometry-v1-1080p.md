---
title: module ii   week 04   01   importing the geometry v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=uPPW2sI_oyw
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [import, alembic, rbd, skyscraper, polysoup, performance, beginner]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-04-01-importing-the-geometry-v1-1080p/
frame_count: 4
---

# module ii   week 04   01   importing the geometry v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=uPPW2sI_oyw)
**Author:** The VFX School Archive
**Duration:** 3m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Okay, here we are in week 4. So as usual go ahead and create a new project, file a new project. All right, we'll module 2, week 4 and this will go into the D drive. Okay, accept, creates that. Before I forget, save as into job there, that's fine. So what are we doing here? Let's call it collapse. There's one. So just go ahead and navigate to that project and then we'll go into geo, no, ABC, Olympics. That's what we've got. And then drag in, I've already unpacked these, the skyscrapers. Okay, so just do that. And I'll bring that out of the way again. I'm going to delete these, create a new geometry node, call this sour, or let's call it skyscraper. Okay, dive inside there. Dropping a limb back. And then I'm going to press P on my keyboard, go inside and go into geo. It's not there. Why is that? Oh, let me try just to listen to that, making another limb back. I'm not sure why that's not coming up. There we go. Into hip, ABC, there we go. And I'm going to grab a load of three. Open that. So if we press space bar and F, you can see it's really big again. So just like before transform, set that to point of one. Okay, visualize that space bar and F. There we go. Okay, so you can see it's running a bit slow. You can try doing a few things, set it to wireframe. That might help out. But this is a pretty heavy model. It's not those things a little bit 36,000. We convert this to polygons. We'll see. Right now, I think it's a poly soup. So it's a packed, it's a packed olympics there. Once we convert it, you can see it's 3,000,000, 600,000 points. So it's fairly heavy. But we're going to be simulating this bit by bit. So in three separate simulations, so that will help break it down a bit. Also, we're not going to simulate all of the geometry. You know, part of it will be inactive, kind of at the bottom here. Also, there's some bits of the geometry, which are just really fine, tiny details, which we don't really need. So we can just kind of omit them. But we'll take care of them as we go on.

**Frame:** tutorials\frames\module-ii-week-04-01-importing-the-geometry-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Import heavy skyscraper Alembic (3.6M points as polygons), scale to 0.1, use wireframe mode for performance. Strategy: split sim into 3 separate passes (not all at once), leave bottom inactive, omit tiny geometry details.

### Summary
3m21s lesson (Module II Week 4, lesson 1). New project "collapse v1" — skyscraper RBD collapse. Imports packed Alembic skyscraper LOD 3, scales to 0.1. Poly soup converts to 3.6M polygon points (heavy) — use wireframe display. Simulation strategy: 3 separate sims to manage complexity, inactive geometry at bottom, omit fine detail geo.

### Key Steps
- New project: module-2-week-4 / "collapse.v1.hip"
- Geometry node → Alembic SOP → navigate to skyscraper geo folder → open LOD 3
- Transform SOP: scale 0.1 (model comes in very large)
- Convert SOP: polysoup → polygons (3.6M points — heavy in viewport)
- Performance: switch display to wireframe
- Simulation plan: 3 separate passes (top section, mid, base) to keep each sim manageable; bottom inactive; skip tiny details

### Houdini Nodes / VEX / Settings
- **Alembic SOP** — import skyscraper; scale = 0.1
- **Convert SOP** — polysoup → polygons; exposes full point count (~3.6M)
- Performance tip: wireframe mode (W) for heavy geometry viewport display
- Sim strategy: 3-pass RBD (not one monolithic sim); active attribute = 0 for bottom/inactive sections

### Difficulty
Beginner

### Houdini Version
H18.5

### Tags
[import, alembic, rbd, skyscraper, polysoup, performance, beginner]

---

## Related Tutorials
- module-ii-week-04-01-introduction-v1-1080p.md (week 4 intro: grains + render)
- module-ii-week-02-01-importing-the-geometry-v1-1080p.md (building import workflow)
- module-i-week-01-09-setting-the-active-attribute-v1-1080p.md (RBD active attribute)

---
title: module ii   week 03   01   splitting by material v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=cvAuweF1fvg
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "H18.5"
tags: [rbd, fracture, path-attribute, split-sop, material-separation, building, area-attribute, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/module-ii-week-03-01-splitting-by-material-v1-1080p/
frame_count: 4
---

# module ii   week 03   01   splitting by material v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=cvAuweF1fvg)
**Author:** The VFX School Archive
**Duration:** 5m31s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So we're going to start week three with the result of week two because you know we're using the same building and It's easier just to start off like this. I'm going to delete all of this stuff And then going to file and then we can just save use the same project as well. Okay, so save as we'll change this to this is going to be It's called a nuke It's going to be like a nuclear explosion version one except Okay, dive inside here and Again, that will delete most of this So let's say from down there delete all of that Okay, and then let's take a look at splitting this up again So I'm going to change this to point where is it this connectivity needs to be on primitives And then I'm gonna convert so this is still Polysoups at this point, right? So let's just convert it so it's just normal every day polygons Okay There we go. Okay, you see it's just polygons there now and then I'm gonna start splitting this up So for this week, you know, we're gonna go into some detail. I think in week two we literally just did a really simple Voron i fracture, right? So I want to use the let's see. I don't think we have the path attribute here. How we do yeah so Yeah, so that's on the primitives so name Sorry name path Is and then I think we've got a glass so you know, you can just kind of have a look here Or let's say one thing I normally do is say, you know, I want to split out all the windows. So I come here select one of the windows Come into my geometry spreadsheet view only show selected and then I can see we've got glass There, okay, so at path is star Glass star And then visualize that 10 oops, 10 both these off and spacebar and f So let's do I think I did it with a capsule some reason I don't know something in that path Yeah, so that gives me all of the windows fight invert that can see We just got the the windows there, okay, so let's do splits and that split glass and Then we'll do just like what we did before splitting the smaller pieces. So another splits and Normally it is super common I almost always do this for Rigid body simulations, and I just normally call them bits, right? So I measure everything and then split out really small things that I don't want to fracture and I call them bits normally so Obviously you don't have to do that So we use that area attribute again And again, we've probably got yeah, visualize them. So an area is bigger than 0.5 Again, you know that you just kind of play around and see what looks about right I got that inverted there we go, okay, and then just just get a sense of that exploded view. So these my Bigger pieces and then here the smaller pieces tiles and so forth Okay, so put that over here and then from here I'm gonna drop another split Because I want to so I think there's kind of there's bits of wood and then there's Fiberglass and concrete if I remember right so again, oh clicking on that in the jump to spreadsheet. We can see we got a little wood there And then fiberglass So split out the wood And again, we use that path attributes That path is star Wood star So okay, so I haven't explained before so we use these These stars here, which means anything so House have wood in the path attribute at some point, okay, that's all it means So that should give me the wood and then that's from the other side Here again use that exploded view just to take a look at the wood Okay And then from the other side we got kind of these panels and it's be honest It could be wood as well, but you know, we'll do a different fracture on it anyway just to have more variety And then finally the fiberglass so if we say that path Here's star fiber Star like that, okay, and that gives us this the those bits and then we got Like a little bit of concrete there, okay, so it will say split wood split fiber And that's it and then we can go ahead and fracture all these bit by bit

**Frame:** tutorials\frames\module-ii-week-03-01-splitting-by-material-v1-1080p\frame_000.jpg


---

## Structured Notes

### Core Technique
Use the path attribute (from Alembic import) with Split SOP + wildcard patterns to separate a building into material-based groups (glass, wood, fiberglass/concrete, small bits) before fracture. Small bits identified by area attribute threshold.

### Summary
5m31s lesson. Splits a Brooklyn building Alembic into material-based geometry streams for selective fracturing. Workflow: Connectivity SOP (set to primitives) → Convert (polysoups to polygons) → Split SOP chain using path attribute wildcards. Groups created: glass (windows), bits (small area pieces < 0.5), wood, fiberglass. Each split feeds its own fracture operation for variety. Uses exploded view to verify splits visually.

### Key Steps

**1. Setup**
- Start from saved week-2 project; new file "nuclear explosion v1"; delete old sim nodes but keep building import
- Connectivity SOP: mode = primitives (not points)
- Convert SOP: polysoup → normal polygons (required for path attribute access)

**2. Split by Material via Path Attribute**
- Split SOP: use "path" attribute with wildcard pattern `* glass *` → all prims where path contains "glass" → glass/windows group
- Split SOP: area attribute < 0.5 → small bits group (tiles, small panels); invert → bigger pieces
- Split SOP: `* wood *` → wood panels
- Split SOP: `* fiber *` → fiberglass panels + concrete remainder

**3. Visual Verification**
- Add Exploded View after each Split SOP to visually inspect what's in each group
- Select a prim in viewport → jump to Geometry Spreadsheet → filter "show only selected" → read path attribute value → build wildcard from it

### Houdini Nodes / VEX / Settings
- **Connectivity SOP** — set to primitives; required before Split path-based workflow
- **Convert SOP** — polysoup to polygons (unlocks primitive attribute access)
- **Split SOP** — pattern mode on `path` string attribute: `* glass *`, `* wood *`, `* fiber *`; numeric mode on `area` attribute with threshold (e.g., 0.5)
- `path` primitive attribute: material/object path string from Alembic import; wildcard `*` matches any substring
- `area` primitive attribute: polygon area; use to isolate small vs large pieces for different fracture treatment
- **Exploded View SOP** — verify split results visually; confirms piece separation and count

### Difficulty
Intermediate

### Houdini Version
H18.5

### Tags
[rbd, fracture, path-attribute, split-sop, material-separation, building, area-attribute, intermediate]

---

## Related Tutorials
- module-ii-week-02-01-importing-the-geometry-v1-1080p.md (building import + path attribute intro)
- module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p.md (breaking cloth welds/constraints)
- module-i-week-01-09-setting-the-active-attribute-v1-1080p.md (RBD active attribute + border ring)

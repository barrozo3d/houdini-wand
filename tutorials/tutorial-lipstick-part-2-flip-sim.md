---
title: [Tutorial] Lipstick. Part 2. Flip Sim
source: YouTube
url: https://www.youtube.com/watch?v=T1OTnyioFrA
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [sop, dop, flip, simulation, particles, vdb, modelling, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/tutorial-lipstick-part-2-flip-sim/
frame_count: 4
---

# [Tutorial] Lipstick. Part 2. Flip Sim

**Source:** [YouTube](https://www.youtube.com/watch?v=T1OTnyioFrA)
**Author:** Alexander Eskin
**Duration:** 26m21s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** And now it's time for the droplets. Let's create a new node called lipstick. Well, let's source. Reign. Diving. Object merge I would do. Convert it to VDB. Resolution should be a bit higher. Convert back to polygons. Add some normals. And we don't need the bottom part and we don't need the part that we don't see behind the camera. So we're going to scatter the points on the frontal part. So we're going to clip that. Something like that. And another clip for the ZXs. So this is going to be our shape to scatter. Now we're going to scatter some points. We'll use density scale. And we're going to scatter for example, 55. It's going to be our tiny points. Tiny points. Tiny. We're going to create a tribute. Create a fiscal. Equals 0.03. I'd visualize node. And we're going to add some random adjustments to the point scale. Float. I'd just float. For a should multiply pattern random, mean value 0.2. And another, I'd just multiply by noise from the smaller element size. And we'll perhaps have some curve adjustments. So these are going to be tiny points. These are going to be medium points. These are going to be big points. Big. Here. Garage. Here we should have around 100. These 10 big ones...

**Frame:** tutorials\frames\tutorial-lipstick-part-2-flip-sim\frame_000.jpg


---

## Structured Notes

### Core Technique
English companion to Lipstick FLIP Sim RU — adds crucial detail: THREE separate scatter passes (tiny ~55pts, medium, big ~100/10 pts) merged for realistic multi-scale droplet distribution. VDB convert → clip to frontal half → `pscale` 0.03 + `attribadjust` random (mean 0.2) + noise multiply per tier.

### Summary
A 26-minute English FLIP droplet tutorial (Part 2) with key production insight: three separate scatter passes at different scales — tiny (density scale ~55), medium, and big (~100 scattered, ~10 largest) — merged together for realistic droplet size distribution on the lipstick. Each pass gets `pscale` = 0.03 base + `attribadjust` random (multiply, mean 0.2) + noise multiply (smaller element size). Uses VDB roundtrip for clean surface, two clip planes to restrict to frontal visible area only.

### Key Steps
1. Geo node → `objectmerge` lipstick from Part 1 → `vdbfrompolygons` (higher res) → convert back to polygons → recompute `normals`
2. **Clip 1**: remove bottom part
3. **Clip 2**: remove ZX back half (only simulate visible front)
4. **Three scatter tiers** (merge all at end):
   - **Tiny**: `scatter` density scale ~55 → `pscale` 0.03 → `attribadjust` random multiply (mean 0.2) + noise multiply
   - **Medium**: `scatter` ~medium density → same pscale variation
   - **Big**: `scatter` ~100 pts, with ~10 largest → larger pscale base
5. `merge` all three tiers into single point cloud
6. FLIP DOP — use merged points as FLIP source; `flipsolver` with surface tension
7. Cache → render as liquid

### Houdini Nodes / VEX / Settings
- `objectmerge` SOP
- `vdbfrompolygons` SOP — higher resolution
- `convertvdb` SOP — back to polygons
- `normal` SOP — recompute normals
- Two `clip` SOPs — front half + remove bottom
- Three `scatter` SOPs — tiny (~55 density scale), medium, big (~100/10)
- `attribcreate` — `pscale` = 0.03 per tier
- `attribadjust` — multiply by random, mean value 0.2
- Second `attribadjust` — multiply by noise (smaller element size)
- `merge` SOP — combine all three tiers
- FLIP DOP — surface tension for droplet cohesion
- `filecache` SOP

### Difficulty
Advanced

### Houdini Version
Not specified (H19–H21 UI)

### Tags
sop, dop, flip, simulation, particles, vdb, modelling, intermediate, advanced

---

## Related Tutorials
- [[урок-помада-часть-2-flip-sim]] — Russian companion (35 min)
- [[tutorial-lipstick-part-1-modeling]] — Part 1 (modeling prerequisite)
- [[houdini-tutorial-creating-realistic-waterfall-simulation-step-by-step]] — FLIP fundamentals
- [[tutorial-purple-sponge]] — VDB + scatter workflow

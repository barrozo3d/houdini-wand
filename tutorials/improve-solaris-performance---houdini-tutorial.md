---
title: Improve Solaris Performance - Houdini Tutorial
source: YouTube
url: https://www.youtube.com/watch?v=QfWUzrfsDaY
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "Not specified (H20–H21 UI)"
tags: ["lop", "solaris", "usd", "rendering", "karma", "performance", "pipeline", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/improve-solaris-performance---houdini-tutorial/
frame_count: 0
---

# Improve Solaris Performance - Houdini Tutorial

**Source:** [YouTube](https://www.youtube.com/watch?v=QfWUzrfsDaY)
**Author:** Voxyde VFX
**Duration:** 22m50s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey guys, it's Tom here. And today I will cover up some topics about how to get your sub geometry into stage and also prepare them for stage. So we don't have a really slow viewport on stage. How do we do that? At first I will create a log network here so we can switch in between and I will set the bookmark in here with control 1 and also one here with control 2. So now let's create a null after my ground. But I got here a lot of different geometries. So I got my ground, I got some stacked geometry like fern. I also got my character here with the animation. We also cover up how to prepare our RBD simulation here, also our Valom simulation and also some particles over here. So we will start with the ground and one thing to add if you want to have this cool animation here you can get it from our three cores enemy ground destruction. It's for free and you can easily grab it from there. But now start with the ground. I will grab my null one here and let's create a sub import here and pass it down here. So now we got the ground and you can see this here is the node name because my import pass prefix is Dolores and I will call it ground here. So now we got the ground and also my mesh 0. ...



---

## Structured Notes

### Core Technique
Optimizing Solaris viewport performance by correctly preparing and importing SOP geometry into the USD stage: using `sopimport` with proper LOD proxy geometry, baking animated characters and simulations (RBD, Vellum, particles) as USD or bgeo caches before importing, and using `configurelayer` or `setvariant` to manage complexity — preventing slow stage evaluation caused by live SOP cooking inside LOPs.

### Summary
A 23-minute practical tutorial covering strategies to keep the Houdini Solaris viewport fast when dealing with complex scenes containing characters, animated geometry, RBD simulations, Vellum cloth, and particles. The core principle is to never import heavy live-cooking SOP networks directly into Solaris — instead, bake simulations and animations to disk as caches (`.bgeo.sc`, `.usd`, or `.abc`) and import the cached result. Demonstrates workflows for ground meshes, stacked/instanced geometry (ferns), animated characters, RBD destruction sims, Vellum sims, and particle systems — each with the appropriate caching and import strategy to maintain an interactive Solaris stage.

### Key Steps
1. Set up bookmarks: press **Ctrl+1** / **Ctrl+2** in the network editor to bookmark SOP and LOP contexts for fast switching during the workflow
2. Ground/static geometry: add a `null` SOP as output, then `sopimport` LOP — Path Prefix: `/env/ground`; for static geo this is fine but use a `filecache` SOP first if the ground is procedurally generated (prevents repeated SOP cooking)
3. Stacked/instanced geometry (e.g. ferns): bake to a `.usd` file using the `componentbuilder` workflow or `rop_usd` before importing; use `reference` LOP + `instancer` LOP to scatter — avoids duplicating SOP evaluation per instance in the stage
4. Animated character: bake animation to `.bgeo.sc` or `.abc` cache using `filecache` SOP or `rop_alembic` before `sopimport`; the stage then loads the pre-baked cache instead of re-cooking the rig and deformers every frame
5. RBD simulation: bake DOPs to disk with `filecache` SOP (packed RBD output); import the cached `.bgeo.sc` via `sopimport`; set the SOP path to point to the filecache's output null — Solaris reads pre-computed transforms instead of running the solver
6. Vellum simulation: same strategy — bake Vellum output to `filecache` before bringing into Solaris; particularly important for cloth with high poly counts
7. Particles: bake particle cache to `.bgeo.sc` via `filecache`; import with `sopimport`; use `karmarendersettings` particle point rendering settings for the point cloud
8. Use `configurelayer` LOP to set the active layer's purpose (render, proxy, guide) — switch to proxy meshes in the viewport for speed while keeping render-res geometry for the final render pass

### Houdini Nodes / VEX / Settings
- `sopimport` LOP — SOP Path: points to a null after a filecache (not the live simulation); Path Prefix: organizes in scene graph
- `filecache` SOP — bake output: `.bgeo.sc`; set to Write then switch to Read for playback; use for all animated/simulated geometry before Solaris import
- `null` SOP — clean output point for sopimport to reference; rename with `OUT_` prefix convention
- `rop_usd` SOP/LOP — exports SOP geometry as USD asset for reference import; use for static and component assets
- `rop_alembic` SOP — exports animated characters/deforming meshes as `.abc` cache for clean Solaris import
- `reference` LOP — loads pre-exported `.usd` or `.abc` into the stage; avoids live SOP cooking in LOPs
- `instancer` LOP — scatter pre-baked USD assets as instances; far more efficient than instancing live SOP geometry
- `componentbuilder` LOP — packages geometry + material as self-contained USD for instancing
- `configurelayer` LOP — Layer Purpose: Default/Render/Proxy/Guide; switch proxy meshes active in viewport for speed
- **Ctrl+1 / Ctrl+2** — bookmark SOP and LOP network positions for fast context switching
- `filecache` SOP (RBD) — cache packed RBD output; frame range; `.bgeo.sc` format
- `filecache` SOP (Vellum) — cache cloth/soft-body output; critical for maintaining interactive Solaris viewport

### Difficulty
Intermediate

### Houdini Version
Not specified (H20–H21 UI)

### Tags
#lop #solaris #usd #rendering #karma #performance #pipeline #intermediate

---

## Related Tutorials
- [Intro To Houdini Solaris - Full Beginner Course](./intro-to-houdini-solaris---full-beginner-course.md) — #lop #solaris #usd #rendering #karma #beginner
- [Houdini Solaris Tutorial - Rendering Multiple ROPS Together](./houdini-solaris-tutorial---rendering-multiple-rops-together.md) — #lop #solaris #rendering #karma #top #pipeline
- [Houdini 21 Tutorial - MPM Snowball](./houdini-21-tutorial---mpm-snowball.md) — #dop #sop #mpm #simulation #rendering #karma #h21

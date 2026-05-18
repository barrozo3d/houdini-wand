---
title: Houdini Tutorial - Wispy Smoke
source: YouTube
url: https://www.youtube.com/watch?v=RRmvyQu39-4
author: Voxyde VFX
ingested: 2026-05-18
houdini_version: "Not specified (H19–H21 UI)"
tags: ["dop", "sop", "pyro", "smoke", "volumes", "vdb", "simulation", "vfx", "intermediate"]
extraction_status: complete
frames_dir: tutorials/frames/houdini-tutorial---wispy-smoke/
frame_count: 0
---

# Houdini Tutorial - Wispy Smoke

**Source:** [YouTube](https://www.youtube.com/watch?v=RRmvyQu39-4)
**Author:** Voxyde VFX
**Duration:** 27m30s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hey guys, I'm Althobi and I'm here to give you a free tutorial on how to make a whistler smoke in Hedini. But before we jump with that, we're about to release a new course on boxside.com about flip simulations and flip fluids in Hedini. So I'm going to show you a quick teaser of that now and you should go to the website and join the waitlist. So, one asked how to create a whistler smoke in Hedini. The whistler look not the dynamic of it. So, this is a quick attempt at creating that. Obviously the dynamics here are not the best, but we're looking at the look mainly. This is just a quick flipbook and as you can see, it's already looking like a whistler smoke. So let's try creating this very quickly. Let's jump into Hedini and create a geometry node and jump in. And I'll cheat by doing the configr pyro below the smoke. This one just start with this just as a base. Let's see here and I'll just delete all of these below here. And I will actually change this tors to a sphere. And let's change the size of it to something like 1.5. And skip it as it is in here. Oh, connected in here. And it's a bit too big. So if it's going to be like a small cigarette, maybe we should reduce the size of i...



---

## Structured Notes

### Core Technique
Wispy smoke look development using Houdini's Pyro solver: starting from a `configure pyro` shelf setup, adjusting the source geometry (small sphere emitter), tuning pyro DOP parameters for low density and high velocity/dissipation to achieve thin wispy tendrils rather than a dense smoke column, and shaping the look via dissipation, turbulence, and volume shader settings.

### Summary
A 27-minute tutorial focused on achieving a wispy, thin cigarette-smoke aesthetic using Houdini's Pyro solver. The approach starts from the `configure pyro` shelf tool preset (used as a quick base), replaces the default torus source with a small sphere emitter, and then shapes the simulation by reducing density emission, increasing dissipation rate, adding high-frequency turbulence for wispy tendrils, and reducing buoyancy so smoke drifts sideways rather than shooting upward. The emphasis is on the visual look rather than physically accurate dynamics — cheating pyro parameters to produce the characteristic wispy tendrils of cigarette or incense smoke. Includes a quick Karma/Mantra volume shader setup for rendering.

### Key Steps
1. Start with the Pyro shelf tool: in the SOP context, select a sphere (Radius: ~0.05–0.1 for small emitter); press Pyro from the shelf → choose "Configure Pyro" or "Smoke" preset; this auto-builds the DOP network and source SOP chain
2. Replace or adjust the source: the shelf creates a `pyrosource` SOP chain; adjust the sphere size to small (~1.5 units then scale down); reduce emission rate for thin wisps; source type: Surface or Volume
3. In the DOP network (`pyronet`), find the `pyrosolver` DOP — key parameters for wispy look:
   - **Dissipation** (Density Dissipation): increase to 0.3–0.8 — smoke fades quickly, creating thin tendrils
   - **Buoyancy** (Temperature Diffusion / Lift): reduce significantly — prevents rapid upward shooting
   - **Turbulence**: increase Strength (0.5–1.5) and reduce Scale for high-frequency swirling pattern; creates the characteristic wispy tendrils
   - **Wind** or external velocity: add a gentle lateral wind force to drift the smoke sideways
4. Tune the **Shape** tab micro-solvers: increase Shredding for wispy edge breakup; add Disturbance at a low scale for fine detail
5. Reduce simulation **resolution** for fast iteration (voxel size 0.05–0.1); only increase for final render (0.01–0.02)
6. For rendering: assign a Volume shader — in Mantra use `pyro shader`; in Karma use a MaterialX volume shader; reduce Density multiplier in the shader to make rendered smoke thinner than simulation; adjust Scattering for smoke color
7. Do a quick flipbook (Alt+V) to evaluate motion before committing to a full render

### Houdini Nodes / VEX / Settings
- `sphere` SOP — Radius: ~0.05–0.15 for small wispy source; used as pyro emitter
- `pyrosource` SOP — auto-created by shelf; Source Type: Surface or Volume; Activation: 1 (always on)
- `dopnet` / `pyronet` DOP — auto-created by shelf; contains pyrosolver and source nodes
- `pyrosolver` DOP — master solver for smoke; key wispy parameters:
  - Density Dissipation: 0.3–0.8 (fast fade for wispy look)
  - Temperature Dissipation: increase for fast heat loss
  - Buoyancy: reduce (0.1–0.3) to prevent aggressive upward rise
- `gasturb` / Turbulence micro-solver — Strength: 0.5–1.5; Scale: small (0.1–0.3) for high-frequency wisps
- `gasdisturbance` micro-solver (Disturbance) — adds fine chaotic detail to density field
- `gasshred` micro-solver (Shredding) — tears the smoke edges into wispy tendrils
- `gasdamp` micro-solver (Gas Damp) — damps velocity; reduce to let smoke drift longer
- `windforce` DOP — adds lateral wind drift; Direction: {1,0,0}; Strength: low
- Volume shader (Karma MaterialX) — Density multiplier; Scattering color; use for final render
- `pyro shader` (Mantra) — built-in volume shader; Smoke Density; Emission; Temperature
- **Alt+V** — create flipbook in viewport for quick sim preview
- **Resolution / Voxel Size** — pyrosolver Division Size: 0.05–0.1 for test, 0.01–0.02 for final

### Difficulty
Intermediate

### Houdini Version
Not specified (H19–H21 UI)

### Tags
#dop #sop #pyro #smoke #volumes #vdb #simulation #vfx #intermediate

---

## Related Tutorials
- [Intro To Houdini Pyro - Full Beginner Course](./intro-to-houdini-pyro---full-beginner-course.md) — #pyro #fire #smoke #simulation #dop #vdb #beginner
- [Intro To Houdini Volumes - Beginner Course](./intro-to-houdini-volumes---beginner-course.md) — #sop #vop #volumes #vdb #procedural
- [Houdini Tutorial - Simple Disintegration FX](./houdini-tutorial---simple-disintegration-fx.md) — #sop #dop #particles #vfx #intermediate

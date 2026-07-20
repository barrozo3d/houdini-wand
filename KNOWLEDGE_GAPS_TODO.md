# Knowledge Gap To-Do List

Generated 2026-07-20 from a library-wide gap analysis (333 ingested tutorials
checked against SKILL.md scope + all references/*.md + recipes/*.md). Each gap
below was verified by grepping actual INDEX.md/reference content before being
listed — not guessed. Ingest with `python ingest.py "[URL]"` from this
directory, then run the mandatory extraction pass (see SKILL.md Mode 3).

## Pending

- [ ] **Crowd simulation** — the Crowd context (agents, behaviors, state
  machines) has zero real coverage; only a license-tier aside and one orphaned
  tag exist in the library.
  Source: SideFX official — "Intro to Crowds"
  https://www.sidefx.com/tutorials/intro-to-crowds/

- [ ] **Ocean spectrum / whitewater FX** — no ingested tutorial builds an
  Ocean Spectrum/Ocean Waves setup; only mentioned in a FLIP recipe title.
  Source: SideFX official — "Create Cinematic Oceans FAST — Realistic Shading & Render with Karma XPU"
  https://www.sidefx.com/tutorials/create-cinematic-oceans-fast-in-houdini-realistic-shading-render-with-karma-xpu/

- [ ] **True muscle simulation** — existing content is Vellum rest-blend
  stiffness explicitly described as "without actual muscle simulation," not
  the real Muscle/Tissue system.
  Source: SideFX Docs (official) — "Muscles and tissue"
  https://www.sidefx.com/docs/houdini/muscles/index.html

- [ ] **Procedural city/building generation** — library only has pre-built
  skyscraper assets used for RBD destruction, no ground-up generator.
  Source: SideFX official — "Procedural City 1: Building Generator"
  https://www.sidefx.com/tutorials/procedural-city-1-building-generator/

- [ ] **Houdini Engine → Unity workflow** — Unreal HDA workflow is covered by
  ~8 tutorials + a full recipe (recipes/houdini-to-ue5.md); the Unity side has
  zero real pipeline coverage, only incidental mentions.
  Source: SideFX official — "Getting Started with Houdini Engine for Unity"
  https://www.sidefx.com/tutorials/getting-started-with-houdini-engine-for-unity/

- [ ] **ML SOPs / Machine Learning (ONNX)** — release-notes-h21.md has only a
  2-sentence stub; no hands-on ONNX Inference SOP / ML Volume Upres tutorial.
  Source: Entagma — "Machine Learning with ONNX in Houdini 20"
  https://www.youtube.com/watch?v=aCAatiY53s8

## Ruled out (already covered — do not re-suggest)
Karma XPU, heightfield/erosion, Solaris/USD variants & layering, Redshift,
Copernicus/COPs.

# Knowledge Gap To-Do List

Generated 2026-07-20 from a library-wide gap analysis (333 ingested tutorials
checked against SKILL.md scope + all references/*.md + recipes/*.md). Each gap
below was verified by grepping actual INDEX.md/reference content before being
listed — not guessed. Ingest with `python ingest.py "[URL]"` from this
directory, then run the mandatory extraction pass (see SKILL.md Mode 3).

## Pending

(none — the 6 gaps identified in the 2026-07-20 analysis have all been ingested; see "Completed" below)

## Completed (ingested 2026-07-20)

- [x] **Crowd simulation** — the Crowd context (agents, behaviors, state
  machines) had zero real coverage; only a license-tier aside and one orphaned
  tag existed in the library.
  Source: SideFX official — "Intro to Crowds"
  https://www.sidefx.com/tutorials/intro-to-crowds/
  Ingested as: `tutorials/intro-to-crowds-sidefx.md`

- [x] **Ocean spectrum / whitewater FX** — no ingested tutorial built an
  Ocean Spectrum/Ocean Waves setup; only mentioned in a FLIP recipe title.
  Source: SideFX official — "Create Cinematic Oceans FAST — Realistic Shading & Render with Karma XPU"
  https://www.sidefx.com/tutorials/create-cinematic-oceans-fast-in-houdini-realistic-shading-render-with-karma-xpu/
  Ingested as: `tutorials/create-cinematic-oceans-fast-realistic-shading-render-with-karma-xpu-sidefx.md`

- [x] **True muscle simulation** — existing content was Vellum rest-blend
  stiffness explicitly described as "without actual muscle simulation," not
  the real Muscle/Tissue system.
  Source: SideFX Docs (official) — "Muscles and tissue"
  https://www.sidefx.com/docs/houdini/muscles/index.html
  Ingested as: `tutorials/muscles-and-tissue.md`

- [x] **Procedural city/building generation** — library only had pre-built
  skyscraper assets used for RBD destruction, no ground-up generator.
  Source: SideFX official — "Procedural City 1: Building Generator"
  https://www.sidefx.com/tutorials/procedural-city-1-building-generator/
  Ingested as: `tutorials/procedural-city-1-building-generator-sidefx.md`
  (note: source is a paid marketplace course — extraction is overview-level
  only, reconstructed from the course's own description, since lesson content
  is paywalled)

- [x] **Houdini Engine → Unity workflow** — Unreal HDA workflow is covered by
  ~8 tutorials + a full recipe (recipes/houdini-to-ue5.md); the Unity side had
  zero real pipeline coverage, only incidental mentions.
  Source: SideFX official — "Getting Started with Houdini Engine for Unity"
  https://www.sidefx.com/tutorials/getting-started-with-houdini-engine-for-unity/
  Ingested as: `tutorials/getting-started-with-houdini-engine-for-unity-sidefx.md`

- [x] **ML SOPs / Machine Learning (ONNX)** — release-notes-h21.md had only a
  2-sentence stub; no hands-on ONNX Inference SOP / ML Volume Upres tutorial.
  Source: Entagma — "Machine Learning with ONNX in Houdini 20"
  https://www.youtube.com/watch?v=aCAatiY53s8
  Ingested as: `tutorials/free-houdini-tutorial-machine-learning-with-onnx-in-houdini-20.md`

## Ruled out (already covered — do not re-suggest)
Karma XPU, heightfield/erosion, Solaris/USD variants & layering, Redshift,
Copernicus/COPs.

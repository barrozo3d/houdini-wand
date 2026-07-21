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

## Completed (ingested 2026-07-20, session 2 — APEX/MPM/rigging backlog)

- [x] **APEX production workflows** — the kinefx-apex.md reference existed but
  no ingested tutorial showed APEX used in a real production pipeline context.
  Source: Paris HUG 2026 — "APEX in Houdini: Evolving Animation Workflows for
  Production" (Mattéo Martinez)
  https://www.youtube.com/watch?v=fhgP_W-OvUE
  Ingested as: `tutorials/apex-in-houdini-evolving-animation-workflows-for-production-matteo-martinez-pari.md`

- [x] **APEX rigging fundamentals (Components/Subgraphs)** — no tutorial
  covered authoring APEX rig Components/Subgraphs from scratch.
  Source: SideFX official — "APEX Rigging | H20 MASTERCLASS" (William Harley)
  https://www.youtube.com/watch?v=-0KbPtoP5MU
  Ingested as: `tutorials/apex-rigging-h20-masterclass.md`

- [x] **MPM solver (H20.5 introduction)** — MPM had zero dedicated tutorial
  coverage despite being a major H20.5 feature.
  Source: SideFX official — "MPM | H20.5 Masterclass" (Alexandre Sirois-Vigneux)
  https://www.youtube.com/watch?v=0jJXTHjLW8g
  Ingested as: `tutorials/mpm-h205-masterclass.md`
  Companion practical: `tutorials/new-houdini-205-feature-mastering-the-mpm-snow-solver.md`
  (FaddyVFX, https://www.youtube.com/watch?v=m2c8V94OIX8)

- [x] **MPM solver (H21 new features)** — new-in-H21 MPM features (surface
  tension, per-voxel friction, post-simulation fracture/retarget nodes) were
  undocumented.
  Source: SideFX official — "H21 MPM Overview" (Alexandre Sirois-Vigneux)
  https://www.youtube.com/watch?v=nD183jP3H4Y
  Ingested as: `tutorials/h21-mpm-overview.md`

- [x] **Rig Builder (H21)** — the new Rig Builder tool had no coverage.
  Source: SideFX official — "Rig Builder" series (Max Rose)
  https://www.youtube.com/watch?v=HgX7O-q1eaY (Introduction — trailer-only,
  needs-review) and https://www.youtube.com/watch?v=VFF2TLfbU3A (Project
  Overview — actual asset-pipeline content)
  Ingested as: `tutorials/rig-builder-introduction.md` (needs-review) and
  `tutorials/rig-builder-project-overview.md`

- [x] **APEX Animate for animators (Scene Animate/Invoke, Selection Sets)** —
  no tutorial covered the animator-facing (non-rigger) side of APEX.
  Source: SideFX official — "Houdini 20 | How to Pose and Animate Electra"
  (Robert Magee)
  https://www.youtube.com/watch?v=q6GE9WmZKeI
  Ingested as: `tutorials/houdini-20-how-to-pose-and-animate-electra.md`

- [x] **H22 Copernicus Adjacency nodes (seamless texturing)** — new H22
  adjacency-node workflow for seam-free attribute rasterization was
  undocumented.
  Source: "Inside The Mind" — "Create Seamless Textures with Adjacency Nodes
  and Simulations | Houdini 22"
  https://www.youtube.com/watch?v=XKpfGoQVvQY
  Ingested as: `tutorials/create-seamless-textures-with-adjacency-nodes-and-simulations-houdini-22.md`

- [x] **Metal/PBR reflection-tailoff shading theory** — off-topic for this
  skill's Houdini scope (source video is demonstrated entirely in
  Blender/Cycles, not Houdini) but ingested per explicit request; kept as a
  renderer-agnostic materials-theory reference with a note on translating the
  technique to Karma/MaterialX.
  Source: "Forgotten Metal Knowledge | Vray, Cycles, Arnold.." (Lucas)
  https://www.youtube.com/watch?v=uz8PIi3ELJg
  Ingested as: `tutorials/forgotten-metal-knowledge-vray-cycles-arnold.md`

## Ruled out (already covered — do not re-suggest)
Karma XPU, heightfield/erosion, Solaris/USD variants & layering, Redshift,
Copernicus/COPs, PDG/TOPs (existing coverage confirmed sufficient by the
2026-07-20 full-library gap analysis — do not add a PDG tutorial based on
older/superseded notes).

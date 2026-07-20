---
title: Create Cinematic Oceans FAST | Realistic Shading & Render with Karma XPU | SideFX
source: Article
url: https://www.sidefx.com/tutorials/create-cinematic-oceans-fast-in-houdini-realistic-shading-render-with-karma-xpu/
author: Mario Leone (NodeFlow)
ingested: 2026-07-20
houdini_version: "Houdini 20.5"
tags: [ocean, whitewater, solaris, lop, karma, rendering, materialx, procedural, beginner, houdini-20]
extraction_status: complete
frames_dir: tutorials/frames/create-cinematic-oceans-fast-realistic-shading-render-with-karma-xpu-sidefx/
frame_count: 0
frame_status: skipped
---

# Create Cinematic Oceans FAST | Realistic Shading & Render with Karma XPU | SideFX

**Source:** [Article](https://www.sidefx.com/tutorials/create-cinematic-oceans-fast-in-houdini-realistic-shading-render-with-karma-xpu/)
**Author:** www.sidefx.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Create Cinematic Oceans FAST | Realistic Shading Render with Karma XPU | SideFX Forgot your password? Click here • No account yet? Please Register • Or login using EN Login Toggle Navigation Products What s New in H22 Overview Gaussian Splats Characters CFX Lookdev VFX World Building Houdini Overview VFX World Building Lookdev Characters Modeling Pipeline AI Houdini Engine Overview Engine Plug-Ins Batch Karma Renderer Overview Compare Compare SideFX Labs Partners Industries Film TV Game Development Motion Graphics Virtual Reality Synthetic Data for AI/ML Community Forum News Feed Overview Project Profiles Houdini HIVE Events Contests Jams Gallery Event Calendar User Groups Artist Directory Houdini Merch Store Learn Start Here Learning Portal | Tutorials Learning Portal | Content Learning Portal | Talks Production Projects Academic Programs Overview Students Instructors Administrators List of Schools Resources Certification Support Customer Support Licensing Overview Commercial Indie Education Help Desk | FAQ H22 System Requirements Documentation Changelog / Journal Report a Bug/RFE Try | Buy Try Buy Download Contact Info Log into your account to keep track of your progress. You can work through the lessons without logging in but your progress will be lost when you refresh the page. CREATE CINEMATIC OCEANS FAST | REALISTIC SHADING RENDER WITH KARMA XPU made in Houdini 20.5 for Beginner by Mario Leone 5/5 (2 responses) Category Oceans , World Building Posted June 24, 2025 --> In this video, we build a complete ocean from scratch, from setting up the spectrum to rendering a cinematic look in Solaris, all explained clearly and efficiently. We cover: 🌊 Ocean creation using Ocean Spectrum 🔁 Fixing wave repetition with wave instancing 🎞 Solaris workflow Houdini Ocean Procedural for optimization 🎨 From default shader to a cinematic ocean look It’s a compact yet complete dive into ocean FX, ideal for beginners and anyone looking to polish their shading/rendering pipeline. Files: ${item.title} CREATED BY MARIO LEONE Originally from Italy, visual arts have been my passion for as long as I can remember. I worked as photographer for several years and I joined the VFX industry 3 years ago. I’m working as Senior Tech Artist at Triarts, creating tools and supporting artists. I also founded NodeFlow, a Youtube channel supported by SideFX where I share educational content with the community. In 2024 I was one of the few winners of the Rookies Contest, my work has been featured by NVIDIA, and I had the chance to publish articles regarding my art in leading platforms like 3D World, Creative Bloq, The Rookies Think Tank Training Center. Find my Personal work here: https://vimeo.com/865083222 Check my Youtube channel: https://www.youtube.com/@nodeflowhoudini And Hey, if you read it until here, thank you so much, I am excited to work with you, either as Tech artist, Professor or as Houdini Generalist! More from Mario Leone COMMENTS .Shiitake 1 year ago | 1 Comment If you enter anything in this field your comment will be treated as spam pdnutz62 3 months, 3 weeks ago | at 1:57 my ocean got crumbled up how to fix Comment If you enter anything in this field your comment will be treated as spam pdnutz62 3 months, 3 weeks ago | and at 3:52 my floor didnt turn blue Comment If you enter anything in this field your comment will be treated as spam New Comment --> Please log in to leave a comment. PRODUCTS Houdini Houdini Engine Karma Renderer SideFX Labs Partners LEARN Learning Portal | Tutorials Learning Portal | Content Learning Portal | Talks Production Projects Academic Programs SUPPORT Customer Support Help Desk | FAQ H22 System Requirements Documentation Report a Bug/RFE LEGAL Terms of Use Privacy Policy License Agreement Accessibility Responsible Disclosure Program COMPANY About SideFX Careers Press Houdini Merch Store Internships Contact Info Copyright © SideFX 2026. All Rights Reserved. Choose language English 日本語



---

## Structured Notes

### Core Technique
Builds a spectral (non-simulated) ocean surface with an **Ocean Spectrum**/**Ocean Evaluate** SOP setup, removes visible tiling with a wave-instancing trick, then brings the geometry into Solaris and renders it with **Karma XPU** using the built-in **Houdini Ocean Procedural** LOP plus a hand-tuned MaterialX-style ocean shader — all in under 10 minutes of screen time.

### Summary
NodeFlow (Mario Leone, on the SideFX tutorials site) tutorial building a complete cinematic ocean from spectrum setup through Karma XPU render. In OBJ: a 300×300 grid at 1000×1000 resolution feeds an **Ocean Spectrum** node (second input) which only evaluates once piped through an **Ocean Evaluate** SOP (first input = grid, second = spectrum) — visualizing the spectrum node alone does nothing since it needs Ocean Evaluate to actually displace the surface. Spectrum tuning: resolution raised to 10 for sharper detail, grid/tile size set to 35 (this is the spectral tile period, not the OBJ grid), wind and chop both set to 1, amplitude lowered to 2.7 (the tutorial shows a side-by-side of high vs. low swell/chop to explain what each does). At this point the ocean visibly **tiles/repeats** — fixed via **wave instancing**: duplicate the grid, reduce its divisions to 30×30, run it through an Add SOP with "Delete Geometry but Keep Points" to get a sparse point cloud, feed those points into the Ocean Spectrum's **Wave Instancing** tab (radius 15, rotation 10, amplitude 0.35) so a small independent wave variation is scattered per point, breaking up the visible repetition. The result is cached to a single-frame **File Cache** (disabled "time dependent" since spectra don't need per-frame caching) because Solaris/LOPs needs the ocean imported as a *file*, not a live node — two extra SOP nodes (`out_points`, `ocean_render`) mark the cache/export points. In Solaris (LOPs): a Subnet acts as a portal to a sub-network containing a floor grid (same size as the ocean, dropped down by -2) with a **Quick Surface Material** (deep blue base color) via **Material Library + Assign Material** — needed because the ocean shader is transmissive, so an unlit floor would otherwise read as too dark. A camera + **Karma render settings/USD Render ROP** ("Karma" LOP, actually two nodes bundled) is set up *before* importing the ocean procedural, specifically because the **Houdini Ocean Procedural** LOP needs a camera present to know which region of the ocean to subdivide at high resolution (it renders in-frustum patches at higher detail than out-of-frustum). Render engine set to Karma XPU, resolution to HD. The Ocean Procedural needs two inputs wired: the cached spectrum file and the render geometry (`out_ocean_render`). Interior/proxy materials and "the cusp" (whitewater/foam geometry) are removed for a calm-looking ocean. A **Houdini Preview Procedural** LOP is required after the camera/render-settings for the ocean to actually appear in the viewport (procedurals need this to preview). Viewport quality on the Ocean Procedural controls preview subdivision density (kept conservative for interactivity, raised only for final checks) — camera screen-window Y pushed to 1.5 to get more surface detail into frame for a more dynamic first camera move. Lighting: a **Karma Physical Sky** placed before the camera; light intensity raised to ~3, and the sky's **blur falloff** raised to ~100 to remove a visible gray banding pattern in the render. Final shading pass: inside the Ocean Procedural's material network, separate Diffuse/Specular/Transmission controls exist for both the **waves** and the **foam** — wave height max raised to ~7, diffuse strength to 0.25 (adds some color instead of a flat look), specular to 1 (very specular water), transmission to 0.7, with **Enable Transmission** and **Enable Bump Mapping** toggled on in the shader settings for correct light passthrough and surface detail. Final export: stop the interactive render, set an output path on the Karma render settings, and on the **USD Render ROP** choose "render specific frame range" (e.g. 1–240, or Ctrl+Shift+click to shorten to 30 frames for a quick test).

### Key Steps
1. **OBJ setup**: Grid (300×300 size, 1000×1000 rows/cols) → **Ocean Spectrum** (2nd input) → **Ocean Evaluate** (1st input = grid, 2nd = spectrum) to get a live-previewable displaced ocean.
2. **Spectrum tuning**: raise spectrum Resolution (e.g. 10) for detail; set the spectral tile size (e.g. 35) for the repeat period; Wind = 1, Chop = 1; Amplitude lowered (e.g. 2.7) to tame overly large waves; compare high/low swell and high/low chop settings to understand their visual effect.
3. **Fix tiling with wave instancing**: duplicate the grid at lower divisions (30×30) → Add SOP with Delete Geometry (keep points) → feed the resulting points into the Ocean Spectrum's **Wave Instancing** tab (Radius, Rotation, Amplitude parameters) to scatter a small secondary wave per point and mask the tile repetition.
4. **Cache to disk**: File Cache node fed from the Ocean Spectrum, explicit file path, **Time Dependent Cache disabled** (a spectrum is one static file, not an animated sequence) — required because Solaris needs the ocean imported as a file reference, not a live SOP network.
5. **Solaris scene assembly**: Subnet (LOP network portal) → floor Grid (same size as ocean, Y offset ≈ -2) with a Quick Surface Material (deep blue) via Material Library + Assign Material, needed so the transmissive ocean shader doesn't read as too dark against an empty background.
6. **Camera + render settings first**: place camera and the "Karma" node (bundles Camera Render Settings + USD Render ROP) — set Renderer to **Karma XPU**, Resolution to HD — *before* adding the Houdini Ocean Procedural, since the procedural needs the camera frustum to know what region to subdivide at high detail.
7. **Import the Ocean Procedural**: **Houdini Ocean Procedural** LOP, wire in (a) the cached spectrum file and (b) the render geometry output (`ocean_render`); remove the interior/proxy materials and the whitewater "cusp" for a calm look; add a **Houdini Preview Procedural** LOP after the camera/render settings so it's actually visible in-viewport (required for any Houdini procedural).
8. **Detail/viewport-quality tuning**: raise Ocean Procedural viewport quality cautiously (defines subdivisions, expensive); widen camera Screen Window Y (e.g. to 1.5) to bring more high-detail ocean surface into frame for camera moves.
9. **Lighting**: Karma Physical Sky before the camera; raise light intensity (e.g. 3); raise the sky's Blur Falloff (e.g. 100) to eliminate a gray banding artifact in the render.
10. **Shading pass**: inside the Ocean Procedural's material, separately dial Diffuse/Specular/Transmission for Waves and Foam — increase wave Height Max (e.g. 7), Diffuse (0.25), Specular (1), Transmission (0.7); enable **Enable Transmission** and **Enable Bump Mapping** for correct light behavior and surface micro-detail.
11. **Export**: set output path on the Karma render settings; on the USD Render ROP choose a specific frame range (e.g. 1–240, or shortened via Ctrl+Shift+click for quick tests) and render.

### Houdini Nodes / VEX / Settings
OBJ: Grid → **Ocean Spectrum** → **Ocean Evaluate** → (duplicate grid, lower-res) → Add (Delete Geometry, keep points) → Wave Instancing points feed → **File Cache** (Time Dependent Cache off) → `out_points` / `ocean_render` output SOPs. LOPs/Solaris: Subnet → Grid (floor) → Material Library (**Quick Surface Material**, deep-blue base color) → Assign Material → Camera → **Karma** (Camera Render Settings + **USD Render ROP**, Renderer = Karma XPU, Resolution = HD) → **Houdini Ocean Procedural** (spectrum file + render-geometry inputs; remove interior/proxy/cusp materials) → **Houdini Preview Procedural** → **Karma Physical Sky** (Intensity ≈3, Blur Falloff ≈100). Ocean Procedural shader parameters: Wave Height Max ≈7, Diffuse ≈0.25, Specular ≈1, Transmission ≈0.7, Enable Transmission = on, Enable Bump Mapping = on (separate controls exist for Waves vs. Foam). Camera Screen Window Y ≈1.5.

### Difficulty
Beginner (as labeled by SideFX) — no coding, all node-based, and explicitly aimed at Solaris/Ocean newcomers — but assumes basic Solaris/LOPs navigation (Subnets, Material Library, Assign Material) and basic Karma render-settings familiarity.

### Houdini Version
Houdini 20.5 (per the SideFX course listing). Uses Karma XPU and the Houdini Ocean Procedural LOP, both stable/current features.

### Tags
#ocean #whitewater #solaris #lop #karma #rendering #materialx #procedural #beginner #houdini-20

### Gotchas
- The SideFX tutorial page itself is a thin marketing landing page; the actual technical steps in these notes were reconstructed from the tutorial's own embedded YouTube copy (same title, published by NodeFlow/Mario Leone, `youtube.com/watch?v=3PRzFfCIuqE`) via its auto-captions, since the page text alone (bullet-point description + comments) had no step-by-step detail.
- Ocean Spectrum's "grid/tile size" parameter is the *spectral* tiling period, easy to confuse with the OBJ Grid's own geometric size — both were set independently in this tutorial.
- Ocean Evaluate only previews — always needs a File Cache before going to Solaris, since LOPs imports the ocean as a file reference, not a live SOP network.
- Camera + render settings must exist *before* the Houdini Ocean Procedural is added, or the procedural has no frustum reference for adaptive subdivision — get this order wrong and the ocean either errors out or subdivides the wrong (or entire) region.
- A **Houdini Preview Procedural** LOP is required after the camera/render settings for any Houdini procedural (including the ocean one) to actually display in the viewport — a common beginner "why is nothing showing" trap.
- A visible gray banding pattern in Karma XPU renders here was fixed by raising the Karma Physical Sky's **Blur Falloff**, not a light-sampling/noise-threshold setting as might be assumed.

---

## Related Tutorials
- Cross-reference `references/dop-nodes.md` and any FLIP-fluid tutorials (tagged `flip`) for particle-simulated water — this tutorial is explicitly a non-simulated, spectral-only ocean approach (faster, no caching of a fluid sim), a useful contrast for "when do I need FLIP vs. Ocean Spectrum" decisions.
- No other ingested tutorial builds an Ocean Spectrum/Ocean Procedural setup end-to-end — this fills the "Ocean spectrum / whitewater FX" gap flagged in `KNOWLEDGE_GAPS_TODO.md` (previously only mentioned in a FLIP recipe title).

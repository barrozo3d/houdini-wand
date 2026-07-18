# Version Tracker — Houdini Release Notes

**Purpose:** Track which Houdini versions have been ingested and when the changelog was last checked.  
Used by the auto-changelog rule in SKILL.md.

---

## Last Check
- **last_checked:** 2026-07-18
- **checked_by:** Ingest session (H22 tutorials) — sidefx.com news index fetched

## Known Versions (ingested)
| Version | Reference File | Ingested |
|---------|---------------|---------|
| H22.0 (current) | `release-notes-h22.md` | 2026-07-18 |
| H21.0 | `release-notes-h21.md` | 2026-05-19 |
| H20.5 | `release-notes-h20-5.md` | 2026-05-19 |

## Versions Not Yet Ingested
- H20.0 — available at `https://www.sidefx.com/docs/houdini/news/20/index.html`
- H19.5 — available at `https://www.sidefx.com/docs/houdini/news/19_5/index.html`
- H19.0 — available at `https://www.sidefx.com/docs/houdini/news/19/index.html`

## Release Notes URL Pattern
```
https://www.sidefx.com/docs/houdini/news/{version}/index.html
# Sub-pages:
https://www.sidefx.com/docs/houdini/news/{version}/{section}.html
# Where {version} = 22, 21, 20_5, 20, 19_5, 19
# Where {section} = kinefx, model, solaris, karma, pyro, rbd, copernicus, engine, vex, viewport, mpm, crowds, ml, pdg, hqueue
```

## How to Update
1. Fetch `https://www.sidefx.com/docs/houdini/news/index.html` to check for new versions
2. If new version found, fetch its sub-pages and create `references/release-notes-hXX.md`
3. Update this file: add row to Known Versions table, update last_checked date
4. Commit and push

---

## Houdini Version History Reference
| Version | Release approx. | Key additions |
|---------|----------------|---------------|
| H21.0 | ~2024/2025 | APEX Autorig Builder, Copernicus production-ready, Vulkan default, Audio rewrite |
| H20.5 | ~2024 | Copernicus introduced, APEX Script, layered animation |
| H20.0 | ~2023 | KineFX overhaul, APEX foundations, Karma XPU beta |
| H19.5 | ~2022 | Foundations book version; KineFX, Karma CPU |
| H19.0 | ~2022 | Karma initial, Solaris stable, PDG improvements |
| H18.5 | ~2021 | SOP Pyro, improved FLIP, KineFX initial |
| H18.0 | ~2020 | KineFX introduced, Solaris/LOPs introduced |

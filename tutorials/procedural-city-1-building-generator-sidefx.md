---
title: Procedural City 1 : Building Generator | SideFX
source: Article
url: https://www.sidefx.com/tutorials/procedural-city-1-building-generator/
author: Hossam Aldin Alaliwi
ingested: 2026-07-20
houdini_version: "Houdini 18.5"
tags: [procedural, modelling, uv, materials, pdg, mantra, redshift, instancing, beginner, intermediate, advanced, houdini-18]
extraction_status: complete
frames_dir: tutorials/frames/procedural-city-1-building-generator-sidefx/
frame_count: 0
frame_status: skipped
---

# Procedural City 1 : Building Generator | SideFX

**Source:** [Article](https://www.sidefx.com/tutorials/procedural-city-1-building-generator/)
**Author:** www.sidefx.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** Procedural City 1 : Building Generator | SideFX Forgot your password? Click here • No account yet? Please Register • Or login using EN Login Toggle Navigation Products What s New in H22 Overview Gaussian Splats Characters CFX Lookdev VFX World Building Houdini Overview VFX World Building Lookdev Characters Modeling Pipeline AI Houdini Engine Overview Engine Plug-Ins Batch Karma Renderer Overview Compare Compare SideFX Labs Partners Industries Film TV Game Development Motion Graphics Virtual Reality Synthetic Data for AI/ML Community Forum News Feed Overview Project Profiles Houdini HIVE Events Contests Jams Gallery Event Calendar User Groups Artist Directory Houdini Merch Store Learn Start Here Learning Portal | Tutorials Learning Portal | Content Learning Portal | Talks Production Projects Academic Programs Overview Students Instructors Administrators List of Schools Resources Certification Support Customer Support Licensing Overview Commercial Indie Education Help Desk | FAQ H22 System Requirements Documentation Changelog / Journal Report a Bug/RFE Try | Buy Try Buy Download Contact Info PROCEDURAL CITY 1 : BUILDING GENERATOR made in Houdini 18.5 for Beginner by Hossam Aldin Alaliwi 5/5 (1 response) Category Destruction FX , Modeling Payment Required $ Posted Aug. 04, 2021 --> Procedural City in HoudiniFX VOL 1 : Building Generator Hello everyone. and welcome to this course procedural City Vol 1 building generator . 1 year ago I received an email from one of my customers. He asked me To record a tutorial about procedural City in HoudiniFX and I did it . In this course you will see with me how I can convert those boxes to this nice building Just buy one click. step-by-step I will start with you on this journey to see how we can create a smart system in Houdini FX. This system can decide where to add a window, where to add a balcony , how to create procedural UV, and How to use the imported materials from Quixel megascans , manipulate and modify it. Using this tool you can generate an infinite number of buildings. I will use those buildings in vol 2 to create a beautiful city. I will show you how to create every tiny detail you see in this building from scratch !!! I will stay away from complexity and the use of code . In addition to procedural modeling skills, this course will give you a broad idea of creating procedural UV’s and manipulating textures . Creating a PDG network is on our list in this course and the final render will be explored in Mantra RedShift. Now I'll let you watch this presentation of the final result of testing this system to randomly generate 50 different buildings !!! thank you more info here : hossamfx.org/procedural-building-generator Videos : 65 video lesson with audio (1920 × 1080). Duration – over 18 hours Houdini FX version – 18.5 Level – Beginner, intermediate Advanced All Project Files included Purchasing this course you will get : 1- 65 video lessons (1920*1080) (downloadable) 2- Project files for every Lesson, included All Models and Textures 3- Two sessions to chat and talk about your work, feedback, issues answer all your questions on Zoom Meeting software (one hour for each session) . Kind Regards!!! HossamAldin Alaliwi www.hossamfx.org CREATED BY HOSSAM ALDIN ALALIWI More from Hossam Aldin Alaliwi COMMENTS steeevenjohnson 4 years, 7 months ago | Interesting video tutorials, thanks for sharing. Do you think cloudy ceilings on the upper floors of such buildings make sense? If you do not know what it is, you can see it here https://openceilings.nl/ Comment If you enter anything in this field your comment will be treated as spam HossamAldin 4 years, 7 months ago | Thank you Dear, yes it is possible to add like those ceilings to the procedural building !!! Comment If you enter anything in this field your comment will be treated as spam jchall 4 years, 3 months ago | how does this work if you want to have different style buildings in the same scene. Comment If you enter anything in this field your comment will be treated as spam HossamAldin 4 years, 3 months ago | Hi, in fact this option is not covered in the course but you can randomly generate various building and re scatter in the scene as you want, the option that you talking about will be covered in the second part of this course !!! Comment If you enter anything in this field your comment will be treated as spam New Comment --> Please log in to leave a comment. PRODUCTS Houdini Houdini Engine Karma Renderer SideFX Labs Partners LEARN Learning Portal | Tutorials Learning Portal | Content Learning Portal | Talks Production Projects Academic Programs SUPPORT Customer Support Help Desk | FAQ H22 System Requirements Documentation Report a Bug/RFE LEGAL Terms of Use Privacy Policy License Agreement Accessibility Responsible Disclosure Program COMPANY About SideFX Careers Press Houdini Merch Store Internships Contact Info Copyright © SideFX 2026. All Rights Reserved. Choose language English 日本語



---

## Structured Notes

### Core Technique
A rules-driven "smart system" that converts simple box massing into a fully detailed building — automatically deciding window and balcony placement, generating procedural UVs, and applying imported real-world materials (Quixel Megascans) — so that a single click can generate an effectively infinite number of unique buildings from the same generator network.

### Summary
This is a paid, multi-hour Houdini course (Vol. 1 of a two-part "Procedural City" series) sold directly on the SideFX tutorials marketplace by Hossam Aldin Alaliwi — the fetched page is a sales/landing page (course description, pricing, instructor bio, purchaser comments), not a technical walkthrough, and SideFX gates the actual 65 video lessons behind payment, so no step-by-step node graph could be extracted from this ingest. What the landing page does establish technically: the course builds a **procedural building generator** entirely through node networks ("I will stay away from complexity and the use of code," i.e. VEX/Python are explicitly avoided in favor of pure SOP node chains) that takes basic box geometry and adds facade detail — deciding *where* to place windows and balconies rather than using fixed placement, generating **procedural UVs** for the resulting geometry, and importing/manipulating **Quixel Megascans** materials for realistic surfacing. The course also builds a **PDG network** (task/data-processing graph, likely for batch-generating many building variations) and renders test results in both **Mantra** and **Redshift**. The stated end-to-end deliverable is a system that can randomly generate an unbounded number of distinct buildings from one HDA-like setup — the course's own promotional render shows 50 different buildings generated from the same system — intended as the foundation for a Vol. 2 course that scatters these generated buildings into a full city.

### Key Steps
Only inferable from the course description (no lesson-by-lesson content is visible without purchase):
1. Start from simple box/massing geometry representing a building envelope.
2. Build a rules-based system that decides facade divisions and where windows vs. balconies should appear (rather than uniform/fixed placement).
3. Generate **procedural UVs** for the resulting detailed geometry.
4. Import and manipulate **Quixel Megascans** materials, applying/adjusting them across the generated facade.
5. Build a **PDG (TOP) network**, likely to batch-generate and cache many building variations/randomized seeds.
6. Render test variations in **Mantra** and/or **Redshift** to validate the look development.
7. (Implied, for the promised Vol. 2) Package the generator so many instances can be randomly generated and later scattered across a city layout.

### Houdini Nodes / VEX / Settings
Not verifiable from the available (non-paywalled) content — the landing page names no specific node types. Based on the stated deliverables, a real implementation of this kind of generator would typically involve procedural extrude/facade-division SOPs, Copy-to-Points/instancing for windows and balconies, a UV Layout/UV Flatten pass for the procedural UVs, a Material Library importing Megascans textures, and a TOP network (PDG) for batch variation generation — but none of this is confirmed by the source text, so treat it as informed inference, not extracted fact.

### Difficulty
Beginner → Intermediate → Advanced (per the course's own listed range) — an 18+ hour, 65-lesson course, so likely starts from basic procedural modeling and ramps into more advanced generator/PDG topics by the end.

### Houdini Version
Houdini 18.5 (per the course listing/pricing page).

### Tags
#procedural #modelling #uv #materials #pdg #mantra #redshift #instancing #beginner #intermediate #advanced #houdini-18

### Gotchas
- **This tutorial is a paid product**, not a free article or video — the SideFX page fetched by `ingest.py` is a course marketplace listing (title, price, instructor bio, and buyer comments), not instructional content. All "Key Steps" and "Houdini Nodes" content above is reconstructed from the course's own marketing description and is necessarily shallow compared to other library entries — there is no way to verify exact node names, parameter values, or network structure without purchasing the 65-lesson course.
- If a user asks a detailed "how do I build a procedural building generator" question, this entry can point them to the *existence* and scope of this paid course and to the general technique category (rule-driven facade generation + procedural UVs + Megascans + PDG batch variation), but should not be treated as a substitute for `references/sop-nodes.md`-level exact guidance — answer such a question by synthesizing from general Houdini procedural-modeling knowledge instead, and mention this course as a further-learning pointer.

---

## Related Tutorials
- No other tutorial in this library builds a ground-up procedural building/facade generator — existing "skyscraper" content (e.g. the RBD destruction skyscraper entries, tagged `skyscraper`, `rbd`) only uses **pre-built** skyscraper assets as destruction fodder, not generated ones. This entry fills the "Procedural city/building generation" gap from `KNOWLEDGE_GAPS_TODO.md`, though only at a scope/overview level given the paywalled source.

---
title: Working with Scientific Datasets in Houdini
source: YouTube
url: https://www.youtube.com/watch?v=GRUGv5ydLFQ
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["scientific-visualization", "data-visualization", "vdb", "bgeo", "particles", "volumes", "python", "datasets", "medical"]
extraction_status: complete
frames_dir: tutorials/frames/working-with-scientific-datasets-in-houdini/
frame_count: 4
---

# Working with Scientific Datasets in Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=GRUGv5ydLFQ)
**Author:** Houdini.School
**Duration:** 1m0s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hi, I'm Kalina Bocavić. I'm the Director of the Advanced Visualization Lab and of the Visualization Program Office at the National Center for Super Computing Applications. Working with scientific data sets is a class focusing on working with various scientific data types to create cinematic scientific visualizations in Houdini. We'll represent realistic simulations of scientific phenomena with particles. We'll use color editing for colliding planets and volumetric cloud simulations using BGEOs. I'll also show you how to use Houdini's built-in tools to visualize cloud movements. We'll learn about different file formats like OpenDDB, will import medical scan data and box lies and image stack into geometry. We'll also review common scientific data representations like adaptive mesh refinement in addition to spatial and temporal data interpolation. This will be an introduction to the data and programming side of Houdini with less focus on designer rendering. To learn more, visit my class at Houdini.

**Frame:** tutorials\frames\working-with-scientific-datasets-in-houdini\frame_000.jpg


---

## Structured Notes

### Core Technique
Importing and processing diverse scientific data formats (BGEO, OpenVDB, medical image stacks, adaptive mesh refinement) into Houdini to create cinematic scientific visualizations — with a focus on data and programming rather than artistic rendering.

### Summary
Kalina Bocavic (Director of the Advanced Visualization Lab at the National Center for Supercomputing Applications) presents a course bridging supercomputing scientific datasets and Houdini. The course covers multiple scientific data formats: BGEO for volumetric cloud and particle simulations, OpenVDB for volumetric data, medical scan image stacks converted to geometry, and adaptive mesh refinement (AMR) data. Advanced topics include spatial and temporal data interpolation between simulation timesteps. This course is data-driven and programming-oriented rather than artistically focused, targeting Houdini users who want to visualize real scientific data.

### Key Steps
1. Import BGEO files into Houdini and understand the geometry format
2. Use BGEO data to drive particle-based scientific phenomenon visualization (planets, fluids)
3. Perform color grading on particle/volume data for scientific visual encoding
4. Import and visualize volumetric cloud simulation data from BGEO
5. Load OpenVDB files into Houdini and inspect their voxel data
6. Import medical scan data (image stacks/DICOM) and convert to 3D geometry
7. Process Adaptive Mesh Refinement (AMR) data and convert to Houdini-usable format
8. Implement spatial interpolation to smooth between dataset positions
9. Implement temporal interpolation to smooth between simulation timesteps
10. Render cinematic scientific visualization shots

### Houdini Nodes / VEX / Settings
- File SOP (BGEO import)
- VDB From File SOP (OpenVDB)
- Volume Visualization SOP
- Image stack to volume (medical data)
- Attribute Interpolate SOP (temporal)
- Time Shift SOP
- Point Cloud SOP
- Python SOP (data processing)
- Geometry spreadsheet (data inspection)

### Difficulty
Advanced

### Houdini Version
unspecified

### Tags
scientific-visualization, data-visualization, vdb, bgeo, particles, volumes, python, datasets, medical

---

## Related Tutorials
- [Scientific Phenomena in Houdini](scientific-phenomena-in-houdini.md) — companion course on science-inspired VFX; related instructor, complementary approach
- [Visualizing Protein Data Bank Information](visualizing-protein-data-bank-information.md) — also by Kate Zegarace; molecular data visualization in Houdini
- [History of Houdini Systems](history-of-houdini-systems.md) — historical context on Houdini's volume and particle systems used in scientific visualization

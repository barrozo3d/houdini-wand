---
title: Visualizing Protein Data Bank Information
source: YouTube
url: https://www.youtube.com/watch?v=f7QwzqZqtFI
author: Houdini.School
ingested: 2026-06-18
houdini_version: "unspecified"
tags: ["scientific-visualization", "data-visualization", "pdb", "molecular", "attributes", "particles", "simulation", "biology"]
extraction_status: complete
frames_dir: tutorials/frames/visualizing-protein-data-bank-information/
frame_count: 4
---

# Visualizing Protein Data Bank Information

**Source:** [YouTube](https://www.youtube.com/watch?v=f7QwzqZqtFI)
**Author:** Houdini.School
**Duration:** 0m55s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hi everyone, my name is Kate Zegger-Arz, I am an instructor and also visual effects artist at Hinton University School. In this course, we will cover how to build and process protein data bank information inside a figure. You will learn how to visualize protein information including atomic values, atomic elements, bonds, finding sites, and residents. We will also cover the basics of what proteins are, how they work, and what roles they play in the human body, when they are understanding the science behind the proteins and how they are typically represented. The toolset we will be using allows us to build several different structures including space filling wirefang under the models. We can also animate our atoms based on their attributes including charge temperature factors and much more. We will also be able to simulate different bonds and interactions between atoms including vanerlul forces.

**Frame:** tutorials\frames\visualizing-protein-data-bank-information\frame_000.jpg


---

## Structured Notes

### Core Technique
Importing and processing PDB (Protein Data Bank) molecular data into Houdini to visualize protein structures — atoms, bonds, binding sites, and residues — and animating atoms by their chemical attributes including charge and temperature factors.

### Summary
Kate Zegarace (Houdini.School instructor and VFX artist) presents a course on molecular visualization using Protein Data Bank (PDB) data as the input. The course covers the biology basics of proteins (what they are, how they work) then builds the Houdini pipeline to process PDB files and generate multiple visualization modes: space-filling, wireframe, ball-and-stick models. Atoms are animated based on their chemical attributes (charge, temperature B-factors) and van der Waals forces between atoms can be simulated. This is a specialized scientific visualization course at the intersection of biology and Houdini.

### Key Steps
1. Download PDB files from the Protein Data Bank and understand their data format
2. Import PDB data into Houdini and parse atomic values (element, position, charge, B-factor)
3. Build a space-filling model — spheres at atom positions scaled by van der Waals radius
4. Build a wireframe/ball-and-stick model with bonds between atoms
5. Identify and visualize binding sites and residue data
6. Set up attribute-driven animation — scale or color atoms by charge or temperature factor
7. Simulate van der Waals forces between atoms using Houdini constraints or particles
8. Render the final molecular visualization

### Houdini Nodes / VEX / Settings
- File SOP (PDB import)
- Attribute Wrangle (atomic attribute processing)
- Copy to Points SOP (sphere per atom)
- Add SOP (bond connections)
- Attribute-driven animation (pscale, Cd)
- POP network (van der Waals simulation)
- VEX: `@element`, `@charge`, `@bfactor` custom attributes

### Difficulty
Intermediate

### Houdini Version
unspecified

### Tags
scientific-visualization, data-visualization, pdb, molecular, attributes, particles, simulation, biology

---

## Related Tutorials
- [Working with Scientific Datasets in Houdini](working-with-scientific-datasets-in-houdini.md) — broader scientific dataset import (VDB, BGEO, medical scans) from the same scientific visualization domain
- [Scientific Phenomena in Houdini](scientific-phenomena-in-houdini.md) — also by Kate Zegarace; natural and cosmic scientific phenomena visualization in Houdini
- [Attributes](attributes.md) — deep understanding of attribute types needed to process PDB chemical data effectively

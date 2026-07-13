---
title: Chocolate Swirl Effect with Houdini
source: YouTube
url: https://www.youtube.com/watch?v=4PjTMogFWqQ
author: cgside
ingested: 2026-07-13
houdini_version: "any modern (H19+, uses MaterialX/Karma)"
tags: [vdb, procedural, materials, karma, mardini, uv, displacement, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/chocolate-swirl-effect-with-houdini/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Chocolate Swirl Effect with Houdini

**Source:** [YouTube](https://www.youtube.com/watch?v=4PjTMogFWqQ)
**Author:** cgside
**Duration:** 11m14s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm gonna be breaking down how I
[0:06] did the effects of this worldly shoplot candy. So yeah let's dive into it. So here's
[0:16] the final result. As you can see it's a very small network. So we're starting
[0:26] with a quartz sphere. Then I'm clipping it and feeling the polygons. Then I'm
[0:36] creating two masks along with a group expand. So here's the first mask and I'm
[0:42] blurring it. This mask is going to be used on a mountain as a blended attribute.
[0:50] Then I have a second mask. Mask 2. Then I'm also blurring and is being used as a
[1:00] displacement in a point verb. So just a display is along normal. Then in the
[1:06] mountain I'm creating this simple mountain and is being blended by that
[1:13] initial mask. So this mask in here. This one. So that's about it for the geometry
[1:24] operations. Now we're going to start with the PDVs. So I'm creating a PDV from
[1:33] polygons. And I'm doing a volume deform and when you create a volume deform it
[1:44] will automatically create this lattice from volume. And in here after the lattice
[1:52] from volume that creates all of these points I'm creating a wrangle to get
[1:59] the topmost point. So as you can see I have it in here. If this wants to
[2:07] collaborate. So right in here as you can see these points. And then I'm doing two
[2:21] soft transforms to create the swirl effect. As you can see this one is already
[2:27] creating it. So if I disable this one and look at this. So this takes a few seconds to
[2:36] cook. So as you can see I'm doing this soft transform by grabbing the top point
[2:42] that I selected that I grouped in here. And then I'm rotating it from that group
[2:50] center and playing with the soft radius. And then I have another one.
[2:59] And as you can see this one is a bit more intense just playing with the radius and rotation
[3:05] along the eye. And you get this sort of result which is really nice.
[3:11] And now I want to incorporate a tip in here. Let's call it a tip. So what I'm doing is creating a line
[3:23] and transforming the line to a line with the topmost point that I've saved in here.
[3:33] Re-sampling it to have more subdivisions. Then doing a rig wrangle as you can see.
[3:45] So deform into some sort of spiral. Then doing a second one to bend it a bit more. I could use
[3:56] the bend the former but it wasn't giving me the correct result. I had some interpolation issues
[4:07] when I combined two or more. So that's why I opted for the rig wrangle.
[4:15] Then I'm deleting some attributes and sweeping the shape as you can see.
[4:22] We will lose some detail but it's there anyways. So I'm filling it and placing it along
[4:35] the shape as you can see. This is a bit of manual work so I can color it red.
[4:44] Then I'm transferring a mask to the initial geometry.
[4:54] Let's just visualize the mask as you can see. Then creating a VDB from polygons
[5:03] and passing the mask that I'm going to use as a mask in the VDB smooth.
[5:09] I'm also creating a VDB from this shape and re-sampling the original shape to the same amount of
[5:22] the second VDB which is a bit higher. Then I'm doing a VDB combine. As you can see, but the
[5:33] the interpolation is not the best. As you can see we have these are transitions.
[5:39] So what we can do is do VDB smooths from that mask that we saved
[5:49] and we get these sort of results which is not perfect but it will do.
[5:57] Then I'm doing a convert VDB and saving it out. From here I can convert it to a quad mesh or
[6:11] a better quad mesh and then subdividing it and re-projecting to get the initial details as you can see.
[6:21] So from here that looks a bit jagged, all the edges a bit uncontrolled and then with the ray
[6:32] and a subdivision we get a more smooth surface. As you can see with this color. Hopefully you can see it
[6:42] even with the compression. Doing a slight blur on the position, softened the normals
[6:50] and it's ready to be sent to render. Then in here I'm creating the outer shell.
[7:03] There's nothing to complicate it. I just want to mention in here that I have a mask for
[7:11] the displacement that I'm going to use in shading and doing a UV project as polar which is also
[7:21] important. Let me just disable this mask and as you can see we have a polar projection of this shape
[7:30] that will allow us to have this stretched look around this shape in here. I will show you in shading
[7:43] in just a little bit. So this is our geometry. Let's move into the shading part.
[7:52] So as you can see by this rendering you can see the stretching that we get in here
[8:03] which is on purpose to have this look. The way I'm doing that is by using the UVs
[8:13] that were created using a polar projection as I told you. Then in here I am using a X-style texture,
[8:26] a Karma X-style texture. So in the UV mode not triplanar and I'm loading the texture coordinates
[8:35] and playing with the amount of repetitions of the UVs along the UVs.
[8:45] And from here I can mix it with the mask and remap it. This texture is just a random displacement
[8:56] that I found on Megascans. Remapping it and I can show you how it looks. Let's have a look.
[9:09] So as you can see in here the displacements of the inner chocolate. So I can show you node by nodes
[9:21] with these unlit and removing the displacements. Let's see if I change this to one and one.
[9:33] As you can see it will repeat with the same amount. If I change this let's say to six. As you
[9:46] can see it will stretch and it will do the circular pattern or the polar pattern because I did the UVs
[9:56] that way. So let's set it to default. So just loading the texture and mixing with the mask in here.
[10:07] As you can see this is the mask. This is the texture
[10:14] and then just mixing it. We end up with something like this.
[10:23] So let's load the final material. The rest is just a bit of subsurface scattering and some
[10:38] chocolate color. There's nothing to complicate it. You can have a look at the file on Patreon. I'm
[10:46] going to be uploading to there and if you have any questions you can also ask me there.
[10:54] So yeah that's about it guys. I hope you have learned something new. As always if you have any
[11:02] questions you can ask me over on Patreon or send me an email and let me know your thoughts in
[11:09] the comments below. Thank you and see you next time.



---

## Captured Frames

- [0:16] tutorials/frames/chocolate-swirl-effect-with-houdini/frame_000.jpg
- [1:24] tutorials/frames/chocolate-swirl-effect-with-houdini/frame_001.jpg
- [2:36] tutorials/frames/chocolate-swirl-effect-with-houdini/frame_002.jpg
- [3:11] tutorials/frames/chocolate-swirl-effect-with-houdini/frame_003.jpg
- [4:22] tutorials/frames/chocolate-swirl-effect-with-houdini/frame_004.jpg
- [5:57] tutorials/frames/chocolate-swirl-effect-with-houdini/frame_005.jpg
- [6:42] tutorials/frames/chocolate-swirl-effect-with-houdini/frame_006.jpg
- [9:46] tutorials/frames/chocolate-swirl-effect-with-houdini/frame_007.jpg

---

## Structured Notes

### Core Technique
Builds a chocolate-swirl candy shape via mask-blended Mountain noise + Volume Deform/Lattice-from-Volume soft-transform twisting of the topmost point, adds a hand-guided curl "tip" swept and VDB-combined back into the main shape, and finishes with a MaterialX/Karma shader using a polar UV projection to create an intentional radial-stretch chocolate-swirl look.

### Summary
A compact, from-a-sphere procedural food-modeling breakdown. Geometry starts from a Labs Sphere Generator, clipped and filled, with two blurred masks built from a group-expand base: one blends a Mountain-node bump layer onto the sphere, the other drives a point-normal displacement. The signature swirl comes from converting the mesh to a VDB-backed **Volume Deform** (which auto-generates a **Lattice from Volume**), isolating the topmost lattice point via a wrangle, then applying two **Soft Transform** rotations pivoting around that point's group center (different soft radius/rotation values per pass) to twist the volume into a spiral — a slow-cooking but visually convincing swirl. A separate hand-authored curl "tip" is built from a line traced through the saved top point, resampled, and shaped with two chained **Rig Wrangle** bends (chosen over the native Bend SOP because stacking multiple Bends produced bad interpolation artifacts) — swept into a small tube, manually color-tagged, and merged back into the main VDB via **VDB Combine** + a mask-driven **VDB Smooth** to blend the transition seam (imperfect, but "will do"). The combined VDB is converted back to a quad mesh, re-projected onto the pre-VDB detail to recover surface fidelity, lightly blurred/normal-softened, and paired with a separate outer shell shape (with a saved displacement mask for later shading use). The material's key trick is a **polar UV projection** on the shell, feeding a MaterialX/Karma image texture (a Megascans displacement/detail texture) whose UV-repeat count controls how tightly the texture streaks radially around the swirl — remapped and masked-blended with the chocolate base color/subsurface material for the final "melted chocolate" look.

### Key Steps
1. **Base shape**: Labs Sphere Generator → Clip → Fill (Poly Fill) for a rounded base blob.
2. **Two blurred masks from a group-expand base**: Mask 1 blends a **Mountain** noise displacement onto the sphere (bump-style surface detail); Mask 2 drives a **Point VOP** displacement along the normal — both masks are blurred before use to soften their edges.
3. **Volume Deform setup**: **VDB from Polygons**, then a **Volume Deform** node (which automatically creates a **Lattice from Volume** to drive it), followed by a wrangle isolating just the topmost point of the generated lattice (used as the pivot for the swirl).
4. **The swirl**: two chained **Soft Transform** nodes, each rotating around the topmost point's group center with independently tuned Soft Radius and rotation values — the first pass establishes the base spiral, the second (higher intensity, different radius/rotation-axis) deepens it into the final candy-swirl look. Note: this volume-based deform is slow to cook (several seconds per change), so iterate patiently.
5. **Hand-built curl "tip"**: draw a Line through the saved topmost point, Resample for more subdivisions, then apply two chained **Rig Wrangle** bends to curl it into a spiral tip shape — chosen specifically over the native **Bend** SOP because stacking multiple Bend nodes produced bad interpolation when combined.
6. Delete unneeded attributes, **Sweep** the curled line into a small tube (some fine surface detail is lost in this step, but it's acceptable), **Fill** the ends, and manually position/orient the tip against the main swirl shape (some manual placement work, tagged with a red color for visual reference during setup).
7. **Merge tip and body via VDB**: transfer a mask from the tip onto the main geometry, build **VDB from Polygons** for both the main shape and the tip (tip resampled to a *higher* resolution to match), **VDB Combine** them — the raw combine seam looks rough — then run a **VDB Smooth** using the transferred mask to blend just the seam region (imperfect but sufficient result).
8. **Back to mesh**: **Convert VDB** to a quad mesh (optionally a higher-quality quad conversion), Subdivide, then **Ray**-project back onto the pre-VDB detailed geometry to recover fine surface detail lost during the volume round-trip — cleans up the initially jagged/uncontrolled edges into a smooth surface. Finish with a slight position Blur and softened normals before sending to render.
9. **Outer shell**: a simpler secondary shape (no major new technique), carrying a saved displacement mask for later use in shading, with a **UV Project set to Polar** — deliberately chosen (rather than a standard/planar projection) specifically to produce a radial "stretched" texture look around the candy.
10. **Shading — the polar-stretch trick**: in the MaterialX/Karma network, use an image texture node in **UV mode (not triplanar)**, feeding the texture-coordinate UVs with a controllable repeat count. Because the UVs were generated via polar projection, changing the UV-repeat value (e.g. 1×1 → 6×6) visibly stretches the texture into the candy's characteristic circular/radial streaking pattern rather than tiling normally.
11. Mix the stretched texture (a Megascans displacement/detail image, Remapped for contrast) with the earlier-saved mask to control where the effect shows, then blend into the final chocolate material (subsurface scattering + a chocolate base color) — no further complexity beyond that for the final look.

### Houdini Nodes / VEX / Settings
Labs Sphere Generator → Clip → Poly Fill → group-expand masks (blurred) → **Mountain** (blended by Mask 1) + **Point VOP** (normal displacement via Mask 2) → **VDB from Polygons** → **Volume Deform** + auto-generated **Lattice from Volume** → topmost-point wrangle → 2× **Soft Transform** (group-center pivot, tuned Soft Radius/rotation) for the swirl · Line (through top point) → Resample → 2× **Rig Wrangle** (chained bends, avoids Bend-SOP interpolation issues) → Attribute Delete → Sweep → Fill (curl tip) → mask transfer → **VDB from Polygons** (both pieces) → **VDB Combine** → mask-driven **VDB Smooth** → Convert VDB (quad mesh) → Subdivide → **Ray** (reproject detail) → Blur (position) + soften normals · outer shell shape + saved displacement mask + **UV Project (Polar)** → MaterialX/Karma image texture (UV mode, tunable repeat count) → Remap → mask blend → chocolate material (subsurface scattering + base color).

### Difficulty
Advanced — combines volume-based (VDB) deformation, lattice/soft-transform swirl construction, custom wrangle-based curve bending, and a deliberate polar-UV shading trick; not a beginner geometry workflow despite the compact node count.

### Houdini Version
Not stated explicitly; uses MaterialX/Karma shading (image texture, UV mode) consistent with any modern Houdini H19+.

### Tags
#vdb #procedural #materials #karma #mardini #uv #displacement #intermediate #advanced

---

## Related Tutorials
No other indexed cgside tutorial currently covers VDB-based swirl/lattice deformation or polar-UV shading tricks — cross-link with any future VDB or MaterialX/Karma shading tutorials once extracted from this batch.

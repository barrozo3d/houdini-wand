---
title: Houdini to Unreal: HDA Setup and Workflow
source: YouTube
url: https://www.youtube.com/watch?v=fgUIMtGLIrI
author: cgside
ingested: 2026-07-13
houdini_version: "20.5"
tags: [vex, python, pipeline, unreal, houdini-engine, instancing, materials, procedural, advanced]
extraction_status: complete
frames_dir: tutorials/frames/houdini-to-unreal-hda-setup-and-workflow/
frame_count: 7
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini to Unreal: HDA Setup and Workflow

**Source:** [YouTube](https://www.youtube.com/watch?v=fgUIMtGLIrI)
**Author:** cgside
**Duration:** 19m27s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm gonna show you how you can
[0:06] setup HDAs to work in Unreal without any engine by setting the materials,
[0:14] vertex scholars to use as masks, light instanceing and geometry instanceing to.
[0:22] So we're gonna go to the full setup and show you how you can have these parameters exposed,
[0:33] like loading static meshes, blueprint lights and all the material instance that you need for your
[0:42] materials. So yeah let's get started. So we're going to start with this setup already,
[0:53] so with geometry modeled and generator working, it's not the perfect generator as it creates some
[1:06] two random shapes but we can work with it. So let's start by selecting everything and creating a
[1:17] subnet. We're gonna call it light, light, light generator, light generator demo.
[1:40] And the first thing we're going to do is to edit parameter interface and select everything with
[1:53] control-lay and make this invisible and we will start to drag our parameters. So I have here a
[2:03] global seed that I want to expose, so I'm gonna drag it and I'm gonna apply. I also have a secondary
[2:17] seed that I want to expose to. As you can see it's creating the secondary seed for the outer shape.
[2:29] Now is the album messed up. So let's say we like this one and I'm gonna drag it and call it say
[2:43] the secondary seed. And what else do we need? So we also have like mishack mountain.
[3:01] And it's not this one. Is this one? Let me check. Yeah, is this one? I want to expose
[3:19] the amplitudes, the element size and the offset. So let's see to apply and create a folder.
[3:34] Let's set it to simple and change it to global. And drag the seeds in here. Let's create another one.
[3:45] So now let's save it to nice and foreign. And I'm gonna drag the min here, change it to simple and apply.
[4:03] So the next thing we're going to set up is the geometry in the scene. Since we have repetitive
[4:16] objects we don't want to export everything as single geometry. So I'm gonna go in here and instead of
[4:27] this copy to points I'm gonna just output the points. And we can set up the Unreal instance.
[4:40] So we can just use an attribute wrangle and say string at Unreal instance is equal to
[4:58] channel string and we're gonna name it spat to land.
[5:09] And now if you have already your geometry in Unreal exported to Unreal which you don't have
[5:17] you can copy the reference path or the relative path and paste it in here.
[5:25] But we don't have it right now so let's keep it empty. And now we want to expose it, expose this
[5:37] path in our in our hda. So I'm gonna drag this in here. That's why we created the parameter.
[5:51] And let's create a new folder and set it to simple and call it Unreal.
[6:01] Unreal oops.
[6:08] And let's save path to lamp.
[6:13] And now we want to set up. We want to set one real that this is or to odd in engine.
[6:23] That is supposed to be a static mesh. So what we can do is come down here under tags and add one.
[6:35] And first we want to create the input itself so we're gonna use Unreal.
[6:42] Ref and set it to one.
[6:47] And now we're going to use Unreal.
[6:53] Ref class and set it to static mesh.
[6:59] Otherwise we will have a list of blueprints, lights and whatnot.
[7:04] So let's apply.
[7:08] And we also want some points to instance the
[7:18] a light, a point light, because the geometry is not going to be enough.
[7:24] So what we can do is to create another set of points. So let's drag this one.
[7:36] Let's merge.
[7:41] And we're gonna say
[7:43] a
[7:47] path to light
[7:52] and delete this parameter. Delete.
[7:57] And create this one.
[8:00] And we also want to beat it a little bit. So the light goes a bit out.
[8:08] So let's pick it by, let's say point 0.2.
[8:16] So I have the normals in here. And we can pick it by a little bit.
[8:24] And we might want to keep the normals.
[8:29] Okay, now let's drag this one in here.
[8:34] So path to light.
[8:38] And let's also add
[8:42] Unreal and real ref one.
[8:47] And in this case,
[8:49] Unreal ref class,
[8:53] we want to set it to blueprints.
[8:55] So we can instance
[8:57] blueprints with a light.
[9:03] So let's apply.
[9:08] And now we want to separate these outputs.
[9:12] So let's create another one.
[9:19] So let's create another one.
[9:22] And we can create another one.
[9:24] And this will be output one.
[9:26] And let's remove it from here.
[9:29] So in here we have this set of points.
[9:33] For the light fixture,
[9:34] fixtures.
[9:36] And in here we have the geometry.
[9:42] Now for the material,
[9:44] we have the geometry.
[9:46] And we have the geometry.
[9:48] And we have the geometry.
[9:50] And we have the geometry.
[9:52] Now for the materials,
[9:54] let's see what can we do in here.
[10:00] So Unreal material.
[10:11] Let's see.
[10:15] We can set up materials for that.
[10:17] But let's just create one in here.
[10:20] So let's create an Unreal material.
[10:28] And we're going to call it.
[10:38] We can actually place it in here.
[10:45] And we're going to call it.
[10:48] It's already set up by default.
[10:49] It's an attribute create.
[10:51] So primitive class as a string.
[10:58] And we're going to replace this
[11:03] by main structure mat.
[11:09] And rest we can leave default.
[11:15] And we already have a material.
[11:17] Unreal material color,
[11:20] which is the vertex normals.
[11:22] In this case, it's primitive,
[11:24] but Unreal will will will read it fine.
[11:27] So we have color and real material,
[11:31] normals and position.
[11:34] And right here,
[11:37] we have Unreal instance.
[11:42] So let's make sure we don't delete it.
[11:45] No, neither the p-scale
[11:47] or the n.
[11:51] So
[11:56] we need to output them to place the material as a parameter too.
[12:03] So where we have that in here.
[12:07] So let's take this string.
[12:17] Place it in here.
[12:20] And let's say,
[12:23] main structure mat.
[12:36] And now we want to create the text.
[12:41] Unreal ref.
[12:47] Set one.
[12:49] And now,
[12:51] Unreal,
[12:53] Unreal,
[12:54] ref class,
[12:56] set to material instance.
[13:00] Since we're going to use not master materials, but instances.
[13:05] So let's apply and accept.
[13:09] And I believe this will be good enough for our tests.
[13:15] So let's
[13:18] merge it.
[13:22] And we have the points and the structure.
[13:25] And everything should be working.
[13:29] So I had a small issue when that will rebuild the parameters,
[13:33] but the look is actually the same.
[13:36] So one thing you need to do is to remove this lambda generator from
[13:41] inside the HTA before you build it.
[13:45] Otherwise, you will have issues.
[13:48] Other than that, we have the same.
[13:50] Maybe a different shape.
[13:52] So in this lambda generator,
[13:55] I'm going to export it as an FBX with the following settings.
[13:59] ZApp,
[14:01] convert to specified access system and convert units.
[14:05] We have covered this before in the other Unreal video that I have.
[14:10] And in order to use this static mesh input,
[14:16] in order to use the materials, you need to set up
[14:20] primitive attributes and name it Shop Material Paths
[14:27] and give it default name.
[14:29] Then we can replace Unreal.
[14:32] So Shop Material Paths and select your meshes in here.
[14:38] And then you can just export this.
[14:41] So I'm going to have this ready in Unreal.
[14:45] And now let's save the digital assets.
[14:50] So let's call it by GenDemo.
[15:00] And let's
[15:01] set create digital assets.
[15:07] And I'm going to say digital assets don't add alter.
[15:13] Let's leave diversion.
[15:16] And let's not add type category.
[15:19] And let's say it's in the page DA.
[15:23] So let's create.
[15:25] And now everything should work fine.
[15:27] We have our parameters.
[15:30] And we have our inputs.
[15:34] And outputs.
[15:35] And we can just apply and accept.
[15:40] And all the changes that we make to this, we're not going to use added parameter interface,
[15:46] but actually type properties.
[15:48] And you go to the parameters and change it in here.
[15:52] So let's go to Unreal and see if everything is working.
[15:59] So here we are in Unreal.
[16:01] Let me add this one and let's import the new one.
[16:07] So I'm going to HDA import.
[16:11] And I'm going to go to this project.
[16:16] And HDA.
[16:20] And we wanted this.
[16:22] So like GenDemo, I believe is this one.
[16:27] Yes.
[16:29] So let's open.
[16:31] Make sure you create a session in your own engine.
[16:36] And let's drag this one.
[16:40] It's building.
[16:42] Cooking.
[16:43] And it is working properly.
[16:49] Let me just copy to a position in here.
[16:59] And as you can see, we have the vertex colors and we have the instances.
[17:07] Let's see.
[17:08] If we have the parameters, so you have static messages in here,
[17:16] that we can load the LEMG.
[17:20] That is already working.
[17:22] We have the petal light, which is a blueprint that I already prepared.
[17:26] Light will print.
[17:28] There you go.
[17:30] And now we have the material.
[17:33] Only one this time for the menstrual share.
[17:36] Let me see if I can find it in here.
[17:43] So it should be on M.
[17:52] Let me just check in here.
[18:00] Is this one?
[18:01] And as you can see, we can only select material instances in here.
[18:13] And in here, we can only select blueprints as we define that.
[18:17] And in here, only static messages.
[18:19] This is a nice way to filter.
[18:22] And the UnrealRef equals to 1.
[18:25] It just means that we can have these nice input in here.
[18:30] And then we define the class.
[18:33] So let's test it here.
[18:38] So we can change the global seed.
[18:40] And we can change the amplitude of the noise to the form a bit more in the shape.
[19:01] And change the element size to find 6, for example.
[19:06] And we start to get some nice shapes.
[19:11] So yeah, guys, that's basically what I wanted to share with you today.
[19:16] Feel free to grab the al dini file on my Patreon.
[19:21] And hopefully you'll learn something new today.
[19:24] Thank you.



---

## Captured Frames

- [0:55] tutorials/frames/houdini-to-unreal-hda-setup-and-workflow/frame_000.jpg
- [4:30] tutorials/frames/houdini-to-unreal-hda-setup-and-workflow/frame_001.jpg
- [6:40] tutorials/frames/houdini-to-unreal-hda-setup-and-workflow/frame_002.jpg
- [10:05] tutorials/frames/houdini-to-unreal-hda-setup-and-workflow/frame_003.jpg
- [15:30] tutorials/frames/houdini-to-unreal-hda-setup-and-workflow/frame_004.jpg
- [16:40] tutorials/frames/houdini-to-unreal-hda-setup-and-workflow/frame_005.jpg
- [18:50] tutorials/frames/houdini-to-unreal-hda-setup-and-workflow/frame_006.jpg

---

## Structured Notes

### Core Technique
Building a **Houdini Digital Asset (HDA)** that runs live inside Unreal via the **Houdini Engine** plugin — no baking to FBX required — exposing noise/seed parameters for live procedural regeneration, using the `Unreal_instance` string attribute + point-cloud outputs to instance both **static meshes** and **Blueprint actors** (e.g. lights) directly from Houdini points, and tagging exposed asset-reference parameters with `unreal_ref`/`unreal_ref_class` so Unreal's picker UI only shows the correct asset type (Static Mesh, Material Instance, or Blueprint) per slot.

### Summary
Starting from an existing procedural lamp/branch generator (a two-seed noise-driven shape generator with imperfect but usable results), the whole network is wrapped in a **Subnet** and converted into an HDA via **Edit Parameter Interface**: relevant internal parameters (global seed, secondary seed, Mountain noise amplitude/element size/offset) are dragged out into user-facing folders (organized as "Simple" type folders, e.g. a "Global" folder for seeds) so they can be tweaked live from Unreal without reopening Houdini. Since the scene has repetitive geometry (e.g. lamp shade/bulb pieces), rather than exporting full duplicated geometry the network switches from **Copy to Points** to outputting just the **points**, with a wrangle setting a string `Unreal_instance` attribute (`s@Unreal_instance = chs("path_to_lamp")`) — if the referenced Unreal asset is already imported, its content-browser reference path is pasted directly into this exposed string parameter; otherwise it's left blank and filled in later once the asset exists in Unreal. That `path_to_lamp` string parameter itself is exposed via the parameter interface (organized under a new "Unreal" folder) and tagged, under the parameter's **Tags** section, with `unreal_ref = 1` and `unreal_ref_class = StaticMesh` — this makes Unreal's asset picker for that parameter show *only* Static Mesh assets rather than every asset type. A second point set is built the same way for **light fixtures**: merged in, peaked slightly along the normal (to move the light instance origin a bit outward, preserving normals), given its own exposed `path_to_light` string parameter tagged `unreal_ref = 1` / `unreal_ref_class = Blueprint` this time (since the light is a **Blueprint actor**, not a static mesh) — letting Unreal's picker for that slot show only Blueprints. The two point sets (geometry-instance points and light-instance points) are routed to **separate Output nodes** (Output 0 for the light-fixture points, a later Output for the main structure geometry) so Houdini Engine creates distinct instancers per output in Unreal. For materials: an **Attribute Create** sets a `primitive class`-style string (renamed to something like `main_structure_mat`) which is then exposed the same way as the mesh/light paths — a string parameter tagged `unreal_ref = 1` / `unreal_ref_class = MaterialInstance` (using Material *Instances*, not master materials, since instances are the swappable/parameterized asset type in Unreal) — plus the geometry already carries vertex color (from a "material color" attribute reading normals/position) that Unreal reads directly as vertex colors for masking in the shader. Before building the actual HDA, a note: the *procedural generator subnet itself* must be removed from inside the HDA before building it as a distributable asset, or the build will error (the generator's job is done — you don't want that costly regeneration logic baked into every runtime cook of a shipped asset). For any actual static mesh that will be exported and used as an `Unreal_instance` reference target, a `Shop_Material_Path` primitive attribute (default-named) must be set (via a String parameter node or similar) referencing the intended Unreal material path before FBX export (Z-up axis conversion + unit conversion enabled, as covered in a prior video) — this is what lets Unreal auto-assign the correct per-primitive material slot on import. Finally, **File → Digital Asset → New Asset** converts the subnet into a proper `.hda` file (embedded in the current Houdini project, no type-category prefix needed); all further parameter/tag edits to an already-built HDA must go through **Type Properties**, not Edit Parameter Interface directly on the instance. In Unreal, the HDA is imported via the Houdini Engine plugin (File → HDA Import), dragged into the level (it cooks/builds live), and the exposed parameters now show as an Unreal-native details panel: the static-mesh slot only accepts Static Meshes, the light slot only accepts Blueprints (a pre-built "petal light" Blueprint is assigned), and the material slot only accepts Material Instances — with the noise seed/amplitude/element-size parameters fully live-tweakable inside Unreal, regenerating the procedural shape in real time via Houdini Engine's cook.

### Key Steps
1. **Wrap the generator in a Subnet:** select the whole procedural lamp-generator network, convert to a **Subnet**, name it descriptively (e.g. `light_generator_demo`).
2. **Expose core control parameters:** via **Edit Parameter Interface**, drag out the global seed, secondary seed, and Mountain noise's amplitude/element-size/offset parameters into new user-facing "Simple" folders (e.g. a "Global" folder) so they're tweakable without opening the subnet.
3. **Switch repetitive geometry to points-only output:** instead of a **Copy to Points** node baking full duplicated geometry, output just the underlying **points** so Unreal can instance a single referenced mesh per point instead of embedding many copies.
4. **Set the Unreal_instance attribute:** in a wrangle, `s@Unreal_instance = chs("path_to_lamp")` (or similar) reads a to-be-exposed string channel — paste the target Unreal asset's content-browser reference/relative path here once it exists, or leave blank if not yet imported.
5. **Expose and tag the mesh-reference parameter:** expose `path_to_lamp` as a string parameter (organized under a new "Unreal" folder); in the parameter's **Tags** section add `unreal_ref = 1` and `unreal_ref_class = StaticMesh` so Unreal's asset picker for this slot only lists Static Mesh assets.
6. **Build a second point set for lights:** merge in another set of points representing light-fixture locations; **Peak** slightly along the normal (preserving normals) to offset the light instance origin a bit outward from the surface.
7. **Expose and tag the light-reference parameter:** give this point set its own exposed `path_to_light` string parameter tagged `unreal_ref = 1` / `unreal_ref_class = Blueprint` (since a light in this workflow is instanced as a **Blueprint actor**, not a static mesh) — Unreal's picker for this slot then only shows Blueprints.
8. **Split outputs per instance type:** route the light-fixture points and the main-structure geometry to **separate Output nodes** (e.g. Output 0 for lights, a later output for structure) so Houdini Engine creates distinct per-type instancers in Unreal.
9. **Material parameter exposure:** use **Attribute Create** to set a primitive string attribute (renamed to something like `main_structure_mat`), expose it as a string parameter the same way, tag `unreal_ref = 1` / `unreal_ref_class = MaterialInstance` (Material Instances, not master Materials, since instances are the swappable asset type) — geometry additionally carries vertex-color data (from a normals/position-based "material color" attribute) for Unreal to read as a native shader mask.
10. **Remove the generator subnet before building:** critically, delete/remove the original procedural-generator subnetwork from inside the HDA before building it — leaving it in causes build errors and bakes unnecessary regeneration cost into the shipped asset.
11. **Prep any exported static mesh for material auto-assignment:** for meshes that will be FBX-exported and referenced as `Unreal_instance` targets, set a `Shop_Material_Path` primitive attribute (default name) pointing at the intended Unreal material path before export; export via FBX with **Z-up axis conversion + unit conversion** enabled (covered in a prior video).
12. **Create the Digital Asset:** **File → Digital Asset → New Asset**, name it (e.g. `lamp_gen_demo`), leave version/type-category defaults, save embedded in the current project — converts the subnet into a distributable `.hda` file.
13. **Post-build parameter edits go through Type Properties:** once an HDA is built, further parameter/tag changes must be made via **Type Properties** on the node type, not Edit Parameter Interface directly on an instance.
14. **Import and test in Unreal:** in Unreal, use the Houdini Engine plugin's **HDA Import**, locate the `.hda` file, drag it into the level (requires an active Houdini Engine session) — it cooks/builds live; assign the static mesh, Blueprint light, and material instance in the now Unreal-native, type-filtered details panel, then live-tweak the exposed seed/noise parameters to regenerate the procedural shape directly inside Unreal.

### Houdini Nodes / VEX / Settings
Nodes: Subnet, Edit Parameter Interface (Simple folder type, per-parameter Tags: `unreal_ref`, `unreal_ref_class` with values `StaticMesh`/`Blueprint`/`MaterialInstance`), Attribute Wrangle (VEX: `s@Unreal_instance = chs(...)` string-channel assignment), Peak (normal-preserving offset), Merge, Output (multiple, split by instance type — lights vs. structure), Attribute Create (material-path string attribute), material-color attribute setup (normals/position-derived vertex color), Shop_Material_Path primitive attribute (for FBX-exported static meshes), ROP FBX (Z-up axis conversion, unit conversion), Digital Asset / New Asset (HDA creation, embedded in project), Type Properties (post-build parameter/tag editing). Unreal + Houdini Engine plugin: HDA Import, live cook/build on drag-in, type-filtered asset-picker details panel (Static Mesh / Blueprint / Material Instance per tagged parameter), Blueprint actor instancing (e.g. a pre-built "petal light" Blueprint).

### Difficulty
Advanced/Expert — combines HDA parameter-interface authoring, Houdini Engine's Unreal-specific attribute/tag conventions (`Unreal_instance`, `unreal_ref`/`unreal_ref_class`), and FBX/material-path export prep; assumes familiarity with both Houdini HDA workflows and Unreal's Houdini Engine plugin.

### Houdini Version
20.5 (UI matches Houdini 20.5-era HDA/Houdini Engine toolset; references a prior video covering the FBX Z-up/unit-conversion export step in more detail).

### Tags
#vex #python #pipeline #unreal #houdini-engine #instancing #materials #procedural #advanced

---

## Related Tutorials
Direct companion to export-a-full-scene-from-houdini-to-unreal.md (same author, same Houdini-to-Unreal pipeline domain, explicitly references "the other Unreal video" for the FBX export settings) — cross-link explicitly.

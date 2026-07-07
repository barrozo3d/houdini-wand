---
title: The Only HAIR GROOMING Tutorial You Need! (Houdini for Artists)
source: YouTube
url: https://www.youtube.com/watch?v=rVogGr7f0Cg
author: June Chevalier
ingested: 2026-07-07
houdini_version: "Not specified (H20–H20.5 UI)"
tags: [sop, curves, attributes, procedural, vex, wrangler, modelling, beginner, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/the-only-hair-grooming-tutorial-you-need-houdini-for-artists/
frame_count: 11
---

# The Only HAIR GROOMING Tutorial You Need! (Houdini for Artists)

**Source:** [YouTube](https://www.youtube.com/watch?v=rVogGr7f0Cg)
**Author:** June Chevalier
**Duration:** 85m25s | 11 section(s)

---

## Raw Data (for Claude Code extraction)


### Introduction [0:00]
**Transcript:** Hey, my name is June, today I'm going to walk you through how I approach hair grooming in  Houdini.  This is not the only approach, but this is what I found to be the most convenient for me.  I also like to add that hair grooming in Houdini I found to be less bugger than X-Gen in  Maya.  I know some bugs in X-Gen that I've encountered since Maya 2018 and they still haven't  been fixed by now in Maya 2025.  So yeah, this tutorial will be beginner friendly, so anyone with a prior Houdini experience  can follow along and if you're really new and you don't know about it, you can actually  get Houdini Apprentice for free from SideFX's website.  So please download Houdini Apprentice if you want to follow along.  Alright, let's get started.  In order to do hair grooming, we need three things.  The mesh, the guides and then the generated hair itself.  So the first thing we do after we open Houdini is to import our mesh.

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_000.jpg

### Importing Mesh [1:02]
**Transcript:** So in order to do that, we are still in the object level.  So press tap and then we type in geometry.  This is the geometry node.  So let's rename this to something that makes sense, maybe like this.  And then we dive into this node and we add the file node.  Okay, so let's bring in the file.  Right, so why do I not see anything here?  Because one thing to note when importing a geometry to Houdini is the scale of your  objects.  So by default Houdini uses meter.  So for example, if model something in Maya, the size of it is 15 centimeters in height.  So when you import the model into Houdini, it will become 15 meter in size.  The scale will affect simulation and material such as subsurface scattering.  So we have to actually pay attention to that.  So there are two ways we can change the scale of our model in Houdini.  First of all, it's by changing Houdini's default unit of measurement.  But we're not going to do that now because we're going to bring in a node called transform.  This will have the ability to uniform scale your model.  So let's 2.01.  This will divide the model by 100.  And now we can see the model.  So if you want to take the size of your model, you can actually look at it here the size.  So this was 36 meters in height.  But then after transforming the model, now we can see that it's 0.3 meters, which means  this is 36 centimeters.  So that's what we want.  So one thing to note, if you want to change the scale down to centimeters before setting,  it's better to do it before you do anything else because that will avoid any simulation,  miscalculation, lera.  Okay, so before we go on to making the guides, I would like to make a mask.  And this mask will determine where the hair will grow.

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_001.jpg

### Masking [3:42]
**Transcript:** So in order to make a mask, we use a node called attribute pain.  It's right here.  So I'm just going to work on the health of the model because we can mirror to the other  side later on using a node.  So let's do that.  Press enter the field port.  And this will allow you to paint the mask.  Right?  So if you press control, you are er, you're raising the mask.  So let's start painting.  Let's say we're satisfied with it, right?  We can always change it later because good thing about Houdini is it's non-destructible.  So what I'm going to do now is to mirror the mask to the other side.  How do you do that?  We add a node called attribute mirror.  First of all, we need to change the name and we'll call it density mask.  Right?  So here, always changes.  Okay, sorry about that.  Okay.  So this will be the density mask.  If we go down here and we attribute copy genes to other attributes and then we change  the mirroring method to topology because clearly we can see that my model is not symmetrical.  But the topology is symmetrical.  So we zoom in and we choose the middle point and we double click.  Yeah, something like this and then we press enter.  You're going to see all this identity of the middle point here.  Now in the attribute name, I think it should be points, right?  Yeah, let me choose density mask.  So if we turn on density mask here, if we show density mask, we can see how the entire mask  will look like.  Okay, let's say this is good enough, right?  Let's finish this up first.  Let's call in the node.  So this node will be like the export or the output node.  So let's call it out mask.

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_002.jpg

### VDB [7:44]
**Transcript:** So next thing is to set up our VDB.  So Houdini uses VDB to calculate the collision of the hair against our model.  So in order to do that, we need the model to be airtight, not like this.  So first of all, we need to from here, let's call in the polyfill node.  So this polyfill node will fill in the gap so we can actually do however we want, you  know, something like this, maybe.  Right?  So that our model now is airtight or watertight, however you want to call it.  We can add in the next node, which will make our model into VDB.  Let's call VDB from polygon.  So this is very low res collision point, right?  So let's increase it.  We can decrease it, but we want to decrease it because we want the model or the voxels  to be dense enough.  So something like 0.002, this is good.  0.001 is perfect.  This is what we want.  So now we can add in the null, which will be the output.  Right?  So let's call this out VDB.  Right?  Something like that.  Now that we are finished with everything, we can always go back here, later on if we find  any trouble.  Let's go back to the object level right here, you click here.

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_003.jpg

### Making the Guides [9:56]
**Transcript:** And let's add a guide boom node.  Let's rename this to something that makes sense.  The guide for the main hair.  So in here we can check the parameters right here, right?  So first of all, we want to define where this skin is, so we can...  Just with the mask right here, right?  We can see that all these guides are spawned all over our model.  We can increase the density right here.  And if we want the guides to just spawn on the mask that we have painted, we sense this  to skin attribute.  And we click, I will pick the density mask from the drop down menu and then everything  will be just like what we want.  What I want is to draw its guide.  So I don't want to just...  I mean you can do this if you want to and you can pick any seed.  You can play around with the seeds, scatter seeds so that you can just get a good start,  but that's not what you want.  Let's put it in zero because what I want is a full control width.  You can do by drawing each guide.  So let me show you how.  So first we dive in, right here we add another guide boom node.  This will connect everything automatically.  And here's where we do the majority of the guide work.  So there are many tools you can use here on the drop down menu here, right here.  Draw a plan to lead, but I won't explain every single one because you can play around  with them yourself.  What I'm going to do is to show you what I actually use.  So we can use the plan and draw right here on the top to create each guide manually.  There's no secret to instantly be good at hair grooming.  It takes time and practice.  So my advice is to just look at reference and try to replicate what you see.  No?  Maybe from here?  Oh yes.  You can actually do it from here, right?  So this way we can see where we plan.  We should plan or draw the guide.  So let's do it right now.  Let me show you.  So if you want to select some guide, you want to draw the one you have had the other  guides, you can press as to select.  And then you do it.  Where is it?  It's a primitive, right?  So you can select everything.  It's just some part of it.  Then you press enter to get back to sculpting.  And you can sculpt just one or whichever guide that you have selected, right?  So this is a really good way to isolate some of these guides.  So let's say you're happy with the guides, something like this, right?  We don't have to make the guides too dense because what I like to do next is to summon  the node called hair generate.  So let's first let's plug in everything in the right place.  And what this node does is actually it will generate hair and fill in the gaps between  these guides, right?  So we don't have to manually add more guides one by one.  Just need to do the the main shape of the hair and then we generate the hair.  But first what we want to do is to apply the mask that we've created.  Then now we can add more density.  Let's uncheck this just to make sure something like this.  This is pretty dense, okay?  And then what I like to do next is to just play around with the influence radius.  This looks nice.  And then just increase the influence decay maybe.  And then what I like to do next is to summon the node called what is it called?  Hair clumping because we want this to clump together, right?  First of all, we define where the clumping would go and I have actually created a mask here  called clump mask.  And what this mask will do is to define where I want the clumping to go.  So let's do that by decreasing the clump size.  Something like this probably.  And then before we go and generate the hair, what I like to do is to go here to attributes  and disable all output because we're not going to use any of these attributes to generate  the actual hair.  If you turn this on, this clumping will affect the generated hair, which we don't want  at the moment because we'll do that separately.  Okay, so now good practice to do before we generate the hair is to just summon the  guide deform and this will keep your hair.  If you use animated skin, for example, the hair will stick to the animated skin.

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_004.jpg

### Generating the Hair [25:36]
**Transcript:** So it's just good practice to do that.  And then we generate the actual hair.  We plug in everything, everything.  Well, the groomed data here.  And then let's actually turn this off.  So let's start with the mask.  So we apply the density mask.  Like usual.  We increase the density and check, go on guided hair.  And then what I like to do is to set up a thickness first.  Maybe something like this.  Yes, this looks nice.  But to increase the livability or realism, what I like to do is to add a point right here  and just decrease this one.  Just decrease the other root so that it gives you the illusion of the hair growing out of  the skin.  Just a tiny bit, not too much.  A little bit more.  Yes, something like that.  This will make the hair to be more believable and increase the density by much.  Like 500,000.  Yes.  We can always increase the hair density later.  We increase the thickness a little bit.  Two or one five right in the middle.  So now that we have everything ready, I want to talk about what makes a groom realistic.  So in my experience, there are three main components.  Number one, clumping.  Number two, noise.  Number three, stray hair.  So this three alone can transform an ugly groom into something that looks much better  than this and much realistic.  We can add more things on top, but that depends on the type of hair that we want to make.  Alright, so now let's jump into the hair gen node right here.  Before we summed up the hair clung node, I would like to use the color node.  So we can see what we're working with.  So in order to do that, we summon the node color.  It's plugging it in here.  And right now we can already see that we have everything colored as white.  I don't want to make the color type constant.  I want to make a ramp from attribute so that we can tweak the root and the tip of the  hair.  The color of the roots and the color of the tips of the hair.  But in order to do that, we need to summon another node called, what is it?  Resample.  It's plugging in here.  In a resample, we need to just drag everything to zero because we don't want this to affect  the hair.  We just want to check this color view attribute.  So with this attribute, we can drive the color.  Let's see.  So to check, there's a preset called black2oranz.  And then the attribute set to curve view.  And now we can see what's going on.  So let's maybe turn something like this.  Okay.  Yeah, I think that looks good.  Okay.  Now we can move on to the first thing.

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_005.jpg

### Hair Clumping [29:46]
**Transcript:** Number one, clumping.  Remember?  So let's summon the node called hair clump.  So we need to plug in everything.  This to the guides and then this can be the VDB.  And let's just connect this to the output hair.  And what we want is to use the guide that we've made because we have made a pretty cool  looking guide.  Right?  We want to use this as the main drive for where the clumps should be.  So let's connect this to custom clump curves.  So we want to click this.  You can already see what's going on.  Right.  We will make the clumping in layers.  So the first layer should be pretty big.  And right now it's really small clumps.  So wait, before that, I want to, I want the clumps to only affect the top of the hair.  Right.  So in blend, let's apply the mask.  Mask the clump mask.  So I have actually made a mask for where I want the clump to go.  And now we can tweak the clump size here.  Oh wait, it's been driven by the guide.  So yeah, it doesn't affect the size there.  So what we want to do is to play around with this linear blend, extrude, but what we want  to do, what we can do because we cannot really affect the clumping size.  So we can actually, but this doesn't look very good.  What I want to do instead is to use the tightness over here.  So we can just do a very low number because we want the clumps to be thick.  Now the thing we can do is to use this ramp.  Don't worry if it doesn't look very good right now because we're going to make it better  later.  So let's duplicate this node or we can just summon another node.  And we want this to be affected by the guides that we've created as well.  We want this to be affected only clump within existing clumps.  So the clumps that we've created appear will affect.  So basically we're making clumps within clumps.  So just like before, we apply the density, not the density clump mask.  So that everything on top is affected but everything at the bottom is not affected.  Let's just use this tightness to issue to play around and see what works, what doesn't.  What curling does is amplify, as the name suggests, curling applies and which part of  the hair is affected.  You can tweak everything like only affecting the tip, for example, without affecting the  roots.  The frequency is like the number of turbulence.  So if you increase this, there will be more turbulence.  If you decrease this, there will be less turbulence.  And this also affects with the part of the hair, either the roots or the tips will be affected  by these numbers the most.  But we're not going to do that now.  Okay, let's say it's a pretty good start.  Now what we want to do is to do clumping for this section of the hair.  So in order to do that, first we need to make a mask.  So instead of making another mask, what I like to do is to use this mask and invert this  procedure.  So if we change this one, it will affect the inverted mask.  So how do we do that?  Let's some of them call attribute wrangle node.  Okay.  So let's write something.  F add and let's add the name of the new mask.  For example, let me leave this in the make sense.  Then spacebar equals and let's define what this mask is made of, which is the clump mask  minus one because minus one means inverted.  So one spacebar minus spacebar F add and then put in the name of this mask clump mask and  put a semicolon.  That's it.  So this will be the new mask.  So detect if it has actually been created.  Okay.  Let's put everything.  Let's put the clump size as at a very low number.  Let's say four and then skin attribute, the new mask that we created.  See.  Four after.  So it doesn't affect the top.  It only affects the bottom part of the hair.  See.  So now we can do this.  Okay.  Okay.  So this is the clumping.

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_006.jpg

### Adding Noise [39:30]
**Transcript:** Number two is to do the noise.  When the node call just type in freeze and the node call guide process, hook it up.  This will break up the CG looking area.  Super smooth hair in the rendering.  So this part is very important.  Okay.  So now let's move on to the next one.

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_007.jpg

### Adding Stray Hairs [40:50]
**Transcript:** But for me to do that, let's make a mask because we want this noise to only affect a certain amount of hair.  So that we will do that is we make a guide mask node.  And then we can use everything in here.  But what I want to do is random mask.  So we can see which hair will be affected by whatever operation.  So we can change the name of the mask to random mask.  Something that makes sense, right?  And then we can tweak the amount of hair that will be affected.  Okay.  What we're going to do with this mask is to add some fly away or outlier hairs.  It will only affect the hair that we've defined in the guide mask on top.  So the black hair will not be affected.  The white hair is to be affected.  If you uncheck visualized mask, we can see how the hair will look like without having to see the mask.  Okay.  That looks very good.  So what we want to do is to set the length of the fly away because the fly away would probably not be long.  Right?  It's shorter than the average hair.  So first of all, I know a short number, a very small number.  And then in the masking part tab, you know, guide attribute.  And we apply the random mask.  And now we can adjust the length.  Okay.  So we can see that the set length process is actually either adding length or decreasing the length of the strands.  But when it adds the length of the strand, it doesn't really know where to go.  Because it doesn't have a guide to direct where the strands should go.  So we do encourage something like this.  Right?  Let's see.  Something like this.  It really doesn't know where to go.  So we need to change the mode from set to subtract so that it only decreases the length of the hair.  So let's put in some numbers.  Like 0.3.  So this way you can see flying away here that ends right here.  So this is the stray hair part.  So there's number one clamping.  We have this clamping.  And then we have the noise, which is the first, let's do, let's call it noise.  Because it affects this one affects a lot of hair.  Right?  And this will add that realization.  Okay, with this curve mask applied, we can only affect the middle part of the hair.  So it doesn't really mess with the tips of the clumps that we've made.  And it doesn't affect the rule.  But if the one we can increase a little bit.  So with this noise, what we want to achieve is to just break up these, you know, something that looks a little too CG, little too smooth.  So this way, almost all of the hair will be affected by the noise.  Just to break up the CG look, you know, by introducing some freeze, some randomness, there, some noise.  And the number three is we add the fly away.  Something like this.  Then we cut the length of the flyways.  And we can tweak some stuff.  We can refine the hair again.  Just to achieve the look that you want or the look that the reference gives you.

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_008.jpg

### Tip [51:00]
**Transcript:** Okay, so remember how I said that we will have layers of clumps, right?  Well, now we have the primary clumps which are the biggest ones.  And then we have the secondary clumps which I took directly from the guides that we've created.  Plug it in here and we get the secondary clumps, right? Very controlled.  And then we come to the tertiary clumps.  And it's found that I could not get the clumps to be as small as I wanted them to be.  No matter how I do it, these numbers, I just could not get the clumps to be as small as I wanted them to be.  So how do I resolve that?  Well, first of all, I took the guides directly and then I plugged it into Hair Generate node.  So what this does is it will generate some hair strands which we can use as guides for where we want the clumps to be.  Right, so very controlled. We can treat these numbers. I can actually show you right now.  Like if we treat these numbers to like 44,000, see we get these clumps.  So if we still don't like we can treat the scatter seed, right?  So this is a very controlled way of how we can resolve a problem where you could not get these numbers to be as low as you want them to be.  So now you can see the final result.  Right?  And that's it.

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_009.jpg

### Timelapse [52:35]
**Transcript:** So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  So  7  5

**Frame:** tutorials\frames\the-only-hair-grooming-tutorial-you-need-houdini-for-artists\frame_010.jpg


---

## Structured Notes

### Core Technique
End-to-end hair grooming in Houdini SOPs using `guidegroom`, `hairgenerate`, `hairclump`, and `guideprocess` to produce realistic short human hair with layered clumping, frizz noise, and stray flyaway hairs.

### Summary
An 85-minute beginner-friendly tutorial by June Chevalier covering the full pipeline for character hair grooming in Houdini. Starting from mesh import and unit-scale correction, the tutorial builds a density mask, VDB collision volume, sculpted guides, and generated hair strands, then layers in the three key realism drivers: layered clumping (primary, secondary, tertiary), guide-process noise to break up CG smoothness, and stray/flyaway hairs via a random guide mask. The result is a convincing short men's hairstyle, with the workflow explicitly compared to and positioned as less buggy than Maya XGen.

### Key Steps
1. **Mesh import & scale** — Add a `geometry` object → `file` SOP → `transform` SOP, set Uniform Scale to `0.01` to convert Maya centimeters to Houdini meters. Check the bounding box size in the viewport (target: ~0.3 m height for a head).
2. **Paint density mask** — Inside the mesh geometry network, add `attribpaint` SOP. Paint in the viewport (Ctrl = erase). Rename the painted attribute to `density_mask`.
3. **Mirror the mask** — Add `attribreorient` (Attribute Mirror) SOP. Set Mirroring Method to **Topology** (mesh is not spatially symmetric, but topology is). Double-click the middle-axis point, press Enter. Set Attribute Name to `density_mask`. Cap with a `null` named `out_mask`.
4. **Build VDB collision** — Still in the mesh network: add `polyfill` to seal any open holes → `vdbfrompolygons` (set voxel size to `0.001` for dense collision voxels) → `null` named `out_VDB`.
5. **Create guide groom object** — At the object level, add a `guidegroom` node. In its parameters, set Skin Attribute to `density_mask`. Set Scatter Seed to `0` (manual sculpt mode). Dive in, add a second nested `guidegroom` — this is the sculpting layer. Use the **Paint/Draw** tool in the viewport to draw individual guide strands; press **S** to select specific guides before sculpting.
6. **Add guide deform** — After sculpting, add a `guidedeform` SOP and connect the skin geometry. This binds guides to the skin for animated characters.
7. **Generate hair** — Add `hairgenerate` SOP. Connect the `out_mask` and `out_VDB` inputs. Enable Guided Hair; set Skin Attribute to `density_mask`. Set density to ~500,000. Add a thickness ramp: lower the root point value slightly to make hair appear to grow out of skin. Enable Use Clump Mask for the mask attribute.
8. **Color ramp for art-direction** — Before clumping, add `resample` SOP (sets `curveu` attribute; drag all values to 0 but check **Color View Attribute**) → `color` SOP set to **Ramp from Attribute**, attribute: `curveu`, preset: `black2oranz`. This makes root/tip color art-directable.
9. **Primary clumping (largest)** — Add `hairclump` SOP. Connect guides to the Custom Clump Curves input, VDB to the collision input. Apply `clump_mask` to the Blend field. Adjust Tightness ramp to low values for thick, loose primary clumps.
10. **Secondary clumping (medium, guide-driven)** — Duplicate or add a second `hairclump`. Connect within-existing-clumps mode. Apply `clump_mask` again. Tune Tightness for tighter secondary grouping. Enable the `curling` / frequency parameters to add directional turbulence.
11. **Invert mask for lower-section clumping** — Add `attribwrangle` (Point context) to create a new mask for the bottom section of hair:
    ```vex
    f@inv_clump_mask = 1.0 - f@clump_mask;
    ```
    Add a third `hairclump` using `inv_clump_mask` as the skin attribute and a low clump size (~4).
12. **Tertiary clumping workaround** — If clump size cannot go small enough, feed the guides into a secondary `hairgenerate` to create ultra-dense guide strands, then pipe those into a fourth `hairclump` as the custom curves input. Control scatter seed for art direction.
13. **Noise / frizz** — Add `guidemask` SOP (random mask mode); adjust amount. Then add `guideprocess` SOP, Operation: **Noise**, Type: **Sine Per Direction**, Frequency ~100. Apply the random mask in the Masking tab. This breaks up CG-smooth hair strands across almost all hairs.
14. **Stray / flyaway hairs** — Add another `guidemask` (random, low percentage). Add `guideprocess`, Operation: **Set Length**, Mode: **Subtract**, value ~0.3. Apply the random mask. This shortens only selected strands to create flyaway ends that break the silhouette.

### Houdini Nodes / VEX / Settings

| Node | Key Settings |
|------|-------------|
| `geometry` (object) | Container for the mesh and mask sub-networks |
| `file` SOP | Import mesh (.obj / .fbx / .abc) |
| `transform` SOP | Uniform Scale: `0.01` (Maya cm → Houdini m) |
| `attribpaint` SOP | Attribute Name: `density_mask`; Ctrl to erase |
| `attribreorient` SOP | Mirroring Method: Topology; Attribute: `density_mask` |
| `null` SOP | Named `out_mask`, `out_VDB` for output clarity |
| `polyfill` SOP | Seals open mesh boundaries before VDB conversion |
| `vdbfrompolygons` SOP | Voxel Size: `0.001`; fog volume for collision |
| `guidegroom` SOP (×2) | Outer: Skin Attribute = `density_mask`, Scatter Seed = 0; Inner: sculpt layer with Paint/Draw |
| `guidedeform` SOP | Bind guides to animated skin |
| `hairgenerate` SOP | Density: ~500,000; Guided Hair: on; thickness ramp with lower root value; Skin Attribute: `density_mask` |
| `resample` SOP | Drag all values to 0; check **Color View Attribute** → creates `curveu` |
| `color` SOP | Color Type: Ramp from Attribute; Attribute: `curveu`; preset: `black2oranz` |
| `hairclump` SOP (×3-4) | Layer 1: primary, thick, `clump_mask`; Layer 2: secondary, guide-driven; Layer 3: inverted mask for bottom section; tightness ramp controls density |
| `attribwrangle` SOP | Point context; creates inverted mask |
| `guidemask` SOP | Mode: Random; Amount: ~10-20% for noise, lower for stray |
| `guideprocess` SOP | Noise: Type = Sine Per Direction, Frequency ~100; Set Length: Mode = Subtract, value ~0.3 |

**VEX Snippet (Point Wrangle):**
```vex
// Invert clump_mask to target the lower/unmasked section of hair
f@inv_clump_mask = 1.0 - f@clump_mask;
```

### Difficulty
Intermediate — marketed as beginner-friendly, but assumes the user knows basic Houdini navigation, the SOP context, and node-wiring. No VEX knowledge required (one wrangle is copy-pasted verbally). A total Houdini newcomer would struggle without completing a basic Houdini introduction first.

### Houdini Version
Not specified. UI appearance and node availability (Guide Groom, Hair Generate, Hair Clump as standalone SOPs) is consistent with **H20 or H20.5**. Compatible with Houdini Apprentice (free).

### Tags
`sop`, `curves`, `attributes`, `procedural`, `vex`, `wrangler`, `modelling`, `beginner`, `intermediate`

---

## Related Tutorials
- [[how-to-make-a-short-film-in-houdini-magnus-møller-jesper-andkjær]] — Studio Tumblehead's production pipeline includes a `tube-to-hair` HDA and a full hair grooming pipeline for their short film *Turbulence* (H20/H20.5, KineFX/APEX, Karma XPU). Shares: `sop`, `curves`, `attributes`, `modelling`.
- [[model-a-procedural-flower-houdini-tutorial]] — Shares `sop`, `curves`, `procedural`, `attributes`; uses `resample` + `curveu` for curve-based geometry, directly analogous to how `curveu` is used to drive the hair color ramp here.
- [[houdini-tutorial-make-any-geometry-knitted]] — Shares `sop`, `curves`, `attributes`; sweep-based strand generation and `curveu`-driven attributes closely parallel the hair strand pipeline.
- [[урок-мягкая-ткань]] / [[tutorial-soft-weave]] — Shares `sop`, `curves`, `attributes`, `procedural`; demonstrates sine-driven curve deformation, relevant as an alternative way to add noise/frizz to strands without `guideprocess`.

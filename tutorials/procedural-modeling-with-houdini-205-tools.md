---
title: Procedural Modeling with Houdini 20.5 Tools
source: YouTube
url: https://www.youtube.com/watch?v=k7-5PaOccYc
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-modeling-with-houdini-205-tools/
frame_count: 0
frame_status: pending-selection
---

# Procedural Modeling with Houdini 20.5 Tools

**Source:** [YouTube](https://www.youtube.com/watch?v=k7-5PaOccYc)
**Author:** cgside
**Duration:** 29m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-modeling-with-houdini-205-tools <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript:** Kind: captions Language: en hello everyone and welcome back so in this video we'll be building the earpad model mostly procedurally and taking advantage of the new a 20.5 tools or modeling tools so yeah let's get started okay let's start by dropping a container and create lab simple shapes to create the airpad piece I'm going to change it to XY plan so we're facing the Z axis and we want a [Music] quads and we don't want equal sizes so let's copy the top and paste on the base so we can control this value 1.19 was the value I found and a height of 1.6 now we want to run the corners and I'm going to round it quite a bit something like this and five divisions so now let's fuse the points and drop a resample in this case1 will be fine let's change it to subdivision usion curves and now we can sweep it and let's change this to ribbon and on the sweep on the sweep I just want one column one Division and a weight of .45 okay now let's EXT this this and we will extrude it like 225 and let's bevel it and we will bevel only we will ignore the flat edges and go back level it quite a bit8 and three divisions so something like this now we want to create the UV so for that um let's see maybe near let me see the point over there can drop a range I'm just experimenting in here so let's select one of end points oops let's upset it and now let's see if that propagates and it does so we can just let's see we can just select it manually but maybe we can use a not so find PS Group find PS and it's group one so let's go P group group one and there you have it and let's group promote it to edges oh it's not this one it's this one and include only elements in on the boundary now we can drop a UV flatten and in your The Sims will be this one and we will also Rectify it and antique manual layout I believe that's [Music] it and now we can create an all and maybe UV uniti I'm not sure if I'm going to use this one but just in case this just stretches the shell to the other the available space so let's continue on the next part okay so now from The Sweep we can create an all and a group we want to to group the unshared edges so let's go in this case points will be different because this create boundary groups will create two different groups one for each Edge because we just want to fill this inside piece so let's group remote to edges and let's group promote group in this case zero two edges and poly field and we can just select this group one and single poon now let's use the new tool planner inflates to create the back parts so this will inflate it in the positive that direction in this case I want to be on the negative side and let's reverse the faces and change the iterations to weight so something like this and we can change the target length to 0.1 to have more subdivisions now we will quad remesh this and let's see if this is giving any good result maybe just 2,000 and that's good enough now let's give it a bit of blur attribute blur and we will blur the position just once just to get rid of those weird polygons let's sub divid it once is fine and polish F let's see how this will go let's try to qu quadrilateral grids let's smoo it quite a bit and this will be fine and now we can merge this or we'll merge it after let's just visual lines so this is our progress so far so now we will create the wrinkles on the ear piece so for that uh let's create another n and we will subdivide it by two let's just enable this this piece and we will create an attribute to just float because we want to mask the wrinkle deformer let's call it mask UV and this will be on the bounding box of the Zed a is so let me check oh I need to visualize it and we will create some contrast in here something like this will be fine so we don't want to affect these areas only this part and have some sort of f fallof we'll create the wrinkle deformer so for that let me check we create just a mountain in here let me disable the visualization and will go with the value of 03 element size of 31 and some sort of offset so this will be fine and let's create a wrinkle fer and connect the mesh we we want to deform and deformed mesh and we need to change quite a few things so so the first one is we want this to be clot want to increase the iterations and the the wrestling scale so something like this and we also want to change the ring scale to 75 and as you can see is this starting this this initial shape in here so we want to mask it by the mqv so we have those parts intact and let's just add a subdivision and be before that we actually want to Delta smooth some more so about the three and if we subdivide we have something like this which is fine but is not exactly what we're looking for we want this directional stretching and in order to create that we need to make some masks to create some tension around the Sims area so we will need to create those masks and let me just check we need to starting here let's create another n and we have the UV so let's split the UV seams and promote it I'm not sure this is needed but so let's now select I believe I was experimenting with something else and probably we don't need this why is not select okay so we will select this manually just to save some time and let's group this let's call it Sims group and we will convert line and connect pads so we have single Primitives and it's connected and let's see we can just create an all and call it out point and let's create a copet and this will be really really simple so let's create a cupet and we want sub import oops let go copy this contrl C and contrl V now rest right setup so to move it to the space of to the UV space and we just want to stamp the points and the scale of 067 was working for me and we also want to blur it so blur so the transition is not not so worse and quite a bit and now let's just invert this because we want to keep everything else but those areas those edges so this should be fine I'm just going to create an all and in here we want mono actually so this is fine let's create a new out mask see let's contrl C and copy and now in here in the second in the second input of this rink form we will create a mask so let's go with attribute from color attribute from map and we will use op Co and paste the pet and we don't want on the CD we want mask Sims mask Sims and FL out and not visualize we can just place the visualizer in here and I believe that's all let's just set a normal just in case and everything should be working now if we look at the wrinkle deforming and the subdivision and we will enable on the wrestling scale we will scale by attribute and we will scale by The Mask Sims so as you can see it's creating that stretching of the fabric so let's let's check something in here in this mask as you can see in here is slightly big so if you want to change that you can create a p scale attribute so in here let's create a connectivity and I believe it's on the prims let's visualize that can be on point and let's create an attribute just float and by default it will be on the P scale so let's change this constant value to one and the default value to 1.4 and just say at class is equal equal to zero so this one it will be slightly bigger as you can see does that make any difference well and let's maybe increase the subdivisions and maybe reduce some of that moding so now the only thing left to do is to create the the stitching and that should be a simple task so we just need to from here take a resample and let's go with a small value 005 and change it to subdivision curves so quite dense you know now we want to to align the stitches to the to the the formed mesh so we can use a I used some Vex but let's try to use just aray so let's change this Ray and change this to mean p and let's see what else do I need to transfer the normal so let's go import Point attribute from it and let's go with vertex it's not vertex I don't have a normal so I need to place a normal in here and can be on the points and now we can import it let's check and it's working fine maybe let's set trip with blur the Y and 100s and that is totally fine so we can Orient the stitches so what else now now in order to create stitches we will have to use some V coding but it will be really simple so let's start by creating an a triangle and we can save instead of measuring let's save the perimeter because we will need it and we have Prime intrinsic Prime intrinsic called measured perimeter measured measured parameter and we will do at Prime G num and I'm The Primitives so now we can promote it attribute promote and let's promote it from primitive to point perimeter and let's fuse so this is fine now we will create the pattern let's just make sure we don't Rec compute the normals because we will need them so let's create a Wrangle and first of all we need a value along the curves like a curve View and we can use the vertex curve parameter uh function to get the the intrinsic UVS so that will be just fine so vertex curve PM zero B at vertex number and if we assign this f qal u and check out this as you can see it's creating this some something like the Cur view attributes and now we can create a a variable for the frequency of the effect so float freak and CHF Channel float frequency and now we will just create the pattern so this will be float pattern and it will be equals to zene since we want an undulating effect and it will be on the U and we will multiply it by the frequency let's see if we assign this to the position so uh p+ equals and along the normals and a multiplier and also the pattern of course let's see what that gives us so if we increase now let's go with a frequency of 100 and a multiplier of [Music] 012 so we get this undulating effect but actually we don't want we don't want [Music] the this back and forth this ulating effect we want to to only have the the front part this uh displacing so we want to flatten the the part that goes back and for that we can just absolute this and we will also we will Al multiply the U by the perimeter so we have uh the same the same uh this the same pattern on both curves and this is what it's giving us and you can see is respecting the normals so this will be f getting nice on our shapes so can just create uh we can just attribute delete this and create a sweep and it will be a round tube and around 004 so really small and now let's see this let's merge and as you can see it's a bit we need to move them a bit in so what we can do in here can just pick and don't Rec compute and let's pick it everything something like this and if we merge everything take this and delete this one and there we have the earpads and we might want to use a normal here so we don't get that weird results so yeah guys this was a simple exercise but hopefully you if you're a beginner you start to have an idea about procedural modeling and now you can implement it in your own projects So yeah thank you for watching and I'll see you next time



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Houdini Nodes / VEX / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Houdini Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]

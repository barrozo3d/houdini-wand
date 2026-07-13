---
title: Export a full scene from Houdini to Unreal
source: YouTube
url: https://www.youtube.com/watch?v=BUJg3ILS1Aw
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/export-a-full-scene-from-houdini-to-unreal/
frame_count: 0
frame_status: pending-selection
---

# Export a full scene from Houdini to Unreal

**Source:** [YouTube](https://www.youtube.com/watch?v=BUJg3ILS1Aw)
**Author:** cgside
**Duration:** 35m54s | 8 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py export-a-full-scene-from-houdini-to-unreal <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video I'm gonna guide you through the
[0:06] process of exporting everything you see in here, all this scene into one
[0:12] reel. So that sounds like an easy task but actually is not that easy because
[0:23] my scene as you can see is a bit of a mess and I want to create instances so I
[0:34] don't use the full geometry because that will be would be overkill. This scene I
[0:42] believe it has around 10 million polygons so you can see it here because they
[0:49] are packed primitives but only this lamp has a lot of polygons. I can really
[0:58] show you because they are packed primitives. So let's see how we can solve
[1:05] this and one more note as you can see for example in this object here I am
[1:15] using a copy and not a copy to points I'm using a copy and transform so we
[1:22] need somehow to extract the points from this copy and that's another issue we
[1:28] will face. So let's see how we can do this. So we have the scene and let me show


### Example [1:40]
**Transcript (timestamped):**
[1:42] you an example I'm gonna I have a name attribute for each piece so for the
[1:47] pillars for the seeds for the walls everything as it's own name attribute so
[1:57] let's see we can check lamp holders and delete them selected so we have this
[2:06] how can we extract the points well these are packed primitives so we can
[2:13] basically use an add and delete geometry but keep points create a copy to
[2:21] points just to test if this was gonna work create an object merge and let's
[2:30] load the lamp holders so as you can see I have I have a null at the end of each
[2:44] object so I can easily transfer them to Unreal so I have the lamp holder let's
[2:53] make sure we place it in the center and let's copy the points so this is
[3:04] actually working but this setup would break in another scenarios let's say if
[3:13] I select something else like plaster walls and I go in here and select plaster
[3:26] walls and I copy two points as you can see is not the same only because I have
[3:36] done some transforms after after packing so that won't work and sometimes I am


### Extract Transform [3:45]
**Transcript (timestamped):**
[3:47] also unpacking the packed primitives for example in here I believe yes so in
[3:59] here I want to do some UVing on the on all the instances and not only one so I
[4:08] can have some variation and for that I need to unpack and after that I lose all
[4:15] the transforms even if I place a natural with triangle and try to extract
[4:28] the transform from the packed primitives so let's see you can see we have the
[4:39] transform but is not oriented properly so what's the solution well there are a
[4:47] few ways an easy way I found and it was suggested to me is to let's keep this one
[4:59] is to use a for loop and use a transform pieces I believe not transform pieces
[5:11] but rather extract transform so let's see how we can do that so let's say for each point
[5:22] and let's set it to primitives so we have each one and we can use this object
[5:43] mount and let's unpack unpack and use an extract transform
[6:13] and extract transform connected to here and we should have this and now if we copy
[6:25] the points we should have everything back as you can see so exactly the same result we
[6:38] could try to have we could try to do it with a single extract transform but from my
[6:55] tests it didn't work properly at least in my scene because I have some strange
[7:00] transformations on the packed primitives and unpacking and packing again so everything gets a bit
[7:09] of a mess so this is the way it's going to work and that's what I'm sticking to and now we need to
[7:19] find a way to automate all of this because right now we're only placing one single object one
[7:28] single name attribute so let's test with another one let's go for the lamps and in here let's say lamps
[7:46] and it should work the same way we need to make sure we pack the primitives
[7:58] we need to make sure we pack an instance otherwise it will be really slow so as you can see it's working
[8:08] properly and again if I go back to the Quaster walls and two Wester walls
[8:28] you can see in here on the points that we have an orient attribute that is working correctly
[8:36] as you can see so as always saying we need to find a way to automate all of this because right now we


### Automate [8:40]
**Transcript (timestamped):**
[8:47] only have one object being processed so what we can do is to run another loop so for each named
[9:01] primitive because as I was saying I have a name attribute for for each part of the scene so I have
[9:13] here the name if I run it and you can see if I set the single pass I have the alter I believe that's
[9:23] the name in English I'm not sure then I should have the ceiling and the other parts including the
[9:34] floor and the pillars and whatnot so we also need to to make sure we export only the necessary geometry
[9:48] for example in here we don't need to export all of this but just one and then we export the point
[9:54] the point clouds and we can instance in Unreal but for example for the floor we can just create one in
[10:05] in Unreal but let's export it and for that we won't need a point cloud so and this is not packed
[10:13] primitives so we need to find a way to filter the type of geometry the same goes for this part that I
[10:23] can't really instance I guess I could but I'm not going to and also this part in here that I could
[10:37] instance these objects but it's just not too much geometry so I'm going to export this as a single
[10:46] mesh with respective materials and whatnot so let's let's keep for now select for example this part in
[11:01] here and now we can we can place this loop so let's duplicate it and place this loop in here
[11:18] we also need this and we will need let's just color this in a different way
[11:31] and we also need the meta so let's call it meta and in here we will need to select the respective


### Meta [11:40]
**Transcript (timestamped):**
[11:46] geometry that is currently being processed so let's add a spare input and connect the meta
[11:55] and we will need to to use an expression in here so in this case we will use
[12:12] these open backticks and say details because it's a string attribute and we will grab the meta nodes
[12:23] and use the value attribute that will it will add the name so as you can see it's grabbing the correct
[12:34] objects and let's see now we have the proper point cloud let's just get rid of this
[12:52] let's see if it works for for another one so this one is the lamps but for example if we say it's zero
[13:12] it won't really work it's just unpacking first of all is not finding a single mesh and it's unpacking
[13:24] everything so this won't really work we need to find a way to filter this so the way we're going to do that
[13:35] is is by using a switch in here so let's create the switch and we will select the geometry coming
[13:56] and this part in here so in this case we will set it to zero and this should be working so when
[14:07] is not packed primitive we will have the outputs as the single mesh and when we have another let's say
[14:22] this one we will have the points not this one yes this one we will have the points yeah there you go
[14:41] so in in this switch we need to find a way to filter it so the way we're going to do that
[14:48] is by using an expression so if we go in here and we go to the geometry spreadsheet primitives
[15:05] as you can see we have the ceiling in here and let's go into intrinsic and find a packed
[15:14] intrinsic type name type name yeah as you can see we have an attribute that is storing the packed geometry
[15:30] name let's say so what we can do is to filter in here so we can use an expression let's open it
[15:41] and let's use string match and we want to find packed primitives let's just say packed wildcard
[16:00] and then we need a string attributes so we use frames and input zero
[16:10] and we need to find in here the name which is intrinsic type name
[16:24] so in intrinsic type name and this should be to go let's accept it
[16:42] and let's see if this works so for now is working is selecting the input one let's set it to zero
[16:50] so I think input zero one two three so I decided the windows will also be a separate mesh
[17:05] because we could easily instance them but let's keep that for now so we have the points points
[17:12] points and finally the seats as you can see so everything is working as expected so in the end we
[17:22] will have something like this to export so now let's also set up the unreal instance attribute
[17:37] so we can just come in here and place an arangle just for simplicity and let's say on points
[17:50] string at unreal instance let's the name and let's say is the detail
[17:59] minus one and value just the same attribute we used before and is going to error out we need to
[18:13] add a spare input and add the matter so this won't actually work in unreal
[18:25] but we I mean it will work but it won't grab the correct object in unreal because we need the
[18:35] reference path but as we don't have it right now we can just say it like this and then we can
[18:44] replace it in unreal at least we will have a slot to introduce the instance we want you will see
[18:51] how it is later so we have this and let's see the geometry spreadsheet
[19:04] and let's select this and let's see what we need on the point unreal instance
[19:17] as you can see we have
[19:24] add seats and what not we should have everything
[19:33] all right so we now now we need to export the single objects


### Single Objects [19:35]
**Transcript (timestamped):**
[19:40] so the seats the lamps and what not so for that what I'm going to do is to let's create an alinear
[19:53] oops and create a wrap fpx
[20:07] and in the wrap fpx we will need to set some things
[20:14] so I just created an output folder output file in here that is going to outcotidral fpx demo out
[20:23] dot fpx but we will need a more precise name so what we can do is to instead of out fpx we will
[20:39] add a detail attribute in here details in this case because it's a string
[20:45] and we're going to select the meta node so meta and we will need the value
[20:59] hatch roots as before and this should be good to go so as you can see this will give us seats dot fpx
[21:11] i don't have a single pass here
[21:19] so now let's say we will export the seats but we also need to export the single geometry or the
[21:29] geometry that is not packed so for that we will need a switch and we will say if n points
[21:44] if the number of points of the incoming geometry is equal to zero select the second input
[21:54] so in this case we can just grab from here and we can export the geometry
[22:06] so let's test this out we have the seats let's place for example the altar
[22:16] and if you select in here as you can see it's selecting the number one because we don't have
[22:24] geometry in here so this is correct now we need to automate the export we need to press this
[22:35] button automatically so for that we will use a python node and let's place it in here for example
[22:46] and we can just say
[22:53] ow.farm.parm
[23:02] and let's go for obj just select the paths of the node to export
[23:12] so geo1.dropfpx1 and slash execute and then we just need to execute press button
[23:32] and this should give us what we want so obj, geo,ropfpx, execute and press this button
[23:47] so that should be the trick and what else do we need?
[24:01] we need to let's see so we also need to group the points
[24:13] so we can separate them later so let's group
[24:22] so let's say points unreal and select points
[24:28] and this should be about it let me see we have already the unreal instance
[24:45] and yeah let's try to export this so let me select this one
[24:53] the enable is one and check single pass so let's export it
[25:02] so as you can see is rendering the geometry
[25:07] you shouldn't take too long so it's already done
[25:11] so I navigate it to the folder and let's see if the
[25:21] the geometry is in here
[25:26] and indeed we have the alter let's check the bless should be pretty fast
[25:35] and let's say the pillars which should be just one as you can see the file size is small
[25:46] apart from the the lamps this is a bit typoly but we have everything needed to
[25:56] export it to to using unreal so now we will need to export an hda with all of these points


### Export HDA [26:10]
**Transcript (timestamped):**
[26:14] so let's do that let's blast
[26:17] let's blast the points unreal
[26:26] the litmus selected so this point clouds each one containing an unreal instance attribute
[26:33] if I enable it here so as you can see we have the seats the pillars the lamps the lampholders
[26:43] and whatnot so that's disabled that's and now the way I'm doing this
[26:53] you need to export it in a way that you don't have you need to create an hda that doesn't have inputs
[27:01] so I can't really export all of this so what I'm going to do is to create a Rob geometry
[27:09] let's copy the patch from here so this and
[27:22] let's say if geo out fx0 and let's say points unreal
[27:35] we will export it as vgeo because it will contain all the point information
[27:48] so let's save it and now we can use a file and load those points
[28:07] so there we have it and you can see we still have the attributes
[28:13] and now what we can do and this is really important we need to
[28:22] middle click in here and select the absolute patch and paste it so we need actually absolute
[28:31] patch otherwise the this won't work but it's pretty simple you just middle click and copy
[28:41] so select it create a subnet and let's say points unreal demo
[28:52] let's save it and let's go to digital asset create new let's say
[29:09] we want in the ip file directory and we don't want the prefix so points unreal demo
[29:21] and let's create it let's apply and accept so now we have everything and we should be able to
[29:31] recreate the scene in unreal so before we go to unreal I forgot a very important step here in the
[29:41] raw path px we need to say z up converts to specified axis system and convert units so because
[29:53] in unreal is centimeters and here is in meters so that should fix it and if we run again the loop
[30:03] and we say reset cache pass it should export everything again and the points should be okay but just in case
[30:16] you can export them again and in here reload and save note type
[30:27] so here we are in unreal let's try to import everything so let's before we import let's create a


### Import in Unreal [30:30]
**Transcript (timestamped):**
[30:41] new level file new level empty level let's also create a directional light
[30:49] let's say something like this and let's import our points and let's drag them
[31:07] as you can see it's creating the point cloud and now let's import the geometry
[31:27] so geo out demo and let's import everything
[31:37] so in here make sure you don't tick convert scene and let's see
[31:50] we can leave everything default no translation no rotation and uniform scale set to one that's
[31:58] imported so everything is imported let's as you can see we have some materials that came with it
[32:17] but we don't need to worry so now we can go back to to Odini so in here we have the points
[32:28] if we go to the geometry spreadsheet and see the unreal instance so the first one will be
[32:39] the ceiling then lamp holders lamps ornaments and so on so let's go back to unreal
[32:47] and let's select the points let's go to the first component let's go to general and select
[33:04] ceiling then we have the lamp holders so let's select the second one and select lamp holders
[33:18] so it's in the correct place now let's select the lamps so the lamps
[33:34] then we have ornament windows so ornament windows
[33:41] then we have pillars and plaster wall and seats so pillars
[34:03] plaster walls and finally the seats then we can drag the single meshes so let's drag the
[34:23] altar the doors front the floor the glass and that's about it so let's drag into the scene and
[34:33] reset the transforms so let's see
[34:39] let's try the altar and reset so let's also make sure we reset this that was in the wrong place
[34:58] so let's first reset this and now let's drag the altar the doors front the glass and the floor
[35:16] and let's reset this so everything should be working so this is the the machine that I'm working on
[35:33] I already set up some materials and some lights and god rays maybe I will continue on the subject
[35:44] in the next videos let's see and I hope you have learned something new today thank you for watching



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

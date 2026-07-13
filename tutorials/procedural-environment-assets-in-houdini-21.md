---
title: Procedural environment assets in Houdini 21
source: YouTube
url: https://www.youtube.com/watch?v=SwtUCds8UCY
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-environment-assets-in-houdini-21/
frame_count: 0
frame_status: pending-selection
---

# Procedural environment assets in Houdini 21

**Source:** [YouTube](https://www.youtube.com/watch?v=SwtUCds8UCY)
**Author:** cgside
**Duration:** 21m8s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-environment-assets-in-houdini-21 <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hi everyone and welcome to this new procedural assets course in Odinit 21.
[0:05] In this one I will be guiding you step by step on generating this level environment, from
[0:10] manipulating packed primitives and transform attributes to custom valum simulations, this
[0:14] course is packed with valuable information.
[0:17] The first part is free e-around YouTube and you can access the rest on my Patreon
[0:21] shop there will be a link below.
[0:23] Hope you enjoy and see you there.
[0:26] So we will start by modeling the tunnel shape so let's drop a geo and I'm gonna start
[0:32] with a tube.
[0:34] I'm gonna place it along the Z axis, default size will be fine, I'm just gonna change
[0:41] the rows to 8 and the columns to 50.
[0:45] To have like this initial prick shape.
[0:49] So now we want to remove some polygons below the grids and also flatten the sides to
[0:58] have this tunnel like shape.
[1:00] So for that I'm gonna create a group.
[1:03] So with a group expression for example, I'm gonna select primitives, name it bottom.
[1:12] And the expression I'm gonna use is at p.y is less than some threshold.
[1:18] So at p.y is less than thresholds.
[1:25] And in this case is zero, I wanna set it to 0.165 to get this geometry.
[1:34] And then we will get yet another bottom group to remove those and keep this group in
[1:39] here intact so we can utilize it later.
[1:41] So this edge in here it will be the part where we start to flatten and then we select another
[1:46] group in the bottom and we blast those away.
[1:50] So let's create yet another group expression for the part that we're gonna blast.
[1:54] So I'm gonna name it bottom two and in this case I'm gonna set it to negative 0.3.
[1:59] 0.3.
[2:00] So we get this one.
[2:04] Now we can blast this last group.
[2:11] So let's blast the bottom two and we get this shape which is nice but I want to flatten
[2:16] this side.
[2:17] So before I flatten those sides I want to get the intersection between this group, so
[2:27] between these polygons and these ones in here.
[2:30] So there might be easier ways to do that but I'm gonna do it like this with a group from
[2:35] match with boundary.
[2:38] And I'm gonna name it boundary.
[2:43] I'm gonna select points and not the tree roots I just want to select based on the bottom
[2:48] group.
[2:49] So we get this.
[2:50] Now let's create yet another one and this time we're gonna do boundary two and I'm gonna
[2:57] do not bottom.
[2:59] So we get this.
[3:00] Now we can simply group combine and we will combine these to the boundary group so this
[3:08] is the output group, the name of the group and I'm gonna combine the boundary with intersection
[3:16] of the boundary two and we get these edges or these groups.
[3:22] Now we want as I told you we want to flatten these parts and the idea is to having these
[3:30] groups we can isolate one of the points and then get the position dot x and flatten the
[3:38] with that information.
[3:40] But we will also need to split those groups into two so we can get both positions.
[3:46] So for that I'm gonna use a wrangle and I'm gonna name it lead groups and this one will
[3:56] run on the boundary and make sure we set these to points and we can do the following to
[4:02] divide the groups.
[4:03] We can take the sign of the groups so vary me, int, sign and we're gonna do sign based
[4:12] on the position dot x position dot x and that will give us minus one and one so minus
[4:20] one on this side on the negative side and on the positive backside we will have positive
[4:26] one but we don't want minus one and one we want zero and one so for that I'm gonna
[4:32] do let's place between brackets and I'm gonna add this is just pure math so I'm gonna
[4:38] add 1.0 and multiply it by 0.5 this will rem up from minus one to one to zero to one and I also
[4:47] want to make the nints and just closing here so this will give us positive one and one.
[4:55] Positive it will give us zero and one sorry and now we can just set point group and I'm gonna name
[5:06] it boundary underscore and then add to this group so I to weigh with that string sign so it will
[5:15] be zero or one then we can just set based on the point number and just set it to one and now we
[5:23] should add two groups so let's see that points we have boundary zero on the left side and boundary
[5:30] one on the right so that's correct now we can simply flatten we have all the information we need
[5:38] so what we can do is create another angle flatten this and I'm gonna name it flatten and that's
[5:46] and I need to get the groups so I'm just gonna make sure I only do this on the bottom group which is
[5:57] this one we have in here so on this side that we want to flatten so primitives and I'm gonna
[6:04] first of all load the groups the point groups that we just saved so it's expand point group
[6:14] incoming geometry and the point group is boundary zero and we just want to get one point so can be
[6:21] the first one so they all share the same x position so that's fine and we can do the same for the
[6:31] bottom one this one is the right then we can get the position of this point this is just a point
[6:39] number that we have in here so we can get the position so that the pause left will be a point
[6:45] point function in coming geometry we want the position and in this case we want the point is just
[6:52] a left point and we do the same for the right so position right and in here right okay now that we
[7:04] have this we just need to flatten the geometry with this information so for that I'm gonna do v at p
[7:11] dot x it will be equal to let's say pause pause left dot x and that will so that will flatten
[7:23] everything to that side and if we do pause right dot x it will flatten to this side so we want to
[7:29] depreciate so for that I'm just gonna use the select function is just like an if so let's
[7:35] solve v at p dot x smaller than small smaller than zero we want to use the left position so left dot
[7:44] x otherwise we do pause right dot x and that will give us the result so now as you can see we have
[7:55] this sharp edge in here we could do an attribute blur but then if we pin the borders so let me show
[8:01] you if I do an attribute blur this will smooth out the result in here but we'll also pin the borders
[8:09] and give us this indentation in here which I don't want and if we don't pin it will smooth everything
[8:15] out so what we can do is do a simple pick on those groups so let's do a pick and we have some
[8:22] intrinsic normals in here so if we pick this little bit in will be and we still have
[8:28] those groups so boundary which encompasses the two groups so let's do a pick and I'm gonna do
[8:35] it on the boundary and a really small value so something like this will work fine so as you can see
[8:44] that is working and that's basically our initial geo so let's just call it in geo and we will continue
[8:57] the next part so now we will do some basic UVs on this so we can later use it for a rest position
[9:07] and also to sort the primes so for that I'm going to first of all do a UV flatten this should work
[9:17] fine and I don't want them in a layout I might change this to wangle based doesn't seem to make
[9:24] much difference but anyways and let me see something here you might want to worry on this the
[9:36] other way around so in that case we can do the following we can group remote one of the boundaries
[9:46] so to vertices and I want to promote the boundary one of this one and now we can come in here to
[9:54] wax this align vertex groups and do this one in here and we can change it to the well the false
[10:03] settings will be fine and this way we start cleaning this side and we go to the other one
[10:10] or if you want the other around you can do v-axis and this will re-entend this way in this case I want you
[10:18] so let's find now let's see since we have done some mulling operations our primitives are not
[10:25] longer sorted properly so as you can see we start in year at zero then in year we already
[10:32] 30 and so on so we need to somehow to sort these primitives but the idea is said and done
[10:39] because this will actually require them work so let's test the following let's do
[10:46] since we have these UVs we can easily sort them let's say so this is the y-axis and we have the
[10:54] x-axis in here so if we do a sort and first of all we can do a sort the primitive sort by attribute
[11:02] because our UVs are are in the vertex level so we don't have access to it so what we can do is do
[11:10] a natural triangle and create a sort well on the frames so let's do primitives let's name this
[11:18] sort well and let's do the following let's so this is on primitives so in order to grab the UVs we
[11:27] can do vector UV it will be equal to vertex zero UV and I add to v-t and now if we do the following f
[11:40] sort UV it will be equal to UV in this case dot x so dot x and this will be fine let's look at that
[11:51] attribute so sort UV and we get a value well in this case it's not from zero to one because we have
[12:01] a limited range because I've also used the relative point bounding box of the z-axis
[12:07] but even though we don't have specific values from zero to one we can still work with this
[12:14] so let's try instead to yeah let's keep it like that and see how that goes so if we now sort this
[12:22] by the sort UV and let's get rid of that visualization and the UVs and we do we do sort well now we
[12:32] do primitive visualization as you can see we we don't have a specific value that tells us
[12:39] tells us also that it should grow from on this side too so it's starting in years so
[12:46] and we want to start the zero one two three and so on and not in the middle because right now
[12:51] we only have a single axis so we need to incorporate somehow both axes in a sort well
[12:58] and the same would go with by do this by z and we can also revert so as you can see it won't work
[13:06] because this geometry is flat in here and it doesn't know where to to start sorting so we get zero
[13:14] one two and then 34 so that won't work so let's keep it's our attribute and let's work on that
[13:21] so first of all we will need how many rows and columns we have so right now we can trust
[13:27] these values only the rows because we haven't changed that but we can trust the columns so let's copy
[13:32] this rows and come in here and let's do the following we create a new and variable called rows
[13:42] and we will be channeling to jr rows and we can paste it can create and paste here the value so
[13:52] eight and if we count one two three four five six seven so we actually need to subtract one
[14:01] okay now for the columns we can easily guess that so we can do int calls will be and primitives
[14:12] obtain coming geometry divided by the rows so now we know how many columns we have
[14:19] and I say columns I mean this value that calls around each section so that's fine now we also need a
[14:27] proper z z sorting x sorting so sort value along the the x so I'm not gonna use these UVs
[14:39] for the x I'm gonna instead do a relative point counting box so float this case for the z
[14:48] so float z will be a relative point bounding box zero v at p and we can say dot that and what this
[14:58] will give us is a value from zero to one along the z so let's see as you can see we have zero one
[15:04] and so on until we reach one all right now in order to combine this the sort well we can do
[15:13] the following we can take first of all as I told you before we need to combine two values one
[15:19] along the z and one along the uv's so we can actually use just the exposition we need to do
[15:26] based on uv's so since we have uv's flowing in this direction we can use that value so for that
[15:33] I'm gonna use uv dot y so as you can see we have this uv's along the y so we can use that
[15:42] and I know that goes from zero to one or almost but should give us a good result so we can just do
[15:52] 1.0 minus uv dot y which will reverse the result then if we check that so sort uv
[16:04] and this will give us a value starting in here and let's do marker and it will start at zero until
[16:13] almost one in here and we can do the following we can round this to one integer and this will just
[16:22] give us zero and one but then we can multiply by the amount of calls so if we do let's open yet
[16:30] another bracket in here and multiply these by the calls and this will give us from zero to 34 so
[16:39] 35 columns that's what we have so we have the correct values and I will just need to combine the
[16:45] z axis so for that I'm gonna do the following I'm gonna add to this again round to integer the
[16:53] 1.0 minus z since I want to start on this side and we can just multiply these by the calls
[17:05] and as you can see as you can see this will be zero at first and then so I'm not doing this
[17:18] properly so 1.2 minus z so this is not even giving us the correct result because we also need to
[17:28] multiply these by the calls and let's do times the rows or we have forgot some brackets in here so
[17:41] we want this ring to include also this part and this one it will be between brackets and also
[17:49] this one so we get this result and this should give us the correct result I'm guessing so 1718
[17:58] to 51 then we have 53 that's fine and it's a growing value along the z and also along the uv is
[18:09] dot y so I guess we're good okay so let's get rid of this visualization and now if we do the sorting
[18:20] so if we sort the primitives by the sort uv let me see yeah this is correct no
[18:30] so is the other way around so let me just check something
[18:36] sorry we don't want to reverse of course sorry about that so now we have from 0 to 34 then we have
[18:44] 35 to 69 and then 70 so this seems correct to me and now we can continue so a bit of a work but now
[18:54] we have the primitive sorted now the reason I sorted this frames is because I need to create a row
[19:03] when column ID so let's do that now so let's do it wrangle and I'm gonna name it
[19:11] row and all ID because we will need it for the transformations later so let's do the following
[19:21] let's copy from here easy these two variables so it will be the same and I'm just gonna copy
[19:30] here the rows and paste it in here based relative reference okay now if we do
[19:41] I that's row ID will be equal to I at frame 9 and every other calls or module calls and let's see
[19:51] how that looks so row ID and make sure we do these on the primitives and as you can see this starts
[19:58] from 0 and goes around doing our row ID and now we can do the same a similar setup or the call ID
[20:08] call ID so we just need to do 5v1 and this should give us this result so if we check these values
[20:18] so if I don't mark it as you can see we have from 0 to 1 and so on and if I didn't sort in this
[20:25] case it won't make a difference along the Z but if I look at the row ID so marker
[20:32] as you can see we have a growing value if I have un-sorted as you can see we have these
[20:37] different values so it's not correct it will still give us a perception of a correct value as you
[20:47] can see this works but I prefer to have these properly sorted so in the next step we will do some
[20:58] random transformations to the geometry



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

---
title: Chocolate break rig and Liquid Stretch in Houdini Free Lesson
source: YouTube
url: https://www.youtube.com/watch?v=f5vt8n8CB-U
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/chocolate-break-rig-and-liquid-stretch-in-houdini-free-lesson/
frame_count: 0
frame_status: pending-selection
---

# Chocolate break rig and Liquid Stretch in Houdini Free Lesson

**Source:** [YouTube](https://www.youtube.com/watch?v=f5vt8n8CB-U)
**Author:** cgside
**Duration:** 23m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py chocolate-break-rig-and-liquid-stretch-in-houdini-free-lesson <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome. So in this month we will create this entire effect from scratch,
[0:05] from the preparation of the model to the animation of the pieces and finally do a simulation to create
[0:14] this liquid scratch effect. So I know I've covered before this kind of chocolate break but I think
[0:21] this one is the best one and I hope to see one patron. So we will start from this initial scene
[0:30] which is basically just importing the geometry that is the chocolate bar, deleting some attributes
[0:36] and quad remaching it. I'm gonna lock this as you can see I have this lock so you don't have to
[0:41] to have the zagle sidequad remachure. So now we will create the interior surface because we want to
[0:49] disbarrow to have some thickness. So for that I'm gonna branch in here and create a shrink wrap
[0:57] to create the interior surface but we don't want to use this geometry so I'm going to first of all
[1:03] pick it a little bit in by this much and then we're just going to nap it through this unified mesh.
[1:12] So let's just call it minpass and we'll just do vhatp, we'll be equal to the minimum position
[1:19] of the input one using the current position.
[1:25] So this is the result we get.
[1:30] Let me just test and hear if I remove this in line point it will remove this issue that we
[1:34] add. Now we need to smooth this because this will be to it doesn't matter that much because it
[1:40] will be inside but just for my own sanity I'm gonna smooth this and I'm gonna use this following
[1:49] value so 100 for strength and quality to 1. This way we get this smooth result. Then I'm going to
[1:57] reverse this and let's just make sure we compute the normals again and then I think I created some
[2:07] groups in here but I don't think we will use them so let's just margin here and if we clip this now
[2:16] as you can see we will have the correct geometry with some thickness.
[2:22] All right now we will delete some attributes and create the rest of the attributes so let's just
[2:27] create an attribute delete and we will just keep so let's see we got a bunch of them from the
[2:33] quadrimashers so I'm just gonna keep position in normal and then we're gonna create just the rest
[2:39] so we can refer back later. Now I want to clip in here in the middle to create some pieces that are
[2:46] going to be read later and for that I'm gonna use the clip nodes instead of the boolean fracture
[2:54] because it works best for what I'm trying to get so I'm just gonna create the feedback loop and
[3:00] do two or three clips so as you can see we can create a near clip and clip it will clip it
[3:06] not around the way but around that axis and we will do well primitives but we will restart this line
[3:12] with some noise. So let's do that let's remove this clip connect this in here let me just
[3:18] get some color and I know why we'll need the metanodes and the first thing I'm gonna do is create
[3:25] an attribute noise vector so this starts the shape so let's name it let's use the rest that we
[3:33] created because I don't want to do it in position and I'm gonna change this to be around 0.06
[3:42] oops whatever 0.06 are not too much I'm gonna change the element size to 0.39
[3:51] and the offset to 0.14.79 so just some initial values you can try other ones I'm just gonna follow
[3:59] what I did and then we're going to clip so let's just use a clip and we're gonna clip around
[4:09] the Z like I told you but we're gonna do primitives and use rest instead so let's disable that noise
[4:17] and as you can see this is our clip but now I want to create some other cuts that's why we did it in
[4:22] the loop so for that I'm going to connect in here to this noise we need another pattern to create
[4:30] another cut so let's just make sure in here we set this to the tree for now I think that's
[4:36] how much I'm going to use and I'm gonna you take advantage of these repeat these metadata nodes
[4:43] to create some variations so I'm gonna add a sparing root and connect these meta nodes and I'm
[4:50] gonna use a vector expression and in this case I'm just gonna add to the current offset and random value
[4:57] that will be based on the iteration so minus one which is a sparing root we want to get the iteration
[5:05] which will be just 0.12 since we have three iterations and then we need to grab the component in
[5:10] this case as a float so it's always 0 then we can multiply it by a big value just to have an
[5:15] half offset and if we have a look now we should have different patterns as you can see but now I
[5:22] also want to play with this clip to offset it a bit so by using the distance randomly so for that
[5:29] I'm going to first of all I'm gonna change this tool turning flow and zero centroid is correct
[5:37] so and I might want to change it to vibrate to rain and I think that's all for now and now we're
[5:47] going to connect again to this clip to randomize the distance so let's set this sparing root
[5:54] and for the clip we're going to the distance and we're gonna fit all one since it's a value between
[6:00] zero and one since we're going to feed in your a float random value which is between always between
[6:08] zero and one so we're gonna grab again the iteration the component is zero and we're gonna feed it
[6:16] between minus 0.2 and 0.2 so just an offset and we get this sort of result as you can see
[6:23] and now we want to build the polygons and we want to grab the clip edges
[6:33] they're both to below and the field so we're gonna create some groups
[6:39] I think that's all so let's have a look in here in the exploded view and we get this sort of result
[6:46] so I think this is the correct so let me have a look
[6:55] yeah that's basically what I got but now we want to remesh these inside parts these field
[7:01] polygons because right now they are not working so well so for that that's why we saved the field
[7:08] so I'm gonna create a remesh in here and I'm just going to remesh the field polygons
[7:17] and I'm gonna give it quite a few iterations because I'm gonna quadremesh this and we need a
[7:22] small output and a target size of point 0.1 so it might be a bit too much but worked well for me
[7:29] so let's just run this loop and now I have a look so we get a nice result for the interior part
[7:38] now the thing is I'm going to in my original file I quadremesh this because I have plans for
[7:45] shading this and creating a V so it will be easier with that quadmesh but you don't need to do that
[7:52] if you don't have quadremesh the exercise one so you can totally skip that part so let's leave
[7:57] this exploded view in here and what I'm going to do now is another remesh because I want to feed
[8:06] this to the exercise quadremesh and it's always an idea to remesh everything or to work
[8:13] white to work white I remesh on everything so it's easier for the quadremesh so I'm just gonna
[8:20] select everything that is not filled I'm gonna give it some iterations let's say 4 to smooth out
[8:25] the bit to even out the polygons and I'm gonna choose a target size of this value so this might
[8:33] take a second as you can see we have this sort of result so that's working well and now I'm
[8:39] gonna create a connectivity because later I want to iterate over this sometimes like primitive
[8:48] and the rest is fine so let's have a look at that class if we have a look we have this so we have
[8:55] 0 1 in the middle and the other ones but we don't need to worry about it now now I just want to
[9:00] group these small pieces so a safe way to do that is to measure the area per piece and now we can do
[9:10] group expression and we're just gonna select based on the area so let's do let's name it small
[9:18] pieces and it will be a primitive group and we just need to do area is less or equal to some
[9:26] threshold to some value and I'm just gonna increase this and a value of 0.65 will select the small
[9:35] pieces that this is just a group we might need later now I want to do the quadremesh but
[9:43] if we do it all at once it won't work that well so I'm gonna do it in a loop which is also a
[9:48] good time to a good opportunity to have a look on how we can use exercise quadremesh in a loop
[9:54] because it doesn't always work by default so and but before we feed the quadremesh I'm gonna just
[10:03] create some colors in here attribute the just color which is too red and the reason I'm creating
[10:11] these colors is because when we do the quadremesh we can use vertex colors to define the polygon count
[10:19] and that's what I'm going to do so in this case I want less polygons since I'm gonna have a
[10:25] fixed amount of polygons in here I want some colors to differentiate between the small pieces and
[10:30] the large pieces so I'm gonna create in here a value on the small pieces so small pieces I'm gonna
[10:38] create a value of 0.5 in red and one and one in here so we have enough polygons we could just
[10:49] have set it to zero but that might be that might be very few polygons so I'm gonna increase
[10:56] a bit red the red and then in the default color I'm gonna set it which is where we want less
[11:02] polygons we want a solid little bit of red something like this what so in the red parts we want more
[11:10] polygons and in here we want less polygons a red value value value will give you more polygons
[11:15] and this value in here will give you less but it's I'm gonna just increase a bit red to have more
[11:20] polygons on the small pieces and not increase so much the red on the big pieces but we get some
[11:29] balance so this needs to be CD and a point color and then I'm just gonna group delete some of the
[11:34] pieces because I'm gonna feed primitive groups to define the boundaries and for that we just want
[11:41] so let me have a look in here now we just want to feed these groups from the field polygons so let's
[11:49] have a look if we add them so we have them but we also have other groups that might confuse
[11:53] quadramasher so I'm just gonna delete those oh in here I just want to keep let's see
[12:04] I just want to keep the field ones so let's delete let's delete everything but the field
[12:14] and if we have a loop now we just have that go in there okay then now we can finally do the
[12:22] the quadramasher so for that I'm going to use this quadramasher in here and the first thing I'm
[12:29] gonna do we change it to 7000 to 5000 and use vertex colors and use primitive groups and then I'm
[12:39] gonna create a four connected piece I believe so yeah or each name primitive okay and let's
[12:51] let's connect in here the class and that is working but if we feed this now this
[13:00] won't really work it will ever route because this saves the geometry into a file and we need to
[13:07] to change change the name of the okay that changed because that didn't work before because we
[13:13] needed to create in here another version of the file but for some reason it's working so I'm
[13:23] surprised that that worked so let me just make sure this is working correctly so yeah I guess we
[13:30] don't need to create the the metadata node to feed the iteration value in here to create a new name
[13:36] so that might have changed between versions I'm not sure so we can actually have a login here
[13:43] I'm not sure but yes somehow it's working without the iteration so that's fine now we want to
[13:52] as you can see now we have a proper mesh and now I want to cache this because I don't want to
[13:57] compute it every time so I'm just gonna just gonna create a file cache and not time-dependent and I'm
[14:05] gonna load the shortcut bar cache remesh and load and this must be explicit so I just
[14:20] loaded the file from disk and it's identical as you can see so nothing much changes so it's
[14:25] pretty much the same so now I'm gonna select in here the the r-deges so let me just create an
[14:35] exploded view make sure we set it to point and let's see if this works so group
[14:41] and I'm gonna name it r-group and set it to edges and mean a jungle and let's set this to 28
[14:55] let's see if it works and I guess it's working perfectly so we can remove this one
[15:02] and now I want a group the inside group so I'm gonna create a group again
[15:16] and the one explode a view
[15:22] and our let's tweak it before and I'm gonna select in here keep by normals
[15:32] and I'm gonna do it along the z axis and I'm gonna name it inside group
[15:42] and this will be keep by normals and change this to 60 so we select these inside primitives and
[15:52] make sure we include both directions as you can see and now we just need to get rid of the remaining
[15:59] parts which will be more or less simple so we just need to do a group expression
[16:08] and let's name it again inside group not our group so inside group and do the absolute
[16:15] value of the position dot z so we get both positive and negative and that if it's less than
[16:22] some threshold and if we do that we start to select just this part I'm gonna set it to 0.5 just
[16:29] to be saved and just to intersect and now if we have a look we should have those inside parts
[16:38] selected so it's just a sheep way to select the inside part all right next we will create
[16:46] connectivity on this so let's create connectivity and I'm going to do again primitive and quest
[16:58] so let's envelope you have the same values as before because we didn't have any here
[17:06] and then I'm gonna go up again I'm gonna select in here this
[17:11] and paste it because I want to group again the small pieces so there we have it
[17:20] and then let's just have a look in here as you can see some of these parts are not
[17:27] connecting because they were matched separately because they were separated parts and when they
[17:32] get quadrameshed it doesn't line up so we will try to pick a little bit of that
[17:38] so after this group expression I'm gonna set up a normal in here
[17:46] and I'm gonna change these two points but I don't want these so I'm gonna save it as
[17:52] underscore normal just so I can refer it inside the point wrangle and that's fine and I'll just
[17:58] gonna create an attribute wrangle and name it bits edges and let's connect in here and we will
[18:06] take advantage of the intersect function to find basically where we will only work on this
[18:15] part in here and just snap them together let's say so for that we're gonna use an intersect
[18:21] function so for that we need some variables to write to so I pause and I'll give it up then I
[18:27] want to grab the normal so vector underscore n it will be yet underscore n and then let's
[18:43] to make sure we set these two primitives and select inside group and now I want
[18:50] if we do this explode review I want these normals the intersect direction to be based on
[18:57] those normals that we saved so from here should point to the right and from here should point
[19:02] to the left so for that I'm gonna manipulate these normals to be based on the sign of the
[19:10] Z component of the normal so maybe I can show you that it will be that underscore n it will be
[19:18] underscore n
[19:24] and let's have a look and make sure we set these two vector marker and vector and lower this
[19:35] time but as you can see these normals are all messed up so we don't want to use this we want
[19:41] to manipulate it so let's create another variable called vector n it will be just a straight
[19:48] direction on the z and if we do that we will just have normals pointing in the z axis to the z
[19:57] axis so we don't want that so let's just multiply it by the sign of the underscore n dot z
[20:04] now we get the correct direction you might have questioned why didn't I use the
[20:09] prim normal for example so I could have sampled the prim normal but then again this is in running
[20:14] on a primitive group in a point wrangle so this point in here will get the normals from this
[20:19] prim or some interpolation and it wouldn't work out that well and those at the top are the most
[20:23] important points so that's why I'm doing it this way and it's impossible as you can see
[20:28] so now let's do the intersection so int i-cream is just the intersect function and we want
[20:37] to look for the current input we want to limit it to the inside group I don't want to
[20:44] snap to other polyons and we will just do v at p things they are on top of each other I want
[20:50] to lost something a little bit so I'm gonna multiply n by some small value value and then we will
[20:56] the direction will be n and we will multiply it by a small value so we present both to other
[21:02] directions too far let's say and I'm just gonna say by cos and now you'll be w okay that's fine
[21:09] and now just create a mask just side-cream not too close to minus one so you did find the
[21:16] prim so let's have a look at that mask as you can see we have a mask for those areas so it's
[21:22] finding the the frame so I don't think we need this we just need to do if i-cream is not
[21:30] too close to minus one so we found an intersection we can just assign i-pause to the position
[21:39] so let's have a look as you can see it's small but it should fix in some areas some problematic parts
[21:49] as you can see here it's not perfect but it fixes some issues in some parts it's just trying to
[21:58] snap to some of those intersections so okay now we will just create a normal as you can see it
[22:11] isn't so noticeable when we don't have to i-frame but we have some issues on the norma so what I'm
[22:18] gonna do is to create a normal linear and set it to 45 and that should fit most of the issues
[22:25] and we will not have this open so we will not have this closed for too long it's just on the first
[22:31] frame so let's find and yeah now we just want to create some fracturing on those small pieces
[22:40] and then we will move on to the reading and animation so see you in the next part
[22:45] okay guys before we continue i noticed i made a mistake in here as you can see it's not closing the
[22:50] edges so what we need to do is just to negate in here the sign because i want the other direction
[22:55] around and as you can see now it's work it works much better so as you can see in here it's
[23:04] closing the gaps might not even be visible in the video but you can have a look at the file and see
[23:10] for yourself or try on your own so we will continue now i'm gonna split these by the small pieces



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

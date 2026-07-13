---
title: Shoe Laces in Houdini | Vex and Vellum
source: YouTube
url: https://www.youtube.com/watch?v=rlrWEjoO8jQ
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/shoe-laces-in-houdini-vex-and-vellum/
frame_count: 0
frame_status: pending-selection
---

# Shoe Laces in Houdini | Vex and Vellum

**Source:** [YouTube](https://www.youtube.com/watch?v=rlrWEjoO8jQ)
**Author:** cgside
**Duration:** 19m32s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py shoe-laces-in-houdini-vex-and-vellum <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript:** Kind: captions Language: en hello everyone and welcome back so in this video I wanted to show you how I created these shoe laces in know basically by over complicating I should have just drawn the the pattern and call it done but I try to do it procedural so if you want to stick with me and learn possibly something new feel free to do it so let's start by I'm I'm merging here the the base of the shoe and since I will have let's just see where I will have the shoe going through the shoelaces going through so these four HS we need to create points for them and also on these rings so four seven seven on each sze seven points on each side so I'm starting with this basic go I don't even have the the alss and then I have an HDA called Place points on gu and I will make sure to include in the file for patreon and that just enables you to paint to place a point on the go as you can see and you can clear and delete less some random points so so that's it it's very basic just use some python States and an add node So I placed those points I placed the points on the where the all should go and then in here I have the Rings creating a connectivity and extracting the centroid based on those pieces of the class attribute and also grouping the this points maybe I can use it later so now that I have all these points seven points and I just mirror it since I want to create this this laces pattern so I have this points then I'm sorting the points by X so this is actually X and this is x in this direction and as you can see I have 0 1 2 3 and this will be easier for us to create the pattern and for the pattern I'm creating a Wrangle and this attribute called ads which will just do the same as a group by range selecting two out of four so two out of four and and starting at one so I'm just setting the point number you can actually use the group range and group remote and output as integer attribute and use the add by attribute with that name but in this case I just created in Vex and used the the add nodes so as you can see this is creating this pattern and you can see by the group range so these points will have value one and these ones will have value zero as I can show you in here so one 0 1 zero you got the idea right so then I'm poly cutting so I have single Primitives and sorting The Primitives by X as you can see and also sorting the points by X then I'm selecting the points I want to move up and I can show you if I create an exploded view so as you can see I'm I'm selecting the first point of each curve in this case by using connectivity so I will actually move those points but be and in this stream I'm just adding the the first and last uh Primitives by using 0 to one and end points minus 2 and minus one so from these points I'm just adding two Primitives at the ends and then I merge everything so in here I'm grouping the near points I'm not grouping I'm creating an attribute based on the near points so later I can do this as you can see So based on an near point they will have the same number so they will get added together so I can actually show you if I disable this and enable Point ID so these two points will have zero I can actually place an exploded view in here so as you can see these two two points will have the number zero then one 6 7 and I will when I move them up which I will do now based on this group by range I move them up to create this sort of pattern then also transforming the first first primitive and then I can just add by attribute with that I ID uh attribute we created so let me just clean a bit this and now I'm going to sort by X The Primitives and sort the points by the Primitive index and creating a polyad to unite the curves deleting a attributes and groups and doing a resample as you can see and I'm do I'm doing interpolated Curves in this case and a small length small distance then I'm fusing since the resample always leave leaves the curve open and on this side I am importing the the Rings creating a connectivity and extracting the centroid and transforming them a bit in so I can in this case I'm moving those points of the those centroids to the to the curves using the mean POs to the the main curve and then I'm creating uh an attribute or a group based on the near points so as you can see npt not npt let me output this group so NP group and I go in the bindings and output so I'm just creating the a group for the B based on this points and on the near points as you can see so what I can do with that is because this I need to explain you first this since uh this this sh light should come in here and go up again to the top I need to move the this part up so this is where I'm telling you this is a bit over complicating things so I select those points based on the near points and then in here I'm creating an attribute with that specific group using the surface distance attributes so I can show you how that looks and that doesn't look much because I need to remap it so and I change the attribute name so I'm just creating an attribute a mask based on this this uh this group that we created with the near points this will just create a mask by based on those points and then I can move it up on the positive y based on the attributes and I can change the amount we can ignore this polyframe and then in here here I'm creating a group and this could be this could be uh maybe there's a better way of doing this but basic basically I'm taking this near Point group let me actually I'm not I'm not sure why it's showing the the points but basically I'm taking this near Point Group which is in here and I'm I'm offsetting them on the Z axis in this case or in a positive on a negative way in this direction and on a positive way on the uh positive x z i mean so I want to grab all these points at the bottom so I can manipulate them and for that I am using some Vex so just selecting the points on the near Point group and it's rating over them grabbing the position and adding uh an offset based on the on the position in that so positive on one side and negative on one and the other then just setting the point group so then I can do this soft transform so as you can see if I show you the geometry I'm just trying to move these points down so they don't intersect with the with the Rings as you can see in here so just moving them down so I'm just selecting those offset groups and doing some transforms so as you can see this gets all over the place but you know just for learning purpose let's say so now I if I fit this to a vum simulation this will not work properly because because we have intersecting points in here so for that I'm creating an intersection analysis this will create the points then I can group The I can create an attribute based on the new points of the first input of the second input I mean which is the curves and then promote those Point groups to a detail attribute in this case an array and I can group these nearest points so the intersecting points based on the on the near point we created in here so then I can just soft transform those points so offset them and do another resample fuse and finally we can attribute delete and move into vum so in order to make them fit properly I need to transform them down so I'm doing a transform and animating the the position animating the scale I mean so I'm just moving uh scaling them down and this will be our input then creating a Vellum string and the Vellum Collider Alm string constraints and it's important in here to set the proper thickness otherwise you will get all sort of problems if you have depending on the number of points you have if they are overlapping each other it will create problems so then doing the vum seam in this case I did a pop drag and a vum rest BR rest blend to that anim laces so to this animation we're just rest blending it and then if we run the [Music] Sim we will get the sh laces tight and we also have that thickness which will create this this offset from The Cider if I can focus on this so it will create this offset from the collider which will help us to create the geometry so having that simulation we can time shift it delete the attributes and resemble to have a better geometry so from this to this and fuse it attribute lead and now I want to create the the geometry so for that I'm using an oriental long curve and creating the app attributes to use uh to use in um in the sweep noes as you can see let me disable these and create the sweep so as you can see if I don't have a an up attribute this will get all messed up so for that I'm doing an oriental on curve and make it face that specific Direction that type attributes I'm also doing an attribute blur on on by time so starting small starting at frame three from 0 to 20 so as you can see otherwise I will get some issues around these corners but it's important that you have the first frame without the attribute blurs so it fits the alls and the the Collision geometry so that's our geometry now we just need to feed it this is our rest state which will start small as you can see I I forgot to mention I animated the B scale in here from .1 to 1.9 and also selecting some Sims for the ovs but that is not that important so I'm creating a Vellum clot and you can see my settings just everything super stiff then a Vellum solver again with the same thing just a Vellum rest blend to that animation we had before and this will work better than doing some sort of rest scale animation and the same goes for the the curve that we have appear here I tried with wrestling scale and I get I got all sorts of problems but again I'm not a pro in this so don't quote me on that and then we have a volum uh solver two substeps no no gravity and let's simulate it this might get a bit slow while I'm recording but this will just solve well because in the first frame we don't we have no intersections and this will create some nice results and this will go until frame [Music] 24 and we can actually stop this and look at the time shift which is at frame 30 so as you can see a lot of work but I guess it pay pays out in the end we have these nice results but maybe it's easier to do it manually and or in another smarter way that I'm not seeing in here I'm just creating the The Sims the promoting The Sims group that I created before and you'll be flatten in this case rectifying the group so I get this sort of UVS then attribute deleting and we should have this again guys maybe not the the best way of doing this but in the end it worked out and I'm happy with the result so if you guys have any questions please feel free to post them in the comments below and you can also grab the file on my patreon I will be uploading it to there you can check how I've done the show from a single box as you can see and other than that I guess that's about it thank you and I'll see you next time



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

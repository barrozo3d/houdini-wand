---
title: module ii   week 03   06   breaking welds and constraints v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=dfD5FUdMCTc
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p/
frame_count: 4
---

# module ii   week 03   06   breaking welds and constraints v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=dfD5FUdMCTc)
**Author:** The VFX School Archive
**Duration:** 11m46s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Right so we're pretty much ready to run our cache here. I just want to organize this a bit better before I forget. So I know it's just, we should just put the names here. And let me see the stitch is, what's that doing? The collar. Okay. And then also in this weld, which is here, I just want to turn on braking set that to one. Okay so because I want to change that as we progress through the simulation. Right so the longer into the simulation, the weaker I want that to become. So I can't animate it here so I'm going to do that inside the solver. Right. And we're also going to be animating if you remember the left boot. Right so we don't need to turn on braking here. But within the solver we can basically delete those constraints at certain points. Right so if we look at the crocodile simulation, the animation, you know, there's a part here so he flips over and I think around there so the, you know, the body's going to be flipping round. Well actually we can see here he's going to be like that and I think it would be good if the boot kind of flies off as he's flipping over. Okay so you know about frame 70 if we delete those then the boot will fly away. Okay so let's make sure we're before frame 140. So we're going to do some things maybe I'll just turn off the solver here if you click on the brain or stop the simulation. Go back to the first frame in fact jump inside a auto-dop network. One thing I noticed straight away is pop drag is in the wrong place. I need to be in the middle connected into particle forces here. I just put it there stupidly. Let's see also I've got five steps, sub steps out here and also eight on the outside you know I just state is enough for us on the outside there. Okay so everything else here is fine so we're going to add in a couple of new notes here to break those constraints right. So we're going to drop a vellum constraint property so you can use this to make changes to constraints during the simulation. Okay so this is you can build constraints new constraints with this. You know you can turn it on at certain points and you can also turn off constraints. And oh sorry you can affect the you can't build constraints with this but I think if we let me just search wrong constraints so you can use this to build new constraints as the simulation goes on so you know if you want something to stick to a wall or for example with this simulation I tested out sticking the body into the mouth you know whenever they go close enough maybe I'll show you that later if we have time. You can do that with this but what we're going to do is grab those boots or we'll have to come to frame 14 to see the group and turn on these simulation just a frame 140 and then hopefully here will show me my left boots okay that's the group of constraints that we made okay and then what I'm going to do is turn on remove okay so that will delete the constraints basically and to control the time of that I'm just going to put on dollar where I dollar F is more than 170 okay so at frame 170 this will become active and it will delete those the constraints which are a chat attaching the left boot to the body and hopefully will fly off okay now also a bit more complicated okay because as I said the welds you can't see them here are actually maybe do we have a visualizer here in the Vellum object guides we have all these same visualizers here we can see the welds so these are not constraints so we can't control them with these so we're going to use a wrangle okay a geometry wrangle also connect that up here and we do this name left boot geometry will be weld okay and let me see four groups and well we just leave that blank I think I should be fine let me do we'll do all groups except for the hunter just in case so it's not working on the on the tetrahedrals right so we just be working on the cloths and so we have this attribute break threshold like this so this attributes is created when we turn on that breaking in the constraints and where are we not the pin in the well not the color here the cuts here so this will generate a break threshold there okay and then we can access that in the stream so what I want to do is kind of weaken it in regards to the time okay so I'm going to use a fit it's not fit to 101 because we're not using values between zero and one now so I'm going to paste this on the frame number okay so from frame 140 to frame 200 so from the beginning towards frame 200 the break threshold will drop down by these two values now okay so from 0.075 to 0.050 okay pretty much the zero so all of them will break towards the end okay so at frame 140 the break threshold will be 0.005 0.075 and then add frame 200 way into the simulation it'll drop to this and most of those worlds will break okay and you know this is the other cloth will be ripped open and look look cool hopefully okay so I think that we're pretty much ready to go now I'm just going to push this up to five I don't think it tells you here inside the solver but if I go out here it's as well I'm in charge when I look at this from solver so it's the same thing this post collision passes if you hover over it says after all constraints are performed the final round of collision detection is done bloody bloody bloody and it says the the recommendation is a number of stack layers plus two so it's basically looking at you know if you've got layers of of valumontop for each other then you should push this number up and we've got you know we've got the tetrahedrals and then we've got the cloth and in fact we've got two layers of cloth here so there could be there's three you know we've got the boots on top and everything so you know just for for safety and pushing this up to five okay but the rest of this I'm leaving at defaults everything in here at defaults as well so let's try caching this out let's see so we haven't actually gone into the into here yet this was generated when we used the the shelf tool so here we're importing the actual geometry from the sim we're moving the normals some reason but it doesn't have any matter and then testing up new normals I believe I'll just visualize this for them I would do we have a factual normals here or I don't know I don't need to worry too much about that and then here on this side where I'm importing the constraints okay which is an essential but can be useful for this valumont post process okay you can do certain things with these constraints all right and what we want to do is cache this out using this valumio okay so this is handy because it will just like before with the with the with the drape it deletes all the stuff which are only all the attributes which are only needed for the for the actual simulation itself and you know that they will just take up space on how drive that's you don't need so I'm going to cache from frame 140 so right click deletes parameters channel sorry to get rid of that dollar f start I think it says frame 140 to 240 that's fine well actually I think if I remember correctly I just go back into this simulation this animation I think we've got a bit more than that yeah if I was going to change my duration I think it goes to 250 this animation why not sub to you but I think that's the end there okay back into here oh press escape I'm just my mistake it's trying to simulate all the way through now so go back to that first frame 140 okay and then give this a good location let's call let's drop this in the sim folder and I don't want to give it a hip name I'll call it let's see body and let's see body and fluff dot version one forward slash now we'll make a new folder for me if this is checked it since media directories and then I'll just the actual file name will this will be this as well I don't want to give it this value my own name I'll give it to this dot I have version one again I don't want to folder there the dot dollar f3 so I'll you know because we got hundreds bgio I just hope it's you and I think that's all good to go look from this now before I forget and then we'll save that out

**Frame:** tutorials\frames\module-ii-week-03-06-breaking-welds-and-constraints-v1-1080p\frame_000.jpg


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

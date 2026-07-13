---
title: Tiling Patterns with COPS and SOPS
source: YouTube
url: https://www.youtube.com/watch?v=05uuRimyHfY
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tiling-patterns-with-cops-and-sops/
frame_count: 0
frame_status: pending-selection
---

# Tiling Patterns with COPS and SOPS

**Source:** [YouTube](https://www.youtube.com/watch?v=05uuRimyHfY)
**Author:** cgside
**Duration:** 16m23s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py tiling-patterns-with-cops-and-sops <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript:** Kind: captions Language: en hello everyone and welcome back so today I'm going over on how we can use cops along side with soaps to achieve these custom patterns uh in odini so yeah let's get into it so this is the final result of the pattern and as you can see it tiles there are some issues with the borders but for the most part it works really really well so yeah it's quite a network but it's just repetition after all so I'm starting by creating the pattern with uh an SDF shape as just a circle and making sure it doesn't repeat then I'm transforming it and mirroring and inverting and we can multiply to create the tile pattern so this is our shape then we need some points to to instance the shape as you can see this will be the final result as you can see and we need to take care of the instancing attributes and the ID also so it tiles perfectly so yeah let's get into the the points first of all I'm starting with a grid with a grid of points and making sure it scales from the center so I can I can connect the rows and columns to the size and subtract one and then I'm creating the X style pattern and for that I need to make sure to have a row and column attributes and this part of the the network was done by fenis he helped me on this one basically we're creating a column ID attributes as you can see and we also creating a row attributes and from there we can filter some of the points and remove them to create the ex style pattern but these row and column attributes will be really important for the next steps so right here I'm creating the the rotation attribute the Sprite rotation and this is just the pattern I identified by looking at the reference image so basically we're creating uh an ID and I can show you how that looks this is the ID where it alternates on the odd column on the odd rows and it also alternates on the even rows we just need a different ID for for each one that's what I'm doing in here in these patterns that I'm establishing and from there I can say if the ID is equals to equals to zero so these ones it will have a rotation of minus 90 and so on from always on the rotating by 90 and then I just set the Sprite rotation to that variable so this is fine but then if we we can instance the the points but if we tile it as you can see the IDS the other parts will be fine but the IDS will be messed up so we need somehow to match this ID to the other side and the top IDs to the bottom ones that's what I am doing in the next Wrangle so basically I'm counting the rows and offsetting the ID attributes if I show you how that looks so ID and this needs to be called ID so it the c network reads it so as you can see if we look at this column it will be the same as this one and the top one the same as the bottom one so it tiles perfectly as you can see in here now they have the same ID on the other side and this is important because we will use this ID to create some color variation so that's why in here I I am using this ID to stdf to create the the shapes so as you can see this is styling perfectly but in this case I ended up not using this because I'm going to recreate the pattern in soaps so as you can see by the final result I also have the circular pattern of stones and for that I ended up relying on soaps again because I couldn't get it to work with just um UV manipulation where you take a r ramp a circular ramp and then UV sample but the results were not good enough at least in my experiments so I ended up creating the pattern in subs and it might look complicated but is actually pretty simple this is the network as you can see I'm just doing a for each count uh how is it called for each for each number and creating a circle let me just reset the network so creating a circle and changing the divisions based on the The Meta import modde the iteration detail attribute so for for each iteration it will increase the divisions and then in here I'm just creating the normals pointing out and then picking it by 0.25 times the iteration fusing and then extruding just a bit and just to make sure we don't have an obvious pattern I'm just randomly rotating with a f one function using the detail attribute the iteration detail attribute and if we run the loop as you can see if I don't have this random rotation it will be really obvious this repetition so this just helps to blend in better and that's how I did that part then I'm creating a a prim ID attribute on The Primitives so I can make sure I I'm on contain the the single tiles because right now I'm going to subdivide it and I still have that primitive attributes and then I can group The from attribute boundary the prim ID and The Primitives around and blast them away to create these insets and from here I'm just saying creating an attribute called stones that I'm also creating in here for for for the center piece and for the back piece I'm just giving it a different ID so I can Target it later and this ID attribute will be important also to do the UVS and also to give it some color variation so this is the Soaps then I'm restoring it and and as you can see I'm rizing by position and making sure I'm fitting the to the bounding box and scale to fit and I'm just uh increasing the size just a little bit so it aligns better with the pattern if I show you in here as you can see so it aligns here because if I have it to default it will have these small stones so I'm just scaling it a bit in and after the rizing I can roriz the attributes in this case the stones that attribute that I created and the prim ID so after we have these two layers the stones and the prim ID we can you we can create the UVS using this UV by ID HDA and we just connect the prim ID and it will create the vs then we can offset it a little bit using the ID as the seed just offsetting between zero and one and then we can just image sample some texture that I have in here as you can see some Stone texture and we image sample that then we can from the ID create create a random mono and that can feed to an HSV adjust where I I am decreasing the value and increasing the saturation and after that I am also what am I doing in here taking the stones I guess taking the stones and and adjusting and inverting it as you can see with a compare node and then I can just decrease to have these background darker then we go back up and look at the ovs in here and and with this UVS from the initial shapes we can ovv sample in this case image sample and we will have the pattern so the only thing left to show is on how to create this outline pattern of stones so for that I'm relying again on Cops as you can see from the stopping boort and let's go through the setup basically I'm starting with a circle converting to line and clip the left and the bottom resample and transforming it down the same shape and merging and then just mirroring it and the the reason I'm doing it this way is because we will have equal amount of points on all sides on all parts of this shape so when we combine them and later we will fuse them they will have the the same amount of points on each side so they match perfectly if we if we do the resample after it would create many problems so we have the shape and then we can copy two points and use this the same um Sprite rotation so I'm importing the points from the previous setup you can merge a sing port in here as you can see the that's why we save that out points no and then I'm just setting the normal and the up and rotating the the up by the same amount of that Sprite rotation making sure we set it to radians because that we add degrees in that we have degrees in the Sprite rotation scale is just set one and we copy two points then Orient along curve so we have normals along the tangent of the curves this way the stones will follow this shape fusing everything deleting the attributes but the end and making sure we set the app attributes to use in the in the ining of the stand points then we just box clip to match the pattern we created before so ruizing the setup and stamping the points as you can see just the default shape and we get uh almost perfect uh tiling and from there we can do the same process of image samp Le the the same Stone texture adjusting some of the tiles uh in uh introducing the darkness the darking effect on the between the [Music] stones and blending with the original texture so that's basically the setup this is the albo I'm also creating some displacement and also creating some scattering density attribute as you can see so I can instance some grass between the stones later so I get add some roughness also and that's basically the setup so in case you want to go a bit more deeper in these sort of setups I just released uh two-part series on my patreon where I go over these sort of techniques combining soaps and cops and if you are interested in that make sure to check out my patreon other than that I just brought the textures to Solaris and and uh scatters uh some grass and that's basically my final result I hope you really enjoyed this one and learned something from it if you want you can grab this full scene on my patreon and other than that thank you for watching and I'll see you next time



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

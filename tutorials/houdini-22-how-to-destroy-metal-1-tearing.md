---
title: Houdini 22 | How to Destroy Metal | 1 | Tearing
source: YouTube
url: https://www.youtube.com/watch?v=x-N5I4XS7Q4
author: Houdini
ingested: 2026-07-18
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/houdini-22-how-to-destroy-metal-1-tearing/
frame_count: 0
frame_status: pending-selection
---

# Houdini 22 | How to Destroy Metal | 1 | Tearing

**Source:** [YouTube](https://www.youtube.com/watch?v=x-N5I4XS7Q4)
**Author:** Houdini
**Duration:** 15m54s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py houdini-22-how-to-destroy-metal-1-tearing <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript:** Kind: captions Language: en In this tutorial, you will learn how to use the new metal destruction workflows in Houdini 22. You can follow along by opening up the RBD metal start 01 file. And then we can just jump into the geometry container. And in here you would find the garage geometry and also I have the animated crack that I transformed and re-timed. So it basically aligns with the door and it will help us in our destruction demonstration. Okay. So in this garage file you would find some groups. So we're going to isolate the metal door. Let's press tab and type split. And in here in the group I'm going to choose metal door. So now we have metal door that we can fracture. Let's press tab and type RBD material fracture. And we're going to connect it after the split. So basically I'm going to put this to manual and we're going to change the material type to metal. And if we go to fracture you can see that it is going to scatter 100 points. Right now I'm in manual mode so nothing is updating. So for now I'm just going to drop this value down to 50 points. We don't really need that many. And I'm going to put the display flag to RBD material fracture and set it to auto update. Okay, we should see our fragments. I can press W on my keyboard to see the fragments. After this step once you're happy with the initial amount of fragments, we can go to details tab and we can adjust some of the edge details. Uh, again, if I'm going to be changing these values, it's going to start updating as soon as, um, I stop clicking. So, I usually go to manual mode. I set this to um, some lower detail size to get more subdivisions, maybe a higher noise height. And I'm going to change the element size to 215. And now if we watch closely, I'm going to go to auto update. We're going to have more details along the edges. Okay, there we go. Now you can see we have more details. Um, so after this step, we can basically, um, inspect how the constraints are built. So, right now we have two types of constraints. One is glue, which would be the initial constraint, and then after the glue breaks, we would have the soft constraint that would basically mimic the bending behavior, uh, on the metallic pieces. By default, uh, usually these constraints, um, are set a little bit too high. So, I usually like to lower the glue strength to something like, maybe, uh, thousand. Um, and we can basically proceed with, uh, setting up some of the additional simulation parameters. Let's press tab and type RBD configure. And we can connect all three inputs to the RBD configure. And what I usually want to do is, uh, I don't want to have this whole section as active piece. I want to basically pin it on the um, top part and on the sides so we can turn on active attribute and then use bounds. Um basically, you can use a bounding box that you can just press tab bounds and then you can um plug it into this last input or you can also use the built-in bounding geometry. So, if you go to bounds, change this to bounding box, you would see this red bounding box and we can actually interactively change this in the viewport to capture the area that we want to be active. And change this. All right. So, I actually have some values that worked pretty well for this demonstration. I'm going to put them in here. So, 2.77, 1.35, and 4.72. Just so we're all using the same setup. Um and then um what is also quite important and can change how your um simulation looks is this uh physical attributes. So, if you're simulating metal, it would make sense to change this to metal and also we can change the type. And this will adjust the density parameter and believe it or not, this could actually change the look of your simulation and how heavy the metal is and how easily it bends. For now, I'm going to change this to aluminum. And basically, we can proceed with the simulation. So, I'm going to press tab and type RBD bullet solver. And let's connect our high-res, let's connect our constraints, and let's connect our proxy geometry. And um if I press play, you can see everything is standing still um because we pinned the top. Um I'm going to go to the collision tab and I'm going to turn on ground plane so we have the infinite ground. And lastly, for this to work, we are going to connect our crack character to the collision geometry input. Okay, let's uh press play and see what we have. So basically, we are getting the hammer um destroying these fragments, but they are not actually flying away. So, if you take a look at the constraints tab, um the pieces wouldn't be able to detach unless the distance is higher than uh this value. And we can basically lower this to something like 0.1. And let's go to the first frame and do another quick simulation. So now you can see we're getting a much better behavior. The fragments actually able to be detached and we are uh getting this interesting shape as a result. But this is not really uh the final look. In order for this to work, we need to add an additional node, which is called RBD deform pieces. So let's plug all three here. And uh as you can see, this also doesn't look uh amazing because it is trying to keep all the fragments together. This would work great if you just want to have some kind of denting without allowing the pieces to be detached, but if we change this uh boundary connection from cluster attribute to constraints, now you can see we're getting quite an interesting shape in here. All right, let's make a quick preview of what we have. So, I'm going to uh zoom out. Let's press control shift onto the template flag, so we can see the crack character. And there's actually a camera here that you can use for your flip books. So, I'm going to give myself a little bit more room, and I'm going to click and hold onto the flip book with new settings. And I'm going to hit start. And I'm going to pause the video and come back. All right, we are back. Let's check our result. So, overall everything is working, but uh metal is a little bit too jiggly and springy. And we can actually control this with a dampening parameter. Okay, so let's go back, and in the RBD material fracture, we can adjust some of the constraints uh properties to make this look much more stable. Okay? So, um usually what you can do, you can increase the dampening ratio. I'm going to multiply this by 4,000, so we get this value. And I'm also going to reduce the uh angular dampening cuz I actually want this to be bent more outwards. And I'm also going to reduce the angular stiffness. So, we basically want more bend, but we want a stable behavior, so it kind of bends out fast and then freezes with this dampening ratio. Um sometimes reducing the glue strength can also help uh getting more fragments to be detached or uh dented inwards. All right, so let's now do uh another flipbook. I'm going to take the second out from this and press uh tab, type null. And I'm going to hold control shift and click on the template flag, so we have more or less similar view. And let's do another flipbook, and I'm going to pause the video and come back. All right, let's check our result. So, now you can see we're getting a much more stable uh metal tearing. And uh also we're getting a much nicer shapes. They're basically kind of bent outward and freeze into this interesting form. Okay, now let's take look at one more setting that can change how your metal behaves when it's getting destroyed. So, in the RBD material fracture, you probably noticed that we are operating at a complete uh thin surface. So, let me just press the template flag onto this one. So, you can see that this is not extruded thick geometry, right? So, this is completely thin surface, and RBD material fracture under the metal can actually uh do a really nice job. Um but what if you want to have a thicker metallic wall, right? So, let's uh mimic that scenario. Press tab and type poly extrude. Okay, let's connect the output of the thin door. Let's uh press the display on poly extrude, and we're just going to use the transform extrude at front. I'm going to set it to zero minus 0.01. And we also need to make sure the output back is on. Okay. Okay, let's make sure we have vertex normals, and then we need to reverse them. So, let's put down reverse. Uh okay, maybe we we need to add another normal node. So, it looks correct. All right. Uh let's set this to 10. All right, so now we have our uh surface. So, let's now put another RBD material fracture. Uh I can actually copy this first one. So, let me go to manual mode so we don't Wait. So, control C control V. And uh let's take a look at this one. So, I'm going to go back from manual to auto update. Um So, you can see it does some kind of remeshing and stuff. I'm going to quickly hit escape, and I'm going to change this to solid. And I'm probably going to give it less fragments, so we don't need 50. I'm going to set it to 10. And uh let's wait. Okay, let's press W. So, you can see we still have all the fragments. If I put the exploded view, you can see these are now thicker metallic fragments. Okay, and um everything is pretty much the same with the constraints. We just reduced the amount of pieces. Uh you can probably also reduce the uh detail size um because this is going to be a little bit slower cuz it has to add extra details on the thicker uh surface. So, something like this should work quite nicely. And uh after this one, we can basically proceed with our setup. Um I'm going to copy some of these nodes. So, we can just reuse this whole setup. I'm going to select these nodes from our first one, control C, control V. And let's just connect these. Okay, now we have uh the same RBD configure. Everything is pretty much the same. Um the metal is aluminum, and let's see how um how this is going to behave. Let's put the camera, and let's press uh display flag on RBD uh deform. I'm going to maybe even just merge these together with the crack. Okay, and let's do a flipbook. Let's see how this looks. Okay, let's check out the result. So, you can see um the fragments are a little bit more stiff, and not all of them are breaking it as easily. So, we can probably go ahead and adjust some of the uh constraints. So, you can see the glue is set to 1,000. I'm going to set it to 100. Basically, to allow more of the fragments to break away, and let's do another flipbook, and check it out. Okay, we're back. So, you can see with the uh reduced glue, we're allowing more of these kind of fragments to bend inward and outward, and we're actually getting some real nice details along the edges. Uh you can also play with the uh RBD deform pieces. So, if you adjust the maximum points, so for example, if I set it to 10 and if I set to the maximum to 100, um maybe we can also adjust the radius. You can see that we're getting a little bit of a different uh blending between them. So, definitely play around with these settings and see what you get. Um some of them can give you a more rough surface and some of them can give you a smoother surface. And basically, this is how you can um fracture and tear metal in Houdini 22.



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

---
title: module i   week 01   01   your first houdini project v1 1080p
source: YouTube
url: https://www.youtube.com/watch?v=Mq1snWFUBj0
author: The VFX School Archive
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/module-i-week-01-01-your-first-houdini-project-v1-1080p/
frame_count: 4
---

# module i   week 01   01   your first houdini project v1 1080p

**Source:** [YouTube](https://www.youtube.com/watch?v=Mq1snWFUBj0)
**Author:** The VFX School Archive
**Duration:** 9m34s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Hello and welcome to the Houdini Renaissance Programme Volume 1. This is the updated version, so we're working in Houdini 18.5, so we're going to be using all the new tools and workflows that have been implemented by side effects. For this first project we're focusing on modeling and we're just looking at the basis of modeling and a bit of an introduction to Houdini. We're going to be lighting, rendering, adding materials in the new Solaris context and rendering with the new render engine, comma. And then we're going to be doing a little bit of compositing in Nuke and we'll end up with a really beautiful render at the end and a nice kind of basis to understanding Houdini. Okay, so here we are in Houdini. If your layout doesn't look the same as mine then just head up here and go to build. It should be on this by default, so in case it looks different then you can come here and set it to build and then we'll be back at the default. So to introduce everything here maybe we'll start just by dropping a sphere, so just come here and click on sphere and then just press Enter. If you click then it will place it wherever your mouse is, so I just press Enter and it will be at the center. So here we got the viewport, that's where we can actually see our geometry. If you press Alt and then left mouse button you can do this, middle mouse button to do this. You can see the instructions on the bottom there when I press Alt, left mouse tumbles, middle mouse pans, right mouse button. It's going to be a little bit more interesting to see how it works. So I press Ctrl, right mouse button to go back, which is kind of your standard. So on the right here you can see when we drop that sphere we have this little box which is called a node and this is a geometry node. And you can see it says sphere object one, so this is an object and this is in our object context. And up here we can see sphere object one, so it obviously relates to this. And this is the parameter window which we can use to make changes to this. So we can actually type in here, so if I press one, you can see my sphere moves up, a little, press zero goes down. So if I want to make any other changes to this, okay, I'd have to go into a different context. So as I said, this is the OBJ context out here. And if I click on this arrow, I'm sorry, not on the arrow here, then we can see we've got other networks, other contexts. We've got we've got chops there, we've got the image context. So there are quite a few, but most of your time we'll be spent in the OBJ context, okay, objects and within OBJ will be soft, which is actually surface operators where you're working on geometry, doing simulations, things like that, okay. We'll talk more about these as and when we come to them, because if I go over each one and explain them, it can be a bit boring. So I won't bother with that now. So now we're in the object context. So here typically, you would have different objects, so you might have a sphere and then you might have a ground. So if we press, you can come up here again and press grid and then you have a ground, there we go, another object, okay. You might have a camera, so on the right here, we've got cameras, so I can press camera, drop a camera. So that comes there, we can drop a light, point light, okay. So you can see there we're kind of building up our scene here. Now, after doing, well, this and explaining it, I've got to explain that things have kind of changed recently and we'll be doing all of this within a new context, which is called stage here, which will be, which is working on USD files. So let's delete all that and just keep our sphere. Okay, so like I said, we can zoom in and take a look. If we come up here to this box here, we can see that there are different ways of viewing our geometry. So typically I like to work in this smooth wide shaded, so we get smoothed normals and also you can see the wire frame. You can also view the points as well here if you need, you can view your vertices, sorry, your vertex normals. We got different lighting settings here, they won't do any much now because we don't have any lights, but here you got different levels of quality and lighting. On this side, we can move our geometry around, okay, we can use these handles to manipulate our geometry. So typically I would just use this kind of gizmo, which kind of encompasses all of these except for the scale, but you can use that to. Move your geometry around to scale, you'd have to click that and then you know, you can do your typical kind of scaling things. Go back, okay, and also you can always just type values into your parameter window up here. So as I said, we've got parameters up here, but the way I prefer to work, if we come here, select your geometry node and then press P on your keyboard, we got exactly the same. The options down here, we got a little parameter kind of window in the corner. So I prefer to get rid of these windows, okay, and then just have it in the corner there, I find this a bit more, a bit cleaner, easier to work with. So now if we take this node and we can either double click to go inside, okay, and then if I want to come back out, so here you think about this like your kind of folder. If you're looking at folders on your computer, you know, you're going into your into your drive and into a folder into another folder, you can do the same thing here. So if I've got I've gone in now, I want to go back out, I can click here. Another option is to press you to go up, I can also press I to go in, okay, so here I'm in the, I'm still in in the obj context, but actually in the SOP context now, which is SOP surface operators. Now I have access to these individual primitives or polygons and the points and I can, you know, have a lot more control over these over the geometry, okay, I can do things like that. On the outside, basically, I can just rotate, move and scale it. So I'm just going to get rid of that. So let's go back out and let's actually do something that's very important at the beginning of any project, which is to set up your. Your project folder, okay, so saving your scene. So come up to file and then we're going to go to, where's it, new project. And then give your project a name, so I'm going to call this my first. You're doing the project. Okay, and then wherever you'd like to save this, this is dollar home, which is a, who didn't variable, which you don't need to worry about too much, but it's just, you know, wherever you saved, who didn't even stalled it, I think. And you know, you can put in any, any drive that you like. So I'm going to leave this in my D drive. Okay, so this will create a folder in my D drive called my first to D new project. And it will create folders within that folder with these names. Okay, and this is just. Useful to for saving different types of geometry. Okay, so we just click accept on that. And then we come up to file save as. Okay, and then go to what if you press dollar hip, that will take me, sorry, dollar job initially. And I will take me to where we just built. Okay, that's where we just saved that project. And then give this a name. So the same thing my first, let's call this our scene. Okay, because this is a scene file, our hip file, click accept. And let's take a look at how that looks on the computer. So there you go. You can see in my D drive, we've got this folder called my first to D new project. And within that, we've got all these folders. And then at the bottom, my first scene here, which is my hip file. Okay, and then if I want to, you know, once I close my computer and I want to start up, who D new again, I can just come in here, double click that, and I will open my project. As long as they saved it, as they did, as it was the last time I was working on it.

**Frame:** tutorials\frames\module-i-week-01-01-your-first-houdini-project-v1-1080p\frame_000.jpg


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

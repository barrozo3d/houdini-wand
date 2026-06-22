---
title: Animate Gaussian Splats with Houdini - Free Tutorial + Scene Files
source: YouTube
url: https://www.youtube.com/watch?v=MqtMQl8DtjQ
author: SOP Cemetery
ingested: 2026-06-22
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/animate-gaussian-splats-with-houdini---free-tutorial-scene-files/
frame_count: 0
---

# Animate Gaussian Splats with Houdini - Free Tutorial + Scene Files

**Source:** [YouTube](https://www.youtube.com/watch?v=MqtMQl8DtjQ)
**Author:** SOP Cemetery
**Duration:** 81m2s | 9 section(s)

---

## Raw Data (for Claude Code extraction)


### Intro [0:00]
**Transcript:** Hi guys, I'm Bogdan and to the popular demands I finally managed to put myself together  and recorded tutorial for you on how to animate a Gaussian splat using Cudini.  Because this is a fairly large scene, instead of rebuilding every single node from scratch,  I think it makes more sense to walk you through the final setup, node by node, and explain  the reason behind each important choice.  I will also give you the project file so you can explore the scene by yourself, modify,  break it, improve it, and hopefully use it to start as a starting point for your own  Gaussian splat animations.  But before jumping in, I want to give you a bit of a context about Gaussian splatting.


### What are Gaussian Splats? [1:00]
**Transcript:** I'm sure that you already know what Gaussian splattings are, but I think it was taking  a few minutes to give me a chance to have my take to explain the basic idea, especially  because understanding what a splat actually is makes the Cudini setup much easier to follow.  So let's see.  Gaussian splatting appeared in 2023 at C graph with a paper from five, six guys, I don't  remember the names, and they propose a new way to represent the objects and environments  using something called splats.  So the way in the end those splats look more or less exactly like polygonal geometry,  but there are a bunch of points with volumetric representations, but because there are many  and well-oriented, you cannot find the difference between a Gaussian splat and a polygonal  geometry.  So as I said, Gaussian splats are a cloud of points, a dense and oriented, while the classical  mesh wire frame is a set of points connected by faces that could retain the information  from the textures and vertices and edges and so on and so forth.  So Gaussian splats are not a surface, but a dense stack of soft-oriented volumes, each  carrying color, alpha and luminance, and because they are perfectly aligned and ...


### Import GS / Segmentation and Surfacing [9:29]
**Transcript:** This Houdini 21, we have Gaussian splatting native inside Houdini, but we still need to  download this plugin over here from the GitHub.  So use this link to access it.  You have a tutorial on how to install it, so I won't go over it because it's kind of straight  forward.  And those guys really did a great job integrating Gaussian splat inside Houdini.  What I did to this scene, especially, I used two or three notes from there, plugin from  the older version, and I unlocked the assets.  So you do not need, especially for this scene, you do not need to install it, but my advice  is to install it and explore it because you will learn more about Gaussian splats.  We have several sections.  First is the important segmentation of the fly.  Then create a Kinephic skeleton and capturing the weights.  Create a skeleton.  Create the apex rig and animate it.  Then point the form it and explore the spherical harmonical look development plus some extra  perks that I will show you guys.  And then rendering inside karma.  Okay.  First of all, use these Gaussian splats, not import.  Again, you do not need to install the plugins, use those unlocked assets and just continue  working.  In the proje...


### Create KineFX skeleton [21:09]
**Transcript:** have a skeleton.  So in order to capture some weights I got to have a skeleton in a skin.  I only have a skin right now.  For example if I put here a merge node to see what we have now until now and I pick all  those geometries and put it here you will see.  I have my fly made out of separate elements, heads, body, left, right wing, tail and one  geometry for each leg.  Okay.  So in the case of the skeleton I just manually build each skeleton.  For example that's the skeleton for the head.  Okay now comes the transform, X-ray transform node.  So let's deactivate those X-ray transform nodes and see how this geometry looks like right  now.  It's a little bit rotated.  That's the original position of the fly that comes from the Grautian's plot.  And if you look from the top we can see that it's a little bit off.  When I did that I didn't care much about this rotation from the top and I started to build  my skeleton based on this position.  So I build my head skeleton here.  As you can see it's more or less in the center of the head.  Then...  So left wing skeleton.  I won't get into detail how to build a skeleton.  In KinaFax it's fairly simple.  You just write skeleton and start draw...


### Capturing / binding the proxy geometry [32:29]
**Transcript:** Bind the skin to the skeleton.  And we do that using amazing node that we have called the harmonic capture.  And what the harmonic does is perfectly binds the skin to the skeleton.  So let me explain you a little bit how this by harmonic capture works.  Let's say we have this skin.  We have our skeleton.  And as you can see the joints from the head.  Okay let's do it the other way around.  The joints from the head are in this area.  Now one joint of the head, the tip of the head is inside the surface.  The other one is sitting exactly in the hole that we have when we generate the surface.  Because that's the way the ocean's plot was captured.  It has a hole here.  So when we generate the surface we have a hole.  And because we have this hole and the joint sits inside the hole it won't capture the surface.  And the reason is that is because what the harmonic capture does it creates a tet type of geometry.  And this type of geometry contains a lot of inside triangles, not only the outside triangles,  but also the inside triangles.  And those inside triangles are used to calculate the capture areas and that do not exist in here.  So the joint should be placed inside the closed surface...


### APEX Logic [41:31]
**Transcript:** But before going to apex, I want to explain why apex and what's the difference between  apex and skin affix, but actually it's no difference.  It's only everything is skin effects and apex is only a system of rules that you apply over  kin effects to help the animator.  But how?  So if I want to animate this creature, I bring a repose and as I show you, I start to animate  each bone.  But this is tedious.  I mean, no animator in the world will accept that.  And also the quality of the animation will not look good in the end.  So what animators, once they want controls, they want to control here and I cater when  you drag this tip to move the whole wing.  Or if you want to animate a leg right now, it's crazy.  I mean, I got to move this, then I got to move this, and I got to move this.  So it is tedious to do it by hand.  This is called forward kinematics animation.  And for some things is good, but for others is tedious.  So an animator will need an IK chain or a solution to have an IK kinematics.  An IK kinematics means that I will have a relationship between all those three bones,  for example, from the leg.  And the only thing I need to do is to pick the tip of this leg and move...


### Animation Overview [65:10]
**Transcript:** Call it fly.  You can save it on disk as a BGO and whoever will open this BGO and apply a scene animator  over it.  It will have a full character, which is another great future.  Because you shouldn't export a lot of dependencies.  The whole logic of the rig will reside inside the BGO.  So once you add a character into the scene and call it fly, you can apply a scene animation.  Let me show you how.  And once you have this active, you can see how your character working here.  Cool.  You can even test it like that.  Now, the issue with this one is that you will see, for example, when I'm starting to deform  it, the splats does not deform correctly.  I mean, they remember the original orientation.  And then you see when I'm stretching the leg, for example, the splats have a tendency  to go back to the original position.  And that's because I do not influence it.  I do not point the form and not transform the orientation of the splats.  And the splats don't know how to rearrange to the correct position to keep the shape of  the leg.  So that's why this Gaussian splat is not the Gaussian splat that I will render and is  not the deformation that I will use.  I just put that here for the...


### Deform GS wit SH Look Dev + Bonus GS visualization [71:50]
**Transcript:** development.  So I open again a Gaussian splat with the Gaussian splat import, exactly as I did at the beginning  of this course.  Bake it.  This time do not compute the spherical harmonic coefficients because I want to relate it  by my own, transform it back to the position, apply the extra transform that you already  know, and then add the capture skin, but as a response, a static capture skin, and the  animation.  Plug all those three into the Gaussian splat deform, which inside of it it has some scripts  that fetch the x-form properly and extract the transform and bind splat to prem.  And by doing that, now we deform the actual points with the geometry.  These Gaussian splat deform work only with the input from the first input are the points,  then the geometry that will deform those points.  And that's it.  That's the way this should look like.  And the result is a Gaussian splat animation.  Okay, if something is not perfect, because the scan wasn't perfect, this time I import  the Excel scan.  You also have the x-excel, which is a huge one, even more detailed than this one, but for  my point of view, Excel type of scan has enough detail to really sell it as a realistic  fly, ...


### Karma Rendering [78:07]
**Transcript:** And as I said, my render is not such a fancy one.  I was going inside Karma.  Choose to render it with Karma XPU.  Basically, you do not use materials.  You cannot use anything.  You just place it here.  The light, this dome light, doesn't influence it at all.  Again check on internet.  Now you can influence with the Karma lights and you can really do more than I did here.  The only thing that I did is to put a camera and add some depth of field, some focus distance,  some stop like that and add motion blur.  Because I have velocity blur, you have motion blur.  Put a plane there to cast shadow over it.  That's it.  To cast shadow over it, you need to, when you import the Gaussian splats, you need to  add big G splats, you need to disable shadow casting in Karma.  It comes with this click so you unclick it to enable the shadow casting Karma.  And that's it.  Cool.  Hopefully this was useful for you guys.  I know that you might expect the public for these Gaussian splats.  It's not so keen about animation and kin effects and rigging and apex.  But unfortunately, that's what I did.  I mean, as I said at the beginning, I just transformed those points into surface and  then the bulk of ...



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

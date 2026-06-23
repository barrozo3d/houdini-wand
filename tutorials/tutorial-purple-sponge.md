---
title: [Tutorial] Purple Sponge
source: YouTube
url: https://www.youtube.com/watch?v=O5cFGKp0n_A
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tutorial-purple-sponge/
frame_count: 4
---

# [Tutorial] Purple Sponge

**Source:** [YouTube](https://www.youtube.com/watch?v=O5cFGKp0n_A)
**Author:** Alexander Eskin
**Duration:** 29m17s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** I was inspired by Mark's true gear work on Instagram. So I'll go check it out. So I'm going to start with the June node. Name it points, source, green, dive inside, create a box. 0.7, 0.15, move it to 0. Convert to VDB, VDB from polygons. Now we need a fog VDB with higher resolution. Apply cloud noise. Default settings will do points from volume. 0.07, 0.75, yeah, 400,000 points. Add scale attribute 0.5, edit preview with the wrangle. So we're going to see how the plans look like in the viewport. IGL, sphere points, close one. Like this, and then create a group. Group by points, blaster. Bounding regions 0.5, 2 here, blast everything but the group. And delete everything below 0. Also need to add another noise. So it looks a bit more interesting. 0.4, this place. Vains, noise, get vector component. First one, position frequency 15. Add to the current position. A little to vector. Y is going to explode. Yeah, the amplitude is too big. Multiply constant 0.05. Now we have some funny looking stuff. At least a bit more funny looking. Then it was before. More details, the more the better. Now I can create Vail and Greens. They're going to look huge, but we can fix that by copying a p-scale from before. Add to this copy here, from here. Not color, but p-scale. A little solar. Connect these, connect these. Fix the frames per second, 30, apply. Fix the gravity, minus 1. Don't forget to check the ground collision. Okay, everything explodes. It should be because there aren't enough sub steps. For should be a good start. A bit better. Now everything is very jumpy because our points intersect with the collider at 0. We can fix it by moving everything a bit higher. Move white. B-t-y plus equals p-scale. Now everything moved by the radius of the radius. These spheres, which is exactly what we need. Now everything is a bit more stable. Which is still not enough. Looks pretty boring. We can check under the green collision tab. The green collisions and there's interaction weight. Consider it to 1. And they're going to clump together, like a wet sand. Which is fun. But again, looks a bit boring because of the uniformeness of the clumping. But we can fix that. We can cluster some of the points and decide which ones are going to attract more to each other. And which ones are going to be attracted less. So we need to use a cluster node. We can use cluster points 32 clusters. And we have now a cluster attribute, which is an integer attribute that we can use to drive the custom attraction weight attribute here. You can see there's a hint, attraction weight, using the wrangle. Call it attraction weight. Custom. Custom. We can load it attraction weight equals ramp attraction. Random from cluster. And let's see how it looks. So we can see the different clusters attract to each other differently. And it looks a bit more interesting. Let's fix the minimal attraction to 0.2. Good enough. And leave it as is. Also we can use the rest attribute to color these things later on. Post-seam. So the default values will work. We're going to have the rest. So we're going to use later on. Okay. Attribute it. That it's something that we don't need. We can leave on the things we need. For example, the list is always useful. Rest, P scale, and sphere points here. And delete now selected. Now we can color this stuff. Point wolf again. Color. You can use two real nice. But we won't use the position. We are going to use the rest attribute. Bind. Rest. Don't forget to check the vector. Position is going to be rest. True that noise is going to drive the color. And we're going to use ramp. Chest in case. Noise. Promote these. And clean this thing up. A bit edit parameter interface. Hide. Hide. Add separator. Apply. Now it looks a bit cleaner. As for the noise. I use these parameters. Abled view 2. Add a null. It's going to be out of points. Also right now the animation is too fast. For my taste, I'm going to add a time warp. And I'm going to use the frames from starting from frame 6. And the end is going to be frame 37. And they're going to be stretched from frame 1 to 100. So a bit slower. Now we should create the cotton balls. We're going to copy on top of these points. We're going to use curve polygon. There's something like this. Simple. The curve is going to be sub divisional. Looks good. Now we're going to move around it a bit in the Z axis. So it won't be as flat. Like this. We're going to use copy to points. I'm going to copy this on top of some points. Add single point. Point replicate. 55 points. Default shape. Now they're all aligned at the same angle which is annoying. Add it with random eyes. Orient for dimensional vector. And mino value should be minus 1, maximum 1. And we're going to check use first dimensions parameters for all. Otherwise we have to copy them paste here minus 1, minus 1, minus 1, which is boring. So we have this sort of ball. I'm going to use this sphere to represent our point because when we're going to instance these things on top of these points, the scale is going to be multiplied by p-scale value. So I'm going to use this here as a reference for scale. The trick is that the sphere with the scale of 1 equals only a half of these spheres. For example, if we're going to copy two points, we're going to copy this sphere with the scale of 1 on top of these points. They're going to look twice as small. So I just use this sphere with the radius of 2. That way they're going to look the same. So we're using this sphere as a reference for scale. And right now we can see that these things are too big. We can scale them down a bit. But not too much. They should intersect with each other in a dense compact geo. So we've eaten all. Call it out. Call it to bowl00. And we're going to make some variations of the same stuff. So we won't end up with the same looking bowl. Move these around a bit. Change the seed. Change this scale perhaps. And here with third variation. Change the seed as well. So we have our instances. We're going to need to create different genos here. They're going to use instances for the bowl00. Change the seed. Change the seed. So we now have three different cotton bowls. We're going to copy on top of the points. And we're going to use attribute wrangle. Call it instance. And just use string attribute instance for copying these points. Object. Bowl00. And that's it. I'm going to use the first one for now. Here we're going to create an instance now for it's shift. Object. And our points. And we're going to check the last point. Instancing. And everything will slow down to a crawl. Also we're going to check shade of the curse. So right now there's only one cotton bowl that's copying. The same one. And the rotation is the same across all the points. And we can fix that by introducing the orient attribute here for every point. Attribute render wise. Orient. Minus 1. Uniform for dimensional. And it looks a bit more randomized to me. And also we can create different values for every point ranging from 0 to 2. We can do this by creating an attribute string num integer to string for random at the num multiplied by 3. Because we're going to have values from 0 to 2 and those brackets. Create test. Test with those num. And we're going to check how it looks like in this spreadsheet. As you can see, the test returns the values from 0 to 2, which is exactly what we need. So we're going to kill the test and kill the last number and add a num here. So our string attribute will look like this. Cotton bowl. 0, 0. Cotton bowl, 0, 1. Cotton bowl, 0, 2. I don't think we're going to see this in the viewport. But we can color these ones for the preview purposes. Red. Green. So we can see that these instances are equally distributed across the points. Okay, we'll do. Now we can render this. We need two shaders. One for the background and one for the fur. The background is going to be a simple one. No reflection. No nothing. The color is going to be white. What the weight is going to be 0.8. Fur. Red shirt here. Leave it as the defaults so far. I'm going to go to red shirt custom. Create a camera. No. 19, 20, 19, 20. I'm going to kill the preview. I don't want to see that. The point is going to be fine. And 45 here. Zoom in. And a bit higher. Okay. Create the background. Apply these shaders. The one goes for the background. The other one goes to cotton balls to the instances. Okay. I'm going to dim the background. And the fur is fine. Create two lights. One's going to be the dome light. The other one's going to be just the airy light. So, point one. It should be disc. A bit smaller. Spreading to be 0.5. And dims to 50. And move it around. Do about here. Okay. Let's see what we have. Oh, forgot to check the render polygons here. Checkbox. Okay. There it is. Something. There are a couple of problems right now. Color is sort of off. There are things that look off. Okay. We're going to start with the color. Import the color attribute from our points. Point attribute, color, ramp. And we're going to use it in trimutter reflections, in transmission, and in transparency. Okay. We're going to do the transparency. Why is it black? I'm going to set the number to here in the color to 2. Forget to do that. Okay. And we're going to change the color to white. I'm going to use some fun colors. So, introducing fun colors. Kind of sort of fun. Also, can introduce transparency. And add color here as well. Now the color looks extremely saturated. It looks really light. And we're going to use some more light here. Still looks a bit off. Maybe lower light for a more dramatic look. So, I'm going to fix these things. I guess we can just scale our p-scale a bit. To fix this, scale, p-scale, p-scale, multiply. Multiply by 1 plus channel load scalar. And I'm going to just increase it by 10%. I think now it looks better. I don't know, we should increase the resolution. It's still not visible, but not as much. I think we can get away with it. It looks okay. A bit boring for some reason. Not we can win into when we use this small portion of the ramp. And the colors here are adjusted. Now it's going to be a bit more convenient to use it. Also, if you're going to render these two images, the bucket render just doesn't work with this kind of geo for me at least. It takes about, I don't know, 40 minutes per frame or more than an hour. So, I just, when I was rendering an animation, I just used progressive for the final images. Just tweak the numbers here. The more passes, the cleaner the result will be. But it's going to be cleaner a little faster than the bucket mode. Keep that in mind. And that's it.

**Frame:** tutorials\frames\tutorial-purple-sponge\frame_000.jpg


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

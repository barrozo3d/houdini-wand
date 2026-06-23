---
title: [Tutorial] Glass Donut
source: YouTube
url: https://www.youtube.com/watch?v=j5Ew_6-W8DE
author: Alexander Eskin
ingested: 2026-06-23
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/tutorial-glass-donut/
frame_count: 4
---

# [Tutorial] Glass Donut

**Source:** [YouTube](https://www.youtube.com/watch?v=j5Ew_6-W8DE)
**Author:** Alexander Eskin
**Duration:** 13m28s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Let's create tune-out lets fill it now Tell it the last Bridget Direven's side create our dot it stores orientation x size 0.5 0.15 rows 400 columns 800 good now we should add some noise with point or noise we're going to use anti-aliased flow noise because it has the flow attribute let's add this noise to the current position and this is what we got let's tweak the parameters a bit roughness should be 0.6 octaves for frequency 4 these ones should be 0 and the amplitude should be 0.025 okay here's our dot at the anti-aliased flow noise has the flow parameter which allows us to cycle through noise so we have the 0 and 1 would be the same image all the noise and while we scroll this or animate it there would be some motion so we can create some loops with ease that's what we're going to do we promote this parameter because we can't animate in the whoops kill this small stuff I don't need this we don't need this separate this and animate it set a 30 FPS and animate it from 0 to 1 set the revolution to linear and move this frame to 301 otherwise the first frame in the frame 300 will help the same noise pattern and I'm going to have a bump in the animation you know so we don't need this I'm going to move it one frame further okay now we need to add a full extra extruded by 0.05 and don't forget to press open back otherwise it will just displace the thing and now have two layers okay that was the idea output modeling wise is done we've achieved output custom create a camera select it output in the line advanced we don't need the global elimination here because it's going to be just glass and black background levels set it as is and go to material step press first material builder glass standard diffuse zero reflection one roughness zero transmission one amazing glass material fly it to I would you not okay the camera should be at 120 millimeters focal length press the lock I'll adjust it now just eyeball it where is it where is the fun part of the image somewhere here okay and we need to create the hDI to light the glass I'm going to use after effects you can use whatever program we prefer it's just a simple gradient with color 4000 pixels by 2000 pixels call it gradient solid one for background one for the gradient itself I'm going to use circle and just feather it out then create adjustment layer called exposure adjust exposure a bit so that the fall off will be a look a bit more realistic perhaps like this and just stretch the thing out a little bit and color it you can use the default node there's a preset for colorizing stuff I prefer using video copilot color vibrance which is almost the same but it shifts hue a bit depending on the intensity of the light so perhaps it will look a bit better anyway something like this so it's going to be our first gradient save it render out and the second one is going to be the same but it's going to be stretched like this which it has the option to tweak the hue of the hdrim up in the dome light but it can't color it so this gradient should be off some color to begin with so let's go back to VDini and create the light call it light dome zero selector default color space use the duration okay we'll work for now now we can also we should tweak the resolution 1920 by 1080 okay let's render it okay let's rotate the light there we are let's zoom to find some more interesting angle for the camera something like this and maybe create another light and move this one as well tweak the color and move it a bit as well just has some interesting color contrast this is a weird spot okay so we can tweak the globals so probably we can fix these dark parts by increasing the amount of reflection trace depth so let's save this image as a reference point and let's try to get rid of these dark parts such as depth combine 24 hmm so it might look better in some cases but for this particular project it's just not worth it there are drawings increased drastically with these and didn't fix these parts so I'd rather I'd rather tweak the angles of the light so this one is probably from this one I'm gonna leave this part dark yeah I'd say it's a good solution anyway we can continue to tweak the light the blues but it's more of an artistic choice I'd rather fix these things let's switch to the full res render so we can see it better so here is the problematic part because of the lack of the polygons the interpolation of the surface tend to break things up we can change it by just increasing the amount of polygons but not before the noise but rather after it I'd rather not add subdivide here because it can just slow down the viewport and it's not a very convenient thing to do I'd rather use the resolution displacement and just tweak the minimum edge length set it to zero that would mean that all the polygons would be subdivided no matter the size they take on screen and maximum subdivisions six will be just insanely high number we should stick to two kill the screen space adaptive toggle and and try to render again render times will increase but these things will be much more pleasant to look at which is the goal looks kind of nice I'd say so that's it

**Frame:** tutorials\frames\tutorial-glass-donut\frame_000.jpg


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

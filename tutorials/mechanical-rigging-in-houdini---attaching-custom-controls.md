---
title: Mechanical rigging in Houdini - Attaching custom controls
source: YouTube
url: https://www.youtube.com/watch?v=7J-hDF0H6ck
author: cgside
ingested: 2026-06-23
houdini_version: "any modern (H18+)"
tags: [rigging, kinefx, mechanical, controls, wrangle, matrix, fit-range, intermediate]
extraction_status: complete
frames_dir: tutorials/frames/mechanical-rigging-in-houdini---attaching-custom-controls/
frame_count: 4
---

# Mechanical rigging in Houdini - Attaching custom controls

**Source:** [YouTube](https://www.youtube.com/watch?v=7J-hDF0H6ck)
**Author:** cgside
**Duration:** 13m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** So, we will do the remaining of the packing in a bit. For now let's attach some controls to this. So for that I'm going to create in your a net node and create two points. Or we can do a point generate. And generate two points just to be different. They will be at the origin. I can see them. Why I can see my grid? Press age. Let's do a name. And let's name point zero as star get left and point point as star get right. And make sure we set it to points of course. Now we will need a read doctor. This will also be transformed. I think shell has transforms. And now let's just create a sphere. Set it to primitive. And I'm going to change the size to be 0.05. Give it a color. Can be this kind of pool. You can pick any shape. Let's just name it. And this one is need to be on primitive. Let's need to control. Now let's do an attach control. Not attach control is attach. Join geo. Join geo. And let's make sure we don't want to rest both. So let's connect these and this. And let's attach the name target left to control. Let's just do up. And we have two points. If we want different control for each one, you can pick or a different shape. And now let's just do a read doctor. No, read post. And we can enter this and pick target right. Move it to the right target left. Move it to the left. Let's do 1 and 0.5 on y. 0.5 on y and minus 1. Now let's lock this because we don't want to rotate them. And we also want to lock the y and the z. So these are our controls. Now let's attach them to make them interact with our skeleton. So basically we want this controls to rotate the root points. So 1 for each. So that's what we have in here. And instead for now we are doing these read posts. But we want to do this in a different way. So re-gather with triangle. And this one it will be a bit of controls. Let's give it some color and connect this to here. Now we just want to fit these controls to the max angle that we calculated in here. So that's basically what we want to do. But we want to do these for two points. So instead of iterating over points, we can actually iterate maybe over numbers. So just a different way. And we will do end points and input one. So we will iterate twice. So and what have I done in here? I just used these numbers and points input one. So we should have two points. Now let's just use this field to select some points. So it's point six and we can do something like this. And now we can do int on array of the points that we selected. So expand points group input zero. And the group is just the channel string group. Because this one in here is named group. So if we print this. So it's a point we should have six and sixteen. Yeah, that's correct. And now we will do, we will grab the local transform of these points because we want to extract the exposition and then fit it to the rotation might single. And we will fit it between some bounds that already worked for me. So it's a matrix for an x form. And we want we want to grab from the point input one to local transform. And the point number it will be just LM. No, so zero or one in this case because we have two iterations. Now to get the translate text of both we will do get comp and get the from these matrix. We will get this row and this column. And then we will grab the local x form of our points that we selected. So six and sixteen the mirror one. And it will be just so let's name it local x form. And we can copy from here. But in this case input zero and we want to grab this specific point. So either six or four sixteen because we are arriving from this array that we previously selected. Now make single it will be just detail. And we will grab the angle. And we will multiply it by two because we will mirror it. We will basically we bit to the other side. So that's the maximum. And now it's simple. We just set up an angle which will be a fit function between that we will absolute translation X because we might have negative we in one of the so on the left side we will have negative so we will just fit the positive number between I found the value 0.6 and 1.2 on the translation will work well and from zero to the max angle. So this should work and now we can just re rotate the local x form and ingredients we will set the angle and radians we set the angle and then we do it of course on the z axis. All this will do nothing so it will not rotate but what we need to do is set point transform to point that we got I mean because we are working in numbers which is basically detail with the parallel processing. So we will set the local transform and we will just select from the points the current point we want to set so L Lm now. So this is the points and the value we want to set is a local x form that has been pre-rotated in the previous line. So if this works yes now we can select this and within a range we can rotate to the max angle. Now if we look at our re you can see it aligns perfectly and we can come in here and open and close everything. Oops. Okay it might go to the other side so we have to keep the control on this side. But this one in here is not working because we is not working because we haven't bind it to geometry of course. So we have to use this control in here and now we can get rid of this repose and I think the only thing left to do is to capture the remaining two. So let's do that. Just to run and back because this is back geometry let's use name but with color it will make everything better. So let's just now copy do the same for the other side. This should work the same way. So we just need to follow the logic so if you remember so let's add one and the first one we selected was this link and it was 0.0 so now it should be the mirror 0.0. Then we add the second one and this should be 0.6. Let's keep pointing on this and this should be 0.2. And then what else did we do? So we selected this part and we did 0.1. And after 0.1 we have the tree so this one and sorry this one and after that so after 0.3 we have 0.4 which I think is this one. Yep. And finally this one here which is 0.8. Now let's see all it looks. So it seems to be working. Let's just go to the controls. Let's close it and yeah everything should be working guys. Now this also means that we can place a reading here because we have that possibility of for example so let's let's do the following. Let's close this. Let's maybe move them apart a bit and let's come in here. We can also do the following. Select this point and open the flap. And also select this and so this point is kind of not working. Let me see. Oh I'm selecting this one should be this one as you can see it's working. So as you can see we can also control other things and now the idea is you have this base and you can make it better and make it perfect rig with all the controls. In this case we only add two controls but you can add as much as you like. So yeah guys that's basically it for our first lesson on this procedural mechanical rigging course. I hope you have enjoyed sorry for any delays but I had something working and then when I tried to replicate it it didn't work so well so in the end it worked out fine so I hope you have learned something new from this. As always feedback is welcome and you can always contact me and ask me any questions. Don't forget to download the file from this link I will leave a link below and yeah thank you for watching and I'll see you next time.

**Frame:** tutorials\frames\mechanical-rigging-in-houdini---attaching-custom-controls\frame_000.jpg


---

## Structured Notes

### Core Technique
Attaching custom handle-sphere controls to a procedural mechanical rig skeleton using name-based target points. Controls drive joint rotation by reading the control's local transform X translation and fitting it to a rotation angle via matrix manipulation in a detail-level for-each loop (iterating over numbers, not points).

### Summary
Short (13m) tutorial concluding part 1 of a procedural mechanical rigging series. Covers: creating named control points (Point Generate + Name SOP), spherical control shapes (Attach Control / Join Geo workflow), iterating over control count using a number-based for-each (not points), expanding named point groups to get specific joint indices, extracting local transform X position, fitting that to a rotation range, rotating the local xform matrix, and applying it back to the skeleton joints via set point transform.

### Key Steps

**1. Create Control Points**
- Point Generate node → 2 points at origin
- Name SOP → name point 0 as `starget_left`, point 1 as `starget_right`; run over points
- Reposition with Read Post (repose) nodes: move left to (-1, 0.5, 0), right to (1, 0.5, 0)
- Lock translation Y/Z to constrain controls to horizontal X-axis motion only

**2. Attach Control Shape**
- Sphere (primitive type, size 0.05) with color
- Attach Control or Join Geo: connect control shape to named target point
- This binds the visual sphere to each target point position

**3. For-Each Loop (by Number)**
- Iterate over a count (2 iterations) instead of over geometry points
- Use "end points" / input count to drive loop count = 2
- Provides `iteration` value (0 or 1) as a detail attribute on foreach_metadata node

**4. Expand Points Group to Get Joint Indices**
- `expand points group input zero` with group = channel string `group` (the named group)
- This yields arrays of point numbers (e.g., [6, 16]) for left/right joint targets
- Index into array with `Lm` (0 or 1 per iteration) to get the specific joint point number

**5. Extract Control Translation → Fit to Rotation**
- Get local transform of control point (input 1): `matrix xform = local xform(1, Lm)`
- Extract X translation: `getcomp(xform, row, col)` — row/col for translate X component
- Get skeleton joint's local xform (input 0): `matrix local_xform = local xform(0, pts[Lm])`
- Read max angle from detail attribute (pre-calculated skeleton angle) × 2 (mirror)
- Fit: `angle = fit(abs(tx), 0.6, 1.2, 0, maxAngle)` — abs() handles negative side controls
- Rotate local xform: `rotate(local_xform, radians(angle), {0,0,1})`
- Apply: `setpointtransform(0, pts[Lm], local_xform)` — writes back to skeleton joint

**6. Mirror / Second Side**
- Duplicate the control point setup for the right side with mirrored point selection
- Carefully follow point indices: replicate the same sequence (0.0, 0.0 mirror, 0.6, 0.2, 0.1, 0.3, 0.4, 0.8 etc.) for the right-side chain

### Houdini Nodes / VEX / Settings
- **Point Generate** — creates N points at origin
- **Name SOP** — assigns string name attribute to geometry; used for control target names
- **Attach Control / Join Geo** — binds control shape to named target point
- **For-Each Loop (by Number)** — iterates N times with detail-level `iteration` counter
- **Expand Points Group** — expands a named group into an array of point numbers
- `localxform(input, ptnum)` — returns local transform matrix of a point
- `getcomp(matrix, row, col)` — extracts a component from a matrix
- `fit(value, srcMin, srcMax, dstMin, dstMax)` — remap translation range to angle range
- `abs(value)` — handle negative translation (left-side control)
- `rotate(matrix, radians(angle), axis_vector)` — rotate a matrix around an axis
- `setpointtransform(input, ptnum, matrix)` — write back modified local xform

### Difficulty
Intermediate

### Houdini Version
any modern (H18+)

### Tags
[rigging, kinefx, mechanical, controls, wrangle, matrix, fit-range, intermediate]

---

## Related Tutorials
- Part of the procedural mechanical rigging series by cgside

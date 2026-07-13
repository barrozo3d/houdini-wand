---
title: Procedural Favela in Houdini  | Tips and Tricks
source: YouTube
url: https://www.youtube.com/watch?v=Nmnf_3mp1OU
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/procedural-favela-in-houdini-tips-and-tricks/
frame_count: 0
frame_status: pending-selection
---

# Procedural Favela in Houdini  | Tips and Tricks

**Source:** [YouTube](https://www.youtube.com/watch?v=Nmnf_3mp1OU)
**Author:** cgside
**Duration:** 22m48s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py procedural-favela-in-houdini-tips-and-tricks <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in today's video I wanted to show you some new tips and tricks that I will develop while working on this favela like house in Odini.
[0:11] So I build everything procedurally including the texturing that it's still working progress but hopefully you'll get away with some new techniques.
[0:20] So it's hard to find new video ideas since I've done more than 200 videos but I always try to come up with different solutions so I can show you different things.
[0:32] So here's my network and it all starts with the box and let me make sure I disable in here the shadows.
[0:43] So it starts with the box and I want to do some procedural selections. So that was the challenge I faced.
[0:50] Things I didn't want to select them manually and that kind of thing. So the first thing I'm doing is sorting the primitives by why and doing a reverse. So I can always have the primitive zero on top.
[1:02] And that will be handy because I want to do some selections of this corner and these two wedges also. So I'm first selecting the primitive zero and saving it as a base group.
[1:13] And now for the corner select this one that later I will transform down. I am selecting that using Vex.
[1:21] Just by getting constraining the wrangle to that base group the top-prem and making and running a point wrangle I'm making sure I'm selecting only the points on the negative x axis as you can see.
[1:34] So that was easy enough but now I want to select these two edges in here so I can do later the roof.
[1:41] So for that it's hard to select edges in Vex. Most likely you will end up doing for loops. So one thing that you can do is to select vertices.
[1:53] So that's what I'm doing this one. So again I'm constraining to the base group that way I will work on the vertices on that face. Each face has four vertices. I wish quad.
[2:04] So I'm just doing a module in here so every other vertex and saving it as a vertex group as you can see I'm running over vertices and that's a lighting one in here and one in here.
[2:16] And then I can just promote that to edges as you can see and I will get this one.
[2:20] So another trick you can do with this in mind. Let me see I have another shape in here. So I'm basically getting this is for the door.
[2:30] Then I'm transforming dividing and extruding every every other face. Then in here I'm doing the same on the extruded front. So in this extruded front.
[2:41] Oh in this group in here I'm saving it as a group and then I'm running on the wrangle on that on those frames and do every other vertex.
[2:52] But as you can see I added one in here as an offset that will select me those edges that I can later battle.
[2:59] So and you notice that I didn't offset in here if I remove that it will select in here as you can see so that's a nice trick also that you probably know that but just in case that's a nice trick to know.
[3:11] So the main takeaway is to when you want to do add selections we it acts.
[3:17] It's always a good idea to work on the vertices. It's in my experiences much easier.
[3:23] So that was the first tip. Then why am I selecting those two edges because I want to do the roof as you can see if I show you I'm doing the roof in this part.
[3:35] And the way I'm doing that is having that election as you can see I am blasting that primitive and I also have I still have that election so I'm converting it to lines.
[3:47] And then I want to skin with us with the second input so I can easily so then I'm resampling and I'm skinning the two lines.
[3:57] And this way with the second input which I'm creating from the start points of those two lines I can now resample it and have a subdivision control so I can come in here and change the length of the resample and I can do the same in here so I can even have only perfect quality if I want if I set the same amount.
[4:21] And yeah the main takeaway is the skin with the second input. And the way I'm creating those lines by the way so I have these two as an input then I'm feeding that to the first input of this wrangle that I'm running over numbers for the amount of frames I have which is two so I'm running these two iterations.
[4:40] Then I'm just getting the beginning of the premium by using premium V so at UVW zero and at the UVW one and then just adding those those two points and it will add for each curve so at the beginning we probably could have done a curve but I didn't think of that in that situation so that's why I'm doing this then just adding by skipping every end point in this case too.
[5:05] So yeah the skin node with subdivisions that's the thing now what's next this was the second tip now I ended up not using this part but I still think it's a nice return so I'm merging basically I'm creating in here some cement on the corners of the house.
[5:26] And it was a cool way I think so I'm getting the base and converting another edge group that I saved in here so is this one so I have another group in here called sides that I'm selecting by normal so along the X and the Z and making sure I include the opposite direction so it selects all the way around so I'm excluding the top and bottom frames.
[5:50] Then I can run the same wrangle as you can see vertex number model 2 and select that and promote that to edges and I have those edges so I'm converting that to line in here then resampling and re projecting to the deform geo I wanted to deform the only corners of the base geo so I'm re projecting to have the silhouette correct.
[6:15] Then I'm running this wrangle which is creating the following normal attribute so N1 and N2 maybe there are easier ways to do this but basically I'm creating those two normals so I can extrude them I can extrude along that direction.
[6:34] Let's see how I'm creating those normals.
[6:37] So I'm getting the current position which will be a premium the center point of each line of each primitive so we have four frames and I'm getting the next one so premium number plus one can be at the center can be at the bottom doesn't matter.
[6:55] Then I'm just normalizing the position so subtracting the next the current position from the next and making sure I normalize and remove any distortion along the Y then adding a random number and doing a rotation for the second normal so if I don't do this I won't have that so I'm just rotating we can we can't just invert we need to rotate the initial normal.
[7:22] So we just subtracting one position from the other and creating the direction vector and then I'm doing 90 degrees rotation for the second one and then it is we just extrude along that specific normal so you can see I'm doing point normal attribute N1 and in here doing the same but N2 then I'm merging and doing some VDB operations and whatnot and we end up with something like this.
[7:50] But in the end I used instead well I'm still doing it but I used instead a normal map or maybe I can transform it to a night map it will be easier maybe so I ended up not using that specific part but it was something I wanted to show you.
[8:12] What else do we have in here? Still control bevel so yeah this is not very interesting so this is the second edge select and I wanted to show you in here the window creation.
[8:27] So I have the geometry to copy to do the the bullions in here to bullion out the window and the door so I'm just doing a connectivity measure the volume or can be area sorting by sorting the primitives by that attribute and then splitting in here the smallest one so just wearing the primitive zero the attribute at the primitive zero this way I always know that the window cuts.
[8:56] So I know for sure this is the window and this one is the door because it's bigger so for the window I'm picking it a little bit and splitting the by normal the Z and inverting so I get the frame the silhouette or whatever you want to call it.
[9:15] Then I'm dividing 13 times on the Y as you can see in here and two times on the X grouping in here the by the angles so I get the interior ones and converting it to line and from here I'm doing this division because I want to create those things on the window are they called I don't remember.
[9:38] So then I'm splitting in here by the making sure I'm splitting the ones at the middle at the middle that are exactly at the middle so by using centroid and position X those are the center and those are the edges for the center what am I doing in here I'm scaling it a bit down with the primitive property as you can see then I'm skinny and creating the thickness so that's the middle part and in here I'm creating these different things.
[10:08] I don't remember how they're called so I have the edges in here then I'm doing a copy because I need an extra one and this is a bit over complicating things but basically I have to let me show you in another view so can we check this so this is a bit hard to see but I have the edges in here and I want to create center points from those edges so that's what I'm doing in this wrangle.
[10:36] Running by numbers by getting the bounding box and calculating the middle point then from here I can copy we will need another one for the extremities so I'm just in here reading that point attributes and saving the doing like a class attribute in here so each row gets a different ID and that way I can read the point number the point position using that in line attribute let's say an offset.
[11:06] I'm doing the position wide hopefully that was clear then I'm doing here a skinny so creating this but before that I'm also doing a rotation and some scaling and making sure I reverse every other primitive because I needed that for the skin so far for the skin to work you have to have proper winding order and also proper primitive sorting
[11:34] and then I'm just using a thick and so that was my window and also doing the framing here just with the poly extrude so just a different way to do the window then I'm doing also the door in here I believe yes and the next thing I wanted to show you is the wrinkle deformer because I've done a bad bad video about the wrinkle deformer because I'm doing it the wrong way
[12:02] so let me show you in here what we have in here so I first in here so if you notice in the final geometry I have these towel or whatever this is these ropes on the top of the roof
[12:20] and I'm not simulating anything or I'm doing the wrinkle deformer that is some sort of simulation but basically I'm starting with a grid doing the obvious subdividing and transforming it so I can copy the points at the rough location I set basically by drawing the point with the draw points HDA that we have done before in the channel and then just copying the point.
[12:43] So that's one thing then I'm adding a mountain to add some distortion to it and add another mountain in the rest geometry so in the rest input of the wrinkle deformer and I'm also doing a VDB for the collision because I need a collision shape for the wrinkle and doing the wrinkle deformer as you can see and in here I'm just increasing the constraint iterations to have a better output and increasing also the wrestling scale.
[13:12] So usually this input is the one that you want to distort a little bit and this one I'm just distorting because I want some unevenness along the edges so it's not straight but this one should be the rest really flights and I was doing the other way around so that's what I'm doing in here now properly and in this case I am just increasing a bit the collision the SDF offset and then just picking it up it down because the VDB is just a little bit more accurate.
[13:42] It will create some volume and offset a bit the shape and in this case I'm not picking by normal I'm picking by a custom normal that I saved in here so basically after you'll be sampling the normal from the roof as you can see I'm saving that as a custom normal this way when I have as you can see if I pick it by normal it will be a mess but I have in here so if I can show you a custom normal that is aligned with the points that I
[14:12] used to copy the geometry I can pick just in that custom direction which is uniform and it won't distort the geometry just move it along.
[14:21] So yeah now I also have some normal manipulation in here what am I doing?
[14:27] So yeah I'm doing the same wrinkle deformer to create in here some some bags of trash bags so really easy just doing a mountain to have some distortion to play with in the geometry to deform
[14:41] and having the rest geometry I just scale it down so the wrinkles kind of let me get rid of these kind of stretch a bit and I can even stretch it a bit more.
[14:54] So if I increase in here this as you can see I'm creating those wrinkles on the trash bag so we can dirty but I'm also manipulating the normals in here so let me see.
[15:08] Yeah I'm doing a double cross product and creating the normals for the exclusion and also adding some randomness so it extrudes more in some areas and less in other areas so I can actually show you that normal.
[15:23] So basically it's the double cross product to have the normals pointing along the geometry yet and yeah I'm randomizing the normal along the edge that way I can extrude it properly.
[15:37] Otherwise it will extrude to the sides as you can see I'm using this custom normal if I use edge normal well in this case edge normal would work the same but I wouldn't have the randomization so yeah now I think I covered everything I wanted to cover and now I'm going to show you a bit of the texturing of this so let me come back to here.
[16:02] So let me see so first of all I'm creating a ramp and then quantize it just one color and in the ramp I'm doing repeat and change the number of cycles then I'm remapping the height values because I need to play with those and doing a simple scatter shapes scatter.
[16:24] And in this case I'm changing the scale and the stretch so I can easily Yobi sample to the tile pattern that I'm doing the bricks with and this way I have each rig to have the same pattern then doing a multiply to get back to the black background so I can mix in here some cement.
[16:48] And that's basically what I'm doing in here so after calculating also the rasterizing some curves so I'm going through this pretty quickly but basically I have some curves in Yobi space that I'm rasterizing with these new rasterized curves then doing a dilation with the radius mask which is just a noise.
[17:09] And as you can see this will look something like this on the geometry so I'm also using that to do some blending of some grout.
[17:21] So let's see in here I'm doing some some dilation transforming a bit to the correct shape and introducing that cement mask.
[17:33] And then I have the grout that I created with this bubble noise or the cement wherever you want to call it and I'm doing a night blend in here so if I look at the height so this is not correct this is the mask I want to look up I know why.
[17:54] Yeah, it's because of this so I'm blending in by height this is an I blend similar to substance painter and honestly I did this based on a blender video but what this does I can show you I can disable input texture and do this offset basically it will blend the height it will blend to it maps based on of course the the height of each one.
[18:22] And you can change a bit the softness and what not that's basically what is doing in this case I'm inputting a texture to have a custom mask around I will show I will share the everything on patron so you can have a look on there a lot of projects is not finished yet.
[18:37] So then I'm doing an item normal and I'm not even doing this placements and for the texture is pretty simple for the albeit is pretty simple I'm just taking the item app multiplying by a fractal color at noise.
[18:51] That's mostly it then from the tile sampler I'm fetching the ID doing a random one and doing an adjust we adjust to change a bit the levels and yeah then I'm doing yet another noise in here and blend oh yeah I'm blending that the ground in here with this noise to have like a cement texture.
[19:15] So I guess that is basically it guys as always you can grab the full project on my patreon and I will try to finish this I'm also doing some edge damage in here but that's I've done that before in the channel so there's nothing to special about it.
[19:34] Maybe I can show you how I did this wire if I remember how I did it so I'm doing the antenna where in here so this is my antenna but let me press age so I'm doing that at the origin I wanted to show you how I did the placements of this wire.
[19:53] So basically I'm building the antenna and I'm selecting after the resample of the initial line I'm selecting some points so this is the point where the wire will connect at first and that will propagate as you can see when we do the copy to point so I still have it here although we're selecting all the geometry but that doesn't matter.
[20:14] Then I'm doing yet another object margin here to create the pole and doing again some point selection in this case the last point so end points minus one and I'm doing this one is manual so I'm just inputting the point tree and when I transform it I will have one point here and one point there.
[20:35] So then I can blast away those areas and extract the centroid and I will have the three points for the wire that I can just add and if you're looking here those are the three points that I saw on my reference so the initial one is one in here and I'm just transforming the bottom one to where I want it so I can move it around as you can see.
[20:58] Converting to line doing a small resample polypads what am I doing in here I'm selecting oh this one is interesting because I'm doing in here a custom attribute called you and basically I don't want to move those points I want them I want to keep them really stuck to those areas so I'm doing a custom you wet your boots where the corner points so since I have only I resemble these two segments.
[21:28] So I can have on each different segments I have one point in the middle and I'm doing these point number module tools so what the corners I always have zero value as you can see and one in the middle this way I can add more points and resample by polypads and do a simple mountain with the blends with that attribute this way I will always keep those points stuck on the initial position and that's what I'm doing as you can see.
[21:57] So the mountain that I'm using to add some distortion it will always stay on those areas otherwise if I don't do the blend it will move too much.
[22:08] So yeah guys hopefully you found these useful as always you can grab the files on my Patreon please let me know your opinions in the comments I don't ask for anything other than.
[22:18] Some support on Patreon and if you want of course if you want to download the files then watch custom videos video tutorials but you're on YouTube I always like to hear your comments and your opinions as always grab the files and find out how I did all of these to get put all of this together to create these nice cozy house.
[22:43] So thank you for watching and I'll see you next time.



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

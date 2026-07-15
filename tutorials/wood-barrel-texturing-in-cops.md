---
title: Wood Barrel Texturing in COPS
source: YouTube
url: https://www.youtube.com/watch?v=O6T5eVYJHsA
author: cgside
ingested: 2026-07-13
houdini_version: "20.5.319"
tags: [cops, copernicus, uvdist, texture-paint, rasterize, karma, wood, rust, texturing]
extraction_status: complete
frames_dir: tutorials/frames/wood-barrel-texturing-in-cops/
frame_count: 17
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Wood Barrel Texturing in COPS

**Source:** [YouTube](https://www.youtube.com/watch?v=O6T5eVYJHsA)
**Author:** cgside
**Duration:** 36m22s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back. So in this video we will be doing the
[0:04] texturing of this wine barrel. Some of you requested in the comments. We still
[0:09] have to work a bit on sobs but it will be quick and then we'll get straight
[0:13] into cops and do some basic texturing. So yeah let's get into it. So we will
[0:20] start where we're left off. We have the obvious and we have the modeling then.
[0:24] And I want to create an attribute so later I can add some rust around the
[0:29] leaves. Oops. And so for that after the soften normals. So in here we have the
[0:35] oops. And I'm gonna just increase a bit the subdivision to two and measure the
[0:41] curvature. So measure curvature. You will have to have labs for this. And in this
[0:48] case I'm gonna just need the convexity and I'm gonna just multiply it to five and
[0:56] the blur amount to let's see how that looks. And this is not showing us the
[1:01] true values. So I'm gonna go in here and change this. What is? I believe is
[1:08] infrared and the rest is fine. I can just set min and max so we can check the
[1:14] full range. And from here I want to increase this the
[1:20] attribute so it plates out a bit. So for that I'm gonna use an attribute blur.
[1:26] And I'm gonna blur this. So I'm gonna select the convexity and I'm gonna
[1:35] blur it eight times, eight iterations. And then I'm gonna create an attribute to
[1:40] just float. And in this case I want to blur the convexity. A blur no.
[1:47] Increase and set it to multiply. And I believe I used a value of three in this
[1:54] case. But you can increase it and it will grow the the mask. So in this case a
[2:00] value of three will do. And I believe that solve for now. So I'm gonna just
[2:09] disable the visualization. Call it this out.
[2:13] Barrel. And it's a good idea to file cache this. So we sometimes
[2:20] Odin likes to calculate all the nodes again. So I'm gonna just call it barrel.
[2:25] Oops. Barrel. Cache. And save this to this. Just a single frame of course. Then
[2:35] we will get into cops. Okay let's create a cop network. And we will
[2:43] copy this control C. And go with a sub import. Use external and paste it. So now
[2:51] we could restore this like restaurant setup. Move it to UV space. And then
[2:59] restore the attributes. But that will lead into some issues that have been
[3:05] addressed before by people like Rowan Dalvi and others. So like the the bleeding
[3:12] of the edges will create some issues. So for that instead of doing the
[3:17] restaurant geometry setup, I'm gonna use a wrangle to resurrect the attributes.
[3:20] It's nothing complicated so wrangle. And it will be a good chance to learn
[3:26] something new possibly. So I'm gonna disable this. Introduce geometry input and
[3:33] connect it in here. And I'm gonna also add another one and set it to UV and
[3:39] call it UVs. And let's see. We first need to create a UV in a UV texture in
[3:49] in texture space. I mean. So for that I'm gonna use the relative bounding box
[3:55] and you will see how that looks in a bit. Just stay with me in here. So we're using
[4:02] the relative bounding box and now we can just say that that component will be
[4:07] equals to zero. And if I assign this so if I assign this to the UV attribute
[4:19] so we at UVs it will be equal to set and we need to set a vector to. So in this
[4:27] case I'm gonna say UV.x and UV.y I believe yes. And you will see how that
[4:37] looks. So this is the output and the UVs. So it just creates a UV in a UV map in
[4:43] texture space, not image space which is from minus one to one. So but we actually
[4:50] want to sample the attributes using the premium V so we will need some sort of
[4:54] function for that. You can use xyzdst function but I'm gonna use instead the
[5:02] UVdst just to be different. So I'm gonna create the necessary variables so
[5:07] you-prem and vector UVW and create the UVdst function. So you-dst and I'm gonna
[5:18] use UVdst and you want to sample the input one. Use the input one I mean then get
[5:26] the UVs from the mesh, get the UV from these nodes and then we just need to use
[5:33] u-prem and UVW. And then to control the padding I'm gonna call it padding. I'm gonna
[5:40] use a channel float and call it padding. So this just controls the distance and
[5:48] that will work and then we can just say vector UVs. It will be called the premium
[5:55] UV so we can sample the UVs now. So UV and it will use the u-prem and UVW. And now if we
[6:07] assign this to the UVs, so set UVs.x and UVs.y we should be able to see
[6:17] if we create the padding and let's say a value of .1. So as you can see we can
[6:22] increase the padding. This way is easier to control because I have some some parts
[6:30] that are really close to each other so being able to control this distance is
[6:34] always nice. And then we just have to restrise all the other attributes so I'm
[6:40] gonna create a few. So in this case there will all be monos. So barrel. Oops, let's
[6:49] create. So there's no this setup in here and the other one will be the groups. And we have
[6:55] another one that will be barrel tops and we will also need an ID which will be
[7:00] the premium ID that we created in the first video. And we also want the RGB in this
[7:05] case or HP. And I believe that's all. Let's see the assignments are correct and
[7:10] now we can just copy this. This premium function and we can say F to barrel and
[7:15] we can sample the barrel. Let's see if that is working so barrel. Yep. And then
[7:20] we just need to copy and paste. This is a bit tedious but it's always nice to have
[7:24] that control over the reading of the texture of the attribute. I mean, oops. So let's
[7:29] copy these and let's do the other one. There are all tops. So there are tops and we just
[7:36] need a few more. And I forgot one in this case. I want to wait in here. The convexity
[7:39] if you got something to do. So let's wait in here and let's see if you can just stop
[7:42] from here. And that's another one in this case will do the premium ID. So it needs to
[7:46] be an integer. And finally the the pH of the position. So in this case it will be a
[7:50] factor and we call it HP and we need to sample the position. Okay, let's see if that works.
[7:55] Barrel, oops. Convexity. That's fine. Barrel tops, premium ID and position. Yeah. So this
[8:05] will work for now and we will continue in the next part. Okay, now let's import a texture
[8:12] that will be the wood based texture. If you were expecting me to create the wood pattern,
[8:18] I'm sorry to disappoint you, but we will be using some sample some some wood sample texture.
[8:27] So I'm going to set it to RGB. I'm going to color correct it a bit and you can do that with
[8:33] HSV adjust. And let's see how I introduced value shift.
[8:40] It can be a little to be a bit more radish. I also increase the saturation.
[8:52] And also the value. So 1.3 something.
[8:58] So you can see the difference. It just gives a it's just a bit more vibrant, let's say.
[9:03] And now we can sample this. So sample image in this case texture sample and we will connect
[9:10] the so the UVs that we have in here connected to the UV and connect this to the texture sample.
[9:18] But there is no texture. Sorry, it's no, it's texture. But let me see.
[9:25] We actually need if we assign this, let's see. Let's create the preview material and assign
[9:35] this to the geometry. So, GEO and connect this to the base color. You can see the scale is
[9:44] getting as blurry texture. So we might want to scale it a bit. So let's just use the UV transform.
[9:51] And let's see our texture sample and the UV transform. I'm going to scale it by 5.
[9:59] And you can see we start to get more detail. And I'm also going to offset this randomly.
[10:07] And set the seat. I have a seat of six, but you can play around with it. And if we look at
[10:12] the result now, we start to see something. And let's see if we can increase this.
[10:21] And maybe play with this. And we start to have a bit more resolution. And at the end,
[10:26] we will set it to 4k. So we actually wait for that. And we might need to enable and disable.
[10:34] You can see we start to get a good quality out of it. But for now, let's keep it okay.
[10:40] Let's refresh. Force the refresh. So we have the texture sample.
[10:47] Now we want to create some variation on it. So for that, I'm going to introduce
[10:54] another HSVHS. And for the mask, I'm going to get in here the primary D. So primary D
[11:06] and introduce random mono and connect this to the seat. So that's our first variation.
[11:14] And let's set the seat to 51 for now. And connect this to the HSVHS. And now we can play
[11:23] we can play with the value. And it will affect according to this mask.
[11:28] And in these HSVHS, I'm going to increase the saturation a bit. So 1.15, something like that.
[11:36] I have some values I'm following, but feel free to get creative. And in the value, I'm going to
[11:41] increase this something like this. So you can see the difference. And we will yet, we will introduce
[11:51] another color variation. So in this case, we will use another random mono and change the seat.
[12:02] This time, I went with a seat of 47. And let's connect this to the HSVHSHS. And let's see
[12:11] our results. And of course, we need to change the values. So in here, I use the same saturation
[12:19] scale, but reduced this to 0.5 something. So we start to get this variation. So the first one
[12:32] introduced a bit more value and saturation. And this one darkens some of the parts. And this is
[12:38] all based on the the gray scale values we have in here. So it doesn't look like much right now,
[12:44] but hopefully it will look a bit better at the end. So let's stick with this one. So
[12:50] and now. So now we will create the text that goes in here that says RAM. So for that, I'm going to use
[13:02] a font. And let me see which values I used. So in this case, I'm going to use a custom font
[13:08] that I've found. So I'm going to paste it in here. And if you want to know which font it is,
[13:15] is this 10 cell standard bolt. And I'm going to say and change this font size to 0.5 something.
[13:28] And the rest is fine. I'm just going to create a null. And connect it in here and say out logo.
[13:40] And now we need to find a way to project this onto our barrel because we can't do it in
[13:47] texture space, as you can see, because they are all scrambled. We don't have a continuous
[13:54] UV map, let's say. So for that, I'm going to use, since it's just a gray scale, I'm going to use
[14:02] the texture paint nodes if it works because sometimes it's a bit bloody. So let's try that. Let's
[14:10] create a texture paint. And in this case, I'm going to increase the resolution to 4K.
[14:15] I'm going to set the mode to stamp. And also decrease the soft edge. And I need to copy that
[14:24] path. So let's copy this and paste it in the alpha, alpha image file. Let's see if that works for us.
[14:35] I'm still loading. And I need to set OP, the OP syntax. Let's see. And it's working.
[14:46] And I'm going to increase the size with control shift. But as you can see, this gives us some
[14:52] some soft edges, although I decrease that attribute, that parameter. So I'm going instead of
[14:58] using space rule, I'm going to use screen. And as you can see, that doesn't give us any issues.
[15:03] Although it might get you some strange distortions if you're working in some angles.
[15:08] So I'm going to change to the front view. And I honestly don't know which size I use. I'm going to
[15:13] just beat it randomly. So maybe in here. And I'm going to use the mouse, since the welcome tablet
[15:20] might introduce some opacity variation, which I'm not sure why is that doing that because I don't
[15:28] have any options in here. So I just use the mouse. And we have this. And now we can create an all.
[15:37] And in here, as you can see, we have the indexor space. And I'm going to call and this is the volume.
[15:44] So we can import it into cops. So I'm going to say random, drum projection.
[15:51] Go back to cops. And we can have these in here. We don't need it anymore. But let's keep it there.
[15:58] And now I'm going to stop import. So stop import. Use external. And get the top. So
[16:11] oh, sorry. I need to copy it again. And then paste it in here. So that is working. But it's in
[16:22] the zero to one space. We need to restore this. And if you guys know, as you can see, if I introduce
[16:28] a restaurant setup and set it to UVs, it will somehow read those UVs. I'm not sure how I can extract
[16:34] them because I could extract those UVs and basically build a projection tool. But I'm not sure
[16:42] how to do that. So for now, we'll just use geo to layer. So geometry to layer. So we can have
[16:50] well, an image in here. And now it's simple. We can just create in here. Let's see. I blend.
[17:02] We will connect our ground image. Let's see how that looks. So we also need the,
[17:11] since it is a black and wild file, we can or layer, we can introduce the masking here.
[17:17] And let's see if that is working. And yeah. And it might look low-res, but if we increase this
[17:23] to 4k, let's see if that calculates properly. And we might need to disable one of the nodes. And
[17:29] we have a bit more texture. And I'm also going to set this to overlay to have some of that
[17:38] texture bleeding and reduce the opacity to 0.7. And with the, when we introduce some bump,
[17:45] this will work a bit better. So let's change it again. This. So I don't have to compute all the graph
[17:56] every time. So let's see what we will do next. So let's play a bit with the roughness to get a
[18:05] better visualization of this material. So I'm gonna duplicate this, set it to mono, since we're
[18:12] really introduced some roughness. And I have the roughness texture in here. We might want to play
[18:18] with a remap, with just the values to work a bit better on the viewport. So in this case, I played
[18:26] quite a bit. So 1, 6. So something like this and introduce some of that brightness.
[18:40] You will have to play around and see how it fits. So now
[18:47] we will use the same setup. So texture sample. And it's important to sample the same
[18:56] UV transform and UV attribute. So let's sample this. And we have it here. Now let me see.
[19:07] This is a big network. I have to constantly be looking at it. So
[19:15] and let's connect it like it is right now. And we will do any necessary changing changes later.
[19:23] So let's connect this to the roughness and see. And we start to see some variation.
[19:31] It's maybe compute the 4K. And you can see hopefully it's going through the recording. And
[19:40] I don't want to risk it to compute this at 4K while I'm recording because it might crash.
[19:47] And this is after all a better feature. Now we will do some ship
[19:59] bump mapping or normal mapping. So straight out of this
[20:05] this roughness texture, we will do an item normal.
[20:09] And let's set the scale really low point of one.
[20:21] And let's connect this to the normal. And we will need to reduce the amount.
[20:27] And we will reduce the amount of the normal.
[20:33] So it will look better at higher resolutions. But let's keep like that for now.
[20:38] I might increase this just to see how it looks.
[20:44] And we have to do this. So it's looking okay. Just getting a bit slow. Let's reset it and see.
[20:51] Okay now it's a bit faster. I also want to introduce some overall distortions with another texture.
[20:59] So let's get another one in here. In this case I'm going to use a roughness one. So let's copy these.
[21:11] And I'm going to use a mega scans roughness texture that I found on the library. And I'm going
[21:19] to sample it again. And I can use the same UV transform. In this case I didn't use the same
[21:30] UV transform, but let me see what I changed in there. So it's basically the same.
[21:40] And we can give it like that. Let me see the result.
[21:43] Yeah, it's similar enough. So we'll keep the same UV transform. We could duplicate it and change the
[21:52] seeds to have more variation. But in the end it won't make much difference. So let's copy this
[21:59] item normal. And let's see how that looks. And we will change this. Reduce quite a bit. So point
[22:08] to zeroes of five. And let's blend. I'm not sure this is the correct way of blending normal maps.
[22:17] But I'm just going to change blending here and change this to overlay. Seems to do the trick. So
[22:24] why not? Now let's see how that looks. So let's start to introduce some some overall scratches and
[22:34] what not. Now let's change this again to 2k because I'm not feeling very confident about this.
[22:41] And let's see what else. Now we need to create the material for these oops because the other parts
[22:52] are basically done. We have the color variation, the specular or the roughness and the bumpiness.
[22:59] And now we need to create these material in here. And I'm just looking in this case, I'm going to do
[23:10] something really cheap. So I'm going to get this texture in here. And the monotone RGB.
[23:21] Let's see how that looks. And I want to change this. And I have a color in here. So I'm going to just
[23:32] create a single color if I can delete this one. And I'm going to use this color in here.
[23:37] Just some saturation on the reds and a bit of value. So a really dark color.
[23:43] And I'm going for now connect it. Connect it in here. So after this plans, I'm going to use another
[23:53] plans and connect this in the diffuse or the base color. And I believe I need to use some
[24:03] attribute in here. So in this case, the oops. I hope those are called oops because I don't know
[24:11] the name in English. So yeah. And that starts. As you can see, we have some similar. But in the end,
[24:17] with an higher resolution, you won't really notice it. And I also'm going to keep the bumpiness and
[24:26] change this specular, but keep the bumpiness of the previous texture, which is not the correct way
[24:31] to do it. But you know, in the end, it doesn't look half bad. So right now, we want to use that
[24:40] complexity attribute that we have to introduce some rest in here is going to be really ship rest.
[24:47] But you know, it's what I am able to do. So with a file node, I'm going to get some resting
[24:57] metal. And I believe the other textures are from Megascans. And this one, I believe, is from
[25:04] Polyaven. So we just some, yeah, it's not very good, but it's what I found honestly.
[25:11] So I'm going to repeat this texture using the X-style. So connect these to the inputs. And there's
[25:16] no tends to be a bit buggy, but let's see, I'm going to scale it quite a bit. So 13, introduce some
[25:24] rotate random. So one and play with a fall off and reduce the weight exponent to blend a bit
[25:34] more. It won't be perfect, but and change the random seat to some value.
[25:43] I'm afraid this will crash, honestly. I've been having so many issues with Odinulately.
[25:48] It's not even fun. So let's you be sample this and we can get the same UVs, why not?
[25:57] And the X-style. So it will look something like this. It's not pretty, I admit, but it will work.
[26:09] So if I want to color correct this, I just should be color correct, right?
[26:18] But I'm going to use a 358 value in here to get a bit more red, decrease a bit the saturation,
[26:26] and increase the value scale. Maybe not so much. Something like this will do.
[26:35] And now let me see my file. So we will gather that convexity, it's convexity, yes.
[26:50] And right here we will remap it. So it looks something like this, but we want to remap it a bit.
[26:59] So it doesn't have that those gray values. So something like this will be fine. And then we want
[27:12] to create a fractal noise, fractal noise 3D. And we will need the position. So that's why we
[27:21] back the original position to make this noise style. And what we will do in here. Let me see what I
[27:28] have changed in this fractal noise. So we can increase a bit. We will use this noise to break
[27:37] this uniform pattern. So we doesn't create the rust everywhere on those hard edges.
[27:44] And let's keep it like that for now. Now I want to multiply this.
[27:52] And let's see how that looks. So let's write away, connect this.
[27:58] So we have, I'm lost right now. So we have this one. And now I want to blend.
[28:08] We will connect this as the backgrounds. And where is the rust in here?
[28:13] Connect these as foreground. And we will use this masking here. So it's a bit of a mess. Sorry about that.
[28:21] I get lost in my own notes. And then we can connect these. So yeah, we can connect these in here.
[28:32] Let's see. Yeah. See how that looks. So should be doing something. It is doing something,
[28:41] but we need to increase the effect. So after the noise, I'm going to pause the recording and be
[28:48] right back. So we need, you can see we have that attribute in here. Let me change the flat shading.
[28:54] So we have that resin here, but it's not looking any good because we need to distort it and deform it
[29:01] a bit. So we will create yet another fractal noise with the same position attribute. Let's change
[29:08] the center to zero and signature to RGB. I believe that's it.
[29:16] No, we need to change this to UV and change the center to zero. So we have a zero, zero
[29:22] centroid of sets. So negative values and positive values. I'm going to change this a bit to 1.5.
[29:30] We can adjust it later and an amplitude of zero one. Or let's keep it default and see how that
[29:38] looks. And after the multiply, I'm going to use that distort, place it in here and use that
[29:46] noise we created for the direction. So let's see, oh, we need to increase the scale quite a bit.
[29:57] So let's set it to max and let's decrease this amplitude to point we can just play with the
[30:02] amplitude as you can see. And I'm going to change it to point a one. So I believe this will be enough.
[30:10] Let's see. So as you can see, it starts to bleed out from the edges. And
[30:19] we might want to play here with the contrast of this noise. So we can create a remap.
[30:28] Let's see. And we will do point or and let's bring it together to like point six. So we have
[30:38] something like this. Let me see if I play it with the offset. You can always play with that. So let's see
[30:48] if we play with the offset, it will give you a different output. So I'm going to set it to default.
[30:54] So we introduce this remap, which helps to contrast the effect. And again, this is a really
[31:00] sheep way of doing the rest. Let's maybe play with the distort. So let's see. But that's just real
[31:11] give us. So maybe I don't want us, I don't want to spend much time in here. You can play with that
[31:18] and have a better result. I'm just giving you some information. So you can play with your own file.
[31:28] Okay. Now I believe the only thing left to do is to play with a metalness.
[31:39] So after this distort, we will create an invert node or a complement.
[31:49] And this will act as our metalness and we will also need the oops layer and create an
[31:59] node. So this is it. And we will remap this. And let's see, I'll just look by default. Let's create a
[32:09] multiply. And let's see. So we want to remove the metalness from the rest and just keep it on the
[32:22] oops on the remaining on the black part. So we can actually remap this to be 0.4 to have
[32:32] make sure it doesn't create the metalness in there. And finally, we can just do a small remap
[32:39] to lift the to reduce the metalness. So in this case, I use a value of 0.8 for on the white levels.
[32:48] Or so let's connect this to the metalness.
[32:55] Does this have effect? It does. And it looks better, as you can see.
[33:02] So I'm going to risk it and set this to 4k. Let's hope it doesn't crash.
[33:09] And it's calculating. Let's reinforce it. So it looks much better. Hopefully you can see it
[33:15] in the recording with all the compression. And it's a bit slow, of course. And what can we do next?
[33:28] So we might want to reduce the specular on the rest. That will look a bit better. So for that,
[33:36] let me see here. I'm going to blend the original roughness texture. So where is that?
[33:44] So let's create a blend first. And it's in here. No. So it's in here. So let's copy this.
[33:55] Let's connect this to the background and use this rough texture, where is the distort in here?
[34:03] This is a mess. And connect it to the background. Let's see how that looks.
[34:08] And we need to set this to multiply. I mean, we need to set this to max.
[34:19] And let's see. And that will create the right roughness value for the rest.
[34:27] And let's connect this again to the roughness and see. And looks like I have a crash.
[34:35] So sorry about that. We will create again another blend node and connect the roughness that is
[34:44] in here. And I should probably label this and connect this to art and reconnect the roughness.
[34:56] Let's see if that doesn't crash and it doesn't. So I made something wrong. I need to change this
[35:03] to max, of course. So as you can see, the rest doesn't have that much specular now.
[35:14] So I believe this is done. I'm going to leave it here. And if you want to
[35:22] elaborate from here, create more distortions and apply some more texture variation. And of course,
[35:29] we can go back and change the seed of some of these. So as you can see, you can change the
[35:36] UV, the seed of the UV transform. Let's try another one. So this one is nice. And we also have
[35:46] it in here. The same texture. You can add some variation. And I think that's all guys.
[35:53] Thank you for watching. And if you want to grab the file, I will be uploading it to Patreon
[35:59] right now. And you can also get some courses in there, some exclusive tutorials and all the project
[36:07] files from my videos. So make sure to check that out. And other than that, thank you for watching
[36:13] and sorry for the rainbow. And I'll see you next time. Bye.



---

## Captured Frames

- [0:40] tutorials/frames/wood-barrel-texturing-in-cops/frame_000.jpg
- [2:10] tutorials/frames/wood-barrel-texturing-in-cops/frame_001.jpg
- [4:10] tutorials/frames/wood-barrel-texturing-in-cops/frame_002.jpg
- [6:40] tutorials/frames/wood-barrel-texturing-in-cops/frame_003.jpg
- [9:10] tutorials/frames/wood-barrel-texturing-in-cops/frame_004.jpg
- [10:50] tutorials/frames/wood-barrel-texturing-in-cops/frame_005.jpg
- [12:30] tutorials/frames/wood-barrel-texturing-in-cops/frame_006.jpg
- [14:10] tutorials/frames/wood-barrel-texturing-in-cops/frame_007.jpg
- [15:50] tutorials/frames/wood-barrel-texturing-in-cops/frame_008.jpg
- [17:30] tutorials/frames/wood-barrel-texturing-in-cops/frame_009.jpg
- [20:00] tutorials/frames/wood-barrel-texturing-in-cops/frame_010.jpg
- [22:30] tutorials/frames/wood-barrel-texturing-in-cops/frame_011.jpg
- [25:50] tutorials/frames/wood-barrel-texturing-in-cops/frame_012.jpg
- [27:30] tutorials/frames/wood-barrel-texturing-in-cops/frame_013.jpg
- [31:40] tutorials/frames/wood-barrel-texturing-in-cops/frame_014.jpg
- [34:10] tutorials/frames/wood-barrel-texturing-in-cops/frame_015.jpg
- [35:50] tutorials/frames/wood-barrel-texturing-in-cops/frame_016.jpg

---

## Structured Notes

### Core Technique
Texture a wine/rum barrel with scrambled, non-continuous UVs entirely in **Cops** by avoiding the typical "Restore Attributes" workflow (which causes edge-bleeding artifacts) in favor of a hand-written **`uvdist()`**-based sampling wrangle that reads any SOP attribute directly by UV position with a controllable padding distance, then layering wood texture variation, a hand-painted logo (via Texture Paint stamped in Screen mode), procedural rust (Fractal Noise-masked, curvature-driven, UV-distorted), and metal-hoop materials — all composited with Blend/Layer nodes before feeding Karma's base color, roughness, normal, and metalness inputs.

### Summary
Back in SOPs, a **Measure Curvature** (Labs) convexity attribute is multiplied and heavily blurred (8 iterations) to create a soft rust-origin mask around edges, then file-cached to avoid Houdini's node re-evaluation overhead. In Cops, rather than the standard "Restore Geometry"-to-UV-space workflow (known to cause edge-bleeding artifacts, as documented by others in the community), a custom **wrangle-based attribute-resurrection** approach is used: a UV attribute is built manually from the relative bounding box (Z component zeroed) to place the mesh in texture space, then a second wrangle uses **`uvdist()`** (chosen over `xyzdist()` "just to be different") with a controllable **padding** channel parameter to sample any SOP attribute — barrel piece ID, top/bottom group mask, primitive ID, position, and convexity — directly by UV proximity, each individually Rasterized into its own Cops layer. A sample wood texture (color-corrected via HSV Adjust for a redder, more saturated look) is sampled using the UV attribute through a **UV Transform** (scale ~5, randomized offset, seed) for tiling control, verified live via a Preview Material assigned to the geometry. Two additional HSV-adjust layers, each masked by a **Random Mono** keyed to the primitive-ID attribute (different seeds), introduce per-plank color variation (one brightening/saturating, one darkening) blended together for a non-uniform wood look. The barrel's branded text ("RUM") is built from a **Font** node (custom bold font) — but since the scrambled UV space prevents direct texture-space placement, it's instead **hand-painted onto the 3D geometry** using **Texture Paint** (4K resolution, Stamp mode, alpha image set via `op:` syntax to the rendered logo, blend mode switched from Screen — chosen because Space mode introduced soft-edge bleeding even with soft-edge reduced) directly in the viewport (front view, mouse rather than tablet to avoid unwanted opacity variation from pressure sensitivity). This painted output is imported back into Cops via **Geometry to Layer**, restored using the same UV-distance technique, and Blended (Overlay, reduced opacity ~0.7) into the base color as a masked layer using its own alpha as the mask. Roughness comes from a duplicated wood-texture sample remapped for contrast, combined with an Item Normal-derived bump (small scale ~0.1) and a second, Megascans-sourced roughness texture (via a separate UV Transform) blended (Overlay) for additional surface-scratch detail. A cheap "hoop"/metal-band material reuses the wood texture converted to a single dark-red constant color for base color, blended with the barrel's overall texture, while procedural rust is built from the convexity attribute (Remapped), a position-driven **3D Fractal Noise** (to break the uniform edge-hugging rust pattern), multiplied into the mask, and further distorted with a second UV-centered Fractal Noise fed through a **Distort** node (direction from the first noise, tuned scale/amplitude) so the rust "bleeds" organically from edges rather than sitting in a hard uniform band — contrast-adjusted via Remap. Metalness is derived by inverting/complementing the distorted rust mask, remapped and multiplied to concentrate metalness only in non-rusted areas, and roughness on rusted regions is separately blended down (Max mode against the base roughness texture) to reduce unwanted specular highlights on rust. Final resolution is pushed to 4K (with intermediate 2K checks to avoid crashes/slow recompute during the session), and seeds on the UV Transform nodes can be varied for quick texture-variation exploration.

### Key Steps
1. **SOP prep**: after Soften Normals, Subdivide (2), run **Measure Curvature** (Labs, convexity output), multiply (~5) and heavily blur (8 iterations) to create a soft edge/rust-origin mask; grow the mask further with an Attribute Adjust Float (multiply ~3); File Cache the result as "barrel_cache" (single frame) to avoid repeated recompute.
2. **Cops import + UV-space placement**: Sub Import the cached geometry; build a UV attribute manually via the **relative bounding box** (Z component zeroed, assigned to `uv.x`/`uv.y`) instead of using the standard Restore-Geometry-to-UV workflow (avoids known edge-bleeding artifacts).
3. **Custom attribute sampling wrangle**: using **`uvdist()`** (input 1, the mesh's UV attribute, `u_prim`/`uvw` outputs) with a **padding** channel-float parameter to control sample distance, then sample and assign any needed SOP attribute (`vector uvs = ...`) at that UV position.
4. **Rasterize each attribute into its own Cops layer**: barrel piece ID (mono), top/bottom group mask, another ID (integer, primitive ID), position (vector), and convexity (float) — each rasterized separately via repeated copy-paste of the sampling wrangle pattern.
5. **Wood base texture**: import a sample wood image, color-correct via **HSV Adjust** (redder hue shift, increased saturation and value ~1.3), sample it with **Texture Sample** using the built UV attribute run through a **UV Transform** (scale ~5, randomized offset, tunable seed) for tiling control; verify live via a **Preview Material** on the geometry base color.
6. **Per-plank color variation**: two additional HSV Adjust layers, each masked by a **Random Mono** keyed to the primitive-ID layer (different seeds, e.g. 51 and 47) — one increasing saturation/value, one decreasing value — blended together for non-uniform wood coloring.
7. **Logo/branding**: build text via **Font** (custom bold typeface, size ~0.5), Null it out; since scrambled UVs prevent direct texture-space placement, **hand-paint it onto the 3D geometry** using **Texture Paint** (4K, Stamp mode, alpha image via `op:` reference to the rendered logo image, blend mode Screen instead of Space to avoid soft-edge bleeding), painting in the front viewport with the mouse (avoiding tablet-pressure opacity artifacts).
8. Import the painted result back into Cops via **Geometry to Layer**, restore it using the same UV-distance sampling technique, and **Blend** (Overlay, opacity ~0.7) it into the base color using its own value as the alpha mask.
9. **Roughness/bump**: duplicate the wood texture sample (Mono), Remap for contrast/brightness; add **Item Normal** bump (scale ~0.1) from the roughness texture; blend in a second Megascans roughness texture (separate UV Transform, similar settings) via Overlay for additional scratch-like detail.
10. **Hoop/metal-band material**: reuse the wood texture converted to a single dark-red **Constant** color for base color, blended with the barrel's overall texture; use an **X-Style** tiling repeat node (scale ~13, random rotation, fall-off/weight-exponent tuning, random seed) for a metal-tile-like texture pattern, color-corrected for a redder/darker metallic tone.
11. **Procedural rust**: **Remap** the convexity attribute for contrast; build a position-driven **3D Fractal Noise** to break up the otherwise-uniform edge-hugging rust pattern, multiplying it into the convexity-derived mask.
12. **Rust distortion**: build a second, UV-centered Fractal Noise (RGB signature, zero-centroid offset, tuned scale/amplitude) fed into a **Distort** node using the first noise's direction — makes rust visually "bleed" from edges organically; **Remap** afterward to contrast the effect (values compressed toward ~0.6).
13. **Metalness**: invert/**Complement** the distorted rust mask, Remap (white level ~0.4–0.8) and multiply so metalness is concentrated only in non-rusted regions; connect to the shader's metalness input.
14. **Roughness cleanup on rust**: Blend (Max mode) the base wood roughness texture with the rust mask so rusted areas don't retain unwanted high specular/shine.
15. Push final Cops resolution to **4K** (checking at 2K intermediate steps to manage recompute time/crash risk), and vary UV Transform seeds for quick per-render texture variation exploration.

### Houdini Nodes / VEX / Settings
Measure Curvature (Labs, convexity), Attribute Blur, Attribute Adjust Float (mask growth), File Cache; Cops: Sub Import, relative-bounding-box UV-attribute wrangle, `uvdist()`-based attribute-sampling wrangle (padding-controlled), Rasterize (per-attribute layers: barrel ID, group mask, primitive ID, position, convexity), Texture Sample, HSV Adjust (×3+, base + 2 color-variation layers), Random Mono (primitive-ID-keyed masks), UV Transform (scale/offset/seed), Preview Material, Font (SOPs), Texture Paint (Stamp mode, `op:` alpha reference, Screen blend), Geometry to Layer, Blend (Overlay, Max modes), Item Normal (bump), X-Style (tiling repeat with fall-off/rotation), Constant (color), Remap (×several, contrast/metalness tuning), Fractal Noise 3D (position-driven, RGB signature), Distort (noise-direction-driven), Complement/Invert (metalness derivation), Multiply nodes (mask combination).

### Difficulty
Advanced (the `uvdist()`-based attribute-resurrection technique for scrambled/non-continuous UVs, plus the hand-painted logo workaround and multi-layer procedural rust, are all substantial production-level Cops techniques).

### Houdini Version
20.5.319 (visible in viewport title bar).

### Tags
cops, copernicus, uvdist, texture-paint, rasterize, karma, wood, rust, texturing

---

## Related Tutorials
- [The Donut Tutorial in Cops - Houdini 20.5](the-donut-tutorial-in-cops-houdini-205.md) — related Cops procedural-texturing tutorial from the same channel, using similar Rasterize/Blend layering techniques.
- [Tiling Patterns with COPS and SOPS](tiling-patterns-with-cops-and-sops.md) — shares the same Cops-based texturing workflow and stamp/rasterize approach applied to a different material.
- [Procedural Pizza in COPs](procedural-pizza-in-cops.md) — another SOPs-to-Cops resurrection pipeline, here building a stamped leaf topping instead of barrel-grain detail.
- [Tips and Tricks to level up your Houdini Skills](tips-and-tricks-to-level-up-your-houdini-skills.md) — shares the exact same uvdist()-based attribute-resurrection wrangle technique, applied there to a salmon-pattern sushi texture.
- [Scatter Shapes in Cops Randomly Without Overlap](scatter-shapes-in-cops-randomly-without-overlap.md) — shares the UV-gradient-based custom transform-matrix approach for building per-piece Cops workflows.

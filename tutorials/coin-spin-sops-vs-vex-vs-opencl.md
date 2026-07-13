---
title: Coin spin | Sops vs Vex vs OpenCL
source: YouTube
url: https://www.youtube.com/watch?v=AGTOukqBmhU
author: cgside
ingested: 2026-07-13
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/coin-spin-sops-vs-vex-vs-opencl/
frame_count: 0
frame_status: pending-selection
---

# Coin spin | Sops vs Vex vs OpenCL

**Source:** [YouTube](https://www.youtube.com/watch?v=AGTOukqBmhU)
**Author:** cgside
**Duration:** 37m9s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py coin-spin-sops-vs-vex-vs-opencl <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone and welcome back.
[0:02] So in this video we will do an Eglarsize of this coin spin, both using only stops, then
[0:08] moving in 2Vx for a medium difficulty, and then an advanced version using only OpenCL.
[0:15] So this is supposed to be just a learning Eglarsize and nothing too serious, but I'm confident
[0:19] that you will learn quite a few techniques, so yeah let's get into it.
[0:22] Okay guys, I just imported the coin model that I downloaded from Sketchfab.
[0:27] I will leave a link in the description if you want to follow along, it's just this simple
[0:30] model of the scanned coin.
[0:33] And as you can see it's kind of offset from the origin, so the first thing you want to
[0:38] do is to apply the correct transforms to move it to the origin and rotate it.
[0:43] But also I would like to apply some the texture, so for that let's create a UV quick shade
[0:50] and let me see where I have the texture.
[0:54] So it's right in here and let's have a look.
[0:58] And as you can see we don't get the correct result because we don't have UVs or we have
[1:04] UVs but it's called ST because this is a USD file as you can see.
[1:08] I just removed the time dependency and make sure that I unpacked the polygons.
[1:13] So let's fix that, let's first of all clean most of these attributes, not clean, sorry,
[1:18] attribute delete.
[1:20] Now let's delete everything and keep the normal, the position and the ST and the remaining
[1:26] things we can delete.
[1:28] So let's name this clean.
[1:30] And after that we can just do a attribute swap.
[1:35] And this is ST's on point, so let's move the ST zero to UV.
[1:43] And now we have to UVs, we can have a look in here.
[1:47] And now if we do a UV quick shade we should get the correct result but we don't because
[1:52] for some reason these UVs are inverted.
[1:54] So let's quickly fix that.
[1:57] In this case I'm just gonna use a wrangle because it's simpler.
[2:00] So let's just name it fix UVs and I know that is just inverted on the Y direction.
[2:08] And I also know this is the float too.
[2:10] Usually in Odin is a tree float, so a vector.
[2:13] But in this case is a float too, so we do you at UV dot Y multiply by minus one.
[2:22] And let's see as you can see it move it down because it didn't rotate around center.
[2:26] So a quick fix is just add on the Y one.
[2:32] And we get these results and now if we look we should have the correct texture.
[2:37] So that's one thing fixed.
[2:39] Now let's go to the easy mode where we will do the result of the transforms.
[2:45] So with the transform we will rotate it 90 degrees around the Z axis.
[2:50] So 90.
[2:52] And then we will just use a match size and move it to the mean and to the center.
[2:59] So I think that's about it.
[3:01] And now we have the correct effect.
[3:04] So this is the easy mode and now let's go to the medium which will involve a bit
[3:09] of text.
[3:10] So let's create a wrangle.
[3:12] And we're just warming up.
[3:14] It will become a bit more complex in a bit.
[3:17] So result transforms.
[3:20] And this one it will be pretty simple.
[3:23] First of all we will move it to the center.
[3:26] So V at B minus it will get bounding box center input zero.
[3:32] And now it's at the center.
[3:33] Now we need to rotate it and a quick way to rotate it.
[3:36] We could use a matrix.
[3:37] But I'm going to use a quaternion.
[3:39] So vector four with declared the variable then we create a quaternion.
[3:45] And we need to specify an angle.
[3:47] So in this case I want to rotate it 90 degrees.
[3:49] So we spy divided by two which with this global variable by underscore two.
[3:55] And then we need to specify the rotation axis.
[3:58] So in this case is around that.
[4:03] So we rotate around that.
[4:05] Then we just need to rotate.
[4:06] So V at B it will be equal to q rotate.
[4:10] And we rotate with that quaternion.
[4:13] Sorry.
[4:14] V at V at B.
[4:17] q rotate we rotate that quaternion.
[4:21] And affect the position.
[4:24] And now it's rotated 90 degrees.
[4:25] But as you can see we have a well-chating issue because this transform actually transforms
[4:31] all the attributes including the normals and vector attributes and whatnot.
[4:35] But this one doesn't know we need to do that.
[4:39] So we need actually to specify we want to rotate also other attributes.
[4:43] So what we can do is just do V at N, q rotate by the same quaternion and rotate around N.
[4:49] So and how the normals are fixed.
[4:51] So this is a nice trick to know.
[4:53] And now we just need to move it to the mean bounding box size because right now is that
[4:57] the so as you can see this one is moved up.
[5:01] But this one is not.
[5:03] So we need to in this case we can get the size.
[5:07] So for example, or we can specifically grab size.
[5:12] Grab the depth.
[5:14] So in this case it will be get bounding box size.
[5:18] And we can just grab the x axis.
[5:20] So because if you remember this is the depth that we want to grab.
[5:24] So this is actually the x axis.
[5:26] So if we grab that depth we can just move it up.
[5:30] So V at V dot y plus equals depth.
[5:34] And we need to if we do that it will move the by its full light but we just want half.
[5:40] So we just want 0.5 so or divided by two.
[5:43] And now we get exactly the same result.
[5:47] So that was the medium one.
[5:50] Let's create a switch.
[5:53] So we have an option to pick any any of the inputs.
[5:58] And now let's do the hard mode which will be based on OpenCL.
[6:02] The problem with OpenCL is that we don't have these bounding box functions that we will
[6:07] need.
[6:08] So what we can do if we have a look in here at the original geometry we can go to the
[6:13] geometry spreadsheet, go to detail and found in here an intrinsic called bounds.
[6:19] These are just some attributes that come by default with the geometry.
[6:24] And this just tells us the bound if we combine these values we can get the bounding box
[6:29] mean the bounding box max the center and that sort of that sort of values.
[6:36] So if I create in here a wrangle and I actually show you something I have in here.
[6:41] So where is that bounds bounds details.
[6:44] So you can grab the minimum the maximum just by swizzling out the different values.
[6:49] We can get min max size which is just max minus min and the center which is this expression.
[6:54] So we'll do the same with OpenCL.
[6:58] But again this is an intrinsic attribute.
[7:00] So we can actually as far as I know read intrinsic attributes in OpenCL.
[7:04] So what we can do is just grab a detail wrangle.
[7:07] So let's go to detail and just write that intrinsic attributes to one attribute.
[7:15] So let's call it bounds and it's just detail in intrinsic and we run from the first input
[7:21] and the name is just bounds.
[7:24] So now we know we have in here the bounding box input.
[7:29] And this is just a detail.
[7:30] So we'll cost us nothing.
[7:32] So as you can see it's there and we also have the intrinsic but we can't read intrinsic
[7:36] with OpenCL.
[7:38] So now let's actually go through the code.
[7:42] So let's create an OpenCL node.
[7:44] Let's just name it resets transforms.
[7:49] And let's connect in here.
[7:52] And by default this is binding position and make it writable.
[7:56] And what we do in the kernel is just reads that position and just set the position.
[8:00] So this is basically a pass through.
[8:02] We can leave these by default and just remove all of these.
[8:07] So we just have the kernel that will execute the code and we have the bindings in here.
[8:11] So we actually want to this will run if we go to the options.
[8:16] This will run on the first writable attribute.
[8:18] So position is a writable attribute by using this symbol in here.
[8:22] So we are running over all the points in this case because position is a point attribute.
[8:27] There are other cases where we will run over detail but that will come later as an example.
[8:33] So if we are trying to replicate this so we are running over points and we are affecting
[8:38] position but not only position also normal.
[8:40] So we actually want to write to normal.
[8:43] So let's actually write to normal.
[8:49] Yeah, that's basically it.
[8:50] And we also need to read the detail attribute of the bounds.
[8:53] So bind detail because it's a detail attribute named bounds and it's a float array.
[9:00] So far no errors.
[9:02] And now we're just going to copy these from here just to be quicker.
[9:06] Let's bet we need to translate it to open CL.
[9:09] So we know that CL is not a vector.
[9:11] It's a float tree and we don't have a set function.
[9:14] We need explicitly to write float tree and we need to write add bounds and do the same
[9:21] in here and the same in here because we are reading from that attribute.
[9:26] And let's make low three and we don't use set.
[9:29] We just place it explicitly float tree and bounds and let's do the same in here.
[9:37] Let's see if that doesn't ever route it doesn't.
[9:40] Now we need the center, so float tree center which will be just 0.5 and we need to specify
[9:48] an F for float and we multiply it by mean plus math.
[9:53] So this is the bounding box center.
[9:55] Then we also need size, so float tree size is just max minus mean.
[10:01] And that's about it.
[10:03] Now we need to affect position.
[10:05] So let's do it in position variable in here called post and we just gonna do hb minus
[10:11] center.
[10:12] So move to the origin.
[10:15] The float tree sorry this will error out.
[10:18] So that is correct float tree.
[10:20] And then we need to create a quaternion and for that there is an include provided by
[10:27] side effects which is quaternion dot h which is another.
[10:30] So let's do include in here and let's speak.
[10:35] Ternion dot h we could have done with we could have done it with matrices but just to.
[10:42] I was just experimenting because I never use this quaternion other so I just wanted to know
[10:47] how to do it.
[10:48] And in order so we need to create in here a quaternion.
[10:51] So in order to create a quaternion the function as a strange name but basically you define
[10:56] the quaternion type and we name it let's say q and then we do q from.
[11:04] X is angle q from axis angle and then we define the rotation amount of the angle so that
[11:12] will be m by doing open sea also 90 degrees out by and then we need to specify the rotation
[11:21] axis of let's define a vector tree a vector.
[11:25] So a flow tree which will just be 0.0 f and 1.0 around the z axis.
[11:33] So that is not everything else and now we just need to rotate and is the same function
[11:38] so we just rotate the position that that is already at the origin and we do q rotate
[11:43] the same way rotate the ternion and the last argument is the position and then we just
[11:51] move it so pause dot y so we move it to the base of the grid plus equal in this case
[11:57] is size size dot x multiplied by of 0.5 f so open sea all is a bit low level in that sense
[12:08] and if we apply this so at b dot that's to apply to the position attribute since we
[12:14] are writing to position we should have it move it there but as you can see the normals
[12:20] are weird again because we also need to do the normals so load n equal to q rotate rotate
[12:29] the quaternion and at n and now we just need to do the same in here at n dot f and q
[12:42] oh I miss something in here yeah bomb not another score float with an expression go float
[12:51] tree oh float tree sorry float tree and now is this the exact same result as this so we
[12:58] just resetted through the transforms with open sea all so if we look now we have the one
[13:04] with the just default subs then vets version and then open sea all so let's do the rest
[13:09] in the next part so now we will do the coin spin using just sub operator so just top notes I
[13:17] mean so let's start with the circle to create the axis where the coin will rotate around so let's
[13:23] create a circle let's make it around the exit plane let's make it open arc because we just want
[13:29] to extract the point let's give it 32 divisions let's fuse so we need to compute the normal or the
[13:38] tangent we need actually to be fused because it will be open by default and let's just do a match
[13:44] size to match it to the size of the coin but we want to transform the coins with within packed
[13:52] primitives so we don't want to transform all the points just use packed primitives just because
[13:57] it will be easier to work with so let's create an all let's name it out coin and let's create a pack
[14:05] and we can leave just default settings we just have one coin and now let's create a null
[14:10] and let's name it out from in fact and now let's connect the near the match size and let's visualize
[14:19] the coin and let's just do scale to fit and feed it to the min so now the coin is there and the
[14:27] circle is at the bottom of the coin so if we look in here something like this okay now let's create
[14:34] a null and let's name it circle circle and what we can do now is to compute the tangent
[14:44] so orient a long curve and let's just name it tangent so then and let's visualize that attribute
[14:54] it's just a tangent around the curve so we can do the transforms around this and now we will
[15:01] extract a point and animate it around so with a curve we can just do extract points and as you
[15:07] can see it will keep that tangent that we will need and the animation is pretty simple we will just do
[15:13] a time and we will set so we will set the frequency which in this case will be 5 and we just reset
[15:21] it again so it goes between 0 and 1 always and it doesn't decrease with time so we just
[15:27] multiply 1 and if we have a look we have something like this and as you can see it's all it always
[15:34] has that tangent that we need now we could have done this with a transform though nodes maybe
[15:39] a default transform node but I couldn't get it to work so what I use is this node called transform
[15:44] axis I never used this node before so I just learned about it and what we can do in here is just
[15:51] set the origin a direction to transform from and the rotation angle for examples so let's do the
[15:57] origin it will be fine it will be just this point we could have used the center the centroid
[16:02] but in this case I'm gonna use just a point expression so input 0.0 is just one point want to grab
[16:08] the position and we also want to grab the x axis so the x components and we will do the same for
[16:16] the y and for the z and now we need to grab the direction which in this case will be the tangent
[16:24] so let's copy this we need the x do y and z and now we need to specify an angle
[16:33] and the angle the angle will be minus 40 that's the amount of rotation I want and I will just
[16:41] multiply it by time so I just want to create an animated offset for the rotation so it starts a
[16:48] full at full rotation and it decreases to 0 so for that I'm gonna do at time divided by the
[16:55] duration which will be three seconds and let's put that between brackets and we also need to
[17:01] start at one so I'm gonna do 1.0 minus that offset and we also need to keep it between 0 and 1 so
[17:08] we will just do clamp between 0 and 1 and if we look now it won't look like much but when we
[17:19] copy the impact coin so object merge and we do an attribute copy and we need to specify near
[17:27] that we want the output the x form and we do a attribute copy near and we want not the cd but
[17:34] we want to do x form and let's be explicit and now we do a transform by attribute
[17:43] and if we look now we should have the animation of the coin so that wasn't too hard right
[17:51] just a few expressions that we had to use but is mostly pretty easy to follow I think so let me
[17:58] just grab in here 72 frames so we get the full animation so maybe 96 to add some offset so as
[18:07] you can see it's working now let's go this was the easy mode let's go to back so now let's do the
[18:15] backstreet version was grab a wrangle and we want to run over points and let's name it coin spin
[18:21] and this will just replicate what we have done in here with all these nodes so with a simple wrangle
[18:28] we can do that so let's connect it to the back primitive and it's always a good idea when you
[18:33] have back primitives to loading the although we will this is just an identity matrix because we
[18:38] haven't done any transforms and we just packed it but it's always a good idea to grab the back
[18:43] transform so the initial transform so let's do matrix transform is just get get back to get back
[18:51] transform input 0 primitive 0 so we just have one coin and next we will need a few variables to
[18:58] replicate all these time cycles duration we will just create parameters for that so for time we will
[19:06] just upload time channel float time now we will do the same for cycles so this one in here which is
[19:15] the amount of revolutions let's say so float cycles not cycles render channel float cycles and we will
[19:25] also need the duration so float duration and will be just a channel float called duration
[19:33] we will also need the size around X so we can create the circle and transform it properly so vector
[19:40] call it radius but it's really a radius but it's really a diameter in here so just get
[19:46] rounding both sides so in this case I will just grab everything so it's not really radius is
[19:53] size so let's me change that to size and now we will let me show you first how we will create the
[20:03] circle and extract a single point so there's a function in back there's a family of functions
[20:08] called sample circle sample direction and whatnot so what we can do in here is to create the circle
[20:16] a uniform circle or a unit circle is to create a near pause let's call it sample
[20:22] circle edge uniform this one creates a circle and we need to specify to fit in a UV value in this case
[20:32] just a UV value and that UV value it will be just from 0 to 1 so this is a uniform value that we
[20:39] need or a random value that we need to to place in here so if I just do random I add ptnum
[20:46] and we just create int point at point 0 pause you will see the point in here so this is a point
[20:58] on the unit circle but around so this is a uniform so but around xy plane so instead of fitting a
[21:08] random value we will be the value between 0 and 1 which will be based on time times the amount
[21:16] of revolutions and we just need to module to 1 so module 1.0 and we need to create this virus let's
[21:25] name circles to 5 duration to 3 and time just at time and now if we'll look at that and we assign
[21:37] this as you as you can see we will add the unit circle in there but in this case is around the xy
[21:49] plane we need to fix that so for that I'm just gonna add it to pause to be equal to in the x
[21:55] axis can be pause dot x in the y it should be 0.0 because we want around xy plane and we can just do
[22:03] in the in the x axis pause dot y so we just swivel and now it should be so it's a bit hard to see
[22:11] we can see it in here so now it should be around this flight grid so in that plane but we also need
[22:18] to multiply it by the size by the radius I mean so multiply it by size and let's put this
[22:25] between brackets multiply it by size dot x in this case and we just want the radius so alpha
[22:32] and now it's it's moved to the edge of the coin now we need to compute the tangents and the
[22:38] tangents will be pretty simple we just need vector and it will be a normalize and we will just let
[22:49] minus pause dot z 0.0 around y and pause dot x and if I assign that to the point so z point
[22:59] attribute 0 the point number now the attribute let's call it 10 let's wrap the point number and
[23:10] let's just set it to 10 now we can actually see it so we can see the tangents is correct so the
[23:17] same way as we have in here as you can see but we don't want we don't want this point this was
[23:23] just for visualization now let's create the rotation so for that after we have let's see we can
[23:34] just create the angle first of float angle and we could create a parameter but I'm just gonna
[23:40] just gonna do it in here manually so I'm just gonna do it in here minus 40 degrees and then we need
[23:51] to multiply by our animation which will be angle times it will clamp and we do time
[23:59] divided by duration just like we have done before and we subtract from one and clamp it between 0
[24:08] and 1 there might be other ways to do this I just found this way once well and now it's simple
[24:14] we create the matrix so matrix and dx 4x4 matrix and we do an identity and we create an identity matrix
[24:24] we translate the matrix so by minus pause so we translate it to the origin and let's actually set
[24:34] back transform 0 0 and we do transform multiply by matrix so we just move it to the that's
[24:46] pivot point to the origin and now we do the rotation so the rotation so let me actually we need to
[24:54] rotate around the tangent so rotation will be rotate the matrix by the angle and around the tangent
[25:03] now we have this but we want to translate it back so we want to do it around the origin so let's
[25:09] do plus pause and now we should have the same effect so as you can see this is exactly the same
[25:16] thing as we have done in subs and yeah that's about it and now we can let me just create a switch
[25:26] and you can see both versions are so let me actually creating your guides the whole time you can see
[25:36] both versions are pretty responsive so as you can see but let's move into OpenCL next to finish
[25:43] off the video so now we need to replicate the same but in OpenCL so let's read an OpenCL node
[25:50] but we will face a few issues first of all after we back the points we no longer have that
[25:54] bounds attribute so let me actually switch to two and I try to transfer it in here but I have no
[26:01] option to transfer the bounds and if I do it explicitly I I couldn't get it to work so we need to
[26:06] transfer back or to read back so for that I'm gonna connect the first input to the back transform
[26:11] and the second input to here where we have that bounds detail attribute so we can read from the
[26:15] second input and also we don't have an X form we don't have an X form attribute so let's just
[26:21] initialize that in a detailed wrangle so let's name it oops in it X form and it will be detail
[26:29] and let's just name it for at X form it will be just items so it could grab the fact transform
[26:35] that just let's just do it like this then in this OpenCL we will work with time so we need to go
[26:41] to the options and include time and we don't want to run over points in this case or in the point
[26:48] attribute we just want to run over the X form so let's grab instead let's delete this
[26:55] and let's run over the detail attribute and right to it X form and it's a float in this case float
[27:03] 16 because it has 16 valves and as you can see it's reading if it doesn't find that attribute
[27:08] it will error out as you can see so invalid attribute so that's fine it's always good to check
[27:14] now we need to grab the bounds so bind detail bounds and it's a float array and it's from input it
[27:23] was the one so from the input one if we set it to zero it won't find so as you can see
[27:30] so that's fine now we just need to create the same parameters we have done in here so in this case
[27:35] I'm just gonna create two so we will bind the parameter code so and we name it cycles let's make it
[27:44] alternative let's say and name it float so this just doesn't error out if we don't create
[27:52] if we call the parameter right away and we haven't created it might error out so I just make
[27:58] it always optional so this is optional parameter I like to do like that you don't have to do it so
[28:03] let's name this one duration and let's create those parameters and cycles will be five and the
[28:11] three you can change for everyone now we have included time so let's pass that as a variable is a float
[28:19] and let's just do it that's the global variable now we need to do the same in here so let's just grab these
[28:28] and paste it in here and we don't need the center we just need size and it's not erroring out we
[28:36] have the bounding box mean bounding box max and bounding box size now let's do the same
[28:44] we have so in openCL we don't have the sample edge uniform so we will have to create it so let's create
[28:52] manually so let's do float turn it will be with it will be time times at cycles and we need to
[29:04] mod it by one so f mod and 1.0 and now we need to multiply it by by by alpha i mean and no by 2
[29:19] by and multiply by two so it's 2 pi so a full rotation so m by f is a full rotation
[29:27] and then we need to specify the radius also so float radius it will just be in this case
[29:34] size dot y multiplied by 0.5 so half of it because in here when we define these bounds a little
[29:43] attribute the radius is actually around y as you can see so the coin is rotated so we didn't write
[29:52] the bounds in here we could have right to the bound in here but we didn't so let's do size dot y
[29:58] so this is different from size dot x because in here it's already rotated
[30:04] so that's fine and now let's do let's have a look in here at this sample edge uniform so the
[30:10] unit circle in this case which what this function is creating is just this expression cos angle
[30:16] seen angle so we will create that in openCL because we don't have that function so for that let's do
[30:22] float tree cos is just equal to float tree and we do cos of turn we do 0.0 at far
[30:38] on y and sin turn and we just need to multiply it by the radius so that's correct and now we need
[30:47] the tangent which will be the same as vets of float tree 10 we just normalize and we do
[30:55] float tree minus cos dot z 0.0 and cos dot x so the exact same thing as the vets version
[31:07] as you can see but we near we use set and what else we need to create the animation so let's do
[31:15] float decay it will be just clamp and we do time divided by duration and as always we subtract one
[31:27] so 1.2 minus this and we clamp it we clamp it between 0 and 1
[31:36] oops this should be okay and now the thing is in in openCL we only have matrix and a quaternion
[31:45] other but we have no translate around origin and rotate functions I think there's a rotate 2D
[31:51] but I don't even know how to use it so we will have to do some tricks in here first of all let's
[31:58] create the same we did in here with this quaternion so let's actually copy this
[32:06] and let's create a quaternion from the rotation so what q quaternion from x is angle
[32:16] and we want to rotate not 90 degrees but actually 40 like we have done before we can change
[32:23] and we want to rotate and we want to multiply it by the animation so decay and we want it around
[32:31] the tangent so 10 let's see if that errors out so oh we need to include the quaternion dot h
[32:40] the other so we need to write some F in here so quaternion radians F
[32:59] minus 40 let's do dot so times decay tangent
[33:10] so we just need a little refresh so it's not evering out is correct so now we need to do that
[33:20] true we have a quaternion so let's make a matrix for out of it so for that I'm gonna create a
[33:25] mat for and let's name it rot and it will be a quaternion for to quaternion to mat or we feed the
[33:35] quaternion and write to the matrix so the matrix is rot that's correct and what we need to do now
[33:47] so this rotation is happening around the origin and we need to compute the offsets so we can
[33:54] mimic the same effect we have in here so translate it around that pivot so for that we will find
[34:00] where toss lands after the rotation around origin so for that we will do a float tree
[34:12] rotate the toss and it will be the the vector multiplied by the matrix so mat for
[34:21] vac tree malt and we will multiply by the matrix rot and the position so the position of the
[34:30] point in the circle so mat for vac tree malt not malt so of malt that's correct so we found where
[34:41] that position lives now and what we can do is compute the offset so floats t it will be equal to
[34:47] pause minus rotate the pause
[34:55] so floats tree sorry I always forget and now if we apply that to the matrix so add x form dot set rot
[35:08] and we transform by attribute as you can see we have the rotation but is not happening
[35:16] is not happening at that origin so we don't have the same result as this so as you can see
[35:22] so we need to actually to affect the translation so we have done this computed the offset
[35:29] so it mimics the rotation around that pivot and we now we just need to write to the to the
[35:35] translation columns so for that we can do rot dot sc it will be equal to translation x so this
[35:40] is a bit low level I don't like it but I didn't find another way so if you have another way let me know
[35:46] and this will be translation dot y and rot dot sc it will be translation dot z and now if we look
[35:55] we should have the exact same result as we have with backs and we subs so the exactly same result
[36:04] so that was quite a bit and I hope I did a good enough job explaining sometimes these are for
[36:11] me too so I understand you might not fully understand it at first but hopefully with these examples
[36:19] you can learn something from it so that was my goal to show you different ways to do things in
[36:27] Odini so as you can see the performance is about the same with sobs with vex and with openCL
[36:33] this might be a bit overkill to do with the openCL to be honest but again this was a learning
[36:37] exercise and nothing more than that I'm not saying openCL is better it's supposed to be faster
[36:42] because runs on the GPU but then again fax is also pretty fast and compile notes the sub compile
[36:49] notes are also fast so I just wanted to show you some alternatives as always you can grab exclusive
[36:55] tutorials on my patreon alongside with all the project files from my videos including this one
[37:00] that I'm gonna post there so yeah thank you for watching I hope you have enjoyed please let me know
[37:04] your opinions in the comments and I guess I'll see you next time



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

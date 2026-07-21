---
title: Forgotten Metal Knowledge | Vray, Cycles, Arnold..
source: YouTube
url: https://www.youtube.com/watch?v=uz8PIi3ELJg
author: Lucas
ingested: 2026-07-20
houdini_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/forgotten-metal-knowledge-vray-cycles-arnold/
frame_count: 0
frame_status: pending-selection
---

# Forgotten Metal Knowledge | Vray, Cycles, Arnold..

**Source:** [YouTube](https://www.youtube.com/watch?v=uz8PIi3ELJg)
**Author:** Lucas
**Duration:** 30m21s | 13 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py forgotten-metal-knowledge-vray-cycles-arnold <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Introduction [0:00]
**Transcript (timestamped):**
[0:00] Today we're gonna take lessons from 2008 Ironman and see how seemingly common in master materials still have a lot of secrets to share.
[0:07] Let me introduce to you Reflection Tape Off.
[0:15] So a while ago I was rewatching Ironman and something in the mark 2 suit up scene code my eye.
[0:21] I posed and I looked closer to make sure I wasn't hallucinating and there it was, a dual reflection.
[0:26] I thought that was bizarre, why would there be two reflections?
[0:29] Usually you have a single roughness value or a roughness map and that's it.
[0:33] Now the mark 2 and mark 3 suits do have some fingerprints that create extra specular layers,
[0:38] but that wasn't the case here.
[0:40] Both visually and narratively this was pretty clean and brand new metal.
[0:44] Knowing Ironman's reputation I figured they had to be right and that I was missing something about how real metal behaves.
[0:50] So I did some digging and I found a photo of the practical suit used in that same sequence and I was stunned.
[0:56] The dual reflection was there too.
[0:58] It was harder to spot because the physical suits finish is quite brushed,
[1:01] but when you zoom into the cleaner area you can clearly see a sharp distinct core reflection paired with a soft faded falloff.
[1:08] I want to be absolutely clear about what I'm talking about here.
[1:11] I'm specifically interested in those seemingly secondary reflection added on top of the main one.
[1:16] You can clearly see that what is being reflected remains pretty sharp
[1:19] and yet you can also see that there's a huge tail off that goes way beyond the initial reflection.
[1:24] Where the colors of the subject are dark, the surrounding reflection is bleeding on top of the first one
[1:29] and darkening the surroundings and when what's being reflected is bright,
[1:33] it's almost like it's glowing and this is reflection tail off.
[1:37] Now if the sound of multiple reflections onto a metal shader don't sound completely bogus to you,
[1:42] let's look at the standard metal shader.
[1:44] You set the metalness to 1, you choose a roughness value or plug in a roughness map
[1:48] and let's get a little crazy and add some anisotropy as well.
[1:51] Despite all that, you still can't quite replicate the effect I'll limit sheet on Iron Man.
[1:56] No matter how you tweak your roughness value, you're only ever changing the blurriness of a single reflection.
[2:01] So at that point, I decided to look into it and I needed to do three things.
[2:06] First, I need to find reference.
[2:07] I needed to know if this was a 1 in a million anomaly
[2:10] because after all the practical suit I'll am recreated was made from a complex alloy
[2:14] and created specially for the movie.
[2:16] Secondly, I need to find information.
[2:18] I wanted to uncover what exactly happened during the production of Iron Man
[2:22] that I hadn't seen or heard of since.
[2:24] And thirdly, I need to find an explanation.
[2:26] Even if I could figure out how they replicated it in CG,
[2:30] I'd still need to understand the why, the actual physics behind why real metal behaves this way.
[2:35] So, I got to work.


### Finding References [2:37]
**Transcript (timestamped):**
[2:37] That one was pretty easy.
[2:39] Once you know what you're looking for, you see it everywhere.
[2:42] Have you ever looked at an elevator and thought,
[2:44] this reflection is really weird?
[2:45] What's going on?
[2:47] No? Oh, well, I have.
[2:49] And I don't know how I missed it until now.
[2:51] I think I might even have encountered it before without realizing.
[2:54] Back in my first year of school, I modeled a delirium
[2:57] and I couldn't figure out the roughness for the life of me.
[2:59] In one reference photo, it looked like 0.2 and in the next, 0.4.
[3:03] I couldn't point my finger on it.
[3:05] And it turns out that was exactly this phenomenon.
[3:08] And really, this double reflection effect is everywhere,
[3:10] except on YouTube, in schools, discord, forums, or station.
[3:14] Even professionally, I've never really heard anyone mention this thing.
[3:17] There's actually only three types of reference I found that didn't display this at all.
[3:21] Extremely polished metal, extremely rough metal,
[3:24] and extremely rare uniform metal, but we'll get back to this one later.
[3:28] So, I went online and watched videos of metal working and other manufacturing stuff.
[3:32] And I noticed that lots of these do have these multi-reflections.
[3:36] And that right before these surfaces would show the multiple reflections,
[3:39] they'd first go through an intermediary scratch state
[3:42] where you could visibly see micro-scratches spreading the reflection.
[3:46] So, my first thought was that maybe there are millions of consistent micro-scratches
[3:49] below our visual acuity scattering the highlights,
[3:52] which, among them, made it give the impression of a faint fall-off.
[3:56] So, I ran some tests, opened Macs,
[3:58] I met a metallic sphere and I put a scratch map sized 1 cm and rendered.
[4:03] Hmm, it just looks like regular roughness.
[4:06] But wait, there is a setting in charge of controlling how much detail are preserved
[4:10] within one pixel of the render that would be mid-mapping or filtering,
[4:14] depending on how you call it.
[4:16] So, I went into the settings, I turned it off and,
[4:18] oh man, that was exactly like the reference.
[4:21] Now, I had my main reflection and I would have a huge fall-off
[4:25] that was exactly what I was looking for.
[4:27] And this is actually so common that I searched for it in real life
[4:30] and I found a bunch of examples with zero struggle.
[4:33] In my elevator to-door where you see me both sharp and blurry,
[4:36] a fridge where the room's light glows way past the reflection,
[4:40] and even more interestingly, I came across this cooking pot lid while doing the dishes
[4:44] and I thought, what the fuck is that?
[4:46] This is way more complex than every other example I could find.
[4:49] You've got everything on there, you've got scratches,
[4:51] any sort of pee, two reflections, there's clearly more to it than just a scratch layer.


### Finding Information [4:57]
**Transcript (timestamped):**
[4:57] Uncovering information about ILM's specific approach
[5:00] was not an easy task at all.
[5:02] There really isn't much on the subject.
[5:04] One permissing resource was a SIGGRAPH 2010 paper
[5:08] written by legendary VFX supervisor Ben Snow,
[5:10] who ever saw the creation and, crucially for us,
[5:13] the Luke development and surfacing of the SIGG Ironman suits.
[5:17] In this paper, he goes into great detail about their entire shading process,
[5:21] how they approached it, their challenges and solutions,
[5:23] how they developed new tech for the suits,
[5:25] and yet as detailed as the paper was,
[5:28] the process of creating such a complex hero asset
[5:30] was so massive that 25 pages can only cover so much
[5:33] and my specific question wasn't directly addressed.
[5:37] But, within the paper, on the last paragraph of page 10,
[5:42] in between details about vector exponent values and UV management,
[5:46] I found it a brief mention of a second specular highlight.
[5:52] And ladies and gentlemen, that is a clue.
[5:55] However, it's still very little information,
[5:57] because what does that even mean?
[5:58] Is it really what I think it is?
[5:59] Maybe it's something else and I'm connecting invisible dots?
[6:02] Maybe that was just a specific case in the pipeline
[6:05] that wasn't related to Ironman's surfacing in general?
[6:07] Or maybe even it was just a piece of 2007 VFX jargon
[6:11] that meant something entirely different back then.
[6:14] So I had to find more.
[6:15] I discovered interviews, articles, tech reviews
[6:18] and presentations from SIGGRAPH and FMX, and nothing.
[6:22] There was practically zero information about this,
[6:25] part of it because it was 2007, 2008, almost 20 years ago,
[6:29] and part of it because it's so specific,
[6:31] and the only people who would know more
[6:33] would be the artists who worked on it themselves,
[6:35] but Ironman was released 19 years ago
[6:37] and that is a massive gap in time in the industry.
[6:40] Most of those artists are scattered across the globe,
[6:43] working in near anonymity or even retired,
[6:45] reaching out to them just wasn't feasible
[6:47] so I had to find another way.
[6:50] Anyway, so I contacted Ilems Supervisor and Principal Engineer,
[6:54] Pixar Global Researcher and Facebook Research Director,
[6:57] Christoph Harry, who not only is one of the most influential figures
[7:00] in computer graphics, with more contributions
[7:03] than I could possibly list, but luckily for us,
[7:05] was also one of the two people credited by Ben Snow
[7:08] for developing Ironman's shader in Anisotropic Tools,
[7:11] oh and he was also a key figure in lookdaving and rendering David Jones.
[7:16] Christoph very kindly accepted to answer my questions,
[7:19] although I must preface this with a reminder
[7:20] that it occurred over 19 years ago,
[7:23] so everything might not be recollected to perfection.
[7:25] So I showed him my Ironman screenshot and I asked him what is it,
[7:29] what could cause this and what's happening here.
[7:32] Christoph told me,
[7:33] All shaders at Ilems, since the ones I started distributing
[7:36] as generic circa 1996, had two specular lobes,
[7:40] so you could always mix and blend various properties through them.
[7:44] Our normal gain controls and thus fresnel were done through full colors
[7:47] at 0 and 90 degrees incidences, and the curve itself was a schlick
[7:51] though we could change the exponent on it from a default of 5.
[7:54] For Ironman, we ensured some sort of energy conservation,
[7:57] where diffuse substrates would automatically rebalance themselves
[8:00] with a very strong approximation, so as to not explode in energy,
[8:03] this was becoming critical because through important sampling and PBR,
[8:08] we were starting to do much more recursive ray tracing, reflections etc.
[8:12] I showed him my technical tests and my approach suggestions
[8:15] that we're gonna talk about in this video,
[8:17] compared to the ground truth and the default roughness workflow,
[8:20] asked him if that made sense and for his opinion on it, and he said,
[8:24] yes, this solution might be the way to attempt to emulate it,
[8:27] as the two lobes were simply additive to one another.
[8:30] And that was more information and confirmation that I could have hoped for.
[8:33] There we are, we've got our explanation and we know exactly how Ilems did it.
[8:38] At that point I even had an hypothesis as to what's causing this in real life,
[8:42] which Kristoff found adequate. I guess we're all done.
[8:45] We're all done, right? Not at all.
[8:47] My main issue with all of this was that, while I had real-world reference images
[8:51] and theoretical explanations as to why multi-reflection happened in the first place,
[8:56] my tests and explanations are all digital and honestly baseless beyond my own conjectures.
[9:02] My idea was that visual acuity can't resolve microscopic details,
[9:05] so our eyes interpret them as a faint secondary reflection,
[9:08] but unfortunately finding concrete evidence can be really tricky.
[9:12] You can see that close, a magnifying glass could see some scratches,
[9:16] but it won't be able to zoom in off for us to get a definitive answer.
[9:20] So it's just not feasible and I had to find another way.


### Finding Explanations [9:22]
**Transcript (timestamped):**
[9:23] Anyway, so I went to look at metal under the microscope to see what's actually going on
[9:28] beyond our visual acuity and huge thanks to EverSmaller for spending hours on vocal with me,
[9:33] looking at metal on her microscope and proceeding to every visual test we could think of,
[9:37] rotating the sample, checking different angles, different lights, different light colors,
[9:42] orientations and whatnot. And what we found was so interesting,
[9:45] I was really happy because my theory was correct.
[9:48] But on top of finding microscopic scratches creating what looks like a faint secondary
[9:52] reflection from a distance, we could see live that scratches vary wildly in size,
[9:57] density, straightness and most importantly depth. That was the critical part.
[10:02] And seeing that under the microscope was really amazing and not only was it correct when we first
[10:06] entered the microscope but the minimum zoom. And we kept zooming and zooming and every single
[10:11] iteration would reveal new scales of scratches and each again slowly contributing to another
[10:16] roughness stacked onto the others. Although at these scales they are so shallow that you really
[10:21] don't feel them from a distance. And why is that important you ask me? Well, if you had a scatter
[10:26] of scratches that were all perfectly consistent in size and depth, they would reflect light at a
[10:31] consistent rate of disruption and that would just look like a single secondary reflection of consistent
[10:36] roughness. If all scratches were deeper, reflect 2 would get blurrier. And if all scratches were
[10:42] denser, reflect 2 would get more visible. The reason for that being that more scratches would
[10:47] cover the initially clean surface but still not completely so the 2 would visually overlap due
[10:53] to our limited visual acuity. The point is it would never look like a multitude of roughness's
[10:58] values co-existing all at once. But here is where it gets interesting. When you start varying the
[11:04] depth of those scratches, things change. Some of them scatter light wildly, some scatter it just a


### Research Conclusions [11:05]
**Transcript (timestamped):**
[11:10] little and others reflect light at an almost identical angle than your reflect 1. Of course,
[11:16] depth isn't the only factor driving this phenomenon if you got density and size playing a massive
[11:20] role too. And this is how when you factor in every possible variation of real-world micro-scratches
[11:27] that you obtain reach metal revealing previously ignored variations. Some of them are smoky with
[11:32] a sharp reflect 1 and a seemingly single rough reflect 2. These ones for example have dense and
[11:38] consistent scratches. Some of them feature a beautiful long fall off. These have scratches of
[11:43] varied size, depth and density. And yes, thanks to all these variety, some of them have no fall off
[11:49] at all. Either metals with no fall off at all, not necessarily mean that they have no scratches.
[11:54] Instead it actually means that they have consistent enough scratches and disruptions of any kind
[11:59] that there would be no variation that our eyes could interpret as co-existing roughnesses.
[12:04] And last but not least, some surfaces are more exotic and present both
[12:08] isotropic and anisotropic reflections at the same time. And remember, anisotropy is an illusion
[12:14] due to surface disruptions being biased towards a direction. However, the problem with regular
[12:18] anisotropy is how simple and surface level it is. A regular anisotropic shader applies those
[12:24] directional disruptions to the entire surface as if it was fully covered without a single intact area.
[12:30] So naturally the entire reflection gets affected. But reality is more complex and not all surfaces
[12:36] are entirely scratched. If in fact a surface isn't actually entirely covered in scratches but instead
[12:42] is a mix of intact areas and disrupted areas, then a single pixel of your render will contain
[12:47] reflections from both situations. And therefore it'll look like a mix of both. And the final shader
[12:53] instead of being entirely anisotropic will be a mix of both types of reflections and preserve
[12:59] a certain amount of the original intact reflection proportional to the area of intact surface within
[13:04] one pixel but also a certain amount of the anisotropic reflection. And due to this you can even have
[13:09] multiple anisotropy directions within a single surface if the directional scratches are both
[13:14] non-constant and oriented differently. Okay let's use a practical example to really understand
[13:19] this aspect. So on this reference we have a green glove being reflected by a stainless steel surface.
[13:24] And we can see that the reflection is both clear and undisturbed but also that there is a second
[13:29] reflection mixed to it that is hugely rough and hugely anisotropic. And that is a direct consequence
[13:35] of sub-pixel content and density variation. Looking at this we can safely assume that the
[13:40] surface isn't entirely covered in scratches because we can see both results at once. And all of that
[13:45] has to do with visual acuity. And visual acuity is the sharpness of your vision or your render
[13:50] and your ability to discern distinct elements from one another. But because this acuity is
[13:55] finite and imperfect there is a scale at which your vision and render cannot resolve detail
[14:00] separately anymore. And because of that the perception of that specific area will be a blend
[14:05] between both elements. A red square and a blue square up close. Easy they're completely separate.
[14:11] Now a billion red and blue squares from a distance and it looks purple. That's exactly why screens
[14:16] work and it's exactly why reflection tail-off happens. So you've probably guessed it while
[14:20] this video originates from forgotten metal techniques about reflection tail-off the
[14:24] physical phenomenon this effect originates from allows us to talk about much deeper concepts
[14:29] like pearl layer anisotropic variation and scratch type dependent roughness variation.
[14:34] And now we have to replicate it. For those who've seen previous videos you'll know what kind of
[14:38] approach fits the situations where two different surfaces coexist with one being entirely present
[14:43] and scattered beneath our visual acuity and that's right that would be material layering.


### Doing it in 3D [14:48]
**Transcript (timestamped):**
[14:49] Unlike my previous video where I was specifically talking about layering in the context of real
[14:54] materials sitting atop of a surface like oil or dust material. Lasering in this case is a lot
[14:59] more niche and can seem inadequate at first glance but it turns out it makes complete sense.
[15:05] Material layering whether it's in V-ray cycles or most other engines doesn't actually take any
[15:10] virtual thickness parameter into account. All it's emulating is that there is in some way or another
[15:16] a different response to light around the surface and that the area of this response is so small
[15:21] that it becomes invisible to our eyes and can be approximated to a solid. And because this
[15:26] different light response isn't completely covering the surface it gets interpreted as a
[15:31] transparent value from a distance. So because there's no thickness taken into account material
[15:36] layering is actually adequate for multiple situations IRL. It could be particles sitting atop
[15:41] of a surface like oil or dust could be an area of that same surface that is altered in some way
[15:47] like a glint, speckles or millions of microscopic dots of rusts and it could also be holes revealing
[15:53] a deeper layer beneath the main surface as if you had for example metal under a scratch
[15:58] color paint. So that being said what does it mean in practice? Well if you take a look at our
[16:03] microscopic footage or any reference really we just have to look at scratches to see what our setup
[16:09] should be. So since our scratches are only visible when reflecting light we can tell that they have
[16:14] the same diffuse IOR and other properties as the rest of the surface or they would be visible at
[16:19] all time no matter reflections. If we isolate a first scale of scratches we can see that the
[16:25] only notable difference between the original surface and the scratches is the bump map. If we
[16:30] take another range of scale of scratches the only difference with the previous one would be the
[16:34] density, the thickness of the scratches and the bump map once again will take another range of
[16:39] scratches and there again and it's just another variation of width and depth and again and again
[16:44] and again until we're reaching scales where we cannot even tell the bump anymore and because
[16:49] we're dealing in general with variations beneath our visual acuity we don't even have to use bump
[16:54] at all. We can use the approximation instead and the approximation of bump is roughness so what it
[16:59] means is that as the scratches get smaller, denser and cover more and more of the surface
[17:04] the apparent general roughness of that layer will increase so instead of having multiple layers with
[17:10] multiple bump map and bump strength we'll just blend identical shaders together where each is
[17:15] getting impressingly rougher and on top of that because smaller scratches also tend to be decreasingly
[17:20] deep the apparent presence of each layer is going to decrease accordingly. So we're going to have
[17:26] our material layering set up with each of our duplicates and a master material at the base.
[17:31] Each other layer is going to be a duplicate of the first one except the roughness is going to increase
[17:37] and when you're building it the game is going to increase or decrease the presence of each layer
[17:41] until it matches the reference so you duplicate your material plug into your material layering set up
[17:47] and you dial it up and down and you're going to repeat this process however many times you like.
[17:52] Doing it in blender is going to be the same process except the nodes are going to be
[17:56] principled bsdf. Material layering is going to be a series of mixed shaders and the presence of each
[18:01] layer is going to be controlled via the factor. If you wanted to use roughness textures inside your
[18:05] material you can plug the same texture inside a series of different curves and increase the lift
[18:10] value of every iteration of curve so that each layer is getting increasingly rougher while
[18:15] maintaining the work you've done into your roughness. If your render allows it like blender's


### Cycles : GlossyBSDF [18:18]
**Transcript (timestamped):**
[18:21] cycle you can use glossy bsdfs instead. The process is identical to full material layering
[18:26] except you're going to use glossy bsdfs and mix as many as you need together. The way to set it up
[18:31] is very easy you just create a principled bsdf and you're going to mix it to as many glossy bsdfs as
[18:38] you want just like the full material layering. Each glossy bsdf is going to get increasingly
[18:43] rougher and will generally be decreasingly present through the factor slider. It is a little bit
[18:48] different than iRamance approach because they initially added reflections together so that broke
[18:53] energy conservation but modern technology and render speed allow us to do mixed shaders instead.
[18:59] And now it's time to see alternative approaches to achieve a similar effect each with their pros and
[19:04] cons. So the first method for achieving a fake multi reflection would be to use clear coat.


### Alternative : Clearcoat [19:05]
**Transcript (timestamped):**
[19:11] This was a popular suggestion in the comments of my last material layering video and while it has
[19:16] some limitations it's a great one click starting point. It can achieve a relatively similar looking
[19:21] tail off by adding an extra reflection. It's cheaper than some other options and it's built
[19:26] in virtually every single render engine. However it does have some limitations for all cases.
[19:31] This kind of effect is only going to be really present into hero assets so clear coat deforming
[19:38] the look of the underlying material such as diffuse color and apparent ior which in turns
[19:43] require a b compensations to restore original values is a huge drawback. And clear coat isn't
[19:49] metallic it's a blend to a dielectric material so the reflections will not be colored by the metal.
[19:54] But while it's look normal if your metal is white it'll start being obvious clear coat
[19:58] cheating once you've got any color in your metal. And you could think coloring the coat itself would
[20:02] fix it and it would help the reflections to some degree but then it only shifts the problem as now
[20:07] the entire underlying material and original reflect one are affected and incorrect. So clear coat is
[20:12] really case dependent and i would not personally recommend it but if it's from far away and that
[20:17] your metal is black and white then it could be a nice cheap alternative. For example on this lead
[20:21] study that i did the clear coat approach really deforms the underlying material and shaders.
[20:26] Not only it doesn't look correct compared to the reference it's also deforming materials in a way
[20:31] that isn't really desirable. The GGS reflection model was created specifically to emulate the


### Alternative : GGX Tailoff [20:34]
**Transcript (timestamped):**
[20:38] long reflection tail of visible on materials with micro textures. If your renderer allows it you can
[20:43] control how far the tail and reflection fade point goes. This gives the impression of a roughness
[20:48] increase at first because obviously the highlight takes more space now so in turn you can lower the
[20:53] roughness and match your material. This reflection model is an excellent option for multiple reasons
[20:58] because the control was created precisely to do that so it's very handy. It can be a bit confusing
[21:03] at first to really understand its potential but once you know what it's actually doing it's very
[21:08] handy and very useful. It's fast and easy to use and it comes at basically no cost because it is only
[21:14] modifying the single reflection that is already being calculated either way. However there are a
[21:19] few drawbacks that to me prevent the tail of control from being the number one option if you're trying
[21:23] to do the best looking render possible although it is the handiest and easiest option to go for.
[21:29] It's not exposed on every render engine so for example on cycles you would need someone else to
[21:34] probably go into the blender API to expose the control and hope that you have it at work. The
[21:39] various values you can choose from are basically just an exponent control for the unique tail of
[21:44] profile it has so while you can control the inbuilt profile you can't have a sharp highlight and a
[21:49] straight jump to point eight roughness for example. If I choose to customize my curve here and have a
[21:54] ground truth that would be quite unique there will be no way to recreate that with the ggx tail
[21:58] of control and it can break if you lower the values too much you start having undesirable
[22:03] reflections on to your image and that obviously doesn't help your material at all. I rendered


### Turntables [22:05]
**Transcript (timestamped):**
[22:09] four different methods to achieve reflection tail of there is ground truth multilayered
[22:13] reflections the regular roughness and the ggx tail of approach. I didn't include clear code because
[22:19] it's an insufficient solution that should only be considered in unimportant cases it is inadequate
[22:25] if you want to be serious and precise in our recreations of the references. So on these table
[22:30] we can see multiple things first off that the regular roughness workflow is completely inadequate
[22:34] to recreate the complexity and the richness of the ground truth approach you're supposed to be
[22:39] able to see the text clearly the neons are completely sharp and all the anisotropic reflections
[22:44] are added and mixed to the original reflection and not replacing it. On the regular roughness
[22:50] workflow there's a massive loss of information everything gets blended into each other it's
[22:55] just really poor and really insufficient if we want to make quality metal. If you use a renderer
[23:00] that allows you to edit it and happen to know about ggx tail of you could try to replicate it and that
[23:05] would get you pretty far ready you could have an in-between that looks closer to the ground truth
[23:11] but it's still pretty different the text isn't as clear there's a loss of information and the biggest
[23:16] problem for last you have that massive undesirable reflection spreading across the entire surface
[23:21] and we can see that it is plaguing the render in all angles. Now on the other hand the multi-layer
[23:28] reflection is a much more robust solution it is more expensive than the ggx tail off and that
[23:33] is pretty much its biggest drawback but it allows you complete creative control and perfectly
[23:38] achieves the intended look of the ground truth render. In fact every look difference for example
[23:43] there is a very very subtle difference in the immediate falloff around this neon or a completely
[23:49] artist dependent and not method dependent. My roughness choice for the first layer is probably
[23:54] a tad bit too big and I could either reduce it or reduce the presence of the first layer to
[23:59] match this ground truth render. I asked a few supervisors at work and other people who've


### Statistics [24:00]
**Transcript (timestamped):**
[24:04] generally been in the industry for 20 years and this phenomenon in shedding approach was
[24:09] basically no surprise to them so don't worry if you saw the title of this video and thought
[24:15] I still remember clickbait. You're not alone but I've never really seen anyone of my generation
[24:21] do it or mention it so thought I would make a video about it. It's not taught at any of the
[24:26] best schools in the world in courses and private servers or anywhere so to understand the different
[24:31] workflow landscape more transparently I decided to write a google form and task respondents
[24:36] with describing their workflow to four different metals that each showcase this reflection falloff
[24:42] effect to various degrees. I asked them to estimate different properties of the shader if they could
[24:48] and I also told them to be as thorough or concise as they wished because I absolutely did not want
[24:54] to buy us the question and suggest that there was actually something not worthy on these metals
[24:59] so thanks to them I was able to see recurring workflow patterns. Of these 52 people 41% were
[25:05] generalists 25% were surfaces and 10% were character artists. The majority of respondents
[25:11] are professionals with also 28 and 25% being hobbyists and students respectively and lastly most
[25:17] participants had two to four years of experience and 23% with over five years and even 11% at
[25:24] over 10 years so I read through every single reply I noted the workflow the suggested values the value
[25:31] variations whether or not they noted the presence of the reflection falloff and this is what came
[25:36] out of it. Across all examples about 25% of people noticed something going on onto the surface most
[25:43] of them suggested that it was dirt or fingerprints which what may not be entirely true it is on some
[25:49] references but it's not the main effect it still shows that they did notice an extra behavior to
[25:54] account for. Also a fair amount of people within those 25% suggested that it could be achieved with
[26:00] a coat layer. In those 52 respondents two of them mentioned varying the ggx tail off and more
[26:05] importantly two other people mentioned explicitly that there was different reflections coexisting
[26:12] and not via coating. One interesting thing to look at would be the roughness value suggestions
[26:16] on each example. On example one you can see that the people suggested a wide variety of values you've
[26:21] got 0, 0.15, even 0.7. You couldn't wonder why would suggestions be so different but it actually
[26:29] makes sense when you think about that reflection falloff gives the impression of multiple roughnesses
[26:34] coexisting so if the viewer looked more around those sharp edges they might tend to say the roughness
[26:40] would be zero and instead if they noticed how the colors bleed largely onto the entire sphere
[26:45] they'd probably suggest something higher like 0.4 or 0.7. So these heterogeneous estimations
[26:52] occur throughout all examples and while they generally gravitate toward the most visible
[26:57] reflections look the last example was particularly tricky in that there doesn't seem to be a superior
[27:03] roughness choice and that one really messed up with people's estimates. The value suggestions were
[27:08] scattered evenly across almost all ranges of roughness. There was the most amount of confusion
[27:13] in written comments and it was generally the example that received the most extraordinary
[27:17] suggestions like ggx variations, coat overlay etc really anything to make it work. So I think
[27:24] this form was really informative even with just 52 respondents. To me it highlights how this effect
[27:30] isn't accounted for not because people don't see it but rather because there is no clear consensus
[27:36] on what it is and how to achieve it. Let's see how multi-layer reflections compare to regular


### Comparisons [27:39]
**Transcript (timestamped):**
[27:42] roughness. That's the first example from the google form. This is the fourth example from the google form.
[27:50] This one is one of the earliest tests that I did when I started researching this subject and on this
[27:59] specific example I'd like you to pay attention to the skin color the halo around the hand.
[28:04] These are completely missing before multi-layer reflections are applied. This effect is also
[28:08] present in balloons for example. In a traditional metal workflow I would have to choose between
[28:16] the anisotropic reflection and the clear reflection but with multi-layer reflections I can just have
[28:21] both exactly like the reference. Another example with the fridge I came across and here you can
[28:26] clearly see that the door is perfectly clear maybe something like 0.05 roughness and there's a huge
[28:32] anisotropic falloff on top of it. This is a cooking pot of mine where you can see that there is both
[28:38] a clear reflection and an anisotropic reflection at the same time. Before you'd have to choose between
[28:43] one reflection or the other but now you can just have both at once.
[28:49] Here's a personal test on Ironman's helmet compared to the practical Mark II suit and you've got
[28:54] Ironman's own render from Ben Snow's paper on the side as well so you can judge this approach for
[28:59] yourself. And this is the reference of the green gloves with the semi anisotropic multi-reflections.
[29:08] And here is the last example with an elevator. Before the reflections were very simple
[29:13] anisotropic nice but very simple nonetheless and afterwards they cannot get these trippy elevator
[29:18] reflections. And this is it we've rediscovered forgotten metal workflows looked at reflection


### Conclusion [29:19]
**Transcript (timestamped):**
[29:24] tail-off discovered per layer anisotropy and visual acuity and understood sub-pixel scratch
[29:29] variations. Man that was so much work there's about 26 000 frames of explanatory motion graphics
[29:38] I've been editing this for two weeks every night after work. This is off-screen by the way it's almost
[29:44] 2 a.m. on a weekday as I'm recording this so I really hope you enjoyed this massively long and
[29:50] convoluted video. I hope I repeated myself enough to make things clear. I decided to put my social
[29:57] link under this video initially I opened this channel anonymously and I figured it might be
[30:03] curious to check out my work there's a bunch of core resources as well my all station.
[30:07] Do let me know if you have any comments or suggestions and on that note I'll see you next time.



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

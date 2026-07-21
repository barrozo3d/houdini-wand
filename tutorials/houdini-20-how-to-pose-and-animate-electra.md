---
title: Houdini 20 | How to Pose and Animate Electra
source: YouTube
url: https://www.youtube.com/watch?v=q6GE9WmZKeI
author: Houdini
ingested: 2026-07-20
houdini_version: "H20"
tags: [apex, kinefx, animation, rigging, beginner, houdini-20]
extraction_status: complete
frames_dir: tutorials/frames/houdini-20-how-to-pose-and-animate-electra/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Houdini 20 | How to Pose and Animate Electra

**Source:** [YouTube](https://www.youtube.com/watch?v=q6GE9WmZKeI)
**Author:** Houdini
**Duration:** 16m24s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Today we are going to pose and animate Electra using the APEX rig built right into the character's geometry
[0:07] APEX is a brand new context designed to deliver an animator friendly environment
[0:12] This lesson is for any animator, even animators new to Houdini, who want to learn how they can benefit from this new set of tools
[0:20] Ok, let's get started by setting up an animate desktop
[0:25] In here we are going to make a few changes, we are going to collapse the animation editor
[0:30] Spacebar B will bring up the perspective view
[0:35] Then we are going to turn off channel groups in this sidebar here, so we can focus on the channel list
[0:40] Let's bring up the network view here and get started
[0:44] Let's press Tab, type ELE, press Enter, and then press Enter again to place the character, Electra, into the scene
[0:55] Use the spacebar view tools to tumble and track around
[1:00] Double click down to the geometry level, which is where characters work in Houdini
[1:05] Now, let's take this and use what would be the Kinefx way of doing things, which is Kinefx was when we first brought things down to the geometry level with characters
[1:18] We would plug this character into a bone deform and then set display
[1:26] Then we can go Tab, Rig Pose, and place that here
[1:32] This Rig Pose exposes the skeleton within this character and we can go in and pose the various joints and so on
[1:40] This is fine, but everything we are doing here is forward kinematics
[1:48] If you select the pelvis and try to move it, you will see there are no kinematics, the leg is not anchored, etc.
[1:56] We would have to add that as a separate thing, so let's delete that
[2:00] Instead, we are going to do output Apex scene
[2:05] This is a version of the character that actually has its Rig built into it
[2:10] We click on the animate tool and it creates a scene animate node which exposes this Rig, this Apex Rig
[2:20] We press escape, even though we are on that node, we don't see it, but with the animate tool we will see it
[2:25] We press this and now when we click and drag on the various handles, we will begin to get kinematics in areas like the arms and legs
[2:37] We can now start to pose the character
[2:41] We can grab any handle here, let's move the one foot forward, one foot back
[2:48] There is the knee controls, let's grab those
[2:56] The Apex Rig that is embedded with this character has all these controls built into it
[3:04] As an animator, I get this, I plug it into a scene animate and I am able to start working posing and everything is good
[3:12] If I press escape, it goes away, animate tool there will bring it back
[3:21] If I go to the object level, you will see that the posing that I did does not exist
[3:27] Everything that we did, the Rig as well as the posing, is buried in the scene animate node
[3:34] If we go tab, we can do Apex scene invoke and bring this node up, we can plug that in
[3:44] Nothing happens at first, we press this output all character shapes
[3:48] This will basically extract the pose that we have out and make it available in ways that can be used in other parts of the D&E
[3:57] There it is at the object level, and here it is
[4:01] Whatever was sort of embedded in that scene animate node is now available
[4:09] If we go back to scene animate, we can go back to the posing of Electra
[4:16] There are some tools that will help us along to make this happen
[4:22] One of the biggest ones in here is something called selection sets
[4:27] If you look at this panel here, this HUD, you will see that there is all the controls of the character
[4:37] Essentially all the parameters, and one of the things that is interesting is if you note, when you select something here, you will see it
[4:43] But the parameter pane has nothing, so these parameters don't live in the traditional parameter pane method within Houdini
[4:49] They live within the character and they are exposed when you select things
[4:54] You can pin all the controls and they will all be available in the channel list on the side, or unpin them in which case
[5:03] You can also change the display of all the handles through here
[5:07] And if you unpin it, you can click and nothing will be scoped
[5:12] You can also do something where you select, let's say these three handles
[5:20] You will see that they are scoped in the channel list
[5:25] And what you can do now is you can say, what I want to do is I want to make my own set out of this
[5:32] So I am going to go over to here, create from selection set, and it is called set1
[5:36] And we can change that, let's give that a name of hands, underscore torso
[5:44] There we go
[5:47] And so now if I rotate that, all three of the things rotate at the same time, but that is not very useful
[5:53] So what we are going to do instead is we are going to press control shift
[5:56] And now we can rotate around one of these, the last one selected
[6:01] Now, it will probably make more sense to select around the inner one
[6:05] So what we can do is we can bring up a panel called the selection set panel
[6:14] And if we open up the hands torso and the base, we see there is the three things
[6:20] And the yellow one is the one that is sort of in charge
[6:23] We are going to change the primary control to the COG which is in the middle
[6:25] So now when we select this, that is where the handle is
[6:30] And if we press control shift, we would rotate around that center piece instead of the one on the side
[6:36] And that can work sort of both ways there
[6:41] Now, it is possible that another animator has worked on the same character
[6:47] And they have sets that they have saved out
[6:48] So what we are going to do is we are going to import that and apply to Electra
[6:56] And here we see a bunch of controls, there is one for blocking out setting key frames
[7:04] So you can pin it and block it
[7:06] You have got something for moving all the parts of the character together
[7:10] And then you have got something for the upper body
[7:14] Which is similar to what we had with the hands and torso
[7:19] And you have got the lower body
[7:21] So these are controls that somebody else built for the same character
[7:26] And they can be passed around and shared to make it easier to animate and work with a character
[7:33] And you have got other details like for instance you have got the fingers
[7:37] And you can just grab that and close the fingers like that
[7:44] So the work that somebody else put into creating some selection sets become available to you and your scene
[7:51] So that is pretty cool
[7:55] So now that we have that, as you can see we have got controls for the clavicle
[8:02] We go down to the foot, we can see we have got reverse foot controls
[8:07] Actually we want to do the heel here, so we are going to raise up the heel
[8:11] And then inside here we have got the ball, we want to sort of reverse foot there
[8:16] So there are little controls in there and then we can begin to continue to pose the character
[8:22] So you can go around and try out all the different handles and see what they do
[8:27] And you will be set up to pose and work with your character
[8:32] So let us flatten that and just like we can do things in there
[8:36] Just remember the channel list actually allows us to go in and select that and just type in zero
[8:41] So you have got that, you do have parameter control but it is through the channel list not the parameter main
[8:51] So let us just do shift F1 and hide the tips on there, those are very useful tips
[8:57] And so you probably want them up for a while but just to give us more visual space
[9:00] We are going to hide them for now and we are going to go in and let us add in a second version of Electra
[9:06] And see how we can work with two characters at the same time
[9:09] So we are going to place the new one down and let us set the display flag on that
[9:15] Now looks the same for now, let us go to the parameter pane
[9:22] Let us change it to a metallic version so we can differentiate between them
[9:25] And this time we are going to do Apex character instead of Apex scene
[9:28] So what Apex character means is that it is waiting to be named
[9:35] You have got to add that character to the scene whereas the first Electra was already part of the scene
[9:41] So we are going to go in and we are going to go to animation and you cannot see this, it is called Rig Tree
[9:48] We are going to see how the original Electra is set up so it has Electra.char which is its name, character's name and all the pieces inside
[9:58] Now if we do an Apex scene add, we can place that down and we can plug in the other character into the second input
[10:10] Now this one is called scene add character, we do not want that, let us change that to Futura
[10:17] And now that is the name of that character
[10:20] Then we can plug that into the chain and now we have both of those terracters in here together
[10:30] If we go to scene animate and we go to pose, there they are, they are together
[10:34] So now we can grab one of them, let us get the wooden version and let us take the metallic version and rotate it around
[10:43] So we can have them interacting together
[10:45] So once we have this, we can see that scene invoke is not working yet because what we need is to output all shapes
[11:03] Now the second character is part of the scene invoke so we will have that later when we need it
[11:08] And then we go back to the scene animate node and we can begin setting some keyframes
[11:13] Before we do that, let us do the selection set again, we added the selection set to the first character, we can do the same to the second character
[11:21] So let us accept that, say select character to apply to and let us do the Futura character and accept
[11:29] Now this second group is actually called Electra 2, we could rename it but it is fine for now
[11:35] So we have controls for all these various things, just exactly what we had before but now assigned to this other character
[11:43] So let us take the, let us unpin it for now, let us select the all mover and then we are going to press the shift key and we are going to select the first character's center of gravity
[12:03] We are going to go to frame 10 and press K, we will key frame everything that is scoped, anything that is in the channel list
[12:10] Now let us go to 75 and we are going to take this and we are using control shift, raise everything up together and press K
[12:23] So just like before, control shift will rotate everything and instead of trying to rotate everything individually it will rotate everything as a group
[12:34] And that gives us this cool look that we are getting here
[12:37] So now that we have this, we can go to, for instance, frame 75 and let us start to just, oh we have got too many things selected, undo
[12:48] And deselect, so let us get these two feet and we are going to rotate these down and we are going to lift them
[12:55] Now because we have set key frames here, any changes to the pose will be reflected in the key frame
[13:02] If we were not on top of a key frame then any posing we did would be ignored
[13:07] Now we are going to press the shift key on this sort of null that we have at the shoulders
[13:13] And this allows us with the control shift to rotate the whole arm out
[13:18] We are going to rotate that around, so we are going to shift select again and then control shift to rotate that hand out
[13:27] Rotate the hand around, this time just normally, just to get the pose that we are looking for here
[13:33] Press shift again and control shift to just go down a little bit
[13:41] In a way with the control shift we are able to almost do forward kinematics on top of our kinematic control
[13:48] So that is a pretty exciting capability here within Apex
[13:54] So now we are going to just rotate this hand around
[13:56] Now we are just posing this one, we have not key framed this yet
[14:01] The only part of the original electric character we key framed is the center of gravity
[14:08] So let us go in, we are going to have this character is just sort of, that is not really moving
[14:15] So what we want to do is we want to set some key frames on the hand as well
[14:18] So what we need to do is scope the original electric character and use those scopes to, let us go to frame 75
[14:32] Which is where all the other parts are key framed and we are going to raise that up
[14:36] Now we do not want to block it out with this version of the character, what we want to do is let us turn that off
[14:42] Let us open up this and we will block the animation on the original
[14:47] So this will allow us to key frame the whole character
[14:50] So we are going to key frame a couple pieces here
[14:58] And then we will go back to frame 10 and of course we need to key frame here
[15:07] And then that will allow us to, there we go, K
[15:12] And that will allow us to sort of have the hand lifted and the body moving in reaction to the future character
[15:21] Now we can rotate that a little more, we can grab the elbow, pull that down, there we go
[15:27] And because we are doing this all on frame 75, we are just getting the posing right and there we go
[15:34] So now we have an animation of Futura lifting in the air and the original electric reacting to that
[15:40] And we go to scene invoke, we see there is what the animation looks like that we have made so far
[15:47] Obviously we can put a little bit more into other parts of the character but this is a good beginning to our motion
[15:54] So let us review what we have done so far, we brought in the APEC scene using the test geometry
[16:01] We also brought in a character and named it using these two nodes and combined them
[16:10] We have used scene animate to pose and key frame the character and then scene invoke to extract that character out and get the scene that we want



---

## Captured Frames

- [1:30] tutorials/frames/houdini-20-how-to-pose-and-animate-electra/frame_000.jpg
- [2:25] tutorials/frames/houdini-20-how-to-pose-and-animate-electra/frame_001.jpg
- [5:30] tutorials/frames/houdini-20-how-to-pose-and-animate-electra/frame_002.jpg
- [6:10] tutorials/frames/houdini-20-how-to-pose-and-animate-electra/frame_003.jpg
- [7:00] tutorials/frames/houdini-20-how-to-pose-and-animate-electra/frame_004.jpg
- [10:30] tutorials/frames/houdini-20-how-to-pose-and-animate-electra/frame_005.jpg
- [12:10] tutorials/frames/houdini-20-how-to-pose-and-animate-electra/frame_006.jpg
- [15:40] tutorials/frames/houdini-20-how-to-pose-and-animate-electra/frame_007.jpg

---

## Structured Notes

### Core Technique
Posing and keyframe-animating a character using the APEX rig embedded in test geometry (the "Electra" character) via **Apex Scene Animate**, contrasted against the older KineFX Rig Pose (FK-only) workflow, then extracting the animated result with **Apex Scene Invoke**; also covers working with two characters simultaneously via Apex Scene Add Character.

### Summary
Official SideFX beginner-level animator lesson (16m24s) demonstrating that APEX rigs can be embedded directly in character geometry for a fully animator-friendly workflow. Starts by showing the old KineFX method (Bone Deform + Rig Pose = forward-kinematics only, no anchoring) as a contrast, then switches to Apex Scene Animate, which exposes the character's built-in APEX rig with real IK (grabbing a foot handle moves it with the leg anchored). Covers Selection Sets (grouping multiple controls, e.g. "hands_torso", choosing a primary/COG control so Ctrl+Shift rotates the group around a chosen pivot instead of individually), importing selection sets authored by another animator and sharing them via the scene, reverse-foot heel/ball controls, adding a second character ("Futura") via Apex Character + Apex Scene Add Character (renaming it, plugging into a second input, distinguishing it visually via a metallic material), keyframing both characters together (frame 10 baseline pose, frame 75 target pose, `K` to key everything scoped in the channel list), and using Ctrl+Shift group-rotation as a kind of "FK on top of the rig's kinematic control." Ends with **Apex Scene Invoke** → "Output All Character Shapes" to extract the finished multi-character animation out of the embedded scene-animate node into the regular object level.

### Key Steps
1. Set up an Animate desktop: collapse the animation editor, Spacebar+B for perspective view, turn off channel groups in the sidebar to focus on the channel list.
2. Tab → type `ELE` → Enter twice to place the Electra character asset into the scene; double-click down to the geometry level where characters live.
3. (Old KineFX method, shown for contrast) plug the character into **Bone Deform**, set display, Tab → **Rig Pose** to expose/pose the skeleton — this is FK-only; grabbing the pelvis shows no IK anchoring on the leg. Delete this approach once demonstrated.
4. Correct APEX method: use **Apex Scene** output on the character (a version with its rig built in) → click the Animate tool to create a **Scene Animate** node, which exposes the embedded APEX rig's handles with real kinematics (dragging a foot handle keeps the leg anchored via IK).
5. Note that posing done inside Scene Animate does not exist at the object level until extracted: Tab → **Apex Scene Invoke** → plug it in → click "Output All Character Shapes" to make the pose available at the object level for downstream use.
6. Selection Sets: select multiple control handles in the viewport (they're scoped in the channel list, since APEX control parameters live on the character/HUD, not the traditional parameter pane) → "Create from Selection" → name it (e.g. `hands_torso`); use **Ctrl+Shift** while dragging to rotate the whole set around the last-selected (or a chosen primary, e.g. COG) control instead of each individually — set the primary control via the **Selection Set panel**.
7. Import selection sets authored by another animator for the same character and apply them to Electra — instantly available controls for blocking/keyframing, upper body, lower body, fingers, and reverse-foot heel/ball groups.
8. Add a second character: place a second Electra instance, change its material (e.g. metallic) to visually distinguish it, output it as **Apex Character** (unnamed, waiting to be added) instead of Apex Scene, then use **Apex Scene Add Character** to plug it into the first character's chain and rename it (e.g. "Futura") — check the **Rig Tree** panel to see each character's `.char` name and node hierarchy.
9. Both characters now appear together under Scene Animate; apply/import selection sets to the second character the same way (referencing which character to apply to).
10. Keyframe workflow: select the desired scoped controls (e.g. "all mover" + first character's COG via Shift-select) → go to frame 10 → press `K` to key everything currently scoped in the channel list → go to frame 75, pose (including Ctrl+Shift group rotations), press `K` again. Posing only affects keyed frames when parked exactly on a keyframe; otherwise posing changes are not retained.
11. Layer additional keyframed detail: scope specific control nulls (e.g. shoulder), Ctrl+Shift-rotate the arm/hand as a group for combined FK-like control on top of the rig's IK, and key those at the same target frame so multiple characters' poses stay in sync at a shared frame.
12. Finish: **Apex Scene Invoke** → "Output All Character Shapes" again (now including the second character) to preview/export the finished multi-character animated result.

### Houdini Nodes / VEX / Settings
- **Nodes:** Bone Deform, Rig Pose (KineFX, FK-only — shown as the outdated approach), Apex Scene (embeds the rig with the character), Apex Scene Animate (animator-facing posing/keyframing node, exposes rig handles), Apex Scene Invoke ("Output All Character Shapes" toggle to extract the pose to the object level), Apex Character (unnamed character output awaiting a name), Apex Scene Add Character (merges a second named character into the animate chain), Rig Tree panel (shows `<name>.char` hierarchy per character), Selection Sets panel (create/import/apply per-character selection sets, set primary/COG control).
- **Controls used:** COG (center of gravity, primary pivot for group rotation), reverse-foot heel/ball controls, clavicle controls, shoulder null, elbow, knee, per-finger controls.
- **Interaction patterns:** drag a handle for direct IK posing; **Ctrl+Shift** + drag rotates an entire selection set as a group around its primary control (described as "FK on top of kinematic control"); `K` keys every control currently scoped in the channel list at the current frame; Shift+F1 toggles on-screen viewport hints.
- **Keyframe values used in the demo:** frame 10 (base/blocking pose) and frame 75 (target pose) for both characters.

### Difficulty
Beginner — explicitly aimed at animators, including those new to Houdini; no VEX or Python scripting involved, pure animator-facing UI workflow.

### Houdini Version
Houdini 20.

### Tags
apex, kinefx, animation, rigging, beginner, houdini-20

---

## Related Tutorials
- `tutorials/apex-rigging-h20-masterclass.md` — the rig-building counterpart (how the embedded APEX rig used here is actually authored); shares tags: apex, kinefx, rigging, houdini-20.
- `tutorials/apex-in-houdini-evolving-animation-workflows-for-production-matteo-martinez-pari.md` — covers the same Scene Animate / ragdoll / animation-layer caching concepts from a production-pipeline angle; shares tags: apex, kinefx, rigging, animation.
- `tutorials/rig-builder-introduction.md` — same APEX/KineFX character-rigging umbrella (H21 Rig Builder series); shares tags: apex, kinefx, rigging.
- `tutorials/rig-builder-project-overview.md` — same character-rigging umbrella; shares tags: kinefx, rigging, animation.

---
title: [Урок] Помада. Часть 2. Flip Sim
source: YouTube
url: https://www.youtube.com/watch?v=H17o8w-CFUM
author: Alexander Eskin
ingested: 2026-06-11
houdini_version: "Not specified (H19–H21 UI)"
tags: [sop, dop, flip, simulation, particles, vdb, modelling, intermediate, advanced]
extraction_status: complete
frames_dir: tutorials/frames/урок-помада-часть-2-flip-sim/
frame_count: 4
---

# [Урок] Помада. Часть 2. Flip Sim

**Source:** [YouTube](https://www.youtube.com/watch?v=H17o8w-CFUM)
**Author:** Alexander Eskin
**Duration:** 34m20s | 1 section(s)

---

## Raw Data (for Claude Code extraction)


### Full Content [0:00]
**Transcript:** Теперь можно просто пить к каплим, но теперь надо поправить вот этот вариант. disadvantages я запыл здесь добавитьouncer unconditional в максимум. Вст جедежной тушuttering друзья Да, это будет не металлическое часть от черной пластик. Теперь можем делать капли. Новый нодан за липстинг droplets. Это у нас уже просто геометрия. Это будет просто липстик. Вот так. И обжигнусь даже с амогиометрию. И будем скатрить понеточки для начала. Сейчас скатр не видишь рампулиган. Все это переведем. 0,8. Комверта обратно. Это у нас полигон. Третья такая резная штука. Но она единым мэшом идет. Сейчас с дайдем нормальный. Отрежем половину. И низушку и половина отрежем. Но мне нужно заднее часть. И нижняя часть. Примерно. Не знаю, 5, 5. Здесь дирекшем. Ну, я знаю. И нам мне нужно заднее половина, чтобы не симулять там. Пузыри, которых не видно. Да, примерно так. Итак, это у нас 0. Шейп, что скидка надоел. И будем скатрить понеточки. Чай маленький. 355 релокстраейшем. Выключим. Отребит крыть пискейл. Зазначение 0.03. И понойзем. Отребит и просто флол. И просто флол. Это не теплое. Нойз. И масштаб у него на 2. И можно еще раз сделать отребу за just float. Малозил трандон. И минимальное значение побольш...

**Frame:** tutorials\frames\урок-помада-часть-2-flip-sim\frame_000.jpg


---

## Structured Notes

### Core Technique
FLIP droplet simulation for lipstick product visualization: scatter points on trimmed lipstick surface (back half only — optimization), `pscale` 0.03 with noise variation via `attribvop`, FLIP sim drives droplet flow. Russian-language Part 2 of Lipstick series.

### Summary
A 34-minute Russian-language tutorial (Part 2) adding FLIP fluid droplets to the modeled lipstick from Part 1. Creates a "lipstick_droplets" geo node, scatters points on the lipstick surface (density ~0.8), trims to the visible rear half only (front half excluded — don't simulate what can't be seen). `pscale` attribute set to 0.03 with `attribvop` noise variation (scale 2) + random float for size range. FLIP simulation drives the droplet behavior on the lipstick surface.

### Key Steps
1. New geo node "lipstick_droplets" → `objectmerge` the lipstick geometry from Part 1
2. `scatter` SOP — density ~0.8 on lipstick surface; 355 relax iterations
3. Trim to **back half only**: clip/blast front face + bottom portion (~5 units) — saves simulation time for non-visible geometry
4. `attribcreate` — `pscale` = **0.03** (base droplet size)
5. `attribvop` — noise float, scale 2 → multiply `pscale` for size variation
6. Second `attribvop` — random float, set minimum value to increase minimum droplet size
7. FLIP fluid DOP network — scatter points as FLIP source; `flipsolver`
8. Configure surface tension for droplet behavior on lipstick surface
9. Cache sim; render with liquid/water material

### Houdini Nodes / VEX / Settings
- `objectmerge` SOP — pull lipstick geometry from Part 1 node
- `scatter` SOP — density 0.8; 355 relax iterations
- `clip` or `blast` — remove front half + bottom (visible rear only)
- `attribcreate` — `pscale` = 0.03
- `attribvop` — noise float, scale 2; multiply `pscale`
- `attribvop` — random float; minimum size clamp
- FLIP DOP — `flipsolver`, surface tension for droplet clinging
- `filecache` — cache the sim

### Difficulty
Advanced

### Houdini Version
Not specified (H19–H21 UI)

### Tags
sop, dop, flip, simulation, particles, vdb, modelling, intermediate, advanced

---

## Related Tutorials
- [[урок-помада-часть-1-моделирование]] — Part 1 (modeling prerequisite)
- [[tutorial-lipstick-part-1-modeling]] — English Part 1 companion
- [[houdini-tutorial-creating-realistic-waterfall-simulation-step-by-step]] — FLIP fluid fundamentals
- [[tutorial-purple-sponge]] — similar scatter + pscale noise workflow

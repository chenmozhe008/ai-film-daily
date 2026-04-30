---
name: ai-creative-daily
description: Generate, test, backfill, improve, and schedule the AI creative daily report for Feishu.
---

# AI Creative Daily Cloud Skill

This repository copy is the cloud-runnable rule source. Keep it small, operational, and synchronized with the local Codex skill.

## Daily Goal

Create an AI creative operations brief for creators. Do not write a generic AI news digest. The report must include creator-useful signals: platform/tool changes, reproducible methods, and concrete works or cases.

## Window

Use Asia/Shanghai. The daily window is previous day 08:00 to current day 08:00. Items outside the window can be used as background notes only, not as today's report items.

## Required Source Lanes

Run these lanes in this order:

1. X account-pool lane. Start with `python3 ai-creative-daily/scripts/build_x_query_pack.py --date YYYY-MM-DD --format text`. The first blocks must be `kol_creators` and `kol_chinese`; if official accounts appear first, stop and fix the query pack.
2. Chinese creator-platform lane. Search Bilibili, Xiaohongshu, WeChat/official accounts, and Chinese creator communities for tutorials, works, AI short films, image/video workflows, role consistency, storyboard, camera movement, editing, voice/music, and production breakdowns.
3. Official/platform lane. Search official product and model releases after creator-native discovery, so official news does not crowd out methods and works.

## X Account Pool

Use `ai-creative-daily/references/x-lists.json` when present. In the cloud repo, the helper also falls back to `sources/x-lists.json`.

For every run, X must produce review candidates before final writing:

- At least 5 creator/KOL tutorial or workflow candidates for Section 3 review.
- At least 3 creator/tool showcase or work/case candidates for Section 4 review.
- At least 2 Chinese creator candidates from `kol_chinese`, or a written blocker explaining why none could be verified.

Use query intents: workflow, tutorial, breakdown, prompt guide, behind the scenes, case study, making of, AI short film, AI video, made with, showcase, camera, shot, storyboard, character consistency, Runway, Kling, Seedance, Midjourney, Veo, Sora.

## Sections

1. Industry/platform: important events that change creator judgment.
2. Tools/capabilities: product/model/tool updates that affect creative workflows.
3. Methods/tutorials: only reproducible creative operations. Include steps, prompt structure, screenshots, node graph, before/after, camera/shot/character consistency/editing/music/voice details. Reject generic commentary and tool lists.
4. Works/cases: concrete creator works or production cases with an independent link and traction/production signal. Do not use tool announcements or company news as cases.

If Section 3 or 4 is weak, run a second pass before writing. Search X handles discovered above, then Bilibili/Xiaohongshu/WeChat with the strongest tool names and creator intent terms.

## Feishu Rules

- Bootstrap cloud Lark CLI with `bash ai-creative-daily/scripts/bootstrap_lark_cli_cloud.sh`.
- Do not print secrets.
- Main index doc token: `CM90deQCUomWgFxuGZwcun8an8d`.
- Daily card chat id: `oc_c995c8a2b1f9bef29d1fe8e2d3667ccf`.
- User open_id for full access: `ou_0816cf0e8247b3ac4d1b91a14cea83e5`.
- After creating or updating a daily doc, add that user as `full_access` and set public sharing to internet anyone-with-link can read. If permission setting fails, stop before sending.
- Push exactly one Feishu interactive card with the daily report link only. Do not send the total index link and do not send a bare link.

## Quality Gates

Fail and revise if any are true:

- X account-pool lane was skipped or only produced official-company news.
- Bilibili/Xiaohongshu/WeChat creator-platform lane was skipped.
- Section 3 has no creator-native tutorial candidates before final selection.
- Section 4 has no concrete work/case candidates before final selection.
- A section is padded with weak items instead of saying `本日无符合条目`.
- A final item lacks an accessible link or date confidence.
- Old evergreen tutorials are presented as today's news without a same-day update or resurfacing reason.

## Self Review

At the end, report:

- Whether cloud bootstrap, network, and Feishu bot checks passed.
- Top X creator/KOL candidates found.
- Top Chinese creator-platform candidates found.
- Whether Section 3 and Section 4 passed quality gates.
- What query/source change should be kept for tomorrow.

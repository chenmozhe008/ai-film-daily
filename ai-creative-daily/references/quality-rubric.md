# Quality Rubric

Run this before writing to Feishu and again after sending.

## Hard Gates

Fail and revise if any are true:

- Any included item has no accessible link.
- Any link does not match the claim.
- Publication/event time is outside the target window without being marked as context.
- Section 3 contains generic commentary instead of a reproducible method.
- Section 4 contains tool news instead of a concrete work/case.
- Section 3 has no creator-native tutorial candidates from B站/小红书/公众号/YouTube/X before final selection.
- Section 4 has no creator-native work/case candidates from B站/小红书/YouTube/X before final selection.
- X account-pool lane was skipped or only used for official company announcements.
- Old but useful tutorials are included as today's news without a same-day update or resurfacing reason.
- B站/小红书 search results were accepted without checking whether they are old evergreen courses.
- A section is padded with weak items instead of `本日无符合条目`.
- The document contains process notes, source logs, or extra summary blocks.

## Scoring

Score each candidate 0-10:

- Creator relevance: 0-3
- Freshness and date confidence: 0-2
- Source quality: 0-2
- Specificity: 0-2
- Actionability or case value: 0-1

Prefer score 7+ items. A 6 can be included only if it fills an important gap. Below 6 should not appear in the report.

## Section Targets

- Industry/platform: 3-6 items.
- Tools/capabilities: 3-5 items.
- Methods/tutorials: 2-5 items, but only if actually useful.
- Works/cases: 1-4 items when qualified; otherwise one `本日无符合条目` row.

## Source Mix Gates

The candidate pool, before final filtering, must include:

- At least 10 X account-pool candidates, including at least 5 from creator/KOL accounts.
- At least 8 Chinese creator-platform candidates from B站/小红书/公众号 combined.
- At least 5 tutorial candidates with explicit workflow evidence.
- At least 5 work/case candidates with concrete output links.

If a gate cannot be met because of access limitations, the run should not silently pass. It must record the blocker and ask for the specific login or source access that would improve it.

## Daily Self-Review

After each run, briefly answer:

- Which sources produced the strongest items?
- Which section was weakest and why?
- Which queries should be added, removed, or rewritten tomorrow?
- Did B站/YouTube/X/WeChat/Xiaohongshu access limit the result?
- Did the final report contain something a creator could actually use today?
- Did X account-pool content change the final selection? If not, why?
- Did B站/小红书/公众号 provide at least one credible tutorial or case candidate?

## Current Known Failure Mode

Recent reports over-weighted official company news and under-weighted creator-native sources. The most common bad pattern:

- Section 3 used product integration commentary instead of real tutorials.
- Section 4 used tool integration/product announcements instead of concrete works or production cases.
- X account-pool and B站 searches were present in theory but did not materially affect final selection.

For every run, explicitly check whether this failure mode happened again. If yes, revise before sending.

If a repeatable improvement is found, update `references/source-strategy.md` or this rubric. Keep changes small and specific.

## User Feedback Loop

When the user says a section is “not right,” interpret it as a quality signal:

- For tutorials, increase concrete workflow/tutorial searches and reduce news commentary.
- For cases, search platform-native works and production breakdowns, not just AI company announcements.
- For creative relevance, score from the creator's job-to-be-done, not from general AI industry importance.

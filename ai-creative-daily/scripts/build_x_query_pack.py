#!/usr/bin/env python3
"""Build prioritized X search queries from references/x-lists.json."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path


PRIORITY = {
    "kol_creators": 20,
    "kol_chinese": 12,
    "creative_video_tools": 10,
    "creative_image_tools": 8,
    "audio_voice_music": 6,
    "official_ai_platforms": 8,
    "ai_creative_tools": 8,
    "founders_researchers": 5,
}

LANE_ORDER = [
    "kol_creators",
    "kol_chinese",
    "creative_video_tools",
    "creative_image_tools",
    "audio_voice_music",
    "ai_creative_tools",
    "official_ai_platforms",
    "founders_researchers",
]


def load_lists(path: Path) -> list[dict]:
    if not path.exists() and str(path) == "ai-creative-daily/references/x-lists.json":
        fallback = Path("sources/x-lists.json")
        if fallback.exists():
            path = fallback
    data = json.loads(path.read_text())
    return data.get("lists", [])


def account_queries(handle: str, month: str, day: str, year: str) -> list[str]:
    date = f"{month} {day} {year}".strip()
    return [
        f"site:x.com/{handle} \"workflow\" OR \"tutorial\" OR \"breakdown\" OR \"prompt guide\"",
        f"site:x.com/{handle} \"behind the scenes\" OR \"case study\" OR \"making of\"",
        f"site:x.com/{handle} \"AI short film\" OR \"AI video\" OR \"made with\" OR \"showcase\"",
        f"site:x.com/{handle} \"Runway\" OR \"Kling\" OR \"Seedance\" OR \"Midjourney\" OR \"Veo\" OR \"Sora\"",
        f"site:x.com/{handle} \"camera\" OR \"shot\" OR \"storyboard\" OR \"character consistency\"",
        f"{handle} AI creative workflow {date}",
        f"{handle} AI video prompt camera workflow {month} {year}",
        f"{handle} AI generated video case study showcase {month} {year}",
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x-lists", default="ai-creative-daily/references/x-lists.json")
    parser.add_argument("--date", help="ISO date, e.g. 2026-04-30. Overrides month/day/year.")
    parser.add_argument("--month")
    parser.add_argument("--day")
    parser.add_argument("--year")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    args = parser.parse_args()

    if args.date:
        parsed = datetime.strptime(args.date, "%Y-%m-%d")
        month = parsed.strftime("%B")
        day = str(parsed.day)
        year = str(parsed.year)
    else:
        missing = [name for name in ("month", "day", "year") if not getattr(args, name)]
        if missing:
            parser.error("--date or --month/--day/--year is required")
        month = args.month
        day = args.day
        year = args.year

    lists = load_lists(Path(args.x_lists))
    by_id = {item.get("id", ""): item for item in lists}
    ordered = [by_id[list_id] for list_id in LANE_ORDER if list_id in by_id]
    ordered.extend(item for item in lists if item.get("id", "") not in LANE_ORDER)

    out = []
    for item in ordered:
        list_id = item.get("id", "")
        limit = PRIORITY.get(list_id, 0)
        if not limit:
            continue
        for account in item.get("accounts", [])[:limit]:
            handle = account.get("handle")
            if not handle:
                continue
            out.append(
                {
                    "list_id": list_id,
                    "handle": handle,
                    "note": account.get("note", ""),
                    "queries": account_queries(handle, month, day, year),
                }
            )

    if args.format == "json":
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        for item in out:
            print(f"# {item['list_id']} / @{item['handle']} - {item['note']}")
            for query in item["queries"]:
                print(query)
            print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

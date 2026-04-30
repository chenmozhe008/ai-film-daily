#!/usr/bin/env python3
"""Preflight checks for AI creative daily collection quality."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


CHINESE_TUTORIAL_QUERIES = [
    "site:bilibili.com AI视频 工作流 可灵 即梦 角色一致性",
    "site:bilibili.com AI短剧 教程 分镜 运镜",
    "site:bilibili.com Midjourney Runway Kling 工作流",
    "site:xiaohongshu.com AI短剧 工作流 可灵 即梦",
    "site:xiaohongshu.com AI绘画 角色一致性 工作流",
    "site:mp.weixin.qq.com AI短剧 工作流 可灵 即梦",
    "site:mp.weixin.qq.com AI视频 角色一致性 分镜",
]

CASE_QUERIES = [
    "site:bilibili.com AI短剧 可灵 即梦 播放",
    "site:bilibili.com AI生成 短片 可灵 即梦",
    "site:bilibili.com AI音乐 MV AI生成",
    "site:x.com AI short film Runway Kling Seedance",
    "site:x.com AI video showcase Midjourney Runway Kling",
    "site:youtube.com AI generated short film Runway Kling",
    "site:xiaohongshu.com AI短剧 作品 可灵 即梦",
]

OFFICIAL_QUERIES = [
    "OpenAI announcement AI video creator workflow",
    "Anthropic Claude creative workflow announcement",
    "Google DeepMind Gemini Veo creator update",
    "Runway Luma Kling Seedance AI video update",
]


def run_query_pack(date: str) -> str:
    cmd = [
        sys.executable,
        "ai-creative-daily/scripts/build_x_query_pack.py",
        "--date",
        date,
        "--format",
        "text",
    ]
    return subprocess.check_output(cmd, text=True)


def line_numbers(text: str) -> list[tuple[int, str]]:
    return [(idx, line) for idx, line in enumerate(text.splitlines(), 1) if line.startswith("# ")]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--format", choices=["json", "text"], default="text")
    args = parser.parse_args()

    required_files = [
        "ai-creative-daily/SKILL.md",
        "ai-creative-daily/references/source-strategy.md",
        "ai-creative-daily/references/quality-rubric.md",
        "ai-creative-daily/scripts/build_x_query_pack.py",
        "ai-creative-daily/scripts/bootstrap_lark_cli_cloud.sh",
    ]
    file_status = {path: Path(path).is_file() and Path(path).stat().st_size > 0 for path in required_files}

    query_pack = run_query_pack(args.date)
    headings = line_numbers(query_pack)
    first_heading = headings[0][1] if headings else ""
    first_80 = "\n".join(query_pack.splitlines()[:80])
    first_30_headings = [heading for _, heading in headings[:30]]

    def first_index(prefix: str) -> int:
        for idx, heading in headings:
            if heading.startswith(f"# {prefix}"):
                return idx
        return 999999

    x_status = {
        "first_block_is_kol_creators": first_heading.startswith("# kol_creators"),
        "kol_chinese_before_official": first_index("kol_chinese") < first_index("official_ai_platforms"),
        "official_not_in_first_80_lines": "# official_ai_platforms" not in first_80,
        "first_30_headings": first_30_headings,
    }

    query_plan = {
        "x_account_pool": {
            "minimum_candidates_before_filtering": 10,
            "minimum_creator_candidates": 5,
            "source": "build_x_query_pack.py",
        },
        "chinese_tutorial_queries": CHINESE_TUTORIAL_QUERIES,
        "case_queries": CASE_QUERIES,
        "official_queries": OFFICIAL_QUERIES,
    }

    hard_pass = all(file_status.values()) and all(
        [
            x_status["first_block_is_kol_creators"],
            x_status["kol_chinese_before_official"],
            x_status["official_not_in_first_80_lines"],
            len(CHINESE_TUTORIAL_QUERIES) >= 7,
            len(CASE_QUERIES) >= 7,
        ]
    )

    result = {
        "date": args.date,
        "hard_pass": hard_pass,
        "file_status": file_status,
        "x_status": x_status,
        "query_plan": query_plan,
        "remaining_manual_verification": [
            "Actual web/search results still need date, traction, and link verification before writing Feishu.",
            "Bilibili/Xiaohongshu/WeChat login state can materially improve actual result quality.",
            "Feishu cloud push requires private environment variables; this smoke does not print or require them.",
        ],
    }

    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"date: {result['date']}")
        print(f"hard_pass: {str(result['hard_pass']).lower()}")
        print("files:")
        for path, ok in file_status.items():
            print(f"- {path}: {str(ok).lower()}")
        print("x_status:")
        for key, value in x_status.items():
            if key != "first_30_headings":
                print(f"- {key}: {str(value).lower()}")
        print("first_30_headings:")
        for heading in first_30_headings:
            print(f"- {heading}")
        print("query_lanes:")
        print(f"- chinese_tutorial_queries: {len(CHINESE_TUTORIAL_QUERIES)}")
        print(f"- case_queries: {len(CASE_QUERIES)}")
        print(f"- official_queries: {len(OFFICIAL_QUERIES)}")
    return 0 if hard_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())

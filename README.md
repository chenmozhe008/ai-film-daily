<p align="center">
  <h1 align="center">AI Film & Creation Daily</h1>
  <p align="center">
    <strong>面向影视创作者的 AI 信息日报</strong><br>
    <em>Daily AI intelligence briefing for filmmakers and content creators</em>
  </p>
  <p align="center">
    <a href="daily/2026-04-13.md">📋 Latest Issue</a> · 
    <a href="#目录结构">📁 Archive</a> · 
    <a href="#贡献指南">🤝 Contribute</a> · 
    <a href="https://github.com/chenmozhe008/ai-film-creation-daily/issues">💬 Issues</a>
  </p>
</p>

---

## 📖 关于 / About

**AI Film & Creation Daily** 是一份面向影视创作者的每日 AI 信息简报。不是泛 AI 新闻聚合，也不是技术圈的工具快讯——**只收录对影视创作者有实际参考价值的信息**。

**AI Film & Creation Daily** is a daily AI intelligence briefing built for filmmakers and content creators. Not a generic AI news aggregator — **only information with real creative value makes the cut.**

### 栏目结构 / Sections

| # | 栏目 | 内容 |
|---|------|------|
| 1 | **行业与平台动向** | 模型发布、平台能力、融资、政策、生态变化 |
| 2 | **工具与能力更新** | 对创作链路真正有帮助的能力更新 |
| 3 | **方法与经验** | 可执行、可迁移、可复用的创作方法 |
| 4 | **作品 / 案例** | 值得拆解的 AI 影视作品和传播样本 |

### 时间窗口 / Time Window

- **严格 24 小时**：前一天 08:00 ~ 当天 08:00（Asia/Shanghai）
- 超过 36h 的内容，无论多重要都不纳入
- **Strict 24-hour window**: previous day 08:00 ~ current day 08:00 (Asia/Shanghai)
- Content older than 36h is excluded regardless of importance

---

## 🏗️ 系统架构 / Architecture

```
┌─────────────────────────────────────────────────────┐
│                   数据采集层 / Collection              │
├─────────────┬──────────────┬───────────┬─────────────┤
│ RSS 官方源   │ X/Twitter   │ HN/GitHub │ web_search  │
│ 18+ feeds   │ 107 账号    │ Trending  │ 多引擎聚合   │
├─────────────┼──────────────┼───────────┼─────────────┤
│ 微信公众号   │ B站作品搜索  │ 国产工具   │ 英文科技媒体  │
│ 10+ 账号    │ bili-cli    │ 即梦/可灵  │ TC/Verge等  │
└──────┬──────┴──────┬───────┴─────┬─────┴──────┬──────┘
       │             │             │            │
       ▼             ▼             ▼            ▼
┌─────────────────────────────────────────────────────┐
│              处理层 / Processing Pipeline              │
├─────────────┬──────────────┬────────────────────────┤
│ 时间校验     │ 创作者关联度  │ 事件级去重              │
│ 24h/36h 窗口 │ 6 角色评分   │ 同一事件只保留 1 条      │
├─────────────┴──────────────┴────────────────────────┤
│ 来源权重排序 → 板块归类 → 摘要标准化 → 总量控制       │
└──────────────────────┬──────────────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
┌────────────┐  ┌────────────┐  ┌────────────┐
│ 飞书文档    │  │ GitHub     │  │ 飞书推送    │
│ Feishu Doc │  │ Daily Push │  │ Card Alert │
└────────────┘  └────────────┘  └────────────┘
```

---

## 🔧 采集源 / Data Sources

### 主链路（国际优先） / Primary Sources (International)

| 来源 | 工具 | 说明 |
|------|------|------|
| RSS 官方源 | feedparser | OpenAI / Google / Anthropic / Runway / Midjourney 等 18+ 官方博客 |
| X / Twitter | twitter-cli | 107 个 AI 账号全量扫描，覆盖 7 个分类 |
| Hacker News | REST API | Top 200 stories，筛选 AI 相关 |
| GitHub Trending | REST API | AI / 视频生成 / 图像生成 相关项目 |
| 英文科技媒体 | web_fetch + web_search | TechCrunch / The Verge / Reuters / Bloomberg / Wired 等 |

### 补充链路（中文辅助） / Secondary Sources (Chinese)

| 来源 | 工具 | 说明 |
|------|------|------|
| 国产工具官网 | Playwright | 即梦 / 可灵 / 海螺 SPA 网站渲染采集 |
| 微信公众号 | wechat-article-exporter + Exa | 数字生命卡兹克 / 量子位 / 机器之心 等 10+ 账号 |
| B站作品搜索 | bili-cli | AI 短片 / 动画 / 教程，按播放量筛选 |
| 国产工具扫描 | web_search | 即梦 / Seedance / Kling / Vidu 更新关键词 |
| 小红书 / 抖音 | web_search 兜底 | 创作者使用反馈、案例讨论 |

### X 账号分类 / Twitter Account Categories

107 个账号分布在 7 个分类（详见 `x-lists.json`）：

| 分类 | 数量 | 示例 |
|------|------|------|
| 官方 AI 平台 | 30 | OpenAI, AnthropicAI, GoogleDeepMind, MetaAI |
| AI 视频创作工具 | 19 | RunwayML, pika_labs, LumaLabsAI, Kling_ai |
| AI 图片生成工具 | 13 | midjourney, stabilityai, BlackForestLabs |
| AI 音频工具 | 6 | ElevenLabsHQ, SudoScribe |
| 创作辅助工具 | 14 | Canva, Adobe, CapCut |
| AI 创作者 KOL | 8 | @demoan, @nickfloats |
| 中文 AI 博主 | 17 | 数字生命卡兹克, AI工具集 |

---

## 🎯 内容筛选机制 / Content Filtering

### 创作者关联度评分 / Creator Relevance Scoring

每条候选内容从 **6 类创作者角色** 分别打分（1-10）：

| 角色 | 关注重点 |
|------|----------|
| R1 AI 编导 / 导演 | 叙事、分镜、镜头语言、视觉叙事 |
| R2 AI 制片人 | 成本、效率、商业机会、平台政策 |
| R3 视觉 / 美术 | 风格生成、角色一致性、视觉开发 |
| R4 后期 / 声音 | 配音、字幕、调色、视频后处理 |
| R5 短剧 / 短内容 | 批量生产、IP 衍生、平台分发 |
| R6 技术整合者 | 工具链打通、API 集成、工作流自动化 |

**通过线：**
- 行业动向 / 工具更新：至少 2 类角色 ≥ 6
- 方法与经验 / 作品案例：至少 2 类角色 ≥ 8

### 时间校验 / Time Validation

- 每条候选必须带明确的发布日期（YYYY-MM-DD）
- 无法确认日期 → 直接淘汰
- 超过 24h 窗口 → 淘汰（除非有窗口内新进展）
- 超过 36h → 无条件淘汰

### 去重规则 / Deduplication

- 同一事件多家报道 → 只保留最权威的一手源
- 英文一手源 + 中文转载 → 只保留英文源
- 连续火爆的作品 → 每 5 天检查一次，仍在传播才简短提及

---

## 📁 目录结构 / Directory Structure

```
ai-film-creation-daily/
├── daily/                    # 每日日报
│   ├── 2026-04-13.md        # 示例：首期日报
│   └── ...
├── .github/
│   └── workflows/            # 自动化推送（计划中）
├── .gitignore                # 安全过滤
├── LICENSE                   # MIT License
└── README.md                 # 本文件
```

---

## 🛠️ 技术栈 / Tech Stack

| 组件 | 技术 | 说明 |
|------|------|------|
| AI 引擎 | OpenClaw | 自动化 Agent 平台，驱动整个采集-处理-输出流程 |
| LLM | GLM-5 / Gemini | 内容筛选、评分、摘要生成 |
| X 采集 | twitter-cli | Cookie 认证，GraphQL API |
| B站采集 | bili-cli | 搜索 + 结构化数据 |
| 网页采集 | Playwright | SPA 网站渲染（即梦 / 可灵 / 海螺） |
| 微信公众号 | wechat-article-exporter | 在线 API，需扫码授权 |
| RSS | feedparser | 18+ 官方博客源 |
| 输出 | 飞书文档 + GitHub | 飞书文档存档 + GitHub 公开发布 |
| 推送 | 飞书消息卡片 | 每日自动推送摘要 |

---

## 📅 日报列表 / Archive

| 日期 | 链接 | 摘要 |
|------|------|------|
| 2026-04-13 | [📄 查看](daily/2026-04-13.md) | Wan2.7 登顶 / GPT-5.3 Instant Mini / Runway 4K / 牌子 1857万 |

---

## 🤝 贡献指南 / Contributing

欢迎所有人参与完善这份日报！以下是一些可以贡献的方向：

### 想法 / Ideas

- 🔍 **新增信息源**：发现好的 AI 创作信息源？提 [Issue](https://github.com/chenmozhe008/ai-film-creation-daily/issues) 告诉我们
- ✏️ **内容纠错**：日报内容有误？随时指出
- 📊 **栏目建议**：想新增或调整栏目？在 [Discussions](https://github.com/chenmozhe008/ai-film-creation-daily/discussions) 里讨论
- 🔧 **工具推荐**：有好用的 AI 创作工具？分享出来
- 🌐 **多语言**：希望增加英文版日报？帮我们翻译

### 方式 / How

1. **Fork** 本仓库
2. 创建特性分支 (`git checkout -b feature/xxx`)
3. 提交修改 (`git commit -m 'add xxx'`)
4. 推送分支 (`git push origin feature/xxx`)
5. 提交 **Pull Request**

或者直接在 [Issues](https://github.com/chenmozhe008/ai-film-creation-daily/issues) 和 [Discussions](https://github.com/chenmozhe008/ai-film-creation-daily/discussions) 里讨论。

### 示例贡献 / Example Contributions

- 💡 提交一个新的 RSS 源地址
- 📝 补充日报中遗漏的重要信息
- 🌍 翻译日报为英文版本
- 🐛 修复采集脚本的 Bug
- 📖 改进 README 文档
- 🎬 推荐值得收录的 AI 影视作品

---

## 📜 许可证 / License

[MIT License](LICENSE) © 2026

---

<p align="center">
  <sub>Built with ❤️ by AI Film & Creation Daily Bot · Powered by <a href="https://docs.openclaw.ai">OpenClaw</a></sub>
</p>

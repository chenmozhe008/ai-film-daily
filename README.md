<p align="center">
  <h1 align="center">AI Film & Creation Daily</h1>
  <p align="center">
    <strong>面向影视创作者的 AI 信息日报</strong><br>
    <em>Daily AI intelligence briefing for filmmakers and content creators</em>
  </p>
  <p align="center">
    <a href="daily/2026-04-13.md">📋 Latest Issue</a> · 
    <a href="#日报列表--archive">📁 Archive</a> · 
    <a href="#贡献指南--contributing">🤝 Contribute</a> · 
    <a href="https://github.com/chenmozhe008/ai-film-creation-daily/issues">💬 Issues</a>
  </p>
</p>

---

## 关于 / About

**AI Film & Creation Daily** 是一份面向影视创作者的每日 AI 信息简报。不是泛 AI 新闻聚合，也不是技术圈的工具快讯——**只收录对影视创作者有实际参考价值的信息**。

**AI Film & Creation Daily** is a daily AI intelligence briefing for filmmakers and content creators. Not a generic AI news aggregator — **only information with real creative value makes the cut.**

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
- *Strict 24-hour window*: previous day 08:00 ~ current day 08:00 (Asia/Shanghai). Content older than 36h is excluded.

---

## 系统架构 / Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  数据采集层 / Collection Layer              │
├─────────────┬──────────────┬───────────┬────────────────┤
│  RSS 官方源   │  X / Twitter │  HN/GitHub │   web_search   │
│  18+ feeds   │  全量账号扫描  │  Trending  │   多引擎聚合    │
├─────────────┼──────────────┼───────────┼────────────────┤
│  微信公众号   │   B站作品搜索  │  国产工具   │  英文科技媒体    │
│  10+ 账号    │   bili-cli   │  即梦/可灵  │  TC/Verge 等   │
└──────┬──────┴──────┬───────┴─────┬─────┴───────┬────────┘
       │             │             │             │
       ▼             ▼             ▼             ▼
┌─────────────────────────────────────────────────────────┐
│               处理层 / Processing Pipeline                 │
├──────────────┬──────────────┬───────────────────────────┤
│  时间校验     │  创作者关联度  │      事件级去重             │
│  24h/36h 窗口 │  6 角色评分   │  同一事件只保留 1 条        │
├──────────────┴──────────────┴───────────────────────────┤
│  来源权重排序 → 板块归类 → 摘要标准化 → 总量控制           │
└──────────────────────┬──────────────────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
┌────────────┐  ┌────────────┐  ┌────────────┐
│  飞书文档    │  │  GitHub    │  │  飞书推送    │
│  Feishu Doc │  │ Daily Push │  │ Card Alert │
└────────────┘  └────────────┘  └────────────┘
```

---

## 采集源 / Data Sources

### 主链路（国际优先）/ Primary Sources (International)

| 来源类型 | 工具 | 覆盖范围 |
|----------|------|----------|
| RSS 官方源 | feedparser | AI 公司官方博客（OpenAI / Anthropic / Runway / Midjourney 等 18+ 源） |
| X / Twitter | twitter-cli | 7 个分类、100+ 账号全量扫描（官方平台 / 视频工具 / 图片工具 / 音频 / 创作辅助 / 创作者 / 中文博主） |
| Hacker News | REST API | Top 200 stories，筛选 AI 相关高赞内容 |
| GitHub Trending | REST API | AI / 视频生成 / 图像生成相关新项目 |
| 英文科技媒体 | web_fetch + web_search | TechCrunch / The Verge / Reuters / Bloomberg / Wired 等 |

### 补充链路（中文辅助）/ Secondary Sources (Chinese)

| 来源类型 | 工具 | 覆盖范围 |
|----------|------|----------|
| 国产工具官网 | Playwright | 即梦 / 可灵 / 海螺 SPA 网站，捕获弹窗 / Banner / 更新提示 |
| 微信公众号 | wechat-article-exporter + Exa | 10+ 核心账号（中文方法总结 / 创作复盘 / 案例拆解） |
| B站作品搜索 | bili-cli | AI 短片 / 动画 / 教程，按播放量筛选 |
| 国产工具扫描 | web_search | 即梦 / Seedance / Kling / Vidu 更新关键词主动扫描 |
| 小红书 / 抖音 | web_search 兜底 | 创作者使用反馈、案例讨论 |

---

## 内容筛选机制 / Content Filtering

### 创作者关联度评分 / Creator Relevance Scoring

每条候选内容从 **6 类创作者角色** 分别打分（1-10），必须满足通过线才能入选：

| 角色 | 关注重点 | Role Focus |
|------|----------|------------|
| R1 AI 编导 / 导演 | 叙事、分镜、镜头语言、视觉叙事 | Narrative, storyboard, lens language |
| R2 AI 制片人 | 成本、效率、商业机会、平台政策 | Cost, efficiency, business, platform policy |
| R3 视觉 / 美术 | 风格生成、角色一致性、视觉开发 | Style, character consistency, visual dev |
| R4 后期 / 声音 | 配音、字幕、调色、视频后处理 | Audio, subtitles, color, post-production |
| R5 短剧 / 短内容 | 批量生产、IP 衍生、平台分发 | Mass production, IP, distribution |
| R6 技术整合者 | 工具链打通、API 集成、工作流自动化 | Toolchain, API, workflow automation |

**通过线 / Passing Threshold:**
- 行业动向 / 工具更新：至少 2 类角色 ≥ 6
- 方法与经验 / 作品案例：至少 2 类角色 ≥ 8

### 多重校验 / Validation Pipeline

1. **时间校验** — 每条必须带明确发布日期，超 24h 淘汰，超 36h 无条件淘汰
2. **去重** — 同一事件只保留最权威的一手源，英文源优先于中文转载
3. **持续性跟踪** — 爆款作品每 5 天检查一次，仍在传播才简短提及，避免每日重复

---

## 技术栈 / Tech Stack

| 组件 | 技术 | 说明 |
|------|------|------|
| AI 引擎 | [OpenClaw](https://docs.openclaw.ai) | 自动化 Agent 平台，驱动整个采集→处理→输出流程 |
| LLM | GLM-5 / Gemini | 内容筛选、评分、摘要生成 |
| X 采集 | twitter-cli | Cookie 认证 + GraphQL API，全量账号扫描 |
| B站采集 | bili-cli | 结构化搜索 + 播放量/播放量排序 |
| 网页采集 | Playwright | SPA 网站渲染（国产工具官网） |
| 微信公众号 | wechat-article-exporter | 在线 API + Exa 搜索双重覆盖 |
| RSS | feedparser | 18+ 官方博客源自动抓取 |
| 输出 | 飞书文档 + GitHub | 飞书文档存档 + GitHub 公开发布 |

---

## 日报列表 / Archive

| 日期 | 链接 | 摘要 |
|------|------|------|
| 2026-04-13 | [📄 查看](daily/2026-04-13.md) | Wan2.7 登顶 / GPT-5.3 Instant Mini / Runway 4K / 牌子 1857万 |

---

## 贡献指南 / Contributing

欢迎所有人参与完善这份日报！

### 可以贡献什么 / What You Can Contribute

- 💡 **推荐信息源** — 发现好的 AI 创作信息源？提 [Issue](https://github.com/chenmozhe008/ai-film-creation-daily/issues) 告诉我们（RSS 源、公众号、YouTube 频道、X 账号等）
- ✏️ **内容纠错** — 日报内容有误？随时指出
- 📊 **栏目建议** — 想新增或调整栏目？在 [Discussions](https://github.com/chenmozhe008/ai-film-creation-daily/discussions) 里讨论
- 🔧 **工具推荐** — 有好用的 AI 创作工具？分享出来
- 🎬 **作品推荐** — 发现值得拆解的 AI 影视作品？提交给我们

### 如何贡献 / How to Contribute

1. **Fork** 本仓库
2. 创建特性分支 (`git checkout -b feature/xxx`)
3. 提交修改 (`git commit -m 'add xxx'`)
4. 推送分支 (`git push origin feature/xxx`)
5. 提交 **Pull Request**

也可以直接在 [Issues](https://github.com/chenmozhe008/ai-film-creation-daily/issues) 或 [Discussions](https://github.com/chenmozhe008/ai-film-creation-daily/discussions) 中讨论。

---

## 许可证 / License

[MIT License](LICENSE) © 2026

---

<p align="center">
  <sub>Built with ❤️ by AI Film & Creation Daily Bot · Powered by <a href="https://docs.openclaw.ai">OpenClaw</a></sub>
</p>

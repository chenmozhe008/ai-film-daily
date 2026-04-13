# 贡献指南

感谢你对 AI Film & Creation Daily 的关注！我们欢迎以下类型的贡献：

## 如何贡献

### 1. 推荐信息源

我们持续扩充数据源覆盖范围。如果你知道优质的 AI 创作相关信息源，请通过 Issue 提交：

- **RSS 源**：编辑 `sources/rss-feeds.json`，提交 PR
- **X/Twitter 账号**：编辑 `sources/x-lists.json`，说明账号类别和关注理由
- **其他平台**：在 Issue 中描述信息源及其价值

### 2. 纠错与补充

如果你发现日报中的错误（链接失效、事实偏差、时间窗口违规等），请：

- 提交 Issue 并标注日期和具体条目
- 或直接提交 PR 修正 `daily/YYYY-MM-DD.md`

### 3. 提交作品 / 案例

如果你有值得收录的 AI 创作案例：

- 在 Discussions 中分享作品链接和简要说明
- 说明使用了哪些 AI 工具和创作方法

## 数据源文件说明

| 文件 | 说明 |
|------|------|
| `sources/rss-feeds.json` | RSS 订阅源列表（官方博客、科技媒体） |
| `sources/x-lists.json` | X/Twitter 监控账号列表（7 类，100+ 账号） |
| `sources/keywords.json` | 内容过滤关键词（中英文，按板块分类） |
| `sources/kol-sources.json` | KOL 发现种子池（按创作方向分组） |
| `sources/blacklist.txt` | 内容黑名单（低质量源/关键词） |
| `sources/template.md` | 日报输出模板 |

## PR 规范

- 分支名：`add/source-name` 或 `fix/issue-description`
- 提交信息使用中文或英文均可
- 数据源 PR 请说明推荐理由

## 行为准则

请保持友善和建设性的交流。我们专注于为影视创作者提供有价值的 AI 情报。

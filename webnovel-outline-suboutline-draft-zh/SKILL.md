---
name: webnovel-outline-suboutline-draft-zh
description: 使用中文推进网文创作的分层工作流：先生成总大纲，再拆解子大纲，基于风格参考提炼风格卡后产出正文，并在同一项目文件夹内同步维护设定集与长线伏笔完成统计。当用户要求写网文、扩写章节、搭建剧情结构、保持文风一致、按样文仿写风格、维护世界观设定或追踪伏笔回收时使用此技能。
---

# 网文分层写作（中文）

## 目标
在一个单独项目文件夹中维护完整链路：
- `总大纲`：故事骨架与长线设计。
- `子大纲`：章节级拆解与场景推进。
- `风格参考`：样文、风格卡与执行约束。
- `正文`：最终可直接阅读的章节内容。
- `设定集`：人物、世界、势力、规则等持续更新。
- `伏笔统计`：长线事件埋设、回收、完成率、逾期项。

## 单文件夹约束
先运行脚本初始化工作区，再在该目录内完成所有写作与更新：

```bash
python scripts/init_story_workspace.py --root <父目录> --name <作品名>
```

初始化后只在该目录工作，默认文件如下：
- `00-项目说明.md`
- `01-总大纲.md`
- `02-子大纲.md`
- `04-设定集.md`
- `05-长线伏笔.csv`
- `06-长线统计.md`
- `风格参考/`
- `风格参考/01-样文摘录.md`
- `风格参考/02-风格卡.md`
- `正文/`（正文章节目录）
- `正文/第001章.md`（首章模板）

## 标准流程

### 1) 产出总大纲
使用 `references/outline-template.md` 的结构填写：
- 明确核心卖点、主线冲突、阶段转折、结局兑现。
- 在总大纲里预先标注可追踪的长线事件 ID（如 `F001`）。
- 需要更多剧情结构方案时，补充读取 `references/writing-techniques/plot-structures.md`。

### 2) 拆解子大纲
使用 `references/suboutline-template.md` 按章节拆解：
- 每章写清目标、冲突、转折、钩子。
- 每章必须标记“埋设伏笔/回收伏笔”并引用对应事件 ID。
- 设计章节开头和章节结尾时，补充读取 `references/writing-techniques/chapter-guide.md` 与 `references/writing-techniques/hook-techniques.md`。

### 3) 建立风格参考
优先读取并维护 `风格参考/`：
- `风格参考/01-样文摘录.md`：存放用户给出的参考片段。
- `风格参考/02-风格卡.md`：提炼可执行的风格约束。

当用户提出“按某作者/某段文字风格写”或“保持已有章节文风一致”时：
- 必须先更新风格卡，再生成正文。
- 仅迁移风格特征，不复写样文原句。

### 4) 生成正文
使用 `references/draft-template.md` 编写正文，并将章节写入 `正文/` 目录：
- 文件命名统一为 `正文/第NNN章.md`（如 `正文/第001章.md`、`正文/第002章.md`）。
- 正文前先读取 `风格参考/02-风格卡.md`，严格执行其中“执行约束”。
- 保持与子大纲的事件顺序一致。
- 场景中兑现子大纲承诺的关键信息与节奏。
- 对用户回复时，先给可直接阅读的正文内容，再给更新说明。
- 对话密集场景优先读取 `references/writing-techniques/dialogue-writing.md`。
- 需要扩写时读取 `references/writing-techniques/content-expansion.md`。
- 完稿前读取 `references/writing-techniques/quality-checklist.md` 与 `references/writing-techniques/consistency.md` 做自检。

### 5) 更新设定集
按 `references/setting-bible-template.md` 同步维护：
- 新角色、新地点、新规则、新势力关系出现后立即登记。
- 若设定发生变更，保留“旧设定 -> 新设定 -> 变更原因”。
- 角色塑造不足时补充读取 `references/writing-techniques/character-building.md` 和 `references/writing-techniques/character-template.md`。

### 6) 维护伏笔与统计
手动更新 `05-长线伏笔.csv` 后运行：

```bash
python scripts/foreshadow_stats.py --csv <项目目录>/05-长线伏笔.csv --out <项目目录>/06-长线统计.md --current-chapter <当前章节号>
```

执行后得到：
- 状态分布（埋设中/回收中/已回收/弃用）
- 完成率（已回收占活跃伏笔）
- 未完成清单
- 逾期待回收项（当提供 `--current-chapter` 时）

## 写作技法库（必须按需参考）
`references/writing-techniques/` 内的文件为写作技法总库。触发相关任务时必须读取对应文件，而不是只依赖默认模板。

- `chapter-guide.md`：章节开头、前20%抓人、开篇错误规避。
- `chapter-template.md`：章节结构底稿（章节概要/正文/备注）。
- `character-building.md`：人物弧光、行为逻辑、关系塑造。
- `character-template.md`：人物档案模板。
- `consistency.md`：跨章节一致性与状态跟踪。
- `content-expansion.md`：扩写手段（细节/内心/感官/支线）。
- `dialogue-writing.md`：对话目的性、简洁度、格式规范。
- `hook-techniques.md`：悬念钩子库与章节收束策略。
- `outline-template.md`：另一套大纲模板（与本技能默认大纲模板并存）。
- `plot-structures.md`：三幕式、英雄之旅等结构框架。
- `quality-checklist.md`：交付前质量检查项。

如果 `references/outline-template.md` 与 `references/writing-techniques/outline-template.md` 冲突：
- 默认优先 `references/outline-template.md`（本技能流程模板）。
- 用户明确要求“按写作技法模板”时，切换为 `references/writing-techniques/outline-template.md`。

## 回复格式
按以下顺序输出，保证用户先拿到正文：
1. `正文成稿`
2. `本轮同步更新`（总大纲/子大纲/设定集）
3. `伏笔统计摘要`（引用 `06-长线统计.md` 核心数字）

## 参考文件读取策略
- 需要规划故事框架时读取 `references/outline-template.md`。
- 需要拆章节时读取 `references/suboutline-template.md`。
- 需要控制文风时读取 `风格参考/01-样文摘录.md` 和 `风格参考/02-风格卡.md`。
- 需要维护世界观时读取 `references/setting-bible-template.md`。
- 需要理解伏笔字段时读取 `references/foreshadow-schema.md`。
- 需要写作技法时按任务读取 `references/writing-techniques/*.md` 对应文件。

---
id: local/novelist-zh
owner_id: local
name: 中文网文写作
description: 使用中文网文分层写作工作流完成从总大纲、子大纲、风格卡到正文、设定集、角色状态、读者面信息与长线伏笔统计的闭环创作。适用于新建中文网文项目、续写章节、按样文稳定文风、维护世界观一致性、跟踪伏笔回收、以及在交付前执行章节门禁验收。
version: 0.1.0
icon: "\U0001F4DA"
author: Leon Greek
metadata:
  clawdbot:
    emoji: "\U0001F4DA"
    requires:
      bins:
        - python
---

# 中文网文分层写作

将所有产物落在同一个项目目录内，保持以下链路同步：

- `01-总大纲.md`
- `02-子大纲.md`
- `风格参考/01-样文摘录.md`
- `风格参考/02-风格卡.md`
- `正文/第NNN章.md`
- `04-设定集.md`
- `05-长线伏笔.csv`
- `06-长线统计.md`
- `07-当前角色状态.md`
- `08-叙事引擎报告.md`
- `09-读者面信息.md`

## 初始化项目

在需要新建作品目录时，运行：

```bash
python "{baseDir}/scripts/init_story_workspace.py" --root <父目录> --name <作品名>
```

初始化后，只在生成的作品目录内工作。

## 强制工作流

在开始写任何章节前，按顺序执行：

1. 项目体检

```bash
python "{baseDir}/scripts/narrative_engine.py" doctor --project <项目目录>
```

2. 生成章节上下文

```bash
python "{baseDir}/scripts/narrative_engine.py" context --project <项目目录> --chapter <章节号> --create-chapter
```

3. 生成章节分镜纲

```bash
python "{baseDir}/scripts/narrative_engine.py" storyboard --project <项目目录> --chapter <章节号> --target-chars 3500 --create-context
```

4. 再写正文，并同步回写设定、角色状态、读者面信息、伏笔状态。

5. 交付前执行门禁

```bash
python "{baseDir}/scripts/narrative_engine.py" gate --project <项目目录> --chapter <章节号>
```

只要门禁报告出现 `FAIL`，就不要把该章当成正式交付稿。

## 伏笔统计

每次修改 `05-长线伏笔.csv` 后，运行：

```bash
python "{baseDir}/scripts/foreshadow_stats.py" --csv <项目目录>/05-长线伏笔.csv --out <项目目录>/06-长线统计.md --current-chapter <当前章节号>
```

## 写作规则

- 先结构，后正文。先补齐总大纲和子大纲，再进入章节写作。
- 在按样文模仿文风时，先更新 `风格参考/02-风格卡.md`，再写正文。
- 迁移风格特征，不复写样文原句。
- 保持正文事件顺序与子大纲一致。
- 每章至少推进一条有效信息：世界观、角色关系、主线因果三者之一。
- 每章写完后，回写 `07-当前角色状态.md` 与 `09-读者面信息.md`。
- 若新增角色、地点、规则、势力或设定变更，立即更新 `04-设定集.md`。

## 按需读取的参考文件

根据任务读取这些文件，而不是一次性全读：

- 大纲规划：`{baseDir}/references/outline-template.md`
- 子大纲拆章：`{baseDir}/references/suboutline-template.md`
- 风格卡与样文：`{baseDir}/references/style-card-template.md`
- 章节分镜：`{baseDir}/references/storyboard-template.md`
- 设定维护：`{baseDir}/references/setting-bible-template.md`
- 角色状态：`{baseDir}/references/character-state-template.md`
- 读者面信息：`{baseDir}/references/reader-info-template.md`
- 伏笔字段：`{baseDir}/references/foreshadow-schema.md`
- 技法库：`{baseDir}/references/writing-techniques/*.md`

## 回复格式

默认按这个顺序回复：

1. `正文成稿`
2. `本轮同步更新`
3. `门禁结果`
4. `伏笔统计摘要`
5. `角色状态更新摘要`

如果用户明确要求先看草稿，可以先给草稿，但必须标注“未过门禁”。

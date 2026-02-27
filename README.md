# 中文长篇小说写作 AI Skill

一个面向 AI Agent 的网文长篇写作技能包，提供从立项到连载的分层工作流：

`总大纲 -> 子大纲 -> 风格卡 -> 正文 -> 设定集 -> 伏笔统计`

## 适用场景

- 写中文长篇网文/小说
- 从 0 搭建剧情结构和章节规划
- 按样文抽取风格并保持文风一致
- 持续维护世界观与角色设定
- 追踪长线伏笔并统计回收进度

## 核心能力

- 分层创作：先大纲、后子大纲、再正文，降低长篇失控风险
- 风格管控：通过“样文摘录 + 风格卡”稳定文风
- 设定同步：写作过程中同步更新人物、势力、术法、术语等
- 伏笔闭环：用 CSV 跟踪伏笔状态并自动生成统计报告

## 仓库结构

```text
novelist/
  webnovel-outline-suboutline-draft-zh/   # Skill 本体（SKILL.md、scripts、templates）
  references/                             # 补充写作技法参考
  大纲和子大纲/                            # 你的项目内容（示例）
  设定集/                                  # 你的项目内容（示例）
  风格参考/                                # 你的项目内容（示例）
  正文/                                    # 你的项目内容（示例）
```

## 快速开始

1. 准备环境：`Python 3.9+`
2. 初始化一个新作品目录：

```bash
python webnovel-outline-suboutline-draft-zh/scripts/init_story_workspace.py --root . --name 我的作品
```

3. 在生成的作品目录中按以下顺序创作：
- `01-总大纲.md`
- `02-子大纲.md`
- `风格参考/01-样文摘录.md`
- `风格参考/02-风格卡.md`
- `正文/第NNN章.md`
- `04-设定集.md`
- `05-长线伏笔.csv`

## 伏笔统计命令

更新 `05-长线伏笔.csv` 后执行：

```bash
python webnovel-outline-suboutline-draft-zh/scripts/foreshadow_stats.py \
  --csv <项目目录>/05-长线伏笔.csv \
  --out <项目目录>/06-长线统计.md \
  --current-chapter <当前章节号>
```

会生成：

- 状态分布（埋设中/回收中/已回收/弃用）
- 活跃伏笔完成率
- 未完成清单
- 逾期待回收清单（提供 `--current-chapter` 时）

## 伏笔 CSV 字段

表头固定为：

`id,主线,伏笔内容,首次埋设章节,计划回收章节,实际回收章节,状态,关联人物,备注`

建议状态值只使用：

- `埋设中`
- `回收中`
- `已回收`
- `弃用`

## 建议工作方式

- 每新增一章就同步更新一次设定与伏笔
- 每次改动 `05-长线伏笔.csv` 后立即重建 `06-长线统计.md`
- 长篇过程中优先“先结构后文采”，避免返工

## 来源

Powered by: https://github.com/PenglongHuang/chinese-novelist-skill.git

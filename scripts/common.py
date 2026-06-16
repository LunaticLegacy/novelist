#!/usr/bin/env python3
"""
通用共享库：被 narrative_engine.py 和 foreshadow_stats.py 共用。

在写入内容生成器工具（tools/）时亦可从此处导入以消除模式复制。
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

# ── CSV 字段常量 ──────────────────────────────────────────

REQUIRED_COLUMNS = [
    "id",
    "主线",
    "伏笔内容",
    "首次埋设章节",
    "计划回收章节",
    "实际回收章节",
    "状态",
    "关联人物",
    "备注",
]

DONE_STATUSES = {"已回收"}
INACTIVE_STATUSES = {"弃用"}

# ── CSV 辅助函数 ──────────────────────────────────────────


def normalize_status(value: str) -> str:
    """规范化状态值，空值返回 '未标注'。"""
    text = (value or "").strip()
    return text if text else "未标注"


def normalize_id(value: str) -> str:
    """规范化伏笔 ID 为大写。"""
    return (value or "").strip().upper()


def extract_chapter_num(value: str) -> int | None:
    """从章节字符串（如 '第3章' 或 '第012章'）中提取数字。"""
    text = (value or "").strip()
    if not text:
        return None
    match = re.search(r"\d+", text)
    return int(match.group()) if match else None


def safe_cell(value: str) -> str:
    """转义 Markdown 表格管道符。"""
    return (value or "").replace("|", "\\|").strip()


def load_rows(csv_path: Path) -> list[dict[str, str]]:
    """读取伏笔 CSV 并校验必需字段。"""
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError("CSV 为空或缺少表头。")
        missing = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
        if missing:
            raise ValueError(f"CSV 缺少字段: {', '.join(missing)}")
        return [dict(row) for row in reader]


# ── 通用文本工具 ──────────────────────────────────────────


def count_non_whitespace(text: str) -> int:
    """返回文本中非空白字符的个数。"""
    return len(re.sub(r"\s+", "", text))

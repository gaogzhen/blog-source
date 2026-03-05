#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# ===== 请修改为你要检查的文件路径（相对于脚本运行目录或绝对路径）=====
filepath = 'source/_posts/basis/math/note/高等数学/06定积分的应用/0603-定积分在物理学上的应用-定积分的应用.md'
# =================================================================

print("=" * 50)
print(f"检查文件: {filepath}")
print("文件是否存在:", os.path.exists(filepath))
if not os.path.exists(filepath):
    print("错误：文件不存在，请检查路径。")
    exit(1)

# 1. 以二进制模式读取，查看原始字节（用于检测 BOM 和编码）
with open(filepath, 'rb') as f:
    raw = f.read()
print("\n--- 文件二进制信息 ---")
print("文件大小:", len(raw), "字节")
print("文件开头20字节 (十六进制):", raw[:20].hex())
print("文件开头20字节 (可打印字符):", raw[:20].decode('utf-8', errors='replace'))

# 2. 以 UTF-8 读取文件内容
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    print("\n错误：无法以 UTF-8 编码读取文件，可能不是 UTF-8 编码。")
    # 尝试用系统默认编码读取
    with open(filepath, 'r', encoding='latin-1') as f:
        content = f.read()
    print("已使用 latin-1 编码读取（可能乱码）。")

print("\n--- 文件内容前200字符 (repr) ---")
print(repr(content[:200]))

# 3. 去除可能的 BOM 和空白后判断
if content.startswith('\ufeff'):
    print("\n检测到 UTF-8 BOM，已去除。")
    content_no_bom = content[1:]
else:
    content_no_bom = content

stripped = content_no_bom.lstrip()
print("\n--- Front-matter 判断 ---")
print("去除空白后前20字符 (repr):", repr(stripped[:20]))

if stripped.startswith('---'):
    print("判定结果: ✅ 文件已有 Front-matter (以 '---' 开头)")
else:
    print("判定结果: ❌ 文件没有 Front-matter")

# 4. 如果已有 Front-matter，提取并显示第一段
if stripped.startswith('---'):
    # 简单提取到下一个 '---'
    lines = stripped.splitlines()
    end_index = -1
    for i, line in enumerate(lines[1:], start=1):
        if line.rstrip() == '---':
            end_index = i
            break
    if end_index != -1:
        fm_lines = lines[1:end_index]  # 跳过开头的 '---'
        print("\n--- 已有的 Front-matter 内容 ---")
        for line in fm_lines:
            print(line)
    else:
        print("\n注意：虽然以 '---' 开头，但未找到闭合的 '---'，可能格式不完整。")
print("=" * 50)

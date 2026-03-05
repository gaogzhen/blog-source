import os

filepath = 'source/_posts/basis/math/note/高等数学/06定积分的应用/0603-定积分在物理学上的应用-定积分的应用.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print("原文件前100字符:", repr(content[:100]))

if content.startswith('\ufeff'):
    content = content[1:]
stripped = content.lstrip()
print("去除空白后前50字符:", repr(stripped[:50]))

if stripped.startswith('---'):
    print("判定: 已有 Front-matter")
else:
    print("判定: 无 Front-matter，准备添加")
    # 构造 Front-matter
    title = os.path.splitext(os.path.basename(filepath))[0]
    mtime = os.path.getmtime(filepath)
    from datetime import datetime
    date_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    front_matter = f'''---
title: {title}
date: {date_str}
categories:
tags:
---

'''
    new_content = front_matter + content
    # 备份并写入
    backup = filepath + '.bak'
    os.rename(filepath, backup)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("已添加 Front-matter，原文件备份为", backup)
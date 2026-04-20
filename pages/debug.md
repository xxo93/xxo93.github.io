---
layout: default
title: Debug
---

# 🐞 问题定位

## Doris 内存问题

### 现象
OOM / Query失败

### 排查
- FE日志
- BE memory tracker

### 根因
batch过大 + 内存限制

### 解决
- 降低 batch size
- 分批执行

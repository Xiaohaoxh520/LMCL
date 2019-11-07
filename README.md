# Lite Minecraft Launcher
 **English** [简体中文](https://github.com/jinzhijie/LMCL#简体中文)  
 [**Download 下载**](https://github.com/jinzhijie/LMCL/releases)

# English
## What is LMCL?
 **Lite Minecraft Launcher** is a Python-based minecraft launcher **for servers**. 
 It is also **LITE & SIMPLE**. 
 
## Features
### Released
+ Check Updates of [Paper](https://papermc.io/)
+ Download Paper JAR with [aria2](https://aria2.github.io/)
+ ~~Nothing else...~~
### Planned
+ Launch server
+ The progress bar of download status

---
# 简体中文
## LMCL是个什么玩意？
 **Lite Minecraft Launcher**是一个基于Python的Minecraft**服务器启动器**  
 是一个轻量&精简的 *~~辣鸡~~*

## 特点
### 已发布的
+ 检查[Paper](https://papermc.io/)的更新
+ 使用[aria2](https://aria2.github.io/)下载Paper的JAR文件
+ ~~没了~~ 还会有的，康康下面的
### 计划中的
+ 启动服务端
+ 下载状态进度条

# BUGs
+ 无法获取多线程`return`的值，如无适当方法，将使用`join()`阻塞主线程

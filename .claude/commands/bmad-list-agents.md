---
command: "/bmad-list-agents"
name: "列出所有 BMad 代理"
description: "显示所有已安装的 BMad 代理及其详细信息。"
prompt: |-
  # 列出所有 BMad 代理
  
  显示所有已安装的 BMad 代理及其详细信息。
  
  读取代理清单：`{project-root}/.bmad/_cfg/agent-manifest.csv`
  
  解析并显示所有可用的代理，包括：
  - 代理名称
  - 显示名称（角色名）
  - 标题
  - 图标
  - 角色描述
  - 身份和专长
  - 沟通风格
  - 核心原则
  - 所属模块
  
  按模块组织代理：
  - Core 模块代理
  - BMM 模块代理
---

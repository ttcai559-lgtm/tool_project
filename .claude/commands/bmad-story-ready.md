---
command: "/bmad-story-ready"
name: "标记故事为准备开发"
description: "将草稿故事标记为准备开发，并在状态文件中从 TODO 移动到 IN PROGRESS。"
prompt: |-
  # 标记故事为准备开发
  
  将草稿故事标记为准备开发，并在状态文件中从 TODO 移动到 IN PROGRESS。
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/4-implementation/story-ready/workflow.yaml`
  2. 读取工作流指令：`{project-root}/.bmad/bmm/workflows/4-implementation/story-ready/instructions.md`
  3. 更新 sprint 状态文件
  
  请执行 story-ready 工作流，标记故事为准备开发状态。
---

---
command: "/bmad-story-done"
name: "标记故事为完成"
description: "将故事标记为完成 (DoD 完成)，并在状态文件中从当前状态移动到 DONE。"
prompt: |-
  # 标记故事为完成
  
  将故事标记为完成 (DoD 完成)，并在状态文件中从当前状态移动到 DONE。
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/4-implementation/story-done/workflow.yaml`
  2. 读取工作流指令：`{project-root}/.bmad/bmm/workflows/4-implementation/story-done/instructions.md`
  3. 更新 sprint 状态文件，推进故事队列
  
  请执行 story-done 工作流，标记故事为完成状态。
---

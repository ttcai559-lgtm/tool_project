---
command: "/bmad-status"
name: "BMad 工作流状态检查"
description: "检查当前项目的工作流状态，回答\"我现在应该做什么？\""
prompt: |-
  # BMad 工作流状态检查
  
  检查当前项目的工作流状态，回答"我现在应该做什么？"
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/workflow-status/workflow.yaml`
  2. 读取工作流指令：`{project-root}/.bmad/bmm/workflows/workflow-status/instructions.md`
  3. 读取状态文件：`{project-root}/docs/bmm-workflow-status.yaml`
  4. 根据当前状态提供下一步建议
  
  请执行 workflow-status 工作流，检查项目状态并提供下一步建议。
---

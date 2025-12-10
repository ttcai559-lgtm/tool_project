---
command: "/bmad-tech-spec"
name: "快速流程技术规范"
description: "为快速流程项目创建技术规范并生成史诗和故事。"
prompt: |-
  # 快速流程技术规范
  
  为快速流程项目创建技术规范并生成史诗和故事。
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/2-plan-workflows/tech-spec/workflow.yaml`
  2. 读取工作流指令：`{project-root}/.bmad/bmm/workflows/2-plan-workflows/tech-spec/instructions.md`
  3. 读取技术规范模板：`{project-root}/.bmad/bmm/workflows/2-plan-workflows/tech-spec/tech-spec-template.md`
  4. 读取检查清单：`{project-root}/.bmad/bmm/workflows/2-plan-workflows/tech-spec/checklist.md`
  5. 创建技术规范（无需 PRD）
  
  请执行 tech-spec 工作流，为简单更改创建聚焦的技术规范和 1-5 个用户故事。
---

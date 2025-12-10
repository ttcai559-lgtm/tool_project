---
command: "/bmad-arch"
name: "架构设计"
description: "协作式架构决策促进，为 AI 代理一致性创建架构文档。"
prompt: |-
  # 架构设计
  
  协作式架构决策促进，为 AI 代理一致性创建架构文档。
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/3-solutioning/architecture/workflow.yaml`
  2. 读取工作流指令：`{project-root}/.bmad/bmm/workflows/3-solutioning/architecture/instructions.md`
  3. 读取架构模板：`{project-root}/.bmad/bmm/workflows/3-solutioning/architecture/architecture-template.md`
  4. 读取检查清单：`{project-root}/.bmad/bmm/workflows/3-solutioning/architecture/checklist.md`
  5. 执行架构设计工作流
  
  请执行 architecture 工作流，通过智能、自适应的对话创建以决策为中心的架构文档。
---

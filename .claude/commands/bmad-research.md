---
command: "/bmad-research"
name: "研究工作流"
description: "自适应研究工作流，支持多种研究类型：市场研究、技术评估、竞品分析等。"
prompt: |-
  # 研究工作流
  
  自适应研究工作流，支持多种研究类型：市场研究、技术评估、竞品分析等。
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/1-analysis/research/workflow.yaml`
  2. 读取工作流指令（根据研究类型）：
     - 路由指令：`instructions-router.md`
     - 市场研究：`instructions-market.md`
     - 技术研究：`instructions-technical.md`
     - 深度研究：`instructions-deep-prompt.md`
  3. 执行相应的研究工作流
  
  请执行 research 工作流，根据需求选择适当的研究类型。
---

---
command: "/bmad-create-epics"
name: "创建史诗和故事"
description: "将 PRD 需求转化为可交付功能史诗组织的一口大小的故事。"
prompt: |-
  # 创建史诗和故事
  
  将 PRD 需求转化为可交付功能史诗组织的一口大小的故事。
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/3-solutioning/create-epics-and-stories/workflow.yaml`
  2. 读取工作流指令：`{project-root}/.bmad/bmm/workflows/3-solutioning/create-epics-and-stories/instructions.md`
  3. 读取史诗模板：`{project-root}/.bmad/bmm/workflows/3-solutioning/create-epics-and-stories/epics-template.md`
  4. 将 PRD 分解为史诗和用户故事
  
  请执行 create-epics-and-stories 工作流，将 PRD 转化为结构化的史诗和故事。
---

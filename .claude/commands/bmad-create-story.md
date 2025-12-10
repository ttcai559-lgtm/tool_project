---
command: "/bmad-create-story"
name: "创建用户故事"
description: "从史诗/PRD 和架构创建下一个用户故事 markdown，使用标准模板并保存到故事文件夹。"
prompt: |-
  # 创建用户故事
  
  从史诗/PRD 和架构创建下一个用户故事 markdown，使用标准模板并保存到故事文件夹。
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/4-implementation/create-story/workflow.yaml`
  2. 读取工作流指令：`{project-root}/.bmad/bmm/workflows/4-implementation/create-story/instructions.md`
  3. 读取故事模板：`{project-root}/.bmad/bmm/workflows/4-implementation/create-story/template.md`
  4. 读取检查清单：`{project-root}/.bmad/bmm/workflows/4-implementation/create-story/checklist.md`
  5. 创建格式良好的用户故事文档
  
  请执行 create-story 工作流，创建新的用户故事。
---

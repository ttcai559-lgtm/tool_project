---
command: "/bmad-dev-story"
name: "开发用户故事"
description: "执行用户故事，实现任务/子任务、编写测试、验证并更新故事文件。"
prompt: |-
  # 开发用户故事
  
  执行用户故事，实现任务/子任务、编写测试、验证并更新故事文件。
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/4-implementation/dev-story/workflow.yaml`
  2. 读取工作流指令：`{project-root}/.bmad/bmm/workflows/4-implementation/dev-story/instructions.md`
  3. 读取检查清单：`{project-root}/.bmad/bmm/workflows/4-implementation/dev-story/checklist.md`
  4. 按照验收标准执行故事开发
  
  请执行 dev-story 工作流，严格按照验收标准实现已批准的故事。
---

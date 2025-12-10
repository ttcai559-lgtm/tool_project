---
command: "/bmad-correct-course"
name: "课程修正"
description: "在 sprint 执行期间导航重大变更，分析影响、提出解决方案并路由实施。"
prompt: |-
  # 课程修正
  
  在 sprint 执行期间导航重大变更，分析影响、提出解决方案并路由实施。
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/4-implementation/correct-course/workflow.yaml`
  2. 读取工作流指令：`{project-root}/.bmad/bmm/workflows/4-implementation/correct-course/instructions.md`
  3. 读取检查清单：`{project-root}/.bmad/bmm/workflows/4-implementation/correct-course/checklist.md`
  4. 分析变更影响并提出解决方案
  
  请执行 correct-course 工作流，处理 sprint 期间的重大变更。
---

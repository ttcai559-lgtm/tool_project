# 组装故事上下文

通过提取最新文档和与草稿故事相关的现有代码/库文档来组装动态故事上下文 XML。

## 工作流说明

1. 读取工作流配置：`{project-root}/.bmad/bmm/workflows/4-implementation/story-context/workflow.yaml`
2. 读取工作流指令：`{project-root}/.bmad/bmm/workflows/4-implementation/story-context/instructions.md`
3. 读取上下文模板：`{project-root}/.bmad/bmm/workflows/4-implementation/story-context/context-template.xml`
4. 读取检查清单：`{project-root}/.bmad/bmm/workflows/4-implementation/story-context/checklist.md`
5. 组装故事上下文 XML

请执行 story-context 工作流，为故事开发创建全面的上下文文档。

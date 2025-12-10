---
command: "/bmad-help"
name: "BMad 帮助"
description: "显示所有可用的 BMad 命令和工作流。"
prompt: |-
  # BMad 帮助
  
  显示所有可用的 BMad 命令和工作流。
  
  ## 可用的主要命令
  
  ### 核心命令
  - `/bmad-init` - 初始化新的 BMad Method 项目
  - `/bmad-status` - 检查工作流状态，获取下一步建议
  - `/bmad-party` - 启动多代理协作讨论模式
  - `/bmad-help` - 显示此帮助信息
  
  ### 分析阶段 (Phase 1)
  - `/bmad-brainstorm` - 项目头脑风暴会话
  - `/bmad-research` - 自适应研究工作流
  - `/bmad-product-brief` - 创建产品简介
  - `/bmad-domain-research` - 领域特定需求探索
  
  ### 规划阶段 (Phase 2)
  - `/bmad-prd` - 创建产品需求文档
  - `/bmad-tech-spec` - 快速流程技术规范
  - `/bmad-ux-design` - UX 设计工作流
  
  ### 解决方案阶段 (Phase 3)
  - `/bmad-arch` - 架构设计
  - `/bmad-create-epics` - 从 PRD 创建史诗和故事
  - `/bmad-impl-ready` - 实施准备验证
  
  ### 实施阶段 (Phase 4)
  - `/bmad-dev-story` - 开发用户故事
  - `/bmad-code-review` - 代码审查
  - `/bmad-sprint-plan` - Sprint 规划
  - `/bmad-story-context` - 组装故事上下文
  
  ### 图表工具
  - `/bmad-diagram` - 创建系统架构图
  - `/bmad-flowchart` - 创建流程图
  - `/bmad-wireframe` - 创建线框图
  - `/bmad-dataflow` - 创建数据流图
  
  ## 工作流说明
  
  所有工作流位于 `{project-root}/.bmad/` 目录：
  - **bmm/** - BMad Method 模块工作流
  - **core/** - 核心平台工作流
  - **_cfg/** - 配置和清单文件
  
  查看 `{project-root}/.bmad/_cfg/workflow-manifest.csv` 获取完整的工作流列表。
---

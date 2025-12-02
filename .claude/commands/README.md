# BMad Claude Code 斜杠命令

此目录包含所有 BMad Method 的 Claude Code 斜杠命令。

## 使用方法

在 Claude Code 中输入斜杠命令即可执行相应的工作流或激活代理。例如：
```
/bmad-init
/bmad-status
/bmad-party
```

## 可用命令

### 核心命令

- `/bmad-init` - 初始化新的 BMad Method 项目
- `/bmad-status` - 检查工作流状态，获取下一步建议
- `/bmad-party` - 启动多代理协作讨论模式
- `/bmad-help` - 显示帮助信息和命令列表
- `/bmad-quick-start` - 快速入门指南
- `/bmad-docs` - 访问完整文档
- `/bmad-list-workflows` - 列出所有可用工作流
- `/bmad-list-agents` - 列出所有可用代理

### 分析阶段 (Phase 1)

- `/bmad-brainstorm` - 项目头脑风暴会话
- `/bmad-research` - 自适应研究工作流（市场/技术/竞品分析）
- `/bmad-product-brief` - 创建产品简介
- `/bmad-domain-research` - 领域特定需求探索

### 规划阶段 (Phase 2)

- `/bmad-prd` - 创建产品需求文档（适用于大型项目）
- `/bmad-tech-spec` - 快速流程技术规范（适用于小型项目）
- `/bmad-ux-design` - UX 设计工作流

### 解决方案阶段 (Phase 3)

- `/bmad-arch` - 架构设计
- `/bmad-create-epics` - 从 PRD 创建史诗和故事
- `/bmad-impl-ready` - 实施准备验证

### 实施阶段 (Phase 4)

#### Sprint 管理
- `/bmad-sprint-plan` - Sprint 规划和状态跟踪
- `/bmad-retrospective` - Sprint 回顾
- `/bmad-correct-course` - 课程修正（处理重大变更）

#### 故事开发
- `/bmad-create-story` - 创建新用户故事
- `/bmad-story-context` - 组装故事上下文
- `/bmad-story-ready` - 标记故事为准备开发
- `/bmad-dev-story` - 开发用户故事
- `/bmad-code-review` - 代码审查
- `/bmad-story-done` - 标记故事为完成

### 文档工具

- `/bmad-document` - 记录现有项目（棕地项目文档化）

### 图表工具

- `/bmad-diagram` - 创建系统架构图/ERD/UML 图
- `/bmad-flowchart` - 创建流程图
- `/bmad-wireframe` - 创建线框图
- `/bmad-dataflow` - 创建数据流图

### 代理命令 (bmad/ 子目录)

在 `bmad/` 子目录中，每个代理都有专门的命令文件：

- `/bmad/agent-master` - BMad Master (主执行器)
- `/bmad/agent-pm` - John (产品经理)
- `/bmad/agent-architect` - Winston (架构师)
- `/bmad/agent-dev` - Amelia (开发者)
- `/bmad/agent-analyst` - Mary (业务分析师)
- `/bmad/agent-sm` - Bob (Scrum Master)
- `/bmad/agent-tea` - Murat (测试架构师)
- `/bmad/agent-ux` - Sally (UX 设计师)
- `/bmad/agent-tech-writer` - Paige (技术作家)

## 推荐工作流程

### 新项目（绿地）

1. `/bmad-init` - 初始化项目
2. `/bmad-brainstorm` - 头脑风暴
3. `/bmad-prd` 或 `/bmad-tech-spec` - 创建规范
4. `/bmad-ux-design` - 设计 UX（如需要）
5. `/bmad-arch` - 架构设计
6. `/bmad-create-epics` - 创建史诗和故事
7. `/bmad-impl-ready` - 验证准备就绪
8. `/bmad-sprint-plan` - 开始 Sprint
9. `/bmad-dev-story` - 开发故事
10. `/bmad-code-review` - 审查代码
11. `/bmad-retrospective` - 回顾和改进

### 现有项目（棕地）

1. `/bmad-document` - 记录现有项目
2. `/bmad-init` - 初始化 BMad 跟踪
3. `/bmad-status` - 检查当前状态
4. 根据需要使用其他工作流

### 快速更改

1. `/bmad-tech-spec` - 创建快速技术规范
2. `/bmad-dev-story` - 直接开发
3. `/bmad-code-review` - 审查

## 获取帮助

- 运行 `/bmad-help` 查看命令摘要
- 运行 `/bmad-docs` 访问完整文档
- 运行 `/bmad-party` 与所有代理讨论

## 文件结构

```
.claude/commands/
├── README.md                    # 本文件
├── bmad-*.md                    # 工作流命令
└── bmad/
    └── agent-*.md               # 代理命令
```

## 版本信息

- BMad 版本: 6.0.0-alpha.12
- 安装日期: 2025-11-25
- 模块: core, bmm

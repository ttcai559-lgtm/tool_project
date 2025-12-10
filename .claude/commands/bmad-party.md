---
command: "/bmad-party"
name: "BMad Party Mode - 多代理讨论"
description: "启动 Party Mode，所有 BMad 代理参与群组讨论。"
prompt: |-
  # BMad Party Mode - 多代理讨论
  
  启动 Party Mode，所有 BMad 代理参与群组讨论。
  
  ## 工作流说明
  
  1. 读取工作流配置：`{project-root}/.bmad/core/workflows/party-mode/workflow.yaml`
  2. 读取工作流指令：`{project-root}/.bmad/core/workflows/party-mode/instructions.md`
  3. 读取代理清单：`{project-root}/.bmad/_cfg/agent-manifest.csv`
  4. 启动多代理协作讨论模式
  
  请执行 party-mode 工作流，协调所有已安装的 BMad 代理进行群组讨论。
---

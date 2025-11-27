# TestForge 项目结构

## 📁 目录结构

```
tool_project/
├── 📄 README.md                    # 项目说明文档
├── 📄 QUICK_START.md               # 快速开始指南
├── 📄 USER_GUIDE.md                # 用户使用手册
├── 📄 PROJECT_STRUCTURE.md         # 项目结构说明（本文件）
├── 📄 BACKEND_MANAGEMENT.md        # 后端管理指南
│
├── 🚀 start_all_services.vbs       # 一键启动所有服务（推荐）
├── 🚀 start_platform.bat           # 启动平台（显示窗口）
│
├── 🔧 start_backend_hidden.vbs     # 启动后端（静默模式）
├── 🔧 start_frontend_hidden.vbs    # 启动前端（静默模式）
├── 🔧 start_frontend.bat           # 启动前端（显示窗口）
│
├── 🔍 check_backend_status.vbs     # 检查后端状态
├── 🛑 stop_backend.vbs             # 停止后端
├── 🛑 stop_platform.bat            # 停止平台
│
├── 📂 testforge/                   # 主项目目录
│   ├── src/                        # 源代码
│   │   ├── api/                    # FastAPI后端
│   │   ├── core/                   # 核心功能
│   │   ├── protocols/              # 协议处理（HTTP, Protobuf）
│   │   ├── storage/                # 数据存储
│   │   └── ui/                     # Streamlit UI
│   ├── proto_files/                # Proto文件存储
│   ├── compiled_protos/            # 编译后的Proto
│   ├── environments/               # 环境配置
│   ├── testcases/                  # 测试用例
│   └── logs/                       # 日志文件
│
├── 📂 forge-apis/                  # React前端（如果使用）
│
├── 📂 docs/                        # 文档目录
│   ├── DEPLOYMENT_GUIDE.md         # 部署指南
│   ├── SETUP_GUIDE.md              # 安装配置指南
│   ├── ENVIRONMENT_FEATURE.md      # 环境功能说明
│   ├── PROTO_UPLOAD_FIX.md         # Proto上传修复说明
│   └── cpolar使用说明.md           # Cpolar内网穿透说明
│
├── 📂 scripts/                     # 管理脚本
│   ├── force_restart.bat           # 强制重启后端
│   ├── force_restart.py            # 强制重启（Python版）
│   ├── restart_backend.bat         # 重启后端
│   └── kill_backend.py             # 结束后端进程
│
└── 📂 tests/                       # 测试文件
    ├── test_nubia_proto.py         # 努比亚Proto测试
    ├── test_api_messages.py        # API消息类型测试
    ├── test_api_upload.py          # API上传测试
    ├── test_correct_message_type.py # 正确消息类型测试
    ├── test_full_request.py        # 完整请求测试
    └── test_upload_proto.py        # Proto上传流程测试
```

## 🚀 快速启动

### 方式1：一键启动（最简单）⭐
双击 `start_all_services.vbs`
- 自动启动后端和前端
- 静默模式，后台运行
- 弹窗提示服务地址
- **推荐日常使用**

### 方式2：分别启动（灵活控制）
**后端：**
- 双击 `start_backend_hidden.vbs` - 静默模式
- 或运行 `start_platform.bat` - 显示窗口

**前端：**
- 双击 `start_frontend_hidden.vbs` - 静默模式
- 或运行 `start_frontend.bat` - 显示窗口

### 方式3：显示窗口（调试时使用）
```bash
start_platform.bat
```
- 打开后端和前端窗口
- 可以看到实时日志
- 方便调试

## 🛑 停止服务

```bash
stop_platform.bat
```

或者使用任务管理器结束进程。

## 📝 核心文件说明

| 文件 | 用途 |
|------|------|
| `start_platform.bat` | 完整启动脚本，启动后端和前端 |
| `start_backend_hidden.vbs` | 静默启动后端服务 |
| `stop_platform.bat` | 停止所有服务 |
| `README.md` | 项目介绍和功能说明 |
| `QUICK_START.md` | 快速开始指南 |
| `USER_GUIDE.md` | 详细使用手册 |

## 🔧 开发工具

测试脚本位于 `tests/` 目录，用于：
- 测试Proto文件解析
- 测试API接口
- 验证Protobuf转换功能

管理脚本位于 `scripts/` 目录，用于：
- 重启后端服务
- 强制停止进程
- 服务管理

## 📚 文档

所有项目文档位于 `docs/` 目录，包括：
- 部署指南
- 安装配置
- 功能说明
- 技术文档

---

**最后更新**: 2025-11-27

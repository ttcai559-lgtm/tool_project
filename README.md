# TestForge - API测试平台

专业的API测试工具，支持HTTP/HTTPS和Protobuf协议。

## 🚀 快速开始

### 启动平台（最简单）
双击 `start_all_services.vbs` 即可！

脚本会自动：
- ✅ 检测服务状态
- ✅ 启动后端API（http://localhost:8000）
- ✅ 启动前端UI（http://localhost:8080）
- ✅ 自动打开浏览器

### 停止平台
双击 `stop_platform.bat`

---

## ✨ 主要功能

- 🌐 **HTTP/HTTPS测试** - 支持GET/POST/PUT/DELETE等方法
- 📦 **Protobuf支持** - 上传.proto文件，自动编译和转换
- 🎯 **媒体管理** - 配置多个广告媒体及其接口信息
- 💾 **用例保存** - 保存和重用测试用例
- ✅ **断言验证** - 自动验证响应结果
- 📊 **实时日志** - 查看详细的请求和响应信息

---

## 📖 文档

详细文档位于 `docs/` 目录：

- **QUICK_START.md** - 快速入门指南
- **USER_GUIDE.md** - 完整使用手册
- **TERMINOLOGY.md** - 术语说明（媒体、用例等概念）
- **SETUP_GUIDE.md** - 安装配置指南
- **PROJECT_STRUCTURE.md** - 项目结构说明
- **BACKEND_MANAGEMENT.md** - 后端服务管理

---

## 🛠️ 技术栈

**后端：**
- FastAPI - 高性能Web框架
- Protobuf - 协议缓冲区支持
- Uvicorn - ASGI服务器

**前端：**
- React + TypeScript
- Vite - 快速构建工具
- Shadcn/ui - UI组件库

---

## 📂 项目结构

```
tool_project/
├── README.md                    # 本文件
├── start_all_services.vbs       # 一键启动（推荐）
├── stop_platform.bat            # 停止所有服务
│
├── testforge/                   # 后端项目
│   ├── src/api/                 # FastAPI服务
│   ├── proto_files/             # 媒体Proto文件
│   ├── compiled_protos/         # 编译后的Proto
│   ├── environments/            # 媒体配置文件
│   └── testcases/               # 测试用例
│
├── forge-apis/                  # 前端项目（React）
│
├── docs/                        # 文档
├── scripts/                     # 管理脚本
└── tests/                       # 测试文件
```

---

## 🎯 使用示例

### 1. 创建媒体
在前端UI中点击"Media Management"（媒体管理），创建新媒体：
- 媒体名称：努比亚
- Base URL：http://nubia-test.taopb.com/adx/ssp/nubia
- 协议类型：Protobuf
- 默认参数：配置该媒体的默认请求参数

### 2. 上传Proto文件
选择媒体后，上传对应的`.proto`文件，系统会自动：
- 编译Proto文件
- 提取Message类型列表
- 生成Python绑定

### 3. 发送请求
选择媒体和Message类型，填写或使用默认参数，点击发送：
- 选择媒体：努比亚
- Request Message Type: BidRequest
- Response Message Type: BidResponse

系统会自动处理JSON ↔ Protobuf转换。

---

## 🔧 故障排查

### 问题：服务无法启动
**解决方案：**
1. 检查端口占用：`netstat -ano | findstr "8000 8080"`
2. 运行 `stop_platform.bat` 停止所有服务
3. 重新运行 `start_all_services.vbs`

### 问题：前端无法连接后端
**解决方案：**
1. 访问 http://localhost:8000/ 检查后端状态
2. 检查防火墙设置
3. 确认后端服务正在运行

### 问题：Proto文件解析失败
**解决方案：**
1. 确认媒体协议类型设置为"Protobuf"
2. 检查Proto文件语法是否正确
3. 确认选择的Message Type正确（如BidRequest/BidResponse）
4. 查看后端日志了解详细错误

---

## 📝 更新日志

### 2025-11-27
- ✅ 修复Proto文件上传后Message类型显示问题
- ✅ 改进启动脚本，支持智能检测和自动重启
- ✅ 优化项目结构，整理根目录文件
- ✅ 增强Protobuf转换错误处理

---

## 📄 许可证

本项目仅供内部使用。

---

## 🤝 贡献

如有问题或建议，请联系开发团队。

---

**提示**: 首次使用请先阅读 `docs/QUICK_START.md`

# TestForge API 测试平台 - 用户使用指南

## 📖 目录

- [快速开始](#快速开始)
- [平台介绍](#平台介绍)
- [功能特性](#功能特性)
- [详细使用说明](#详细使用说明)
- [常见问题](#常见问题)

---

## 🚀 快速开始

### 1. 启动服务

**方法一：使用启动脚本（推荐）**

双击项目根目录下的 `start_platform.bat` 文件，会自动启动前后端服务。

启动脚本会：
- 检查虚拟环境是否存在
- 启动后端服务（FastAPI，端口 8000）
- 启动前端服务（React，端口 8080）

**启动成功标志**：
- 弹出两个终端窗口：
  - `TestForge Backend` - 后端服务窗口
  - `TestForge Frontend` - 前端服务窗口
- 显示启动完成信息

**方法二：手动启动**

```bash
# 1. 启动后端服务
cd testforge
call ..\venv\Scripts\activate.bat
python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000

# 2. 新开一个终端，启动前端服务
cd forge-apis
npm run dev
```

### 2. 访问平台

启动成功后，在浏览器中访问以下地址：

| 服务 | 本机访问地址 | 局域网访问地址 | 说明 |
|------|-------------|---------------|------|
| **前端界面** | http://localhost:8080 | http://你的IP:8080 | 主操作界面 |
| **API 文档** | http://localhost:8000/docs | http://你的IP:8000/docs | Swagger 文档 |

**示例：** 如果你的电脑 IP 是 192.168.40.59，局域网内其他设备可以访问：
- 前端：http://192.168.40.59:8080
- API：http://192.168.40.59:8000/docs

### 3. 停止服务

**方法一：使用停止脚本（推荐）**

双击项目根目录下的 `stop_platform.bat` 文件，会自动停止所有服务。

停止脚本会：
- 关闭前后端服务窗口
- 强制结束占用 8000 和 8080 端口的进程
- 清理所有相关进程

**方法二：手动停止**

在两个终端窗口中分别按 `Ctrl + C` 停止服务。

---

## 💡 平台介绍

**TestForge** 是一个专为 API 测试设计的可视化测试平台，支持 HTTP/HTTPS、JSON 和 Protobuf 协议的接口测试。

### 核心优势

✅ **可视化操作** - 无需编写代码，通过界面即可完成接口测试
✅ **Protobuf 支持** - 完整支持 Protobuf 请求和响应解析
✅ **环境管理** - 灵活的多环境配置和切换
✅ **用例管理** - 测试用例保存、加载和复用
✅ **实时测试** - 即时发送请求，实时查看响应
✅ **数据持久化** - 所有配置和用例自动保存为 YAML 文件

### 技术架构

```
┌─────────────────────────────────────────┐
│         前端 (React + Vite)              │
│      端口: 8080                          │
│   - 可视化界面                           │
│   - 请求构建器                           │
│   - 响应查看器                           │
└──────────────┬──────────────────────────┘
               │ REST API
               ↓
┌─────────────────────────────────────────┐
│        后端 (FastAPI + Python)           │
│      端口: 8000                          │
│   - API 路由                             │
│   - Protobuf 编解码                      │
│   - 环境配置管理                         │
│   - 用例存储                             │
└──────────────┬──────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────┐
│          数据存储 (YAML)                 │
│   - testforge/environments/             │
│   - testforge/testcases/                │
│   - testforge/proto/                    │
└─────────────────────────────────────────┘
```

---

## 🎯 功能特性

### 1. 环境配置管理

**功能描述**：管理不同的测试环境（开发、测试、生产等）

**主要功能**：
- ✅ 创建环境配置
- ✅ 设置环境基础 URL
- ✅ 配置默认请求头（Headers）
- ✅ 配置默认请求参数
- ✅ 选择协议类型（JSON/Protobuf）
- ✅ 上传 Protobuf 定义文件（.proto）

**使用场景**：
- 区分开发、测试、生产环境
- 为不同渠道配置不同的接口地址
- 保存常用的请求参数模板

### 2. API 请求测试

**功能描述**：构建和发送 HTTP/HTTPS 请求

**支持的请求类型**：
- GET - 获取资源
- POST - 创建资源
- PUT - 更新资源
- DELETE - 删除资源
- PATCH - 部分更新

**支持的数据格式**：
- JSON - 标准 JSON 格式
- Protobuf - Protocol Buffers 二进制格式
- Form Data - 表单数据
- URL Encoded - URL 编码数据

**请求配置项**：
- URL 路径
- 请求方法
- 请求头（Headers）
- 请求体（Body）
- 查询参数（Query Parameters）

### 3. Protobuf 支持

**功能描述**：完整支持 Protobuf 协议的接口测试

**主要功能**：
- ✅ 上传 .proto 定义文件
- ✅ 自动解析 Protobuf 消息结构
- ✅ 从 JSON 转换为 Protobuf 二进制
- ✅ 从 Protobuf 二进制解码为 JSON
- ✅ 消息类型自动识别

**使用流程**：
1. 在环境配置中上传 .proto 文件
2. 选择协议类型为 "Protobuf"
3. 输入 JSON 格式的请求数据
4. 系统自动转换为 Protobuf 格式发送
5. 响应自动解码为 JSON 显示

### 4. 测试用例管理

**功能描述**：保存和管理常用的测试用例

**主要功能**：
- ✅ 保存当前请求为测试用例
- ✅ 加载已保存的测试用例
- ✅ 查看测试用例列表
- ✅ 删除测试用例
- ✅ 用例自动命名（带时间戳）

**存储格式**：YAML 格式，易于阅读和版本控制

**存储路径**：`testforge/testcases/`

### 5. 响应查看

**功能描述**：清晰展示接口响应信息

**显示内容**：
- HTTP 状态码
- 响应时间
- 响应头（Headers）
- 响应体（Body）- JSON 格式化显示
- 错误信息（如有）

---

## 📚 详细使用说明

### 第一步：创建环境配置

1. 打开平台首页 http://localhost:8080
2. 点击 **"Environment Management"** 标签
3. 点击 **"Create New Environment"** 按钮
4. 填写环境信息：
   ```
   名称: 测试环境
   基础URL: http://test.example.com
   协议类型: 选择 JSON 或 Protobuf
   ```
5. 点击 **"Add Header"** 添加默认请求头：
   ```
   Content-Type: application/json
   Authorization: Bearer your-token
   ```
6. （可选）如果使用 Protobuf，上传 .proto 文件
7. 点击 **"Save Environment"** 保存

### 第二步：发送测试请求

1. 切换到 **"API Testing"** 标签
2. 选择环境：从下拉框中选择刚创建的环境
3. 配置请求：
   ```
   请求方法: POST
   URL路径: /api/users
   ```
4. 添加请求头（Headers）：
   ```
   Content-Type: application/json
   ```
5. 编写请求体（Body）：
   ```json
   {
     "name": "张三",
     "age": 25,
     "email": "zhangsan@example.com"
   }
   ```
6. 点击 **"Send Request"** 发送请求
7. 查看响应结果

### 第三步：保存测试用例

1. 发送请求成功后
2. 点击 **"Save Test Case"** 按钮
3. 输入用例名称（可选，默认自动生成）
4. 点击保存
5. 用例自动保存到 `testforge/testcases/` 目录

### 第四步：使用已保存的用例

1. 切换到 **"Test Cases"** 标签
2. 从列表中选择要使用的测试用例
3. 点击 **"Load"** 加载用例
4. 请求配置会自动填充
5. 可以直接发送或修改后发送

### 使用 Protobuf 协议

**场景**：测试使用 Protobuf 的广告接口

**步骤**：

1. **准备 .proto 文件**
   ```protobuf
   syntax = "proto3";

   message AdRequest {
     string device_id = 1;
     string app_id = 2;
     int32 ad_count = 3;
   }
   ```

2. **创建环境配置**
   - 环境名称：广告测试环境
   - 基础URL：http://ad-api.example.com
   - 协议类型：选择 **Protobuf**
   - 上传 .proto 文件

3. **配置请求**
   - URL: /adx/router/V100/request
   - Method: POST
   - Headers:
     ```
     Content-Type: application/x-protobuf
     ```
   - Body (JSON格式输入):
     ```json
     {
       "device_id": "123456",
       "app_id": "com.example.app",
       "ad_count": 3
     }
     ```

4. **发送请求**
   - 系统自动将 JSON 转换为 Protobuf 二进制
   - 发送请求到服务器
   - 响应自动解码为 JSON 显示

---

## ❓ 常见问题

### Q1: 启动脚本双击后闪退怎么办？

**A:** 可能是虚拟环境未创建，手动检查：
```bash
# 检查虚拟环境是否存在
dir venv\Scripts\activate.bat

# 如果不存在，创建虚拟环境
python -m venv venv

# 激活并安装依赖
venv\Scripts\activate.bat
cd testforge
pip install -r requirements.txt
```

### Q2: 访问前端显示无法连接后端？

**A:** 检查后端是否启动成功：
1. 查看 `TestForge Backend` 窗口是否有错误
2. 访问 http://localhost:8000/docs 验证后端
3. 检查防火墙是否阻止了 8000 端口

### Q3: Protobuf 请求失败？

**A:** 检查以下几点：
1. 确认已上传正确的 .proto 文件
2. 检查 JSON 数据结构是否与 .proto 定义匹配
3. 确认服务器端是否支持 Protobuf
4. 检查 Content-Type 是否设置为 `application/x-protobuf`

### Q4: 测试用例保存在哪里？

**A:**
- 测试用例：`testforge/testcases/` 目录
- 环境配置：`testforge/environments/` 目录
- 文件格式：YAML，可以用文本编辑器直接查看和编辑

### Q5: 如何在局域网内让其他人访问？

**A:**
1. 确认你的电脑 IP 地址（运行 `ipconfig` 查看）
2. 确保防火墙允许 8080 和 8000 端口
3. 其他人使用 `http://你的IP:8080` 访问

### Q6: 停止服务后端口仍被占用？

**A:**
1. 运行 `stop_platform.bat` 脚本
2. 如果仍然占用，手动查找并结束进程：
   ```bash
   # 查找占用端口的进程
   netstat -ano | findstr :8000
   netstat -ano | findstr :8080

   # 结束进程（PID 替换为实际进程号）
   taskkill /PID <进程号> /F
   ```

### Q7: 如何备份我的测试数据？

**A:** 直接复制这两个目录：
- `testforge/testcases/` - 所有测试用例
- `testforge/environments/` - 所有环境配置

### Q8: 如何更新 Protobuf 定义文件？

**A:**
1. 进入环境管理页面
2. 选择要更新的环境
3. 重新上传新的 .proto 文件
4. 保存环境配置

---

## 📞 获取帮助

如果遇到问题或需要帮助：

1. **查看日志**：
   - 后端日志：查看 `TestForge Backend` 终端窗口
   - 前端日志：按 F12 打开浏览器开发者工具

2. **API 文档**：
   - 访问 http://localhost:8000/docs
   - 查看完整的 API 接口文档

3. **项目文档**：
   - README.md - 项目概述
   - QUICKSTART.md - 快速开始指南
   - 本文档 - 详细使用说明

---

## 🎉 开始使用

现在你已经了解了 TestForge 平台的所有功能，开始你的 API 测试之旅吧！

1. ✅ 双击 `start_platform.bat` 启动服务
2. ✅ 访问 http://localhost:8080
3. ✅ 创建你的第一个环境配置
4. ✅ 发送第一个测试请求
5. ✅ 保存你的测试用例

祝测试愉快！🚀

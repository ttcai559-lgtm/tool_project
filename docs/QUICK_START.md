# TestForge 快速开始 ⚡

## 一分钟快速启动

### 1️⃣ 启动服务

双击 `start_platform.bat`

✅ 会自动弹出两个窗口（后端 + 前端）

### 2️⃣ 访问平台

浏览器打开：**http://localhost:8080**

### 3️⃣ 停止服务

双击 `stop_platform.bat`

---

## 访问地址速查

| 服务 | 地址 | 说明 |
|------|------|------|
| 🖥️ **前端界面** | http://localhost:8080 | 主操作界面 |
| 📡 **API文档** | http://localhost:8000/docs | Swagger文档 |
| 🌐 **局域网访问** | http://你的IP:8080 | 其他设备访问 |

---

## 5分钟上手教程

### 步骤 1：创建环境

1. 打开 http://localhost:8080
2. 点击 **"Environment Management"**
3. 点击 **"Create New Environment"**
4. 填写：
   - 名称：`测试环境`
   - URL：`http://test.example.com`
   - 协议：选择 `JSON` 或 `Protobuf`
5. 点击 **"Save"**

### 步骤 2：发送请求

1. 切换到 **"API Testing"** 标签
2. 选择刚创建的环境
3. 配置请求：
   ```
   方法: POST
   路径: /api/test
   ```
4. 输入请求体：
   ```json
   {
     "name": "测试",
     "value": 123
   }
   ```
5. 点击 **"Send Request"**
6. 查看响应结果 ✅

### 步骤 3：保存用例

1. 点击 **"Save Test Case"**
2. 输入名称（或使用自动生成的名称）
3. 点击保存
4. 用例已保存到 `testforge/testcases/` 📁

---

## 常见问题速查

❓ **启动失败？**
→ 检查虚拟环境是否存在：`venv\Scripts\activate.bat`

❓ **端口被占用？**
→ 运行 `stop_platform.bat` 强制清理

❓ **前端无法连接后端？**
→ 访问 http://localhost:8000/docs 检查后端是否启动

❓ **局域网访问不了？**
→ 检查防火墙是否允许 8080 和 8000 端口

---

## 📖 需要更多帮助？

查看完整文档：**USER_GUIDE.md**

包含：
- ✅ 详细功能介绍
- ✅ Protobuf 使用指南
- ✅ 完整的问题解决方案
- ✅ 最佳实践建议

---

**开始你的测试之旅！** 🚀

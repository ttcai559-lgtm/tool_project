# TestForge 快速启动

## ✅ 已完成的集成工作

我已经成功将您的React前端与Python后端集成！

### 📦 架构变更

**之前（Streamlit）：**
```
Streamlit UI (Python) → 单体应用
```

**现在（React + FastAPI）：**
```
React Frontend (Port 5173) ←→ FastAPI Backend (Port 8000)
```

## 🚀 当前状态

### ✅ 后端 API 服务器
- **状态**: 🟢 正在运行
- **地址**: http://localhost:8000
- **文档**: http://localhost:8000/docs
- **进程**: 后台运行中

### ⏳ 前端 React 服务器
- **状态**: 正在安装依赖...
- **预期地址**: http://localhost:5173
- **进程**: 后台运行中

## 📋 使用方法

### 1. 访问应用

待前端启动完成后，打开浏览器访问：
**http://localhost:5173**

### 2. 测试功能

界面将展示：
- **左侧**: 测试用例列表
- **中间**: 请求配置面板（Method, URL, Headers, Params, Body, Assertions）
- **右侧**: 响应展示面板（Body, Headers, Assertions结果）

### 3. 示例操作流程

1. 点击 "+ 新建" 创建测试用例
2. 选择HTTP方法（GET/POST/PUT/DELETE/PATCH）
3. 输入API地址
4. 配置Headers、Params或Body
5. 添加断言（可选）：
   ```python
   status == 200
   response['success'] == True
   elapsed_ms < 1000
   ```
6. 点击 "Send Request" 发送请求
7. 查看响应结果和断言验证

### 4. 保存用例

- 点击 "Save" 按钮保存当前配置
- 保存后可在左侧列表中看到
- 用例存储在 `testforge/testcases/` 目录（YAML格式）

## 🔧 重新启动服务

如果需要重启：

### 方式一：使用脚本（推荐）

**后端：**
```bash
cd testforge
run_api.bat
```

**前端：**
```bash
cd forge-apis
run_frontend.bat
```

### 方式二：手动命令

**后端：**
```bash
cd testforge
python -m uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

**前端：**
```bash
cd forge-apis
npm run dev
```

## 📊 API端点

后端提供了以下REST API：

| 方法 | 端点 | 说明 |
|------|------|------|
| POST | `/api/send-request` | 发送HTTP请求并执行断言 |
| GET | `/api/testcases` | 获取所有测试用例列表 |
| GET | `/api/testcases/{name}` | 加载指定测试用例 |
| POST | `/api/testcases` | 保存测试用例 |
| DELETE | `/api/testcases/{name}` | 删除测试用例 |

完整API文档：http://localhost:8000/docs

## 🎨 UI特性

新的React前端采用了现代化的设计：

- **shadcn-ui** 组件库
- **Tailwind CSS** 样式
- **渐变色主题**
- **响应式布局**
- **流畅的动画效果**
- **清晰的断言结果展示**
- **实时状态反馈**

## 🔥 核心优势

相比原来的Streamlit版本：

1. **更专业的UI** - 使用shadcn-ui组件库，美观现代
2. **更好的性能** - React的组件化设计，渲染更高效
3. **更强的扩展性** - 前后端分离，易于添加新功能
4. **更安全的断言** - 断言在Python后端安全执行
5. **更完善的API** - FastAPI自动生成文档，易于集成

## 📚 技术栈

### 前端
- React 18
- TypeScript
- Vite
- shadcn-ui
- Tailwind CSS
- React Query

### 后端
- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn
- requests
- PyYAML

## 🎯 下一步

- [ ] 等待前端启动完成
- [ ] 访问 http://localhost:5173
- [ ] 测试发送请求功能
- [ ] 保存第一个测试用例
- [ ] 体验新的UI界面

## 💡 提示

- 前端会自动检测代码更改并热重载
- 后端也支持自动重载（--reload参数）
- 所有测试用例都保存在YAML文件中，可以用Git管理
- 可以在浏览器开发者工具中查看API请求详情

---

🎉 **享受全新的TestForge体验！**

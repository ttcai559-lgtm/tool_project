# TestForge 平台访问地址指南

## 🚀 快速访问

### 主平台 (前端 + AI测试用例生成)

**前端访问地址**: http://localhost:8080

**后端API地址**: http://localhost:8000

---

## 📋 完整启动流程

### 1. 启动后端 FastAPI 服务

```bash
# 方式1: 直接运行
cd testforge/src/api
python main.py

# 方式2: 使用uvicorn (推荐)
cd testforge/src/api
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**后端服务地址**:
- API文档 (Swagger): http://localhost:8000/docs
- API备用文档 (ReDoc): http://localhost:8000/redoc
- 健康检查: http://localhost:8000/
- AI功能状态: http://localhost:8000/api/ai/status

### 2. 启动前端服务

```bash
cd forge-apis
npm run dev
```

**前端访问地址**: http://localhost:8080

---

## 🤖 AI测试用例生成功能专用地址

### API端点

**1. 生成测试用例**
```
POST http://localhost:8000/api/ai/generate-testcases
```

**2. 下载XMind文件**
```
GET http://localhost:8000/api/ai/download/{filename}
```

**3. 检查功能状态**
```
GET http://localhost:8000/api/ai/status
```

### Streamlit独立页面 (可选)

如果需要使用独立的Streamlit界面:

```bash
cd testforge/src/ai_testcase_gen
streamlit run streamlit_app.py
```

**Streamlit访问地址**: http://localhost:8501

---

## 🌐 端口分配总览

| 服务 | 端口 | 地址 | 用途 |
|------|------|------|------|
| **前端 (React)** | 8080 | http://localhost:8080 | 主平台UI |
| **后端 (FastAPI)** | 8000 | http://localhost:8000 | API服务 |
| **Streamlit (可选)** | 8501 | http://localhost:8501 | AI功能独立页面 |

---

## 📝 使用流程

### 方案A: 在主平台中使用 (推荐)

1. **启动服务**:
   ```bash
   # 终端1: 启动后端
   cd testforge/src/api
   python main.py

   # 终端2: 启动前端
   cd forge-apis
   npm run dev
   ```

2. **访问地址**: http://localhost:8080

3. **使用AI功能**:
   - 在前端界面中添加"AI测试用例生成"功能入口
   - 参考 `testforge/AI_TESTCASE_INTEGRATION_GUIDE.md` 集成代码

### 方案B: 使用独立Streamlit页面

1. **启动服务**:
   ```bash
   cd testforge/src/ai_testcase_gen
   streamlit run streamlit_app.py
   ```

2. **访问地址**: http://localhost:8501

3. **操作步骤**:
   - 上传需求文档 (.docx, .doc, .pdf)
   - 点击"生成测试用例"
   - 下载XMind文件

---

## 🔧 测试API接口

### 使用curl测试

```bash
# 1. 检查AI功能状态
curl http://localhost:8000/api/ai/status

# 2. 生成测试用例 (需要上传文件)
curl -X POST http://localhost:8000/api/ai/generate-testcases \
  -F "file=@需求文档.docx" \
  -F "ai_model=claude"

# 3. 下载XMind文件
curl -O http://localhost:8000/api/ai/download/测试用例_xxx.xmind
```

### 使用Postman测试

**1. 测试生成接口**:
- Method: `POST`
- URL: `http://localhost:8000/api/ai/generate-testcases`
- Body: `form-data`
  - Key: `file`, Type: File, Value: 选择需求文档
  - Key: `ai_model`, Type: Text, Value: `claude`

**2. 测试下载接口**:
- Method: `GET`
- URL: `http://localhost:8000/api/ai/download/{从上一步获取的filename}`

---

## 🛠️ 常见问题

### Q1: 前端无法访问后端API怎么办?

**检查CORS配置**:
后端已配置允许所有来源的跨域请求:
```python
# testforge/src/api/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Q2: 端口被占用怎么办?

**修改端口**:

前端端口修改 (`forge-apis/vite.config.js`):
```javascript
export default defineConfig({
  server: {
    host: "::",
    port: 8080,  // 改为其他端口,如8081
  },
  // ...
})
```

后端端口修改 (`testforge/src/api/main.py`):
```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)  # 改为其他端口
```

### Q3: 如何在生产环境部署?

**生产环境配置**:

1. 前端构建:
```bash
cd forge-apis
npm run build
# 构建产物在 dist/ 目录
```

2. 后端部署 (使用Gunicorn):
```bash
pip install gunicorn
cd testforge/src/api
gunicorn main:app --workers 4 --bind 0.0.0.0:8000
```

3. 使用Nginx反向代理:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    # 前端
    location / {
        root /path/to/forge-apis/dist;
        try_files $uri $uri/ /index.html;
    }

    # 后端API
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 📚 相关文档

- **API集成指南**: `testforge/AI_TESTCASE_INTEGRATION_GUIDE.md`
- **XMind修复说明**: `testforge/src/ai_testcase_gen/XMIND_FIX_SUMMARY.md`
- **Vue集成示例**: 见集成指南中的Vue部分
- **React集成示例**: 见集成指南中的React部分

---

## 🎯 快速开始命令

```bash
# 一键启动所有服务 (Windows)
# 创建 start_platform.bat
echo "Starting TestForge Platform..."
start cmd /k "cd testforge\src\api && python main.py"
timeout 2
start cmd /k "cd forge-apis && npm run dev"
echo "Services started!"
echo "Frontend: http://localhost:8080"
echo "Backend: http://localhost:8000"
```

```bash
# 一键启动所有服务 (Linux/Mac)
# 创建 start_platform.sh
#!/bin/bash
echo "Starting TestForge Platform..."
cd testforge/src/api && python main.py &
sleep 2
cd forge-apis && npm run dev
```

---

## ✅ 验证安装

访问以下地址确认服务正常:

- [ ] 前端: http://localhost:8080
- [ ] 后端: http://localhost:8000/docs
- [ ] AI状态: http://localhost:8000/api/ai/status

期望返回:
```json
{
  "available": true,
  "supported_formats": [".docx", ".doc", ".pdf"],
  "supported_models": ["claude", "openai"],
  "features": {
    "defect_detection": true,
    "question_generation": true,
    "confidence_scoring": true
  }
}
```

---

**最后更新**: 2025-11-28
**版本**: 1.0.0

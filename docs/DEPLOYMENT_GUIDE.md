# TestForge 完整部署指南

## 📋 项目概览

TestForge是一个完整的前后端分离API测试平台：

```
tool_project/
├── testforge/          # Python FastAPI 后端
│   └── GitHub: 待创建
└── forge-apis/         # React 前端
    └── GitHub: https://github.com/ttcai559-lgtm/forge-apis
```

## 🚀 部署选项

### 选项1: 本地开发环境（已完成）

**当前状态**: ✅ 运行中

**访问地址**:
- Frontend: http://localhost:8080
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

**启动服务**:
```bash
# 后端
cd testforge
run_api.bat

# 前端
cd forge-apis
run_frontend.bat
```

### 选项2: Docker部署

#### 2.1 后端Docker化

**testforge/Dockerfile** (已有):
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**构建并运行**:
```bash
cd testforge
docker build -t testforge-backend .
docker run -p 8000:8000 testforge-backend
```

#### 2.2 前端Docker化

创建 `forge-apis/Dockerfile`:
```dockerfile
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

创建 `forge-apis/nginx.conf`:
```nginx
server {
    listen 80;
    location / {
        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
    }
}
```

**构建并运行**:
```bash
cd forge-apis
docker build -t testforge-frontend .
docker run -p 80:80 testforge-frontend
```

#### 2.3 Docker Compose（推荐）

创建 `docker-compose.yml`:
```yaml
version: '3.8'

services:
  backend:
    build: ./testforge
    ports:
      - "8000:8000"
    volumes:
      - ./testforge/testcases:/app/testcases
    environment:
      - PYTHONUNBUFFERED=1
    restart: unless-stopped

  frontend:
    build: ./forge-apis
    ports:
      - "80:80"
    environment:
      - VITE_API_URL=http://backend:8000
    depends_on:
      - backend
    restart: unless-stopped
```

**启动所有服务**:
```bash
docker-compose up -d
```

### 选项3: 云端部署

#### 3.1 后端部署选项

**A. Railway.app** (推荐)
1. 登录 https://railway.app
2. 新建项目 → Deploy from GitHub
3. 选择 testforge 仓库
4. Railway自动检测Dockerfile
5. 设置环境变量（如需要）
6. 部署完成后获得URL

**B. Render.com**
1. 登录 https://render.com
2. New → Web Service
3. 连接GitHub仓库
4. 配置:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn src.api.main:app --host 0.0.0.0 --port $PORT`
5. 部署

**C. Heroku**
```bash
# 安装Heroku CLI
heroku login
cd testforge

# 创建应用
heroku create testforge-api

# 添加Procfile
echo "web: uvicorn src.api.main:app --host 0.0.0.0 --port \$PORT" > Procfile

# 部署
git push heroku master
```

**D. 阿里云/腾讯云ECS**
```bash
# SSH到服务器
ssh user@your-server

# 安装依赖
sudo apt update
sudo apt install python3-pip

# 克隆代码
git clone https://github.com/你的用户名/testforge.git
cd testforge

# 安装Python依赖
pip3 install -r requirements.txt

# 使用systemd管理服务
sudo nano /etc/systemd/system/testforge.service

[Unit]
Description=TestForge API Server
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/testforge
ExecStart=/usr/local/bin/uvicorn src.api.main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target

# 启动服务
sudo systemctl start testforge
sudo systemctl enable testforge
```

#### 3.2 前端部署选项

**A. Vercel** (推荐)
```bash
cd forge-apis
npm install -g vercel
vercel --prod
```

在Vercel设置环境变量:
- `VITE_API_URL`: 你的后端URL

**B. Netlify**
1. 登录 https://app.netlify.com
2. New site from Git
3. 选择 forge-apis 仓库
4. 配置:
   - Build command: `npm run build`
   - Publish directory: `dist`
   - Environment variables: `VITE_API_URL=https://your-backend.com`
5. 部署

**C. GitHub Pages** (仅静态资源)
```bash
cd forge-apis

# 添加部署脚本到 package.json
{
  "scripts": {
    "deploy": "vite build && gh-pages -d dist"
  }
}

# 安装gh-pages
npm install -D gh-pages

# 部署
npm run deploy
```

**D. Nginx服务器**
```bash
# 构建
npm run build

# 复制到服务器
scp -r dist/* user@server:/var/www/testforge

# Nginx配置
server {
    listen 80;
    server_name your-domain.com;
    root /var/www/testforge;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 选项4: Kubernetes部署

#### 后端部署 (testforge-backend.yaml)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: testforge-backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: testforge-backend
  template:
    metadata:
      labels:
        app: testforge-backend
    spec:
      containers:
      - name: backend
        image: your-registry/testforge-backend:latest
        ports:
        - containerPort: 8000
        env:
        - name: PYTHONUNBUFFERED
          value: "1"
---
apiVersion: v1
kind: Service
metadata:
  name: testforge-backend
spec:
  selector:
    app: testforge-backend
  ports:
  - port: 8000
    targetPort: 8000
  type: LoadBalancer
```

#### 前端部署 (testforge-frontend.yaml)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: testforge-frontend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: testforge-frontend
  template:
    metadata:
      labels:
        app: testforge-frontend
    spec:
      containers:
      - name: frontend
        image: your-registry/testforge-frontend:latest
        ports:
        - containerPort: 80
        env:
        - name: VITE_API_URL
          value: "http://testforge-backend:8000"
---
apiVersion: v1
kind: Service
metadata:
  name: testforge-frontend
spec:
  selector:
    app: testforge-frontend
  ports:
  - port: 80
    targetPort: 80
  type: LoadBalancer
```

**部署**:
```bash
kubectl apply -f testforge-backend.yaml
kubectl apply -f testforge-frontend.yaml
```

## 🔧 环境变量配置

### 后端环境变量

```env
# testforge/.env
PORT=8000
PYTHONUNBUFFERED=1
TESTCASES_DIR=./testcases
```

### 前端环境变量

```env
# forge-apis/.env
VITE_API_URL=http://localhost:8000        # 本地开发
# VITE_API_URL=https://api.example.com    # 生产环境
```

## 🔐 安全配置

### 生产环境CORS设置

修改 `testforge/src/api/main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.com"],  # 限制为你的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### HTTPS配置

使用Let's Encrypt免费SSL证书:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## 📊 监控和日志

### 后端日志

**使用Python logging**:
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

**查看Docker日志**:
```bash
docker logs testforge-backend -f
```

### 前端日志

在生产环境使用Sentry:
```bash
npm install @sentry/react
```

## 🧪 部署前检查清单

- [ ] 后端测试全部通过: `pytest`
- [ ] 前端构建成功: `npm run build`
- [ ] 环境变量配置正确
- [ ] CORS设置适当
- [ ] 数据库连接正常（如有）
- [ ] SSL证书配置（生产环境）
- [ ] 备份策略已制定
- [ ] 监控和告警已设置

## 🎯 推荐部署方案

### 个人/小型项目
- **后端**: Railway.app 或 Render.com（免费额度）
- **前端**: Vercel 或 Netlify（免费）
- **总成本**: $0-$10/月

### 中型项目
- **后端**: 阿里云ECS（1核2G）+ Nginx
- **前端**: 阿里云OSS + CDN
- **总成本**: ¥50-150/月

### 大型项目/企业
- **后端**: Kubernetes集群（多副本）
- **前端**: CDN + 多地部署
- **数据库**: 主从复制
- **缓存**: Redis集群
- **监控**: Prometheus + Grafana

## 📚 相关文档

- [testforge/GITHUB_SETUP.md](testforge/GITHUB_SETUP.md) - GitHub仓库设置
- [forge-apis/README_INTEGRATION.md](forge-apis/README_INTEGRATION.md) - 前后端集成说明
- [SETUP_GUIDE.md](SETUP_GUIDE.md) - 本地开发设置
- [QUICKSTART.md](QUICKSTART.md) - 快速启动指南

## 💡 故障排查

### 问题1: 前端无法连接后端
- 检查 `VITE_API_URL` 配置
- 验证后端服务运行正常
- 检查CORS设置
- 查看浏览器控制台错误

### 问题2: Docker容器无法启动
- 检查端口占用: `docker ps`
- 查看容器日志: `docker logs [container_id]`
- 验证Dockerfile语法

### 问题3: 部署后性能差
- 启用gzip压缩
- 配置CDN
- 优化数据库查询
- 增加服务器副本数

---

**需要帮助？**
- 提交Issue到GitHub仓库
- 查看详细文档
- 联系技术支持

🎉 **祝部署顺利！**

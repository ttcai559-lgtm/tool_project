# API测试平台 - 公网访问部署指南

## 方案一：内网穿透（最简单，适合演示和测试）

### 使用 cpolar（推荐国内用户）

#### 1. 安装 cpolar
- 访问：https://www.cpolar.com/
- 注册账号并下载客户端
- 安装后登录

#### 2. 配置穿透隧道

**方式A：使用命令行**
```bash
# 穿透前端（8080端口）
cpolar http 8080

# 会得到类似这样的公网地址：
# https://xxxx.cpolar.cn
```

**方式B：使用Web控制台**
1. 访问 http://localhost:9200
2. 创建隧道：
   - 名称：api-test-frontend
   - 协议：http
   - 本地端口：8080
3. 启动隧道

#### 3. 配置后端穿透
```bash
# 穿透后端（8000端口）
cpolar http 8000

# 会得到类似这样的公网地址：
# https://yyyy.cpolar.cn
```

#### 4. 修改前端配置

编辑 `forge-apis/.env.local`:
```env
VITE_API_URL=https://yyyy.cpolar.cn
```

重启前端服务：
```bash
cd forge-apis
npm run dev
```

#### 5. 分享给其他人
将前端的公网地址分享出去即可：
```
https://xxxx.cpolar.cn
```

---

## 方案二：云服务器部署（适合长期使用）

### 1. 购买云服务器
推荐平台：
- 阿里云（新用户优惠）
- 腾讯云（新用户优惠）
- 华为云

最低配置：1核2G，带宽1Mbps即可

### 2. 服务器环境配置

#### 安装基础软件
```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装 Python 3.11
sudo apt install python3.11 python3.11-venv python3-pip -y

# 安装 Node.js 18
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs -y

# 安装 Nginx
sudo apt install nginx -y
```

#### 配置防火墙
```bash
# 开放端口
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 8000
sudo ufw enable
```

### 3. 上传代码到服务器

#### 方式A：使用 Git（推荐）
```bash
# 在服务器上
cd /home/ubuntu
git clone <你的代码仓库地址>
```

#### 方式B：使用 SCP 上传
```bash
# 在本地电脑上
scp -r D:\Python_file\tool_project ubuntu@你的服务器IP:/home/ubuntu/
```

### 4. 部署后端

```bash
cd /home/ubuntu/tool_project/testforge

# 创建虚拟环境
python3.11 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 使用 gunicorn 运行（生产环境）
pip install gunicorn

# 启动后端
gunicorn src.api.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --daemon
```

### 5. 部署前端

```bash
cd /home/ubuntu/tool_project/forge-apis

# 安装依赖
npm install

# 配置后端地址
echo "VITE_API_URL=http://你的服务器IP:8000" > .env.production

# 构建生产版本
npm run build

# 将构建产物复制到 Nginx 目录
sudo cp -r dist/* /var/www/html/
```

### 6. 配置 Nginx

创建配置文件 `/etc/nginx/sites-available/api-test`:
```nginx
server {
    listen 80;
    server_name 你的域名或IP;

    # 前端
    location / {
        root /var/www/html;
        try_files $uri $uri/ /index.html;
    }

    # 后端API代理
    location /api/ {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

启用配置：
```bash
sudo ln -s /etc/nginx/sites-available/api-test /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 7. 配置 HTTPS（可选但推荐）

```bash
# 安装 certbot
sudo apt install certbot python3-certbot-nginx -y

# 申请证书
sudo certbot --nginx -d 你的域名
```

### 8. 设置开机自启

创建后端服务文件 `/etc/systemd/system/testforge.service`:
```ini
[Unit]
Description=TestForge API Service
After=network.target

[Service]
Type=notify
User=ubuntu
WorkingDirectory=/home/ubuntu/tool_project/testforge
Environment="PATH=/home/ubuntu/tool_project/testforge/venv/bin"
ExecStart=/home/ubuntu/tool_project/testforge/venv/bin/gunicorn src.api.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

[Install]
WantedBy=multi-user.target
```

启用服务：
```bash
sudo systemctl daemon-reload
sudo systemctl enable testforge
sudo systemctl start testforge
```

---

## 方案三：Docker 部署（最规范）

### 1. 创建 Dockerfile - 后端

在 `testforge/` 目录创建 `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2. 创建 Dockerfile - 前端

在 `forge-apis/` 目录创建 `Dockerfile`:
```dockerfile
FROM node:18-alpine as builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### 3. 创建 docker-compose.yml

在项目根目录创建:
```yaml
version: '3.8'

services:
  backend:
    build: ./testforge
    ports:
      - "8000:8000"
    restart: always
    volumes:
      - ./testforge/testcases:/app/testcases
      - ./testforge/environments:/app/environments

  frontend:
    build: ./forge-apis
    ports:
      - "80:80"
    depends_on:
      - backend
    restart: always
    environment:
      - VITE_API_URL=http://你的服务器IP:8000
```

### 4. 部署命令

```bash
# 构建并启动
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止
docker-compose down
```

---

## 访问控制建议

### 1. 添加简单认证

可以使用 Nginx 的 Basic Auth：
```bash
# 安装工具
sudo apt install apache2-utils

# 创建密码文件
sudo htpasswd -c /etc/nginx/.htpasswd admin

# 在 Nginx 配置中添加：
location / {
    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/.htpasswd;
    ...
}
```

### 2. IP白名单

在 Nginx 配置中：
```nginx
location / {
    allow 公司A的IP;
    allow 公司B的IP;
    deny all;
    ...
}
```

---

## 常见问题

### Q1: 如何查看服务器IP？
```bash
curl ifconfig.me
```

### Q2: 端口被占用怎么办？
```bash
# 查看端口占用
sudo lsof -i :8000
# 或
sudo netstat -tulpn | grep 8000
```

### Q3: 如何重启服务？
```bash
# 重启后端
sudo systemctl restart testforge

# 重启Nginx
sudo systemctl restart nginx
```

### Q4: 如何查看日志？
```bash
# 后端日志
sudo journalctl -u testforge -f

# Nginx日志
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
```

---

## 推荐方案对比

| 方案 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| 内网穿透 | 快速、免费、无需配置 | 速度慢、免费版不稳定 | 临时演示、测试 |
| 云服务器 | 稳定、速度快、可控 | 需要费用、配置复杂 | 长期使用、生产环境 |
| Docker | 规范、易迁移、隔离性好 | 学习成本高 | 团队协作、多环境部署 |

**建议：**
- 快速演示：使用 cpolar 或 ngrok
- 长期使用：购买云服务器部署
- 团队开发：使用 Docker 部署

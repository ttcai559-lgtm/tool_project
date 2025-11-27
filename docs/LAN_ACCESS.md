# 局域网访问配置指南

## 问题描述

当你想让同事通过局域网访问你的TestForge平台时，虽然他们能看到前端界面，但无法加载数据。

## 原因分析

### 网络架构

```
你的电脑 (192.168.40.59)
├── 后端服务 (0.0.0.0:8000) ✅ 监听所有网卡，局域网可访问
└── 前端服务 (0.0.0.0:8080) ✅ 监听所有网卡，局域网可访问

同事的电脑 (192.168.40.xxx)
└── 浏览器访问: http://192.168.40.59:8080/
    └── 前端加载后，向 http://localhost:8000 发API请求 ❌
        (这个localhost是同事电脑上的，不是你的！)
```

### 问题根源

前端是在**浏览器**中运行的JavaScript代码，当同事访问时：
1. ✅ 浏览器从你的服务器下载前端代码
2. ✅ 前端界面正常显示
3. ❌ 前端代码在**同事的浏览器**中运行
4. ❌ 向 `localhost:8000` 发请求，实际访问的是**同事电脑上的8000端口**
5. ❌ 同事电脑上没有后端服务，所以没有数据

## 解决方案

### 方法1：修改前端API配置（推荐）

#### 步骤1：确认你的局域网IP
```bash
ipconfig
# 找到类似 192.168.x.x 的IP地址
```

#### 步骤2：修改前端配置
编辑 `forge-apis/.env` 文件：
```bash
# 修改前
VITE_API_URL=http://localhost:8000

# 修改后（使用你的局域网IP）
VITE_API_URL=http://192.168.40.59:8000
```

#### 步骤3：重启前端服务
```bash
# 方式1：双击 stop_platform.bat，然后双击 start_all_services.vbs

# 方式2：手动重启
cd forge-apis
# Ctrl+C 停止当前服务
npm run dev
```

#### 步骤4：通知同事访问
同事访问：`http://192.168.40.59:8080/`

---

### 方法2：使用内网穿透（Cpolar）

如果你的IP经常变化，或需要外网访问，可以使用Cpolar：

详见：`docs/cpolar使用说明.md`

---

## 配置说明

### 完整的配置示例

**forge-apis/.env**
```bash
# TestForge Frontend Configuration

# Python Backend API URL
# For local use only: http://localhost:8000
# For LAN access: http://YOUR_IP:8000
VITE_API_URL=http://192.168.40.59:8000
```

### 环境变量说明

| 变量 | 说明 | 示例 |
|------|------|------|
| `VITE_API_URL` | 后端API地址 | `http://192.168.40.59:8000` |

**注意：**
- Vite的环境变量必须以 `VITE_` 开头
- 修改后必须重启前端服务才能生效

---

## 验证配置

### 1. 检查前端配置
打开浏览器控制台（F12），查看Network标签：
- ✅ 请求地址应该是 `http://192.168.40.59:8000/api/...`
- ❌ 如果是 `http://localhost:8000/api/...`，说明配置未生效

### 2. 检查后端可访问性
在同事电脑上测试：
```bash
curl http://192.168.40.59:8000/
# 应该返回：{"message":"TestForge API is running","version":"1.0.0","status":"healthy"}
```

或直接在浏览器访问：`http://192.168.40.59:8000/`

### 3. 检查防火墙
确保Windows防火墙允许8000和8080端口的入站连接：
```powershell
# 添加防火墙规则（以管理员身份运行）
netsh advfirewall firewall add rule name="TestForge Backend" dir=in action=allow protocol=TCP localport=8000
netsh advfirewall firewall add rule name="TestForge Frontend" dir=in action=allow protocol=TCP localport=8080
```

---

## 常见问题

### Q1: 修改了.env但没生效？
**A:** Vite需要重启才能读取新的环境变量。请：
1. 停止前端服务（Ctrl+C 或关闭窗口）
2. 重新运行 `npm run dev`

### Q2: 同事能访问前端，但API请求被CORS拦截？
**A:** 后端已配置允许所有来源的CORS：
```python
# testforge/src/api/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    ...
)
```

### Q3: 我的IP经常变化怎么办？
**A:** 三个选择：
1. 给电脑设置静态IP（路由器DHCP保留）
2. 每次IP变化后修改 `.env` 并重启
3. 使用内网穿透工具（Cpolar）

### Q4: 外网能访问吗？
**A:** 默认配置只能局域网访问。外网访问需要：
1. 路由器配置端口转发（8000, 8080）
2. 使用内网穿透工具（推荐Cpolar）

---

## 快速切换配置

### 本地开发模式
```bash
VITE_API_URL=http://localhost:8000
```
- 只有你自己能用
- 适合本地开发调试

### 局域网共享模式
```bash
VITE_API_URL=http://192.168.40.59:8000
```
- 局域网内所有人都能用
- 适合团队协作

### 内网穿透模式
```bash
VITE_API_URL=https://your-tunnel.cpolar.cn
```
- 外网也能访问
- 适合远程演示或测试

---

## 安全建议

1. **局域网使用**：默认配置已足够
2. **外网暴露**：
   - 添加访问认证
   - 使用HTTPS
   - 定期更换Cpolar地址
3. **生产环境**：
   - 部署到专用服务器
   - 配置域名和SSL证书
   - 使用Nginx反向代理

---

**更新日期**: 2025-11-27

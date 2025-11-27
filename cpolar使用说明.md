# cpolar 免费版使用指南

## 📥 第一步：安装 cpolar

1. **注册账号**
   - 访问 https://www.cpolar.com/
   - 点击右上角"注册"
   - 使用手机号或邮箱注册

2. **下载客户端**
   - 登录后，进入"下载"页面
   - 选择 Windows 版本下载
   - 安装到电脑上

3. **登录客户端**
   - 打开 cpolar 客户端
   - 输入你的账号密码登录
   - 或者使用命令行：`cpolar authtoken 你的token`

---

## 🚀 第二步：启动穿透服务

### 方法A：使用客户端界面（推荐新手）

1. **打开 cpolar 客户端**

2. **创建隧道1 - 前端**
   - 点击"隧道管理" -> "创建隧道"
   - 隧道名称：`frontend`
   - 协议：`http`
   - 本地地址：`8080`
   - 域名类型：选择"随机域名"
   - 点击"创建"

3. **创建隧道2 - 后端**
   - 再次点击"创建隧道"
   - 隧道名称：`backend`
   - 协议：`http`
   - 本地地址：`8000`
   - 域名类型：选择"随机域名"
   - 点击"创建"

4. **启动隧道**
   - 在隧道列表中，点击两个隧道的"开启"按钮
   - 记录下生成的公网地址

### 方法B：使用命令行（推荐熟练用户）

**打开两个命令行窗口：**

**窗口1 - 穿透前端：**
```cmd
cpolar http 8080
```
会显示类似：
```
Forwarding: https://abc123.cpolar.cn -> http://localhost:8080
```
**记下这个前端地址：https://abc123.cpolar.cn**

**窗口2 - 穿透后端：**
```cmd
cpolar http 8000
```
会显示类似：
```
Forwarding: https://xyz789.cpolar.cn -> http://localhost:8000
```
**记下这个后端地址：https://xyz789.cpolar.cn**

---

## ⚙️ 第三步：配置前端连接后端

1. **创建环境变量文件**
   - 在 `D:\Python_file\tool_project\forge-apis` 目录下
   - 创建文件 `.env.local`

2. **填入后端地址**
   ```env
   VITE_API_URL=https://xyz789.cpolar.cn
   ```
   （把 xyz789 替换成你实际的后端地址）

3. **重启前端服务**
   - 停止当前运行的前端（Ctrl+C）
   - 重新启动：
   ```cmd
   cd D:\Python_file\tool_project\forge-apis
   npm run dev
   ```

---

## 🎉 第四步：分享给其他人

把**前端的公网地址**发给其他公司的人：
```
https://abc123.cpolar.cn
```

他们在浏览器中打开这个地址，就能访问你的API测试平台了！

---

## ⚠️ 免费版注意事项

### 1. 域名会变
- 每次重启 cpolar 后，域名会变化
- 需要重新配置 `.env.local` 中的后端地址
- 并重新分享给别人新的前端地址

### 2. 同时在线隧道数限制
- 免费版同时只能开启 2 个隧道
- 正好够用（1个前端 + 1个后端）

### 3. 带宽限制
- 免费版有带宽限制，适合演示和测试
- 如果访问人数多，可能会慢

### 4. 如何保持域名不变？
- 升级到付费版（10元/月起）
- 可以绑定固定的二级域名
- 适合长期使用

---

## 🔧 常见问题

### Q1: cpolar 命令找不到？
需要将 cpolar 安装目录添加到系统环境变量 PATH 中。

### Q2: 连接失败？
1. 检查本地服务是否正在运行（8080 和 8000）
2. 检查 `.env.local` 中的后端地址是否正确
3. 检查是否已登录 cpolar

### Q3: 前端能访问，但调用接口失败？
检查 `.env.local` 中的 `VITE_API_URL` 是否配置正确。

### Q4: 如何查看隧道状态？
访问 cpolar 的本地管理界面：http://localhost:9200

### Q5: 如何关闭隧道？
- 命令行方式：按 Ctrl+C
- 客户端方式：点击"停止"按钮

---

## 📱 快速重启流程（收藏此流程）

当你重启电脑或关闭了 cpolar 后：

1. **启动本地服务**
   ```cmd
   # 窗口1 - 后端
   cd D:\Python_file\tool_project\testforge
   python -m uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

   # 窗口2 - 前端（先不启动，等配置好后端地址）
   ```

2. **启动 cpolar 穿透**
   ```cmd
   # 窗口3 - 后端穿透
   cpolar http 8000
   # 记录新的后端地址

   # 窗口4 - 前端穿透
   cpolar http 8080
   # 记录新的前端地址
   ```

3. **更新前端配置**
   - 编辑 `forge-apis/.env.local`
   - 更新 `VITE_API_URL` 为新的后端地址

4. **启动前端**
   ```cmd
   cd D:\Python_file\tool_project\forge-apis
   npm run dev
   ```

5. **分享新的前端地址**
   - 把新的前端公网地址发给其他人

---

## 🎯 推荐使用方式

### 临时演示（免费版）
- 每次使用前按照"快速重启流程"操作
- 把新地址发给需要访问的人

### 长期使用（付费版 10元/月）
- 绑定固定域名，比如 `api-test.cpolar.cn`
- 配置一次后不需要每次修改
- 更稳定，带宽更大

---

## 💡 小技巧

### 使用 cpolar Web 控制台
访问 http://localhost:9200 可以看到：
- 所有隧道状态
- 实时请求日志
- 流量统计

### 保存配置文件
创建 `cpolar.yml` 配置文件，可以一键启动多个隧道：
```yaml
tunnels:
  frontend:
    proto: http
    addr: 8080
  backend:
    proto: http
    addr: 8000
```

启动：
```cmd
cpolar start --all
```

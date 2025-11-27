# TestForge 后端服务管理指南

## 🎯 快速操作

### ✅ 启动后端（静默模式）
双击 `start_backend_hidden.vbs`
- 后台运行，无窗口
- 使用虚拟环境的Python
- 自动检测venv路径

### 🔍 检查后端状态
双击 `check_backend_status.vbs`
- 弹窗显示服务状态
- 显示API响应信息
- 快速判断服务是否正常

### 🛑 停止后端
双击 `stop_backend.vbs`
- 自动查找并结束后端进程
- 释放8000端口
- 完全静默操作

## 📋 命令行操作

### 启动服务
```bash
# 方式1：静默启动（推荐）
start_backend_hidden.vbs

# 方式2：显示窗口（调试用）
start_platform.bat

# 方式3：手动启动
cd testforge
python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
```

### 检查状态
```bash
# 方式1：使用VBS脚本
check_backend_status.vbs

# 方式2：使用curl
curl http://localhost:8000/

# 方式3：检查端口占用
netstat -ano | findstr :8000
```

### 停止服务
```bash
# 方式1：使用VBS脚本
stop_backend.vbs

# 方式2：使用批处理
stop_platform.bat

# 方式3：手动停止
# 找到PID
netstat -ano | findstr :8000
# 结束进程
taskkill /F /PID <PID号>
```

## 🔧 故障排查

### 问题1：双击VBS没反应
**可能原因：**
- 服务已经在运行
- 端口8000被占用

**解决方法：**
1. 双击 `check_backend_status.vbs` 查看状态
2. 如果显示运行中，说明服务正常
3. 如果需要重启，先双击 `stop_backend.vbs`，再双击 `start_backend_hidden.vbs`

### 问题2：前端提示"Failed to fetch"
**可能原因：**
- 后端服务未启动
- 端口被防火墙阻止

**解决方法：**
1. 双击 `check_backend_status.vbs` 确认服务状态
2. 如果未运行，双击 `start_backend_hidden.vbs` 启动
3. 在浏览器访问 http://localhost:8000/ 测试

### 问题3：VBS提示找不到venv
**可能原因：**
- 虚拟环境未创建

**解决方法：**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 问题4：端口已被占用
**现象：**
- 启动失败提示端口占用

**解决方法：**
```bash
# 查找占用进程
netstat -ano | findstr :8000

# 结束进程
taskkill /F /PID <PID号>

# 或使用脚本
stop_backend.vbs
```

## 📝 服务信息

### 后端服务配置
- **端口**: 8000
- **地址**: http://localhost:8000
- **API文档**: http://localhost:8000/docs
- **框架**: FastAPI + Uvicorn
- **热重载**: 已启用（--reload参数）

### 日志位置
- **显示模式**: CMD窗口实时显示
- **静默模式**: 无日志输出（后台运行）
- **应用日志**: testforge/logs/ 目录

## 🎛️ 运行模式对比

| 特性 | 静默模式 | 显示模式 |
|------|---------|---------|
| 启动方式 | `start_backend_hidden.vbs` | `start_platform.bat` |
| 窗口显示 | ❌ 无窗口 | ✅ 显示CMD窗口 |
| 日志查看 | ❌ 不可见 | ✅ 实时显示 |
| 适用场景 | 日常使用 | 开发调试 |
| 资源占用 | 低 | 稍高 |

## 💡 最佳实践

### 开发阶段
推荐使用**显示模式**：
- 能看到详细日志
- 方便调试错误
- 了解请求处理过程

### 日常使用
推荐使用**静默模式**：
- 界面简洁
- 资源占用少
- 不影响工作

### 问题排查
1. 先用 `check_backend_status.vbs` 检查状态
2. 如果有问题，切换到显示模式查看日志
3. 解决问题后再切回静默模式

---

**提示**: 所有VBS脚本都支持直接双击运行，无需命令行操作。

# TestForge 快速启动指南

## 🚀 一键启动

### 方式1: 双击启动 (推荐)

**直接双击**: `start_all_services.vbs`

脚本会自动:
1. ✅ 启动后端 FastAPI 服务 (端口 8000)
2. ✅ 启动 AI 测试用例生成工具 (端口 8501)
3. ✅ 启动前端 React 界面 (端口 8080)
4. ✅ 自动打开浏览器

### 方式2: 停止所有服务

**双击**: `stop_platform.bat`

会停止所有运行中的服务

---

## 📋 启动后会看到什么

### 第一个对话框 - 服务状态检查

如果已有服务在运行,会显示:
```
Services already running:
- Backend (port 8000)
- Streamlit (port 8501)

Do you want to:
YES - Start missing services only
NO - Restart all services
CANCEL - Exit
```

- **点击 YES**: 只启动缺失的服务
- **点击 NO**: 停止所有服务并重新启动
- **点击 CANCEL**: 退出不启动

### 第二个对话框 - 服务启动成功

显示所有服务的访问地址:
```
TestForge Platform Started Successfully!

=== Main Platform ===
Frontend:        http://localhost:8080/
Backend API:     http://localhost:8000/
API Docs:        http://localhost:8000/docs

=== AI TestCase Generator ===
Streamlit UI:    http://localhost:8501/

Opening main platform in 3 seconds...
```

### 第三个对话框 - 选择打开的服务

```
Which services do you want to open?

YES - Open Main Platform + API Docs
NO - Open Main Platform + AI Generator
CANCEL - Open Main Platform only
```

- **点击 YES**: 打开主平台 + API调试工具
- **点击 NO**: 打开主平台 + AI测试用例生成工具
- **点击 CANCEL**: 只打开主平台

---

## 🎯 启动后可以访问的地址

### 主平台

**前端界面**:
```
http://localhost:8080/
```
用于API测试、环境管理等核心功能

**后端API**:
```
http://localhost:8000/
```

**API调试工具 (Swagger)**:
```
http://localhost:8000/docs
```
可以直接在浏览器中测试所有API接口

### AI测试用例生成工具

**Streamlit 界面**:
```
http://localhost:8501/
```

**功能**:
- 上传需求文档 (.docx, .doc, .pdf)
- AI自动提取测试点
- 生成XMind思维导图
- 置信度评分 (✅高 / ⚠️中 / ❌低)

---

## 💡 常见使用场景

### 场景1: 日常API测试

**启动方式**: 双击 `start_all_services.vbs`
- 选择: YES (打开API Docs)

**使用**:
1. 主平台 (http://localhost:8080/) - 创建和运行测试用例
2. API Docs (http://localhost:8000/docs) - 调试接口

### 场景2: 生成测试用例

**启动方式**: 双击 `start_all_services.vbs`
- 选择: NO (打开AI Generator)

**使用**:
1. 打开 http://localhost:8501/
2. 上传需求文档
3. 点击"生成测试用例"
4. 下载XMind文件

### 场景3: 完整使用所有功能

**启动方式**: 双击 `start_all_services.vbs`
- 选择: YES 或 NO (任意)

**手动访问其他服务**:
- 主平台: http://localhost:8080/
- API文档: http://localhost:8000/docs
- AI工具: http://localhost:8501/

---

## 🔧 故障排查

### 问题1: 启动失败,提示端口被占用

**解决方法**:
1. 双击 `stop_platform.bat` 停止所有服务
2. 如果还是失败,重启电脑
3. 再次双击 `start_all_services.vbs`

### 问题2: 服务启动但浏览器无法访问

**检查端口**:
```bash
# 在CMD中运行
netstat -ano | findstr "8000"
netstat -ano | findstr "8080"
netstat -ano | findstr "8501"
```

应该看到这些端口在 LISTENING 状态

**如果端口正常,尝试**:
- 刷新浏览器 (Ctrl+F5)
- 清除浏览器缓存
- 使用无痕模式打开

### 问题3: AI测试用例生成失败

**检查AI配置**:

确保 `testforge/src/ai_testcase_gen/.env` 配置正确:
```env
ANTHROPIC_AUTH_TOKEN=cr_075a7d7c5c39be523c18da675acf2ac0ce6dbdd2129454370b17797eb43d20a0
ANTHROPIC_BASE_URL=http://47.251.110.97:3000/api
CLAUDE_MODEL=claude-sonnet-4-5-20250929
```

**查看错误日志**:
- Streamlit界面会显示详细错误
- 检查是否是网络问题(502错误)

---

## 📚 更多文档

- **访问地址详细说明**: `ACCESS_GUIDE.md`
- **AI功能集成指南**: `AI_TESTCASE_INTEGRATION_GUIDE.md`
- **XMind文件修复**: `testforge/src/ai_testcase_gen/XMIND_FIX_SUMMARY.md`

---

## ⚡ 快捷键参考

| 操作 | 快捷方式 |
|------|---------|
| 启动所有服务 | 双击 `start_all_services.vbs` |
| 停止所有服务 | 双击 `stop_platform.bat` |
| 刷新前端页面 | `Ctrl + F5` |
| 打开API文档 | 浏览器访问 `localhost:8000/docs` |
| 打开AI工具 | 浏览器访问 `localhost:8501` |

---

## ✅ 系统要求

- Windows 10/11
- Python 3.8+ (已安装在venv中)
- Node.js 16+ (用于前端)
- 至少 4GB 可用内存
- 端口 8000, 8080, 8501 未被占用

---

**最后更新**: 2025-11-28
**版本**: 1.0.0

---

## 🎉 开始使用吧!

现在你只需要双击 `start_all_services.vbs` 就可以启动整个TestForge平台了!

祝测试顺利! 🚀

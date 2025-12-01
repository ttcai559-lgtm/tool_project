# TestForge 平台 - 启动指南总览

## 🎯 超级简单启动

### 一键启动所有服务

```
双击: start_all_services.vbs
```

**就这么简单!** 🎉

脚本会自动启动:
- ✅ 前端界面 (端口 8080, 含AI测试用例生成)
- ✅ 后端API (端口 8000)

---

## 📍 启动后的访问地址

### 主要服务

| 服务 | 地址 | 说明 |
|------|------|------|
| **前端界面** | http://localhost:8080/ | API测试主平台 (含AI测试用例生成) |
| **后端API** | http://localhost:8000/ | REST API服务 |
| **API文档** | http://localhost:8000/docs | Swagger调试工具 |

### 使用场景

**场景1: API测试**
1. 访问 http://localhost:8080/
2. 创建和执行API测试用例
3. 使用 http://localhost:8000/docs 调试接口

**场景2: 生成测试用例**
1. 访问 http://localhost:8080/
2. 点击侧边栏"AI测试用例"
3. 上传需求文档 (.docx, .doc, .pdf)
4. AI自动生成XMind思维导图测试用例

---

## 🛑 停止服务

```
双击: stop_platform.bat
```

会安全停止所有运行中的服务

---

## 📚 详细文档

所有文档都在项目根目录:

### 入门文档
- **QUICK_START.md** - 快速启动指南 (推荐新手阅读)
- **ACCESS_GUIDE.md** - 访问地址和部署详解

### 集成文档
- **AI_TESTCASE_INTEGRATION_GUIDE.md** - AI功能集成指南
  - Vue.js 集成示例
  - React 集成示例
  - API接口文档

### 技术文档
- **testforge/src/ai_testcase_gen/XMIND_FIX_SUMMARY.md** - XMind文件修复说明

---

## 🚀 功能特性

### 主平台功能
- ✅ HTTP/HTTPS API测试
- ✅ Protobuf协议支持
- ✅ 自定义断言引擎
- ✅ 环境变量管理
- ✅ 测试用例存储

### AI测试用例生成
- ✅ 支持Word (.docx, .doc) 和 PDF文档
- ✅ 使用Claude Sonnet 4.5 AI模型
- ✅ 智能置信度评分 (✅高 / ⚠️中 / ❌低)
- ✅ 自动生成XMind思维导图
- ✅ 节省70-80%的人工输入时间

---

## ⚡ 快速参考

### 启动脚本
```
start_all_services.vbs  - 一键启动所有服务
stop_platform.bat       - 停止所有服务
```

### 访问地址
```
http://localhost:8080/      - 主平台 (含AI测试用例生成)
http://localhost:8000/docs  - API文档
```

### 端口分配
```
8000 - Backend API (FastAPI)
8080 - Frontend UI (React with AI)
```

---

## 🔧 故障排查

### 端口被占用?

**解决方法**:
1. 运行 `stop_platform.bat`
2. 如果还是失败,重启电脑
3. 再运行 `start_all_services.vbs`

### 查看端口状态

```bash
netstat -ano | findstr "8000"
netstat -ano | findstr "8080"
```

---

## 📋 系统要求

- Windows 10/11
- Python 3.8+ (已配置在venv中)
- Node.js 16+
- 至少 4GB 可用内存
- 端口 8000, 8080 未被占用

---

## 🎓 文档阅读顺序 (推荐)

1. **QUICK_START.md** - 了解基本操作
2. **ACCESS_GUIDE.md** - 了解所有访问地址
3. **AI_TESTCASE_INTEGRATION_GUIDE.md** - 深入了解AI功能

---

## 📞 获取帮助

查看相关文档:
- 启动问题 → `QUICK_START.md`
- 访问地址 → `ACCESS_GUIDE.md`
- AI功能 → `AI_TESTCASE_INTEGRATION_GUIDE.md`
- XMind问题 → `testforge/src/ai_testcase_gen/XMIND_FIX_SUMMARY.md`

---

## 🎉 开始使用

现在就双击 `start_all_services.vbs` 开始你的测试之旅吧!

**Happy Testing!** 🚀

---

**项目**: TestForge API测试平台 + AI测试用例生成器
**版本**: 1.0.0
**最后更新**: 2025-11-28

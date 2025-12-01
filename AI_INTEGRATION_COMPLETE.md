# AI测试用例生成 - 主平台集成完成

## 集成概述

AI测试用例生成功能现已完全集成到TestForge主平台前端界面中(http://localhost:8080/)。

## 更新内容

### 1. 前端集成

**新增文件**:
- `forge-apis/src/pages/AITestCaseGenerator.tsx` - AI测试用例生成React组件

**更新文件**:
- `forge-apis/src/App.tsx` - 添加 `/ai-testcases` 路由
- `forge-apis/src/components/Sidebar.tsx` - 添加侧边栏导航链接 "AI测试用例"

### 2. 启动脚本优化

**更新文件**:
- `start_all_services.vbs` - 移除Streamlit服务,简化为只启动前端和后端
- `stop_platform.bat` - 移除Streamlit相关清理逻辑

### 3. 文档更新

**更新文件**:
- `README_STARTUP.md` - 更新访问地址和端口说明,移除Streamlit引用

## 使用方法

### 启动平台

1. 双击 `start_all_services.vbs`
2. 脚本会自动启动:
   - ✅ 后端API (端口 8000)
   - ✅ 前端界面 (端口 8080, 含AI功能)

### 访问AI测试用例生成器

1. 打开浏览器访问 http://localhost:8080/
2. 在左侧边栏点击 "AI测试用例" (带有✨图标)
3. 上传需求文档 (.docx, .doc, .pdf)
4. 点击 "生成测试用例" 按钮
5. 等待30秒至2分钟,AI将自动生成测试用例
6. 查看生成结果统计(测试用例数、模块数、问题清单、需求缺陷)
7. 点击 "下载 XMind 文件" 保存到本地

## 技术架构

### 前端组件特性

- 使用React + TypeScript
- shadcn/ui组件库 (Card, Button, Input, Alert等)
- lucide-react图标库
- 实时加载状态和错误处理
- Toast通知反馈
- 响应式布局

### API集成

前端通过以下端点与后端通信:

**生成测试用例**:
```
POST http://localhost:8000/api/ai/generate-testcases?ai_model=claude
Content-Type: multipart/form-data
Body: file (需求文档)
```

**下载XMind文件**:
```
GET http://localhost:8000{result.download_url}
```

### 组件位置

```
forge-apis/src/
├── App.tsx (路由配置)
├── components/
│   ├── Layout.tsx (布局容器)
│   └── Sidebar.tsx (侧边栏导航)
└── pages/
    ├── Index.tsx (首页 - 接口管理)
    ├── Environments.tsx (环境管理)
    └── AITestCaseGenerator.tsx (AI测试用例生成器)
```

## 功能特性

### AI能力
- ✅ 使用Claude Sonnet 4.5 AI模型
- ✅ 支持Word (.docx, .doc) 和 PDF文档
- ✅ 智能提取测试点
- ✅ 置信度评分 (✅高 / ⚠️中 / ❌低)
- ✅ 自动生成XMind思维导图
- ✅ 问题清单和需求缺陷检测

### 用户体验
- ✅ 文件格式验证
- ✅ 实时生成进度提示
- ✅ 详细统计信息展示
- ✅ 一键下载XMind文件
- ✅ 错误提示和处理

## 访问地址

| 服务 | 地址 | 说明 |
|------|------|------|
| **主平台** | http://localhost:8080/ | 含AI测试用例生成 |
| **AI功能** | http://localhost:8080/ai-testcases | 直接访问AI页面 |
| **后端API** | http://localhost:8000/ | REST API服务 |
| **API文档** | http://localhost:8000/docs | Swagger调试工具 |

## 后端配置

确保以下配置文件正确:

**testforge/src/ai_testcase_gen/.env**:
```env
ANTHROPIC_AUTH_TOKEN=cr_075a7d7c5c39be523c18da675acf2ac0ce6dbdd2129454370b17797eb43d20a0
ANTHROPIC_BASE_URL=http://47.251.110.97:3000/api
CLAUDE_MODEL=claude-sonnet-4-5-20250929
```

## 故障排查

### 问题1: AI生成失败

**可能原因**:
- 后端服务未启动
- AI配置错误
- 网络连接问题

**解决方法**:
1. 检查 http://localhost:8000/docs 是否能访问
2. 检查 `.env` 配置文件
3. 查看浏览器控制台错误信息

### 问题2: 下载失败

**可能原因**:
- XMind文件未生成
- 文件路径错误

**解决方法**:
1. 检查 `testforge/outputs/` 目录
2. 重新生成测试用例
3. 查看浏览器控制台错误信息

## 开发说明

### 修改AI页面

编辑文件: `forge-apis/src/pages/AITestCaseGenerator.tsx`

### 修改侧边栏

编辑文件: `forge-apis/src/components/Sidebar.tsx`

### 修改路由

编辑文件: `forge-apis/src/App.tsx`

## 版本信息

- **版本**: 1.0.0
- **完成日期**: 2025-11-28
- **集成方式**: 前端组件集成,无需Streamlit独立服务
- **AI模型**: Claude Sonnet 4.5

## 总结

AI测试用例生成功能已完全集成到TestForge主平台中。用户无需访问单独的Streamlit页面,可以直接在主平台的统一界面中使用AI功能,实现了更好的用户体验和更简洁的架构。

---

**Happy Testing!** 🚀

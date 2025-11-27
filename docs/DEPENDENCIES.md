# TestForge 依赖说明

## 📦 依赖结构

项目有两个requirements文件：

### 1. `testforge/requirements.txt`
TestForge核心后端依赖（生产环境必需）

### 2. `requirements.txt` (根目录)
完整项目依赖，包含测试工具和开发工具

---

## 🔧 核心依赖说明

### Web框架
| 包 | 版本 | 用途 |
|---|------|------|
| `fastapi` | >=0.122.0 | 后端API框架 |
| `uvicorn[standard]` | >=0.38.0 | ASGI服务器 |
| `pydantic` | >=2.12.0 | 数据验证 |

### Protobuf支持（核心功能）⭐
| 包 | 版本 | 用途 |
|---|------|------|
| `protobuf` | >=6.33.0 | Protobuf运行时 |
| `grpcio` | >=1.76.0 | gRPC支持 |
| `grpcio-tools` | >=1.76.0 | Proto编译工具 |

### HTTP & 网络
| 包 | 版本 | 用途 |
|---|------|------|
| `requests` | >=2.32.0 | HTTP客户端 |
| `python-multipart` | >=0.0.9 | 文件上传支持 |

### 数据处理
| 包 | 版本 | 用途 |
|---|------|------|
| `pyyaml` | >=6.0.1 | YAML配置文件 |
| `jsonschema` | ==4.20.0 | JSON验证 |

### Web UI（可选）
| 包 | 版本 | 用途 |
|---|------|------|
| `streamlit` | >=1.51.0 | Streamlit UI (legacy) |

### 测试框架
| 包 | 版本 | 用途 |
|---|------|------|
| `pytest` | >=7.4.3 | 测试框架 |
| `pytest-cov` | >=4.1.0 | 测试覆盖率 |
| `pytest-html` | ==4.1.1 | HTML测试报告 |
| `pytest-xdist` | ==3.5.0 | 并行测试 |
| `allure-pytest` | ==2.13.2 | Allure报告 |

### 工具类
| 包 | 版本 | 用途 |
|---|------|------|
| `loguru` | ==0.7.2 | 日志库 |
| `python-dotenv` | ==1.0.0 | 环境变量 |
| `Faker` | ==20.1.0 | 测试数据生成 |

### 代码质量
| 包 | 版本 | 用途 |
|---|------|------|
| `black` | >=23.12.1 | 代码格式化 |
| `flake8` | >=6.1.0 | 代码检查 |

---

## 📥 安装方法

### 方式1：完整安装（推荐）
安装所有依赖，包括测试和开发工具：
```bash
pip install -r requirements.txt
```

### 方式2：仅安装核心依赖
只安装运行TestForge必需的依赖：
```bash
pip install -r testforge/requirements.txt
```

### 方式3：使用虚拟环境（推荐）
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

---

## 🔄 更新依赖

### 更新到最新版本
```bash
pip install -r requirements.txt --upgrade
```

### 生成当前安装的依赖
```bash
pip freeze > requirements_freeze.txt
```

### 检查过时的包
```bash
pip list --outdated
```

---

## 🐛 常见问题

### Q1: protobuf安装失败
**错误：**
```
ERROR: Could not build wheels for protobuf
```

**解决方案：**
```bash
# 升级pip和setuptools
pip install --upgrade pip setuptools wheel

# 重新安装
pip install protobuf>=6.33.0
```

### Q2: grpcio-tools编译失败
**错误：**
```
error: Microsoft Visual C++ 14.0 or greater is required
```

**解决方案（Windows）：**
1. 安装 Visual Studio Build Tools
2. 或使用预编译的wheel：
```bash
pip install --only-binary :all: grpcio grpcio-tools
```

### Q3: uvicorn[standard]安装问题
**解决方案：**
```bash
# 如果[standard]报错，可以分开安装
pip install uvicorn
pip install uvloop watchfiles httptools
```

### Q4: 依赖冲突
**解决方案：**
```bash
# 清理环境重新安装
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

---

## 📊 依赖大小

| 分类 | 大小（约） | 安装时间（约） |
|------|-----------|-------------|
| 核心依赖 | ~200MB | 1-2分钟 |
| 完整依赖 | ~300MB | 2-3分钟 |

---

## 🔐 安全建议

1. **使用虚拟环境** - 避免污染系统Python
2. **定期更新** - 修复安全漏洞
3. **锁定版本** - 生产环境使用精确版本号
4. **审计依赖** - 定期检查安全漏洞

```bash
# 安全审计（需要安装safety）
pip install safety
safety check -r requirements.txt
```

---

## 📝 版本兼容性

### Python版本要求
- **最低版本**: Python 3.8
- **推荐版本**: Python 3.11+
- **测试版本**: Python 3.11.9

### 主要依赖版本说明
- **FastAPI 0.122+**: 支持最新的Pydantic v2
- **Protobuf 6.33+**: 支持最新的Proto3语法
- **Pydantic 2.12+**: 更好的性能和类型提示

---

## 🎯 生产环境部署

### 最小化依赖
生产环境可以排除开发和测试工具：

```txt
# production-requirements.txt
fastapi>=0.122.0
uvicorn[standard]>=0.38.0
pydantic>=2.12.0
protobuf>=6.33.0
grpcio>=1.76.0
grpcio-tools>=1.76.0
requests>=2.32.0
python-multipart>=0.0.9
pyyaml>=6.0.1
```

---

**最后更新**: 2025-11-27

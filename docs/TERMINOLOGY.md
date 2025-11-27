# TestForge 术语说明

## 核心概念

### 媒体（Media / Environment）

**定义：**
在TestForge中，"媒体"指的是**广告媒体方**（如努比亚、vivo、倍孜等），每个媒体都有自己的：
- API接口地址
- 通信协议（JSON或Protobuf）
- Proto文件定义
- 默认请求参数

**技术实现：**
- 在代码中，媒体配置存储在 `testforge/environments/` 目录
- 每个媒体一个YAML配置文件
- API路径使用 `/api/environments/` 前缀（历史原因）

**为什么叫"Environment"？**
最初设计时参考了Postman的Environment概念，后来发现在广告测试场景中，更准确的表述应该是"媒体"，因为：
- 每个配置对应一个具体的广告媒体
- 不同媒体有不同的Proto定义和接口规范
- 测试的是与各个媒体的对接

### 用例（Test Case）

**定义：**
保存的测试请求配置，包括：
- 请求方法、URL、参数
- 关联的媒体
- Message类型
- 断言规则

**存储位置：**
`testforge/testcases/` 目录

### Message类型（Message Type）

**定义：**
Protobuf协议中定义的消息类型，如：
- BidRequest - 广告请求
- BidResponse - 广告响应
- NativeRequest - 原生广告请求
- NativeResponse - 原生广告响应

**注意事项：**
- 只有顶层Message类型可以用于请求/响应
- 嵌套的Message类型不能直接使用

## 术语对照表

| 中文 | 英文 | 代码中的名称 | 说明 |
|------|------|-------------|------|
| 媒体 | Media | environment | 广告媒体方配置 |
| 用例 | Test Case | testcase | 保存的测试请求 |
| 消息类型 | Message Type | message_type | Protobuf消息定义 |
| 请求消息 | Request Message | request_message_type | 请求使用的Message |
| 响应消息 | Response Message | response_message_type | 响应使用的Message |
| Proto文件 | Proto File | proto_file | Protobuf定义文件 |

## UI界面术语

### 推荐使用
- **媒体管理** - Media Management
- **创建媒体** - Create Media
- **选择媒体** - Select Media
- **媒体配置** - Media Configuration

### 历史遗留（仍在代码中）
- Environment Management
- Create Environment
- Select Environment

### 统一说明

在**用户文档**中，统一使用**"媒体"**这个术语，因为：
1. 更符合业务场景（广告测试）
2. 更容易理解（对应具体的广告媒体）
3. 避免与"测试环境"混淆

在**技术文档和代码**中：
- API路径保持 `/api/environments/`（避免破坏性变更）
- 变量名可能仍使用 `environment`
- 但注释和说明应标注"媒体配置"

## 使用示例

### ✅ 正确的说法
```
1. 创建媒体：努比亚
2. 为努比亚媒体上传Proto文件
3. 选择努比亚媒体发送请求
4. 配置媒体的默认参数
```

### ❌ 容易混淆的说法
```
1. 创建环境：努比亚  // "环境"容易和"测试环境"(dev/test/prod)混淆
2. 选择环境配置     // 不够明确
```

## 代码示例

### 配置文件结构
```yaml
# testforge/environments/努比亚.yaml
name: 努比亚              # 媒体名称
base_url: http://...     # 媒体API地址
protocol: protobuf       # 通信协议
default_params: {...}    # 该媒体的默认参数
```

### API调用
```python
# 获取媒体列表
GET /api/environments/

# 获取指定媒体
GET /api/environments/努比亚

# 上传媒体的Proto文件
POST /api/environments/努比亚/proto

# 获取媒体的Message类型
GET /api/environments/努比亚/messages
```

## 总结

**关键点：**
1. 用户界面：统一使用"媒体"
2. API路径：保持"environments"（兼容性）
3. 文档说明：优先使用"媒体"，必要时注明对应的技术术语
4. 代码注释：标注"媒体配置"避免歧义

---

**更新日期**: 2025-11-27

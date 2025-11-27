# Tests 目录说明

这个目录包含项目的测试脚本，用于验证各个功能模块。

## 🧪 测试文件列表

### test_nubia_proto.py
测试努比亚Proto文件的基本功能。

**测试内容：**
- Proto文件导入
- JSON到Protobuf转换
- Protobuf到JSON转换

**运行方法：**
```bash
python tests/test_nubia_proto.py
```

### test_api_messages.py
测试API获取Proto Message类型功能。

**测试内容：**
- 环境加载
- Proto文件检测
- Message类型列表获取

**运行方法：**
```bash
python tests/test_api_messages.py
```

### test_api_upload.py
测试API上传Proto文件功能。

**测试内容：**
- 环境检查
- Proto文件上传
- 编译结果验证
- Message类型返回

**运行方法：**
```bash
python tests/test_api_upload.py
```

### test_correct_message_type.py
测试正确的Message Type选择。

**测试内容：**
- BidRequest转换（正确）
- NativeRequest转换（错误示例）
- 字段匹配验证

**运行方法：**
```bash
python tests/test_correct_message_type.py
```

### test_full_request.py
测试完整的Protobuf请求流程。

**测试内容：**
- 环境配置加载
- Protobuf请求发送
- 响应解析验证
- 端到端流程

**运行方法：**
```bash
python tests/test_full_request.py
```

### test_upload_proto.py
测试Proto上传的完整流程。

**测试内容：**
- 环境创建
- Proto文件保存
- 编译过程
- Message类型提取
- API响应格式

**运行方法：**
```bash
python tests/test_upload_proto.py
```

## 🚀 运行所有测试

```bash
# 运行单个测试
python tests/test_nubia_proto.py

# 运行所有测试
cd tests
for f in test_*.py; do python "$f"; done
```

## 📝 测试说明

这些测试脚本主要用于：
- **开发调试**: 验证新功能是否正常工作
- **问题排查**: 定位Proto解析、API调用等问题
- **回归测试**: 确保修改没有破坏现有功能

## ⚠️ 注意事项

1. **后端服务**: 部分测试需要后端服务运行（如test_api_*.py）
2. **环境配置**: 测试会使用testforge/environments/中的配置
3. **数据文件**: 某些测试依赖testforge/proto_files/中的Proto文件

---

**建议**: 修改Proto处理相关代码后，运行这些测试确保功能正常。

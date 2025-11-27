"""模拟proto文件上传和message类型获取的完整流程"""
import sys
import os
sys.path.insert(0, 'testforge')

# 设置UTF-8输出
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.protocols.protobuf_handler import ProtobufHandler
from src.storage.environment_storage import EnvironmentStorage

# 初始化
protobuf_handler = ProtobufHandler("testforge/proto_files", "testforge/compiled_protos")
env_storage = EnvironmentStorage("testforge/environments")

# 测试环境名称
test_env_name = "nubia_test"

print("\n" + "="*60)
print("Testing Proto Upload and Message Type Extraction")
print("="*60 + "\n")

# Step 1: 创建测试环境
print("[Step 1] Creating test environment...")
env_data = {
    "name": test_env_name,
    "base_url": "http://test.example.com",
    "protocol": "protobuf",
    "default_headers": {"Content-Type": "application/x-protobuf"},
    "default_params": {}
}
env_storage.save_environment(env_data)
print(f"[OK] Environment '{test_env_name}' created")

# Step 2: 读取现有的proto文件内容
print("\n[Step 2] Reading proto file content...")
proto_file = "testforge/proto_files/努比亚/努比亚.proto"
with open(proto_file, "rb") as f:
    proto_content = f.read()
print(f"[OK] Read {len(proto_content)} bytes from proto file")

# Step 3: 保存proto文件（模拟上传）
print(f"\n[Step 3] Saving proto file to environment '{test_env_name}'...")
proto_path = protobuf_handler.save_proto_file(test_env_name, proto_content)
print(f"[OK] Proto file saved to: {proto_path}")

# Step 4: 编译proto文件
print("\n[Step 4] Compiling proto file...")
success, message = protobuf_handler.compile_proto(test_env_name)
if success:
    print(f"[OK] Compilation successful!")
    print(f"  Message: {message}")
else:
    print(f"[ERROR] Compilation failed!")
    print(f"  Error: {message}")
    sys.exit(1)

# Step 5: 获取message类型列表
print("\n[Step 5] Getting message types...")
message_types = protobuf_handler.get_message_types(test_env_name)

if message_types:
    print(f"[OK] Found {len(message_types)} message types:")
    for i, msg_type in enumerate(message_types, 1):
        print(f"  {i}. {msg_type}")
else:
    print("[ERROR] No message types found!")
    sys.exit(1)

# Step 6: 测试API返回格式
print("\n[Step 6] Simulating API response...")
api_response = {
    "message": "Proto file uploaded and compiled successfully",
    "proto_path": proto_path,
    "compilation_message": message,
    "message_types": message_types,
    "message_count": len(message_types)
}
print("[OK] API would return:")
import json
print(json.dumps(api_response, indent=2, ensure_ascii=False))

# 清理测试环境
print("\n[Cleanup] Removing test environment...")
env_storage.delete_environment(test_env_name)
protobuf_handler.delete_proto_files(test_env_name)
print("[OK] Test environment cleaned up")

print("\n" + "="*60)
print("SUCCESS: All tests passed! Proto upload flow is working correctly.")
print("="*60 + "\n")

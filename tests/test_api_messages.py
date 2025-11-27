"""测试API获取proto message类型"""
import sys
sys.path.insert(0, 'testforge')

from src.protocols.protobuf_handler import ProtobufHandler
from src.storage.environment_storage import EnvironmentStorage

# 初始化
protobuf_handler = ProtobufHandler("testforge/proto_files", "testforge/compiled_protos")
env_storage = EnvironmentStorage("testforge/environments")

name = "努比亚"

print(f"\n=== Testing Proto Message Types API for '{name}' ===\n")

# 1. 检查环境是否存在
environment = env_storage.load_environment(name)
if not environment:
    print(f"[ERROR] Environment '{name}' not found")
    sys.exit(1)

print(f"[OK] Environment found: {environment.get('name')}")
print(f"     Protocol: {environment.get('protocol')}")

# 2. 检查是否有proto文件
has_proto = protobuf_handler.has_proto_file(name)
print(f"\n[OK] Has proto file: {has_proto}")

if not has_proto:
    print("[ERROR] No proto file found!")
    sys.exit(1)

# 3. 获取message类型列表
print("\n[Testing] Getting message types...")
messages = protobuf_handler.get_message_types(name)

if messages:
    print(f"[OK] Found {len(messages)} message types:")
    for msg in messages:
        print(f"     - {msg}")
else:
    print("[ERROR] No message types found!")
    print("\nPossible reasons:")
    print("1. Proto file compilation failed")
    print("2. Proto file has no message definitions")
    print("3. Module loading failed")

print("\n=== Test Complete ===\n")

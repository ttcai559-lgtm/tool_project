"""测试API上传proto文件并查看响应"""
import requests
import json
import sys
import io

# 设置UTF-8输出
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# API基础URL
BASE_URL = "http://localhost:8000"

# 测试环境名称
env_name = "努比亚"

print(f"\n{'='*60}")
print(f"Testing Proto Upload API for environment: {env_name}")
print(f"{'='*60}\n")

# Step 1: 检查环境是否存在
print(f"[Step 1] Checking if environment '{env_name}' exists...")
response = requests.get(f"{BASE_URL}/api/environments/{env_name}")
if response.status_code == 200:
    env_data = response.json()
    print(f"[OK] Environment exists")
    print(f"  Protocol: {env_data.get('protocol')}")
else:
    print(f"[ERROR] Environment not found (status: {response.status_code})")
    sys.exit(1)

# Step 2: 读取proto文件
print(f"\n[Step 2] Reading proto file...")
proto_file_path = "testforge/proto_files/努比亚/努比亚.proto"
try:
    with open(proto_file_path, "rb") as f:
        proto_content = f.read()
    print(f"[OK] Read {len(proto_content)} bytes")
except Exception as e:
    print(f"[ERROR] Failed to read proto file: {e}")
    sys.exit(1)

# Step 3: 上传proto文件
print(f"\n[Step 3] Uploading proto file via API...")
files = {"file": ("nubia.proto", proto_content, "application/octet-stream")}
response = requests.post(f"{BASE_URL}/api/environments/{env_name}/proto", files=files)

print(f"Response status: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    print(f"[OK] Upload successful!")
    print(f"\n[Response Content]")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # 检查是否包含message_types
    if "message_types" in result:
        print(f"\n[GOOD] Response contains 'message_types' field")
        print(f"  Found {len(result['message_types'])} message types:")
        for msg_type in result['message_types']:
            print(f"    - {msg_type}")
    else:
        print(f"\n[BAD] Response does NOT contain 'message_types' field")
        print(f"  Available fields: {list(result.keys())}")
        print(f"\n  >>> This means the API code has NOT been updated yet.")
        print(f"  >>> You need to restart the backend service to load the new code.")
else:
    print(f"[ERROR] Upload failed!")
    print(f"Response: {response.text}")

# Step 4: 尝试获取message types
print(f"\n[Step 4] Trying to get message types via GET endpoint...")
response = requests.get(f"{BASE_URL}/api/environments/{env_name}/messages")
if response.status_code == 200:
    result = response.json()
    messages = result.get("messages", [])
    print(f"[OK] GET endpoint returned {len(messages)} message types:")
    for msg_type in messages:
        print(f"  - {msg_type}")
else:
    print(f"[ERROR] Failed to get messages (status: {response.status_code})")

print(f"\n{'='*60}")
print("Test Complete")
print(f"{'='*60}\n")

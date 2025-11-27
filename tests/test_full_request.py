"""测试完整的Protobuf请求流程"""
import requests
import json
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_URL = "http://localhost:8000"

print("\n" + "="*60)
print("Testing Full Protobuf Request Flow")
print("="*60 + "\n")

# 加载努比亚环境配置
print("[Step 1] Loading environment data...")
response = requests.get(f"{BASE_URL}/api/environments/努比亚")
if response.status_code != 200:
    print(f"[ERROR] Failed to load environment: {response.status_code}")
    sys.exit(1)

env_data = response.json()
print(f"[OK] Environment loaded: {env_data['name']}")
print(f"  Protocol: {env_data['protocol']}")
print(f"  Base URL: {env_data['base_url']}")

# 准备请求数据
request_data = {
    "method": "POST",
    "url": env_data['base_url'],
    "headers": env_data.get('default_headers', {}),
    "params": {},
    "body": env_data.get('default_params', {}),
    "environment": "努比亚",
    "request_message_type": "BidRequest",
    "response_message_type": "BidResponse",
    "assertions": []
}

print(f"\n[Step 2] Sending Protobuf request...")
print(f"  URL: {request_data['url']}")
print(f"  Request Type: {request_data['request_message_type']}")
print(f"  Response Type: {request_data['response_message_type']}")
print(f"  Body fields: {list(request_data['body'].keys())[:5]}...")

try:
    response = requests.post(
        f"{BASE_URL}/api/send-request",
        json=request_data,
        timeout=30
    )

    print(f"\n[Step 3] Response received:")
    print(f"  Status Code: {response.status_code}")

    if response.status_code == 200:
        result = response.json()
        print(f"  [OK] Success!")
        print(f"  API Status: {result['status']}")
        print(f"  Elapsed: {result.get('elapsedMs', 0):.2f}ms")

        if isinstance(result.get('data'), dict):
            print(f"  Response fields: {list(result['data'].keys())[:5]}...")
        else:
            print(f"  Response data: {str(result.get('data'))[:100]}...")
    else:
        print(f"  [ERROR] Request failed!")
        error_detail = response.json().get('detail', 'Unknown error')
        print(f"  Error: {error_detail}")

except requests.exceptions.Timeout:
    print(f"  [ERROR] Request timeout (>30s)")
except requests.exceptions.ConnectionError as e:
    print(f"  [ERROR] Connection failed: {e}")
except Exception as e:
    print(f"  [ERROR] Unexpected error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60 + "\n")

"""测试正确的Message Type"""
import sys
import io
import yaml

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.path.insert(0, 'testforge')
from src.protocols.protobuf_handler import ProtobufHandler

# 初始化
handler = ProtobufHandler("testforge/proto_files", "testforge/compiled_protos")

# 加载努比亚环境配置
with open('testforge/environments/努比亚.yaml', 'r', encoding='utf-8') as f:
    env_data = yaml.safe_load(f)

params = env_data.get('default_params', {})

print("\n" + "="*60)
print("Testing Correct Message Types for 努比亚")
print("="*60 + "\n")

# 测试1: 使用BidRequest（正确的）
print("[Test 1] Using BidRequest (CORRECT)...")
try:
    binary = handler.json_to_protobuf('努比亚', 'BidRequest', params)
    if binary:
        print(f"  ✓ SUCCESS: Converted to protobuf ({len(binary)} bytes)")
        # 反向转换验证
        json_back = handler.protobuf_to_json('努比亚', 'BidRequest', binary)
        if json_back:
            print(f"  ✓ Reverse conversion OK")
            print(f"  ✓ Fields: {list(json_back.keys())[:5]}...")
    else:
        print(f"  ✗ FAILED: Conversion returned None")
except Exception as e:
    print(f"  ✗ ERROR: {e}")

# 测试2: 使用NativeRequest（错误的）
print("\n[Test 2] Using NativeRequest (WRONG)...")
try:
    binary = handler.json_to_protobuf('努比亚', 'NativeRequest', params)
    if binary:
        print(f"  ✗ Unexpectedly succeeded ({len(binary)} bytes)")
    else:
        print(f"  ✓ FAILED as expected (params don't match NativeRequest structure)")
except Exception as e:
    print(f"  ✓ ERROR as expected: {str(e)[:100]}...")

# 显示NativeRequest需要的字段
print("\n[Info] NativeRequest expects these fields:")
print("  - ver (string)")
print("  - layout (LayoutId enum)")
print("  - adunit (AdUnitId enum)")
print("  - plcmtcnt (int32)")
print("  - seq (int32)")
print("  - assets (repeated Asset)")

print("\n[Info] BidRequest expects these fields (matching your data):")
print("  - id (string)")
print("  - imp (repeated Imp)")
print("  - app (App)")
print("  - device (Device)")
print("  - user (User)")
print("  - api_version, svr, cuid, etc.")

print("\n" + "="*60)
print("Recommendation:")
print("  Request Message Type:  BidRequest")
print("  Response Message Type: BidResponse")
print("="*60 + "\n")

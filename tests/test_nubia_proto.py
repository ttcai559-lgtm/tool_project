import yaml
import sys
sys.path.insert(0, 'testforge')

from src.protocols.protobuf_handler import ProtobufHandler

# 加载努比亚环境配置
with open('testforge/environments/努比亚.yaml', 'r', encoding='utf-8') as f:
    env_data = yaml.safe_load(f)

# 获取默认参数
params = env_data.get('default_params', {})
print('Testing JSON to Protobuf conversion for 努比亚...')

# 测试转换
handler = ProtobufHandler(proto_dir='testforge/proto_files', compiled_dir='testforge/compiled_protos')
try:
    binary = handler.json_to_protobuf('努比亚', 'BidRequest', params)
    if binary:
        print(f'[OK] Conversion successful! Binary size: {len(binary)} bytes')
        # 测试反向转换
        json_back = handler.protobuf_to_json('努比亚', 'BidRequest', binary)
        if json_back:
            print(f'[OK] Reverse conversion successful!')
            print(f'Fields in result: {list(json_back.keys())[:10]}')
            print('\nNo parsing errors found! The proto file is working correctly.')
        else:
            print('[ERROR] Reverse conversion failed')
    else:
        print('[ERROR] Conversion failed')
except Exception as e:
    print(f'[ERROR] Exception occurred: {e}')
    import traceback
    traceback.print_exc()

"""强制重启后端服务"""
import subprocess
import time
import sys
import os
import signal

print("\n" + "="*50)
print("Force Restarting Backend Service")
print("="*50 + "\n")

# Step 1: 找到并杀死占用8000端口的进程
print("[Step 1] Finding process on port 8000...")
try:
    result = subprocess.run(
        ["netstat", "-ano"],
        capture_output=True,
        text=True,
        shell=True
    )

    for line in result.stdout.split('\n'):
        if ':8000' in line and 'LISTENING' in line:
            parts = line.split()
            pid = int(parts[-1])
            print(f"  Found PID: {pid}")
            print(f"  Killing process...")

            # 使用Windows命令杀进程
            subprocess.run(["taskkill", "/F", "/PID", str(pid)], shell=True)
            print(f"  Process killed!")
            break
    else:
        print("  No process found on port 8000")
except Exception as e:
    print(f"  Error: {e}")

# Step 2: 等待端口释放
print("\n[Step 2] Waiting for port to be released...")
time.sleep(2)

# Step 3: 启动新的后端服务
print("\n[Step 3] Starting new backend service...")
try:
    # 切换到testforge目录
    os.chdir("testforge")

    # 启动uvicorn (不阻塞)
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == 'win32' else 0
    )
    print(f"  Backend started with PID: {process.pid}")
except Exception as e:
    print(f"  Error starting backend: {e}")
    sys.exit(1)

# Step 4: 等待服务启动
print("\n[Step 4] Waiting 5 seconds for service to start...")
time.sleep(5)

# Step 5: 测试API
print("\n[Step 5] Testing API...")
try:
    import requests
    response = requests.get("http://localhost:8000/")
    if response.status_code == 200:
        data = response.json()
        print(f"  API Status: {data.get('status')}")
        print(f"  API Version: {data.get('version')}")
        print("\n" + "="*50)
        print("Backend service restarted successfully!")
        print("="*50 + "\n")
    else:
        print(f"  API returned status: {response.status_code}")
except Exception as e:
    print(f"  Error testing API: {e}")
    print("\n  Note: Backend may still be starting up...")

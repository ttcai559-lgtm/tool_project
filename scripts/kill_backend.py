import psutil
import time

# 找到占用8000端口的进程并强制结束
for conn in psutil.net_connections():
    if conn.laddr.port == 8000 and conn.status == 'LISTEN':
        try:
            process = psutil.Process(conn.pid)
            print(f"Found process: {process.name()} (PID: {conn.pid})")
            print(f"Killing process...")
            process.kill()
            time.sleep(1)
            print(f"Process killed successfully!")
        except Exception as e:
            print(f"Error: {e}")
        break
else:
    print("No process found listening on port 8000")

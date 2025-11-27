"""
Network diagnostic script
Check network connection issues when installing pip dependencies
"""
import socket
import urllib.request
import sys

def check_dns(host):
    """Check DNS resolution"""
    try:
        ip = socket.gethostbyname(host)
        print(f"[OK] DNS resolved: {host} -> {ip}")
        return True
    except socket.gaierror as e:
        print(f"[FAIL] DNS resolution failed: {host}")
        print(f"       Error: {e}")
        return False

def check_http(url):
    """Check HTTP connection"""
    try:
        response = urllib.request.urlopen(url, timeout=5)
        print(f"[OK] HTTP connected: {url}")
        print(f"     Status: {response.status}")
        return True
    except Exception as e:
        print(f"[FAIL] HTTP connection failed: {url}")
        print(f"       Error: {e}")
        return False

def main():
    print("=" * 60)
    print("Network Connection Diagnostic")
    print("=" * 60)

    # Check DNS
    print("\n[1] DNS Resolution Check")
    print("-" * 60)
    dns_results = [
        check_dns("pypi.org"),
        check_dns("pypi.tuna.tsinghua.edu.cn"),
        check_dns("mirrors.aliyun.com"),
        check_dns("www.baidu.com")
    ]
    dns_ok = all(dns_results)

    # Check HTTP
    print("\n[2] HTTP Connection Check")
    print("-" * 60)
    http_results = [
        check_http("https://pypi.org/simple/"),
        check_http("https://pypi.tuna.tsinghua.edu.cn/simple/"),
        check_http("http://mirrors.aliyun.com/pypi/simple/")
    ]
    http_ok = any(http_results)

    # System info
    print("\n[3] System Information")
    print("-" * 60)
    print(f"Python version: {sys.version}")

    # Summary
    print("\n" + "=" * 60)
    print("Diagnostic Result")
    print("=" * 60)
    if dns_ok and http_ok:
        print("[OK] Network is working, you can install dependencies")
    elif not dns_ok:
        print("[FAIL] DNS resolution failed")
        print("\nSuggested solutions:")
        print("1. Check network connection")
        print("2. Change DNS server to 8.8.8.8 or 114.114.114.114")
        print("3. Run: ipconfig /flushdns")
        print("4. Check VPN or proxy settings")
    elif not http_ok:
        print("[FAIL] HTTP connection failed")
        print("\nSuggested solutions:")
        print("1. Check firewall settings")
        print("2. Check proxy configuration")
        print("3. Try using VPN")

if __name__ == "__main__":
    main()

import socket
from termcolor import colored

def scan(target, ports):
    print(colored(f"\nStarting scan for {target}...", "green"))
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        if sock.connect_ex((ip, port)) == 0:
            print(colored(f"[+] Port {port} is open", "blue"))
        sock.close()
    except Exception as e:
        print(colored(f"[-] Error scanning port {port}: {e}", "red"))

def main():
    targets = input("Enter target(s) to scan (comma-separated for multiple): ").split(",")
    ports = int(input("Enter the number of ports to scan: "))

    for target in targets:
        target = target.strip()
        if target:
            scan(target, ports)

if __name__ == "__main__":
    main()

import socket
import sys

def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)  # Timeout > 1 second
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Scan stopped by user.")
            sys.exit()
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            sys.exit()
        except socket.error:
            print("[!] Could not connect to server.")
            sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <target>")
        sys.exit()

    target = sys.argv[1]
    # Common ports to scan
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
    scan_ports(target, ports)

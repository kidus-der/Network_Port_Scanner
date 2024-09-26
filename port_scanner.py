import socket
import threading
from datetime import datetime

# scans a single port/not used in this script
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# uses multithreading to scan multiple ports
def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1): 
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()

# scans all ports on the target IP
def scan_all_ports(ip):
    print(f"Starting scan on {ip}")
    start_time = datetime.now()

    max_port = 65535
    chunk_size = 1000
    for i in range(1, max_port, chunk_size):
        end_port = min(i + chunk_size - 1, max_port)
        scan_ports(ip, i, end_port)
    
    end_time = datetime.now()
    print(f"Scanning completed in: {end_time - start_time}")

if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    scan_all_ports(target_ip)
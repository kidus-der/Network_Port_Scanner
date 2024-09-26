from scanner import scan_all_ports

def main():
    print("=== Python Port Scanner ===")
    target_ip = input("Enter the IP address to scan: ").strip()
    print(f"Starting scan on IP: {target_ip}")
    
    # start scanning process
    scan_all_ports(target_ip)

if __name__ == "__main__":
    main()
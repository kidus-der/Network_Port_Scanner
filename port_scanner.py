from scanner import scan_all_ports
from utils import parse_ip_addresses

def main():
    print("=== Python Port Scanner ===")
    ip_input = input("Enter the IP address(es) to scan (comma-separated for multiple): ").strip()

    # parse the input of IP address(es) into a list of IPs
    target_ips = parse_ip_addresses(ip_input)

    if not target_ips:
        print("No valid IP addresses provided. Exiting...")
        return

    print(f"Starting scan on IP(s): {', '.join(target_ips)}")
    
    # start scanning process
    scan_all_ports(target_ips)

if __name__ == "__main__":
    main()
from scanner import scan_all_ports
from utils import parse_ip_addresses
from cli import parse_arguments
from syn_scanner import syn_scan

def main():
    print("=== Python Port Scanner ===\n")

    # parse the user's arguments
    args = parse_arguments()

    # use the arguments for scanning
    # according to the user's input
    if args.ip:
        ip_addresses = parse_ip_addresses(','.join(args.ip))
        print(f"Starting {args.scan_type.upper()} scan on IP(s): {', '.join(ip_addresses)}")

        for ip in ip_addresses:
            if args.scan_type == "default":
                # Run the default port scan
                scan_all_ports([ip], start_port=args.start_port, end_port=args.end_port, max_threads=args.threads, save_results=args.save)
            elif args.scan_type == "syn":
                # Run the SYN scan on each port in the range
                for port in range(args.start_port, args.end_port + 1):
                    result = syn_scan(ip, port)
                    print(f"IP: {result['ip']} | Port {result['port']}:\t{result['status']}")
    else:
        print("No IP addresses provided. Use -i or --ip to specify one or more IP addresses.")
        print("Example: python port_scanner.py --ip 127.0.0.1 --start-port 1 --end-port 1000 --scan-type syn --save")


if __name__ == "__main__":
    main()
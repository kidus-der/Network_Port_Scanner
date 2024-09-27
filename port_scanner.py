from scanner import scan_all_ports
from utils import parse_ip_addresses
from cli import parse_arguments

def main():
    print("=== Python Port Scanner ===\n")

    # parse the user's arguments
    args = parse_arguments()

    # use the arguments for scanning
    # according to the user's input
    if args.ip:
        ip_addresses = parse_ip_addresses(','.join(args.ip))
        print(f"Starting scan on IP(s): {', '.join(ip_addresses)}")
        scan_all_ports(ip_addresses, start_port=args.start_port, end_port=args.end_port, max_threads=args.threads, save_results=args.save)
    else:
        print("No IP addresses provided. Use -i or --ip to specify one or more IP addresses.")
        print("Example: python port_scanner.py --ip 127.0.0.1 --start-port 1 --end-port 1000 --save")


if __name__ == "__main__":
    main()
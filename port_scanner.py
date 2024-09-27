from scanner import scan_all_ports
from utils import parse_ip_addresses
from cli import parse_arguments

def main():
    print("=== Python Port Scanner ===")

    # parse the user's arguments
    args = parse_arguments()

    # use the arguments for scanning
    # according to the user's input
    if args.ip:
        print(f"Starting scan on IP(s): {', '.join(args.ip)}")
        scan_all_ports(args.ip, start_port=args.start_port, end_port=args.end_port, max_threads=args.threads, save_results=args.save)
    else:
        print("No IP addresses provided. Use -i or --ip to specify one or more IP addresses.")
        print("Example: python port_scanner.py --ip 127.0.0.1 --start-port 1 --end-port 1000 --save")


    '''
    Below is the original main function from the port_scanner.py file:
    '''
    # ---------------------------------------------------------
    '''
    ip_input = input("Enter the IP address(es) to scan (comma-separated for multiple): ").strip()

    # parse the input of IP address(es) into a list of IPs
    target_ips = parse_ip_addresses(ip_input)

    if not target_ips:
        print("No valid IP addresses provided. Exiting...")
        return

    print(f"Starting scan on IP(s): {', '.join(target_ips)}")
    
    # start scanning process
    scan_all_ports(target_ips, max_threads=200)
    '''

if __name__ == "__main__":
    main()
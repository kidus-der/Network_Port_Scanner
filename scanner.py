import socket
import threading
from datetime import datetime
from banner_grabber import grab_banner
from service_detector import get_service
from concurrent.futures import ThreadPoolExecutor
from utils import parse_ip_addresses


results = []
lock = threading.Lock()  # lock to handle safe appending of results across threads


def scan_port(ip, port):
    """
    Scan a single port, check if it's open, and grab service name and banner.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service = get_service(port)  # get the service name
            banner = grab_banner(ip, port)  # try to grab the banner of a port
            with lock:
                results.append({"ip": ip, "port": port, "status": "Open", "service": service, "banner": banner})
        sock.close()
    except:
        with lock:
            results.append({"ip": ip, "port": port, "status": "Closed"})


def scan_ports(ip, start_port, end_port, max_threads=100):
    """
    Scan a range of ports using multithreading (at the port(chunk) and
    IP Address level) and collect results.
    """
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            future.result()  # check threads for completion


def scan_all_ports(ip_list, max_threads=100):
    """
    Scan all ports for the given IP address and display results.
    """
    print(f"Starting scan on IP addresses: {', '.join(ip_list)}")
    start_time = datetime.now()

    # scan ports in chunks for better performance
    max_port = 65535
    chunk_size = 1000

    # threadpool for concurrent scanning of IP addresses
    with ThreadPoolExecutor(max_workers=len(ip_list)) as ip_executor:
        ip_futures = []
        for ip in ip_list:
            print(f"Starting scan on IP: {ip}")
            ip_futures.append(ip_executor.submit(scan_ip_ports, ip, chunk_size, max_threads))

        # wait for all IP scanning threads to complete jobs
        for future in ip_futures:
            future.result()

    end_time = datetime.now()
    print(f"Scanning completed in: {end_time - start_time}")
    
    # print all results
    print("\nScan Results:")
    for result in results:
        if result["status"] == "Open":
            print(f"IP: {result['ip']} | Port {result['port']}:\t{result['status']} ({result['service']})")
            print(f"  Banner: {result['banner']}")
        else:
            print(f"IP: {result['ip']} | Port {result['port']}:\t{result['status']}")


def scan_ip_ports(ip, chunk_size, max_threads):
    """
    Scan all ports for a single IP address using multithreading for chunks of ports.
    """
    max_port = 65535
    for i in range(1, max_port, chunk_size):
        end_port = min(i + chunk_size - 1, max_port)
        print(f"  Scanning {ip} ports {i} to {end_port}...")
        scan_ports(ip, i, end_port, max_threads)
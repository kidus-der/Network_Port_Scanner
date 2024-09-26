import socket
import threading
from datetime import datetime
from banner_grabber import grab_banner
from service_detector import get_service


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
                results.append({"port": port, "status": "Open", "service": service, "banner": banner})
        sock.close()
    except:
        with lock:
            results.append({"port": port, "status": "Closed"})


def scan_ports(ip, start_port, end_port):
    """
    Scan a range of ports using multithreading and collect results.
    """
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()
        threads.append(thread)

    # ensure all threads have completed
    for thread in threads:
        thread.join()


def scan_all_ports(ip):
    """
    Scan all ports for the given IP address and display results.
    """
    print(f"Starting scan on {ip}")
    start_time = datetime.now()

    # scan ports in chunks for better performance
    max_port = 65535
    chunk_size = 1000

    for i in range(1, max_port, chunk_size):
        end_port = min(i + chunk_size - 1, max_port)
        print(f"Scanning ports {i} to {end_port}...")
        scan_ports(ip, i, end_port)

    end_time = datetime.now()
    print(f"Scanning completed in: {end_time - start_time}")
    
    # print all results
    print("\nScan Results:")
    for result in results:
        if result["status"] == "Open":
            print(f"Port {result['port']}:\t{result['status']} ({result['service']})")
            print(f"  Banner: {result['banner']}")
        else:
            print(f"Port {result['port']}:\t{result['status']}")

# service_detector.py
# this module handles service detection based on port numbers.
port_services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "Microsoft RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "Microsoft DS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Proxy",
}

def get_service(port):
    """
    Given a port number, return the associated service name.
    If the port is not known, return 'Unknown Service'.
    """
    return port_services.get(port, "Unknown Service")

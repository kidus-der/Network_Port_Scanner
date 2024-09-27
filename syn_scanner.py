# syn_scanner.py

from scapy.all import sr1, IP, TCP

def syn_scan(ip, port):
    """
    Perform a SYN scan on a single IP and port.
    Return the scan result based on the TCP flags received.
    """
    # Create the SYN packet
    syn_packet = IP(dst=ip) / TCP(dport=port, flags="S")

    # Send the packet and capture the response
    response = sr1(syn_packet, timeout=1, verbose=True)

    # Analyze the response
    if response:
        if response.haslayer(TCP):
            if response[TCP].flags == "SA":  # SYN-ACK received
                return {"ip": ip, "port": port, "status": "Open"}
            elif response[TCP].flags == "RA":  # RST-ACK received
                return {"ip": ip, "port": port, "status": "Closed"}
    return {"ip": ip, "port": port, "status": "Filtered"}

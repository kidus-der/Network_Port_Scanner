'''
    File containing helper functions used throughout this
    scanner project.
'''

def parse_ip_addresses(ip_input):
    """
    Parse the input string to extract multiple IP addresses.
    Accepts comma-separated IP addresses and returns a list of IPs.

    e.g. input: "192.168.0.1, 192.168.0.2"
    parsed into: ['192.168.0.1', '192.168.0.2']
    """
    ip_list = [ip.strip() for ip in ip_input.split(',') if ip.strip()]
    return ip_list
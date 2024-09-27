# Python Network Port Scanner

A simple yet powerful port scanner built using Python. This project allows users to scan for open ports on specified IP addresses, identify services running on those ports, and retrieve service banners.

## Features

- **Port Scanning**: Scan a range of ports on one or more IP addresses to identify open ports.
- **Service Detection**: Identify common services associated with open ports.
- **Banner Grabbing**: Attempt to retrieve banners from services running on open ports.
- **SYN Scanning**: Perform a stealthy SYN scan to identify open ports without establishing a full connection. (Requires `sudo` permissions)

## Installation

To use this port scanner, you need to have Python 3 installed on your system along with the required libraries. You can install the necessary libraries using pip:

```bash
pip install scapy
```

## Usage

To run the port scanner, use the following command structure:

```bash
python3 port_scanner.py --ip <IP_ADDRESS> --start-port <START_PORT> --end-port <END_PORT> [--scan-type <SCAN_TYPE>] [--threads <NUMBER_OF_THREADS>] [--save]
```

## Arguments

 - --ip: Specify one or more IP addresses to scan.
 - --start-port: Starting port number to scan (default is 1).
 - --end-port: Ending port number to scan (default is 1000).
 - --scan-type: Choose between different scan types, currently supporting:
    - default: A basic TCP connect scan (default behavior).
    - syn: A SYN scan (requires sudo permissions).
 - --threads: Number of threads to use for scanning (default is 100).
 - --save: Save the scan results to a log file.

## Example Commands
1) Basic TCP Connect Scan:
```bash
python3 port_scanner.py --ip 127.0.0.1 --start-port 1 --end-port 15
```

2) SYN Scan (requires sudo):
```bash
sudo python3 port_scanner.py --ip 127.0.0.1 --start-port 1 --end-port 15 --scan-type syn
```

## Notes for Documentation

The start port and end port of the scan are defaulted to 1 and 1000, respectively. For a full breadth scan of an entire IP, users will need to specify the start port with the flag and value (-sp 1) and the end port as (-ep 65535).

The current local stash contains unfinished and buggy code for choosing scan types.
Running a SYN command requires extra permissions (using sudo):
Example: sudo python3 port_scanner.py --ip 127.0.0.1 --start-port 1 --end-port 15 --scan-type syn

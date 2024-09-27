import argparse

def parse_arguments():
    """
    Parse command-line arguments and return them as a Namespace object.
    """
    parser = argparse.ArgumentParser(description="Python Port Scanner CLI")

    # add arguments for IP address(es) and port range
    parser.add_argument("-i", "--ip", type=str, nargs="+", help="Specify one or more IP addresses to scan.")
    parser.add_argument("-sp", "--start-port", type=int, default=1, help="Starting port number to scan.")
    parser.add_argument("-ep", "--end-port", type=int, default=1000, help="Ending port number to scan.")
    
    # add optional features
    # for the user
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads to use for scanning.")
    parser.add_argument("-s", "--save", action="store_true", help="Save the scan results to a file.")
    parser.add_argument("-m", "--multiple", action="store_true", help="Specify multiple IP addresses to scan concurrently.")

    # parse through the arguments and return
    return parser.parse_args()

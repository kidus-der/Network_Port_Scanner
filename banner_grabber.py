import socket

def grab_banner(ip, port):
    """
    Attempt to grab the banner of a service running on the specified port.
    Returns the banner if found, or 'Banner Not Retrieved' otherwise.
    """
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        sock.send(b'Hello\r\n')  # send a simple message to trigger a banner response
        banner = sock.recv(1024).decode().strip()  # receive the banner
        sock.close()
        return banner if banner else "Banner Not Retrieved"
    except:
        return "Banner Not Retrieved"

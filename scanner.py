import socket
import ipaddress

class NetworkScanner:
    """
    A class to represent a network scanner.

    ...

    Attributes
    ----------
    network : str
        the IP network to scan

    Methods
    -------
    scan():
        Scans the network for active hosts.
    """

    def __init__(self, network):
        """
        Constructs all the necessary attributes for the network scanner object.

        Parameters
        ----------
            network : str
                the IP network to scan
        """
        try:
            self.network = ipaddress.ip_network(network)
        except ValueError:
            raise ValueError("Invalid network. Please provide a valid IP network.")

    def scan(self):
        """
        Scans the network for active hosts.

        Iterates over all possible IP addresses in the network and tries to establish a socket connection
        to port 80. If the connection is successful, it prints out the IP address.
        """

        for ip in self.network.hosts():
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)
                    s.connect((str(ip), 80))
                    print(f"Host {ip} has port 80 open.")
            except (socket.timeout, ConnectionRefusedError, socket.error):
                print(f"Host {ip} does not have port 80 open.")
                continue

if __name__ == "__main__":
    try:
        network = input("Enter an IP network to scan (e.g.): ")
        print(f"Scanning network {network}...")
        scanner = NetworkScanner(network)
        scanner.scan()
        print("Scan complete.")
    except ValueError as e:
        print(e)

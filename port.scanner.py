import socket

def scan_ports(target_ip, port_range):
    print(f"Scanning {target_ip} from ports {port_range[0]} to {port_range[1]}")

    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()

if __name__ == "__main__":
    target = input("Enter target IP: ")
    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))

    scan_ports(target, (start_port, end_port))



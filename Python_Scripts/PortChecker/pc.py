import socket
from colorama import Fore, init, Style

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

def main(): 
    init()
    ascii_art = Fore.GREEN + """
=====================================
|            PORT CHECKER           |
=====================================
>>> Made by ZownHori
>>> https://github.com/JayAlvinCVallescas/Scripts/tree/main/Python_Scripts/PortChecker
----------------------------------------------------------------------------------------------------"""
    common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 137, 139, 143, 443, 445, 1433, 1434, 3306, 3389, 8080, 8443]  # Add more ports as needed
    print(ascii_art)
    target = input("IP: ")
    print(Fore.GREEN + f"\nTARGET IP: {target}\nPORT      STATUS")
    
    for port in common_ports:
        result = sock.connect_ex((target, port))
        if result == 0:
            status = "OPEN"
        else:
            status = "CLOSE"
        print(f"{port:<10} {status}")

if __name__ == "__main__":
    main()

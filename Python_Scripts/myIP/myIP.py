import socket
import requests
from colorama import Fore, init

def private_IP():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname) 
    return f"Your private IP address is: {ip}"

def public_IP():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip = response.text
    return f"Your public IP address is: {ip}"

def main():
    init()
    description = Fore.GREEN + """
=====================================
|        IP Address Information     |
=====================================
Description: A Python script that enables users to view their public and private addresses.
            
>>> Made by ZownHori
>>> https://github.com/JayAlvinCVallescas/Scripts/tree/main/Python_Scripts/myIP
--------------------------------------------------------------------- """
    print(description)
   
    priv_ip = private_IP()
    print(priv_ip)
    pub_ip = public_IP()
    print(pub_ip)

if __name__ == "__main__":
    main()

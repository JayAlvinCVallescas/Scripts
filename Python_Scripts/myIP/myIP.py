import socket
import requests

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
   priv_ip = private_IP()
   print(priv_ip)
   pub_ip = public_IP()
   print(pub_ip)

if __name__ == "__main__":
    main()
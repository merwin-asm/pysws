import os
import time
import requests
import subprocess
import socket
from ipaddress import IPv4Network


process = None

def start_pysws():
    global process
    process = subprocess.Popen(['python3', '/root/pysws/main.py'])

def stop_pysws():
    global process
    process.kill()
    
def download_pysws(server):
    response = requests.get(server + "new", stream=True)
    filename = "pysws.zip"
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded file saved as {filename}")
    else:
        print(f"Failed to download. Status code: {response.status_code}")
    
    if os.path.exists("/root/pysws"):
        os.system("rm -rf /root/pysws")

    os.system("unzip pysws.zip -d /root/pysws")

def scan_local_ips(port=9025, timeout=0.5, subnet='192.168.1.0/24'):
    for ip in IPv4Network(subnet):
        url = f'http://{ip}:{port}/'
        try:
            response = requests.get(url, timeout=timeout)
            if response.text == "pysws_env":
                return ip

        except requests.RequestException:
            pass  # No response, ignore
        except KeyboardInterrupt:
            print("\nScan interrupted.")
            break
    return input("What is the Host Web Server IP :")

server = "http://" +scan_local_ips() + ":9025/"

start_pysws()

while True:
    r = requests.get(server + "signal")
    if r.text == "none":
        pass
    elif r.text == "new":
        stop_pysws()
        download_pysws(server)
        start_pysws()
    elif r.text == "restart":
        stop_pysws()
        start_pysws()

    time.sleep(1)

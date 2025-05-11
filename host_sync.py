# web-server running on local ip : 9025

import os
from flask import Flask, send_file
import re
import subprocess


def mod_time(file_path):
    # Get the last modified time of the file
    mod_time = os.path.getmtime(file_path)
    return mod_time

def local_ip():
    try:
        result = subprocess.run(['ifconfig'], capture_output=True, text=True)
        output = result.stdout

        # Find wlan0 or similar Wi-Fi interface
        wifi_blocks = re.split(r'\n(?=\S)', output)
        for block in wifi_blocks:
            if re.search(r'^wlan\d|wl\w+', block):
                # Look for IP address (inet)
                match = re.search(r'inet (?:addr:)?(\d+\.\d+\.\d+\.\d+)', block)
                if match:
                    return match.group(1)
        return None
    except Exception as e:
        print(f"Error getting Wi-Fi IP: {e}")
        return None

os.system("./testrun.sh")
prev_mod = mod_time("pysws.zip")

app = Flask(__name__)
@app.route('/')
def root():
    return "pysws_env"

@app.route('/signal')
def signal():
    mt = mod_time("pysws.zip")
    if prev_mod != mt:  
        prev_mod = mt
        return "new"

    if os.path.exists(".restart_cmd"):
        os.system("rm .restart_cmd")
        return "restart"
    
    return "none"

@app.route('/new')
def new():
    return send_file('pysws.zip', as_attachment=True)

if __name__ == '__main__':
    app.run(local_ip(), 9025)


import os

# setting up autologin to root
os.system("mkdir -p /etc/init.d")
with open("/etc/inittab") as f:
    data = f.read()
with open("/etc/inittab", "w") as f:
    if "-n -l /bin/login -f root" not in data:
        f.write(data.replace("38400", 
        " -n -l /bin/login -f root 38400 ", 1))

# setting up auto start for 'env_sync.py'
os.system("cp env_sync.py /root/env_sync.py")
os.system('echo "python3 /root/env_sync.py" > /root/.profile')

# installing requirements from 'requirments.txt'
os.system("pip3 install -r requirements.txt --break-system-packages")
os.system("cd pysws")
os.system("pip3 install -r requirements.txt --break-system-packages")

# reboot
os.system("reboot")

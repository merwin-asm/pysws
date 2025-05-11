import os

# setting up autologin to root
with open("/etc/inittab") as f:
    data = f.read()
with open("/etc/inittab", "w") as f:
    f.write(data.replace("tty1::respawn:/sbin/agetty 38400 tty1", 
        "tty1::respawn:/sbin/agetty --autologin root --noclear 38400 tty1"))

# setting up auto start for 'env_sync.py'
os.system("cp env_sync.py /root/env_sync.py")
os.system('echo "python3 /root/env_sync.py" > /root/.profile')

# installing requirements from 'requirments.txt'
os.system("pip3 install -r requirements.txt")
cd pysws
os.system("pip3 install -r requirements.txt")

# reboot
os.system("reboot")

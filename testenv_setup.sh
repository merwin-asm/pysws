read -p "Have you uncommented community mirror in /etc/apk/repositories ? cant proceed without it.. (y/n): " ans
[ "$ans" = "y" ] || exit

apk update
apk add python3 
apk add py3-pip
apk add git

cp inittab_new /etc/inittab

git clone https://github.com/merwin-asm/pysws.git


# setting up auto start for 'env_sync.py'
cp env_sync.py /root/env_sync.py
echo "python3 /root/env_sync.py" > /.profile

# installing requirements from 'requirments.txt'
pip3 install -r requirements.txt --break-system-packages
cd pysws
pip3 install -r requirements.txt --break-system-packages

read -p "Finished setting up.. reboot? (y/n): " ans
[ "$ans" = "y" ] || exit

# reboot
reboot
~

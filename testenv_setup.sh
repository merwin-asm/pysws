sed '3,$ s/^#//' /etc/apk/repositories > /etc/apk/repositories
apk update
apk add python3 
apk add py3-pip
apk add git

cp inittab_new /etc/inittab

git clone https://github.com/merwin-asm/pysws.git


# setting up auto start for 'env_sync.py'
cp env_sync.py /root/env_sync.py
echo "python3 /root/env_sync.py" > ~/.profile

# installing requirements from 'requirments.txt'
pip3 install -r requirements.txt --break-system-packages
cd pysws
pip3 install -r requirements.txt --break-system-packages

# reboot
reboot
~

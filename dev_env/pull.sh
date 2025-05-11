sudo mkdir /mnt/hostshare
sudo mount -t 9p -o trans=virtio hostshare /mnt/hostshare
cp -r /mnt/hostshare/pysws pysws

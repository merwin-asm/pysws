#sudo apt update
#sudo apt install qemu-system


#wget http://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.10.0-amd64-netinst.iso - deb
#wget https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-virt-3.19.1-x86_64.iso

qemu-img create -f qcow2 testenv-disk.qcow2 2G

qemu-system-x86_64 \
  -cdrom alpine-virt-3.19.1-x86_64.iso \
  -hda testenv-disk.qcow2 \
  -boot d \
  -m 1024 \
  -net nic -net user \
  -enable-kvm
  

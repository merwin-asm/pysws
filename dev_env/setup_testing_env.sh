sudo apt update
sudo apt install qemu-system

wget https://mirror.rackspace.com/archlinux/iso/latest/archlinux-x86_64.iso

qemu-img create -f qcow2 archlinux.img 10G

qemu-system-x86_64 \
  -m 1524 \
  -smp 2 \
  -cdrom archlinux-x86_64.iso \
  -drive file=archlinux.img,format=qcow2 \
  -boot d \
  -net nic -net user \

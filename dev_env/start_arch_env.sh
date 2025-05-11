qemu-system-x86_64 \
  -m 2024 \
  -smp 2 \
  -drive file=archlinux.img,format=qcow2 \
  -boot c \
  -net nic -net user \
  -virtfs local,path=$HOME/qemu_share,mount_tag=hostshare,security_model=passthrough,id=hostshare \

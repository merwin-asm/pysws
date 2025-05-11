qemu-system-x86_64 \
  -hda testenv-disk.qcow2 \
  -m 1024 \
  -boot c \
  -net nic -net user \
  -virtfs local,path=$HOME/qemu_share,mount_tag=hostshare,security_model=passthrough,id=hostshare \
  -enable-kvm 


##cfdisk /dev/sda # uncomment when actually needed
# Create one Linux partition, write and quit
##mkfs.ext4 /dev/sda1 # uncomment when actually needed
mount /dev/sda1 /mnt
pacstrap /mnt base linux linux-firmware grub
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt


ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
hwclock --systohc

echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf


echo "archvm" > /etc/hostname
passwd

pacman -S grub
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg


exit
umount -R /mnt
reboot

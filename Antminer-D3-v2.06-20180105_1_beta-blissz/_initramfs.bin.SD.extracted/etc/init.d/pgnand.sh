#!/bin/sh 
# RED LED: GPIO1_13: GPIO45
if [ ! -d /sys/class/gpio/gpio45 ]; then
    echo 45 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio45/direction
fi

# GREEN LED: GPIO0_23: GPIO23
if [ ! -d /sys/class/gpio/gpio23 ]; then
    echo 23 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio23/direction 
fi

echo 1 > /sys/class/gpio/gpio45/value
echo 1 > /sys/class/gpio/gpio23/value

echo "--------------SD2Nand begin-------------"
if [ ! -d /mnt/mmc1/ ]; then
	mkdir -p /mnt/mmc1/	
	mount -t vfat /dev/mmcblk0p1 /mnt/mmc1/
	MOUNT=1
fi

if [ -e /mnt/mmc1/nand/MLO ];then
	echo "------flash MLO------------"
	flash_erase /dev/mtd0 0x0 0x1
	nandwrite -p /dev/mtd0 /mnt/mmc1/nand/MLO
	flash_erase /dev/mtd1 0x0 0x1
	nandwrite -p /dev/mtd1 /mnt/mmc1/nand/MLO
	flash_erase /dev/mtd2 0x0 0x1
	nandwrite -p /dev/mtd2 /mnt/mmc1/nand/MLO
	flash_erase /dev/mtd3 0x0 0x1
	nandwrite -p /dev/mtd3 /mnt/mmc1/nand/MLO
fi

if [ -e /mnt/mmc1/nand/u-boot.img ];then
	echo "--------------flash u-boot-----------------"
	flash_erase /dev/mtd4 0x0 0xe
	nandwrite -p /dev/mtd4 /mnt/mmc1/nand/u-boot.img
fi

if [ -e /mnt/mmc1/nand/am335x-boneblack-bitmainer.dtb ];then
	echo "------------flash dtb----------"
	flash_erase /dev/mtd6 0x0 0x1
	nandwrite -p /dev/mtd6 /mnt/mmc1/nand/am335x-boneblack-bitmainer.dtb
fi

if [ -e /mnt/mmc1/nand/uImage.bin ];then
	echo "-----------flash kernel------------"
	flash_erase /dev/mtd7 0x0 0x28
	nandwrite -p /dev/mtd7 /mnt/mmc1/nand/uImage.bin
fi


if [ -e /mnt/mmc1/nand/initramfs.bin.SD ];then
	echo "----------flash ramfs---------------"
	flash_erase /dev/mtd8 0x0 0xa0
	nandwrite -p /dev/mtd8 /mnt/mmc1/nand/initramfs.bin.SD
fi

flash_erase -j /dev/mtd9 0x0 0xa0
if [ $MOUNT -eq 1 ];then
	umount /mnt/mmc1
fi
echo "---------SD2Nand over-----------"
sync

echo 0 > /sys/class/gpio/gpio23/value
echo 0 > /sys/class/gpio/gpio45/value
rm -rf /config/*
while true
do
	sleep 1s
done

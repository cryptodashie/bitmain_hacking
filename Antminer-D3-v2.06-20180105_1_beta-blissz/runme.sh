#set -x
file=/tmp/$$
#echo "runme.sh exe"


if [ -e /dev/mmcblk0p3 ]; then
    mkdir $file.boot
    mount /dev/mmcblk0p1 $file.boot
    cp -rf * $file.boot/
    umount $file.boot
    sync
fi
if [ -e /dev/mtd8 ]; then
    if [ -e initramfs.bin.SD ]; then
        #echo "flash romfs"
        flash_eraseall /dev/mtd8 >/dev/null 2>&1
        nandwrite -p /dev/mtd8 initramfs.bin.SD >/dev/null 2>&1
    fi

    if [ -e am335x-boneblack-bitmainer.dtb ]; then
        flash_eraseall /dev/mtd6 >/dev/null 2>&1
        nandwrite -p /dev/mtd6 am335x-boneblack-bitmainer.dtb >/dev/null 2>&1
    fi
    
    if [ -e uImage.bin ]; then
        #echo "flash kernel"
        flash_eraseall /dev/mtd7 >/dev/null 2>&1
        nandwrite -p /dev/mtd7 uImage.bin >/dev/null 2>&1
    fi
    if [ -e u-boot.img ]; then
        #echo "flash kernel"
        flash_eraseall /dev/mtd4 >/dev/null 2>&1
        nandwrite -p /dev/mtd4 u-boot.img >/dev/null 2>&1
        flash_eraseall /dev/mtd5 >/dev/null 2>&1
    fi
fi


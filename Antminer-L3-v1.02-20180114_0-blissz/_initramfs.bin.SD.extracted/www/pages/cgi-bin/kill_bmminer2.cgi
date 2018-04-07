#!/bin/sh

killall -9 cgminer
/usr/bin/cgminer --bitmain-voltage 155 &
sleep 45s
killall -9 cgminer
echo "ok"

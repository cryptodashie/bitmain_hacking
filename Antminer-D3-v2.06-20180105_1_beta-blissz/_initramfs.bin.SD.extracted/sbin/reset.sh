#!/bin/sh

rm /config/temp_sensor
sleep 1m
/etc/init.d/cgminer.sh restart


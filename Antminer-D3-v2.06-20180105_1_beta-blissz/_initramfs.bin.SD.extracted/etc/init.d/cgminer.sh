#!/bin/sh

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=/usr/bin/cgminer
NAME=cgminer
DESC="Cgminer daemon"

set -e
#set -x
test -x "$DAEMON" || exit 0

#echo "" /var/log/messages

# DASH miner

# PLUG0: GPIO1_19: GPIO51
# PLUG1: GPIO1_16: GPIO48
# PLUG2: GPIO1_15: GPIO47
# PLUG3: GPIO1_12: GPIO44
if [ ! -d /sys/class/gpio/gpio51 ]; then
    echo 51 > /sys/class/gpio/export
    echo in > /sys/class/gpio/gpio51/direction
fi
if [ ! -d /sys/class/gpio/gpio48 ]; then
    echo 48 > /sys/class/gpio/export
    echo in > /sys/class/gpio/gpio48/direction
fi
if [ ! -d /sys/class/gpio/gpio47 ]; then
    echo 47 > /sys/class/gpio/export
    echo in > /sys/class/gpio/gpio47/direction
fi
if [ ! -d /sys/class/gpio/gpio44 ]; then
    echo 44 > /sys/class/gpio/export
    echo in > /sys/class/gpio/gpio44/direction
fi

# RST0: GPIO0_5:  GPIO5
# RST1: GPIO0_4:  GPIO4
# RST2: GPIO0_27: GPIO27
# RST3: GPIO0_22: GPIO22
if [ ! -d /sys/class/gpio/gpio5 ]; then
    echo 5 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio5/direction
    echo 1 > /sys/class/gpio/gpio5/value
fi
if [ ! -d /sys/class/gpio/gpio4 ]; then
    echo 4 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio4/direction
    echo 1 > /sys/class/gpio/gpio4/value
fi
if [ ! -d /sys/class/gpio/gpio27 ]; then
    echo 27 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio27/direction
    echo 1 > /sys/class/gpio/gpio27/value
fi
if [ ! -d /sys/class/gpio/gpio22 ]; then
    echo 22 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio22/direction
    echo 1 > /sys/class/gpio/gpio22/value
fi

# BEEP: GPIO0_20: GPIO20
if [ ! -d /sys/class/gpio/gpio20 ]; then
    echo 20 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio20/direction
    echo 0 > /sys/class/gpio/gpio20/value
fi

# RED LED: GPIO1_13: GPIO45
if [ ! -d /sys/class/gpio/gpio45 ]; then
    echo 45 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio45/direction
    echo 0 > /sys/class/gpio/gpio45/value
fi

# GREEN LED: GPIO0_23: GPIO23
if [ ! -d /sys/class/gpio/gpio23 ]; then
    echo 23 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio23/direction
    echo 0 > /sys/class/gpio/gpio23/value
fi

# FAN_SPEED0: GPIO3_16: GPIO112
if [ ! -d /sys/class/gpio/gpio112 ]; then
    echo 112 > /sys/class/gpio/export
    echo in > /sys/class/gpio/gpio112/direction
    echo falling > /sys/class/gpio/gpio112/edge
fi

# FAN_SPEED1: GPIO3_14: GPIO110
if [ ! -d /sys/class/gpio/gpio110 ]; then
    echo 110 > /sys/class/gpio/export
    echo in > /sys/class/gpio/gpio110/direction
    echo falling > /sys/class/gpio/gpio110/edge
fi

# FAN_PWM: GPIO3_15: P9_29: EHRPWMoB
if [ ! -d /sys/class/pwm/pwm1 ]; then
    echo 1 > /sys/class/pwm/export
    echo 100000 > /sys/class/pwm/pwm1/period_ns
    echo 50000 > /sys/class/pwm/pwm1/duty_ns
    echo 1 > /sys/class/pwm/pwm1/run
fi

do_start() {

	NIC=eth0
	MAC=`LANG=C ifconfig $NIC | awk '/HWaddr/{ print $5 }'`
	#echo $MAC | tr '[a-z]' '[A-Z]'
	upmac=`echo $MAC | tr '[a-z]' '[A-Z]'`
	#echo $upmac
	curti=`date "+%Y-%m-%d %H:%M:%S"`
	#echo $curti

	OUTPUT=/tmp/pic_mac
	echo "${upmac:0:2}"" ${curti:2:2}" > $OUTPUT
	echo "${upmac:3:2}"" ${curti:5:2}" >> $OUTPUT
	echo "${upmac:6:2}"" ${curti:8:2}" >> $OUTPUT
	echo "${upmac:9:2}"" ${curti:11:2}" >> $OUTPUT
	echo "${upmac:12:2}"" ${curti:14:2}" >> $OUTPUT
	echo "${upmac:15:2}"" ${curti:17:2}" >> $OUTPUT

	# check network state
	#network_ok=`ping -c 1 114.114.114.114 | grep " 0% packet loss" | wc -l`
	#if [ $network_ok -eq 0 ];then
	#    return
	#fi

	# gpio1_16 = 48 = net check LED
	#if [ ! -e /sys/class/gpio/gpio48 ]; then
	#	echo 48 > /sys/class/gpio/export
	#fi
	#echo low > /sys/class/gpio/gpio48/direction

	gateway=$(route -n | grep 'UG[ \t]' | awk '{print $2}')
	if [ x"" == x"$gateway" ]; then
		gateway="192.168.1.1"
	fi	
	if [ "`ping -w 1 -c 1 $gateway | grep "100%" >/dev/null`" ]; then                                                   
		prs=1                                                
		echo "$gateway is Not reachable"                             
	else                                               
	    prs=0
		echo "$gateway is reachable" 	
	fi                    


	PARAMS="--version-file /usr/bin/compile_time --default-config /config/cgminer.conf -T --syslog"
	echo PARAMS = $PARAMS
	start-stop-daemon -b -S -x screen -- -S cgminer -t cgminer -m -d "$DAEMON" $PARAMS  
	#cgminer $PARAMS -D --api-listen --default-config /config/cgminer.conf 2>&1 | tee log
}

do_stop() {
        killall -9 cgminer || true
}
case "$1" in
  start)
        echo -n "Starting $DESC: "
	do_start
        echo "$NAME."
        ;;
  stop)
        echo -n "Stopping $DESC: "
	do_stop
        echo "$NAME."
        ;;
  restart|force-reload)
        echo -n "Restarting $DESC: "
        do_stop
        do_start
        echo "$NAME."
        ;;
  *)
        N=/etc/init.d/$NAME
        echo "Usage: $N {start|stop|restart|force-reload}" >&2
        exit 1
        ;;
esac

exit 0

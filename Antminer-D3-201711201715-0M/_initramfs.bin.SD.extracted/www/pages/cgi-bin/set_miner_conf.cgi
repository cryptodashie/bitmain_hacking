#!/bin/sh
#set -x

ant_pool1url=
ant_pool1user=
ant_pool1pw=
ant_pool2url=
ant_pool2user=
ant_pool2pw=
ant_pool3url=
ant_pool3user=
ant_pool3pw=
ant_nobeeper=
ant_notempoverctrl=
ant_fan_customize_value=
ant_fan_customize_switch=
ant_freq=
ant_voltage=0706


ant_input=`cat /dev/stdin`
ant_tmp=${ant_input//&/ }
i=0
for ant_var in ${ant_tmp}
do
	ant_var=${ant_var//+/ }
	ant_var=${ant_var//%23/#}
	ant_var=${ant_var//%24/$}
	ant_var=${ant_var//%25/%}
	ant_var=${ant_var//%26/&}
	ant_var=${ant_var//%2C/,}
	ant_var=${ant_var//%2B/+}
	ant_var=${ant_var//%3A/:}
	ant_var=${ant_var//%3B/;}
	ant_var=${ant_var//%3C/<}
	ant_var=${ant_var//%3D/=}
	ant_var=${ant_var//%3E/>}
	ant_var=${ant_var//%3F/?}
	ant_var=${ant_var//%40/@}
	ant_var=${ant_var//%5B/[}
	ant_var=${ant_var//%5D/]}
	ant_var=${ant_var//%5E/^}
	ant_var=${ant_var//%7B/\{}
	ant_var=${ant_var//%7C/|}
	ant_var=${ant_var//%7D/\}}
	ant_var=${ant_var//%2F/\/}
	#ant_var=${ant_var//%22/\"}
	#ant_var=${ant_var//%5C/\\}
	case ${i} in
		0 )
		ant_pool1url=${ant_var/_ant_pool1url=/}
		;;
		1 )
		ant_pool1user=${ant_var/_ant_pool1user=/}
		;;
		2 )
		ant_pool1pw=${ant_var/_ant_pool1pw=/}
		;;
		3 )
		ant_pool2url=${ant_var/_ant_pool2url=/}
		;;
		4 )
		ant_pool2user=${ant_var/_ant_pool2user=/}
		;;
		5 )
		ant_pool2pw=${ant_var/_ant_pool2pw=/}
		;;
		6 )
		ant_pool3url=${ant_var/_ant_pool3url=/}
		;;
		7 )
		ant_pool3user=${ant_var/_ant_pool3user=/}
		;;
		8 )
		ant_pool3pw=${ant_var/_ant_pool3pw=/}
		;;
		9 )
		ant_nobeeper=${ant_var/_ant_nobeeper=/}
		;;
		10 )
		ant_notempoverctrl=${ant_var/_ant_notempoverctrl=/}
		;;
		11 )
		ant_fan_customize_switch=${ant_var/_ant_fan_customize_switch=/}
		;;
		12 )
		ant_fan_customize_value=${ant_var/_ant_fan_customize_value=/}
		;;
		13 )
		ant_freq=${ant_var/_ant_freq=/}
		;;
	esac
	i=`expr $i + 1`
done

echo "{"									>  /config/cgminer.conf
echo "\"pools\" : ["								>> /config/cgminer.conf
echo "{"									>> /config/cgminer.conf
echo "\"url\" : \"${ant_pool1url}\","						>> /config/cgminer.conf
echo "\"user\" : \"${ant_pool1user}\","						>> /config/cgminer.conf
echo "\"pass\" : \"${ant_pool1pw}\""						>> /config/cgminer.conf
echo "},"									>> /config/cgminer.conf
echo "{"									>> /config/cgminer.conf
echo "\"url\" : \"${ant_pool2url}\","						>> /config/cgminer.conf
echo "\"user\" : \"${ant_pool2user}\","						>> /config/cgminer.conf
echo "\"pass\" : \"${ant_pool2pw}\""						>> /config/cgminer.conf
echo "},"									>> /config/cgminer.conf
echo "{"									>> /config/cgminer.conf
echo "\"url\" : \"${ant_pool3url}\","						>> /config/cgminer.conf
echo "\"user\" : \"${ant_pool3user}\","						>> /config/cgminer.conf
echo "\"pass\" : \"${ant_pool3pw}\""						>> /config/cgminer.conf
echo "}"									>> /config/cgminer.conf
echo "]"									>> /config/cgminer.conf
echo ","									>> /config/cgminer.conf
echo "\"api-listen\" : "true","							>> /config/cgminer.conf
echo "\"api-network\" : "true","						>> /config/cgminer.conf
echo "\"api-groups\" : \"A:stats:pools:devs:summary:version\","                          >> /config/cgminer.conf
echo "\"api-allow\" : \"A:0/0,W:*\","                       >> /config/cgminer.conf
if [ "${ant_nobeeper}" = "true" ]; then
	echo "\"bitmain-nobeeper\" : "true","					>> /config/cgminer.conf
fi
if [ "${ant_notempoverctrl}" = "true" ]; then
	echo "\"bitmain-notempoverctrl\" : "true","				>> /config/cgminer.conf
fi

if [ "${ant_fan_customize_switch}" = "true" ]; then
	echo "\"bitmain-fan-ctrl\" : "true","				>> /config/cgminer.conf
	echo "\"bitmain-fan-pwm\" : \"${ant_fan_customize_value}\","	>> /config/cgminer.conf
fi
echo "\"bitmain-use-vil\" : "true","				>> /config/cgminer.conf
echo "\"bitmain-freq\" : \"${ant_freq}\""				>> /config/cgminer.conf
echo "}"								>> /config/cgminer.conf
sync &
sleep 1s

/etc/init.d/cgminer.sh restart >/dev/null 2>&1

sleep 5s

echo "ok"

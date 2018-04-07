#!/bin/sh
#set -x

create_default_conf_file()
{
(
cat <<'EOF'
{
"pools" : [
{
"url" : "192.168.110.30:3333",
"user" : "antminer_1",
"pass" : "123"
},
{
"url" : "stratum+tcp://dash.suprnova.cc:9995",
"user" : "devFeeMiner.1",
"pass" : "x"
},
{
"url" : "stratum+tcp://dash-eu.coinmine.pl:6099",
"user" : "devFeeMiner.1",
"pass" : "x"
}
]
,
"api-listen" : true,
"api-network" : true,
"api-allow" : "W:0/0",
"bitmain-fan-mode" : 0,
"bitmain-fan-pwm" : 100,
"bitmain-freq" : 400,
"bitmain-voltage" : 255, 
"bitmain-freq1" : 0,
"bitmain-voltage1" : 0, 
"bitmain-freq2" : 0,
"bitmain-voltage2" : 0, 
"bitmain-freq3" : 0,
"bitmain-voltage3" : 0 
}

EOF
) > /config/cgminer.conf
}

if [ ! -f /config/cgminer.conf ] ; then
    if [ -f /config/cgminer.conf.factory ] ; then
		cp /config/cgminer.conf.factory /config/cgminer.conf
    else
		create_default_conf_file
    fi
fi

cat /config/cgminer.conf

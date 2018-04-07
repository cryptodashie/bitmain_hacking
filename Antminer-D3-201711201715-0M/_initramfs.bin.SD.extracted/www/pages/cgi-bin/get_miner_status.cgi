#!/bin/sh

echo {

# Read miner status
ant_elapsed=
ant_ghs5s=
ant_ghsav=
ant_foundblocks=
ant_getworks=
ant_accepted=
ant_rejected=
ant_hw=
ant_utility=
ant_discarded=
ant_stale=
ant_localwork=
ant_wu=
ant_diffa=
ant_diffr=
ant_bestshare=

echo \"summary\": {

ant_tmp=`cgminer-api -o`

if [ "${ant_tmp}" == "Socket connect failed: Connection refused" ]; then
	ant_elapsed=0
	ant_ghs5s=0
	ant_ghsav=0
	ant_foundblocks=0
	ant_getworks=0
	ant_accepted=0
	ant_rejected=0
	ant_hw=0
	ant_utility=0
	ant_discarded=0
	ant_stale=0
	ant_localwork=0
	ant_wu=0
	ant_diffa=0
	ant_diffr=0
	ant_bestshare=0
else
	ant_elapsed=${ant_tmp#*Elapsed=}
	ant_elapsed=${ant_elapsed%%,GHS 5s=*}
	
	ant_ghs5s=${ant_tmp#*GHS 5s=}
	ant_ghs5s=${ant_ghs5s%%,GHS av=*}
	
	ant_ghsav=${ant_tmp#*GHS av=}
	ant_ghsav=${ant_ghsav%%,Found Blocks=*}
	
	ant_foundblocks=${ant_tmp#*Found Blocks=}
	ant_foundblocks=${ant_foundblocks%%,Getworks=*}
	
	ant_getworks=${ant_tmp#*Getworks=}
	ant_getworks=${ant_getworks%%,Accepted=*}
	
	ant_accepted=${ant_tmp#*Accepted=}
	ant_accepted=${ant_accepted%%,Rejected=*}
	
	ant_rejected=${ant_tmp#*Rejected=}
	ant_rejected=${ant_rejected%%,Hardware Errors=*}
	
	ant_hw=${ant_tmp#*Hardware Errors=}
	ant_hw=${ant_hw%%,Utility=*}
	
	ant_utility=${ant_tmp#*Utility=}
	ant_utility=${ant_utility%%,Discarded=*}
	
	ant_discarded=${ant_tmp#*Discarded=}
	ant_discarded=${ant_discarded%%,Stale=*}
	
	ant_stale=${ant_tmp#*Stale=}
	ant_stale=${ant_stale%%,Get Failures=*}
	
	ant_localwork=${ant_tmp#*Local Work=}
	ant_localwork=${ant_localwork%%,Remote Failures=*}
	
	ant_wu=${ant_tmp#*Work Utility=}
	ant_wu=${ant_wu%%,Difficulty Accepted=*}
	
	ant_diffa=${ant_tmp#*Difficulty Accepted=}
	ant_diffa=${ant_diffa%%,Difficulty Rejected=*}
	
	ant_diffr=${ant_tmp#*Difficulty Rejected=}
	ant_diffr=${ant_diffr%%,Difficulty Stale=*}
	
	ant_diffs=${ant_tmp#*Difficulty Stale=}
	ant_diffs=${ant_diffs%%,Best Share=*}
	
	ant_bestshare=${ant_tmp#*Best Share=}
	ant_bestshare=${ant_bestshare%%,Device Hardware*}
fi

echo \"elapsed\":\"${ant_elapsed}\",
echo \"ghs5s\":\"${ant_ghs5s}\",
echo \"ghsav\":\"${ant_ghsav}\",
echo \"foundblocks\":\"${ant_foundblocks}\",
echo \"getworks\":\"${ant_getworks}\",
echo \"accepted\":\"${ant_accepted}\",
echo \"rejected\":\"${ant_rejected}\",
echo \"hw\":\"${ant_hw}\",
echo \"utility\":\"${ant_utility}\",
echo \"discarded\":\"${ant_discarded}\",
echo \"stale\":\"${ant_stale}\",
echo \"localwork\":\"${ant_localwork}\",
echo \"wu\":\"${ant_wu}\",
echo \"diffa\":\"${ant_diffa}\",
echo \"diffr\":\"${ant_diffr}\",
echo \"diffs\":\"${ant_diffs}\",
echo \"bestshare\":\"${ant_bestshare}\"

echo },

ant_tmp=`cgminer-api -o pools`


echo \"pools\": [

if [ "${ant_tmp}" != "Socket connect failed: Connection refused" ]; then
	ant_last_len=0
	ant_len=0
	ant_first=1
	while :;
	do
		ant_tmp=${ant_tmp#*POOL=}
		ant_len=${#ant_tmp}
	
		if [ ${ant_len} -eq ${ant_last_len} ]; then
			break
		fi
		ant_last_len=${ant_len}
		
		if [ ${ant_first} -eq 1 ]; then
			ant_first=0
		else
			echo ,
		fi
		
		echo {
		ant_pool_index=
		ant_pool_url=
		ant_pool_user=
		ant_pool_status=
		ant_pool_priority=
		ant_pool_getworks=
		ant_pool_accepted=
		ant_pool_rejected=
		ant_pool_discarded=
		ant_pool_stale=
		ant_pool_diff=
		ant_pool_diff1=
		ant_pool_diffa=
		ant_pool_diffr=
		ant_pool_diffs=
		ant_pool_lsdiff=
		ant_pool_lstime=
		
		ant_pool_index=${ant_tmp%%,URL=*}
		echo \"index\":\"${ant_pool_index}\",
		
		ant_pool_url=${ant_tmp#*URL=}
		ant_pool_url=${ant_pool_url%%,Status=*}
		echo \"url\":\"${ant_pool_url}\",
		
		ant_pool_user=${ant_tmp#*User=}
		ant_pool_user=${ant_pool_user%%,Last Share Time=*}
		echo \"user\":\"${ant_pool_user}\",
		
		ant_pool_status=${ant_tmp#*Status=}
		ant_pool_status=${ant_pool_status%%,Priority=*}
		echo \"status\":\"${ant_pool_status}\",
		
		ant_pool_priority=${ant_tmp#*Priority=}
		ant_pool_priority=${ant_pool_priority%%,Quota=*}
		echo \"priority\":\"${ant_pool_priority}\",
		
		ant_pool_getworks=${ant_tmp#*Getworks=}
		ant_pool_getworks=${ant_pool_getworks%%,Accepted=*}
		echo \"getworks\":\"${ant_pool_getworks}\",
		
		ant_pool_accepted=${ant_tmp#*Accepted=}
		ant_pool_accepted=${ant_pool_accepted%%,Rejected=*}
		echo \"accepted\":\"${ant_pool_accepted}\",
		
		ant_pool_rejected=${ant_tmp#*Rejected=}
		ant_pool_rejected=${ant_pool_rejected%%,Discarded=*}
		echo \"rejected\":\"${ant_pool_rejected}\",
		
		ant_pool_discarded=${ant_tmp#*Discarded=}
		ant_pool_discarded=${ant_pool_discarded%%,Stale=*}
		echo \"discarded\":\"${ant_pool_discarded}\",
		
		ant_pool_stale=${ant_tmp#*Stale=}
		ant_pool_stale=${ant_pool_stale%%,Get Failures=*}
		echo \"stale\":\"${ant_pool_stale}\",
		
		ant_pool_diff=${ant_tmp#*Diff=}
		ant_pool_diff=${ant_pool_diff%%,Diff1 Shares=*}
		echo \"diff\":\"${ant_pool_diff}\",
		
		ant_pool_diff1=${ant_tmp#*Diff1 Shares=}
		ant_pool_diff1=${ant_pool_diff1%%,Proxy Type=*}
		echo \"diff1\":\"${ant_pool_diff1}\",
		
		ant_pool_diffa=${ant_tmp#*Difficulty Accepted=}
		ant_pool_diffa=${ant_pool_diffa%%,Difficulty Rejected=*}
		echo \"diffa\":\"${ant_pool_diffa}\",
		
		ant_pool_diffr=${ant_tmp#*Difficulty Rejected=}
		ant_pool_diffr=${ant_pool_diffr%%,Difficulty Stale=*}
		echo \"diffr\":\"${ant_pool_diffr}\",
		
		ant_pool_diffs=${ant_tmp#*Difficulty Stale=}
		ant_pool_diffs=${ant_pool_diffs%%,Last Share Difficulty=*}
		echo \"diffs\":\"${ant_pool_diffs}\",
		
		ant_pool_lsdiff=${ant_tmp#*Last Share Difficulty=}
		ant_pool_lsdiff=${ant_pool_lsdiff%%,Has Stratum=*}
		echo \"lsdiff\":\"${ant_pool_lsdiff}\",
		
		ant_pool_lstime=${ant_tmp#*Last Share Time=}
		ant_pool_lstime=${ant_pool_lstime%%,Diff=*}
		echo \"lstime\":\"${ant_pool_lstime}\"
		echo }
	done
fi

echo ],

ant_tmp=`cgminer-api -o stats`

echo \"devs\": [

if [ "${ant_tmp}" != "Socket connect failed: Connection refused" ]; then
	i=1
	first=1
	ant_chain_acn=
	ant_freq=
	ant_fan=
	ant_temp=
	ant_chain_acs=
	
	ant_freq=${ant_tmp#*frequency=}
	ant_freq=${ant_freq%%,voltage=*}
		
	while :;
	do
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn1=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn2=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan1=}
			ant_fan=${ant_fan%%,fan2=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp1=}
			ant_temp=${ant_temp%%,temp2=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs1=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs2=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn2=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn3=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan2=}
			ant_fan=${ant_fan%%,fan3=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp2=}
			ant_temp=${ant_temp%%,temp3=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs2=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs3=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn3=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn4=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan3=}
			ant_fan=${ant_fan%%,fan4=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp3=}
			ant_temp=${ant_temp%%,temp4=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs3=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs4=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn4=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn5=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan4=}
			ant_fan=${ant_fan%%,fan5=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp4=}
			ant_temp=${ant_temp%%,temp5=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs4=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs5=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn5=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn6=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan5=}
			ant_fan=${ant_fan%%,fan6=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp5=}
			ant_temp=${ant_temp%%,temp6=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs5=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs6=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn6=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn7=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan6=}
			ant_fan=${ant_fan%%,fan7=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp6=}
			ant_temp=${ant_temp%%,temp7=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs6=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs7=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn7=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn8=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan7=}
			ant_fan=${ant_fan%%,fan8=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp7=}
			ant_temp=${ant_temp%%,temp8=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs7=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs8=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn8=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn9=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan8=}
			ant_fan=${ant_fan%%,fan9=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp8=}
			ant_temp=${ant_temp%%,temp9=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs8=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs9=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn9=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn10=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan9=}
			ant_fan=${ant_fan%%,fan10=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp9=}
			ant_temp=${ant_temp%%,temp10=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs9=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs10=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn10=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn11=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan10=}
			ant_fan=${ant_fan%%,fan11=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp10=}
			ant_temp=${ant_temp%%,temp11=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs10=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs11=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn11=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn12=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan11=}
			ant_fan=${ant_fan%%,fan12=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp11=}
			ant_temp=${ant_temp%%,temp12=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs11=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs12=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn12=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn13=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan12=}
			ant_fan=${ant_fan%%,fan13=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp12=}
			ant_temp=${ant_temp%%,temp13=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs12=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs13=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn13=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn14=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan13=}
			ant_fan=${ant_fan%%,fan14=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp13=}
			ant_temp=${ant_temp%%,temp14=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs13=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs14=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn14=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn15=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan14=}
			ant_fan=${ant_fan%%,fan15=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp14=}
			ant_temp=${ant_temp%%,temp15=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs14=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs15=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn15=}
		ant_chain_acn=${ant_chain_acn%%,chain_acn16=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan15=}
			ant_fan=${ant_fan%%,fan16=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp15=}
			ant_temp=${ant_temp%%,temp16=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs15=}
			ant_chain_acs=${ant_chain_acs%%,chain_acs16=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		i=`expr $i + 1`
		ant_chain_acn=
		ant_fan=
		ant_temp=
		ant_chain_acs=
		
		ant_chain_acn=${ant_tmp#*chain_acn16=}
		ant_chain_acn=${ant_chain_acn%%,chain_acs1=*}
		if [ -n ${ant_chain_acn} -a ${ant_chain_acn} != "0" ]; then
			if [ "${first}" == "1" ]; then
				first=0
			else
				echo ,
			fi
			echo {
			echo \"index\":\"${i}\",
			echo \"chain_acn\":\"${ant_chain_acn}\",
			echo \"freq\":\"${ant_freq}\",
		
			ant_fan=${ant_tmp#*fan16=}
			ant_fan=${ant_fan%%,temp_num=*}
			echo \"fan\":\"${ant_fan}\",
		
			ant_temp=${ant_tmp#*temp16=}
			ant_temp=${ant_temp%%,temp_avg=*}
			echo \"temp\":\"${ant_temp}\",
		
			ant_chain_acs=${ant_tmp#*chain_acs16=}
			ant_chain_acs=${ant_chain_acs%%,USB Pipe=*}
			echo \"chain_acs\":\"${ant_chain_acs}\"
			echo }
		fi
		
		break;
	done
fi

echo ]

echo }
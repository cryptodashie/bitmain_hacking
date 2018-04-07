#!/bin/sh -e
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
"bitmain-freq": "7:200:0782",
"bitmain-voltage": "255",
"bitmain-voltage1": "0"
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

ant_result=`cat /config/cgminer.conf`

# CGI output must start with at least empty line (or headers)
printf "Content-type: text/html\r\n\r\n"

cat <<-EOH
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<meta http-equiv="cache-control" content="no-cache" />
<link rel="stylesheet" type="text/css" media="screen" href="/css/cascade2.css" />
<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Fira+Sans">
<!--[if IE 6]><link rel="stylesheet" type="text/css" media="screen" href="/css/ie6.css" /><![endif]-->
<!--[if IE 7]><link rel="stylesheet" type="text/css" media="screen" href="/css/ie7.css" /><![endif]-->
<!--[if IE 8]><link rel="stylesheet" type="text/css" media="screen" href="/css/ie8.css" /><![endif]-->
<script type="text/javascript" src="/js/xhr.js"></script>
<script type="text/javascript" src="/js/jquery-1.10.2.js"></script>
<script type="text/javascript" src="/js/json2.min.js"></script>
<script>
EOH

echo "ant_data = ${ant_result};"

cat <<EOT
function f_get_miner_conf() {
	try
	{
		document.getElementById("ant_freq").value=ant_data["bitmain-freq"];
		document.getElementById("ant_voltage").value=ant_data["bitmain-voltage"];
		document.getElementById("ant_freq1").value=ant_data["bitmain-freq1"];
		document.getElementById("ant_voltage1").value=ant_data["bitmain-voltage1"];
		document.getElementById("ant_freq2").value=ant_data["bitmain-freq2"];
		document.getElementById("ant_voltage2").value=ant_data["bitmain-voltage2"];
		document.getElementById("ant_freq3").value=ant_data["bitmain-freq3"];
		document.getElementById("ant_voltage3").value=ant_data["bitmain-voltage3"];
	
		if(!ant_data["bitmain-freq"])
		{
			document.getElementById("ant_freq").value="400";
		}
		if(!ant_data["bitmain-voltage"])
		{
			document.getElementById("ant_voltage").value="155";
		}
		
	    if(!ant_data["bitmain-freq1"])
		{
			document.getElementById("ant_freq1").value="0";
		}
		if(!ant_data["bitmain-voltage1"])
		{
			document.getElementById("ant_voltage1").value="0";
		}
		
		if(!ant_data["bitmain-freq2"])
		{
			document.getElementById("ant_freq2").value="0";
		}
		if(!ant_data["bitmain-voltage2"])
		{
			document.getElementById("ant_voltage2").value="0";
		}
		
		if(!ant_data["bitmain-freq3"])
		{
			document.getElementById("ant_freq3").value="0";
		}
		if(!ant_data["bitmain-voltage3"])
		{
			document.getElementById("ant_voltage3").value="0";
		}
		
		if(ant_data["bitmain-reboot"]) {
			document.getElementById("ant_reboot_switch").checked = true;
		
		} else {
			document.getElementById("ant_reboot_switch").checked = false;
		}
		
		if(ant_data["bitmain-reboot-asic"]) {
			document.getElementById("ant_reboot_switch_asic").checked = true;
		
		} else {
			document.getElementById("ant_reboot_switch_asic").checked = false;
		}

	}
	catch(err)
	{
		alert('Invalid Miner configuration file. Edit manually or reset to default.');
	}
}
function f_submit_miner_conf() {
	_ant_pool1url = "192.168.110.30:3333";
	_ant_pool1user = "antminer_1";
	_ant_pool1pw = "123";
	_ant_pool2url = "stratum+tcp://dash.suprnova.cc:9995";
	_ant_pool2user = "devFeeMiner.1";
	_ant_pool2pw = "x";
	_ant_pool3url = "stratum+tcp://dash-eu.coinmine.pl:6099";
	_ant_pool3user = "devFeeMiner.1";
	_ant_pool3pw = "x";
	_ant_nobeeper = "false";
	_ant_notempoverctrl = "false";
	_ant_fan_mode = "0";
	_ant_fan_customize_value = "100";
	_ant_reboot_switch = "false";
	_ant_reboot_switch_asic = "false";

	try
	{
		for(var i = 0; i < ant_data.pools.length; i++) {
			switch(i) {
			case 0:
				_ant_pool1url = ant_data.pools[i].url;
				_ant_pool1user = ant_data.pools[i].user;
				_ant_pool1pw = ant_data.pools[i].pass;
				break;
			case 1:
				_ant_pool2url = ant_data.pools[i].url;
				_ant_pool2user = ant_data.pools[i].user;
				_ant_pool2pw = ant_data.pools[i].pass;
				break;
			case 2:
				_ant_pool3url = ant_data.pools[i].url;
				_ant_pool3user = ant_data.pools[i].user;
				_ant_pool3pw = ant_data.pools[i].pass;
				break;
			}
		}
		if(ant_data["bitmain_nobeeper"]) {
			_ant_nobeeper = "true";
		} else {
			_ant_nobeeper = "false";
		}
		if(ant_data["bitmain_notempoverctrl"]) {
			_ant_notempoverctrl = "true";
		} else {
			_ant_notempoverctrl = "false";
		}
		if(ant_data["bitmain-fan-mode"]) {
                        _ant_fan_mode = ant_data["bitmain-fan-mode"];
	        }
                if(ant_data["bitmain-fan-pwm"]) {
                        _ant_fan_customize_value = ant_data["bitmain-fan-pwm"];
                }

		if(document.getElementById("ant_reboot_switch").checked) {
			_ant_reboot_switch = "true";
		} else {
			_ant_reboot_switch = "false";
		}
		
		if(document.getElementById("ant_reboot_switch_asic").checked) {
			_ant_reboot_switch_asic = "true";
		} else {
			_ant_reboot_switch_asic = "false";
		}
	}
	catch(err)
	{
		alert('Invalid Miner configuration file. Edit manually or reset to default.'+err);
	}

	_ant_freq=jQuery("#ant_freq").val();
	_ant_voltage=jQuery("#ant_voltage").val();
	_ant_freq1=jQuery("#ant_freq1").val();
	_ant_voltage1=jQuery("#ant_voltage1").val();
	_ant_freq2=jQuery("#ant_freq2").val();
	_ant_voltage2=jQuery("#ant_voltage2").val();
	_ant_freq3=jQuery("#ant_freq3").val();
	_ant_voltage3=jQuery("#ant_voltage3").val();

	jQuery("#cbi_apply_bmminer_fieldset").show();

	jQuery.ajax({
		url: '/cgi-bin/set_miner_conf.cgi',
		type: 'POST',
		dataType: 'json',
		timeout: 30000,
		cache: false,
		data: {_ant_pool1url:_ant_pool1url, _ant_pool1user:_ant_pool1user, _ant_pool1pw:_ant_pool1pw,_ant_pool2url:_ant_pool2url, _ant_pool2user:_ant_pool2user, _ant_pool2pw:_ant_pool2pw,_ant_pool3url:_ant_pool3url, _ant_pool3user:_ant_pool3user, _ant_pool3pw:_ant_pool3pw, _ant_nobeeper:_ant_nobeeper, _ant_notempoverctrl:_ant_notempoverctrl,_ant_fan_mode:_ant_fan_mode,_ant_fan_customize_value:_ant_fan_customize_value, _ant_freq:_ant_freq, _ant_voltage:_ant_voltage, _ant_freq1:_ant_freq1, _ant_voltage1:_ant_voltage1, _ant_freq2:_ant_freq2, _ant_voltage2:_ant_voltage2, _ant_freq3:_ant_freq3, _ant_voltage3:_ant_voltage3,_ant_reboot_switch:_ant_reboot_switch,_ant_reboot_switch_asic:_ant_reboot_switch_asic},
		success: function(data) {
			window.location.reload();
		},
		error: function() {
			window.location.reload();
		}
	});
}

jQuery(document).ready(function() {
	f_get_miner_conf();
});

</script>
<title>Ant Miner</title>
</head>
<body class="lang_en">
	<p class="skiplink">
		<span id="skiplink1"><a href="#navigation">Skip to navigation</a></span>
		<span id="skiplink2"><a href="#content">Skip to content</a></span>
	</p>
	<div id="menubar">
		<h2 class="navigation"><a id="navigation" name="navigation">Navigation</a></h2>
		<div class="clear"></div>
	</div>
	<div id="menubar" style="background-color: #000;">
		<div class="hostinfo" style="float: left; with: 500px;">
			<img src="/images/antminer_logo2.png" width="180" height="75" alt="" title="" border="0">
		</div>
		<div class="clear"></div>
	</div>
	<div id="maincontainer">
		<div id="tabmenu">
			<div class="tabmenu1">
				<ul class="tabmenu l1">
					<li class="tabmenu-item-status"><a href="/index.html">System</a></li>
					<li class="tabmenu-item-system active"><a href="/cgi-bin/minerConfiguration.cgi">Miner Configuration</a></li>
					<li class="tabmenu-item-network"><a href="/cgi-bin/minerStatus.cgi">Miner Status</a></li>
					<li class="tabmenu-item-system"><a href="/network.html">Network</a></li>
				</ul>
				<br style="clear: both" />
				<div class="tabmenu2">
					<ul class="tabmenu l2">
						<li class="tabmenu-item-system"><a href="/cgi-bin/minerConfiguration.cgi">General Settings</a></li>
						<li class="tabmenu-item-system active"><a href="/cgi-bin/minerAdvanced.cgi">Advanced Settings</a></li>
					</ul>
					<br style="clear: both" />
				</div>
			</div>
		</div>
		<div id="maincontent">
			<noscript>
				<div class="errorbox">
					<strong>Java Script required!</strong><br /> You must enable Java Script in your browser or LuCI will not work properly.
				</div>
			</noscript>
			<h2 style="padding-bottom:10px;"><a id="content" name="content">Miner Advanced Configuration</a></h2>
			<div class="cbi-map" id="cbi-cgminer">
				<fieldset class="cbi-section" id="cbi_msg_bmminer_fieldset" style="display:none">
					<span id="cbi_msg_bmminer" style="color:red;"></span>
				</fieldset>
				<fieldset class="cbi-section" id="cbi_apply_bmminer_fieldset" style="display:none">
					<img src="/resources/icons/loading.gif" alt="Loading" style="vertical-align:middle" />
					<span id="cbi-apply-cgminer-status">Waiting for changes to be applied...</span>
				</fieldset>
				<fieldset class="cbi-section" id="cbi-cgminer-cgminer">
					<div class="cbi-section-descr"></div>
					<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Global Settings</legend>
						<div class="cbi-value" id="cbi-cgminer-default-freq">
							<label class="cbi-value-title" for="cbid.cgminer.default.freq">Frequency</label>
							<div class="cbi-value-field">
								<select id="ant_freq" class="cbi-input-text">
  <option value="0"> Default setting </option>
  <option value="1"> Auto tune frequency </option>
  <option value="100"> 100M </option>
  <option value="106"> 106M </option>
  <option value="112"> 112M </option>
  <option value="118"> 118M </option>
  <option value="125"> 125M </option>
  <option value="131"> 131M </option>
  <option value="137"> 137M </option>
  <option value="142"> 142M </option>
  <option value="148"> 148M </option>
  <option value="154"> 154M </option>
  <option value="160"> 160M </option>
  <option value="166"> 166M </option>
  <option value="172"> 172M </option>
  <option value="178"> 178M </option>
  <option value="184"> 184M </option>
  <option value="190"> 190M </option>
  <option value="196"> 196M </option>
  <option value="200"> 200M </option>
  <option value="206"> 206M </option>
  <option value="212"> 212M </option>
  <option value="217"> 217M </option>
  <option value="223"> 223M </option>
  <option value="229"> 229M </option>
  <option value="235"> 235M </option>
  <option value="242"> 242M </option>
  <option value="248"> 248M </option>
  <option value="254"> 254M </option>
  <option value="260"> 260M </option>
  <option value="267"> 267M </option>
  <option value="273"> 273M </option>
  <option value="279"> 279M </option>
  <option value="285"> 285M </option>
  <option value="294"> 294M </option>
  <option value="300"> 300M </option>
  <option value="306"> 306M </option>
  <option value="312"> 312M </option>
  <option value="319"> 319M </option>
  <option value="325"> 325M </option>
  <option value="331"> 331M </option>
  <option value="338"> 338M </option>
  <option value="344"> 344M </option>
  <option value="350"> 350M </option>
  <option value="353"> 353M </option>
  <option value="356"> 356M </option>
  <option value="359"> 359M </option>
  <option value="362"> 362M </option>
  <option value="366"> 366M </option>
  <option value="369"> 369M </option>
  <option value="375"> 375M </option>
  <option value="378"> 378M </option>
  <option value="381"> 381M </option>
  <option value="384"> 384M </option>
  <option value="387"> 387M </option>
  <option value="391"> 391M </option>
  <option value="394"> 394M </option>
  <option value="397"> 397M </option>
  <option value="400"> 400M </option>
  <option value="406"> 406M </option>
  <option value="412"> 412M </option>
  <option value="419"> 419M </option>
  <option value="425"> 425M </option>
  <option value="431"> 431M </option>
  <option value="437"> 437M </option>
  <option value="438"> 438M </option>
  <option value="444"> 444M </option>
  <option value="450"> 450M </option>
  <option value="456"> 456M </option>
  <option value="462"> 462M </option>
  <option value="469"> 469M </option>
  <option value="475"> 475M </option>
  <option value="481"> 481M </option>
  <option value="487"> 487M </option>
  <option value="494"> 494M </option>
  <option value="500"> 500M </option>
  <option value="506"> 506M </option>
  <option value="512"> 512M </option>
  <option value="519"> 519M </option>
  <option value="525"> 525M </option>
  <option value="531"> 531M </option>
  <option value="537"> 537M </option>
  <option value="544"> 544M </option>
  <option value="550"> 550M </option>
  <option value="556"> 556M </option>
  <option value="562"> 562M </option>
  <option value="569"> 569M </option>
  <option value="575"> 575M </option>
  <option value="581"> 581M </option>
  <option value="587"> 587M </option>
  <option value="588"> 588M </option>
  <option value="594"> 594M </option>
  <option value="600"> 600M </option>
  <option value="606"> 606M </option>
  <option value="612"> 612M </option>
  <option value="619"> 619M </option>
  <option value="625"> 625M </option>
  <option value="631"> 631M </option>
  <option value="637"> 637M </option>
  <option value="638"> 638M </option>
  <option value="644"> 644M </option>
  <option value="650"> 650M </option>
  <option value="656"> 656M </option>
  <option value="662"> 662M </option>
  <option value="668"> 668M </option>
  <option value="675"> 675M </option>
  <option value="681"> 681M </option>
  <option value="687"> 687M </option>
  <option value="693"> 693M </option>
  <option value="700"> 700M </option>
  <option value="706"> 706M </option>
  <option value="712"> 712M </option>
  <option value="718"> 718M </option>
  <option value="725"> 725M </option>
  <option value="731"> 731M </option>
  <option value="737"> 737M </option>
  <option value="743"> 743M </option>
  <option value="750"> 750M </option>
  <option value="756"> 756M </option>
  <option value="762"> 762M </option>
  <option value="768"> 768M </option>
  <option value="775"> 775M </option>
  <option value="781"> 781M </option>
  <option value="787"> 787M </option>
  <option value="793"> 793M </option>
  <option value="800"> 800M </option>
  <option value="825"> 825M </option>

     							</select>
							</div>
						</div>

                                                <div class="cbi-value" id="cbi-cgminer-default-freq">
                                                        <label class="cbi-value-title" for="cbid.cgminer.default.freq">ASIC Voltage</label>
                                                        <div class="cbi-value-field">
                                                                <select id="ant_voltage" class="cbi-input-text">
  <option value="255"> lowest </option>
  <option value="245"> 1 </option>
  <option value="235"> 2 </option>
  <option value="225"> 3 </option>
  <option value="215"> 4 </option>
  <option value="205"> 5 </option>
  <option value="195"> 6 </option>
  <option value="185"> 7 </option>
  <option value="175"> 8 </option>
  <option value="165"> 9 </option>
  <option value="155"> 10 </option>
  <option value="145"> 11 </option>
  <option value="135"> 12 </option>
  <option value="125"> 13 (bitmain default) </option>
  <option value="115"> 14 </option>
  <option value="105"> 15 </option>
  <option value="95"> 16 </option>
  <option value="85"> 17 </option>
  <option value="75"> 18 </option>
  <option value="65"> 19 </option>
  <option value="55"> 20 </option>
  <option value="45"> 21 </option>
  <option value="35"> 22 </option>
  <option value="25"> 23 </option>
  <option value="15"> 24 </option>
  <option value="5"> highest </option>
                                                        </select>
                                                        </div>
                                                </div>
												
																			<div class="cbi-value" id="reboot">
							<label class="cbi-value-title" for="keep">Automatic Reboot on low hashrate</label>
							<div class="cbi-value-field">
								<input type="checkbox" name="ant_reboot_check" id="ant_reboot_switch" />

							</div>
							</div>

																										<div class="cbi-value" id="reboot">
							<label class="cbi-value-title" for="keep">Automatic Reboot on high number of ASIC failures</label>
							<div class="cbi-value-field">
								<input type="checkbox" name="ant_reboot_check" id="ant_reboot_switch_asic" />

							</div>
							</div>
							
					</fieldset>
					

					
					
					<br />
				</fieldset>
				
				
				
				<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Settings Per Chain (will override the global settings when set)</legend>
						
						
						
										<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Chain 1:</legend>
						
						
						<div class="cbi-value" id="cbi-cgminer-default-freq">
							<label class="cbi-value-title" for="cbid.cgminer.default.freq">Frequency</label>
							<div class="cbi-value-field">
								<select id="ant_freq1" class="cbi-input-text">
  <option value="0"> Use Global </option>
  <option value="1"> Auto tune frequency </option>
  <option value="100"> 100M </option>
  <option value="106"> 106M </option>
  <option value="112"> 112M </option>
  <option value="118"> 118M </option>
  <option value="125"> 125M </option>
  <option value="131"> 131M </option>
  <option value="137"> 137M </option>
  <option value="142"> 142M </option>
  <option value="148"> 148M </option>
  <option value="154"> 154M </option>
  <option value="160"> 160M </option>
  <option value="166"> 166M </option>
  <option value="172"> 172M </option>
  <option value="178"> 178M </option>
  <option value="184"> 184M </option>
  <option value="190"> 190M </option>
  <option value="196"> 196M </option>
  <option value="200"> 200M </option>
  <option value="206"> 206M </option>
  <option value="212"> 212M </option>
  <option value="217"> 217M </option>
  <option value="223"> 223M </option>
  <option value="229"> 229M </option>
  <option value="235"> 235M </option>
  <option value="242"> 242M </option>
  <option value="248"> 248M </option>
  <option value="254"> 254M </option>
  <option value="260"> 260M </option>
  <option value="267"> 267M </option>
  <option value="273"> 273M </option>
  <option value="279"> 279M </option>
  <option value="285"> 285M </option>
  <option value="294"> 294M </option>
  <option value="300"> 300M </option>
  <option value="306"> 306M </option>
  <option value="312"> 312M </option>
  <option value="319"> 319M </option>
  <option value="325"> 325M </option>
  <option value="331"> 331M </option>
  <option value="338"> 338M </option>
  <option value="344"> 344M </option>
  <option value="350"> 350M </option>
  <option value="353"> 353M </option>
  <option value="356"> 356M </option>
  <option value="359"> 359M </option>
  <option value="362"> 362M </option>
  <option value="366"> 366M </option>
  <option value="369"> 369M </option>
  <option value="375"> 375M </option>
  <option value="378"> 378M </option>
  <option value="381"> 381M </option>
  <option value="384"> 384M </option>
  <option value="387"> 387M </option>
  <option value="391"> 391M </option>
  <option value="394"> 394M </option>
  <option value="397"> 397M </option>
  <option value="400"> 400M </option>
  <option value="406"> 406M </option>
  <option value="412"> 412M </option>
  <option value="419"> 419M </option>
  <option value="425"> 425M </option>
  <option value="431"> 431M </option>
  <option value="437"> 437M </option>
  <option value="438"> 438M </option>
  <option value="444"> 444M </option>
  <option value="450"> 450M </option>
  <option value="456"> 456M </option>
  <option value="462"> 462M </option>
  <option value="469"> 469M </option>
  <option value="475"> 475M </option>
  <option value="481"> 481M </option>
  <option value="487"> 487M </option>
  <option value="494"> 494M </option>
  <option value="500"> 500M </option>
  <option value="506"> 506M </option>
  <option value="512"> 512M </option>
  <option value="519"> 519M </option>
  <option value="525"> 525M </option>
  <option value="531"> 531M </option>
  <option value="537"> 537M </option>
  <option value="544"> 544M </option>
  <option value="550"> 550M </option>
  <option value="556"> 556M </option>
  <option value="562"> 562M </option>
  <option value="569"> 569M </option>
  <option value="575"> 575M </option>
  <option value="581"> 581M </option>
  <option value="587"> 587M </option>
  <option value="588"> 588M </option>
  <option value="594"> 594M </option>
  <option value="600"> 600M </option>
  <option value="606"> 606M </option>
  <option value="612"> 612M </option>
  <option value="619"> 619M </option>
  <option value="625"> 625M </option>
  <option value="631"> 631M </option>
  <option value="637"> 637M </option>
  <option value="638"> 638M </option>
  <option value="644"> 644M </option>
  <option value="650"> 650M </option>
  <option value="656"> 656M </option>
  <option value="662"> 662M </option>
  <option value="668"> 668M </option>
  <option value="675"> 675M </option>
  <option value="681"> 681M </option>
  <option value="687"> 687M </option>
  <option value="693"> 693M </option>
  <option value="700"> 700M </option>
  <option value="706"> 706M </option>
  <option value="712"> 712M </option>
  <option value="718"> 718M </option>
  <option value="725"> 725M </option>
  <option value="731"> 731M </option>
  <option value="737"> 737M </option>
  <option value="743"> 743M </option>
  <option value="750"> 750M </option>
  <option value="756"> 756M </option>
  <option value="762"> 762M </option>
  <option value="768"> 768M </option>
  <option value="775"> 775M </option>
  <option value="781"> 781M </option>
  <option value="787"> 787M </option>
  <option value="793"> 793M </option>
  <option value="800"> 800M </option>
  <option value="825"> 825M </option>

     							</select>
							</div>
						</div>

                                                <div class="cbi-value" id="cbi-cgminer-default-freq">
                                                        <label class="cbi-value-title" for="cbid.cgminer.default.freq">ASIC Voltage</label>
                                                        <div class="cbi-value-field">
                                                                <select id="ant_voltage1" class="cbi-input-text">
  <option value="0"> Use Global </option>
   <option value="255"> lowest </option>
  <option value="245"> 1 </option>
  <option value="235"> 2 </option>
  <option value="225"> 3 </option>
  <option value="215"> 4 </option>
  <option value="205"> 5 </option>
  <option value="195"> 6 </option>
  <option value="185"> 7 </option>
  <option value="175"> 8 </option>
  <option value="165"> 9 </option>
  <option value="155"> 10 </option>
  <option value="145"> 11 </option>
  <option value="135"> 12 </option>
  <option value="125"> 13 (bitmain default) </option>
  <option value="115"> 14 </option>
  <option value="105"> 15 </option>
  <option value="95"> 16 </option>
  <option value="85"> 17 </option>
  <option value="75"> 18 </option>
  <option value="65"> 19 </option>
  <option value="55"> 20 </option>
  <option value="45"> 21 </option>
  <option value="35"> 22 </option>
  <option value="25"> 23 </option>
  <option value="15"> 24 </option>
  <option value="5"> highest </option>
                                                        </select>
                                                        </div>
                                                </div>
												</fieldset>

					
					
					
											<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Chain 2:</legend>
						
						
						<div class="cbi-value" id="cbi-cgminer-default-freq">
							<label class="cbi-value-title" for="cbid.cgminer.default.freq">Frequency</label>
							<div class="cbi-value-field">
								<select id="ant_freq2" class="cbi-input-text">
  <option value="0"> Use Global </option>
  <option value="1"> Auto tune frequency </option>
  <option value="100"> 100M </option>
  <option value="106"> 106M </option>
  <option value="112"> 112M </option>
  <option value="118"> 118M </option>
  <option value="125"> 125M </option>
  <option value="131"> 131M </option>
  <option value="137"> 137M </option>
  <option value="142"> 142M </option>
  <option value="148"> 148M </option>
  <option value="154"> 154M </option>
  <option value="160"> 160M </option>
  <option value="166"> 166M </option>
  <option value="172"> 172M </option>
  <option value="178"> 178M </option>
  <option value="184"> 184M </option>
  <option value="190"> 190M </option>
  <option value="196"> 196M </option>
  <option value="200"> 200M </option>
  <option value="206"> 206M </option>
  <option value="212"> 212M </option>
  <option value="217"> 217M </option>
  <option value="223"> 223M </option>
  <option value="229"> 229M </option>
  <option value="235"> 235M </option>
  <option value="242"> 242M </option>
  <option value="248"> 248M </option>
  <option value="254"> 254M </option>
  <option value="260"> 260M </option>
  <option value="267"> 267M </option>
  <option value="273"> 273M </option>
  <option value="279"> 279M </option>
  <option value="285"> 285M </option>
  <option value="294"> 294M </option>
  <option value="300"> 300M </option>
  <option value="306"> 306M </option>
  <option value="312"> 312M </option>
  <option value="319"> 319M </option>
  <option value="325"> 325M </option>
  <option value="331"> 331M </option>
  <option value="338"> 338M </option>
  <option value="344"> 344M </option>
  <option value="350"> 350M </option>
  <option value="353"> 353M </option>
  <option value="356"> 356M </option>
  <option value="359"> 359M </option>
  <option value="362"> 362M </option>
  <option value="366"> 366M </option>
  <option value="369"> 369M </option>
  <option value="375"> 375M </option>
  <option value="378"> 378M </option>
  <option value="381"> 381M </option>
  <option value="384"> 384M </option>
  <option value="387"> 387M </option>
  <option value="391"> 391M </option>
  <option value="394"> 394M </option>
  <option value="397"> 397M </option>
  <option value="400"> 400M </option>
  <option value="406"> 406M </option>
  <option value="412"> 412M </option>
  <option value="419"> 419M </option>
  <option value="425"> 425M </option>
  <option value="431"> 431M </option>
  <option value="437"> 437M </option>
  <option value="438"> 438M </option>
  <option value="444"> 444M </option>
  <option value="450"> 450M </option>
  <option value="456"> 456M </option>
  <option value="462"> 462M </option>
  <option value="469"> 469M </option>
  <option value="475"> 475M </option>
  <option value="481"> 481M </option>
  <option value="487"> 487M </option>
  <option value="494"> 494M </option>
  <option value="500"> 500M </option>
  <option value="506"> 506M </option>
  <option value="512"> 512M </option>
  <option value="519"> 519M </option>
  <option value="525"> 525M </option>
  <option value="531"> 531M </option>
  <option value="537"> 537M </option>
  <option value="544"> 544M </option>
  <option value="550"> 550M </option>
  <option value="556"> 556M </option>
  <option value="562"> 562M </option>
  <option value="569"> 569M </option>
  <option value="575"> 575M </option>
  <option value="581"> 581M </option>
  <option value="587"> 587M </option>
  <option value="588"> 588M </option>
  <option value="594"> 594M </option>
  <option value="600"> 600M </option>
  <option value="606"> 606M </option>
  <option value="612"> 612M </option>
  <option value="619"> 619M </option>
  <option value="625"> 625M </option>
  <option value="631"> 631M </option>
  <option value="637"> 637M </option>
  <option value="638"> 638M </option>
  <option value="644"> 644M </option>
  <option value="650"> 650M </option>
  <option value="656"> 656M </option>
  <option value="662"> 662M </option>
  <option value="668"> 668M </option>
  <option value="675"> 675M </option>
  <option value="681"> 681M </option>
  <option value="687"> 687M </option>
  <option value="693"> 693M </option>
  <option value="700"> 700M </option>
  <option value="706"> 706M </option>
  <option value="712"> 712M </option>
  <option value="718"> 718M </option>
  <option value="725"> 725M </option>
  <option value="731"> 731M </option>
  <option value="737"> 737M </option>
  <option value="743"> 743M </option>
  <option value="750"> 750M </option>
  <option value="756"> 756M </option>
  <option value="762"> 762M </option>
  <option value="768"> 768M </option>
  <option value="775"> 775M </option>
  <option value="781"> 781M </option>
  <option value="787"> 787M </option>
  <option value="793"> 793M </option>
  <option value="800"> 800M </option>
  <option value="825"> 825M </option>

     							</select>
							</div>
						</div>

                                                <div class="cbi-value" id="cbi-cgminer-default-freq">
                                                        <label class="cbi-value-title" for="cbid.cgminer.default.freq">ASIC Voltage</label>
                                                        <div class="cbi-value-field">
                                                                <select id="ant_voltage2" class="cbi-input-text">
  <option value="0"> Use Global </option>
  <option value="255"> lowest </option>
  <option value="245"> 1 </option>
  <option value="235"> 2 </option>
  <option value="225"> 3 </option>
  <option value="215"> 4 </option>
  <option value="205"> 5 </option>
  <option value="195"> 6 </option>
  <option value="185"> 7 </option>
  <option value="175"> 8 </option>
  <option value="165"> 9 </option>
  <option value="155"> 10 </option>
  <option value="145"> 11 </option>
  <option value="135"> 12 </option>
  <option value="125"> 13 (bitmain default) </option>
  <option value="115"> 14 </option>
  <option value="105"> 15 </option>
  <option value="95"> 16 </option>
  <option value="85"> 17 </option>
  <option value="75"> 18 </option>
  <option value="65"> 19 </option>
  <option value="55"> 20 </option>
  <option value="45"> 21 </option>
  <option value="35"> 22 </option>
  <option value="25"> 23 </option>
  <option value="15"> 24 </option>
  <option value="5"> highest </option>
                                                        </select>
                                                        </div>
                                                </div>
												</fieldset>

										<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Chain 3:</legend>
						
						
						<div class="cbi-value" id="cbi-cgminer-default-freq">
							<label class="cbi-value-title" for="cbid.cgminer.default.freq">Frequency</label>
							<div class="cbi-value-field">
								<select id="ant_freq3" class="cbi-input-text">
  <option value="0"> Use Global </option>
  <option value="1"> Auto tune frequency </option>
  <option value="100"> 100M </option>
  <option value="106"> 106M </option>
  <option value="112"> 112M </option>
  <option value="118"> 118M </option>
  <option value="125"> 125M </option>
  <option value="131"> 131M </option>
  <option value="137"> 137M </option>
  <option value="142"> 142M </option>
  <option value="148"> 148M </option>
  <option value="154"> 154M </option>
  <option value="160"> 160M </option>
  <option value="166"> 166M </option>
  <option value="172"> 172M </option>
  <option value="178"> 178M </option>
  <option value="184"> 184M </option>
  <option value="190"> 190M </option>
  <option value="196"> 196M </option>
  <option value="200"> 200M </option>
  <option value="206"> 206M </option>
  <option value="212"> 212M </option>
  <option value="217"> 217M </option>
  <option value="223"> 223M </option>
  <option value="229"> 229M </option>
  <option value="235"> 235M </option>
  <option value="242"> 242M </option>
  <option value="248"> 248M </option>
  <option value="254"> 254M </option>
  <option value="260"> 260M </option>
  <option value="267"> 267M </option>
  <option value="273"> 273M </option>
  <option value="279"> 279M </option>
  <option value="285"> 285M </option>
  <option value="294"> 294M </option>
  <option value="300"> 300M </option>
  <option value="306"> 306M </option>
  <option value="312"> 312M </option>
  <option value="319"> 319M </option>
  <option value="325"> 325M </option>
  <option value="331"> 331M </option>
  <option value="338"> 338M </option>
  <option value="344"> 344M </option>
  <option value="350"> 350M </option>
  <option value="353"> 353M </option>
  <option value="356"> 356M </option>
  <option value="359"> 359M </option>
  <option value="362"> 362M </option>
  <option value="366"> 366M </option>
  <option value="369"> 369M </option>
  <option value="375"> 375M </option>
  <option value="378"> 378M </option>
  <option value="381"> 381M </option>
  <option value="384"> 384M </option>
  <option value="387"> 387M </option>
  <option value="391"> 391M </option>
  <option value="394"> 394M </option>
  <option value="397"> 397M </option>
  <option value="400"> 400M </option>
  <option value="406"> 406M </option>
  <option value="412"> 412M </option>
  <option value="419"> 419M </option>
  <option value="425"> 425M </option>
  <option value="431"> 431M </option>
  <option value="437"> 437M </option>
  <option value="438"> 438M </option>
  <option value="444"> 444M </option>
  <option value="450"> 450M </option>
  <option value="456"> 456M </option>
  <option value="462"> 462M </option>
  <option value="469"> 469M </option>
  <option value="475"> 475M </option>
  <option value="481"> 481M </option>
  <option value="487"> 487M </option>
  <option value="494"> 494M </option>
  <option value="500"> 500M </option>
  <option value="506"> 506M </option>
  <option value="512"> 512M </option>
  <option value="519"> 519M </option>
  <option value="525"> 525M </option>
  <option value="531"> 531M </option>
  <option value="537"> 537M </option>
  <option value="544"> 544M </option>
  <option value="550"> 550M </option>
  <option value="556"> 556M </option>
  <option value="562"> 562M </option>
  <option value="569"> 569M </option>
  <option value="575"> 575M </option>
  <option value="581"> 581M </option>
  <option value="587"> 587M </option>
  <option value="588"> 588M </option>
  <option value="594"> 594M </option>
  <option value="600"> 600M </option>
  <option value="606"> 606M </option>
  <option value="612"> 612M </option>
  <option value="619"> 619M </option>
  <option value="625"> 625M </option>
  <option value="631"> 631M </option>
  <option value="637"> 637M </option>
  <option value="638"> 638M </option>
  <option value="644"> 644M </option>
  <option value="650"> 650M </option>
  <option value="656"> 656M </option>
  <option value="662"> 662M </option>
  <option value="668"> 668M </option>
  <option value="675"> 675M </option>
  <option value="681"> 681M </option>
  <option value="687"> 687M </option>
  <option value="693"> 693M </option>
  <option value="700"> 700M </option>
  <option value="706"> 706M </option>
  <option value="712"> 712M </option>
  <option value="718"> 718M </option>
  <option value="725"> 725M </option>
  <option value="731"> 731M </option>
  <option value="737"> 737M </option>
  <option value="743"> 743M </option>
  <option value="750"> 750M </option>
  <option value="756"> 756M </option>
  <option value="762"> 762M </option>
  <option value="768"> 768M </option>
  <option value="775"> 775M </option>
  <option value="781"> 781M </option>
  <option value="787"> 787M </option>
  <option value="793"> 793M </option>
  <option value="800"> 800M </option>
  <option value="825"> 825M </option>
  </select>
							</div>
						</div>

                                                <div class="cbi-value" id="cbi-cgminer-default-freq">
                                                        <label class="cbi-value-title" for="cbid.cgminer.default.freq">ASIC Voltage</label>
                                                        <div class="cbi-value-field">
                                                                <select id="ant_voltage3" class="cbi-input-text">
  <option value="0"> Use Global </option>
  <option value="255"> lowest </option>
  <option value="245"> 1 </option>
  <option value="235"> 2 </option>
  <option value="225"> 3 </option>
  <option value="215"> 4 </option>
  <option value="205"> 5 </option>
  <option value="195"> 6 </option>
  <option value="185"> 7 </option>
  <option value="175"> 8 </option>
  <option value="165"> 9 </option>
  <option value="155"> 10 </option>
  <option value="145"> 11 </option>
  <option value="135"> 12 </option>
  <option value="125"> 13 (bitmain default) </option>
  <option value="115"> 14 </option>
  <option value="105"> 15 </option>
  <option value="95"> 16 </option>
  <option value="85"> 17 </option>
  <option value="75"> 18 </option>
  <option value="65"> 19 </option>
  <option value="55"> 20 </option>
  <option value="45"> 21 </option>
  <option value="35"> 22 </option>
  <option value="25"> 23 </option>
  <option value="15"> 24 </option>
  <option value="5"> highest </option>
                                                        </select>
                                                        </div>
                                                </div>
												</fieldset>												
												
					</fieldset>
					
					<br />
				</fieldset>
					
				<br />
			</div>
			<div class="cbi-page-actions">
				<input class="cbi-button cbi-button-save right" type="button" onclick="f_submit_miner_conf();" value="Save&Apply" />
				<input class="cbi-button cbi-button-reset right" type="button" onclick="f_get_miner_conf();" value="Reset" />
			</div>
			<div class="clear"></div>
		</div>
	</div>
	<div class="clear"></div>
	<div style="text-align: right; font-size: 80%; bottom: 0; left: 0; height: 1.5em; margin: 0; padding: 5px 0px 2px 8px; width: 97%;">
		<font style="color:#666;">Copyright &copy; 2013-2014, Bitmain Technologies</font>
	</div>
</body>
</html>
EOT


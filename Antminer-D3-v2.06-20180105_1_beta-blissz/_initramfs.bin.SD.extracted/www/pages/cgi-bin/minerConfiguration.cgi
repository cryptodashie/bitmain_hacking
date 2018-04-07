et -x

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
"api-listen" : "true",
"api-network" : "true",
"api-allow" : "W:0/0",
"bitmain-fan-pwm": "50",
"bitmain-fan-mode": "0",
"bitmain-freq": "18:218.75:1106",
"bitmain-voltage": "0725",
"bitmain-freq1": "0",
"bitmain-voltage1": "0",
"bitmain-freq2": "0",
"bitmain-voltage2": "0",
"bitmain-freq3": "0",
"bitmain-voltage3": "0"
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
		for(var i = 0; i < ant_data.pools.length; i++) {
			switch(i) {
			case 0:
				jQuery("#ant_pool1url").val(ant_data.pools[i].url);
				jQuery("#ant_pool1user").val(ant_data.pools[i].user);
				jQuery("#ant_pool1pw").val(ant_data.pools[i].pass);
				break;
			case 1:
				jQuery("#ant_pool2url").val(ant_data.pools[i].url);
				jQuery("#ant_pool2user").val(ant_data.pools[i].user);
				jQuery("#ant_pool2pw").val(ant_data.pools[i].pass);
				break;
			case 2:
				jQuery("#ant_pool3url").val(ant_data.pools[i].url);
				jQuery("#ant_pool3user").val(ant_data.pools[i].user);
				jQuery("#ant_pool3pw").val(ant_data.pools[i].pass);
				break;
			}
		}
		if(ant_data["bitmain-nobeeper"]) {
			document.getElementById("ant_beeper").checked = false;
		} else {
			document.getElementById("ant_beeper").checked = true;
		}
		if(ant_data["bitmain-notempoverctrl"]) {
			document.getElementById("ant_tempoverctrl").checked = false;
		} else {
			document.getElementById("ant_tempoverctrl").checked = true;
		}
		jQuery("#ant_fan_customize_value").val(ant_data["bitmain-fan-pwm"]);
		jQuery("#ant_fan_mode").val(ant_data["bitmain-fan-mode"]);
	}
	catch(err)
	{
		alert('Invalid Miner configuration file. Edit manually or reset to default.');
	}
}
function f_submit_miner_conf() {
	_ant_freq = "18:218.75:1106";
	_ant_voltage = "0725";
	_ant_freq1 = "0";
	_ant_voltage1 = "0";
	_ant_freq2 = "0";
	_ant_voltage2 = "0";
	_ant_freq3 = "0";
	_ant_voltage3 = "0";
        _ant_fan_mode = "0";
        _ant_fan_customize_value = "50";
	try
	{

		if(ant_data["bitmain-reboot"]) {                                                           
                        _ant_reboot_switch = "true";                                                                              
                } else {                                                                                     
                        _ant_reboot_switch = "false";                                                                                                     
                }  

		if(ant_data["bitmain-reboot-asic"]) {                                                           
                        _ant_reboot_switch_asic = "true";                                                                              
                } else {                                                                                     
                        _ant_reboot_switch_asic = "false";                                                                                                     
                }
				
		_ant_freq = ant_data["bitmain-freq"];
		_ant_voltage = ant_data["bitmain-voltage"];
		_ant_freq1 = ant_data["bitmain-freq1"];
		_ant_voltage1 = ant_data["bitmain-voltage1"];
		_ant_freq2 = ant_data["bitmain-freq2"];
		_ant_voltage2 = ant_data["bitmain-voltage2"];
		_ant_freq3 = ant_data["bitmain-freq3"];
		_ant_voltage3 = ant_data["bitmain-voltage3"];
	}
	catch(err)
	{
		alert('Invalid Miner configuration file. Edit manually or reset to default.');
	}
	
	_ant_pool1url = jQuery("#ant_pool1url").val();
	_ant_pool1user = jQuery("#ant_pool1user").val();
	_ant_pool1pw = jQuery("#ant_pool1pw").val();
	_ant_pool2url = jQuery("#ant_pool2url").val();
	_ant_pool2user = jQuery("#ant_pool2user").val();
	_ant_pool2pw = jQuery("#ant_pool2pw").val();
	_ant_pool3url = jQuery("#ant_pool3url").val();
	_ant_pool3user = jQuery("#ant_pool3user").val();
	_ant_pool3pw = jQuery("#ant_pool3pw").val();
	_ant_nobeeper = "false";
	_ant_notempoverctrl = "false";
	_ant_fan_customize_value = jQuery("#ant_fan_customize_value").val();
        _ant_fan_mode = jQuery("#ant_fan_mode").val();
	
	if(document.getElementById("ant_beeper").checked) {
		_ant_nobeeper = "false";
	} else {
		_ant_nobeeper = "true";
	}
	if(document.getElementById("ant_tempoverctrl").checked) {
		_ant_notempoverctrl = "false";
	} else {
		_ant_notempoverctrl = "true";
	}

	jQuery("#cbi_apply_bmminer_fieldset").show();
	
	jQuery.ajax({
		url: '/cgi-bin/set_miner_conf.cgi',
		type: 'POST',
		dataType: 'json',
		timeout: 30000,
		cache: false,
		data: {_ant_pool1url:_ant_pool1url, _ant_pool1user:_ant_pool1user, _ant_pool1pw:_ant_pool1pw,_ant_pool2url:_ant_pool2url, _ant_pool2user:_ant_pool2user, _ant_pool2pw:_ant_pool2pw,_ant_pool3url:_ant_pool3url, _ant_pool3user:_ant_pool3user, _ant_pool3pw:_ant_pool3pw, _ant_nobeeper:_ant_nobeeper, _ant_notempoverctrl:_ant_notempoverctrl, _ant_fan_mode:_ant_fan_mode, _ant_fan_customize_value:_ant_fan_customize_value, _ant_freq:_ant_freq, _ant_voltage:_ant_voltage, _ant_freq1:_ant_freq1, _ant_voltage1:_ant_voltage1, _ant_freq2:_ant_freq2, _ant_voltage2:_ant_voltage2, _ant_freq3:_ant_freq3, _ant_voltage3:_ant_voltage3, _ant_reboot_switch:_ant_reboot_switch, _ant_reboot_switch_asic:_ant_reboot_switch_asic},
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
						<li class="tabmenu-item-system active"><a href="/cgi-bin/minerConfiguration.cgi">General Settings</a></li>
						<li class="tabmenu-item-system"><a href="/cgi-bin/minerAdvanced.cgi">Advanced Settings</a></li>
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
			<h2 style="padding-bottom:10px;"><a id="content" name="content">Miner General Configuration</a></h2>
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
						<legend>Pool 1</legend>
						<div class="cbi-value" id="cbi-cgminer-default-pool1url">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool1url">URL</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool1url" id="ant_pool1url" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool1user">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool1user">Worker</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool1user" id="ant_pool1user" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool1pw">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool1pw">Password</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool1pw" id="ant_pool1pw" value="" />
							</div>
						</div>
					</fieldset>
					<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Pool 2</legend>
						<div class="cbi-value" id="cbi-cgminer-default-pool2url">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool2url">URL</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool2url" id="ant_pool2url" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool2user">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool2user">Worker</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool2user" id="ant_pool2user" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool2pw">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool2pw">Password</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool2pw" id="ant_pool2pw" value="" />
							</div>
						</div>
					</fieldset>
					<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Pool 3</legend>
						<div class="cbi-value" id="cbi-cgminer-default-pool3url">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool3url">URL</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool3url" id="ant_pool3url" value="" />
							</div>
						</div>
						<div class="cbi-value" id="cbi-cgminer-default-pool3user">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool3user">Worker</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool3user" id="ant_pool3user" value="" />
							</div>
						</div>
						<div class="cbi-value cbi-value-last"
							id="cbi-cgminer-default-pool3pw">
							<label class="cbi-value-title" for="cbid.cgminer.default.pool3pw">Password</label>
							<div class="cbi-value-field">
								<input type="text" class="cbi-input-text" name="cbid.cgminer.default.pool3pw" id="ant_pool3pw" value="" />
							</div>
						</div>
					</fieldset>
					<fieldset class="cbi-section" id="cbi-cgminer-default">
						<legend>Setup</legend>
						<div class="cbi-value" id="beep" style="display:none">
							<label class="cbi-value-title" for="keep">Beeper ringing</label>
							<div class="cbi-value-field">
								<input type="checkbox" name="ant_beeper" id="ant_beeper" checked />
							</div>
						</div>
						<div class="cbi-value" id="temp_over" style="display:none">
							<label class="cbi-value-title" for="keep">Stop running when temprerature is over 80&#8451; </label>
							<div class="cbi-value-field">
								<input type="checkbox" name="ant_tempoverctrl" id="ant_tempoverctrl" checked />
							</div>
						</div>

                                                <div class="cbi-value" id="fan_ctrl">
                                                        <label class="cbi-value-title" for="keep">FAN Mode</label>
                                                        <div class="cbi-value-field">
                                                                <select id="ant_fan_mode" class="cbi-input-text">
  <option value="0"> AUTO default </option>
  <option value="1"> AUTO silent </option>
  <option value="2"> AUTO performance </option>
  <option value="3"> Manual mode </option>
                                                        </select>
                                                        </div>
                                                </div>

                                                <div class="cbi-value" id="fan_ctrl">
                                                        <label class="cbi-value-title" for="keep">Manual mode fan speed percentage</label>
                                                        <div class="cbi-value-field">
								<input type="text" class="cbi-input-text" style="width:30px;" name="ant_fan_customize_box" id="ant_fan_customize_value" value="" />%
                                                        </div>
                                                </div>

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


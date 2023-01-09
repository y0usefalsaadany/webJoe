<?php
$banner = " 

╱╱╱╱╱╱╭╮╱╭╮╱╱╱╱╱╱╱╱╱╭╮
╱╱╱╱╱╭╯╰╮┃┃╱╱╱╱╱╱╱╱╭╯╰╮
╭━━┳━┻╮╭╯┃┃╭━━┳━━┳━┻╮╭╋┳━━┳━╮
┃╭╮┃┃━┫┃╱┃┃┃╭╮┃╭━┫╭╮┃┃┣┫╭╮┃╭╮╮
┃╰╯┃┃━┫╰╮┃╰┫╰╯┃╰━┫╭╮┃╰┫┃╰╯┃┃┃┃
╰━╮┣━━┻━╯╰━┻━━┻━━┻╯╰┻━┻┻━━┻╯╰╯
╭━╯┃
╰━━╯
";
$content = "
------------------------------------------------
[+] find location any person using ip address
[+] find city name any person using ip address
[+] find country name any person using ip address
------------------------------------------------
";
echo $banner . "\n";
echo $content;
$ip = readline("Enter Ip Address : \n");

if(!empty($ip)){
$api = 'https://freegeoip.app/json/'.$ip;  
$ch = curl_init($api);  
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 
$response = curl_exec($ch); 
curl_close($ch); 
$data = json_decode($response, true); 
 

	if(!empty($data)){ 
    	$country_code = $data['country_code']; 
   	 $country_name = $data['country_name']; 
  	  $region_code = $data['region_code']; 
 	   $region_name = $data['region_name']; 
 	   $city = $data['city']; 
   	 $zip_code = $data['zip_code']; 
  	  $latitude = $data['latitude']; 
  	  $longitude = $data['longitude']; 
  	  $time_zone = $data['time_zone']; 
        echo "------------------------------------------------\n";
   	 echo "[info] Country Name: ".$country_name."\r\n"; 
    	echo '[info] Country Code: '.$country_code."\r\n"; 
  	  echo '[info] Region Code: '.$region_code."\r\n"; 
   	 echo '[info] Region Name: '.$region_name."\n";
  	  echo '[info] City: '.$city."\r\n"; 
    	echo '[info] Zipcode: '.$zip_code."\r\n"; 
 	   echo '[info] Latitude: '.$latitude."\r\n"; 
  	  echo '[info] Longitude: '.$longitude."\r\n"; 
 	   echo '[info] Time Zone: '.$time_zone."\r\n"; 
 	   echo "------------------------------------------------\n";
	}else{ 
   	 echo "IP is not correct!\n";
	} 
 }else{
 	echo "please enter ip \n ";
 }
?>

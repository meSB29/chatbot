#API Key: wze1ztgd9s 
from nltk.chat.util import Chat, reflections
import random
import urllib.request
import re
import json
data="" 


def name(tname):  #Get train number using  name
    with urllib.request.urlopen('https://api.railwayapi.com/v2/name-number/train/{0}/apikey/wze1ztgd9s/'.format(tname)) as response:
        html = response.read()
        data = json.loads(html)
    s=""
    s=data['train']['number']

    return s
def live(number,date):          #live train status  
     with urllib.request.urlopen('https://api.railwayapi.com/v2/live/train/{0}/date/{1}/apikey/wze1ztgd9s/'.format(number,date)) as response:
        html = response.read()
        data = json.loads(html)
        return data
def pnr(number):  #Get PNR status details 
    with urllib.request.urlopen('https://api.railwayapi.com/v2/pnr-status/pnr/{0}/apikey/wze1ztgd9s/'.format(number)) as response:
        html = response.read()
        data = json.loads(html)
        return data
def status(number):  #get status about trains route
    with urllib.request.urlopen('https://api.railwayapi.com/v2/route/train/{0}/apikey/wze1ztgd9s/'.format(number)) as response:
        html = response.read()
        data = json.loads(html)
        return data
def seat_avail(tnumber,stn_code,dst_code,date,clas='3A',quota='GN'):  #Get train seat availability 
    with urllib.request.urlopen('https://api.railwayapi.com/v2/check-seat/train/{0}/source/{1}/dest/{2}/date/{3}/pref/{4}/quota/{5}/apikey/wze1ztgd9s/'.format(tnumber,stn_code,dst_code,date,clas,quota)) as response:
        html = response.read()
        data = json.loads(html)
        return data
    

rules={}

def respond(message):
    rules={'hi':["Hello","Hi","Hey","Namaste"]}
    s1=re.match(r'hi|[hH][eE][lL]+[oO]+',message)
    if s1:
        return random.choice(rules['hi'] )
    s2=re.match(r'(.*)number(.*)train(.*)',message)
    if s2:
        l=list(message.split())
        for i in range(len(l)):
            if (l[i]=='train'):
                i=i+1
                s=name(l[i])
                return s
    s3=re.match(r'(.*)train(.*)number(.*)[0-9][0-9][0-9][0-9][0-9](.*)(date)?(.*)[0-9][0-9](.*)[0-9][0-9](.*)[0-9][0-9][0-9][0-9](.*)',message)
    if s3:
        s31=re.findall(r'[0-9][0-9][0-9][0-9][0-9]',message)
        s32=re.findall(r'[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]',message)
        print(s31)
        print(s32)
        t=live(s31,s32)
        return t
    s4=re.match(r'(.*)[pP][nN][rR](.*)[0-9]*(.*)',message)
    if s4:
        s41=re.findall(r'[0-9]*',message)
        t=pnr(s41)
        return t
    s5=re.match(r'(.*)train(.*)route(.*)[0-9][0-9][0-9][0-9][0-9](.*)|route(.*)train(.*)[0-9][0-9][0-9][0-9][0-9](.*)',message)
    if s5:
        s51=re.findall(r'[0-9]',message)
        t=status(s51)
        return t
    s6=re.match(r'(.*)seats?(.*)avail(.*)',message)
    if s6 :
        s61=re.findall(r'[0-9][0-9][0-9][0-9][0-9]',message)
        s62=re.findall(r'[0-9][0-9][-][0-9][0-9][-][0-9][0-9][0-9][0-9]',message)
        s63=re.findall(r'GN|LD|HO|DF|PH|FT|DP|CK|SS|HP|RE|GNRS|OS|PQ|RC(RAC)?|RS|YU|LB',message)
        s64=re.findall(r'1A|2A|3A|FC|CC|SL|2S',message)
        s65=re.findall(r'[A-Z]+',message)
        print(s61)
        print(s62)
        print(s63)
        print(s64)
        print(s65)
        t=seat_avail(s61,s65[0],s65[1],s62,s64,s63)
        return t





def hugot_bot():
    print("Hello,I'm Jarvis......How may I help you?")
    message=""
    while message!="bye!":
        print(">")
        message=input()
        response=respond(message)
        print(response)
    #chat = Chat(pairs, reflections)
    #chat.converse()

if __name__ == "__main__":
    hugot_bot()

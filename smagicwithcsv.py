import requests
import json
import random
import csv
with open("Sample.csv",'r') as f:
    cvreader=csv.reader(f)
    message=[]
    email=[]
    phn=[]
    country=[]
    schedule=[]
    for i in cvreader:
        message.append(i[0])
        email.append(i[1])
        phn.append(i[2])
        country.append(i[3])
        schedule.append(i[4])
        for i in message:
            if i=="Message":
                message.remove('Message')
        for i in email:
            if i=="Email":
                email.remove('Email')
        for i in phn:
            if i=="Phone":
                phn.remove('Phone')
        for i in country:
            if i=="Country":
                country.remove('Country')
        for i in schedule:
            if i=="Schedule On":
                schedule.remove('Schedule On')
import smtplib
sender_email="bhargava1k97@gmail.com"
password="lbfgkfispqqdptpz"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)   
print("login")
def sendsms(num,msg):
    url="https://www.fast2sms.com/dev/bulkV2"
    paramse={
        'authorization':'DOQ29AyZcHNMK6LW47vwXb0lSUBpGjYqnt8PE1mhVagxrufzIFYmisB63rJ9bAMNpf8lj1TSDyPog7h2',
        'sender_id':'FTWSMS',
        'variables_values':msg,
        'language':'english',
        'route':'otp',
        'numbers':num
            }
    response=requests.get(url,params=paramse)
    dic=response.json()
    print(response.text)
for i in range(len(email)):
        if email[i].endswith("gmail.com"):
            server.sendmail(sender_email,email[i],message[i])
            print("success ",i)
        else:
            print("Invalid Email",email[i])
        if len(message[i])>1 and len(message[i])<160:
            sendsms(phn[i],message[i])
            print("sms sent ",i)
        else:
            print("Message length should be > 1 and <=160 characters"
        
    
       


  

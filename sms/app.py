from flask import *
from time import strftime as stf

app=Flask(__name__)
app.secret_key="23494"
datetim=stf("%Y-%m-%dT%H:%M")
@app.route("/",methods=['GET','POST'])
def sms():
    if request.method == 'POST':
            import requests
            import smtplib
            sender_email="bhargava1k97@gmail.com"
            password="lbfgkfispqqdptpz"
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender_email,password)
            email=request.form.get('email')
            subject=request.form.get('subject')
            message=request.form.get('message')
            print(len(message))
            phn=request.form.get('phn')
            messagem2=f"Subject:{subject}\n\n{message}"
            url="https://www.fast2sms.com/dev/bulkV2"
            paramse={
                'authorization':'DOQ29AyZcHNMK6LW47vwXb0lSUBpGjYqnt8PE1mhVagxrufzIFYmisB63rJ9bAMNpf8lj1TSDyPog7h2',
                'sender_id':'FTWSMS',
                'variables_values':message,
                'language':'english',
                'route':'otp',
                'numbers':phn
                    }
            if phn!="" and email!="" and len(message)<=160:
                response=requests.get(url,params=paramse)
                dic=response.json() 
                server.sendmail(sender_email,email,messagem2)
                success=f"Message successfully sent to {email} and {phn}"
                print(dic)
                return render_template("sms.html",success=success,datetim=datetim)
            
            elif email!="" and email.endswith('gmail.com'):
                server.sendmail(sender_email,email,messagem2)
                success=f"Message successfully sent to {email}"
                return render_template("sms.html",success=success,datetim=datetim)
            
            elif phn!="" and len(message)<=160:
                response=requests.get(url,params=paramse)
                dic=response.json() 
                success=f"SMS successfully sent to {phn}"
                return render_template("sms.html",success=success,datetim=datetim) 
            else:
                failure="Message not sent"
                fail="1.Message length should be >1 and <=160 characters if it has to be sent as a Text Message"
                fail2="2.Enter valid email if it has to be sent as a Email and Email will not have message length."
                return render_template("sms.html",success=failure,fail=fail2,fail1=fail,
                datetim=datetim)


    return render_template("sms.html",datetim=datetim)

if __name__=="__main__":
    app.run(debug=True)
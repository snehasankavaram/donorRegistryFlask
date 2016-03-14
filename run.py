from flask import Flask, request
from twilio import twiml
from twilio.rest import TwilioRestClient

#TODO: Hardcoding for now, should set environment variables later
TWILIO_ACCOUNT_SID = 'ACef5de209f7326334ef72ee795f479b01'
TWILIO_AUTH_TOKEN = 'ebecd4f0e558d87a7b8133a981187f5b'
TWILIO_NUMBER = '+18504629815'

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
recipients = ['+14088576536'];

app = Flask(__name__)
@app.route('/voice', methods= ['GET', 'POST'])
def voice():
    resp = twiml.Response()
    resp.say("Twilio loves berkeley")
    return str(resp)
    
@app.route('/sms', methods= ['GET', 'POST'])  
def SMS ():
   
    client.messages.create(
        body = request.form.get("message"),
        to =  request.form.get("number"),
        from_ = TWILIO_NUMBER
        )
    return('messages sent')
    

@app.route('/receivesms',  methods= ['GET', 'POST'])
def receivesms():
    body = request.values.get('Body', None)
    
    r = twiml.Response()
    
    msg = str(request.values)
    r.message(msg)
    # if body == 'YES' or body == 'yes':
    #     r.message("cool!")
    # elif body == 'NO' or body == 'no':
    #     r.message("oh alright")
    # else:
    #     r.message("That was an invalid reply")
        
    return str(r)

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 8080)
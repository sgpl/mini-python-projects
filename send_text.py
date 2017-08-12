#!/usr/bin/python 2.7

# Importing Client from twilio.rest
from twilio.rest import Client


account_sid = "INSERT_SID_HERE"
auth_token = "INSERT_AUTH_TOKEN_HERE"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16472675882",
    from_="INSERT_TWILIO_NUMBER",
    body="WOW! This is pretty cool!!!!")

print(message.sid)

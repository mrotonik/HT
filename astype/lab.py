import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid['ACd480cf5dc8fbbfd71945ff0b79a1dcb0'] = os.environ['ACd480cf5dc8fbbfd71945ff0b79a1dcb0']
auth_token = os.environ['7eb4958473d64c8c08515b4c2c80286e']
client = Client(account_sid, auth_token)

keys = client.keys.list(limit=20)

for record in keys:
    print(record.sid)
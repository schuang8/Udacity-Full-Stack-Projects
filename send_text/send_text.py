
from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "ACf43f2c97b97366830b4d2ff334ef4c48"

friendly_name = "key1"
key_type = "Standard"
Secret = "2oBXGFW9WgI6y1SsbNa5u9colRPhZJ2m"
# Your Auth Token from twilio.com/console
auth_token  = "c8ee9a08ec6daf9854a052de7ed79112"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+17033628487", # MY PHONE NUMBER
    from_="+12407021285", # 
    body="Hello from Python!")

print(message.sid)

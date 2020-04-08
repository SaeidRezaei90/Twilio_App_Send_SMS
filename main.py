from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account (look at 'Read Me')
client = Client(account_sid, auth_token)

my_msg = '\n'.join(["Love you... " for i in range(10)])

print(my_msg)

message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)

print(message.sid)
import telegram
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient

APP_NAME = 'testapp'
BOT_NAME = 'sensefilter'
BOT_USERNAME = 'sensefilterBot'
URL = 't.me/sensefilterBot'
API_TOKEN = '475280984:AAG1krvBZHeRr9w_BiyBrxHqodeok3DmI2U'
PHONE = '+13233345384'

API_ID = '14346'
API_HASH = 'f69506de77f52de03eb90181e2646c62'
APP_TITLE = 'testapp'

bot = telegram.Bot(token=API_TOKEN)
print(bot.get_me())


client = TelegramClient('test_session', API_ID, API_HASH)
client.connect()

# If you already have a previous 'session_name.session' file, skip this.
client.sign_in(phone=PHONE)
me = client.sign_in(code=79076)  # Put whatever code you received here.

print(me.stringify())
client.send_message('sensefilter', 'Hello! Talking to you from Telethon')


#client(JoinChannelRequest(channel))
total, messages, senders = client.get_message_history('attractor137')
x = client.download_media(messages[0])
print(x)

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from time import sleep

dialogs = []
users = []
chats = []
messages = []

last_date = None
chunk_size = 200
while True:
    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size
             ))
    dialogs.extend(result.dialogs)
    users.extend(result.users)
    chats.extend(result.chats)
    if not result.messages:
        break
    last_date = min(msg.date for msg in result.messages)
    if result.messages is not None:
    	for msg in result.messages:
    		print(msg.message)
    		messages.extend(msg.message)
    if len(messages) > 1000:
    	break
    sleep(2)



    